## Dwarven Resilience
*Prerequisite: Dwarf*

You have the blood of dwarf heroes flowing through your veins. You gain the following benefits:

Increase your Constitution score by 1, to a maximum of 20.

Whenever you take the Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1).

```
name = 'Dwarven Resilience'
description = "***Feat: Dwarven Resilience.*** You have the blood of dwarf heroes flowing through your veins."
def prereq(npc): return True if npc.race.name == 'Dwarf' else False
def apply(npc):
    npc.CON += 1

    npc.actions.append("***Resilient Dodge.*** When you take this Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1).")
```

