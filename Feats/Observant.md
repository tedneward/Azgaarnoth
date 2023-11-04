## Observant
Quick to notice details of your environment, you gain the following benefits:

* Increase your Intelligence or Wisdom score by 1, to a maximum of 20.
* If you can see a creature's mouth while it is speaking a language you understand, you can interpret what it's saying by reading its lips.
* You have a +5 bonus to your passive Wisdom (Perception) and passive Intelligence (Investigation) scores.

```
name = 'Observant'
description = "***Feat: Observant.*** You are quick to notice details of your environment."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1
    npc.senses['passive Perception'] += 5
    npc.traits.append("***Observant.*** If you can see a creature's mouth while it is speaking a language you understand, you can interpret what it's saying by reading its lips. You have a +5 bonus to your passive Intelligence (Investigation) scores.")
```
