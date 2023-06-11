import os
import sqlite3
import sys

# This script parses spells in a directory and creates Spell objects.
# From there, Spell objects can be manipulated to create spell lists,
# reformatted and reprinted, stored to XML.

# Input options:
#   parsemd mdfile|dir: Parse spells in markdown format;
#       if (mdfile) is a file, parse that single file;
#       if (dir) is a directory, parse the directory
#       default is ".", the current directory
#   parsexml (xmlfile): Draw spells in from XML;
#       if (xmlfile) is specified, read them all from a single XML file
#
# Output options:
#   writemd: Write spells out in markdown format
#   writexml: Write spells out to xml
#   writemdlist (bard|cleric|druid|...):
#       write a list of all (class) spells in Markdown to STDOUT
#   writexmllist (bard|cleric|druid|...):
#       write a list of all (class) spells in XML to STDOUT

classes = ["Artificer", "Bard", "Cleric", "Druid", "Mystic",
           "Paladin", "PaleMaster","Ranger", "Shaman",
           "Sorcerer", "Warlock", "Wizard"]

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
            spell.name = lines[0][5:].strip()

            subtitle = lines[1].replace('*', '')

            # Does subtitle have "ritual" in it?
            if subtitle.find("(ritual)") > 0:
                spell.ritual = True
                subtitle.replace('(ritual)', '')
                subtitle.replace('ritual', '')

            spell.classes = extractClasses(subtitle)
            if spell.classes == []:
                print("WARNING: No classes found in parse")
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
                spell.level = "Cantrip"
                # need to get spell type

            # lines[2] is ___
            spell.casting_time = lines[3][20:].strip() # - **Casting Time:** 1 action
            spell.range = lines[4][13:].strip() # - **Range:** 120 feet
            spell.components = lines[5][18:].strip() # - **Components:** V, S, M (a small piece of phosphorus)
            spell.duration = lines[6][16:].strip() # - **Duration:** Concentration, up to 1 minute
            # lines[7[ is ---
            spell.description = lines[8:]

        elif lines[0].startswith('#'):
            spell.name = lines[0][2:].replace('\n', '')

            subtitle = lines[1].replace('*', '') # *1st-level necromancy (ritual)* (classes)
            subtitle = lines[1].replace('*', '')

            # Does subtitle have "ritual" in it?
            if subtitle.find("(ritual)") > 0:
                spell.ritual = True
                subtitle.replace('(ritual)', '')
                subtitle.replace('ritual', '')

            spell.classes = extractClasses(subtitle)
            if spell.classes == []:
                print("WARNING: " + spell.name + ": No classes found in parse")
            else:
                classStartIdx = subtitle.find('(')
                subtitle = subtitle[0:classStartIdx]

            if subtitle.startswith("1st-"):
                spell.level = "1"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("2nd-"):
                spell.level = "2"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("3rd-"):
                spell.level = "3"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("4th-"):
                spell.level = "4"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("5th-"):
                spell.level = "5"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("6th-"):
                spell.level = "6"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("7th-"):
                spell.level = "7"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("8th-"):
                spell.level = "8"
                spell.type = subtitle[10:].strip()
            elif subtitle.startswith("9th-"):
                spell.level = "9"
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
    
    def parseXML():
        spell = Spell()

        return spell
    
    def parseRow(row):
        spell = Spell()

        return spell
    
    def printMD(self):
        text = "#### " + self.name + "\n"
        text += "*" + self.level + "-level " + self.type + "* (" + ",".join(self.classes) + ")\n"
        text += "___\n"
        text += "- **Casting Time:** " + self.casting_time + "\n"
        text += "- **Range:** " + self.range + "\n"
        text += "- **Components:** " + self.components + "\n"
        text += "- **Duration:** " + self.duration + "\n"
        text += "---\n"
        text += "".join(self.description)

        return text
    
    def printXML(self):
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
        sql = "INSERT INTO spell VALUES("
        sql += self.name + ","
        sql += ")"
        conn.execute(sql)

spells = []

def main():
    # Examine passed options
    argi = 1
    while argi < len(sys.argv):
        command = sys.argv[argi]

        ################
        # Parse SQLite
        if command == "parsesql":
            argi += 1

            target = ""
            if argi <= len(sys.argv):
                target = sys.argv[argi]
                argi += 1
            else:
                print("You must specify a SQLite database file")
                return
            
            with sqlite3.connect(target) as conn:
                pass

        ################
        # Parse Markdown
        if command == "parsemd":
            argi += 1

            target = "."
            if (argi) <= len(sys.argv):
                target = sys.argv[argi]
                argi += 1
            
            if os.path.isfile(target):
                spell = Spell.parseMDSpell(target)
                spells.append(spell)
            elif os.path.isdir(target):
                files = os.listdir(target)
                for f in files:
                    spell = Spell.parseMDSpell(target + "/" + f)
                    spells.append(spell)

        ################
        # Parse XML
        elif command == "parsexml":
            print("XML not yet support as an input format")
            argi += 1
            return

        ################
        # Write Markdown
        elif command == "writemd":
            argi += 1

            target = "."
            if (argi + 1) <= len(sys.argv):
                target = sys.argv[argi + 1]
                argi += 1

            if len(spells) > 1:
                for spell in spells:
                    print(spell.printMD())
                    print(" ")
                    print("----------")
                    print("  ")
            else:
                print(spells[0].printMD())

        ################
        # Write XML
        elif command == "writexml":
            argi += 1

            target = "-"
            if (argi + 1) <= len(sys.argv):
                target = sys.argv[argi + 1]
                argi += 1

            if len(spells) > 1:
                print("<spellbook>")
                for spell in spells:
                    print(spell.printXML())
                print("</spellbook>")
            else:
                print(spells[0].printXML())

        ################
        # Write SQLite
        elif command == "writesql":
            argi += 1

            target = ""
            if argi <= len(sys.argv):
                target = sys.argv[argi]
                argi += 1
            else:
                print("You must specify a SQLite database file")
                return

            with sqlite3.connect(target) as conn:
                conn.execute("""
CREATE TABLE spell(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR(80),
level VARCHAR(10),
ritual VARCHAR(2),
type VARCHAR(20),
classes VARCHAR(80).
castingtime VARCHAR(80),
range VARCHAR(80),
duration VARCHAR(80),
components VARCHAR(80),
description VARCHAR(1024)
);""")
                for spell in spells:
                    spell.writeRow(conn)

        ################
        # Unrecognized
        else:
            print("Unrecognized option: " + sys.argv[argi])
            return

if __name__ == '__main__':
	main()
