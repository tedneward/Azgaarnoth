## Silver-Tongued
You develop your conversational skill to better deceive others. You gain the following benefits:

* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency in the Deception skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* When you take the Attack action on your turn, you can replace one attack with an attempt to deceive one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Deception) check contested by the target's Wisdom (Insight) check. If your check succeeds, your movement doesn't provoke opportunity attacks from the target and your attack rolls against it have advantage; both benefits last until the end of your next turn or until you use this ability on a different target. If your check fails, the target can't be deceived by you in this way for 1 hour.

```
name = 'Silver-Tongued'
description = "***Feat: Silver-Tongued.*** You develop your conversational skill to better deceive others."
def prereq(npc): return True
def apply(npc):
    npc.CHA += 1

    npc.addskillorexpertise('Deception')

    npc.actions.append("***Silver-Tongued.*** When you take the Attack action on your turn, you can replace one attack with an attempt to deceive one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Deception) check contested by the target's Wisdom (Insight) check. If your check succeeds, your movement doesn't provoke opportunity attacks from the target and your attack rolls against it have advantage; both benefits last until the end of your next turn or until you use this ability on a different target. If your check fails, the target can't be deceived by you in this way for 1 hour.")
```
