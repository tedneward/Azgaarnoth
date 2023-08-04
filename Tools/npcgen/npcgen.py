#!/usr/bin/env python3

import argparse
import importlib.machinery
import importlib.util
import os
import random

# This script parses class options in directories and applies them
# (imperatively/script-like) to the creation of NPCs.
# I think I want to rewrite this to take advantage of two
# ideas:
# 1) Literate Python programming. Put the Python modules into
# the Markdown descriptions so as to keep text and code together.
# This also means the modules are coming out of /Races, /Classes, etc.
# 2) Include Backgrounds as part of NPC generation.
# 3) Include name suggestions.
# 4) Include suggested personality traits (quirks, etc) from tables.
# 5) Have "scripts" be lambdas/functions that are executed all
# at once rather than level-at-a-time; this will make it easier
# to include specific modifier text correctly (such as the ability
# gained at level 1 that uses the NPC's proficiency bonus, which could
# easily be higher because of later levels).
# 6) Assume links will be to a MkDocs-generated website rather
# than to GitHub directly.
# 7) Magic items! NPCs get goodies, too, you know....
# 8) Spell lists
# 9) Feats

def spelllinkify(name):
    return "["+ name+"](https://github.com/tedneward/Azgaarnoth/tree/master/Magic/Spells/"+ name.replace(' ', '-') + ".md)"

def abilitybonus(score):
    bonus = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11:	0,
        12: 1,
        13:	1,
        14: 2,
        15:	2,
        16: 3,
        17:	3,
        18: 4,
        19:	4,
        20: 5,
        21:	5,
        22: 6,
        23:	6,
        24: 7,
        25:	7,
        26: 8,
        27:	8,
        28: 9,
        29: 9,
        30: 10
    }
    return bonus[score]

class NPC:
    def __init__(self):
        self.size = ''

        # Race is the module for the race selected
        self.race = None
        # Subrace is a string (easier)
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

        self.speed = ''
        self.senses = ['passive Perception']
        self.savingthrows = []
        self.resistances = []
        self.immunities = []
        # Skills and proficiencies are basically the same thing; having a proficiency
        # in a skill means adding your profbonus to the skill's ability bonus
        self.proficiencies = []
        self.skills = []
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

    def proficiencybonus(self):
        return (len(self.classes) // 4) + 2

    def hits(self, die):
        self.hitdice[die] += 1
        if len(self.classes) == 1:
            self.hitpoints += int(die[1:]) # Strip off the 'd'
        else:
            top = int(die[1:])
            self.hitpoints += random.randrange(4, top)
        self.hitconbonus += abilitybonus(self.CON)
        self.hitpoints += abilitybonus(self.CON)

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)

    def racedesc(self):
        desc = self.race.name
        if self.subrace != None:
            desc = desc + " (" + self.subrace + ")"
        return desc

    def classdesc(self):
        classmap = {}
        for cl in self.classes:
            if cl in classmap:
                classmap[cl] += 1
            else:
                classmap[cl] = 1
        classlist = []
        for pair in classmap.items():
            if pair[0] in self.subclasses:
                classlist.append(pair[0] + " (" + self.subclasses[pair[0]].name + ") " + str(pair[1]))
            else:
                classlist.append(pair[0] + " " + str(pair[1]))
        return ", ".join(classlist)
    
    def classlevel(self, clss):
        count = 0
        for cli in self.classes:
            if cli == clss:
                count += 1
        return count
    
    def level(self):
        return len(self.classes)

    def print_markdown(self):
        print("# Name")
        print("*" + self.size + " " + self.racedesc() + " " + self.classdesc() + " (alignment)*")
        print("")
        print("**Armor Class** 10") # Maybe stack up AC bonuses?
        print("")
        print("**Hit Points** " + str(self.hitpoints) + " (" + str(self.hitdicedesc()) + " + " + str(self.hitconbonus) + ")")
        print("")
        print("**Speed** " + self.speed)
        print("")
        print(self.print_stats())
        print("")
        print("**Proficiency Bonus** +" + str(self.proficiencybonus()))
        print("")
        print("**Damage Resistances** " + ", ".join(self.resistances))
        print("")
        print("**Damage Immunities** " + ", ".join(self.immunities))
        print("")
        print(self.print_savingthrows())
        print("")
        print(self.print_skills())
        print("")
        print("**Senses** " + ", ".join(self.senses))
        print("")
        print("**Languages** " + ", ".join(self.languages))
        print("")
        for feature in self.features:
            print(feature)
            print("")
        if len(self.cantripsknown) > 0: 
            print(self.print_cantrips())
            print("")
        if self.maxspellsknown > 0:
            print(self.print_spells())
            print("")
        print("#### Actions")
        for action in self.actions:
            print(action)
            print("")
        print("")
        print("#### Bonus Actions")
        for action in self.bonusactions:
            print(action)
            print("")
        print("")
        print("#### Reactions")
        for action in self.reactions:
            print(action)
            print("")
        print("")
        print("----")
        print('\n'.join(self.description))

    def print_stats(self):
        desc =  "**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**\n"
        desc += "-------|-------|-------|-------|-------|-------\n"
        desc += (str(self.STR) + "(" + str(abilitybonus(self.STR)) + ") | " + 
                 str(self.DEX) + "(" + str(abilitybonus(self.DEX)) + ") | " + 
                 str(self.CON) + "(" + str(abilitybonus(self.CON)) + ") | " + 
                 str(self.INT) + "(" + str(abilitybonus(self.INT)) + ") | " + 
                 str(self.WIS) + "(" + str(abilitybonus(self.WIS)) + ") | " + 
                 str(self.CHA) + "(" + str(abilitybonus(self.CHA)) + ")")
        return desc

    def print_savingthrows(self):
        desc = "**Saving Throws** "
        savingthrowlist = map(lambda attr: attr + " +" + str(self.proficiencybonus() + abilitybonus(getattr(self, attr))), self.savingthrows)
        return desc + ", ".join(savingthrowlist)
    
    def print_skills(self):
        desc = "**Skills** "
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
            return skill + " +" + str(self.proficiencybonus() + abilitybonus(getattr(self, skillmap[skill])))
        skilllist = map(mapskill, self.skills)
        return desc + ", ".join(skilllist)
    
    def print_cantrips(self):
        cantriplinks = map(spelllinkify, self.cantripsknown)
        desc = "**Cantrips.** You know the following cantrips: " + ", ".join(cantriplinks)
        return desc

    def print_spells(self):
        spelllinks = map(spelllinkify, self.spellsknown)

        desc = "**Spellcasting.** Spell save DC = 8 + your proficiency bonus + " + self.spellcastingattribute + " bonus. Spell attack modifier = your proficiency bonus + " + self.spellcastingattribute + " modifier.\n"
        desc += "Spells known (Max " + str(self.maxspellsknown) + "): " + ", ".join(spelllinks) + "\n"
        ordinals = [ "", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th" ]
        desc += "Spell slots:\n"
        for lvl in self.spellslots.keys():
            desc += "* " + ordinals[lvl] + ": " + str(self.spellslots[lvl]) + "\n"
        return desc

# This dict is shared to all race/class modules for consistent feature text.
feats = {
    'Lucky' : "**Lucky.** You have 3 luck points. Whenever you make an attack roll, an ability check, or a saving throw, you can spend one luck point to roll an additional d20. You can choose to spend one of your luck points after you roll the die, but before the outcome is determined. You choose which of the d20s is used for the attack roll, ability check, or saving throw. You can also spend one luck point when an attack roll is made against you. Roll a d20 and then choose whether the attack uses the attacker's roll or yours. If more than one creature spends a luck point to influence the outcome of a roll, the points cancel each other out; no additional dice are rolled. You regain your expended luck points when you finish a long rest.",
}

commonfeatures = {
    'amphibious' : "**Amphibious.**. You can breathe air and water.",
    'darkvision30' : "**Darkvision.**. You can see in dim light within 30 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    'darkvision' : "**Darkvision.**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.",
    'superiordarkvision' : "**Superior Darkvision.**. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
}

def discover(dirname):
    results = {}
    for file in os.listdir(dirname):
        if file == '__pycache__':
            continue
        if file == '_Base.py':
            continue

        loader = importlib.machinery.SourceFileLoader( file, dirname + '/' + file )
        spec = importlib.util.spec_from_loader( file, loader )
        mymodule = importlib.util.module_from_spec( spec )
        loader.exec_module( mymodule )

        # Use mymodule
        results[mymodule.name] = mymodule

        # "import" some useful definitions from here
        populateModule(mymodule)
    return results

def replace(text, list, newtext):
    for it in list:
        if it[0:len(text)] == text:
            list.remove(it)
    list.append(newtext)

# scriptedinput declared in process()
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

def levelinvoke(module, level, npc):
    def nop(npc): pass

    levelfn = getattr(module, 'level' + str(level), nop)
    levelfn(npc)

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

def feat(npc):
    pass

def asiorfeat(npc):
    choice = choose("Ability Score Improvement or Feat?", ["ABI", "Feat"])
    if choice == "ABI": return abilityscoreimprovement(npc)
    elif choice == "Feat": return feat(npc)
    else: raise BaseException("Unrecognized input: " + choice)

def populateModule(module):
    module.commonfeatures = commonfeatures
    module.replace = replace
    module.choose = choose
    module.discover = discover
    module.levelinvoke = levelinvoke
    module.asiorfeat = asiorfeat
    module.abilityscoreimprovement = abilityscoreimprovement
    module.feat = feat
    module.spelllinkify = spelllinkify

# Slurp functions--these pull in races and classes
#
def loadraces():
    results = {}
    for file in os.listdir("races"):
        if file == '__pycache__':
            continue

        loader = importlib.machinery.SourceFileLoader( file, 'races/' + file )
        spec = importlib.util.spec_from_loader( file, loader )
        mymodule = importlib.util.module_from_spec( spec )
        loader.exec_module( mymodule )

        # Use mymodule
        results[mymodule.name] = mymodule

        # "import" some useful definitions from here
        populateModule(mymodule)
    # Sort the results
    keys = list(results.keys())
    keys.sort()
    sortedresults = {i: results[i] for i in keys}
    return sortedresults

def loadclasses():
    results = {}
    for file in os.listdir("classes"):
        if file == '__pycache__':
            continue

        loader = importlib.machinery.SourceFileLoader( file, 'classes/' + file + '/_Base.py' )
        spec = importlib.util.spec_from_loader( file, loader )
        mymodule = importlib.util.module_from_spec( spec )
        loader.exec_module( mymodule )

        # Use mymodule
        results[mymodule.name] = mymodule

        # "import" some useful definitions from here
        populateModule(mymodule)
    return results

def loadfeats():
    results = {}
    for file in os.listdir("feats"):
        if file == '__pycache__':
            continue

        loader = importlib.machinery.SourceFileLoader( file, 'feats/' + file )
        spec = importlib.util.spec_from_loader( file, loader )
        mymodule = importlib.util.module_from_spec( spec )
        loader.exec_module( mymodule )

        # Use mymodule
        results[mymodule.name] = mymodule

        # "import" some useful definitions from here
        populateModule(mymodule)
    return results

def process(script):
    scriptfile = open(script, 'r')
    with scriptfile:
        text = scriptfile.readline()
    global scriptedinput
    scriptedinput = text.split(",")

def gennpc():
    npc = NPC()

    # Preload what we need
    races = loadraces()
    classes = loadclasses()
    #feats = loadfeats()

    def roll():
        return random.randrange(1,6) + random.randrange(1,6) + random.randrange(1,6)
    def handentry(npc):
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
    def randomgen(npc):
        npc.STR = roll()
        npc.DEX = roll()
        npc.CON = roll()
        npc.INT = roll()
        npc.WIS = roll()
        npc.CHA = roll()
        print(npc.print_stats())
    def average(npc):
        npc.STR = 11 
        npc.DEX = 11
        npc.CON = 11
        npc.INT = 11
        npc.WIS = 11
        npc.CHA = 11
    (choose("Ability score generation:", {"Hand": handentry, "Randomgen": randomgen, "Average": average}))[1](npc)

    racemodule = choose("Choose race:", races)[1]
    npc.race = racemodule
    racemodule.apply_race(npc)
    if len(racemodule.subraces) > 0:
        subrace = choose("Choose subrace:", racemodule.subraces)
        npc.subrace = subrace
        racemodule.apply_subrace(subrace, npc)

    level = 0
    levelup = True
    while levelup == True:
        level += 1
        print("-------- Level " + str(level))

        # Any racial/subracial level advancements?
        levelinvoke(npc.race, level, npc)

        clss = choose("Choose class:", classes)[1]

        clsslevel = npc.classlevel(clss.name) + 1
        levelinvoke(clss, clsslevel, npc)

        if len(scriptedinput) == 0:
            levelup = (input("Another level? ") == 'y')
        else:
            continue

    return npc

def main():
    parser = argparse.ArgumentParser(
                    prog='NPCGen',
                    description='A tool for generating 5th-ed NPCs')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('scripts', type=process, nargs='?',
                    help='Generate an NPC from script rather than interactively')
    parser.parse_args()

    npc = gennpc()
    npc.print_markdown()

if __name__ == '__main__':
	main()
