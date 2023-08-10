#!/usr/bin/env python3

import argparse
import csv
import random
import os
import sqlite3
import sys

# This script takes the CSV from the Azgaar tool and fleshes out cities
# ("burbs") with some greater detail. Honestly, really should only need
# to be run once across all the cities in Azgaarnoth, and generate a ton
# of detail pages into /Cities, but I don't know yet if I'll want to
# re-run for particular cities or not.

class City:
    def __init__(self):
        self.name = ''
        self.state = ''
        self.description = ''
        self.province = ''
        self.geography = ''
        self.features = []
        self.authorities = []
        self.populationct = 0
        self.populationbreakdown = { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }
        self.militaryunits = []
        self.houses = []
        self.militantorders = []
        self.roguesguilds = []
        self.merchantguilds = []
        self.mageschools = []
        self.duelingcolleges = []
        self.religions = []
    
    def parsecsvrow(self, row):
        self.name = row[1]
        self.province = row[2]
        self.state = row[4]
        self.religions.append(row[7])
        self.populationct = int(row[8])

    def parsemd(self, lines):
        pass

    def calculatepopulationbreakdown(self):
        baseproportions = {
            # AlUma
            ['Alalihat', 'Almalz', 'Zabalasa'] : { 'Human': 50, 'Firstborn' : 30, 'Created': 15, 'Hordish': 5 },
            # Liria
            ['Liria', 'Mighalia', ] : { 'Human': 40, 'Firstborn' : 20, 'Created': 20, 'Hordish': 20 },
            # Travesimia
            ['Travesimia', 'Bagonbia', 'Whavesimia'] : { 'Human': 35, 'Firstborn' : 25, 'Created': 25, 'Hordish': 15 },
            # Travenia
            ['Travenia'] : { 'Human': 35, 'Firstborn' : 25, 'Created': 25, 'Hordish': 15 },
            # Dradehalia
            ['Dradehalia'] : { 'Human': 65, 'Firstborn' : 15, 'Created': 15, 'Hordish': 5 },
            # Hordes
            ['Tragekia', 'Ulm'] : { 'Human': 10, 'Firstborn' : 20, 'Created': 20, 'Hordish': 50 },
            # Yithia
            ['Yithi', 'Zhi'] : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 },
        }
        def randomize5(value):
            return value + int((value / 100) * random.randint(-25, 25))

        baseprops = {}
        for states in baseproportions.keys():
            if self.state in states:
                baseprops = baseproportions[states]
        for race in self.populationbreakdown.keys():
            self.populationbreakdown[race] = randomize5(baseprops[race])

    def calculatemilitia(self):
        results = "**Militia.** "
        onepercentpopulation = self.populationct // 100
        if self.populationct > 25000:
            # Militia is 4-6% of total
            militia = onepercentpopulation * (4 + random.randint(0, 2))
            onepercentmilitia = militia // 100
            # 1% level 5; 4% level 4; 10% level 3; 25% level 2; 60% level 1
            level5 = onepercentmilitia
            level4 = onepercentmilitia * 4
            level3 = onepercentmilitia * 10
            level2 = onepercentmilitia * 25
            level1 = militia - (level5 + level4 + level3 + level2)
            results += f'Mustered on demand. {level1}xFighter1, {level2}xFighter2, {level3}xFighter3, {level4}xFighter4, {level5}xFighter5 (Total: ~{militia})'
        elif self.populationct > 10000:
            # Militia is around 8-12% of total
            militia = onepercentpopulation * (8 + random.randint(0, 4))
            onepercentmilitia = militia // 100
            # 1% level4; 5-9% level3; 15-20% level2; rest level1
            level4 = onepercentmilitia
            level3 = onepercentmilitia * (random.randint(5, 9))
            level2 = onepercentmilitia * (random.randint(15, 20))
            level1 = militia - (level4 + level3 + level2)
            results += f'Mustered on demand. {level1}xFighter1, {level2}xFighter2, {level3}xFighter3, {level4}xFighter4 (Total: ~{militia})'
        elif self.populationct > 5000:
            # Militia is around 15-25% of total
            militia = onepercentpopulation * (15 + random.randint(0, 10))
            onepercentmilitia = militia // 100
            # 3-5% level3; 15-20% level2; rest level1
            level3 = onepercentmilitia * (random.randint(3, 5))
            level2 = onepercentmilitia * (random.randint(15, 20))
            level1 = militia - (level3 + level2)
            results += f'Mustered on demand. {level1}xFighter1, {level2}xFighter2, {level3}xFighter3 (Total: ~{militia})'
        else:
            # Militia is 30-50% of total
            militia = onepercentpopulation * (30 + random.randint(0, 20))
            onepercentmilitia = militia // 100
            # level 2, 1-10%; level1 for the rest
            level2 = onepercentmilitia * (random.randint(1, 10))
            level1 = militia - level2
            results += f'Mustered on demand. {level1}xFighter1, {level2}xFighter2 (Total: ~{militia})'
        self.militaryunits.append(results)
        return results
    
    def calculateduelingcolleges(self):
        pass
    
    def calculatepopulationbreakdown(self):
        baseproportions = {
            # AlUma
            ['Alalihat', 'Almalz', 'Zabalasa'] : { 'Human': 50, 'Firstborn' : 30, 'Created': 15, 'Hordish': 5 },
            # Liria
            ['Liria', 'Mighalia', ] : { 'Human': 40, 'Firstborn' : 20, 'Created': 20, 'Hordish': 20 },
            # Travesimia
            ['Travesimia', 'Bagonbia', 'Whaveminsia'] : { 'Human': 35, 'Firstborn' : 25, 'Created': 25, 'Hordish': 15 },
            # Travenia
            ['Travenia'] : { 'Human': 35, 'Firstborn' : 25, 'Created': 25, 'Hordish': 15 },
            # Dradehalia
            ['Dradehalia'] : { 'Human': 65, 'Firstborn' : 15, 'Created': 15, 'Hordish': 5 },
            # Hordes
            ['Tragekia', 'Ulm'] : { 'Human': 10, 'Firstborn' : 20, 'Created': 20, 'Hordish': 50 },
            # Yithia
            ['Yithi', 'Zhi'] : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 },
        }
        def randomize5(value):
            return value + int((value / 100) * random.randint(-25, 25))

        baseprops = {}
        for states in baseproportions.keys():
            if self.state in states:
                baseprops = baseproportions[states]

    def parsecsvrow(self, row):
        self.name = row[1]
        self.province = row[2]
        self.state = row[4]
        self.religions.append(row[7])
        self.populationct = int(row[8])

    def parsemd(self, lines):
        pass

    def formatmd(self):
        results = f"# {self.name}\n"
        results += f"*({self.province}, [{self.state}](../Nations/{self.state}.md))*\n"
        results += "\n"
        results += f"**Population:** {self.populationct}\n"
        results += (f"*(Humans: {self.populationbreakdown['Human']}, " + 
            f"Firstborn: {self.populationbreakdown['Firstborn']}" + 
            f"Created: {self.populationbreakdown['Created']}" + 
            f"Hordish: {self.populationbreakdown['Hordish']}" + 
            ")*\n")
        results += "**Features:** " + ", ".join(self.features) + "\n"
        results += "\n"
        results += self.description + "\n"
        results += "\n"
        results += "## Geography\n"
        results += f"![]({self.name}.jpeg)" + "\n"
        results += "## Authority Figures\n"
        results += "\n"
        results += "## Military Units\n"
        results += "\n".join(self.militaryunits) + "\n"
        results += self.calculatemilitia() + "\n"
        results += "\n"
        results += "## Militant Orders\n"
        results += "\n"
        results += "## Mercenary Companies\n"
        results += "\n"
        results += "## Dueling Colleges\n"
        results += "\n"
        results += "## Great Houses\n"
        results += "\n"
        results += "## Mage Schools\n"
        results += "\n"
        results += "## Religious Organizations\n"
        results += "\n"
        results += "## Rogues' Guilds\n"
        results += "\n"

        return results

burbs = []

def parsecsv(csvfilename):
    results = []
    with open(csvfilename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        burb_count = -1
        for row in csv_reader:
            if burb_count == -1:
                burb_count = 0
            else:
                burb = City()
                burb.parsecsvrow(row)
                results.append(burb)
                burb_count += 1
    return results

def parsemd(mddirname):
	return []

def main():
    parser = argparse.ArgumentParser(
                    prog='SpellTool',
                    description='A spell list(s) and contents tool',
                    epilog='Text at the bottom of help')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--parsemd', help='File or directory for parsing MD file(s)')
    parser.add_argument('--parsecsv', help='CSV file to use as input database')
    parser.add_argument('--writeindex', help='Create an index.md page for all cities')
    parser.add_argument('--writecities', help='Write out MD descriptions of cities to given target directory')
    args = parser.parse_args()

    global burbs
    if args.parsecsv != None:
        burbs = parsecsv(args.parsecsv)
    elif args.parsemd != None:
        burbs = parsemd(args.parsemd)

    if args.writeindex != None:
        print("# Cities in Azgaarnoth\n\n")
        states = ['Alalihat', 'Almalz', 'Zabalasa', 'Liria', 'Mighalia', 
                  'Travesimia', 'Bagonbia', 'Whaveminsia', 'Travenia','Dradehalia', 
                  'Tragekia', 'Ulm', 'Yithi', 'Zhi']
        for state in states:
            print(f"## [{state}](../Nations/{state}.md)")
            stateburbs = list(filter(lambda city: city.state == state, burbs))
            stateburbs.sort(key=lambda city: city.name)
            for burb in stateburbs:
                print(f"* [{burb.name}]({burb.name}.md) *({burb.province})*")
            print("\n")
        sys.exit()
    elif args.writecities != None:
        target = args.writecities
        for burb in burbs:
            with open(target + "/" + burb.name + ".md", 'w') as outfile:
                outfile.write(burb.formatmd())
    else:
        parser.print_help()
        exit()


if __name__ == '__main__':
	main()
