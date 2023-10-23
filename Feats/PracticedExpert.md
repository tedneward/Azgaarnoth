## Practiced Expert
You have honed your proficiency with particular skills or tools, gaining the following benefits:

* Increase one ability score of your choice by 1, to a maximum of 20.
* You gain proficiency with one skill or tool of your choice.
* Choose one of your skill or tool proficiencies. Your proficiency bonus is doubled for any ability check you make that uses the chosen proficiency. 

```
name = 'Practiced Expert'
description = "***Feat: Practiced Expert.*** You have honed your proficiency with particular skills or tools."
def prereq(npc): return True
def apply(npc):
    chooseability(npc)

    npc.skillchoice()

    npc.addskillorexpertise(choose("Choose one: ", npc.skills + npc.proficiencies))
```
