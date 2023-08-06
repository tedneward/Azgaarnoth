#!/usr/bin/env python3

import argparse
import importlib.machinery
import importlib.util
import os
import random

# This script parses the markdown files in /Races, /Classes, and /Backgrounds
# loading the Python code found in each .md file into a script that is then
# dynamically loaded into a module and used as part of the NPC generation
# process. In essence, this is a flavor of "literate programming".

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

    if isinstance(choices, list) and len(scriptedinput) == 0: return choosefromlist(choices)
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

commonfeatures = {
    'amphibious' : "**Amphibious.**. You can breathe air and water.",
    'darkvision30' : "**Darkvision.**. You can see in dim light within 30 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    'darkvision' : "**Darkvision.**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    'superiordarkvision' : "**Superior Darkvision.**. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
}

def populatemodule(module):
    module.commonfeatures = commonfeatures
    module.choose = choose
    module.levelinvoke = levelinvoke
    module.abilityscoreimprovement = abilityscoreimprovement
    #module.feat = feat
    #module.spelllinkify = spelllinkify


# ---------------------------------------------------------
# Module management
def discover(directory, loadfn):
    files = os.listdir(directory)
    for f in files:
        if f != '__pycache__':
            loadfn(directory + "/" + f)

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
    if pythoncode == "":
        print("WARNING: No literate Python found")
    return pythoncode

# We expect race modules to contain the following top-level symbols:
# Mandatory:
# name : string
# level0(npc) : function
# subraces : map<string, modules>
def loadraces():
    def loadrace(mdfilename):
        print("Loading " + str(mdfilename))
        code = parsemd(mdfilename)

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

def loadbackgrounds():
    backgrounds = os.listdir(REPOROOT + 'Cultures/Backgrounds')
    for c in backgrounds:
         print("Loading " + str(c))



class NPC:
    def __init__(self):
        self.size = ''

        # Race is the module for the race selected
        self.race = None
        # Subrace is a module for the subrace selected
        self.subrace = None
        # Type is "humanoid", "aberrant", etc
        self.type = ''
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
        self.senses = ['passive Perception']
        self.savingthrows = []
        self.conditionimmunities = []
        self.damageresistances = []
        self.damageimmunities = []
        # Proficiencies are for weapons and armor only; everything else is a skill
        self.proficiencies = []
        self.skills = []
        # Languages are read/write/speak
        self.languages = []
        self.features = []

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

    def replace(text, list, newtext):
        for it in list:
            if it[0:len(text)] == text:
                list.remove(it)
        list.append(text + " " + newtext)



def main():
    parser = argparse.ArgumentParser(
        prog='NPCBuilder',
        description='A tool for generating 5th-ed NPCs'
	)
    parser.add_argument('--version', action='version', version='%(prog)s 0.0')
    parser.parse_args()

    races = loadraces()
    #classes = loadclasses()
    #backgrounds = loadbackgrounds()

    parser.print_usage()

if __name__ == '__main__':
	main()
