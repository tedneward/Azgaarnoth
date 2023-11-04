# Jungle Halfling
The halflings of the deep forest and jungle are the most isolated of the halfling populations. Some seek to live a lifestyle that focuses on obtaining the most elusive and delicious foods of the forest, foraging and hunting in tight-knit groups. Some seek a lifestyle less isolated, and focus more on acting as jungle and forest guides for the other races, especially when other halflings happen to travel through. 

As a jungle halfling, you have keen senses, you have spent much of your life climbing the branches and trees of your homeland, and you've been trained in the ways of foraging and hunting with your tribal weaponry.

In Azgaarnoth, many of these jungle halflings are found in Zhi and the jungle/wetlands of Yithi and the northern stretches of the Al'Uma nations (Almalz, Zabalasa, and Alalihat).

***Ability Score Increase.*** Your Wisdom score increases by 1.

***Bracbiator.*** You have a climbing speed of 30 feet.

***Hunter's Weapon Training.*** You have proficiency with the blowgun, net, spear, and whip.

***Tropical Resilience.*** You're naturally adapted to hot climates.

```
name = 'Jungle'
description = "***Subrace: Jungle Halfling.*** You have keen senses, you have spent much of your life climbing the branches and trees of your homeland, and you've been trained in the ways of foraging and hunting with your tribal weaponry."

def level0(npc):
    npc.WIS += 1

    npc.speeds['climbing'] = 30

    npc.proficiencies.append("Blowgun")
    npc.proficiencies.append("Net")
    npc.proficiencies.append("Spear")
    npc.proficiencies.append("Whip")

    npc.traits.append("***Tropical Resilience.*** You're naturally adapted to hot climates.")
```
