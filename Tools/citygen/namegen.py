#!/usr/bin/env python3

import argparse
import os
import random

def namegen(which):
    def oneof(options):
        return options[random.randint(0, len(options)-1)]
    def replace(phrase):
        mappings = {
            'Abstract' : abstracts,
            'Adjective' : adjectives,
            'Animal' : animals,
            'Arcane' : arcane,
            'Building' : buildings,
            'College' : colleges,
            'Feature' : features,
            'Geographical' : geographical,
            'Guild' : guilds,
            'Humanoid' : humanoids,
            'Instrument' : instruments,
            'Location' : locations,
            'Noun' : nouns,
            'Numeric' : numeric,
            'Militant' : militants,
            'Royalty' : royalty,
            '_Tavern' : taverns,
            'Weapon' : weapons
        }
        done = False
        while not done:
            found = False
            for (keyword, repls) in mappings.items():
                if phrase.find(keyword) > -1:
                    phrase = phrase.replace(keyword, repls[random.randint(0, len(repls)-1)], 1)
                    found = True
            
            if not found: done = True

        return phrase

    abstracts = [
        'Harmony', 'Light', 'Dark', 'Soul', 'Abyss', 'Star', 'Shadows', 
        'Earth', 'Air', 'Fire', 'Water', 'Coil', 'Endless Night',
        'Soul', 'Mind', 'Body', 'Sun', 'Moon', 'Winds',
    ]
    adjectives = [ 
        'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Sanguine', 'Sepia', 'Ochre',
        'Puce', 'Navy', 'Maroon', 'Pink', 'Peach', 'Cyan', 'Violet', 'Brown', 'Black',
        'Gray', 'White', 'Silver', 'Gold', 'Jumping', 'Sleeping', 'Running', 'Rolling',
        'Laughing', 'Singing', 'Flying', 'Burning', 'Swimming', 'Crying', 'Roaring',
        'Screaming', 'Silent', 'Petrified', 'Hiding', 'Hidden', 'Lost', 'Forgotten',
        'Shiny', 'Drowning', 'Giant', 'Tiny', 'Fat', 'Skinny', 'Humorous', 'Lonely',
        'Drunken', 'Slimy', 'Undead', 'Dark', 'Bright', 'Magical', 'Enchanted', 'Poor',
        'Wealthy', 'Lucky', 'Unfortunate', 'Angry', 'Happy', 'Sad', 'Thieving', 'Desperate',
        'Divine', 'Arcane', 'Profane', 'Discreet', 'Buried', 'False', 'Foolish',
        'Flatulent', 'Hypnotic', 'Haunted', 'Special', 'Fun', 'Drab', 'Daring', 'Stubborn',
        'Sober', 'Talking', 'Naked', 'Suffering', 'Cheap', 'Smelly', 'Easy', 'Heroic',
        'Hovering', 'Married', 'Pious', 'Pompous', 'Illegal', 'Sacred', 'Defiled', 'Spoilt',
        'Wooden', 'Bloody', 'Yawning', 'Sleepy', 'Hungry','Shining', 'Gleaming', 'Barking',
        'Vorpal', 'Savage', 'Stout', 'Slow', 'Dull', 'Soaked', 'Drunken', 'Fabulous', 'Crooked',
        'Noble', 'Soft', 'Broken', 'Shattered', 'Mighty', 'Strong', 'Lonely', 'Poor', 'Old',
        'Generous', 'Lanky', 'Hapless', 'Tall', 'Remarkable', 'Frugal', 'Prudent', 'Foul',
        'Evil', 'Good', 'Rotten', 'Shining', 'Fragile', 'Hungry', 'Tired', 'Patient', 'Merciful',
        'Immortal', 'Faithful', 'Friendly', 'Forlorn', 'Adoring', 'Brittle', 'Floating',
        'Sharp', 'Worn', 'Cursed', 'Beautiful', 'Beloved', 'Quiet', 'Happy', 'Courageous',
        'Wounded', 'Blind', 'Clairvoyant', 'Wishing', 'Calm', 'Wary', 'Cheerful', 'Wise',
        'Clumsy', 'Boorish', 'Boastful', 'Humble', 'Sly', 'Daring', 'Rebellious', 'Diligent',
        'Disguised', 'Ominous', 'Determined', 'Reliable', 'Loyal', 'Raging', 'Excited',
        'Shy', 'Golden', 'Frozen', 'Gracious', 'Hairy', 'Hoarse', 'Honest', 'Deceptive',
        'Limping', 'Lively', 'Lucky', 'Lean', 'Nefarious', 'Crazy'
    ]
    animals = [
        'Rooster', 'Hound', 'Elk',  'Cat', 'Flounder', 'Whale', 'Pegasus', 'Mastiff', 
        'Dog', 'Wolf', 'Fox', 'Puma', 'Cat', 'Lion', 'Tiger', 'Kitten', 'Ox', 'Cow',
        'Sow', 'Bull', 'Calf', 'Horse', 'Stallion', 'Mare', 'Foal', 'Owl', 'Eagle',
        'Falcon', 'Hawk', 'Raven', 'Crow', 'Gull', 'Fish', 'Whale', 'Shark', 'Octopus',
        'Squid', 'Goat', 'Sheep', 'Ewe', 'Fly', 'Butterfly', 'Dragonfly', 'Beetle', 'Ant',
        'Wasp', 'Termite', 'Louse', 'Worm', 'Lizard', 'Frog', 'Toad', 'Snake', 'Chameleon',
        'Unicorn', 'Gryphon', 'Dragon', 'Wyvern', 'Roc', 'Clam', 'Oyster', 'Starfish', 'Slug',
        'Snail', 'Mouse', 'Rat', 'Beaver', 'Marten', 'Mink', 'Otter', 'Seal', 'Manatee',
        'Swallow', 'Drake', 'Monkey', 'Viper', 'Crane', 'Mantis', 'Bear', 
        'Chipmunk', 'Squirrel', 'Gopher', 'Goose', 'Duck', 'Rat',
    ]
    arcane = [ 
        'Infinite', 'Miasmal', 'Nonesuch', 'Chthonic', 'Celestial', 'Spiral', 'Silver', 'Gold',
        'Crimson', 'Silent', 'Bronze', 'Colossal', 'Elemental', 'Gilded', 'Shimmering', 'Eldritch',
        'Immaculate', 'Fey', 'Astral', 'Chaos', 'Enduring', 'Everlasting', 'Mercury', 'Night', 
        'Midnight', 'Raven', 'Grey', 'Fire', 'Dusk', 'Nightshade', 'Reviled', 'Umbral', 'Stained', 
        'Cursed', 'Long', 'Tranquil', 'Blue', 'Green', 'Gold', 'Verdant', 'Radiant', 'Silent',
        'Focused', 'Elemental', 'Harmonic'
    ]
    buildings = [ 
        'Cylinder', 'Minaret', 'Monument', 'Pylon', 'Tower', 'Spire', 'Turret', 'Column', 
        'Obelisk', 'Rock', 'Eye', 'Tome', 'Citadel', 'Fortress', 'Arch', 'Castle', 'Keep',
        'Outpost', 'Watchpost', 'Spire',
    ]
    colleges = [
        'College', 'University', 'School', 'Hall', 'Conservatory', 'Academy', 'Society', 'Institute',
        'Fraternity', 'Sorority', 'Lyceum', 'Study', 'Fellowship', 'Band', 'Body', 'Lodge'
    ]
    features = [
        'Flower', 'Petal', 'Tree', 'Woods', 'Mountain', 'Falls', 'Swamp', 'Fens', 'Forest',
        'River', 'Lake', 'Sea', 'Badlands', 'Grasslands', 'Cliffs', 'Hills',
    ]
    geographical = [ 
        'Lirian', 'Whaveminsian', 'Tragekian', 'Yithian', "Zhian", 'Ravenian', 'Mighalian',
        'Bedian', 'Tragekian', 'Northern', 'Eastern', 'Western', 'Southern']
    guilds = [ 
        'Compact', 'Company', 'Pact', 'Guild', 'Contract', 'Order', 'Alliance',
        'Federation', 'College', 'League', 'Group', 'Lodge', 'Order', 'Society', 'Trade', 
        'Union', 'Association', 'Club', 'Brotherhood', 'Confederation', 'Faction', 'Congress',
        'Fellowship', 'Foundation', 'Fraternity', 'Sorority', 'Institute', 'Traders' 
    ]
    humanoids = [
        'Druid', 'Cleric', 'Barbarian', 'Paladin', 'Sorcerer', 'Wizard', 'Warrior', 'Rogue',
        'Guardian', 'Hunter', 'Acrobat', 'Minstrel', 'Hobgoblin', 'Triton', 'Mermaid', 'Merman',
        'Witch', 'Wench', 'Warlock',
        'Elf', 'Dwarf', 'Halfling', 'Orc', 'Goblin', 'Bugbear', 'Giant', 'Troll',
        'Ghoul', 'Zombie', 'Devil', 'Demon', 'Vampire', 'Skeleton', 
        'Minstrel','Strumpet','Wench','Matron','Innkeeper','Brute','Page','Drunk'
    ]
    instruments = [
        'Flutes', 'Song', 'Players', 'Zithers', 'Drums', 'Lutes', 'Thespiates', 'Actors',
        'Trumpets', 'Horns', 'Strings', 'Harpers', 'Bells', 'Cabasa', 'Claves', 'Cymbals',
        'Gongs', 'Pipes', 'Quartet', 'Conch',
    ]
    locations = [ 
        'Liria', 'Mighalia', 'Tragekia', 'Yithia', 'Zhi', 'Bedia', 'Mighal', 'Brinwal',
        'Stagraven', 'Nacoal', 'Flakew', 
    ]
    militants = [ 
        'Dragoons', 'Knights', 'Myrmidons', 'Gladiators', 'Cavalry', 'Reavers', 'Scoundrels',
        'Devils', 'Demons', 'Knights', 'Cavaliers', 'Warriors', 'Raptors', 'Guards', 
        'Highlanders', 'Marines', 'Infantry', 'Scouts', 'Blades', 'Squad', 'Platoon',
        'Company', 'Battalion', 'Army', 'Legion', 'Ranks',
    ]
    nouns = [
        'Cups','Plates','Flagon','Chalice','Spoon','Knife','Spice','Trough',
        'Flask','Pint','Shot','Jug',

        'Staff','Wand','Rod','Hat',

        'Hat', 'Boot', 'Cloak', 'Robe',
    ]
    numeric = [
        'Lone', 'Twin', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Dozen', 'Thirteen',
    ]
    royalty = [
        'Emperor', 'Empress', 'King', 'Queen', 'Prince', 'Princess', 'Knight',
        'Duke', 'Duchess', 'Baron', 'Baroness', 'Lord', 'Lady', 'Master', 'Mistress',
    ]
    taverns = [ 
        'Bar', 'Brew House', 'Beer House', 'Mead House', 'Ale House', 'Speakeasy', 'Pub', 
        'Lounge', 'Brewery', 'Loft', 'Club', 'Inn', 'Tavern', 'Den', 'Lodge' ]
    weapons = [ 
        'Axe', 'Knife', 'Sword', 'Blade', 'Lance', 'Hatchet', 'Shield', 'Dagger', 'Rapier',
        'Saber', 'Scythe', 'Spit']

    schemes = {
        'tavern' : [ 
            'Animal & Animal',
            'Noun & Animal',
            'Animal & Noun',
            'Noun & Noun',
            'Humanoid & Animal',
            'Animal & Humanoid',
            'Noun & Humanoid',
            'Humanoid & Noun',
            'Adjective Animal',
            'Adjective Noun',
            'Adjective Humanoid',
            'Adjective _Tavern',
            'Royalty _Tavern',
            'Adjective Royalty',
            'Royalty Humanoid'
        ],
        'bardiccollege': [
            'Adjective Instrument', 
            'Descriptor Instrument', 
            'The Instrument & Instrument Merchant',
            'The Location Instrument', 
            'Merchant of the Descriptor Instrument',
            'Merchant of the Instrument', 
            'Merchant of the Adjective Instrument',
            'Instrument College', 
            'Adjective Instrument College', 
            'Descriptor Instrument College',
            'College of the Instrument', 
            'College of the Adjective Instrument',
            'College of the Descriptor Instrument'
        ],
        'duelingcollege': [
            'Adjective Weapon College', 
            'Descriptor Weapon College',
            'College of the Adjective Weapon', 
            'College of the Descriptor Weapon',
            'College of the Weapon', 
            'College of the Adjective Descriptor Weapon'
        ],
        'house': ['HOUSE'],
        'mageschool' : [
            'Adjective Building', 
            'Arcane Building', 
            'Arcane Militant', 
        ],
        'mercenarycompany': [
            'Adjective Weapon Company',
            'Location Militant', 
            'Location Weapon',
            'Adjective Weapon Company',
            'Weapon Militant', 
            'Adjective Militant', 
            'Adjective Weapon Company',
        ],
        'merchantguild' : [
            'Geographical Merchant', 
            'Merchant of Location', 
            'Adjective Geographical Merchant', 
            'Adjective Merchant of Location', 
            'Descriptor Geographical Merchant', 
            'Descriptor Merchant of Location', 
            'The Descriptor Geographical Merchant',
        ],
        'monasticorder' : [
            'Order of the Arcane Abstract', 
            'Order of the Adjective Noun', 
            'Order of the Arcane Weapon',
            'Order of the Adjective Weapon', 
            'Order of the Adjective Abstract',
            'Order of the Abstract Weapon',
        ],
        'roguesguild': [
            'Merchant of the Noun', 'Descriptor Noun', 'Merchant of the Descriptor Noun',
            'Merchant of the Adjective Noun', 'Descriptor Adjective Noun'
        ]
    }

    return replace(oneof(schemes[which]))

def main():
    namechoices = [
         'tavern', 'bardiccollege', 'duelingcollege', 'house', 'mageschool',
         'merchantguild', 'mercenarycompany', 'monasticorder', 'roguesguild'
    ]
    parser = argparse.ArgumentParser(
                    prog='NameGen',
                    description='A tool for generating random organization/business names',
                    epilog='Written in Python with love')
    parser.add_argument('--version', action='version', version='%(prog)s 0.1')
    parser.add_argument('--name', choices=namechoices, help="What kind of name to generate")
    parser.add_argument('--num', help='How many to generate')
    args = parser.parse_args()

    iterations = 1
    if args.num != None:
        iterations = int(args.num)
    which = args.name
    for _ in range(iterations):
        print(namegen(which))

if __name__ == '__main__':
	main()
