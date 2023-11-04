# [Tabaxi](../Creatures/Tabaxi.md)
Tabaxi are catlike humanoids driven by curiosity to wander, often to collect interesting artifacts, gather tales and stories, and lay eyes on all the world's wonders. Ultimate travelers, the inquisitive tabaxi rarely stay in one place for long. Their innate nature pushes them to leave no secrets uncovered, no treasures or legends lost.

***Tabaxi Traits.*** Your tabaxi character has the following racial traits.

* **Ability Score Increase.** Your Dexterity score increases by 2, and your Charisma score increases by 1.

* **Age.** Tabaxi have lifespans equivalent to humans.

* **Size.** Tabaxi are taller on average than humans and relatively slender. Your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Darkvision.** You have a cat’s keen senses, especially in the dark. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

* **Feline Agility.** Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can’t use it again until you move 0 feet on one of your turns.

* **Cat’s Claws.** Because of your claws, you have a climbing speed of 20 feet. In addition, your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

* **Cat’s Talent.** You have proficiency in the Perception and Stealth skills.

* **Languages.** You can speak, read, and write Common and one other language of your choice.

```
name = 'Tabaxi'
description = "***Race: Tabaxi.*** Tabaxi are catlike humanoids driven by curiosity to wander, often to collect interesting artifacts, gather tales and stories, and lay eyes on all the world's wonders. Ultimate travelers, the inquisitive tabaxi rarely stay in one place for long. Their innate nature pushes them to leave no secrets uncovered, no treasures or legends lost."
type = 'humanoid'
def level0(npc):
    npc.DEX += 2
    npc.CHA += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.speed['climbing'] = 20

    npc.senses['darkvision'] = 60

    npc.actions.append("***Feline Agility.*** When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can’t use it again until you move 0 feet on one of your turns.")

    npc.defer(lambda npc: npc.actions.append(f"***Claws.*** *Melee Weapon Attack:* +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5ft., one target. Hit: 1d4 + {npc.STRbonus()} slashing damage"))

    npc.skills.append('Perception')
    npc.skills.append('Stealth')

    npc.languages.append('Common')
    npc.languages.append('CHOOSE')
```

## Tabaxi Personality
A tabaxi might have motivations and quirks much different from a dwarf or an elf with a similar background. You can use the following tables to customize your character in addition to the trait, ideal, bond, and flaw from your background.

The Tabaxi Obsession table can help hone your character’s goals. For extra fun, roll a new result every few days that pass in the campaign to reflect your ever-changing curiosity.

**Tabaxi Obsessions**

d8 | My curiosity is currently fixed on ...
-- | --------------------------------------
1 | A god or planar entity
2 | A monster
3 | A lost civilization
4 | A wizard’s secrets
5 | A mundane item
6 | A magic item
7 | A location
8 | A legend or tale

**Tabaxi Quirks**

d10	| Quirk
--- | ----
1 | You miss your tropical home and complain endlessly about the freezing weather, even in summer.
2 | You never wear the same outfit twice, unless you absolutely must.
3 | You have a minor phobia of water and hate getting wet.
4 | Your tail always betrays your inner thoughts.
5 | You purr loudly when you are happy.
6 | You keep a small ball of yarn in your hand, which you constantly fidget with.
7 | You are always in debt, since you spend your gold on lavish parties and gifts for friends.
8 | When talking about something you’re obsessed with, you speak quickly and never pause and others can’t understand you.
9 | You are a font of random trivia from the lore and stories you have discovered.
10 | You can’t help but pocket interesting objects you come across.

```
    obsessions = [
        "A god or planar entity",
        "A monster",
        "A lost civilization",
        "A wizard’s secrets",
        "A mundane item",
        "A magic item",
        "A location",
        "A legend or tale"
    ]
    npc.description.append(f"***Tabaxi Personality: Obsession.*** {obsessions[dieroll('d8') - 1]}")
    quirks = [
        "You miss your tropical home and complain endlessly about the freezing weather, even in summer.",
        "You never wear the same outfit twice, unless you absolutely must.",
        "You have a minor phobia of water and hate getting wet.",
        "Your tail always betrays your inner thoughts.",
        "You purr loudly when you are happy.",
        "You keep a small ball of yarn in your hand, which you constantly fidget with.",
        "You are always in debt, since you spend your gold on lavish parties and gifts for friends.",
        "When talking about something you’re obsessed with, you speak quickly and never pause and others can’t understand you.",
        "You are a font of random trivia from the lore and stories you have discovered.",
        "You can’t help but pocket interesting objects you come across."
    ]
    npc.description.append(f"***Tabaxi Personality: Quirk.*** {quirks[dieroll('d10') - 1]}")
```


## Sample Tabaxi names (from https://www.roll4.net/generators/dd-name-generators/dd-tabaxi-name-generator)
Rune of the Leeches of the Defeated Cave Clan
Shy Hare of The Washing Islet Clan
Amethyst Logic of The Encroaching Inlet Clan
Diamond Face of the Gilded Jungle Clan
Talented Sulfer of the Inquisitive Hill Clan
Mindrot of Night of The Flaying River Clan
Submission of the Manatee of The Engaging Lagoon Clan
Cold of Bubble of the Grumpy Coast Clan
Sound of the of The Inspiring Swamp Clan
Jealousy of the Swarms of The Diminishing River Clan
Selfish Darts of the Vast Summit Clan
Courage of Thunder of The Blood-Drinking Mesa Clan
Doubtful Lightning of the Radiant Inlet Clan
Sleep of the Blades of the Thankful Gully Clan
Cobalt Manticore of The Rummaging Jungle Clan
Engulfment of the Goose of the Muddy Swamp Clan
Powerful Fall of The Clutching River Clan
Ability of Thunder of The Mismanaging Plain Clan
Goblin Hamster of the Repulsive Oasis Clan
Creation of Cone of the Evil Marsh Clan
Silliness of Morning of the Forward Lagoon Clan
Hooked Trout of the Grieving Hill Clan
Brilliance of the Metals of the Elegant Valley Clan
Famous Smelt of The Scouring Ocean Clan
Diamond Robin of The Ribbing Forest Clan
Creepy Joy of The Approaching Cave Clan
Cobalt Luxury of The Rewarding Channel Clan
Dictatorship of the Pixie of The Sagging Valley Clan
Divine Hooves of The Tittering Glacier Clan
Hearsay of Water of the Discordant Jungle Clan
Filaments Geyser of The Breathtaking Channel Clan
Sound of the of the Cautious Canyon Clan
Lovely Pegasus of The Accomplishing Glacier Clan
Fate of Rake of the Forceful Peninsula Clan
Beautiful Maturity of the Troubled Lagoon Clan
Need of the Hooves of the Bone-Chilling Plain Clan
Sound of the of The Pronouncing Hill Clan
Shivers of Water of the Hilarious Coast Clan
Justice of Summer of The Shaking Peninsula Clan
Pronged Anteater of The Unlocking Oasis Clan
Freedom of the Elk of The Unleashing Marsh Clan
Innocent Deathcap of The Slashing Bay Clan
Unusual Winter of The Brainwashing Jungle Clan
Stupid Fire of the Sparkling Dune Clan
Ferocity of Lotus of The Flashing Hollows Clan
Dull Egg of The Scathing Hill Clan
Sound of the of the Fearful Wasteland Clan
Emerald Dreadblade of the Etheric Desert Clan
Graceful Coils of the Unusual Glacier Clan
Peridot Nightmares of the Grieving Ocean Clan
Aquamarine Gorgon of the Zany Plateau Clan
Absorbtion of Calvary of the Zealous Tundra Clan
Sound of the of the Muddy Jungle Clan
Glance of Beard of The Thrashing Tundra Clan
Ravenous Trees of The Assimilating Inlet Clan
Sound of the of The Cascading Hollows Clan
Distortion of Shade of The Tripping Bay Clan
Necro of Hand of the Fey Tundra Clan
Calm Spirits of The Climbing Jungle Clan
Fiery Loss of The Crashing Gully Clan
