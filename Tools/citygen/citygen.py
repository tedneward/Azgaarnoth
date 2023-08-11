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

def namegen(which):
    if which == 'roguesguild':
        prefixes = [
            'Order of the ', 'Council of the '
        ]
        descriptors = [
            'Mercury', 'Night', 'Midnight', 'Raven', 'Grey', 'Fire', 'Dusk',
            'Nightshade', 'Reviled', 'Umbral', 'Stained', "Butcher's", 'Cursed'
        ]
        nouns = [
            'Blades', 'Knives', 'Star', 'Consortium', 'Syndicate', 'Cabal', 'Court',
            'Daggers', 'Gang', 'Boys', 'Hand', 'Coil', 'Alliance', 'Maggots'
        ]
        desc = descriptors[random.randint(0, len(descriptors))] + ' ' + nouns[random.randint(0, len(nouns))]
        if random.randint(0, 100) > 50:
            desc = prefixes[random.randint(0, len(prefixes))] + ' ' + desc
        return desc
    elif which == 'mageschool':
        if random.randint(0, 100) > 60:
            schools = os.listdir('../../Organizations/MageSchools')
            school = schools[random.randint(0, len(schools))][0:-3]
            return school
        else:
            descriptors = [
                'Infinite', 'Miasmal', 'Nonesuch', 'Chthonic', 'Celestial', 'Spiral', 
                'Crimson', 'Silent', 'Bronze', 'Colossal', 'Elemental', 'Gilded',
                'Shimmering', 'Eldritch', 'Immaculate', 'Fey', 'Astral', 'Chaos',
                'Enduring', 'Everlasting'
            ]
            nouns = [
                'Cylinder', 'Minaret', 'Monument', 'Pylon', 'Tower', 'Spire', 'Turret', 
                'Column', 'Obelisk', 'Rock', 'Eye', 'Tome'
            ]
            descriptor = descriptors[random.randint(0, len(descriptors))]
            noun = nouns[random.randint(0, len(nouns))]
            return descriptor + ' ' + noun
    elif which == 'bardiccollege':
        return "**BARDIC COLLEGE**"
    elif which == 'duelingcollege':
        return "**DUELING COLLEGE**"
    elif which == 'merchantguild':
        return "**DUELING COLLEGE**"
    elif which == 'mercenarycompany':
        if random.randint(0, 100) > 50:
            names = []
            collective = [
                'Reavers', 'Scoundrels', 'Devils', 'Demons', 'Knights', 'Dragoons',
                'Cavaliers', 'Warriors', 'Raptors', ''
            ]
        else:
            descriptors = [
                'Shining', 'Gleaming', 'Barking'
            ]
            weapons = [
                'Axe', 'Knife', 'Swords', 'Blades'
            ]
            organization = [
                'Compact', 'Company', 'Pact', 'Dragoons', 'Knights'
            ]
        return "**MERC COMPANY**"
    elif which == 'monasticorder':
        return "**MONASTIC ORDER**"
    elif which == 'house':
        houses = os.listdir('../../Organizations/Houses')
        house = houses[random.randint(0, len(houses))][0:-3]
        return house
    else:
        return "UNRECOGNIZED NAME: '" + which + "'"
    pass

class City:
    def __init__(self):
        self.name = ''
        self.state = ''
        self.description = []
        self.province = ''
        self.geography = ''
        self.capital = False
        self.port = False
        self.citadel = False
        self.walls = False
        self.plaza = False
        self.temple = False
        self.shantytown = False
        self.authorities = []
        self.populationct = 0
        self.populationbreakdown = { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }
        self.militaryunits = []
        self.mercenarycompanies = []
        self.houses = []
        self.militantorders = []
        self.roguesguilds = []
        self.merchantguilds = []
        self.mageschools = []
        self.duelingcolleges = []
        self.religion = ''      # The dominant religion in the city
        self.religiousgroups = []
        self.monasticorders = []
    
    def parsecsvrow(self, row):
        # 0: Id, 1: Burg, 2: Province, 3: Province Full Name,
        # 4: State, 5: State Full Name, 6: Culture, 7: Religion,
        # 8: Population, 9: Latitude, 10: Longitude,
        # 11: Elevation (ft),
        # 12: Capital, 13: Port, 14: Citadel, 15: Walls, 16: Plaza, 17: Temple, 18: Shanty Town
        self.name = row[1]
        self.province = row[2]
        self.state = row[4]
        self.religion = row[7]
        self.populationct = int(row[8])

        if row[12] != '':
            self.capital = True
            self.description.append(f"{self.name} is the capital of {self.state}, and ...")
        if row[13] != '':
            self.port = True
            self.militaryunits.append(f"**Marines.** These are typically rotated between port guard duty, tariff duty in incoming vessels, and extended patrols out into the waters around {self.name}. **TODO**")
            self.description.append(f"{self.name} boasts a port for maritime shipping....")
        if row[14] != '':
            self.citadel = True
            if self.populationct > 5000:
                self.militaryunits.append(f"**Palace Guard.** These typically rotate between citidel guard duty and special missions as dictated by city authorities. 75xFighter 3-5, 20xWizard/Sorcerer 3-5, 30xCleric/Druid 3-5, 25xRogue 3-5.")
                self.description.append(f"{self.name} retains a citadel for the upper ranks and guests, and much of the elite guard resides there.")
            else:
                self.description.append(f"An ancient citadel stands within {self.name}'s city limits, but currently is all but abandoned.")
        if row[15] != '':
            self.walls = True
            wallprob = random.randint(1,100)
            if  wallprob > 50:
                self.description.append(f"The walls are in good shape, kept in good order by the city authorities.")
            elif wallprob > 25:
                self.description.append(f"The city walls still stand, but clearly have seen neglect over the years.")
            else:
                self.description.append(f"{self.name}'s walls are crumbling and in disrepair, with obvious gaps from previous sieges or battles still as yet unrepaired.")
        if row[16] != '':
            self.plaza = True
            if self.populationct > 10000:
                self.description.append(f"{self.name}'s city center boasts a large plaza, called **TODO**, which is a central place in the lives of many within the city.")
            elif self.populationct > 5000:
                self.description.append(f"{self.name}'s city center has a central plaza that provides common, day-to-day shopping and farmer's markets, made up primarily of foodstuff's and artisan's shops.")
            else:
                self.description.append("The city has a central area of shops which sees much traffic. Already several fountains and other decorative statues mark the rough edges of this plaze.")
        if row[17] != '':
            self.temple = True
            self.description.append(f"The {self.religion} religion has a large temple here near the city center.")
        if row[18] != '':
            self.shantytown = True
            poppercent = (random.randint(1, 8) * 5) 
            desc = f"Sadly, {self.name} has a shantytown. Roughly {poppercent}% of the city live within it. "
            if poppercent > 25:
                desc += "Most of the city's guards and other law enforcement avoid or outright refuse to enter. "
            else:
                desc += "The city's guards and other law enforcement groups struggle to keep the inhabitants safe. "
            if len(self.roguesguilds) > 1:
                desc += "The various Rogues' Guilds battle here for dominance and recruits, as well as to carve out the freedom to carry out their activities. "
            desc += "\n"
            self.description.append(desc)


    def parsemd(self, lines):
        pass

    def calculate(self):
        self.calculatepopulationbreakdown()
        self.calculateauthorities()
        self.calculatemilitia()
        self.calculateduelingcolleges()
        #self.calculatemercenaries()
        #self.calculatemageschools()
        #self.calculatereligiousgroups()
        #self.calculateroguesguilds()
        #self.calculatemerchantguilds()
        #self.calculatemonasticorders()

    def calculatepopulationbreakdown(self):
        pass

    def calculateauthorities(self):
        # Police chief/law enforcement
        if self.populationct > 10000:
            # The Guard
            self.militaryunits.append("**City Guard.** **TODO**")
            # Captain of the Guard
            self.authorities.append("**TODO**, Captain of the City Guard")
        else:
            self.militaryunits.append("**Town Guard.** **TODO**")
            self.authorities.append("**TODO**, Captain of the Guard")

        # Religious figures
        if self.temple:
            self.authorities.append("**TODO**, High Priest of ${self.religion}")

        # Rogues Guild
        if len(self.roguesguilds) > 2:
            self.authorities.append(f"**TODO**, Guildmaster of the {self.roguesguilds[random.randint(0, len(self.roguesguilds))]} Rogues' Guild.")

        # Mage Schools
        if len(self.mageschools) > 1:
            self.authorities.append(f"**TODO**, Arcane Master of the ${self.mageschools[random.randint(0, len(self.mageschools))]} Mage School.")

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
        numcolleges = self.militaryunits
        if len(self.mercenarycompanies) > 0:
            numcolleges *= 2
        pass

    def calculateroguesguilds(self):
        numguilds = self.populationct // 5000
        if self.shantytown:
            numguilds *= 2
        numguilds -= len(self.militaryunits)
        pass
    
    def formatmd(self):
        results = f"# {self.name}\n"
        results += f"*({self.province}, [{self.state}](../Nations/{self.state}.md))*\n"
        results += "\n"
        results += f"**Population:** {self.populationct}\n"
        results += (f"*(Humans: {self.populationbreakdown['Human']}, " + 
            f"Firstborn: {self.populationbreakdown['Firstborn']} " + 
            f"Created: {self.populationbreakdown['Created']} " + 
            f"Hordish: {self.populationbreakdown['Hordish']})*\n\n")
        results += "\n\n".join(self.description) + "\n"
        results += "\n"
        results += "## Geography\n"
        results += f"![]({self.name}.jpeg)\n\n"
        results += "## Authority Figures\n"
        results += "\n\n".join(self.authorities) + "\n"
        results += "\n"
        results += "## Great Houses\n"
        results += "\n\n".join(self.houses) + "\n"
        results += "\n"
        results += "## Military Units\n"
        results += "\n\n".join(self.militaryunits) + "\n"
        results += "\n"
        results += "## Militant Orders\n"
        results += "\n\n".join(self.militantorders) + "\n"
        results += "\n"
        results += "## Mercenary Companies\n"
        results += "\n\n".join(self.mercenarycompanies) + "\n"
        results += "\n"
        results += "## Dueling Colleges\n"
        results += "\n\n".join(self.duelingcolleges) + "\n"
        results += "\n"
        results += "## Mage Schools\n"
        results += "\n\n".join(self.mageschools) + "\n"
        results += "\n"
        results += "## Religious Organizations\n"
        results += "\n\n".join(self.religiousgroups) + "\n"
        results += "\n"
        results += "## Monastic Orders\n"
        results += "\n\n".join(self.monasticorders) + "\n"
        results += "\n"
        results += "## Rogues' Guilds\n"
        results += "Like any city, " + self.name + " has its share of crimincals and seedy activity; however, the Rogues' Guilds that prominently domainte that activity include:\n\n"
        results += "\n\n".join(self.roguesguilds) + "\n"
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
                burb.calculate()
                outfile.write(burb.formatmd())
    else:
        parser.print_help()
        exit()


if __name__ == '__main__':
	main()
