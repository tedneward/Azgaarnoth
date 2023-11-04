## Resilient
You are harder to kill than most. You gain the following benefits:

* Choose one ability score. Increase the chosen ability score by 1, to a maximum of 20.
* You gain proficiency in saving throws using the chosen ability.

```
name = 'Resilient'
description = "***Feat: Resilient.*** You are harder to kill than most."
def prereq(npc): return True
def apply(npc):
    ability = chooseability(npc)
    npc.savingthrows.append(ability)
```
