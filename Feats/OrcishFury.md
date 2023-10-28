## Orcish Fury
*Prerequisite: Half-orc, Orc*

Your fury burns tirelessly. You gain the following benefits:

* Increase your Strength or Constitution score by 1, up to a maximum of 20.
* When you hit with an attack made with a simple or martial weapon, you can roll one of the weapon's damage dice an additional time and add it as extra damage of the weapon's damage type. Once you use this ability, you can't use it again until you finish a short or long rest.
* Immediately after you use your Relentless Endurance trait, you can use your reaction to make one weapon attack.

```
name = 'Orcish Fury'
description = "***Feat: Orcish Fury.*** Your fury burns tirelessly."
def prereq(npc): return npc.race.name == 'Half-Orc' or npc.race.name == 'Orc'
def apply(npc): 
    ability = choose("Choose ability: ", ['STR', 'CON'])
    if ability == 'STR': npc.STR += 1
    elif ability == 'CON': npc.CON += 1
    else: error("Should never happen")

    npc.actions.append("***Orcish Fury (Recharges on short or long rest).*** When you hit with an attack made with a simple or martial weapon, you can roll one of the weapon's damage dice an additional time and add it as extra damage of the weapon's damage type.")

    npc.reactions.append("***Orcish Fury.*** Immediately after you use your Relentless Endurance trait, you make one weapon attack.")
```
