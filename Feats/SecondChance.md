## Second Chance
*Prerequisite: Halfling*

Fortune favors you when someone tries to strike you. You gain the following benefits:

* Increase your Dexterity, Constitution, or Charisma score by 1, to a maximum of 20.
* When a creature you can see hits you with an attack roll, you can use your reaction to force that creature to reroll. Once you use this ability, you can't use it again until you roll initiative at the start of combat or until you finish a short or long rest.

```
name = 'Second Chance'
description = "***Feat: Second Chance.*** Fortune favors you when someone tries to strike you."
def prereq(npc): return True if npc.race.name == 'Halfling' else False
def apply(npc):
    chooseability(npc, ['DEX', 'CON', 'CHA'])

    npc.reactions.append("***Second Chance (Recharges on initiative roll, short or long rest).*** When a creature you can see hits you with an attack roll, you can force that creature to reroll.")
```
