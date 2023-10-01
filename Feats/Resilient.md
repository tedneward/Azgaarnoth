## Resilient
Choose one ability score. You gain the following benefits:

* Increase the chosen ability score by 1, to a maximum of 20.
* You gain proficiency in saving throws using the chosen ability.

```
name = 'Resilient'
description = "***Feat: Resilient.***"
def prereq(npc): return True
def apply(npc):
    ability = chooseability(npc)
    npc.savingthrows.append(ability)
```
