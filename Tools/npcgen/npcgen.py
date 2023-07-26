#!/usr/bin/env python3

import argparse
import importlib.machinery
import importlib.util
import os

# This script parses class options in directories and applies them
# (imperatively/script-like) to the creation of NPCs.

class NPC:
    def __init__(self):
        self.size = ''
        self.race = ''
        self.subrace = ''
        self.classes = []   # This will be a list of each level of class taken, e.g., "[Fighter, Fighter, Monk, Monk, Fighter]" for 1-5 level
        self.subclasses = {}# This will be a map of the subclasses mapped to a class, e.g., "{Fighter:Defender, Wizard:Necromancer}", etc
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
        self.skills = []
        self.resistances = []
        self.immunities = []
        self.proficiencies = []
        self.languages = []
        self.features = []
        self.actions = []
        self.bonusactions = []
        self.reactions = []
        self.description = []

    def hitdicedesc(self):
        dicelist = []
        for key in self.hitdice.keys():
            if self.hitdice[key] > 0:
                dicelist.append(str(self.hitdice[key]) + str(key))
        return " + ".join(dicelist)

    def racedesc(self):
        desc = self.race
        if self.subrace != '':
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
                classlist.append(pair[0] + " (" + self.subclasses[pair[0]] + ") " + str(pair[1]))
            else:
                classlist.append(pair[0] + " " + str(pair[1]))
        return ", ".join(classlist)

    def print_markdown(self):
        print("# NPC")
        print("*" + self.size + " " + self.racedesc() + " " + self.classdesc() + " (any alignment)*")
        print("")
        print("**Armor Class** 10")
        print("")
        print("**Hit Points** ?? (" + str(self.hitdicedesc()) + ")") # Need to incorporate CON bonus later
        print("")
        print("**Speed** " + self.speed)
        print("")
        print("**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**")
        print("-------|-------|-------|-------|-------|-------")
        print(str(self.STR) + " | " + str(self.DEX) + " | " + str(self.CON) + " | " + str(self.INT) + " | " + str(self.WIS) + " | " + str(self.CHA))
        print("")
        print("**Saving Throws** " + ", ".join(self.savingthrows))
        print("")
        print("**Skills** " + ", ".join(self.skills))
        print("")
        print("**Senses** ")
        print("")
        print("**Languagess** " + ", ".join(self.languages))
        print("")
        for feature in self.features:
            print(feature)
            print("")
        print("#### Actions")
        for action in self.actions:
            print(action)
        print("")
        print("#### Bonus Actions")
        for action in self.bonusactions:
            print(action)
        print("")
        print("#### Reactions")
        for action in self.reactions:
            print(action)
        print("----")
        print('\n'.join(self.description))

class Race:
    def __init__(self):
        pass

# Be nice if there was a way to get race/class modules to be able to share
# a common pool of common features, but there's probably some scoping mechanism
# that needs to be sorted to make that work. Right now hobgoblin.py can't see
# `features`, so maybe try to figure that out in the future.
features = {
    'amphibious' : "**Amphibious**. You can breathe air and water.",
    'darkvision' : "**Darkvision**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."
}

def subclassload(dirname):
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

def choose(text, choices):
    """Present a list of choices to the engine for selection"""
    print(text)
    if isinstance(choices, list):
        choiceidx = 0
        for c in choices:
            choiceidx += 1
            print(f'{choiceidx}: {c}')

        response = None
        while response == None:
            response = input(">>> ")
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choices):
                response = None

        response = int(response) - 1 # Account for zero-based index
        return choices[response]
    elif isinstance(choices, dict):
        choiceidx = 0
        for c in choices.items():
            choiceidx += 1
            print(f'{choiceidx}: {c[0]}: {c[1]}')

        response = None
        while response == None:
            response = input(">>> ")
            if not response.isnumeric:
                response = None
            if int(response) < 1:
                response = None
            if int(response) > len(choices):
                response = None

        responseidx = int(response) - 1 # Account for zero-based index
        responsekey = list(choices.keys())[responseidx]
        print(responsekey, choices[responsekey])
        return (responsekey, choices[responsekey])
    else:
        raise BaseException('Unrecognized type of choices: ' + str(type(choices)))

def levelinvoke(module, level, npc):
    levelfn = getattr(module, 'level' + str(level))
    if levelfn == None:
        print("No level function found for " + module + " for level " + str(level))
    levelfn(npc)

def abilityscoreimprovement(npc):
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    abilityidx = choose("Improve an ability score by 1:", abilities)
    ability = abilities[abilityidx]
    newvalue = int(getattr(npc, ability)) + 1
    setattr(npc, ability, newvalue)
    abilityidx = choose("Improve an ability score by 1:", abilities)
    ability = abilities[abilityidx]
    newvalue = int(getattr(npc, ability)) + 1
    setattr(npc, ability, newvalue)

def feat(npc):
    pass

def populateModule(module):
    module.features = features
    module.replace = replace
    module.choose = choose
    module.subclassload = subclassload
    module.levelinvoke = levelinvoke

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
    return results

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

def main():
    npc = NPC()

    # What do we do for ability scores? Hand entry, random gen, weighted average, ...?
    # TODO: DO a choose(...) against the different strategies, each of which is a function, then execute that
    print("Ability scores:")

    def handentry(npc):
        npc.STR = int(input("  STR: "))
        npc.DEX = int(input("  DEX: "))
        npc.CON = int(input("  CON: "))
        npc.INT = int(input("  INT: "))
        npc.WIS = int(input("  WIS: "))
        npc.CHA = int(input("  CHA: "))
    handentry(npc)

    # Load all races into the array
    races = loadraces()
    race = races[choose("Choose race:", list(races.keys()))]
    race.apply_race(npc)
    if len(race.subraces) > 0:
        subrace = choose("Choose subrace:", race.subraces)
        race.apply_subrace(subrace, npc)

    # Load all classes into the array
    classes = loadclasses()
    level = 0
    levelup = True
    while levelup == True:
        level += 1
        clss = classes[choose("Choose class:", list(classes.keys()))]

        # TODO: For multiclassing, we need to get the level of JUST the chosen class
        # not the total levels of the NPC.

        #(getattr(clss, 'level' + str(level)))(npc)
        levelinvoke(clss, level, npc)
        levelup = (input(">>> Currently level " + str(level) + "; Another level? ") == 'y')

    npc.print_markdown()

def oldmain():
    parser = argparse.ArgumentParser(
                    prog='NPCGen',
                    description='A tool for generating 5th-ed NPCs')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # Input commands
    #parser.add_argument('--class', help='Class to generate')
    #parser.add_argument('--subclass', help='Subclass to generate')
    #parser.add_argument('--race', help='Race to generate')
    #parser.add_argument('--subrace', help='Subrace to generate')
    #parser.add_argument('--level', help='Level to generate to')

    # Process arguments
    args = parser.parse_args()
    print(vars(args))



if __name__ == '__main__':
	main()
