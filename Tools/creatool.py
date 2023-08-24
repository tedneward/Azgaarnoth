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
        self.generaldescription = []

    def emitMD(self):
        def linkify(string):
            return '#' + string.replace('/','').replace(' ','-').lower()
        
        subtypejumplinks = " | ".join(map(lambda st: f'[{st.name}]({linkify(st.name)})', self.subtypes))

        results  =  ''
        results += f'# {self.name}\n'
        results += self.generaldescription[0] + '\n'
        results += '\n'
        results += '> Jump to: ' + subtypejumplinks + '\n'
        results += '\n'.join(self.generaldescription[1:])
        for creature in self.subtypes:
            results += '---\n\n'
            results += creature.emitMD()
            results += '\n'
        return results

# A creature entry.
class Creature:
    class TitledText:
        def __init__(self):
            self.title = ''
            self.text = ''

        def __str__(self) -> str:
            return f'***{self.title}.*** {self.text}'
        
        def parse(self, line):
            self.title = ''
            self.text = ''
        
    class Lair:
        def __init__(self):
            self.description = ''
            self.lairactions = []
            self.regionalprefix = ''
            self.regionaleffects = []
            self.regionalpostfix = ''

    def __init__(self):
        self.name = ''
        self.size = ''
        self.type = ''
        self.subtypes = []
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
        self.lair = None

    def abilitybonus(self, score):
        return (score // 2) - 5

    def abilitytext(self, score):
        return f"{score} ({self.abilitybonus(score):+g})"

    def parseMD(self, mdlines):
        "Parse a list of strings that contain well-formed Markdown"
        if mdlines[0][0,1] == '# ':
            # This is a multi-creature file
            subtypedcreature = SubtypedCreature()

            # Start by parsing the SubtypedCreature description text

            # Now loop through the rest of the file, breaking on the '---' breaks
            # and parse each one as a separate creature

            #return subtypedcreature
            print("I CAN'T PARSE MULTI_CREATURE FILES YET SORRY")
        elif mdlines[0][0,1] == '##':
            # This is a single-creature file
            return self.parseSingleCreatureMD(mdlines)

    def parseSingleCreatureMD(self, mdlines):
        "Parse a list of strings that contain well-formed Markdown containing a single creature"

        linect = 0
        self.name = mdlines[linect].replace('#', '').strip()
        print(self.name)

        while linect < len(mdlines):
            line = mdlines[linect].strip()

            if line[0:5] == '>### ':
                break
            else:
                if len(line) > 0:
                    self.description.append(mdlines[linect])
                linect += 1

        # name
        line = mdlines[linect]
        print("Name: " + line)
        linect += 1

        # size type (optional-subtype, optional-subtype, ...), alignment
        # TODO: Handle multiple subtypes someday
        line = mdlines[linect][1:].strip().replace('*', '')
        (sizetype, alignment) = line.split(',')
        self.alignment = alignment.strip()
        size = sizetype[0:sizetype.index(' ')]
        ctype = sizetype[sizetype.index(' '):]
        self.size = size.strip()
        self.type = ctype.strip()
        linect +=1

        # >___
        linect += 1

        # Armor Class
        line = mdlines[linect]
        print("AC: " + line)
        self.ac = line[len('>- **Armor Class** '):].strip()
        linect += 1

        # Hit Points
        line = mdlines[linect]
        print("HP: " + line)
        self.hp = line[len('>- **Hit Points** '):].strip()
        linect += 1

        # Speed
        line = mdlines[linect]
        print("Spd: " + line)
        self.speed = line[len('>- **Speed** '):].strip()
        linect += 1

        # >___
        # >Stat block headers
        # >Stat block table row divider
        # >Stat block
        # >
        # >___
        # >Prof Bonus
        # >Saving Throws
        # >Dmg Vul
        # >Dmg Res
        # >Dmg Imm
        # >Cond Imm
        # >Skills
        # >Senses
        # >Langs
        # >CR
        # >Features -> Actions -> Bonus Actions? -> Reactions? -> Lair Actions? -> Legendary Actions?
        # ### A {name}'s Lair
        # Lair-description
        # #### Lair Actions
        # * Action
        # #### Regional Effects
        # Regionalpretext
        # * Effect
        # Regionalposttext

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

        if len(self.subtypes) > 0:
            result += f">*{self.size} {self.type} ({','.join(self.subtypes)}), {self.alignment}*\n"
        else:
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
        if isinstance(self.profbonus, str):
            result += f">- **Proficiency Bonus** {self.profbonus}\n"
        elif isinstance(self.profbonus, int):
            result += f">- **Proficiency Bonus** {self.profbonus:+g}\n"
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

        if self.lair != None:
            result += '\n'
            result += f"### A {self.name}'s Lair\n"
            result += self.lair.description + '\n'
            result += "\n#### Lair Actions\n"
            result += "\n* ".join(self.lair.lairactions)
            result += "\n#### Regional Effects\n"
            result += self.lair.regionalprefix
            result += "\n* ".join(self.lair.regionaleffects)
            result += self.lair.regionalpostfix
            result += "\n"

        return result



######################################################################

creatures = []

def ingest(arg):
    def cleanup(line):
        if line.find(u"“") > 0:
            print("I HATE SMART QUOTES!!!!")

        utf8s = "“”‘’‹›«»−–"
        repls = "\"\"''''\"\"--"
        transl_table = dict( [ (ord(x), ord(y)) for x,y in zip( utf8s,  repls) ] ) 

        # Get rid of the damn smart quotes
        result = line.translate( transl_table)
        result = result.strip()
        return result
    
    # Recursively ingest if arg is a directory
    if os.path.isdir(arg):
        files = os.listdir(arg)
        for f in files:
            if os.path.isfile(arg + '/' + f):
                ext = str(f)[-4:].lower()
                if ext != '.png' and ext != '.jpg' and ext != 'webp':
                    ingest(arg + '/' + f)
        return

    def ingestrawstatblock(lines):
        creature = Creature()

        # Parse name line
        linect = 0
        creature.name = lines[linect].lower().strip().title()

        # Parse size type (subtype(s)), alignment line
        linect += 1
        def parsesecondline(line):
            size = ''
            type = ''
            subtypes = []
            alignment = ''

            if line.find('(') > 0:
                # It has a parenthesized subtype
                # Find the parenthesized string and split there
                endparen = line.find(')')
                sizeandtype = line[0:endparen+1]
                # Fnd the paren in the new sizeandtype string
                startparen = line.find('(')
                endparen = line.find(')')
                sizeandtype = line[0:startparen]
                subtype = line[startparen+1:endparen]
                size = sizeandtype.split(' ')[0]
                type = sizeandtype.split(' ')[1]
                subtypes = subtype.split(',')
                alignment = line[endparen+3:].strip()
            else:
                (sizeandtype, alignment) = line.split(',')
                alignment = alignment.strip()
                size = sizeandtype.split(' ')[0]
                type = sizeandtype.split(' ')[1]

            return (size, type, subtypes, alignment)
        (creature.size, creature.type, creature.subtypes, creature.alignment) = parsesecondline(lines[linect])

        # Start parsing AC, HP, Speed, attributes
        linect += 1
        while linect < len(lines):
            line = cleanup(lines[linect])

            # Just blow past empty lines
            if len(line) < 1:
                linect += 1
                continue

            print("Examining line '" + line + "'")

            if 'Armor Class ' in line:
                creature.ac = line[len('Armor Class '):].strip()
            elif 'Hit Points ' in line:
                creature.hp = line[len('Hit Points '):].strip()
            elif 'Speed ' in line:
                creature.speed = line[len('Speed '):].strip()

            # Ability scores
            # Are they all on one line?
            elif ('STR' in line) and ('INT' in line):
                linect += 1
                line = lines[linect]
                groupofsix = line.split(')')
                creature.STR = int(groupofsix[0].strip().split(' ')[0])
                creature.DEX = int(groupofsix[1].strip().split(' ')[0])
                creature.CON = int(groupofsix[2].strip().split(' ')[0])
                creature.INT = int(groupofsix[3].strip().split(' ')[0])
                creature.WIS = int(groupofsix[4].strip().split(' ')[0])
                creature.CHA = int(groupofsix[5].strip().split(' ')[0])

            # The scores are on successive lines
            elif 'STR' in line:
                linect += 1 # Next line holds the score
                creature.STR = int(lines[linect].split('(')[0])
            elif 'DEX' in line:
                linect += 1 # Next line holds the score
                creature.DEX = int(lines[linect].split('(')[0])
            elif 'CON' in line:
                linect += 1 # Next line holds the score
                creature.CON = int(lines[linect].split('(')[0])
            elif 'INT' in line:
                linect += 1 # Next line holds the score
                creature.INT = int(lines[linect].split('(')[0])
            elif 'WIS' in line:
                linect += 1 # Next line holds the score
                creature.WIS = int(lines[linect].split('(')[0])
            elif 'CHA' in line:
                linect += 1 # Next line holds the score
                creature.CHA = int(lines[linect].split('(')[0])

            elif 'Damage Vulnerabilities' in line:
                dvs = line[len('Damage Vulnerabilities '):].split(',')
                for dv in dvs:
                    creature.dmgvuls.append(cleanup(dv))

            elif 'Damage Resistances' in line:
                drs = line[len('Damage Resistances '):].split(',')
                for dr in drs:
                    creature.dmgresists.append(cleanup(dr))

            elif 'Damage Immunities' in line:
                dis = line[len('Damage Immunities '):].split(',')
                for di in dis:
                    creature.dmgimmunes.append(cleanup(di))

            elif 'Condition Immunities' in line:
                cis = line[len('Condition Immunities '):].split(',')
                for ci in cis:
                    creature.condimmunes.append(cleanup(ci))

            elif 'Saving Throws' in line:
                saves = line[len('Saving Throws '):].split(',')
                for st in saves:
                    creature.savingthrows.append(cleanup(st))

            elif 'Skills' in line:
                skills = line[len('Skills '):].split(',')
                for sk in skills:
                    creature.skills.append(sk.strip())

            elif 'Senses' in line:
                senses = line[len('Senses '):].split(',')
                for sn in senses:
                    creature.senses.append(sn.strip())

            elif 'Languages' in line:
                langs = line[len('Languages '):].split(',')
                for l in langs:
                    creature.languages.append(l.strip())

            elif ('Challenge' in line) and ('Proficiency Bonus' in line):
                creature.cr = line[len('Challenge '):line.find('Proficiency Bonus')].split(' ')[0].strip()
                # Find start of Proficiency Bonus in line
                pb = line[line.find('Proficiency Bonus '):]
                creature.profbonus = pb[len('Proficiency Bonus '):].strip()

            elif 'Challenge' in line:
                creature.cr = line[len('Challenge '):].split(' ')[0].strip()

            elif 'Proficiency Bonus' in line:
                creature.profbonus = line[:len('Proficiency Bonus ')].strip()

            elif ('Actions' in line) or ('Action' in line):
                break

            else:
                creature.features.append(line)

            linect += 1

        # Now we're in to Actions
        block = ''
        while linect < len(lines):
            line = cleanup(lines[linect])
            if len(line) == 0:
                linect += 1
                continue

            print("Examining '" + line + "'")

            if 'Legendary' == line[0:len('Legendary')]:
                block = 'legendary'
            elif 'Action' == line[0:len('Action')]:
                block = 'actions'
            elif 'Actions' == line[0:len('Actions')]:
                block = 'actions'
            elif 'Bonus Actions' == line[0:len('Bonus Actions')]:
                block = 'bonusactions'
            elif 'Reactions' == line[0:len('Reactions')]:
                block = 'reactions'
            elif line.find('Lair') > 0:
                block = 'lair'
                creature.lair = Creature.Lair()
            elif 'Lair Actions' == line[0:len('Lair Actions')]:
                block = 'lairactions'
            elif 'Regional Effects' == line[0:len('Regional Effects')]:
                block = 'laireffects'
            else:
                if block == 'actions': creature.actions.append(line)
                elif block == 'reactions': creature.reactions.append(line)
                elif block == 'bonusactions': creature.bonusactions.append(line)
                elif block == 'legendary': creature.legendaryactions.append(line)
                elif block == 'lair': creature.lair.description += line
                elif block == 'lairactions': creature.lair.lairactions.append(line)
                elif block == 'laireffects': creature.lair.regionaleffects.append(line)
                else:
                    print("WTF?!? Unrecognized block! '" + block + "'")

            linect += 1

        return creature

    def ingestrawtextfile(lines):
        def ingestsinglecreature(lines):
            # Eat any blank lines
            while (len(lines) > 0) and (len(lines[0].strip()) == 0):
                del lines[0]

            name = lines[0]
            print("INGESTING CREATURE " + name)
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

        def ingestsubtypedcreature(lines):
            subtypedcreature = SubtypedCreature()

            # Eat any blank lines
            while len(lines[0].strip()) == 0:
                del lines[0]
            subtypedcreature.name = lines[0].strip()
            print("INGESTING SUBTYPED CREATURE " + subtypedcreature.name + "--->")
            del lines[0]

            while lines[0].strip() != '---':
                subtypedcreature.generaldescription.append(cleanup(lines[0]))
                del lines[0]

            del lines[0:1]

            while lines.count('---\n') > 0:
                breakline = lines.index('---\n')
                subtypedcreature.subtypes.append(ingestsinglecreature(lines[0:breakline]))
                del lines[0:breakline+1]
            
            subtypedcreature.subtypes.append(ingestsinglecreature(lines))
            print("<---")
            return subtypedcreature

        def ingestmultiplecreatures(lines):
            print("INGESTING MULTIPLE CREATURES>>>>")
            crs = []
            while lines.count('===\n') > 0:
                # This is a multiple-creatures file
                breakline = lines.index('===\n')
                crs.append(ingestrawtextfile(lines[0:breakline]))
                del lines[0:breakline+1]

            if lines.count('---\n') > 0:
                crs.append(ingestsubtypedcreature(lines))
            else:
                crs.append(ingestsinglecreature(lines))
            print("<<<<")
            return crs

        # Let's look to see if this is a multi-creature file
        # I put === lines to demarcate between multiple creatures in one file
        # I put --- lines to demarcate between related creatures in one file
        if lines.count('===\n') > 0:
            return ingestmultiplecreatures(lines)
        elif lines.count('---\n') > 0:
            return ingestsubtypedcreature(lines)
        else:
            return ingestsinglecreature(lines)
    
    def ingestmymdformat(lines):
        if lines[3][0:len('**Armor Class**')] != '**Armor Class**':
            # This is one of my multi-statblock formats
            print("I can't support multi-statblock formats yet")
            pass
        else:
            # This is one creature
            creature = Creature()

            creature.name = lines[0][2:].strip().title()
            (sizeandtype, alignment) = lines[1][1:-2].split(',')
            creature.alignment = alignment.strip()
            creature.size = sizeandtype.split(' ')[0]
            # TODO: type might have parens in it, eg "Large humanoid (goblin)"
            creature.type = sizeandtype.split(' ')[1]

            creature.ac = lines[3][len('**Armor Class** '):].strip()
            creature.hp = lines[5][len('**Hit Points** '):].strip()
            creature.speed = lines[7][len('**Speed** '):].strip()

            abilities = lines[11].split('|')
            creature.STR = int(abilities[0].split('(')[0])
            creature.DEX = int(abilities[1].split('(')[0])
            creature.CON = int(abilities[2].split('(')[0])
            creature.INT = int(abilities[3].split('(')[0])
            creature.WIS = int(abilities[4].split('(')[0])
            creature.CHA = int(abilities[5].split('(')[0])

            linect = 13
            while linect < len(lines):
                line = lines[linect].strip()
                if len(line) == 0:
                    pass
                elif '**Damage Vulnerabilities**' in line:
                    dvs = line[len('**Damage Vulnerabilities** '):].split(',')
                    for dv in dvs:
                        creature.dmgvuls.append(dv.replace('*', '').strip())
                elif '**Proficiency Bonus**' in line:
                    creature.profbonus = int(line[len('**Proficiency Bonus** '):])
                elif '**Damage Resistances**' in line:
                    drs = line[len('**Damage Resistances** '):].split(',')
                    for dr in drs:
                        creature.dmgresists.append(dr.strip())
                elif '**Damage Immunities**' in line:
                    dis = line[len('**Damage Immunities** '):].split(',')
                    for di in dis:
                        creature.dmgimmunes.append(di.strip())
                elif '**Condition Immunities**' in line:
                    cis = line[len('**Condition Immunities** '):].split(',')
                    for ci in cis:
                        creature.condimmunes.append(ci.strip())
                elif '**Saving Throws**' in line:
                    saves = line[len('**Saving Throws** '):].split(',')
                    for st in saves:
                        creature.savingthrows.append(st.strip())
                elif '**Skills**' in line:
                    skills = line[len('**Skills** '):].split(',')
                    for sk in skills:
                        creature.skills.append(sk.strip())
                elif '**Senses**' in line:
                    senses = line[len('**Senses** '):].split(',')
                    for sn in senses:
                        creature.senses.append(sn.strip())
                elif '**Languages**' in line:
                    langs = line[len('**Languages** '):].split(',')
                    for l in langs:
                        creature.languages.append(l.strip())
                elif '**Challenge**' in line:
                    creature.cr = line[len('**Challenge** '):].split(' ')[0].strip()
                elif '# Actions' in line:
                    break

                else:
                    creature.features.append(line.replace('*', ''))

                linect += 1

            # Now we're in to Actions/Reactions/Bonus Actions/Legendary Actions/Description
            # blocks, so this gets interesting
            block = ''
            while linect < len(lines):
                line = lines[linect].strip()
                if len(line) == 0:
                    linect += 1
                    continue

                if '## Description' == line[0:len('## Description')]:
                    block = 'description'
                elif '#### Description' == line[0:len('#### Description')]:
                    block = 'description'
                elif '#### Legendary' == line[0:len('#### Legendary')]:
                    block = 'legendary'
                elif '## Actions' == line[0:len('#### Actions')]:
                    block = 'actions'
                elif '#### Actions' == line[0:len('#### Actions')]:
                    block = 'actions'
                elif '#### Reactions' == line[0:len('Reactions')]:
                    block = 'reactions'
                elif '#### Bonus Actions' == line[0:len('#### Actions')]:
                    block = 'bonusactions'
                else:
                    text = line.replace('*', '')
                    if block == 'actions': creature.actions.append(text)
                    elif block == 'reactions': creature.reactions.append(text)
                    elif block == 'bonusactions': creature.bonusactions.append(text)
                    elif block == 'legendary': creature.legendaryactions.append(text)
                    elif block == 'description': creature.description.append(text)
                    else:
                        print("WTF?!? Unrecognized block! " + block)

                linect += 1

            return creature

    # Arg is a file
    with open(arg, 'r', errors='ignore', encoding='utf-8') as argfile:
        lines = argfile.readlines()

        if len(lines) < 1:
            print(f"Empty file: {arg}")

        linect = 0
        while linect < len(lines):
            if lines[linect].find(u"“") > 0:
                line = lines[linect].replace(u"“", '"')
                lines[linect] = line
            if lines[linect].find(u"”") > 0:
                line = lines[linect].replace(u"”", '"')
                lines[linect] = line
            if lines[linect].find(u"’") > 0:
                line = lines[linect].replace(u"’", "'")
                lines[linect] = line
            if lines[linect].find(u"—") > 0:
                line = lines[linect].replace(u"—", "--")
                lines[linect] = line
            linect += 1

        if lines[0][0:2] == '# ':
            # Might be one of my original MD formats
            creatures.append(ingestmymdformat(lines))
#        elif lines[0] == '<!DOCTYPE html>\n':
#            # We are going to parse a DnD Beyond page, let's go!
#            cs = ingestdndbeyondwebp(lines)
        elif lines[0].upper() == lines[0]:
            # Guessing this is a stat block
            creatures.append(ingestrawstatblock(lines))
        else:
            # Maybe this is a longer-form description?
            result = ingestrawtextfile(lines)
            if isinstance(result, list):
                for c in result:
                    creatures.append(c)
            else:
                creatures.append(result)

def camelcaseify(string):
    return string.lower().replace(' ', '')

def main(argv):
    parser = argparse.ArgumentParser(
                    prog='CreaTool',
                    description='A creature list(s) and contents tool',
                    epilog='Text at the bottom of help')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    # Source sets
    parser.add_argument('--parsemd', help='Source directory of MD files to use')
    parser.add_argument('--parsesql', help='Source SQLite database to use')
    # Ingestion
    parser.add_argument('--ingest', help='File(s) to import into the set')
    # Linting/normalizing
    parser.add_argument('--lint', help='Warn about non-normalized data')
    # Filter the current set by one or more options
    #parser.add_argument('--filter', help='Filter the source set') # When I figure out an expression language to use
    parser.add_argument('--filteralignment', help='Filter the source set by alignment')
    parser.add_argument('--filtercr', help='Filter the source set by Challenge Rating')
    parser.add_argument('--filtertype', choices=['construct', 'elemental', 'fey', 'fiend', 'humanoid', 'undead'], help='Filter the source set by type')
    # Apply templates to the filtered creatures
    parser.add_argument('--apply', choices=['ghostly', 'skeletal', 'zombie'], help='TODO: Apply a template to the current list of creatures')
    parser.add_argument('--list', help='Print out the current set of creatures')
    parser.add_argument('--writeindex', help='Write out an index of the creatures')
    parser.add_argument('--writemd', help='Target directory for MD files to be emitted')
    args = parser.parse_args()

    # What's the source set to start with?
    if args.parsemd != None:
        # Parse MD files
        if os.path.isdir(args.parsemd):
            files = os.listdir(args.parsemd)
            for f in files:
                if os.path.isfile(args.parsemd + '/' + f):
                    with open(args.parsemd + '/' + f, 'r') as mdfile:
                        lines = mdfile.readlines()
                        creature = Creature()
                        creature.parseMD(lines)
                        creatures.append(creature)
        else:
            with open(args.parsemd, 'r') as mdfile:
                lines = mdfile.readlines()
                creature = Creature()
                creature.parseMD(lines)
                creatures.append(creature)

    elif args.parsesql != None:
        # Parse SQLite db
        pass
    else:
        print("No source set specified!")

    # Filter?

    # Ingest?
    if args.ingest != None:
        ingest(args.ingest)

    # Apply template?

    # List
    if args.list != None:
        for name in map(lambda crea: creature.name, creatures):
            print(name)

    # Store?
    if args.writemd != None:
        dest = args.writemd
        if dest == '-':
            for creature in creatures:
                print(creature.emitMD())
        elif os.path.isdir(dest):
            for creature in creatures:
                print("Writing " + str(creature))
                with open(camelcaseify(args.writemd + '/' + creature.name).title() + ".md", 'w') as mdfile:
                    mdfile.write(creature.emitMD())
    else:
        parser.print_help()

if __name__ == '__main__':
	main(sys.argv)
