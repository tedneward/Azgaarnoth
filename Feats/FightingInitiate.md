## Fighting Initiate
*Prerequisite: Proficiency with a martial weapon*

Your martial training has helped you develop a particular style of fighting. As a result, you learn one [Fighting Style](../Classes/Fighter/Styles.md) option of your choice from the fighter class. If you already have a style, the one you choose must be different.

Whenever you gain a level, you can replace this feat's fighting style with another one from the fighter class that you don't have.

```
name = 'Fighting Initiate'
description = "***Feat: Fighting Initiate.*** Your martial training has helped you develop a particular style of fighting."
def prereq(npc):
    return True
def apply(npc):
    npc.style = allclasses['Fighter'].choosestyle(npc)
```
