## Crossbow Expert
Thanks to extensive practice with the crossbow, you gain the following benefits:

* You ignore the loading quality of crossbows with which you are proficient.
* Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.
* When you use the Attack action and attack with a one handed weapon, you can use a bonus action to attack with a hand crossbow you are holding.

```
name = 'Crossbow Expert'
description = "***Feat: Crossbow Expert.*** Thanks to extensive practice with the crossbow, you have some benefits when using one."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Crossbow Expert.*** You ignore the loading quality of crossbows with which you are proficient. Being within 5 feet of a hostile creature doesn't impose disadvantage on your ranged attack rolls.")
    npc.bonusactions.append(f"***Crossbow Expert.*** When you use the Attack action and attack with a one handed weapon, you can attack with a hand crossbow you are holding. *Ranged Weapon Attack:* +{npc.proficiencybonus() + npc.DEXbonus()} to hit, range 30/120, one target. Hit: 1d6 + {npc.DEXbonus()} piercing damage.")
```
