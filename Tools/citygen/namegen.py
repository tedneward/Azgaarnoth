#!/usr/bin/env python3

import os
import random

def namegen(which):
    def oneof(options):
        return options[random.randint(0, len(options)-1)]
    def replace(phrase):
        mappings = {
            'Adjective' : adjectives,
            'Building' : buildings,
            'College': colleges,
            'Descriptor' : descriptors,
            'Geographical' : geographical,
            'Instrument': instruments,
            'Noun' : nouns,
            'Location' : locations,
            'Merchant' : merchants,
            'Militant' : militants,
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
    descriptors = [ 
        'Infinite', 'Miasmal', 'Nonesuch', 'Chthonic', 'Celestial', 'Spiral', 'Silver', 'Gold',
        'Crimson', 'Silent', 'Bronze', 'Colossal', 'Elemental', 'Gilded', 'Shimmering', 'Eldritch',
        'Immaculate', 'Fey', 'Astral', 'Chaos', 'Enduring', 'Everlasting', 'Mercury', 'Night', 
        'Midnight', 'Raven', 'Grey', 'Fire', 'Dusk', 'Nightshade', 'Reviled', 'Umbral', 'Stained', 
        'Cursed', 'Long', 'Tranquil', 'Blue', 'Green', 'Gold', 'Verdant', 'Radiant', 'Silent',
        'Focused', 'Elemental', 'Harmonic'
    ]
    buildings = [ 
        'Cylinder', 'Minaret', 'Monument', 'Pylon', 'Tower', 'Spire', 'Turret', 'Column', 
        'Obelisk', 'Rock', 'Eye', 'Tome', 'Citadel', 'Fortress', 'Arch' ]
    nouns = [ 
        'Rooster', 'Hound', 'Elk',  'Cat', 'Guardian', 'Hunter', 'Troll', 'Sword', 'Shield',
        'Bow', 'Hammer', 'Helm', 'Acrobat', 'Ghoul', 'Zombie', 'King', 'Pegasus', 'Mastiff', 
        'Druid', 'Master', 'Mistress', 'Prince', 'Princess', 'Duke', 'Duchess', 'Baron', 'Baroness',
        'Flounder', 'Whale', 'Elf', 'Dwarf', 'Halfling', 'Orc', 'Goblin', 'Bugbear', 'Giant',
        'Dog', 'Wolf', 'Fox', 'Puma', 'Cat', 'Lion', 'Tiger', 'Kitten', 'Ox', 'Cow',
        'Sow', 'Bull', 'Calf', 'Horse', 'Stallion', 'Mare', 'Foal', 'Owl', 'Eagle',
        'Falcon', 'Hawk', 'Raven', 'Crow', 'Gull', 'Fish', 'Whale', 'Shark', 'Octopus',
        'Squid', 'Goat', 'Sheep', 'Ewe', 'Fly', 'Butterfly', 'Dragonfly', 'Beetle', 'Ant',
        'Wasp', 'Termite', 'Louse', 'Worm', 'Lizard', 'Frog', 'Toad', 'Snake', 'Chameleon',
        'Unicorn', 'Gryphon', 'Dragon', 'Wyvern', 'Roc', 'Clam', 'Oyster', 'Starfish', 'Slug',
        'Snail', 'Mouse', 'Rat', 'Beaver', 'Marten', 'Mink', 'Otter', 'Seal', 'Manatee',
        'Minstrel', 'Brute', 'Strumpet', 'Helmet', 'Devil', 'Demon', 'Throne',
        'Chipmunk', 'Squirrel', 'Gopher', 'Tower', 'Castle', 'Dagger', 'Sword', 'Bow',
        'Arrow', 'Hat', 'Boot', 'Trophy', 'Goose', 'Duck', 'Boat', 'Ship', 'River', 'Falls', 
        'Forest', 'Mountain', 'Vampire', 'Skeleton', 'Witch', 'Wench', 'Lady', 'Lord', 
        'Blades', 'Knives', 'Star', 'Consortium', 'Syndicate', 'Cabal', 'Court',
        'Swallow', 'Drake', 'Light', 'Soul', 'Mind', 'Body', 'Sun', 'Moon', 'Winds', 
        'Shadows', 'Harmony', 'Monkey', 'Viper', 'Crane', 'Mantis', 'Bear', 'Element',
        'Daggers', 'Gang', 'Boys', 'Hand', 'Coil', 'Alliance', 'Maggots', 'Rats',
        'Knight', 'Page', 'Drunk', 'Shield', 'Wand', 'Helm', 'Flask', 'Flagon', 'Pint', 'Shot' ]
    geographical = [ 
        'Lirian', 'Whaveminsian', 'Tragekian', 'Yithian', "Zhian", 'Ravenian', 'Mighalian',
        'Bedian', 'Tragekian', 
        '' ]
    locations = [ 
        'Liria', 'Mighalia', 'Tragekia', 'Yithia', 'Zhi', 'Bedia', 'Mighal', 'Brinwal',
        'Stagraven', 'Nacoal', 'Flakew', 
        '' ]
    merchants = [ 
        'Compact', 'Company', 'Pact', 'Guild', 'Contract', 'Order', 'Alliance',
        'Federation', 'College', 'League', 'Group', 'Lodge', 'Order', 'Society', 'Trade', 
        'Union', 'Association', 'Club', 'Brotherhood', 'Confederation', 'Faction', 'Congress',
        'Fellowship', 'Foundation', 'Fraternity', 'Sorority', 'Institute', 'Traders' ]
    militants = [ 
        'Dragoons', 'Knights', 'Myrmidons', 'Gladiators', 'Cavalry', 'Reavers', 'Scoundrels',
        'Devils', 'Demons', 'Knights', 'Cavaliers', 'Warriors', 'Raptors', 'Guards', 'Highlanders',
        'Marines', 'Infantry', 'Scouts', ''
    ]
    colleges = [
        'College', 'University', 'School', 'Hall', 'Conservatory', 'Academy', 'Society', 'Institute',
        'Fraternity', 'Sorority', 'Lyceum', 'Study', 'Fellowship', 'Band', 'Body', 'Lodge'
    ]
    taverns = [ 
        'Bar', 'Brew House', 'Beer House', 'Mead House', 'Ale House', 'Speakeasy', 'Pub', 
        'Lounge', 'Brewery', 'Loft', 'Club', 'Inn', 'Tavern', 'Den', 'Lodge' ]
    weapons = [ 
        'Axe', 'Knife', 'Sword', 'Blade', 'Lance', 'Hatchet', 'Shield', 'Dagger', 'Rapier',
        'Saber', 'Scythe', 'Spit']
    instruments = [
        'Flute', 'Song', 'Players', 'Zither', 'Drum', 'Lute', 'Thespiates', 'Actors',
        'Trumpet', 'Horn', 'Strings', 'Harpers', 'Bells', 'Cabasa', 'Claves', 'Cymbals',
        'Gongs', 'Pipes', 'Quartet', 'Conch', ''
    ]

    schemes = {
        'tavern' : [ 
            'Adjective Noun', 'Adjective Noun _Tavern', 'The Adjective Noun', 
            'The Adjective Noun _Tavern', 'Noun & Noun', 'Noun & Noun _Tavern',
            'The Noun & Noun', 'The Noun & Noun _Tavern', 'Adjective _Tavern',
            'The Adjective _Tavern' ],
        'bardiccollege': [
            'Adjective Instrument', 'Descriptor Instrument', 'The Instrument & Instrument Merchant',
            'The Location Instrument', 'Merchant of the Descriptor Instrument',
            'Merchant of the Instrument', 'Merchant of the Adjective Instrument',
            'Instrument College', 'Adjective Instrument College', 'Descriptor Instrument College',
            'College of the Instrument', 'College of the Adjective Instrument',
            'College of the Descriptor Instrument'
        ],
        'duelingcollege': [
            'Adjective Weapon College', 'Descriptor Weapon College',
            'College of the Adjective Weapon', 'College of the Descriptor Weapon',
            'College of the Weapon', 'College of the Adjective Descriptor Weapon'
        ],
        'mageschool' : [
            'Descriptor Building', 'Adjective Building', 'The Descriptor Building', 'The Adjective Building'
        ],
        'mercenarycompany': [
            'Location Militant', 'Weapon Militant', 'Location Weapon',
            'Adjective Militant', 'Adjective Weapon'
        ],
        'merchantguild' : [
            'Geographical Merchant', 'Merchant of Location', 'The Geographical Merchant',
            'Adjective Geographical Merchant', 'Adjective Merchant of Location', 'The Adjective Geographical Merchant',
            'Descriptor Geographical Merchant', 'Descriptor Merchant of Location', 'The Descriptor Geographical Merchant',
        ],
        'monasticorder' : [
            'Order of the Descriptor Noun', 'Order of the Adjective Noun', 'Order of the Descriptor Weapon',
            'Order of the Adjective Weapon', 'Order of the Adjective Descriptor Weapon', 
        ],
        'roguesguild': [
            'Merchant of the Noun', 'Descriptor Noun', 'Merchant of the Descriptor Noun',
            'Merchant of the Adjective Noun', 'Descriptor Adjective Noun'
        ]
    }

    return replace(oneof(schemes[which]))
