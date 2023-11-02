## Infernal Constitution
*Prerequisite: Tiefling*

Fiendish blood runs strong in you, unlocking a resilience akin to that possessed by some fiends. You gain the following benefits:

* Increase your Constitution score by 1, up to a maximum of 20.
* You have resistance to cold damage and poison damage.
* You have advantage on saving throws against being poisoned.

```
name = 'Infernal Constitution'
description = "***Feat: Infernal Constitution.*** Fiendish blood runs strong in you, unlocking a resilience akin to that possessed by some fiends."
def prereq(npc): return npc.race.name == 'Tiefling'
def apply(npc):
    npc.CON += 1

    npc.damageresistances.append('cold')
    npc.damageresistances.append('poison')

    npc.traits.append("***Infernal Constitution.*** You have advantage on saving throws against being poisoned.")
```
