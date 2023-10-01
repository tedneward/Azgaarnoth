## Alert
Always on the lookout for danger, you gain the following benefits:

* You can't be surprised while you are conscious.
* You gain a +5 bonus to initiative.
* Other creatures don't gain advantage on attack rolls against you as a result of being unseen by you.

```
name = 'Alert'
description = "***Feat: Alert.*** You are always on the lookout for danger."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Alert.*** You can't be surprised while you are conscious. You gain a +5 bonus to initiative. Other creatures don't gain advantage on attack rolls against you as a result of your not being able to see them.")
```
