## Savage Attacker
Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total.

```
name = 'Savage Attacker'
description = "***Feat: Savage Attacker.***"
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Savage Attacker.*** Once per turn when you roll damage for a melee weapon attack, you can reroll the weapon's damage dice and use either total.")
```
