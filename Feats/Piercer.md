## Piercer
You have achieved a penetrating precision in combat, granting you the following benefits:

* Increase your Strength or Dexterity by 1, to a maximum of 20.
* Once per turn, when you hit a creature with an attack that deals piercing damage, you can reroll one of the attack's damage dice, and you must use the new roll.
* When you score a critical hit that deals piercing damage to a creature, you can roll one additional damage die when determining the extra piercing damage the target takes.

```
name = 'Piercer'
description = "***Feat: Piercer.*** You have achieved a penetrating precision in combat."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR','DEX'])

    npc.traits.append("***Piercer.*** Once per turn, when you hit a creature with an attack that deals piercing damage, you can reroll one of the attack's damage dice, and you must use the new roll. When you score a critical hit that deals piercing damage to a creature, you can roll one additional damage die when determining the extra piercing damage the target takes.")
```

