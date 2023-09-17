#!/usr/bin/env python3

import argparse
import dis
import os
import random
import traceback
import types

# This script parses the markdown files in /Races, /Classes, and /Backgrounds
# loading the Python code found in each .md file into a script that is then
# dynamically loaded into a module and used as part of the NPC generation
# process. In essence, this is a flavor of "literate programming".

quiet = False
verbose = False
scripted = False
SAVEPY = os.getenv('SAVE_PY')

def error(*values):
    print(*values)

def warn(*values):
    if not quiet:
        print("WARNING: ", end='')
        print(*values)

def log(*values):
    if verbose and not quiet:
        print(*values)

REPOROOT = '../../'

# ----------------------------------------------------------
# Common routines available to all loaded modules
def levelinvoke(module, level, npc):
    def nop(npc): pass

    levelfn = getattr(module, 'level' + str(level), nop)
    levelfn(npc)

global scriptedinput
scriptedinput = []
inputhistory = []
def choose(text, choices):
    """Present a list of choices to the engine for selection"""
    print(text)

    def choosefromlist(choicelist):
        "Present a list of choices interactively"
        choicelist.sort()
        choiceidx = 0
        for c in choicelist:
            choiceidx += 1
            print(f'{choiceidx}: {c}')

        response = None
        while response == None:
            response = input(">>> ")
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choicelist):
                response = None

        response = int(response) - 1 # Account for z'ero-based 'index
        print("You chose " + choicelist[response])
        inputhistory.append(str(response))
        return choices[response]

    def scriptfromlist(choicelist):
        """Accept a scripted choice from a list of choices"""
        choicelist.sort()
        choiceidx = 0
        for c in choicelist:
            choiceidx += 1
            print(f'{choiceidx}: {c}')

        response = scriptedinput.pop(0).strip()
        print(">>> " + str(response))
        if response.isdigit():
            response = int(response)
            return choicelist[response]
        elif response == "random":
            responseidx = random.randrange(0, len(choicelist))
            return choicelist[responseidx]
        else:
            return response

    def choosefrommap(choicemap):
        """Present a map of choices interactively"""
        choiceidx = 0
        for c in choicemap.items():
            choiceidx += 1
            print(f'{choiceidx}: {c[0]} ({c[1]})')

        # Interactive
        response = None
        while response == None:
            response = input(">>> ")
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choicemap):
                response = None

        responseidx = int(response) - 1 # Account for z'ero-based 'index
        responsekey = list(choicemap.keys())[responseidx]
        inputhistory.append(str(responseidx))
        print("You chose " + str((responsekey, choicemap[responsekey])))
        return (responsekey, choicemap[responsekey])

    def scriptfrommap(choicemap):
        """Accept a scripted choice from a map of choices"""
        choiceidx = 0
        for c in choicemap.items():
            choiceidx += 1
            print(f'{choiceidx}: {c[0]} ({c[1]})')

        response = scriptedinput.pop(0).strip()
        print(">>> " + str(response))
        if response.isdigit():
            responseidx = int(response) - 1
            responsekey = list(choicemap.keys())[responseidx]
            result = (responsekey, choicemap[responsekey])
            return result
        elif response == "random":
            responseidx = random.randrange(0, len(choicemap))
            responsekey = list(choicemap.keys())[responseidx]
            result = (responsekey, choicemap[responsekey])
            return result
        else:
            return (response, choicemap[response])
        
    def chooseopen():
        """Accept open-ended input interactively"""
        response = None
        while response == None:
            response = input(">>> ")
            if len(response.strip()) > 0:
                return response

    def scriptedopen():
        """Accept scripted open-ended input"""
        response = scriptedinput.pop(0).strip()
        print(">>> " + str(response))
        return response

    if len(choices) == 0 and len(scriptedinput) == 0: return chooseopen()
    elif len(choices) == 0 and len(scriptedinput) > 0: return scriptedopen()
    elif isinstance(choices, list) and len(scriptedinput) == 0: return choosefromlist(choices)
    elif isinstance(choices, dict) and len(scriptedinput) == 0: return choosefrommap(choices)
    elif isinstance(choices, list) and len(scriptedinput) > 0: return scriptfromlist(choices)
    elif isinstance(choices, dict) and len(scriptedinput) > 0: return scriptfrommap(choices)
    else:
        raise BaseException('Unrecognized type of choices: ' + str(type(choices)))

def spelllinkify(name):
    linkdest = name.replace(' ','-')
    return f"[{name}](http://azgaarnoth.tedneward.com/magic/spells/{linkdest}/)"

def replace(text, list, newtext):
    for it in list:
        if it[0:len(text)] == text:
            list.remove(it)
    list.append(text + " " + newtext)

def randomlist(listofchoices):
    return listofchoices[random.randint(0, len(listofchoices)-1)]

def dieroll(dpattern):
    (number, size) = dpattern.split("d")
    accum = 0
    for _ in range(int(number)):
        accum += random.randint(1, int(size))
    return accum

def choosefeat(npc):
    choices = {}
    for (featname, featmod) in feats.items():
        print(f"Examining {featmod}")
        if featmod.prereq == None or featmod.prereq(npc):
            choices[featname] = featmod
    (_, chosenfeatmod) = choose("Choose a feat: ", choices)
    chosenfeatmod.apply(npc)

def chooseskill(npc, skills = None):
    skilllist = None
    if skills != None:
        skilllist = skills.copy()
    else:
        skilllist = [ 'Acrobatics', 'Animal Handling', 'Arcana','Athletics',
            'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
            'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
            'Religion', 'Sleight of Hand', 'Stealth', 'Survival']
    
    for sk in npc.skills:
        skilllist.remove(sk)

    npc.skills.append(choose("Choose a skill:", skilllist))

def abilityscoreimprovement(npc):
    asiorfeat = choose("Ability Score Improvement, or Feat?", ['Ability', 'Feat'])
    if asiorfeat == 'Ability':
        for _ in range(0,2):
            abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
            ability = choose("Choose an ability to improve: ", abilities)
            if ability == 'STR': npc.STR += 1
            elif ability == 'DEX': npc.DEX += 1
            elif ability == 'CON': npc.CON += 1
            elif ability == 'INT': npc.INT += 1
            elif ability == 'WIS': npc.WIS += 1
            elif ability == 'CHA': npc.CHA += 1
    else:
        choosefeat(npc)

traits = {
    'amphibious' : "***Amphibious.*** You can breathe air and water.",
    'fey-ancestry' : "***Fey Ancestry.*** You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
    'powerful-build': "***Powerful Build.*** You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
    'sea-emissary' : "***Emissary of the Sea.*** You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.",
    'sunlight-sensitivity' : "***Sunlight Sensitivity.*** You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.",
}

weapons = {
    'Longsword': ['1d8', 'slashing', ['versatile (1d10)']],
    'Battleaxe': ['1d8', 'slashing', ['versatile (1d10)']],
    'Flail': ['1d8', 'bludgeoning', []],
    'Glaive': ['1d10', 'slashing', ['heavy', 'reach', 'two-handed']],
    'Greataxe': ['1d12', 'slashing', ['heavy', 'two-handed']],
    'Greatsword': ['2d6', 'slashing', ['heavy', 'two-handed']],
    'Halberd': ['1d10', 'slashing', ['heavy', 'reach', 'two-handed']],
    'Lance': ['1d12', 'piercing', ['reach', 'special']],
    'Maul': ['2d6', 'bludgeoning', ['heavy', 'two-handed']],
    'Morningstar': ['1d8', 'piercing', []],
    'Pike': ['1d10', 'piercing', ['heavy', 'reach', 'two-handed']],
    'Rapier': ['1d8', 'piercing', ['finesse']],
    'Scimitar': ['1d6', 'slashing', ['finesse', 'light']],
    'Shortsword': ['1d6', 'piercing', ['finesse', 'light']],
    'Trident': ['1d6', 'piercing', ['thrown (range 20/60)', 'versatile (1d8)']],
    'War pick': ['1d8', 'piercing', []],
    'Warhammer': ['1d8', 'bludgeoning', ['versatile (1d10)']],
    'Whip': ['1d4', 'slashing', ['finesse', 'reach']],
    'Club': ['1d4', 'bludgeoning', ['Light']],
    'Dagger': ['1d4', 'piercing', ['finesse', 'light', 'thrown (range 20/60)']],
    'Greatclub': ['1d8', 'bludgeoning', ['two-handed']],
    'Handaxe': ['1d6', 'slashing', ['Light', 'thrown (range 20/60)']],
    'Javelin': ['1d6', 'piercing', ['thrown (range 30/120)']],
    'Light hammer': ['1d4' 'bludgeoning', ['Light', 'thrown (range 20/60)']],
    'Mace': ['1d6', 'bludgeoning', []],
    'Quarterstaff': ['1d6', 'bludgeoning', ['versatile (1d8)']],
    'Sickle': ['1d4', 'slashing', ['light']],
    'Spear': ['1d6', 'piercing',	['thrown (range 20/60)', 'versatile (1d8)']],
    'Light Crossbow': ['1d8', 'piercing', ['ammunition (range 80/320)', 'loading', 'two-handed']],
    'Dart': ['1d4' 'piercing', ['finesse', 'thrown (range 20/60)']],
    'Shortbow': ['1d6', 'piercing', ['ammunition (range 80/320)', 'two-handed']],
    'Sling': ['1d4' 'bludgeoning',	['ammunition (range 30/120)']],
    'Blowgun': ['1' 'piercing', ['ammunition (range 25/100)', 'loading']],
    'Hand Crossbow': ['1d6', 'piercing', ['ammunition (range 30/120)', 'light', 'loading']],
    'Heavy Crossbow': ['1d10', 'piercing', ['ammunition (range 100/400)', 'heavy', 'loading', 'two-handed']],
    'Longbow': ['1d8', 'piercing', ['ammunition (range 150/600)', 'heavy', 'two-handed']],
    'Net': ['-', 'special', ['thrown (range 5/15)']]
}



# ------------------------------------
# Module management
def ismdfile(filepath): 
    if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.md': return True
    else: return False

def loadmodule(filename, modulename=None):
    def parsemd(mdfilename):
        pythoncode = ""
        with open(mdfilename) as mdfile:
            lines = mdfile.readlines()
            codeblock = False
            for line in lines:
                if line[0:3] == "```":
                    codeblock = not codeblock
                    continue

                if codeblock == True:
                    pythoncode += line

        if SAVEPY != None and SAVEPY in mdfilename:
            with open('./Python/' + os.path.basename(mdfilename) + '.py', 'w') as pyfile:
                pyfile.write(pythoncode)
        return pythoncode

    def builddict(module):
        global classes
        global races
        builtins = {
            "allclasses": classes,
            "allraces": races,
            "feats": feats,
            "traits": traits,
            "spelllinkify": spelllinkify,
            "choose": choose,
            "choosefeat":choosefeat,
            "chooseskill": chooseskill,
            "replace": replace,
            "random": randomlist,
            "dieroll": dieroll,
            "abilityscoreimprovement": abilityscoreimprovement,
            "min": min,
            "len": len,
            "print": print,
            "types": types,
            "loadmodule": loadmodule
        }
        for (key, value) in builtins.items():
            module.__dict__[key] = value

    literatecode = parsemd(filename)
    if len(literatecode) > 0:
        if verbose: print(literatecode)
        if modulename == None:
            modulename = os.path.splitext(os.path.basename(filename))[0]
        module = types.ModuleType(modulename)
        builddict(module)
        exec(literatecode, module.__dict__)
        return module
    else:
        warn(f"{filename} has no literate code")
        return None

# We expect race modules to contain the following 'top-level 'symbols:
# Mandatory:
#   name : string
#   level0(npc) : function
#   subraces : map<string, dict(name, levelX functions)>
# Optional:
#   levelX(npc) : function
#   generate_name(npc, 'male'|'female') : function
#   height(npc) : function
#   weight(npc) : function
races = {}
def loadraces():
    racesroot = REPOROOT + 'Races'
    entries = os.listdir(racesroot)
    for f in entries:
        if f == 'index.md': continue

        entryname = racesroot + "/" + f

        # Load subraces if they are present
        if os.path.isdir(entryname):
            dirpath = entryname
            dirname = os.path.basename(dirpath)
            basemodule = loadmodule(dirpath + "/index.md", dirname)
            if basemodule != None:
                subraces = {}
                for sf in os.listdir(dirpath):
                    if ismdfile(dirpath + "/" + sf) and sf != "index.md":
                        log(f"Parsing {sf}...")
                        subracename = os.path.splitext(sf)[0]
                        subracemod = loadmodule(dirpath + '/' + sf, basemodule.name + "-" + subracename)
                        subraces[subracename] = subracemod
                setattr(basemodule, "subraces", subraces)
            if basemodule != None:
                races[basemodule.name] = basemodule

        # Load just the base race since there's no subraces
        elif ismdfile(entryname):
            log(f"Parsing {entryname}...")
            module = loadmodule(entryname)
            if module != None:
                races[module.name] = module

# We expect class modules to contain the following 'top-level 'symbols:
# name : string
# levelX(npc) : functions invoked at each level in that class
# preferredstats() : function returning (in order) the stats preferred
# subclasses: map<string, dict(name, levelX functions)>
classes = {}
def loadclasses():
    classesroot = REPOROOT + 'Classes'
    entries = os.listdir(classesroot)
    for f in entries:
        entryname = classesroot + "/" + f

        excludedentries = [ 'Prestige' ]

        # Load class and subclasses
        if os.path.isdir(entryname) and (os.path.basename(entryname) not in excludedentries):
            dirpath = entryname
            dirname = os.path.basename(dirpath)
            basemodule = loadmodule(dirpath + "/index.md", dirname)
            if basemodule != None:
                classes[basemodule.name] = basemodule

                dependentmods = []
                if getattr(basemodule, "dependentmodules", None) != None:
                    dependentmods = basemodule.dependentmodules
                    for depname in dependentmods:
                        loadmodule(dirpath + "/" + depname, basemodule.name + "-" + depname)

                log("Parsing subclasses")
                subclasses = {}
                excludedmds = [ 'index.md', 'SpellList.md' ] + dependentmods
                log("Ignoring " + str(excludedmds))
                for sf in os.listdir(dirpath):
                    if ismdfile(dirpath + "/" + sf) and (sf not in excludedmds):
                        log(f"Parsing {sf}...")
                        subclassname = os.path.splitext(sf)[0]
                        subclassmod = loadmodule(dirpath + '/' + sf, basemodule.name + "-" + subclassname)
                        if subclassmod != None: 
                            setattr(subclassmod, "baseclass", basemodule)
                        subclasses[subclassname] = subclassmod
                setattr(basemodule, "subclasses", subclasses)

# Backgrounds....
#backgrounds = {}
#def loadbackgrounds():
#    backgroundsroot = os.listdir(REPOROOT + 'Cultures/Backgrounds')
#    entries = os.listdir(backgroundsroot)
#    for f in entries:
#        entry = backgroundsroot + "/" + f
#
#        excludedentries = [ 'index.md' ]
#        
#        # Load class and subclasses
#        if (ismdfile(entry) and os.path.basename(entry) not in excludedentries):
#            log(f"Parsing Feat {entry}...")
#            bgmodule = loadmodule(entry, os.path.basename(entry))
#            if bgmodule != None:
#                backgrounds[bgmodule.name] = bgmodule

# Feats....
# name : string
# prereq : fn to determine if npc meets the *Prerequisite* criteria for the feat
# apply : fn to apply the feat to the npc
feats = {}
def loadfeats():
    featsroot = REPOROOT + 'Feats'
    entries = os.listdir(featsroot)
    for f in entries:
        entry = featsroot + "/" + f

        excludedentries = [ 'index.md' ]
        
        # Load class and subclasses
        if (ismdfile(entry) and os.path.basename(entry) not in excludedentries):
            log(f"Parsing Feat {entry}...")
            featmodule = loadmodule(entry, os.path.basename(entry))
            if featmodule != None:
                feats[featmodule.name] = featmodule


class NPC:
    class Spellcasting:
        def __init__(self, npc, ability):
            self.npc = npc
            # Caster class is the base class for this Spellcasting trait.
            # It can be None, which means there is no base class (typically for Innate casters)
            self.casterclass = None
            # INT, WIS, or CHA
            self.ability = ability
            # INTbonus(), WISbonus(), or CHAbonus()
            self.abilitybonus = None
            self.maxcantripsknown = 0
            self.cantripsknown = []
            self.maxspellsknown = 0
            self.spellsprepared = 0
            self.spellsalwaysprepared = []
            self.spells = { 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [] }

            # This is a dict of level-to-list describing the slots at each level (offset by 1, of course....)
            self.slottable = {}
            # This is for the spellcasting that isn't level-based (e.g., Innate casting)
            self.slots = []

        def __str__(self):
            return f"{self.casterclass} / {self.npc.levels(self.casterclass)} / {self.ability} / {self.spells} / {self.slottable}"

        def casterlevel(self):
            if self.casterclass == None: return 0
            else: return self.npc.levels(self.casterclass)

        def spellsavedc(self):
            return 8 + self.npc.proficiencybonus() + (self.npc.abilitybonus(self.ability))

        def spellattack(self):
            return self.npc.proficiencybonus() + (self.npc.abilitybonus(self.ability))

    def __init__(self):
        self.description = []

        self.size = 'Medium'
        self.type = ''
        self.gender = ''

        # Race is a dict ('name', 'type', ...) for the race selected
        self.race = None
        # Subrace is a dict ('name', 'levelX', ...) for the subrace selected
        self.subrace = None
        # Classes is a list of the class-dicts for each class taken
        # e.g, '[<fighter>,<fighter>,<monk>,<monk>,<fighter>] for a Fighter 3/Monk 2 NPC
        self.classes = []
        # Subclasses is a map of the classmodule.name : subclassmodule
        # e.g, '{'Fighter':<samurai>,'Wizard':<necromancer>}
        self.subclasses = {}

        # Armorclass is a dict of 'type'-to-value pairs; e.g., 'shield' : 2, 'breastplate' : 15, etc
        # This is so that we can put the descriptors into parens after the total value
        self.armorclass = { }

        self.hitpoints = 0
        self.hitdice = { 'd6':0, 'd8':0, 'd10':0, 'd12':0, 'd20':0 }
        self.hpconbonus = 0

        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0

        self.speed = { 'walking': 0 }
        self.senses = { 'passive Perception': 0 }
        self.savingthrows = []
        self.damagevulnerabilities = []
        self.damageresistances = []
        self.damageimmunities = []
        self.conditionimmunities = []

        # Proficiencies are for weapons and armor only; everything else is a skill
        # TODO: It sounds like 5e holds the idea that skills are just proficiencies,
        # so maybe unify these two at some point in the future. Ditto for langs?
        self.proficiencies = []
        self.skills = []

        # Languages are read/write/speak
        self.languages = []

        # Traits are anything that isn't an action, bonus action, reaction, ...
        self.traits = []
        self.actions = []
        self.bonusactions = []
        self.reactions = []

        self.equipment = []

        # Spellcasting data; each is a hash tied to the name of the class (or race, if 
        # it's Innate) whose spellcasting this is (Cleric, Wizard, Rogue (for Arcane 
        # Trickster), Fighter (for Eldritch Knight), etc)
        self.spellcasting = { }

        # Normalizers are fns run when the NPC is frozen;
        # usually these are level-dependent text/traits/features/etc
        self.normalizers = []
        self.deferred = {}

    def defer(self, fn):
        """Defer fn to be invoked when the NPC is normalized/frozen"""
        self.normalizers.append(fn)

    def STRbonus(self): return (self.STR // 2) - 5
    def DEXbonus(self): return (self.DEX // 2) - 5
    def CONbonus(self): return (self.CON // 2) - 5
    def INTbonus(self): return (self.INT // 2) - 5
    def WISbonus(self): return (self.WIS // 2) - 5
    def CHAbonus(self): return (self.CHA // 2) - 5
    def abilitybonus(self, ability):
        match ability:
            case 'STR': return self.STRbonus()
            case 'DEX': return self.DEXbonus()
            case 'CON': return self.CONbonus()
            case 'INT': return self.INTbonus()
            case 'WIS': return self.WISbonus()
            case 'CHA': return self.CHAbonus()
            case _ : return None

    def proficiencybonus(self):
        return (self.levels() // 4) + 2

    def levels(self, clss = None):
        if clss == None:
            return len(self.classes)
        else:
            count = 0
            if type(clss) is str:
                for cli in self.classes:
                    if cli.name == clss: count += 1
            else:
                for cli in self.classes: 
                    if cli == clss: count += 1
            return count

    def classmodulefor(self, name):
        classobjs = list(filter(lambda c: c.name == name, self.classes))
        if len(classobjs) > 0:
            return classobjs[0]
        else:
            return None

    def hits(self, die):
        """Generate the hit points gained at the current level, using the die specified."""
        self.hitdice[die] += 1
        if self.levels() == 1:
            # Max hit points at first level
            self.hitpoints += int(die[1:]) # Strip off the 'd'
        else:
            # We roll randomly (sort of)
            top = int(die[1:])
            self.hitpoints += random.randrange(4, top)
        # Keep a running total for the CON bonus, since it can change over time/levels
        self.hpconbonus += self.CONbonus()
        # Likewise, keep a running total for hit points
        self.hitpoints += self.CONbonus()

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)
    
    def skillchoice(self):
        skilllist = [ 'Acrobatics', 'Animal Handling', 'Arcana','Athletics',
            'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
            'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
            'Religion', 'Sleight of Hand', 'Stealth', 'Survival']
        
        for sk in self.skills:
            skilllist.remove(sk)

        self.skills.append(choose("Choose a skill:", skilllist))

    def newspellcasting(self, source, ability):
        """Convenience factory method to be used from literate Race/Class/Background/Feats"""
        spellcasting = NPC.Spellcasting(self, ability)
        self.spellcasting[source] = spellcasting
        spellcasting.abilitybonus = self.INTbonus if ability == 'INT' else self.WISbonus if ability == 'WIS' else self.CHAbonus if ability == 'CHA' else None
        return spellcasting

    def freeze(self):
        """The NPC is finished building, so normalize any traits/features to this level."""
        for dfn in self.normalizers:
            dfn(self)

        # Let's see if there's any duplicate skills or other things
        skilllist = []
        for skill in self.skills:
            if skill in skilllist:
                warn("Duplicated skill: " + skill)
            else:
                skilllist.append(skill)
        self.skills = skilllist

        proflist = []
        for prof in self.proficiencies:
            if prof in proflist:
                warn("Duplicated proficiency: " + prof)
            else:
                proflist.append(prof)
        self.proficiencies = proflist

        damagetypes = [ 
            'acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning', 'necrotic', 
            'piercing', 'poison', 'psychic', 'radiant', 'slashing', 'thunder'            
        ]
        def verifytypes(list):
            for entry in list:
                if entry not in damagetypes:
                    warn("Unrecognized energy type: " + entry)
        verifytypes(self.damageimmunities)
        verifytypes(self.damageresistances)
        verifytypes(self.damagevulnerabilities)

    def getsavingthrows(self):
        results = []
        for st in self.savingthrows:
            results.append(f"{st.title()} +{self.proficiencybonus() + (getattr(self, st + 'bonus', None))()}")
        return ",".join(results)

    def getskills(self):
        skillmap = {
            'Acrobatics' : 'DEX', 
            'Animal Handling' : 'WIS', 
            'Arcana' : 'INT',
            'Athletics' : 'STR',
            'Deception' : 'CHA', 
            'History' : 'INT',
            'Insight' : 'WIS',
            'Intimidation' : 'CHA',
            'Investigation' : 'INT',
            'Medicine' : 'WIS',
            'Nature' : 'INT',
            'Perception' : 'WIS',
            'Performance' : 'CHA', 
            'Persuasion' : 'CHA',
            'Religion' : 'INT', 
            'Sleight of Hand' : 'DEX', 
            'Stealth' : 'DEX', 
            'Survival' : 'WIS'
        }
        def mapskill(skill):
            return f"{skill} +{(getattr(self, str(skillmap[skill]) + 'bonus', None)()) + self.proficiencybonus()}"
        return ", ".join(map(mapskill, self.skills))
 
    def emitMD(self):
        def getarmorclass():
            result = []
            ac = 10
            for (actext, acnum) in self.armorclass.items():
                if acnum > 8:
                    # Only armor itself is ever a value 10+
                    ac = acnum
                    result.append(f'{actext} ({acnum})')
                else:
                    ac += acnum
                    result.append(f'{actext} (+{acnum})')
            ac += self.DEXbonus()
            result.append(f'DEX ({self.DEXbonus():+g})')
            return str(ac) + ' (' + ",".join(result) + ')'
        
        def getspeed():
            text = str(self.speed['walking']) + ' ft'
            for (key, value) in self.speed.items():
                if key == 'walking': continue
                else:
                    text += ", " + key + " " + str(value) + " ft"
            return text
                       
        def getsenses():
            perception = f"passive Perception {10 + self.WISbonus() + (self.proficiencybonus() if 'Perception' in self.skills else 0)}"
            if len(self.senses) == 1:
                return perception
            else:
                text = ""
                for (key, value) in self.senses.items():
                    if key == 'passive Perception': continue
                    else:
                        text += f"{key} {value} ft, "
                return text + perception
        
        def getracesubstring():
            return f"{self.race.type} ({'' if self.subrace == None else self.subrace.name + ' '}{self.race.name})"
        
        def getclasssubstring():
            classmap = {}
            for c in self.classes:
                if c not in classmap:
                    classmap[c] = 1
                else:
                    classmap[c] += 1

            strs = []
            for c in classmap:
                if c in self.subclasses.keys():
                    strs.append(f"{c.name} ({self.subclasses[c].name}) {classmap[c]}")
                else:
                    strs.append(f"{c.name} {classmap[c]}")
            return "/".join(strs)

        linesep = ">___\n"

        result  =  ">### Name\n"
        result += f'*{self.size} {self.gender} {getracesubstring()} {getclasssubstring()}, any alignment*\n'
        result += linesep
        result += f">- **Armor Class** {getarmorclass()}\n"
        result += f">- **Hit Points** {self.hitpoints} ({self.hitdicedesc()} + {self.hpconbonus})\n"
        result += f">- **Speed** {getspeed()}\n"
        result += linesep
        result +=  ">|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|\n"
        result +=  ">|:-:|:-:|:-:|:-:|:-:|:-:|\n"
        result += f">|{self.STR} ({self.STRbonus():+g})"
        result += f"|{self.DEX} ({self.DEXbonus():+g})"
        result += f"|{self.CON} ({self.CONbonus():+g})"
        result += f"|{self.INT} ({self.INTbonus():+g})"
        result += f"|{self.WIS} ({self.WISbonus():+g})"
        result += f"|{self.CHA} ({self.CHAbonus():+g})|\n"
        result += linesep
        result += f">- **Proficiency Bonus** {self.proficiencybonus():+g}\n"
        result += f">- **Saving Throws** {self.getsavingthrows()}\n"
        result += f">- **Damage Vulnerabilities** {','.join(self.damagevulnerabilities)}\n"
        result += f">- **Damage Resistances** {','.join(self.damageresistances)}\n"
        result += f">- **Damage Immunities** {','.join(self.damageimmunities)}\n"
        result += f">- **Condition Immunities** {','.join(self.conditionimmunities)}\n"
        result += f">- **Skills** {self.getskills()}\n"
        result += f">- **Proficiencies** {','.join(self.proficiencies)}\n"
        result += f">- **Senses** {getsenses()}\n"
        result += f">- **Languages** {','.join(self.languages)}\n"
        result += linesep
        for trait in self.traits:
            result += f">{trait}\n"
            result +=  ">\n"
        result +=  ">#### Actions\n"
        for action in self.actions:
            result += f">{action}\n"
            result +=  ">\n"

        #Spellcasting is an action most of the time, so....
        advlevel = [ '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th']
        if len(self.spellcasting.keys()) > 0:
            for (source, details) in self.spellcasting.items():
                casterlevel = ''
                if details.casterlevel() > 0:
                    casterlevel = ", at level " + str(details.casterlevel())
                text = f">***{source} Spellcasting ({details.ability.title()}{casterlevel}. Recharges on long rest).*** "
                if details.maxcantripsknown > 0:
                    text += f"{details.maxcantripsknown} cantrips known. "
                if details.maxspellsknown > 0:
                    text += f"{details.maxspellsknown} spells known. "
                if details.spellsprepared > 0:
                    text += f"{details.spellsprepared} spells prepared. "
                text += f"Spell save DC: {details.spellsavedc()}, Spell attack bonus: +{details.spellattack()}\n"
                if len(details.spellsalwaysprepared) > 0:
                    text += f">\n>Spells always prepared: {','.join(map(lambda c: spelllinkify(c),details.spellsalwaysprepared))}\n"
                text +=  ">\n"
                if details.maxcantripsknown > 0 or len(details.cantripsknown):
                    text += ">* *Cantrips:* " + ",".join(map(lambda c: spelllinkify(c),details.cantripsknown)) + "\n"
                if details.casterclass != None:
                    slots = details.slottable[details.casterlevel()]
                    for lvl in range(len(slots)):
                        text += f">* *{advlevel[lvl]} ({slots[lvl]} slots):* {','.join(map(lambda c: spelllinkify(c),details.spells[lvl+1]))}\n"
                else:
                    for lvl in range(len(details.slots)):
                        text += f">* *{advlevel[lvl]} ({details.slots[lvl]} slots):* {','.join(map(lambda c: spelllinkify(c),details.spells[lvl+1]))}\n"
                text += ">\n"
                result += text

        if len(self.reactions) > 0:
            result +=  ">#### Reactions\n"
            for reaction in self.reactions:
                result += f">{reaction}\n"
                result +=  ">\n"
        if len(self.bonusactions) > 0:
            result +=  ">\n>#### Bonus Actions\n"
            for bonus in self.bonusactions:
                result += f">{bonus}\n"
                result +=  ">\n"
        if len(self.equipment) > 0:
            result +=  ">\n>#### Equipment\n"
            for equip in self.equipment:
                result += f">{equip}\n"
                result +=  ">\n"
        result += "\n#### Description\n"
        for descrip in self.description:
            result += f"{descrip}\n\n"

        return result

def generatenpc():
    npc = NPC()

    def levelinvoke(module, level, npc):
        levelfn = getattr(module, 'level' + str(level), None)
        if levelfn != None: levelfn(npc)

    def selectabilities():
        def roll():
            return random.randrange(1,6) + random.randrange(1,6) + random.randrange(1,6)
        def handentry():
            def numberorrandom(ability):
                maybe = choose(ability, [])
                if maybe == "random":
                    return roll()
                else:
                    return int(maybe)
                
            npc.STR += numberorrandom("STR")
            npc.DEX += numberorrandom("DEX")
            npc.CON += numberorrandom("CON")
            npc.INT += numberorrandom("INT")
            npc.WIS += numberorrandom("WIS")
            npc.CHA += numberorrandom("CHA")
        def randomgen():
            npc.STR += roll()
            npc.DEX += roll()
            npc.CON += roll()
            npc.INT += roll()
            npc.WIS += roll()
            npc.CHA += roll()
        def average():
            npc.STR += 11 
            npc.DEX += 11
            npc.CON += 11
            npc.INT += 11
            npc.WIS += 11
            npc.CHA += 11
        def standard():
            scores = [15, 14, 13, 12, 10, 8]
            stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
            while len(stats) > 0:
                stat = choose(f"Apply the {scores[0]}: ", stats)
                current = getattr(npc, stat, 0)
                setattr(npc, stat, current + scores[0])
                scores.pop(0)
                stats.remove(stat)
        def npcstandard():
            scores = [16, 15, 12, 12, 12, 8]
            stats = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
            while len(stats) > 0:
                stat = choose(f"Apply the {scores[0]}: ", stats)
                current = getattr(npc, stat, 0)
                setattr(npc, stat, current + scores[0])
                scores.pop(0)
                stats.remove(stat)

        (choose("Method:", {"Standard": standard, "NPC": npcstandard, "Hand": handentry, "Randomgen": randomgen, "Average": average}))[1]()

    def selectrace():
        (_, mod) = choose("Choose a race: ", races)
        npc.race = mod
        npc.type = npc.race.type
        npc.description.append(npc.race.description)
        if getattr(npc.race, 'level0', None) != None:
            log('Firing racial level0')
            getattr(npc.race, 'level0', None)(npc)

        if getattr(npc.race, 'subraces', None) != None:
            (_, subracemod) = choose("Subrace: ", npc.race.subraces)
            npc.subrace = subracemod
            npc.description.append(npc.subrace.description)
            if getattr(npc.subrace, 'level0', None) != None:
                log('Firing subracial level0')
                getattr(npc.subrace, 'level0', None)(npc)

    # Do we want to start with race, class, or ability scores?
    startoptions = ['Ability Scores', 'Race', 'Gender']#, 'Name']
    while len(startoptions) > 0:
        opt = choose("Decide which?", startoptions)
        if opt == 'Ability Scores':
            selectabilities()
        elif opt == 'Race':
            selectrace()
        elif opt == 'Gender':
            npc.gender = choose("Choose gender: ", ['Male', 'Female'])
        #elif opt == 'Name':
        #    npc.name = generatename()
        startoptions.remove(opt)

    # That's level 0; now do level 1+
    # Select a class, append it to npc.classes, invoke the class level functions, repeat
    level = 0
    levelup = True
    while levelup == True:
        level += 1
        print("Choices for Level " + str(level))

        # Level up race and subrace
        levelinvoke(npc.race, level, npc)
        if npc.subrace != None:
            levelinvoke(npc.subrace, level, npc)

        # Choose a class
        clss = choose("Choose class:", classes)[1]
        npc.classes.append(clss)
        clsslevel = npc.levels(clss)
        if clsslevel == 1:
            npc.description.append(clss.description)
        # Every class should have an "everylevel(npc)" function, so crash if its not there
        (getattr(clss, 'everylevel', None))(npc)
        levelinvoke(clss, clsslevel, npc)
        if clss in npc.subclasses:
            levelinvoke(npc.subclasses[clss], clsslevel, npc)

        # Magic items
        if npc.levels() == 4:
            npc.equipment.append("***Magic Item: Uncommon Permanent.***")
        if npc.levels() == 7:
            npc.equipment.append("***Magic Item: Uncommon Permanent.***")
        if npc.levels() == 10:
            npc.equipment.append("***Magic Item: Rare Permanent.***")
        if npc.levels() == 13:
            npc.equipment.append("***Magic Item: Rare Permanent.***")
        if npc.levels() == 16:
            npc.equipment.append("***Magic Item: Very Rare Permanent.***")
        if npc.levels() == 19:
            npc.equipment.append("***Magic Item: Legendary Permanent.***")

        levelup = False if (choose("Another level? ", ['Yes','No']) == 'No') else True

    npc.freeze()
    return npc

def process(script):
    global scripted
    global scriptedinput

    scripted = True
    scriptfile = open(script, 'r')
    with scriptfile:
        alltext = scriptfile.readlines()
    for text in alltext:
        # Let's support comments in the scripted input
        if text[0] == '#': continue

        scriptedinput += text.split(",")

    with open('output.md', 'w') as outputfile:
        while len(scriptedinput) > 0:
            try:
                npc = generatenpc()
                outputfile.write(npc.emitMD())
                outputfile.write("\n\n")
            except Exception as ex:
                traceback.print_exception(ex)

def main():
    global verbose
    global quiet
    global scripted

    loadraces()
    loadclasses()
    loadfeats()
    #loadbackgrounds()

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs using PC rules/templates'
	)
    parser.add_argument('-verbose', choices=['quiet', 'verbose'])
    parser.add_argument('-version', action='version', version='%(prog)s 0.1')
    parser.add_argument('scripts', type=process, nargs='?',
                    help='Generate an NPC from script rather than interactively')
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbose != None:
        if args.verbose == 'verbose':
            verbose = True
        elif args.verbose == 'quiet':
            quiet = True
    
    if not scripted:
        npc = generatenpc()
        print(npc.emitMD())

if __name__ == '__main__':
	main()
