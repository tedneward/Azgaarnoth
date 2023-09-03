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


commonfeatures = {
    'amphibious' : "***Amphibious.*** You can breathe air and water.",
}


# ---------------------------------------------------------
# Module management
def discover(directory, loadfn):
    files = os.listdir(directory)
    for f in files:
        filename = directory + "/" + f
        if os.path.isfile(filename):
            loadfn(filename)

def loadmodule(filename, modulename):
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

    def builddict(codeobj):
        allowed_builtins = {
            "__builtins__": {
                "commonfeatures": commonfeatures,
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
        }

        moduledict = {}; count = 0
        for name in codeobj.co_names:
            element = codeobj.co_consts[count]
            if isinstance(element, types.CodeType):
                moduledict[name] = types.FunctionType(element, globals=allowed_builtins)
            else:
                moduledict[name] = element
            count += 1
        return moduledict

    literatecode = parsemd(filename)
    if len(literatecode) > 0:
        if verbose: print(literatecode)
        codeobj = compile(literatecode, modulename, 'exec')
        return builddict(codeobj)
    else:
        return {}

# We expect race modules to contain the following top-level symbols:
# Mandatory:
#   name : string
#   level0(npc) : function
#   subraces : map<string, dict(name and level functions)>
# Optional:
#   levelX(npc) : function
races = {}
def loadraces():
    def loadrace(filename):
        if os.path.splitext(filename)[1] == '.md':
            print(f"Parsing {str(filename)}... ", end = '')
            basename = os.path.basename(filename)
            modulename = os.path.splitext(basename)[0]
            module = loadmodule(filename, modulename)
            if len(module.keys()) > 0:
                races[modulename] = module
                print(f" loaded. " + modulename + ": " + str(races[modulename].keys()))
            else:
                print("No code found")

    discover(REPOROOT + 'Races', loadrace)

# We expect class modules to contain the following top-level symbols:
# name : string
# level0(npc) : function
#
# We expect subclass modules to contain the following top-level symbols:
# name : string
# levelX(npc) : function (where X is the subclass steps)
def loadclasses():
    classes = os.listdir(REPOROOT + 'Classes')
    for c in classes:
         print("Loading " + str(c))

# Backgrounds....
#def loadbackgrounds():
#    backgrounds = os.listdir(REPOROOT + 'Cultures/Backgrounds')
#    for c in backgrounds:
#         print("Loading " + str(c))

# Feats....


class NPC:
    def __init__(self):
        self.size = ''

        # Race is the module ('name', 'type', ...) for the race selected
        self.race = None
        # Subrace is a dict ('name', 'levelX', ...) for the subrace selected
        self.subrace = None
        # Classes is a list of the modules for each class taken
        # e.g, '[<fighter>,<fighter>,<monk>,<monk>,<fighter>] for a Fighter 3/Monk 2 NPC
        self.classes = []
        # Subclasses is a map of the classmodule.name : subclassmodule
        # e.g, '{'Fighter':<samurai>,'Wizard':<necromancer>}
        self.subclasses = {}

        self.hitpoints = 0
        self.hitconbonus = 0
        self.hitdice = { 'd6':0, 'd8':0, 'd10':0, 'd12':0, 'd20':0 }

        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.INT = 0
        self.WIS = 0
        self.CHA = 0

        self.speed = {}
        self.senses = { 'passive Perception': 0 }
        self.savingthrows = []
        self.conditionimmunities = []
        self.damageresistances = []
        self.damageimmunities = []
        # Proficiencies are for weapons and armor only; everything else is a skill
        self.proficiencies = []
        self.skills = []
        # Languages are read/write/speak
        self.languages = []
        self.traits = []

        self.cantripsknown = []
        self.spellsknown = []
        self.spellcastingattribute = ''
        self.maxspellsknown = 0
        self.spellslots = {}

        self.actions = []
        self.bonusactions = []
        self.reactions = []

        self.description = []

    def abilitybonus(num):
        return (num / 2) - 5

    def proficiencybonus(self):
        return (len(self.classes) // 4) + 2

    def hits(self, die):
        """Generate the hit points gained at the current level, using the die specified."""
        self.hitdice[die] += 1
        if len(self.classes) == 1:
            self.hitpoints += int(die[1:]) # Strip off the 'd'
        else:
            top = int(die[1:])
            self.hitpoints += random.randrange(4, top)
        self.hitconbonus += self.abilitybonus(self.CON)
        self.hitpoints += self.abilitybonus(self.CON)

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)

    def emitMD(self):
        pass

def main():
    global verbose
    global quiet

    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs'
	)
    parser.add_argument('--verbose', choices=['quiet', 'verbose'])
    parser.add_argument('--version', action='version', version='%(prog)s 0.0')
    args = parser.parse_args()

    if args.verbose != None:
        if args.verbose == 'verbose':
            verbose = True
        elif args.verbose == 'quiet':
            quiet = True

    races = loadraces()
    #classes = loadclasses()
    #backgrounds = loadbackgrounds()

    parser.print_usage()

if __name__ == '__main__':
	main()
