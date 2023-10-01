## Grappler
*Prerequisite: Strength 13 or higher*

You've developed the skills necessary to hold your own in close-quarters grappling. You gain the following benefits:

* You have advantage on attack rolls against a creature you are grappling.
* You can use your action to try to pin a creature grappled by you. To do so, make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends.

```
name = 'Grappler'
description = "***Feat: Grappler.*** You've developed the skills necessary to hold your own in close-quarters grappling."
def prereq(npc): return npc.STR >= 13
def apply(npc):
    npc.traits.append("***Grappling.*** You have advantage on attack rolls against a creature you are grappling.")
    npc.actions.append("***Pin.*** If you are grappling a creature, you can make another grapple check. If you succeed, you and the creature are both restrained until the grapple ends.")
```
