## Skilled
You gain proficiency in any combination of three skills or tools of your choice.

```
name = 'Skilled'
description = "***Feat: Skilled.** You are skilled in a variety of skills and tools."
def prereq(npc): return True
def apply(npc):
    chooseskill(npc)
    chooseskill(npc)
    chooseskill(npc)
```
