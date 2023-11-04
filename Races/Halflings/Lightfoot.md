## Lightfoot Halflings
The Lightfoot family is an wide-sprawling family tree of halflings who were some of the world's best stealth artists; not that the Lightfoots knew how to turn invisible, but that the Lightfoot family perfected the art of being present without being noticed. They tend to be affable in social situations, getting along well with others, and when they choose to be, utterly forgettable.

```
name = 'Lightfoot'
description = "***Lightfoot Halfling.***"
```

**Ability Score Increase.** Your Charisma score increases by 1.

**Naturally Stealthy.** You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.

```
def level0(npc):
    npc.CHA += 1
    npc.traits.append("***Naturally Stealthy.*** You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you.")
```
