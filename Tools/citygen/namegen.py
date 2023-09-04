#!/usr/bin/env python3
import random

def namegen(which):
    def replace(phrase):
        mappings = {
            'Adjective' : adjectives,
            'Descriptor' : descriptors,
            'Building' : buildings,
            'Noun' : nouns,
            'Geographical' : geographical,
            'Location' : locations,
            'Merchant' : merchants,
            'Militant' : militants,
            '_Tavern' : taverns
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

    adjectives = [ 'Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Purple', 'Sanguine', 'Sepia', 'Ochre',
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
                   'Vorpal', 'Savage' ]
    descriptors = [ 
        'Infinite', 'Miasmal', 'Nonesuch', 'Chthonic', 'Celestial', 'Spiral', 'Silver', 'Gold',
        'Crimson', 'Silent', 'Bronze', 'Colossal', 'Elemental', 'Gilded', 'Shimmering', 'Eldritch',
        'Immaculate', 'Fey', 'Astral', 'Chaos', 'Enduring', 'Everlasting', 'Mercury', 'Night', 
        'Midnight', 'Raven', 'Grey', 'Fire', 'Dusk', 'Nightshade', 'Reviled', 'Umbral', 'Stained', 
        'Cursed', 'Long', 'Tranquil', 'Blue', 'Green', 'Gold', 'Verdant', 'Radiant', 'Silent',
        'Focused', 'Elemental', 'Harmonic'
    ]
    buildings = [ 'Cylinder', 'Minaret', 'Monument', 'Pylon', 'Tower', 'Spire', 'Turret', 'Column', 
                  'Obelisk', 'Rock', 'Eye', 'Tome', 'Citadel', 'Fortress', 'Arch' ]
    nouns = [ 'Dog', 'Wolf', 'Fox', 'Pul', 'Cat', 'Lion', 'Tiger', 'Kitten', 'Ox', 'Cow',
              'Sow', 'Bull', 'Calf', 'Horse', 'Stallion', 'Mare', 'Foal', 'Owl', 'Eagle',
              'Falcon', 'Hawk', 'Raven', 'Crow', 'Gull', 'Fish', 'Whale', 'Shark', 'Octopus',
              'Squid', 'Goat', 'Sheep', 'Ewe', 'Fly', 'Butterfly', 'Dragonfly', 'Beetle', 'Ant',
              'Wasp', 'Termite', 'Louse', 'Worm', 'Lizard', 'Frog', 'Toad', 'Snake', 'Chameleon',
              'Unicorn', 'Gryphon', 'Dragon', 'Wyvern', 'Roc', 'Clam', 'Oyster', 'Starfish', 'Slug',
              'Snail', 'Mouse', 'Rat', 'Beaver', 'Marten', 'Mink', 'Otter', 'Seal', 'Manatee',
              'Chipmunk', 'Squirrel', 'Gopher', 'Tower', 'Castle', 'Dagger', 'Sword', 'Bow',
              'Arrow', 'Hat', 'Boot', 'Trophy', 'Goose', 'Duck', 'Boat', 'Ship', 'River', 'Falls', 
              'Forest', 'Mountain', 'Vampire', 'Skeleton', 'Witch', 'Wench', 'Lady', 'Lord', 
              'Blades', 'Knives', 'Star', 'Consortium', 'Syndicate', 'Cabal', 'Court',
              'Swallow', 'Drake', 'Light', 'Soul', 'Mind', 'Body', 'Sun', 'Moon', 'Winds', 
              'Shadows', 'Harmony', 'Monkey', 'Viper', 'Crane', 'Mantis', 'Bear', 'Element',
              'Daggers', 'Gang', 'Boys', 'Hand', 'Coil', 'Alliance', 'Maggots', 'Rats',
              'Knight', 'Page', 'Drunk', 'Shield', 'Wand', 'Helm', 'Flask', 'Flagon', 'Pint', 'Shot' ]
    geographical = [ 'Lirian', 'Whaveminsian', 'Tragekian', 'Yithian', "Zhian", 'Ravenian', 'Mighalian' ]
    locations = [ 'Liria', 'Mighalia', 'Tragekia', 'Yithia', 'Zhi', 'Bedia', 'Mighal', 'Brinwal',
                  'Stagraven', 'Nacoal', 'Flakew', '' ]
    merchants = [ 'Compact', 'Company', 'Pact', 'Guild', 'Contract', 'Order', 'Alliance',
                  'Federation', 'College', 'League', 'Group', 'Lodge', 'Order', 'Society', 'Trade', 
                  'Union', 'Association', 'Club', 'Brotherhood', 'Confederation', 'Faction', 'Congress',
                  'Fellowship', 'Foundation', 'Fraternity', 'Sorority', 'Institute', 'Traders' ]
    militants = [ 'Dragoons', 'Knights', 'Myrmidons', 'Gladiators', 'Cavalry', 'Reavers', 'Scoundrels',
                  'Devils', 'Demons', 'Knights', 'Cavaliers', 'Warriors', 'Raptors' ]
    taverns = [ 'Bar', 'Brew House', 'Beer House', 'Mead House', 'Ale House', 'Speakeasy', 'Pub', 
                'Lounge', 'Brewery', 'Loft', 'Club', 'Inn', 'Tavern', 'Den', 'Lodge' ]
    weapons = [ 'Axe', 'Knife', 'Sword', 'Blade', 'Lance', 'Hatchet', 'Shield', 'Dagger', 'Rapier',
                'Saber', ]

    if which == 'tavern':
        schemes = [ 'Adjective Noun', 'Adjective Noun _Tavern', 'The Adjective Noun', 
                    'The Adjective Noun _Tavern', 'Noun & Noun', 'Noun & Noun _Tavern',
                    'The Noun & Noun', 'The Noun & Noun _Tavern', 'Adjective _Tavern',
                    'The Adjective _Tavern' ]
        return replace(schemes[random.randint(0, len(schemes)-1)])
    elif which == 'roguesguild':
        schemes = [
            'Merchant of the Noun', 'Descriptor Noun', 'Merchant of the Descriptor Noun',
            'Merchant of the Adjective Noun', 'Descriptor Adjective Noun'
        ]
        return replace(schemes[random.randint(0, len(schemes)-1)])
    elif which == 'mageschool':
        schemes = [
            'Descriptor Building', 'Adjective Building', 'The Descriptor Building', 'The Adjective Building'
        ]
        return replace(schemes[0])
    elif which == 'merchantguild':
        schemes = [
            'Geographical Merchant', 'Merchant of Location', 'The Geographical Merchant'
        ]
        return replace(schemes[random.randint(0, len(schemes)-1)])
    elif which == 'monasticorder':
        schemes = [
            'Order of the Descriptor Noun', 'Order of the Adjective Noun'
        ]
        return replace(schemes[random.randint(0, len(schemes)-1)])
    else:
        return "UNRECOGNIZED NAME: '" + which + "'"


print("Tavern: " + namegen('tavern'))
print("Rogues Guild: " + namegen('roguesguild'))
print("Mage School: " + namegen('mageschool'))
print("Merchant Guild: " + namegen('merchantguild'))
print("Monastic Order: " + namegen('monasticorder'))
