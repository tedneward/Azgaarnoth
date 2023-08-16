#!/usr/bin/env python3

# Tool to normalize Creature stat blocks

from enum import Enum
import argparse
import xml.etree.ElementTree as etree
import os
import sqlite3
import sys

# These sorts of creature entries are typically for a collection of such; the
# "Troll" entry, for example, contains "Troll", "Aquatic Troll", "Rot Troll",
# and so on.
class SubtypedCreature:
     def __init__(self):
        self.name = ''
        self.subtypes = []
        self.generaldescription = ''

# A creature entry.
class Creature:
    class Size(Enum):
        TINY = 'Tiny',
        SMALL = 'Small',
        MEDIUM = 'Medium',
        LARGE = 'Large',
        HUGE = 'Huge',
        GARGANTUAN = 'Gargantuan'

    class Type(Enum):
        ELEMENTAL = 'elemental',
        FEY = 'fey',
        FIEND = 'fiend'
        HUMANOID = 'humanoid',
        UNDEAD = 'undead'

    def __init__(self):
        self.name = ''
        self.size = Creature.Size.MEDIUM
        self.type = Creature.Type.HUMANOID
        self.alignment = ''
        self.description = []
        self.ac = ''
        self.hp = ''
        self.speed = ''
        self.STR = 10
        self.DEX = 10
        self.CON = 10
        self.INT = 10
        self.WIS = 10
        self.CHA = 10
        self.profbonus = 0
        self.savingthrows = []
        self.dmgvuls = []
        self.dmgresists = []
        self.dmgimmunes = []
        self.condimmunes = []
        self.skills = []
        self.senses = []
        self.languages = []
        self.cr = 0
        self.features = []
        self.actions = []
        self.bonusactions = []
        self.reactions = []

    def abilitybonus(self, score):
        return (score / 2) - 5

    def abilitytext(self, score):
        return f"{score} ({self.abilitybonus(score):+g})"

    def parseMD(self, mdlines):
        "Parse a list of strings that contain well-formed Markdown"
        pass

    def parserow(self, sqlrow):
        "Parse a row from a SQLite cursor"
        pass

    def emitMD(self):
        "Emit this creature description and stat block"

        linebreak = ">___\n"

        result  = ""
        #result += f"## {self.name}"
        #result += "\n\n".join(self.description)
        result += f">### {self.name}\n"
        result += f">*{self.size} {self.type}, {self.alignment}*"
        result += linebreak
        result += f">- **Armor Class** {self.ac}\n"
        result += f">- **Hit Points** {self.hp}\n"
        result += f">- **Speed** {self.speed}\n"
        result += linebreak
        result +=  ">|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|\n"
        result +=  ">|:---:|:---:|:---:|:---:|:---:|:---:|\n"
        result += f">|{self.abilitytextself.STR}|{self.abilitytextself.DEX}|{self.abilitytextself.CON}|"
        result += f"{self.abilitytextself.INT}|{self.abilitytextself.WIS}|{self.abilitytextself.CHA}|\n"
        result +=  ">\n"
        result += linebreak
        result += f">- **Proficiency Bonus** {self.profbonus}\n"
        result += f">- **Saving Throws** {','.join(self.savingthrows)}\n"
        result += f">- **Damage Vulnerabilities** {','.join(self.dmgvuls)}\n"
        result += f">- **Damage Resistances** {','.join(self.dmgresists)}\n"
        result += f">- **Damage Immunities** {','.join(self.dmgimmunes)}\n"
        result += f">- **Condition Immunities** {','.join(self.condimmunes)}\n"
        result += f">- **Skills** {','.join(self.skills)}\n"
        result += f">- **Senses** {','.join(self.senses)}\n"
        result += f">- **Languages** {','.join(self.languages)}\n"
        result += f">- **Challenge** {self.cr}\n" 
        result += linebreak
        result += ">\n>\n".join(self.features)   
        result +=  ">\n"
        result +=  ">#### Actions\n"
        result += ">\n>\n".join(self.actions)   

        return result

def ingest(arg):
    # Recursively ingest if arg is a directory
    if os.path.isdir(arg):
        files = os.listdir(arg)
        for f in files:
            if os.path.isfile(arg + '/' + f):
                ext = str(f)[-4:]
                if ext.lower() != '.png' and ext.lower() != '.jpg':
                    ingest(arg + '/' + f)
        return

    def ingestrawtextfile(lines):
        pass

    def ingestmymdformat(lines):
        pass

    # Arg is a file
    print(f"Ingesting file {arg}")
    with open(arg, 'r') as argfile:
        lines = argfile.readlines()


def main(argv):
    parser = argparse.ArgumentParser(
                    prog='CreaTool',
                    description='A creature list(s) and contents tool',
                    epilog='Text at the bottom of help')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--parsemd', help='Source directory of MD files to use')
    parser.add_argument('--parsesql', help='Source SQLite database to use')
    parser.add_argument('--testmd', help='Use test Creature')
    parser.add_argument('--ingest', help='File(s) to import into the set')
    parser.add_argument('--lint', help='Warn about non-normalized data')
    #parser.add_argument('--filter', help='Filter the source set') # When I figure out an expression language to use
    parser.add_argument('--filtercr', help='Filter by Challenge Rating')
    parser.add_argument('--writeindex', help='Write out an index of the creatures')
    parser.add_argument('--writemd', help='Target directory for MD files to be emitted')
    args = parser.parse_args()

    creatures = []
    if args.parsemd != None:
        # Parse MD files
        pass
    elif args.parsesql != None:
        # Parse SQLite db
        pass
    elif args.testmd != None:
        creature = Creature()
        creature.name = 'Testit'
        creature.size = Creature.Size.MEDIUM
        creature.type = Creature.Type.FEY
        creature.alignment = 'neutral'
        creature.ac = '15 (natural armor)'
        creature.hp = '135 (12d10 + 35)'
    else:
        print("No source set specified!")

    # Filter?

    # Ingest?
    if args.ingest != None:
        ingest(args.ingest)
    else:
        parser.print_help()

    # Store?

if __name__ == '__main__':
	main(sys.argv)
