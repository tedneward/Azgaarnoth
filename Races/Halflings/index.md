# Halflings
There are no halfling "subraces", per se, but halflings will identify closely with the community they call "home", and have widespread communication with other halfling communities within relatively close range. For these reasons, halflings often find themselves engaged by, in, and then become part of, various [Merchant Guilds](../Organizations/MerchantGuilds/index.md). It also comes as no surprise to anyone that they're quite good at being merchants and guildmasters, particularly when it comes to negotiating.

It is rumored that many halflings are also high-ranking members of various Rogues' Guilds, including some of the most nefarious assassin organizations, but this has never been proven.

Halflings may be [dragonmarked](Dragonmarked.md) with the [Mark of Healing](Healing.md) or the [Mark of Hospitality](Hospitality.md); see those entries for details.

### [Lightfoot](Lightfoot.md) and [Stout](Stout.md) halflings
These halflings are pretty intermixed amongst each other by this point in Azgaarnoth's history, and no non-halfling can tell them apart. Culturally, there is little to no difference or differentiation between them, and many halfling families proudly claim to belong to one or the other (or sometimes both) without exhibiting any of the characteristics of either.

### [Jungle](Jungle.md) halflings
Halflings born and raised in the jungles of Azgaarnoth are a touch more "wild" than their more urban Lightfoot/Stout cousins, but no less halfling.

### [River](River.md) halflings
Many groups of halflings took to the seas and rivers of Azgaarnoth, and make a home upon the waters. Some call a major river (such as the Lenets River in Alalihat, or the Samny/Teyaslav Rivers in Zabalasa, or the Dustcross in Bagonbia) their home, using barges to travel up and down the waterways, others live in a communal ocean-going vessel, often as a cargo ship for hire by merchants or militaries.

### Ghostwise and Lotusden halflings
Some halflings have independently shown characteristics of these two subraces of halfling, but there appears to be no widespread shared genetic legacy--it seems to randomly appear in various halflings throughout Azgaarnoth. Ghostwise halflings frequently tend to end up associating with some of the psionic-leaning [Mage Schools](../Organizations/MageSchools/index.md) and Lotusden halflings often wander the wildnerness alongside druids and rangers.

```
name = 'Halfling'
description = "***Race: Halfling.*** Halflings are the archetypal small race, and have made beloved thieves and trackers and hosts for millennia."

def level0(npc):
    npc.DEX += 2

    npc.size = 'Small'
    npc.speed['walking'] = 25
    npc.traits.append("***Lucky.*** When you roll a 1 on the d20 for an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll.")
    npc.traits.append("***Brave.*** You have advantage on saving throws against being frightened.")
    npc.traits.append("***Halfling Nimbleness.*** You can move through the space of any creature that is of a size larger than yours.")

    npc.languages.append("Common")
    npc.languages.append("Halfling")

def generate_name(npc, gender):
    male_names = [ "Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby" ]

    female_names = ["Andry", "Bree", "Callie", "Cora", "Euphemia", "Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela", "Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]

    family_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Lightleaf", "Lightgage", "Goodleaf", "Tealeaf", "Thorngage", "Tosscobble", "Tossleaf", "Underbough", "Underhill"]
```
