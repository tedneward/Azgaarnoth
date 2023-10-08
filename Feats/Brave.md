## Brave
You are used to staring down dangerous monsters and running straight into deadly situations. You gain the following benefits:

* Your Wisdom score increases by 1, to a maximum of 20.
* You have advantage on saving throws to resist becoming frightened.
* All of your allies within 30 feet of you are rallied by your bravery. They also have advantage on saving throws to resist becoming frightened, as long as you are conscious.

```
name = 'Brave'
description = "***Feat: Brave.*** You are used to staring down dangerous monsters and running straight into deadly situations."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    npc.traits.append("***Brave.*** You have advantage of saving throws to resist becoming frightened. All of your allies within 30 feet of you are rallied by your bravery. They also have advantage on saving throws to resist becoming frightened, as long as you are conscious.")
```
