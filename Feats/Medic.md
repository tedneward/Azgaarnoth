## Medic
You master the physician's arts, gaining the following benefits:

* Increase your Wisdom score by 1, to a maximum of 20.
* You gain proficiency in the Medicine skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* During a short rest, you can clean and bind the wounds of up to six willing beasts and humanoids. Make a DC 15 Wisdom (Medicine) check for each creature. On a success, if a creature spends a Hit Die during this rest, that creature can forgo the roll and instead regain the maximum number of hit points the die can restore. A creature can do so only once per rest, regardless of how many Hit Dice it spends.

```
name = 'Medic'
description = "***Feat: Medic.*** You master the physician's arts."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    npc.addskillorexpertise('Medicine')

    npc.traits.append("***Medical Treatment.*** During a short rest, you can clean and bind the wounds of up to six willing beasts and humanoids. Make a Wisdom (Medicine) check (DC 15) for each creature. On a success, if a creature spends a Hit Die during this rest, that creature can forgo the roll and instead regain the maximum number of hit points the die can restore. A creature can do so only once per rest, regardless of how many Hit Dice it spends.")
```
