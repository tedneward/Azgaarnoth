## Durable
Hardy and resilient, you gain the following benefits:

* Increase your Constitution score by 1, to a maximum of 20.
* When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals twice your Constitution modifier (minimum of 2).

```
name = 'Durable'
description = "***Feat: Durable.*** You are hardy and resilient."
def prereq(npc): return True
def apply(npc):
    npc.CON += 1
    npc.traits.append("***Durable.*** When you roll a Hit Die to regain hit points, the minimum number of hit points you regain from the roll equals twice your Constitution modifier (minimum of 2).")
```
