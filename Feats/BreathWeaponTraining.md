## Breath Weapon Training
*Prerequisite: Dragonborn, Half-Dragon*

You have had a draconic mentor teach you how to maximize the effectiveness of your breath weapon. Your breath weapon deals an extra d6 of damage.

```
name = 'Breath Weapon Training'
description = "***Feat: Breath Weapon Training.*** You have had a draconic mentor teach you how to maximize the effectiveness of your breath weapon."
def prereq(npc): return npc.race.name == 'Dragonborn' or npc.race.name == 'Half-Dragon'
def apply(npc):
    npc.actions.append("TODO: Add 1d6 to Breath Weapon.")
```
