## Determination
*Prerequisite: human*

You are filled with a determination that can draw the unreachable within your reach. You gain the following benefits: 

* Increase one ability score of your choice by 1, to a maximum of 20.
* When you make an attack roll, an ability check, or a saving throw, you can do so with advantage. Once you use this ability, you can't use it again until you finish a short or long rest.

```
name = 'Determination'
description = "***Feat: Determination.*** You are filled with a determination that can draw the unreachable within your reach."
def prereq(npc): return True if npc.race.name == 'Human' else False
def apply(npc):
    chooseability(npc)

    npc.traits.append("***Determination (Recharges on short or long rest).*** When you make an attack roll, an ability check, or a saving throw, you can do so with advantage.")
```
