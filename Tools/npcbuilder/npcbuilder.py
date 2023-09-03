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

def abilityscoreimprovement(npc):
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

    def interactive():
        return choose("Improve an ability score by 1:", abilities) 

    def scripted():
        scriptedin = scriptedinput.pop(0).strip()
        if scriptedin.isdigit():
            return abilities[int(scriptedin)]
        else:
            return scriptedin

    ability = interactive() if len(scriptedinput) == 0 else scripted()
    newvalue = int(getattr(npc, ability)) + 1
    setattr(npc, ability, newvalue)

def skillchoice(npc):
    skills = [ 'Acrobatics', 'Animal Handling', 'Arcana','Athletics',
        'Deception', 'History', 'Insight', 'Intimidation', 'Investigation',
        'Medicine', 'Nature', 'Perception', 'Performance', 'Persuasion',
        'Religion', 'Sleight of Hand', 'Stealth', 'Survival']

    def interactive():
        return choose("Choose a skill:", skills) 

    def scripted():
        scriptedin = scriptedinput.pop(0).strip()
        if scriptedin.isdigit():
            return skills[int(scriptedin)]
        else:
            return scriptedin

    skill = interactive() if len(scriptedinput) == 0 else scripted()
    npc.skills.append(skill)

def spelllinkify(name):
    return f'[{name}](http://azgaarnoth.tedneward.com/spells/{name}.md)'

def replace(text, list, newtext):
    for it in list:
        if it[0:len(text)] == text:
            list.remove(it)
    list.append(text + " " + newtext)


traits = {
    'amphibious' : "***Amphibious.*** You can breathe air and water.",
    'fey' : "***Fey Ancestry.*** You have advantage on saving throws against being charmed, and magic can't put you to sleep.",
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

        return pythoncode

    def builddict(module):
        builtins = {
            "traits": traits,
            "levelinvoke": levelinvoke,
            "abilityscoreimprovement": abilityscoreimprovement,
            "spelllinkify": spelllinkify,
            "choose": choose,
            "scriptedinput": scriptedinput,
            "inputhistory": inputhistory,
            "loadmodule": loadmodule,
            "replace": replace,
            "min": min,
            "len": len,
            "print": print,
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
races = {}
def loadraces():
    def ismdfile(filepath): 
        if os.path.isfile(filepath) and os.path.splitext(filepath)[1] == '.md': return True
        else: return False

    racesroot = REPOROOT + 'Races'
    entries = os.listdir(racesroot)
    for f in entries:
        entryname = racesroot + "/" + f

        if os.path.isdir(entryname):
            dirpath = entryname
            log(f"Parsing directory {dirpath}...")
            dirname = os.path.basename(dirpath)
            log(dirname)
            basemodule = loadmodule(dirpath + "/index.md", dirname)
            log(basemodule)
            subraces = {}
            for sf in os.listdir(dirpath):
                if ismdfile(sf):
                    log(f"Parsing subracefile {sf}")
                    subracename = os.path.basename(sf)
                    subracemod = loadmodule(dirpath + '/' + sf, subracename)
                    subraces[subracename] = subracemod
            setattr(basemodule, "subraces", subraces)
            print(basemodule)
            races[basemodule.name] = basemodule

        elif ismdfile(entryname):
            log(f"Parsing {entryname}...")
            module = loadmodule(entryname)
            if module != None:
                races[module.name] = module

# We expect class modules to contain the following top-level symbols:
# name : string
# levelX(npc) : functions invoked at each level in that class
# subclasses: map<string, dict(name, levelX functions)>
classes = {}
def loadclasses():
    directory = REPOROOT + 'Classes'
    files = os.listdir(directory)
    for f in files:
        filename = directory + "/" + f
        if os.path.isfile(filename) and os.path.splitext(filename)[1] == 'md':
            module = loadmodule(filename)
            if module != None:
                classes[module.name] = module

# Backgrounds....
#def loadbackgrounds():
#    backgrounds = os.listdir(REPOROOT + 'Cultures/Backgrounds')
#    for c in backgrounds:
#         print("Loading " + str(c))

# Feats....


class NPC:
    def __init__(self):
        self.size = ''

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
        self.hitconbonus = 0
        self.hitdice = { 'd6':0, 'd8':0, 'd10':0, 'd12':0, 'd20':0 }

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

        # Spellcasting data; this one is going to be a touch tricky to sort out
        self.cantripsknown = []
        self.spellsknown = []
        self.spellcastingattribute = ''
        self.maxspellsknown = 0
        self.spellslots = {}

        self.description = []

        # Normalizers are fns run when the NPC is frozen;
        # usually these are level-dependent text/traits/features/etc
        self.normalizers = []

    def defer(self, fn):
        """Defer fn to be invoked when the NPC is normalized/frozen"""
        self.normalizers.append(fn)

    def abilitybonus(num):
        return (num / 2) - 5

    def proficiencybonus(self):
        return (len(self.classes) // 4) + 2

    def hits(self, die):
        """Generate the hit points gained at the current level, using the die specified."""
        self.hitdice[die] += 1
        if len(self.classes) == 1:
            # Max hit points at first level
            self.hitpoints += int(die[1:]) # Strip off the 'd'
        else:
            # We roll randomly (sort of)
            top = int(die[1:])
            self.hitpoints += random.randrange(4, top)
        # Keep a running total for the CON bonus, since it cah change over time/levels
        self.hitconbonus += self.abilitybonus(self.CON)
        # Likewise, keep a running total for hit points
        self.hitpoints += self.abilitybonus(self.CON)

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)
    
    def freeze(self):
        """The NPC is finished building, so normalize any traits/features to this level."""

    def emitMD(self):
        """
>### Bright Elf
>*Medium Humanoid (Elf), Any Chaotic Alignment*
>___
>- **Armor Class** 11
>- **Hit Points** 4 (1d8)
>- **Speed** 30 ft.
>___
>|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|10 (+0)|12 (+1)|10 (+0)|10 (+0)|10 (+0)|10 (+0)|
>
>___
>- **Proficiency Bonus** +2
>- **Saving Throws** 
>- **Damage Vulnerabilities** 
>- **Damage Resistances** 
>- **Damage Immunities** 
>- **Condition Immunities** 
>- **Skills** Perception +2
>- **Senses** Darkvision 60 ft.,Passive Perception 12
>- **Languages** Elvish
>- **Challenge** 0
>___
>***Fey Ancestry.*** Elf commoners have advantage on saving throws against being charmed, and magic can't put you to sleep.
>
>#### Actions
>***Club.*** Melee Weapon Attack: +2 to hit, reach 5 ft., one target. Hit: 2 (1d4) bludgeoning damage.
>
>***Shortbow.*** Ranged Weapon Attack: +3 to hit, range 80/320 ft., one target. Hit: 4 (1d6+1) piercing damage.
>
        """
        def getsubracename():
            if self.subrace != None: return self.subrace.name + ' '
            else: return ''

        def getarmorclass():
            result = []
            ac = 10
            for (actext, acnum) in self.armorclass:
                if acnum > 8:
                    # Only armor itself is ever a value 10+
                    ac = acnum
                    result.append(f'{actext} ({acnum})')
                else:
                    ac += acnum
                    result.append(f'{actext} (+{acnum})')
            ac += self.abilitybonus(self.DEX)
            result.append(f'DEX ({self.abilitybonus(self.DEX)})')
            return str(ac) + ' (' + ",".join(result) + ')'

        result  =  '# Name\n'
        result +=  '\n'
        result +=  '\n\n'.join(self.description)
        result +=  '>### Name\n'
        result += f'*{self.size} {self.race.type} ({getsubracename()}{self.race.name}), any alignment*\n'
        result +=  '>___\n'
        result += f'>- **Armor Class** {getarmorclass()}'
        pass

def generatenpc():
    npc = NPC()

    def selectabilities():
        def roll():
            return random.randrange(1,6) + random.randrange(1,6) + random.randrange(1,6)
        def handentry():
            def numberorrandom():
                maybe = scriptedinput.pop(0).strip()
                if maybe == "random":
                    return roll()
                else:
                    return int(maybe)
                
            npc.STR = numberorrandom()
            npc.DEX = numberorrandom()
            npc.CON = numberorrandom()
            npc.INT = numberorrandom()
            npc.WIS = numberorrandom()
            npc.CHA = numberorrandom()
        def randomgen():
            npc.STR = roll()
            npc.DEX = roll()
            npc.CON = roll()
            npc.INT = roll()
            npc.WIS = roll()
            npc.CHA = roll()
        def average():
            npc.STR = 11 
            npc.DEX = 11
            npc.CON = 11
            npc.INT = 11
            npc.WIS = 11
            npc.CHA = 11
        (choose("Method:", {"Hand": handentry, "Randomgen": randomgen, "Average": average}))[1]()

    def selectclass():
        pass

    def selectrace():
        (name, mod) = choose("Choose a race: ", races)
        npc.race = mod
        if 'subraces' in npc.race:
            print(npc.race['subraces'])

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

    return npc

def main():
    global verbose
    global quiet

    global races
    global classes

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs'
	)
    parser.add_argument('--verbose', choices=['quiet', 'verbose'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.0')
    parser.add_argument('--input FILENAME', help='File to use for scripted input')
    args = parser.parse_args()

    # Logging off, on, or a lot?
    if args.verbose != None:
        if args.verbose == 'verbose':
            verbose = True
        elif args.verbose == 'quiet':
            quiet = True

    loadraces()
    loadclasses()
    #loadbackgrounds()

    npc = generatenpc()
    print(npc.emitMD())

if __name__ == '__main__':
	main()
