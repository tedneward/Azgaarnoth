#!/usr/bin/env python3

import argparse
import csv
import random
import os
import sqlite3
import sys
import namegen as NameGenerator

quiet = False
verbose = False

def error(*values):
    print(*values)

def warn(*values):
    if not quiet:
        print("WARNING: ", end='')
        print(*values)

def log(*values):
    if verbose and not quiet:
        print(*values)

def dieroll(dpattern):
    (number, size) = dpattern.split("d")
    if number == '': number = 1
    accum = 0
    for _ in range(int(number)):
        accum += random.randint(1, int(size))
    return accum


"""
Generate a random number that is between min and max, but weighted (50%)
to be withiin avgmin and avgmax.
"""
def between(min, avgmin, avgmax, max):
    majorrange = random.randint(0, 100)
    # 76-100 you're above the avgmax
    if majorrange > 75:
        return random.randint(avgmax, max)
    # 26 - 75 you're in the avg range
    elif majorrange > 25:
        return random.randint(avgmin, avgmax)
    # 0 - 25 you're below the avgmin
    else:
        return random.randint(min, avgmin)

REPOROOT = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../../') + "/"

states = ['Alalihat', 'Almalz', 'Zabalasa', 'Liria', 'Mighalia', 
            'Travesimia', 'Bagonbia', 'Whaveminsia', 'Travenia','Dradehalia', 
            'Tragekia', 'Ulm', 'Yithi', 'Zhi']
continents = ["Al'Uma",'Bedia','Chidia','Dradehalia','Liria','Tragekia','Travenia','Yithia']

"""
City is a domain object for all kinds of permanent settlements, ranging in size from 20
to 100,000 individuals (or more!). A city belongs to a state, in a province, and is affected
by the surrounding region (province's) population density (which I will probably want to
track somewhere in the future).
"""
class City:
    def __init__(self):
        self.name = ''
        self.state = ''
        self.description = []
        self.province = ''
        self.geography = ''

        self.populationct = 0
        self.populationbreakdown = { 
            'Human': 0, 
            'Firstborn' : 0, 
            'Created': 0, 
            'Hordish': 0 
        }

        self.features = {
            'Capital': False,
            'Port': False,
            'Citadel': False,
            'Walls': False,
            'Plaza': False,
            'Shantytown': False
        }

        self.authorities = []
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

    def calculatepopulationbreakdown(self, human, firstborn, created, hordish):
        # Make sure incoming ranges add up to 100
        if human + firstborn + created + hordish != 100:
            error("Population breakdowns don't add up correctly")
            return

        # Now let's randomize the values a bit
        for _ in range(5):
            # Choose the deviation
            pts = random.randint(0, 5)
            # Pick one of the four categories to go up by a few points
            choice = random.randint(1, 4)
            if choice == 1: human += pts
            elif choice == 2: firstborn += pts
            elif choice == 3: created += pts
            elif choice == 4: hordish += pts
            # Pick one of the four categories to go down by the same
            choice = random.randint(1, 4)
            if choice == 1: human -= pts
            elif choice == 2: firstborn -= pts
            elif choice == 3: created -= pts
            elif choice == 4: hordish -= pts

        # That's our breakdown
        log("Breakdown (percentages): ",human,firstborn,created,hordish)
        self.populationbreakdown['Human'] = (self.populationct // 100) * human
        self.populationbreakdown['Firstborn'] = (self.populationct // 100) * firstborn
        self.populationbreakdown['Created'] = (self.populationct // 100) * created
        self.populationbreakdown['Hordish'] = (self.populationct // 100) * hordish
        log("Population: ",self.populationct,"(",self.populationbreakdown,")")

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
        results += "## Nobility and the Great Houses\n"
        results += "\n\n".join(self.houses) + "\n"
        results += "\n"
        results += "## Military Units of Note\n"
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
        results += "## Merchant Guilds\n"
        results += "\n\n".join(self.merchantguilds) + "\n"
        results += "\n"
        results += "## Rogues' Guilds\n"
        results += "\n\n".join(self.roguesguilds) + "\n"
        results += "\n"

        return results

# Population breakdowns
popbreakdowns = {
    # Al'Uman
    'Alalihat' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Almalz' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Zabalasa' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    # Lirian and "Western" nations
    'Liria' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Mighalia' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Travesimia' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Bagonbia' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Whaveminsia' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 }, 
    'Travenia' : { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0 },
    # Dradehalia
    'Dradehalia' : { 'Human': 40, 'Firstborn' : 40, 'Created': 10, 'Hordish': 10 }, 
    # Hordish Nations
    'Tragekia' : { 'Human': 20, 'Firstborn' : 10, 'Created': 20, 'Hordish': 50 },
    'Ulm' : { 'Human': 10, 'Firstborn' : 10, 'Created': 20, 'Hordish': 60 },
    'Yithi' : { 'Human': 30, 'Firstborn' : 20, 'Created': 15, 'Hordish': 35 },
    'Zhi' : { 'Human': 25, 'Firstborn' : 15, 'Created': 15, 'Hordish': 45 }
}

out = None
def main():
    global verbose
    global quiet
    global out

    parser = argparse.ArgumentParser(
                    prog='TownGen',
                    description='A tool for generating random settings for a village or town',
                    epilog='Written in Python with love')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--verbose', choices=['quiet', 'verbose'])
    parser.add_argument('--out', default=".", help='Target directory for any written files')
    parser.add_argument('--size', choices=['Village', 'Town', 'City'], help="Town, village, city, ...?")
    parser.add_argument('--pop', help="Specify a population count")
    parser.add_argument('--density', choices=['Desolate', 'Low', 'Settled', 'Average', 'High', 'Maximum'], help="Surrounding population density")
    parser.add_argument('--state', choices=states, help="The nation this town is in")
    parser.add_argument('--options', choices=['Capital','Port','Citadel','Walls','Plaza','Temple','Shantytown'], help="Various features to generate")
    args = parser.parse_args()
    log(args)

    city = City()

    if args.verbose != None:
        if args.verbose == 'verbose':
            verbose = True
        elif args.verbose == 'quiet':
            quiet = True

    # Figure out burb population
    if args.pop == None:
        if args.size == None:
            error("TownGen: error: If you don't specify the pop, you must specify a size")
            parser.print_usage()
        elif args.size == 'Village':
            log("We're building a village.")
            city.populationct = between(20, 30, 50, 100)
        elif args.size == 'Town':
            log("We're building a town!")
            city.populationct = between(200, 300, 500, 1000)
        elif args.size == 'City':
            log("We're building a city!!")
            city.populationct = between(2000, 3000, 10000, 50000)
    else:
        city.populationct = int(args.pop)

    # ... and population breakdown
    if args.state == None:
        error("We can't determine population breakdown without knowing where this is at")
        return
    popbd = popbreakdowns[args.state]
    city.calculatepopulationbreakdown(popbd['Human'], popbd['Firstborn'], popbd['Created'], popbd['Hordish'])

if __name__ == '__main__':
	main()
