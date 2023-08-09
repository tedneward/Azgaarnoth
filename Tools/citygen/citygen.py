#!/usr/bin/env python3

import argparse
import csv
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
        self.province = ''
        self.geography = ''
        self.features = []
        self.authorities = []
        self.populationct = 0
        self.populationbreakdown = { 'Human': 0, 'Firstborn' : 0, 'Created': 0, 'Hordish': 0}
        self.military = []
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
        self.populationct = row[8]

    def formatmd(self):
        results = f"# {self.name} [{self.state}](../Nations/{self.state}.md)\n"
        results += f"**Population:** {self.populationct} -- {self.populationbreakdown}"
        return results

burbs = []

def parsecsv(csvfilename):
    results = []
    with open(csvfilename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        burb_count = -1
        for row in csv_reader:
            if burb_count == -1:
                print(f'Column names are {", ".join(row)}')
                burb_count = 0
            else:
                print(f'\t{row[1]} is in the {row[2]} province of {row[4]}.')
                burb = City()
                burb.parsecsvrow(row)
                results.append(burb)
                burb_count += 1
        print(f'Processed {burb_count} lines.')
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
    parser.add_argument('--out', help='Directory to which to write generated cities')
    args = parser.parse_args()

    global burbs
    if args.parsecsv != None:
	    burbs = parsecsv(args.parsecsv)
    elif args.parsemd != None:
	    burbs = parsemd(args.parsemd)
    else:
        parser.print_help()
        exit()

    for burb in burbs:
        print(burb.formatmd())

if __name__ == '__main__':
	main()
