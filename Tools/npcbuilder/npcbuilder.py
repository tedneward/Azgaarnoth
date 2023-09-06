#!/usr/bin/env python3

import argparse
import os
import random
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

# ---------------------------------------------------------
# 'Common' routines available to all loaded modules
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

        response = int(response) - 1 # Account for zero-based index
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

        responseidx = int(response) - 1 # Account for zero-based index
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
    filename = name.replace(' ','-')
    return f'[{name}](http://azgaarnoth.tedneward.com/spells/{filename}.md)'

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

traits = {
    'amphibious' : "***Amphibious.*** You can breathe air and water.",
    'fey-ancestry' : "***Fey Ancestry.*** You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
    'powerful-build': "***Powerful Build.*** You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.",
    'sea-emissary' : "***Emissary of the Sea.*** You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.",
    'sunlight-sensitivity' : "***Sunlight Sensitivity.*** You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.",
}


# ---------------------------------------------------------
# Module management
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
        builtins = {
            "traits": traits,
            "spelllinkify": spelllinkify,
            "choose": choose,
            "replace": replace,
            "random": randomlist,
            "dieroll": dieroll,
            "min": min,
            "len": len,
            "print": print,
            "types": types
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

# We expect race modules to contain the following top-level symbols:
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
    def ismdfile(filepath): 
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.md': return True
        else: return False

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

# We expect class modules to contain the following top-level symbols:
# name : string
# levelX(npc) : functions invoked at each level in that class
# preferredstats() : function returning (in order) the stats preferred
# subclasses: map<string, dict(name, levelX functions)>
classes = {}
def loadclasses():
    def ismdfile(filepath): 
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.md': return True
        else: return False

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
                subclasses = {}
                excludedmds = [ 'index.md', 'SpellList.md', 'Infusions.md', 'Invocations.md', 'Talents.md' ]
                for sf in os.listdir(dirpath):
                    if ismdfile(dirpath + "/" + sf) and (sf not in excludedmds):
                        log(f"Parsing {sf}...")
                        subclassname = os.path.splitext(sf)[0]
                        subclassmod = loadmodule(dirpath + '/' + sf, basemodule.name + "-" + subclassname)
                        subclasses[subclassname] = subclassmod
                setattr(basemodule, "subclasses", subclasses)
            if basemodule != None:
                classes[basemodule.name] = basemodule

# Backgrounds....
#def loadbackgrounds():
#    backgrounds = os.listdir(REPOROOT + 'Cultures/Backgrounds')
#    for c in backgrounds:
#         print("Loading " + str(c))

# Feats....


class NPC:
    class Spellcasting:
        def __init__(self, npc, ability):
            self.npc = npc
            self.ability = ability
            self.cantrips = []
            self.maxspellsknown = 0
            self.spells = []
            self.slots = []
        
        def spellsavedc(self):
            return 8 + self.npc.proficiencybonus() + (getattr(self.npc, self.ability + "bonus", None))()

        def spellattack(self):
            return self.npc.proficiencybonus() + (getattr(self.npc, self.ability + "bonus", None))()

        def spellslots(self):
            pass

    def __init__(self):
        self.description = []

        self.size = 'Medium'
        self.type = ''

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
        self.proficiencies = []
        self.skills = []

        # Languages are read/write/speak
        self.languages = []

        # Traits are anything that isn't an action, bonus action, reaction, ...
        self.traits = []
        self.actions = []
        self.bonusactions = []
        self.reactions = []

        # Spellcasting data; each is a hash tied to the name of the
        # class or race whose spellcasting this is (Cleric, Wizard,
        # Arcane Trickster, etc)
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

    def abilityscoreimprovement(self):
        abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
        ability = choose("Choose an ability to improve: ", abilities)
        if ability == 'STR': self.STR += 1
        elif ability == 'DEX': self.DEX += 1
        elif ability == 'CON': self.CON += 1
        elif ability == 'INT': self.INT += 1
        elif ability == 'WIS': self.WIS += 1
        elif ability == 'CHA': self.CHA += 1

    def proficiencybonus(self):
        return (self.levels() // 4) + 2

    def levels(self, clss = None):
        if clss == None:
            return len(self.classes)
        else:
            count = 0
            for cli in self.classes:
                if cli == clss:
                    count += 1
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
        spellcasting = NPC.Spellcasting(self, ability)
        self.npc.spellcasting[source] = spellcasting
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
        def getsubracename(): return '' if self.subrace == None else self.subrace.name + ' '

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
            return f"{self.race.type} ({getsubracename()}{self.race.name})"
        def getclasssubstring():
            classmap = {}
            for c in self.classes:
                if c not in classmap:
                    classmap[c] = 1
                else:
                    classmap[c] += 1
            strs = []
            for c in classmap:
                if c in c.subclasses.keys():
                    strs.append(f"{c.name} ({c.subclasses[c].name}) {classmap[c]}")
                else:
                    strs.append(f"{c.name} {classmap[c]}")
            return "/".join(strs)

        linesep = ">___\n"

        result  =  ">### Name\n"
        result += f'*{self.size} {getracesubstring()} {getclasssubstring()}, any alignment*\n'
        result += linesep
        result += f">- **Armor Class** {getarmorclass()}\n"
        result += f">- **Hit Points** {self.hitpoints} ({self.hitdicedesc()} + {self.hpconbonus})\n"
        result += f">- **Speed** {getspeed()}\n"
        result += linesep
        result +=  ">|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|\n"
        result +=  ">|:---:|:---:|:---:|:---:|:---:|:---:|\n"
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
        if len(self.cantripsknown) > 0:
            result += f">***Innate Spellcasting.*** You know the cantrip{'s' if len(self.cantripsknown) > 1 else ''} {','.join(self.cantripsknown)}.\n>\n"
        if len(self.reactions) > 0:
            result +=  ">#### Rections\n"
            for reaction in self.reactions:
                result += f">{reaction}\n"
                result +=  ">\n"
        if len(self.bonusactions) > 0:
            result +=  ">\n>#### Bonus Actions\n"
            for bonus in self.bonusactions:
                result += f">{bonus}\n"
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
            def numberorrandom():
                if len(scriptedinput) > 0:
                    maybe = scriptedinput.pop(0).strip()
                    if maybe == "random":
                        return roll()
                    else:
                        return int(maybe)
                else:
                    return roll()
                
            npc.STR += numberorrandom()
            npc.DEX += numberorrandom()
            npc.CON += numberorrandom()
            npc.INT += numberorrandom()
            npc.WIS += numberorrandom()
            npc.CHA += numberorrandom()
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

        (choose("Method:", {"Standard": standard, "Hand": handentry, "Randomgen": randomgen, "Average": average}))[1]()

    def selectrace():
        (name, mod) = choose("Choose a race: ", races)
        npc.race = mod
        npc.type = mod.type
        if getattr(npc.race, 'level0', None) != None:
            log('Firing racial level0')
            getattr(npc.race, 'level0', None)(npc)

        if getattr(npc.race, 'subraces', None) != None:
            (_, subracemod) = choose("Subrace: ", npc.race.subraces)
            npc.subrace = subracemod
            if getattr(npc.subrace, 'level0', None) != None:
                log('Firing subracial level0')
                getattr(npc.subrace, 'level0', None)(npc)

    # Do we want to start with race, class, or ability scores?
    startoptions = ['Ability Scores', 'Race']
    while len(startoptions) > 0:
        opt = choose("Decide which?", startoptions)
        if opt == 'Ability Scores':
            selectabilities()
        elif opt == 'Race':
            selectrace()
        startoptions.remove(opt)

    # That's level 0; now do level 1+
    # Select a class, append it to npc.classes, invoke the class level functions, repeat
    level = 0
    levelup = True
    while levelup == True:
        level += 1
        print("-------- Choices for Level " + str(level))

        # Level up race and subrace
        levelinvoke(npc.race, level, npc)
        if npc.subrace != None:
            levelinvoke(npc.subrace, level, npc)

        # Choose a class
        clss = choose("Choose class:", classes)[1]
        npc.classes.append(clss)
        clsslevel = npc.levels(clss)
        # Every class should have an "everylevel(npc)" function, so crash if its not there
        (getattr(clss, 'everylevel', None))(npc)
        levelinvoke(clss, clsslevel, npc)

        # Magic items
        if npc.levels() == 4:
            npc.description.append("***Magic Item: Uncommon Permanent.***")
        if npc.levels() == 7:
            npc.description.append("***Magic Item: Uncommon Permanent.***")
        if npc.levels() == 10:
            npc.description.append("***Magic Item: Rare Permanent.***")
        if npc.levels() == 13:
            npc.description.append("***Magic Item: Rare Permanent.***")
        if npc.levels() == 16:
            npc.description.append("***Magic Item: Very Rare Permanent.***")
        if npc.levels() == 19:
            npc.description.append("***Magic Item: Legendary Permanent.***")

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
                outputfile.write("---\n\n")
            except Exception:
                print("Exception!")

def main():
    global verbose
    global quiet
    global scripted

    loadraces()
    loadclasses()
    #loadbackgrounds()

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs using PC rules/templates'
	)
    parser.add_argument('--verbose', choices=['quiet', 'verbose'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
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
