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
    def __init__(self):
        self.name = ''
        self.size = ''
        self.type = ''
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
        self.legendaryactions = []
        self.lairactions = []

    def abilitybonus(self, score):
        return (score // 2) - 5

    def abilitytext(self, score):
        return f"{score} ({self.abilitybonus(score):+g})"

    def parseMD(self, mdlines):
        "Parse a list of strings that contain well-formed Markdown"
        pass

    def parserow(self, sqlrow):
        "Parse a row from a SQLite cursor"
        pass

    def titleify(self, items, prefix='>'):
        results = ''
        for item in items:
            line = item.strip()

            if '.' in line:
                firstdot = line.index('.')
                if firstdot < 35:
                    title = '***' + line[0:firstdot] + '.***'
                    text = line[firstdot:]
                    results += prefix + title + text
                else:
                    results += prefix + line
            else:
                results += prefix + line

            results += '\n'
            results += prefix + '\n'

        return results

    def emitMD(self):
        "Emit this creature description and stat block"

        linebreak = ">___\n"

        result  = ""
        result += f"## {self.name}\n"
        if len(self.description) > 0:
            result += self.titleify(self.description, '')
        else:
            result += '\n'
        result += f">### {self.name}\n"
        result += f">*{self.size} {self.type}, {self.alignment}*\n"
        result += linebreak
        result += f">- **Armor Class** {self.ac}\n"
        result += f">- **Hit Points** {self.hp}\n"
        result += f">- **Speed** {self.speed}\n"
        result += linebreak
        result +=  ">|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|\n"
        result +=  ">|:---:|:---:|:---:|:---:|:---:|:---:|\n"
        result += f">|{self.abilitytext(self.STR)}|{self.abilitytext(self.DEX)}|{self.abilitytext(self.CON)}|"
        result += f"{self.abilitytext(self.INT)}|{self.abilitytext(self.WIS)}|{self.abilitytext(self.CHA)}|\n"
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
        result += self.titleify(self.features)
        result += ">#### Actions\n" + self.titleify(self.actions)
        if len(self.bonusactions) > 0:
            result +=  ">#### Bonus Actions\n" + self.titleify(self.bonusactions)
        if len(self.reactions) > 0:
            result +=  ">#### Reactions\n" + self.titleify(self.reactions)
        if len(self.legendaryactions) > 0:
            result +=  ">#### Legendary Actions\n" + self.titleify(self.legendaryactions)

        return result

creatures = []

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

    def ingestrawstatblock(lines):
        creature = Creature()

        creature.name = lines[0].lower().strip().title()
        (sizeandtype, alignment) = lines[1].split(',')
        creature.alignment = alignment.strip()
        creature.size = sizeandtype.split(' ')[0]
        creature.type = sizeandtype.split(' ')[1]

        creature.ac = lines[3][len('Armor Class '):].strip()

        creature.hp = lines[5][len('Hit Points '):].strip()

        creature.speed = lines[7][len('Speed '):].strip()

        creature.STR = int(lines[10].split('(')[0])
        creature.DEX = int(lines[12].split('(')[0])
        creature.CON = int(lines[14].split('(')[0])
        creature.INT = int(lines[16].split('(')[0])
        creature.WIS = int(lines[18].split('(')[0])
        creature.CHA = int(lines[20].split('(')[0])

        linect = 21
        while linect < len(lines):
            if 'Damage Vulnerabilities' in lines[linect]:
                dvs = lines[linect][len('Damage Vulnerabilities '):].split(',')
                for dv in dvs:
                    creature.dmgvuls.append(dv.strip())

            elif 'Damage Resistances' in lines[linect]:
                drs = lines[linect][len('Damage Resistances '):].split(',')
                for dr in drs:
                    creature.dmgresists.append(dr.strip())

            elif 'Damage Immunities' in lines[linect]:
                dis = lines[linect][len('Damage Immunities '):].split(',')
                for di in dis:
                    creature.dmgimmunes.append(di.strip())

            elif 'Condition Immunities' in lines[linect]:
                cis = lines[linect][len('Condition Immunities '):].split(',')
                for ci in cis:
                    creature.condimmunes.append(ci.strip())

            elif 'Saving Throws' in lines[linect]:
                saves = lines[linect][len('Saving Throws '):].split(',')
                for st in saves:
                    creature.savingthrows.append(st.strip())

            elif 'Skills' in lines[linect]:
                skills = lines[linect][len('Skills '):].split(',')
                for sk in skills:
                    creature.skills.append(sk.strip())

            elif 'Senses' in lines[linect]:
                senses = lines[linect][len('Senses '):].split(',')
                for sn in senses:
                    creature.senses.append(sn.strip())

            elif 'Languages' in lines[linect]:
                langs = lines[linect][len('Languages '):].split(',')
                for l in langs:
                    creature.languages.append(l.strip())

            elif 'Challenge' in lines[linect]:
                creature.cr = lines[linect][len('Challenge '):].split(' ')[0].strip()

            elif 'Actions' in lines[linect]:
                break

            else:
                creature.features.append(lines[linect])

            linect += 2

        # Now we're in to Actions
        while linect < len(lines):
            line = lines[linect].strip()
            if 'Legendary' == line[0:len('Legendary')]:
                break
            elif 'Actions' == line[0:len('Actions')]:
                linect += 2
                continue
            elif 'Reactions' == line[0:len('Reactions')]:
                break
            else:
                creature.actions.append(lines[linect].strip())

            linect += 2

        # Now we're in to Legendary Actions
        while linect < len(lines):
            line = lines[linect].strip()
            if 'Legendary' == line[0:len('Legendary')]:
                linect += 2
                continue
            else:
                creature.legendaryactions.append(lines[linect].strip())

            linect += 2

        return creature

    def ingestrawtextfile(lines):
        name = lines[0]
        description = []

        linect = 1
        while lines[linect] != name.upper():
            if len((lines[linect]).strip()) > 0:
                description.append(lines[linect])
            linect += 1

        creature = ingestrawstatblock(lines[linect:])
        creature.name = name.strip()
        creature.description = description
        return creature
    
    def ingestdndbeyondwebp(lines):
        creaturelist = []
        currentcreature = None

        # Creature descriptions start on lines starting with '<h2 class="compendium-hr heading-anchor"
        # and the name is in the 'id' (id="Aarakocra") attribute
        h2line = '<h2 class="compendium-hr heading-anchor"'
        linect = 0
        while linect < len(lines):
            line = lines[linect]

            if line[0:len(h2line)] == h2line:
                # Starting a new creature!
                if currentcreature != None:
                    creaturelist.append(currentcreature)
                currentcreature = Creature()

                creaturename = line[len(h2line) + len(' id="'):]
                currentcreature.name = creaturename[0:creaturename.index('"')]

            linect += 1

        creaturelist.append(currentcreature)
        print(creaturelist)
        return creaturelist


    def ingestmymdformat(lines):
        pass

    # Arg is a file
    with open(arg, 'r') as argfile:
        lines = argfile.readlines()
        if len(lines) < 1:
            print(f"Empty file: {arg}")
        elif lines[0] == '<!DOCTYPE html>\n':
            # We are going to parse a DnD Beyond page, let's go!
            cs = ingestdndbeyondwebp(lines)
        elif lines[0].upper() == lines[0]:
            # Guessing this is a stat block
            creatures.append(ingestrawstatblock(lines))
        else:
            # Maybe this is a longer-form description?
            creatures.append(ingestrawtextfile(lines))

def snakecaseify(string):
    return string.lower().replace(' ', '-')

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
        creature.senses.append('darkvision 60ft')

        creature.STR = 20
        creature.CON = 15
        creature.DEX = 7
        creature.INT = 3
        creature.WIS = 9
        creature.CHA = 10

        creatures.append(creature)
    else:
        print("No source set specified!")

    # Filter?

    # Ingest?
    if args.ingest != None:
        ingest(args.ingest)

    # Store?
    if args.writemd != None:
        dest = args.writemd
        if dest == '-':
            for creature in creatures:
                print(creature.emitMD())
        elif os.path.isdir(dest):
            for creature in creatures:
                with open(snakecaseify(creature.name).title() + ".md", 'w') as mdfile:
                    mdfile.write(creature.emitMD())
    else:
        parser.print_help()

if __name__ == '__main__':
	main(sys.argv)
