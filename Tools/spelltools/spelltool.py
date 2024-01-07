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
spelltypes = ['abjuration', 'conjuration', 'divination', 'evocation', 
              'enchantment', 'illusion', 'necromancy', 'transmutation']

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
        # Tags: ritual, blood, psionic, (damage types?)
        self.tags = []
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

        try:
            lines = file.readlines()

            if lines[0].startswith('####'):
                # The #### form is something I downloaded from the Web, but prefer it
                # as a display format. This is likely to be the format most often
                # encountered when parsing spells from this repository.
                spell.name = lines[0][5:].strip()

                def extractSecondLine(text):
                    subtitle = ""
                    tags = ""
                    classes = ""

                    parts = text.split("*")
                    if len(parts) == 5:
                        # There's tags
                        subtitle = parts[1]
                        tags = parts[3][1:len(parts[3])-1]
                        classes = parts[4].strip()
                    elif len(parts) == 3:
                        # There's no tags
                        subtitle = parts[1]
                        classes = parts[2].strip()

                    return [subtitle, tags, classes]

                parts = extractSecondLine(lines[1])
                subtitle = parts[0]
                if len(parts[1]) > 0:
                    spell.tags = parts[1].split(',')
                spell.classes = extractClasses(parts[2])
                if spell.classes == []:
                    pass # print("WARNING: No classes found in parse: " + spell.filename)

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
                # pull "At Higher Levels" out of the description, if present

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
                # pull "At Higher Levels" out of the description, if present

        except UnicodeDecodeError as udex:
            print("Error parsing " + spellfile + ": " + udex)
        else:
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
        #spell.at_higher_levels = root.findall('at-higher-levels').text

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
            text += self.level + "-level " + self.type
        text += "*"

        if len(self.tags) > 0:
            text += " *("
            text += ",".join(self.tags)
            text += ")*"

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
        #text += "\n"
        #text += "***At Higher Levels.*** " + "".join(self.at_higher_levels)

        return text
    
    def writeXML(self):
        text = "<spell>"
        text += "  <name>" + self.name + "</name>"
        text += "  <level>" + self.level + "</level>"
        text += "  <type>" + self.type + "</type>"
        text += "  <tags>"
        for tag in self.tags:
            text += "<tag>${tag}</tag>"
        text += "  </tags>"
        text += "  <classes>" + ",".join(self.classes) + "</classes>"
        text += "  <casting-time>" + self.casting_time + "</casting-time>"
        text += "  <range>" + self.range + "</range>"
        text += "  <components>" + self.components + "</components>"
        text += "  <duration>" + self.duration + "</duration>"
        text += "  <description>" + "".join(self.description) + "</description>"
        #text += "  <at-higher-levels>"" + "".join(self.at_higher_levels) + "</at-higher-levels>"
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
        sql = "INSERT INTO spell (name, level, tags, type, classes, castingtime, range, duration, components, description) "
        sql += "VALUES("
        sql += "\"" + self.name + "\","
        sql += "\"" + self.level + "\","
        sql += "\"" + self.type + "\","
        sql += "\"" + ",".join(self.tags) + "\","
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
    global spells

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
    # Find commands
    parser.add_argument('--findclass', choices=classOpts, help='Find spells for a given class')
    parser.add_argument('--findname', help='Find spells with particular text in the name')
    parser.add_argument('--findtag', help='Find spells by tag (ritual, blood, etc)')
    parser.add_argument('--findtype', choices=spelltypes, help='Find spells by type')
    parser.add_argument('--findtext', help='Find keywords in spell text or title')
    # Output commands
    parser.add_argument('--list', choices=['md', 'text'], help='Print a spell list in the format given (Markdown, text, etc)')
    parser.add_argument('--summarymd', help='Write an MD spell summary in the file named')
    parser.add_argument('--summarytext', help='Write a text spell summary in the file named')
    parser.add_argument('--writemd', help='Directory to which to write MD files')
    parser.add_argument('--writesql', help='SQLite filename to write spells to')
    parser.add_argument('--writexml', help='Directory to which to write XML files')

    # Process arguments
    args = parser.parse_args()
    #print(vars(args))

    ########
    ### Input source
    listtitle = ""

    if args.parsemd != None:
        target = args.parsemd
        files = os.listdir(target)
        for f in files:
            if f == "." or f == ".." or f == "index.md":
                continue
            else:
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
    else:
        print('No input source specified; exiting')
        return
    
    def findSpells(predicate):
        found = []
        for spell in spells:
            if predicate(spell) == True:
                found.append(spell)
        return found

    if args.findclass != None:
        sclass = args.findclass
        print("Finding spells for class " + str(sclass))
        listtitle += sclass + " "
        found = []
        if sclass == 'all':
            found = spells
        elif sclass == 'none':
            found = findSpells(lambda s : s.classes == [])
        else:
            found = findSpells(lambda s : (sclass in s.classes))
        spells = found

    if args.findtag != None:
        tag = args.findtag
        print("Finding spells tagged " + str(tag))
        listtitle += tag + " "
        found = findSpells(lambda s: tag in s.tags)
        spells = found
    
    if args.findname != None:
        name = args.findname
        print("Finding spells with name containing '" + str(name) + "'")
        listtitle += name + " "
        found = findSpells(lambda s: name.casefold() in s.name.casefold())
        spells = found

    if args.findtype != None:
        stype = args.findtype
        print("Finding spells of type " + stype)
        listtitle += stype + " "
        found = findSpells(lambda s: s.type == args.findtype)
        spells = found

    if args.findtext != None:
        def descriptionsearch(txt, description):
            for desc in description:
                if txt.casefold() in desc:
                    return True
            return False
        
        text = args.findtext
        print("Finding spells with text containing '" + str(text) + "'")
        listtitle += text + " "
        found = findSpells(lambda s: descriptionsearch(text, s.description) )
        spells = found

    ########
    ### Lint
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
                if loweredType not in spelltypes:
                    print(spell.name + ': Unrecognized spell type: ' + loweredType)
            if args.lint == 'general' or args.lint == 'all':
                if spell.level in ['6th', '7th', '8th', '9th']:
                    for c in ['Artificer', 'Paladin', 'Ranger']:
                        if c in spell.classes:
                            print(spell.name + ': Unusable by half-caster ' + c)
                if spell.casting_time == "":
                    print(spell.name + ": No parsed casting time")
                if spell.range == "":
                    print(spell.name + ": No parsed range")
                if spell.components == "":
                    print(spell.name + ": No parsed components")
                if spell.duration == "":
                    print(spell.name + ": No parsed duration")
                if (" ".join(spell.description).find("At Higher Levels") > -1) and (" ".join(spell.description).find("***At Higher Levels") < 0):
                    print(spell.name + ": At Higher Levels probably not bolded")

    def snakecasefilename(name):
        return name.replace(' ', '-').replace('\'', '').replace('/', '-').lower()

    # Are we doing a search, or lists?

    def listmd(withclasses=False,withtags=False,title=""):
        lines = []
        def print(text):
            lines.append(text)
        if title != "":
            print("# " + title)
        for level in levels:
            levelspells = list(filter(lambda s: s.level.strip() == level.strip(), spells))
            if len(levelspells) == 0:
                continue
            levelspells.sort(key=lambda s: s.name)
            print("## " + level + "-Level Spells")
            for spell in levelspells:
                if withclasses and withtags:
                    if len(spell.tags) > 0:
                        print("* [" + str(spell.name) + "](" + spell.filename + ") *" + ",".join(spell.tags) + "* (" + ",".join(spell.classes) + ")")
                    else:
                        print("* [" + str(spell.name) + "](" + spell.filename + ") (" + ",".join(spell.classes) + ")")
                elif withclasses:
                    print("* [" + str(spell.name) + "](" + spell.filename + ") (" + ",".join(spell.classes) + ")")
                elif withtags:
                    if len(spell.tags) > 0:
                        print("* [" + str(spell.name) + "](" + spell.filename + ") *" + ",".join(spell.tags) + "*" )
                    else:
                        print("* [" + str(spell.name) + "](" + spell.filename + ")")
                else:
                    print("* [" + str(spell.name) + "](" + spell.filename + ")")
            print(" ")
        return lines
    
    def listtext(withclasses=False,withtags=False):
        lines = []
        def print(text):
            lines.append(text)
        print(listtitle)
        for level in levels:
            levelspells = list(filter(lambda s: s.level.strip() == level.strip(), spells))
            if len(levelspells) == 0:
                continue
            print(level + "-Level Spells")
            levelspells.sort(key=lambda s: s.name)
            for spell in levelspells:
                if withclasses and withtags:
                    print("  " + spell.name)
                elif withclasses:
                    print("  " + spell.name + " (" + ",".join(spell.classes) + ")")
                elif withtags:
                    print("  " + spell.name + " -- " + ",".join(spell.tags))
                else:
                    print("  " + spell.name)
            print(" ")
        return lines

    if args.summarymd != None:
        filename = args.summarymd
        print("Writing " + filename + "; " + str(len(spells)) + " spells")
        with open(filename, 'w') as file:
            if listtitle == "":
                lines = listmd(True, True, "Spell List Summary: " + listtitle)
            else:
                lines = listmd(False, True, "Spell List Summary: " + listtitle)
            for line in lines: file.write(line + "\n")

    if args.summarytext != None:
        filename = args.summarytext
        print("Writing " + filename + "; " + str(len(spells)) + " spells")
        with open(filename, 'w') as file:
            lines = listmd(False, True)
            for line in lines: file.write(line + "\n")

    if args.list != None:
        if args.list == 'md':
            lines = listmd(True)
            for line in lines: print(line)
        elif args.list == 'text':
            lines = listtext(True)
            for line in lines: print(line)
        else:
            print("Unrecognized list format!")
        print(str(len(spells)) + " spells")

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
