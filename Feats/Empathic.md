## Empathic
You possess keen insight into how other people think and feel. You gain the following benefits:

* Increase your Wisdom score by 1, to a maximum of 20.
* You gain proficiency in the Insight skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You can use your action to try to get uncanny insight about one humanoid you can see within 30 feet of you. Make a Wisdom (Insight) check contested by the target's Charisma (Deception) check. If your check succeeds, you have advantage on attack rolls and ability checks against the target until the end of your next turn.

```
name = 'Empathic'
description = "***Feat: Empathic.*** You possess keen insight into how other people think and feel."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    npc.addskillorexpertise('Insight')

    npc.actions.append("***Uncanny Insight.*** You can try to get uncanny insight about one humanoid you can see within 30 feet of you. Make a Wisdom (Insight) check contested by the target's Charisma (Deception) check. If your check succeeds, you have advantage on attack rolls and ability checks against the target until the end of your next turn.")
```
