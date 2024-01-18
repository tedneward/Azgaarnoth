#!/usr/bin/env python3

import argparse
import csv
import random
import os
import sys
import namegen as NameGenerator

# This script takes the CSV from the Azgaar tool and fleshes out cities
# ("burbs") with some greater detail. Honestly, really should only need
# to be run once across all the cities in Azgaarnoth, and generate a ton
# of detail pages into /Cities, but I don't know yet if I'll want to
# re-run for particular cities or not.

def existingorg(orgtype, directory):
    orgs = os.listdir(directory)
    orgs.remove('index.md')
    if 'Code.md' in orgs:
        orgs.remove('Code.md')
    filename = directory + '/' + orgs[random.randint(0, len(orgs)-1)]
    org = open(filename, 'r').readlines()[0][len(f'# {orgtype}: '):-1]
    return (org, filename)

def randreligion():
    religions = ["[Al'Uma - Prophet](../Religions/AlUma.md)", "[Al'Uma - Disciple](../Religions/AlUma.md)",
                 '[Dail](../Religions/Dail.md)', '[Druidism]((../Religions/Druidism.md))', 
                 '[Kaevarian Church](../Religions/KaevarianChurch.md)', 
                 'Pantheon', 
                 '[Spiritualism](../Religions/Spirits.md)', 
                 '[Trinitarian Church](../Religions/Trinitarian.md)']
    religion = religions[random.randint(0, len(religions)-1)]
    if religion == 'Pantheon':
        gods = os.listdir('../../Religions/Pantheon')
        gods.remove('index.md')
        return gods[random.randint(0, len(gods)-1)][:-3]
    else:
        return religion

def namegen(which):
    if which == 'roguesguild':
        if random.randint(0,100) > 50:
            guilds = os.listdir('../../Organizations/RoguesGuilds')
            guilds.remove('index.md')
            guild = open('../../Organizations/RoguesGuilds/' + guilds[random.randint(0, len(guilds)-1)], 'r').readlines()[0][len('# Rogues Guild: '):-1]
            return guild
    elif which == 'mageschool':
        if random.randint(0, 100) > 60:
            schools = os.listdir('../../Organizations/MageSchools')
            schools.remove('index.md')
            school = open('../../Organizations/MageSchools/' + schools[random.randint(0, len(schools))], 'r').readlines()[0][len('# Mage School: '):-1]
            return school
    elif which == 'duelingcollege':
        pass
    elif which == 'merchantguild':
        if random.randint(0, 100) > 60:
            guilds = os.listdir('../../Organizations/MerchantGuilds')
            guilds.remove('index.md')
            guild = open('../../Organizations/MerchantGuilds/' + guilds[random.randint(0, len(guilds)-1)], 'r').readlines()[0][len('# Merchant Guild: '):-1]
            return guild
    elif which == 'mercenarycompany':
        if random.randint(0, 100) > 50:
            mercs = os.listdir('../../Organizations/MercCompanies')
            mercs.remove('index.md')
            merc = open('../../Organizations/MercCompanies/' + mercs[random.randint(0, len(mercs)-1)], 'r').readlines()[0][len('# Mercenary Company: '):-1]
            return merc
    elif which == 'house':
        return "**GREAT HOUSE**"

    # If we're still here, then let's gen a name
    return NameGenerator.namegen(which)

def dieroll(dpattern):
    (number, size) = dpattern.split("d")
    if number == '': number = 1
    accum = 0
    for _ in range(int(number)):
        accum += random.randint(1, int(size))
    return accum


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
        self.religiousgroups = []
        self.monasticorders = []


    # Based https://donjon.bin.sh/fantasy/demographics/medieval-demographics-made-easy.pdf
    # Villages range from 20 to 1,000 people, with most in 50-300 range. Agrarian communities.
    # Towns range 1,000-8,000, with most around 2,500. Tend to have walls only if they're 
    # politically important or frequently threatened.
    # Cities 8,000 to 12,000. Universities tend to be in cities of this size
    # Big cities: 12,000 to 100,000. Where large arteries of traffic converge.
        
    def gendemographics(self):
        popdensity = 0
        if self.state == '':
            popdensity = dieroll('6d4') * random.randint(5, 8)
        else:
            densities = {
                'Dense province name': 7,
                'Sparse province name': 1
            }
            if self.province in densities.keys():
                popdensity = dieroll('6d4') * densities[self.province]
            else:
                popdensity = dieroll('6d4') * random.randint(5, 8)

    def genbusinesses(self):
        business = {
            "Shoemakers": 150,
            "Furriers": 250,
            "Servants": 250,
            "Tailors": 250,
            "Barbers": 350,
            "Jewelers": 400,
            "Taverns": 400,
            "Pastrycooks": 500,
            "Masons": 500,
            "Carpenters": 550, 
            "Weavers": 600,
            "Chandlers": 700, # Only if docks
            "Mercers": 700,
            "Coopers": 700,
            "Bakers": 800,
            "Watercarriers": 850,
            "Winesellers": 900,
            "Hatmakers": 950,
            "Saddlers": 1000,
            "Pursemakers": 1100,
            "Woodsellers": 2400,
            "Magic shops": 2800,
            "Bookbinders": 3000,
            "Butchers": 1200,
            "Fishmongers": 1200,
            "Beersellers": 1400,
            "Buckle-makers": 1400,
            "Plasterers": 1400,
            "Spice merchants": 1400,
            "Blacksmiths": 1500,
            "Painters": 1500,
            "Doctors": 350,
            "Roofers": 1800,
            "Locksmiths": 1900,
            "Bathhouses": 1900,
            "Ropemakers": 1900,
            "Inns": 2000,
            "Tanners": 2000,
            "Copyists": 2000,
            "Sculptors": 2000,
            "Rugmakers": 2000,
            "Cutlers": 2300,
            "Glovemakers": 2400,
            "Woodcarvers": 2400,
            "Booksellers": 6300,
            "Illuminators": 3900,
            "Legal advocates": 650,
            "Clergy": 40,
            "Priest": 150
        }
        numbers = {}
        for (name, sv) in business.items():
            sv += (dieroll('4d4') - 6) * 10
            if self.populationct < sv:
                if random.randint(1, 100) < int((self.populationct / sv) * 100):
                    numbers[name] = 1
            else:
                numbers[name] = self.populationct // sv

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
        self.latitude = float(row[9])
        self.longitude = float(row[10])
        self.elevation = row[11]

        if row[12] != '':
            self.capital = True
            self.description.append(f"**Capital.** {self.name} is the capital of {self.state}, and ...")
        if row[13] != '':
            self.port = True
            self.militaryunits.append(f"**Marines.** These are typically rotated between port guard duty, tariff duty in incoming vessels, and extended patrols out into the waters around {self.name}. **TODO**")
            self.description.append(f"**Docks.** {self.name} boasts a port for maritime shipping....")
        if row[14] != '':
            self.citadel = True
            if self.populationct > 5000:
                self.militaryunits.append("**Palace Guard.** These typically rotate between citidel guard duty and special missions as dictated by city authorities. 75xFighter 3-5, 20xWizard/Sorcerer 3-5, 30xCleric/Druid 3-5, 25xRogue 3-5.")
                self.description.append(f"**Citadel.** {self.name} retains a citadel for the upper ranks and guests, and much of the elite guard resides there.")
            else:
                self.description.append(f"**Citadel.** An ancient citadel stands within {self.name}'s city limits, but currently is all but abandoned.")
        if row[15] != '':
            self.walls = True
            wallprob = random.randint(1,100)
            if  wallprob > 50:
                self.description.append("**City Walls.** The walls are in good shape, kept in good order by the city authorities.")
            elif wallprob > 25:
                self.description.append("**City Walls.** The city walls still stand, but clearly have seen neglect over the years.")
            else:
                self.description.append(f"**City Walls.** {self.name}'s walls are crumbling and in disrepair, with obvious gaps from previous sieges or battles still as yet unrepaired.")
        if row[16] != '':
            self.plaza = True
            if self.populationct > 10000:
                self.description.append(f"**Plaza.** {self.name}'s city center boasts a large plaza, called **TODO**, which is a central place in the lives of many within the city.")
            elif self.populationct > 5000:
                self.description.append(f"**Plaza.** {self.name}'s city center has a central plaza that provides common, day-to-day shopping and farmer's markets, made up primarily of foodstuff's and artisan's shops.")
            else:
                self.description.append("**Plaza.** The city has a central area of shops which sees much traffic. Already several fountains and other decorative statues mark the rough edges of this plaze.")
        if row[17] != '':
            self.temple = True
            self.description.append("**Temple.** A large temple to **TODO** here sits near to the city center.")
        if row[18] != '':
            self.shantytown = True
            poppercent = (random.randint(1, 8) * 5) 
            desc = f"**Shantytown.** {self.name}'s shantytown is home to roughly {poppercent}% of the city. "
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

    ###### Some leader-type generations
    def genleader(self, title):
        def randomoption(dictoptions):
            roll = random.randint(1, 100)
            accum = 0
            for (option, chance) in dictoptions.items():
                if roll <= (accum + chance):
                    return option
                else:
                    accum += chance
            return "We rolled {roll} against {dictoptions} and nothing came back?!?"
        
        townlevels = { 4: 30, 5: 40, 6: 30 }
        citylevels = { 7: 20, 8: 20, 9: 20, 10: 20, 11: 10, 12: 10 }
        levels = townlevels if self.populationct < 10000 else citylevels

        if title == 'City Guard':
            classdict = { "Fighter": 60, "Paladin": 20, "Rogue": 10, "Cleric": 5, "Wizard": 5 }
            return f"{randomoption(classdict)} {randomoption(citylevels)}"
        elif title == 'Town Guard':
            classdict = { "Fighter": 65, "Paladin": 15, "Rogue": 10, "Cleric": 5, "Wizard": 5 }
            return f"{randomoption(classdict)} {randomoption(townlevels)}"
        elif title == 'Mercenary Captain':
            classdict = { "Fighter": 60, "Rogue": 20, "Ranger": 10, "Cleric": 5, "Wizard": 5 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        elif title == 'Arcane Master':
            classdict = { "Wizard": 40, "Sorcerer": 40, "Warlock": 20 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        elif title == 'High Priest':
            classdict = { "Cleric": 55, "Paladin": 20, "Druid": 15, "Warlock": 10 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        elif title == 'Grand Sensei':
            classdict = { "Monk": 85, "Mystic": 15 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        elif title == 'Dueling College':
            classdict = { "Fighter": 35, "Rogue": 25, "Monk": 10, "Ranger": 10, "Barbarian": 10, "Bard": 5, "Wizard": 5 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        elif title == 'Rogues Guild':
            classdict = { "Rogue": 50, "Fighter": 10, "Monk": 10, "Ranger": 10, "Wizard": 10, "Warlock": 5, "Bard": 5 }
            return f"{randomoption(classdict)} {randomoption(levels)}"
        else:
            return f"Unknown leader type: {title}"

    def calculate(self):
        # This is temporary, until the CSV data is finally not needed anymore
        self.populationct = int(self.populationct * random.randint(20, 30)) // 1000 * 100

        self.calculatepopulationbreakdown()
        self.calculateauthorities()
        self.calculatemilitia()
        self.calculateduelingcolleges()
        self.calculatemercenaries()
        self.calculatemageschools()
        self.calculatereligiousgroups()
        self.calculateroguesguilds()
        self.calculatemerchantguilds()
        self.calculatemonasticorders()

    def calculatepopulationbreakdown(self):
        pass

    def calculateauthorities(self):
        # Police chief/law enforcement
        if self.populationct > 10000:
            # The Guard
            self.militaryunits.append("**City Guard.** **TODO**")
            # Captain of the Guard
            self.authorities.append(f"**TODO**, {self.genleader('City Guard')}, Captain of the City Guard")
        else:
            self.militaryunits.append("**Town Guard.** **TODO**")
            self.authorities.append(f"**TODO**, {self.genleader('Town Guard')}, Captain of the Town Guard")

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
    
    def calculatemercenaries(self):
        nummercs = 0

        # How many mercs are associated here?
        # Really, this should be tripled or more for all cities in Chidia
        nummercs = int(self.populationct // 5000)
        if nummercs > 3: nummercs = 3

        for _ in range(nummercs):
            merc = namegen('mercenarycompany')
            self.mercenarycompanies.append(f'**[{merc}](../Organizations/MercCompanies/{merc}.md)**')
            self.authorities.append(f"**TODO**, {self.genleader('Mercenary Captain')}, Captain - {merc}")

    def calculatemageschools(self):
        # How many schools are here? 1 per 7500 population?
        numschools = int(self.populationct // 7500)

        for _ in range(numschools):
            schoolpop = random.randint(1,3) * (self.populationct // 7500)
            if random.randint(0, 100) > 25:
                (school, link) = existingorg('Mage School', '../../Organizations/MageSchools')
                self.mageschools.append(f'**[{school}]({link}).** The school currently has {schoolpop * 2} active members.')
                self.authorities.append(f"**TODO**, {self.genleader('Arcane Master')}, Arcane Master, [{school}]({link})")
            else:
                school = namegen('mageschool')
                self.mageschools.append(f'**{school}.** The school currently has {schoolpop} active members.')
                self.authorities.append(f"**TODO**, {self.genleader('Arcane Master')}, Arcane Master, {school}")

    def calculatereligiousgroups(self):
        numgroups = int(self.populationct // 7500)

        for _ in range(numgroups):
            god = randreligion()
            pop = random.randint(10, 20) * int(self.populationct // 100)
            self.religiousgroups.append(f'**Temple.** The temple to {god} has around {pop} followers.')
            self.authorities.append(f"**TODO**, {self.genleader('High Priest')}, High Priest of {god}")

    def calculatemerchantguilds(self):
        numguilds = self.populationct // 5000
        if self.shantytown:
            numguilds /= 2
        numguilds += len(self.militaryunits)

        numguilds += random.randint(-2, 2)
        if numguilds < 0: numguilds = 0

        for _ in range(int(numguilds)):
            if random.randint(0, 100) <= 25:
                (guild, link) = existingorg('Merchant Guild', '../../Organizations/MerchantGuilds')
                self.merchantguilds.append(f'**[{guild}](../Organizations/MerchantGuilds/{link})**')
                self.authorities.append(f'**TODO**, Guildmaster - {guild}')
            else:
                guild = namegen('merchantguild')
                self.merchantguilds.append(f'**{guild}**')
                self.authorities.append(f'**TODO**, Guildmaster - {guild}')
    
    def calculatemonasticorders(self):
        numorders = int(self.populationct // 15000)

        for _ in range(numorders):
            pop = random.randint(10, 50)
            name = namegen('monasticorder')
            self.monasticorders.append(f'**Monastic Order: {name}.** The order currently has {pop} monks.')
            self.authorities.append(f"**TODO**, {self.genleader('Grand Sensei')} Grand Sensei of the {name} monastic order")

    def calculateduelingcolleges(self):
        numcolleges = len(self.militaryunits)
        if len(self.mercenarycompanies) > 0:
            numcolleges += len(self.mercenarycompanies)
        if self.populationct < 10000:
            numcolleges -= 1
        if self.populationct < 5000:
            numcolleges -= 1
        if self.populationct < 2500:
            numcolleges -= 1

        numcolleges += random.randint(-2, 2)
        if numcolleges < 0: numcolleges = 0

        for _ in range(numcolleges):
            dc = namegen('duelingcollege')
            self.duelingcolleges.append(dc)
            self.authorities.append(f"**TODO**, {self.genleader('Dueling College')}, Head of the {dc} dueling college")

    def calculateroguesguilds(self):
        numguilds = self.populationct // 5000
        if self.shantytown:
            numguilds *= 2
        numguilds -= len(self.militaryunits)

        numguilds += random.randint(-2, 2)
        if numguilds < 0: numguilds = 0

        for _ in range(numguilds):
            if random.randint(0, 100) <= 25:
                (guild, link) = existingorg('Rogues Guild', '../../Organizations/RoguesGuilds')
                self.roguesguilds.append(f'**[{guild}]({link})**')
                self.authorities.append(f'**TODO**, Guildmaster, [{guild}]({link})')
            else:
                guild = namegen('roguesguild')
                self.roguesguilds.append(f'**{guild}**')
                self.authorities.append(f'**TODO**, Guildmaster, {guild}')
    
    def formatmd(self):
        results = f"# {self.name}\n"
        if self.province != '':
            results += f"*({self.province}, [{self.state}](../Nations/{self.state}.md))*\n"
        else:
            results += f"*([{self.state}](../Nations/{self.state}.md))*\n"
        results += "\n"
        results += f"**Population:** {self.populationct}  "
        results += (f"*(Humans: {self.populationbreakdown['Human']}, " + 
            f"Firstborn: {self.populationbreakdown['Firstborn']} " + 
            f"Created: {self.populationbreakdown['Created']} " + 
            f"Hordish: {self.populationbreakdown['Hordish']})*\n\n")
        results += "\n\n".join(self.description) + "\n"
        results += "\n"
        results += "## Geography\n"
        results += "\n"
        results += f"![]({self.name}.jpeg)\n"
        results += "\n"
        results += f"Latitude: {self.latitude}, Longitude: {self.longitude}\n"
        results += "\n"
        results += f"City Elevation: {self.elevation}\n"
        results += "\n"
        results += "## Prominent Figures\n"
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

states = ['Alalihat', 'Almalz', 'Zabalasa', 'Liria', 'Mighalia', 
            'Travesimia', 'Bagonbia', 'Whaveminsia', 'Travenia','Dradehalia', 
            'Tragekia', 'Ulm', 'Yithi', 'Zhi']
def main():
    parser = argparse.ArgumentParser(
                    prog='CityGen',
                    description='A tool for generating random settings for a city',
                    epilog='Written in Python with love')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--parsemd', help='CSV file to use as input database')
    parser.add_argument('--parsecsv', help='CSV file to use as input database')
    parser.add_argument('--out', help='Target directory for any written files')
    parser.add_argument('--writeindex', choices=states + ['all'], help='Create an index.md page for all cities in given state')
    parser.add_argument('--writecities', choices=states + ['all'], help='Write out MD descriptions of cities for given state')
    parser.add_argument('--writecity', help='Write out MD description of specific city passed')
    args = parser.parse_args()

    global burbs
    if args.parsecsv != None:
        burbs = parsecsv(args.parsecsv)
    elif args.parsemd != None:
        burbs = parsemd(args.parsemd)

    target = ''
    if args.out == None:
        target = '.'
    else:
        target = args.out

    if args.writeindex != None:
        if args.writeindex == 'all':
            with open(target + "/index.md", 'w') as outfile:
                print("# Cities in Azgaarnoth\n\n")
                for state in states:
                    outfile.write(f"## [{state}](../Nations/{state}.md)")
                    stateburbs = list(filter(lambda city: city.state == state, burbs))
                    stateburbs.sort(key=lambda city: city.name)
                    for burb in stateburbs:
                        outfile.write(f"* [{burb.name}]({burb.name}.md) *({burb.province})*")
                    outfile.write("\n")
        else:
            with open(target + "/" + args.writeindex + ".md", 'w') as outfile:
                stateburbs = list(filter(lambda city: city.state == state, burbs))
                stateburbs.sort(key=lambda city: city.name)
                for burb in stateburbs:
                    outfile.write(f"* [{burb.name}]({burb.name}.md) *({burb.province})*")
                outfile.write("\n")

    elif args.writecities != None:
        if args.writecities == 'all':
            for burb in burbs:
                with open(target + "/" + burb.name + ".md", 'w') as outfile:
                    burb.calculate()
                    outfile.write(burb.formatmd())
        else:
            stateburbs = list(filter(lambda city: city.state == state, burbs))
            stateburbs.sort()
            for burb in stateburbs:
                with open(target + "/" + burb.name + ".md", 'w') as outfile:
                    burb.calculate()
                    outfile.write(burb.formatmd())
    elif args.writecity != None:
        cityname = args.writecity
        burb = list(filter(lambda city: city.name == cityname, burbs))[0]
        with open(target + "/" + burb.name + ".md", 'w') as outfile:
            burb.calculate()
            outfile.write(burb.formatmd())
    else:
        parser.print_help()


if __name__ == '__main__':
	main()
