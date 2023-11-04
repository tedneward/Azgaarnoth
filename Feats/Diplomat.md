## Diplomat
You master the arts of diplomacy, gaining the following benefits:

* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency in the Persuasion skill. If you are already proficient in this skill, you add double your proficiency bonus to checks you make with it.
* If you spend 1 minute talking to someone who can understand what you say, you can make a Charisma (Persuasion) check contested by the creature's Wisdom (Insight) check. If you or your companions are fighting the creature, your check automatically fails. If your check succeeds, the target is charmed by you as long as it remains within 60 feet of you and for 1 minute thereafter.

```
name = 'Diplomat'
description = "***Feat: Diplomat.*** You master the arts of diplomacy."
def prereq(npc): return True
def apply(npc):
    npc.CHA += 1

    npc.addskillorexpertise("Persuasion")

    npc.traits.append("***Diplomat.*** If you spend 1 minute talking to someone who can understand what you say, you can make a Charisma (Persuasion) check contested by the creature's Wisdom (Insight) check. If you or your companions are fighting the creature, your check automatically fails. If your check succeeds, the target is charmed by you as long as it remains within 60 feet of you and for 1 minute thereafter.")
```

