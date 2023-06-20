#!/usr/bin/env python3

import argparse
import xml.etree.ElementTree as etree
import os
import sqlite3
import sys

# This script parses spells in a directory and creates Spell objects.
# From there, Spell objects can be manipulated to create spell lists,
# reformatted and reprinted, stored to XML.

classes = ["Artificer", "Bard", "Cleric", "Druid",
           "Paladin", "Pale Master","Ranger", "Shaman",
           "Sorcerer", "Warlock", "Wizard"]
levels = ["cantrip", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th"]

def extractClasses(subtitle):
    clazzes = []
    for clazz in classes:
        if subtitle.find(clazz) > 0:
            clazzes.append(clazz)
    return clazzes

class Spell:
    """A simple record type for each spell."""
    def __init__(self):
        # The name of the spell
        self.name = ""
        # Conjuration, evocation, ...
        self.type = ""
        # Cantrip, 1st-level, 2nd-level, ...
        self.level = ""
        # Ritual?
        self.ritual = False
        # Casting time
        self.casting_time = ""
        # Range of the spell
        self.range = ""
        # V, S, M
        self.components = ""
        # Duration of the spell
        self.duration = ""
        # Description of the spell
        self.description = ""
        # The classes on which this spell appears
        self.classes = []
        # The filename containing the spell
        self.filename = ""

    def summary(self):
        return self.name + " (" + self.level + " " + self.type + ")"

    def parseMDSpell(spellfile):
        """Parse a Markdown file into a Spell object."""
        spell = Spell()

        spell.filename = spellfile
        file = open(spellfile, 'r')
        lines = file.readlines()

        if lines[0].startswith('####'):
            # The #### form is something I downloaded from the Web, but prefer it
            # as a display format. THis is likely to be the format most often
            # encountered when parsing spells from this repository.
            spell.name = lines[0][5:].strip()

            subtitle = lines[1].replace('*', '')

            # Does subtitle have "ritual" in it?
            if subtitle.find("(ritual)") > 0:
                spell.ritual = True
                subtitle = subtitle.replace('(ritual)', '')
                subtitle = subtitle.replace('ritual', '')

            spell.classes = extractClasses(subtitle)
            if spell.classes == []:
                pass # print("WARNING: No classes found in parse: " + spell.filename)
            else:
                classStartIdx = subtitle.find('(')
                subtitle = subtitle[0:classStartIdx]

            if subtitle.startswith("1st-"):
                spell.level = "1st"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("2nd-"):
                spell.level = "2nd"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("3rd-"):
                spell.level = "3rd"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("4th-"):
                spell.level = "4th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("5th-"):
                spell.level = "5th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("6th-"):
                spell.level = "6th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("7th-"):
                spell.level = "7th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("8th-"):
                spell.level = "8th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("9th-"):
                spell.level = "9th"
                spell.type = subtitle[10:].strip()
            else:
                spell.level = "cantrip"
                # need to get spell type
                typeEndIdx = subtitle.find("antrip") - 1
                spell.type = subtitle[0:typeEndIdx].strip()

            # lines[2] is ___
            spell.casting_time = lines[3][20:].strip() # - **Casting Time:** 1 action
            spell.range = lines[4][13:].strip() # - **Range:** 120 feet
            spell.components = lines[5][18:].strip() # - **Components:** V, S, M (a small piece of phosphorus)
            spell.duration = lines[6][16:].strip() # - **Duration:** Concentration, up to 1 minute
            # lines[7[ is ---
            spell.description = lines[8:]

        elif lines[0].startswith('#'):
            # This form is one I originally used, and it's more bare-boned
            # but somewhat easier to translate from cut/pasted PDF sources.
            # A future form might remove the blank lines but let's see.
            spell.name = lines[0][2:].replace('\n', '')

            subtitle = lines[1].replace('*', '') # *1st-level necromancy (ritual)* (classes)
            subtitle = lines[1].replace('*', '')

            # Does subtitle have "ritual" in it?
            if subtitle.find("ritual") > 0:
                spell.ritual = True
                subtitle = subtitle.replace('(ritual)', '')
                subtitle = subtitle.replace('ritual', '')

            spell.classes = extractClasses(subtitle)
            if spell.classes == []:
                pass # print("WARNING: No classes found in parse: " + spell.filename)
            else:
                classStartIdx = subtitle.find('(')
                subtitle = subtitle[0:classStartIdx]

            if subtitle.startswith("1st-"):
                spell.level = "1st"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("2nd-"):
                spell.level = "2nd"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("3rd-"):
                spell.level = "3rd"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("4th-"):
                spell.level = "4th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("5th-"):
                spell.level = "5th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("6th-"):
                spell.level = "6th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("7th-"):
                spell.level = "7th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("8th-"):
                spell.level = "8th"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("9th-"):
                spell.level = "9th"
                spell.type = subtitle[10:].strip()
            else:
                spell.level = "cantrip"
                cantripIdx = subtitle.find(" cantrip")
                spell.type = subtitle[0:cantripIdx]
            # lines[2] is blank
            spell.casting_time = lines[3][18:].strip() # **Casting Time:** 1 action 
            # lines[4] is blank
            spell.range = lines[5][11:].strip() # **Range:** 60 feet
            # lines[6] is blank
            spell.components = lines[7][16:].strip() # **Components:** V, S
            # lines[8] is blank
            spell.duration = lines[9][14:].strip() # **Duration:** 1 hour
            # lines[10] is blank
            spell.description = lines[11:]

        file.close()
        return spell
    
    def parseXML(spellfile):
        spell = Spell()
        spell.filename = spellfile

        tree = etree.parse(spellfile)
        root = tree.getroot()
        spell.name = root.findall('name').text
        spell.level = root.findall('level').text
        spell.type = root.findall('type').text
        spell.classes = root.findall('classes')[0].text.split(',')
        spell.casting_time = root.findall('casting-time').text
        spell.components = root.findall('components').text
        spell.duration = root.findall('duration').text
        spell.range = root.findall('range').text
        spell.description = root.findall('description').text

        return spell
    
    def parseRow(row):
        spell = Spell()



        return spell
    
    def writeMD(self):
        text = "#### " + self.name + "\n"
        text += "*"
        if self.level == "cantrip":
            text += self.type + " " + self.level
        else:
            text += self.level + "-level " + self.type + "*"

        if self.ritual:
            text += " *(ritual)*"

        if len(self.classes) == 0:
            text += " (WARNING: NO CLASSES LISTED)\n"
        else:
            text += " (" + ",".join(self.classes) + ")\n"

        text += "___\n"
        text += "- **Casting Time:** " + self.casting_time + "\n"
        text += "- **Range:** " + self.range + "\n"
        text += "- **Components:** " + self.components + "\n"
        text += "- **Duration:** " + self.duration + "\n"
        text += "---\n"
        text += "".join(self.description)

        return text
    
    def writeXML(self):
        text = "<spell>"
        text += "  <name>" + self.name + "</name>"
        text += "  <level>" + self.level + "</level>"
        text += "  <type>" + self.type + "</type>"
        if self.ritual:
            text += "   <ritual />"
        text += "  <classes>" + ",".join(self.classes) + "</classes>"
        text += "  <casting-time>" + self.casting_time + "</casting-time>"
        text += "  <range>" + self.range + "</range>"
        text += "  <components>" + self.components + "</components>"
        text += "  <duration>" + self.duration + "</duration>"
        text += "  <description>" + "".join(self.description) + "</description>"
        text += "</spell>"
        return text

    # SQL schema for spell table:
    # CREATE TABLE spell(
    # id INTEGER PRIMARY KEY,
    # name VARCHAR(80),
    # level VARCHAR(10),
    # ritual VARCHAR(2),
    # type VARCHAR(20),
    # classes VARCHAR(80).
    # castingtime VARCHAR(80),
    # range VARCHAR(80),
    # duration VARCHAR(80),
    # components VARCHAR(80),
    # description VARCHAR(1024)
    # );
    def writeRow(self, conn):
        sql = "INSERT INTO spell (name, level, ritual, type, classes, castingtime, range, duration, components, description) "
        sql += "VALUES("
        sql += "\"" + self.name + "\","
        sql += "\"" + self.level + "\","
        if self.ritual:
            sql += "'Y',"
        else:
            sql += "'N',"
        sql += "\"" + self.type + "\","
        sql += "\"" + ",".join(self.classes) + "\","
        sql += "\"" + self.casting_time + "\","
        sql += "\"" + self.range + "\","
        sql += "\"" + self.duration + "\","
        sql += "\"" + self.components + "\","
        sql += "\"" + "".join(self.description) + "\""
        sql += ")"
        print("Executing " + sql)
        conn.execute(sql)

spells = []

def main():
    classOpts = ['all'] + classes

    parser = argparse.ArgumentParser(
                    prog='SpellTool',
                    description='A spell list(s) and contents tool',
                    epilog='Text at the bottom of help')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # Input commands
    parser.add_argument('--parsemd', help='File or directory for parsing MD file(s)')
    parser.add_argument('--parsesql', help='SQLite file to use as input database')
    parser.add_argument('--parsexml', help='File or directory for parsing XML file(s)')
    # Verification commands
    parser.add_argument('--lint', choices=['classes', 'general', 'name', 'type', 'all'], help='Examine parsed spells for oddness')
    # Lists commands
    parser.add_argument('--listmd', choices=classOpts, help='Produce an MD spell list for the passed class')
    parser.add_argument('--listtext', choices=classOpts, help='Produce a plain-text spell list for the passed class')
    parser.add_argument('--ritualsmd', choices=classOpts, help='Produce an MD ritual list for the passed class')
#    parser.add_argument('--summarymd', help='Produce an MD spell summary for all spells')
    # Output commands
    parser.add_argument('--writemd', help='Directory to which to write MD files')
    parser.add_argument('--writesql', help='SQLite filename to write spells to')
    parser.add_argument('--writexml', help='Directory to which to write XML files')

    # Process arguments
    args = parser.parse_args()
    #print(vars(args))

    # Get input
    if args.parsemd != None:
        target = args.parsemd
        files = os.listdir(target)
        for f in files:
            spell = Spell.parseMDSpell(target + "/" + f)
            spells.append(spell)
    elif args.parsexml != None:
        target = args.parsexml
        files = os.listdir(target)
        for f in files:
            spell = Spell.parseXMLSpell(target + "/" + f)
            spells.append(spell)
    elif args.parsesql != None:
        target = args.parsesql
        with sqlite3.connect(target) as conn:
            with conn.execute("SELECT * FROM spell;") as cursor:
                for row in cursor:
                    spell = Spell.parseRow(row)
                    spells.append(spell)
            pass
    else:
        print('No input source specified; exiting')
        return
    
    def findClassSpells(classname):
        found = []
        for spell in spells:
            if classname == 'all' or classname in spell.classes:
                found.append(spell)
            if classname == 'none' and spell.classes == []:
                found.append(spell)
        return found

    if args.lint != None:
        for spell in spells:
            if args.lint == 'classes' or args.lint == 'all':
                if spell.classes == []:
                    print(spell.name + ": No classes found")
                for c in spell.classes:
                    if c not in classes:
                        print(spell.name + ": Unrecognized class in class list: " + c)
            if args.lint == 'name' or args.lint == 'all':
                if spell.name == "" or len(spell.name) < 1:
                    print(spell.filename + " failed to pase spell name")
            if args.lint == 'type' or args.lint == 'all':
                loweredType = spell.type.lower()
                if loweredType not in ['abjuration', 'conjuration', 'divination', 'evocation', 'enchantment', 'illusion', 'necromancy', 'transmutation']:
                    print(spell.name + ': Unrecognized spell type: ' + loweredType)
            if args.lint == 'general' or args.lint == 'all':
                if spell.casting_time == "":
                    print(spell.name + ": No parsed casting time")
                if spell.range == "":
                    print(spell.name + ": No parsed range")
                if spell.components == "":
                    print(spell.name + ": No parsed components")
                if spell.duration == "":
                    print(spell.name + ": No parsed duration")

    def snakecasefilename(name):
        return name.replace(' ', '-').replace('\'', '').replace('/', '-').lower()

    # Are we doing lists?
    if args.listtext != None:
        classTarget = str(args.listtext)
        found = findClassSpells(classTarget)
        print(classTarget + " Spells")
        for spell in found:
            print(str(spell.name) + " (" + spell.filename + ")")

    elif args.listmd != None:
        classTarget = str(args.listmd)
        found = findClassSpells(classTarget)
        if classTarget == 'all':
            print("# Master List of Spells")
            print("For all spellcasting classes (" + ", ".join(classes) + ")")
        else:
            print("# " + classTarget + " Spells")
        print(" ")

        for level in levels:
            print("## " + level + "-Level Spells")
            for spell in found:
                if spell.level == level:
                    if classTarget == 'all':
                        print("* [" + str(spell.name) + "](" + spell.filename + "): " + ", ".join(spell.classes))
                    else:
                        print("* [" + str(spell.name) + "](" + spell.filename + ")")
            print(" ")

    elif args.ritualsmd != None:
        classTarget = str(args.ritualsmd)
        found = findClassSpells(classTarget)
        if classTarget == 'all':
            print("# Master List of Rituals")
            print("For all spellcasting classes (" + ", ".join(classes) + ")")
        else:
            print("# " + classTarget + " Rituals")
        print(" ")

        for level in levels:
            print("## " + level + "-Level Rituals")
            for spell in found:
                if spell.level == level and spell.ritual == True:
                    if classTarget == 'all':
                        print("* [" + str(spell.name) + "](" + spell.filename + "): " + ", ".join(spell.classes))
                    else:
                        print("* [" + str(spell.name) + "](" + spell.filename + ")")
            print(" ")

# This is only useful if I'm worried that spells are being lost in the
# from the lists somehow.
#    elif args.summarymd != None:
#        print("# Summary Spell List")
#        print("For all spellcasting classes (" + ", ".join(classes) + ")")
#        print(" ")
#        for level in levels:
#            print("## " + level + "-Level Spells")
#            for spell in spells:
#                if spell.level == level:
#                    print("* [" + str(spell.name) + "](" + spell.filename + "): " + ", ".join(spell.classes))
#            print(" ")

    elif args.writemd != None:
        prefix = args.writemd
        # Create prefix directory if it doesn't exist
        if os.path.isdir(prefix) == False:
            print("Directory does not exist! Creating it.")
            os.mkdir(prefix)

        # Write out all the spells
        for spell in spells:
            filename = prefix + '/' + snakecasefilename(spell.name) + ".md"
            print("Writing " + filename)
            with open(filename, 'w') as file:
                file.write(spell.writeMD())

    elif args.writexml != None:
        prefix = args.writexml
        # Create prefix directory if it doesn't exist
        if os.path.isdir(prefix) == False:
            print("Directory does not exist! Creating it.")
            os.mkdir(prefix)

        # Write out all the spells
        for spell in spells:
            filename = prefix + '/' + snakecasefilename(spell.name) + ".xml"
            print("Writing " + filename)
            with open(filename, 'w') as file:
                file.write(spell.writeXML())
    
    elif args.writesql != None:
        sqlfile = args.writesql
        with sqlite3.connect(sqlfile) as conn:
            sql = """CREATE TABLE spell(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(80),
level VARCHAR(10),
ritual VARCHAR(2),
type VARCHAR(20),
classes VARCHAR(80),
castingtime VARCHAR(80),
range VARCHAR(80),
duration VARCHAR(80),
components VARCHAR(80),
description VARCHAR(4096)
);"""
            conn.execute(sql)

            for spell in spells:
                spell.writeRow(conn)

if __name__ == '__main__':
	main()
