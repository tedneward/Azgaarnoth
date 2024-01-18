#!/usr/bin/env python3

import argparse
import random
import os
import namegen as NameGenerator

quiet = False
verbose = False
scripted = False

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

def randompick(list):
    return list[random.randint(0, len(list)-1)]

REPOROOT = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../../') + "/"

def getexistingorgs(path, title):
    results = []
    orgfiles = os.listdir(REPOROOT + path)

    # Exceptions
    if 'index.md' in orgfiles: orgfiles.remove('index.md')
    if 'Code.md' in orgfiles: orgfiles.remove('Code.md')

    for file in orgfiles:
        name = open(REPOROOT + path + '/' + file).readlines()[0][len(f'# {title}: '):-1]
        results.append((name, file))
    return results

bardiccolleges = getexistingorgs('/Organizations/BardicColleges', 'Bardic College')
duelingcolleges = getexistingorgs('/Organizations/DuelingColleges', 'Dueling College')
houses = getexistingorgs('/Organizations/Houses', 'Great House')
mageschools = getexistingorgs('/Organizations/MageSchools', 'Mage School')
mercs = getexistingorgs('/Organizations/MercCompanies', 'Mercenary Company')
guilds = getexistingorgs('/Organizations/MerchantGuilds', 'Merchant Guild')
monasticorders = getexistingorgs('/Organizations/MonasticOrders', 'Monastic Order')
rogues = getexistingorgs('/Organizations/RoguesGuilds', 'Rogues Guild')

def orggen(which):
    #if which == 'bardiccollege':
    #    pass
    #elif which == 'duelingcollege':
    #    pass
    if which == 'house':
        if random.randint(0, 100) > 50:
            (name, file) = randompick(houses)
            return f"[{name}]({file})"
    elif which == 'mageschool':
        if random.randint(0, 100) > 60:
            (name, file) = randompick(mageschools)
            return f"[{name}]({file})"
    elif which == 'mercenarycompany':
        if random.randint(0, 100) > 50:
            (name, file) = randompick(mercs)
            return f"[{name}]({file})"
    elif which == 'merchantguild':
        if random.randint(0, 100) > 60:
            (name, file) = randompick(guilds)
            return f"[{name}]({file})"
    elif which == 'roguesguild':
        if random.randint(0,100) > 50:
            (name, file) = randompick(rogues)
            return f"[{name}]({file})"

    return NameGenerator.namegen(which)

for _ in range(50):
    which = randompick(['house', 'mageschool', 'mercenarycompany', 'tavern', 'monasticorder'])
    print(which, orggen(which))
