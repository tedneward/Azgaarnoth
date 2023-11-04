# River Halflings
Traveling by raft, barge, or even large aquatic beast, the halflings of the bays, rivers, and lakes are by far the most nomadic families of halflings. These halflings are known for their swimming ability, and for their skill upon any manner of aquatic vessei performing rigging, navigating, or fishing tasks with ease. The riverfolk are guides, traders, and hunters that move up and down their ancestral waterways, enjoying a slow-flowing life. Many are known for their sharp distrust of outsiders and lack of wanderlust, features that are truly exceptional among most halflings, and they live as an insular community. Some are more oceanic, carrying out long voyages from island to island and continent to continent on communal boats across a vast and seemingly endless ocean.

As a river halfling, you were born on the waters, and you grew up surrounded by the working knowledge of the boat and river you lived on. You've also practiced both swimming and holding your breath so long that they've become second nature to you.

***Ability Score Increase.*** Your Constitution score increases by 1.

***Fisher's Weapon Training.*** You have proficiency with the lance, net, spear, and trident.

***River Traveler.*** You have proficiency with water vehicles, and you have advantage on ability checks made to forage or navigate near a natural body of water.

***Waterborne.*** You have a swimming speed of 30 feet and you can hold your breath for twice as long as normal

```
name = 'River'
description = "***Subrace: River Halfling.*** As a river halfling, you were born on the waters, and you grew up surrounded by the working knowledge of the boat and river you lived on. You've also practiced both swimming and holding your breath so long that they've become second nature to you."

def level0(npc):
    npc.CON += 1
    
    npc.proficiencies.append("Lance")
    npc.proficiencies.append("Net")
    npc.proficiencies.append("Spear")
    npc.proficiencies.append("Trident")

    npc.proficiencies.append("Water vehicles")
    npc.traits.append("***River Traveler.*** You have advantage on ability checks made to forage or navigate near a natural body of water.")

    npc.speeds['swimming'] = 30
    npc.traits.append("***Waterborne.*** You can hold your breath for twice as long as normal.")
```
