## Menacing
You become fearsome to others, gaining the following benefits:

* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency in the Intimidation skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* When you take the Attack action on your turn, you can replace one attack with an attempt to demoralize one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Intimidation) check contested by the target's Wisdom (Insight) check. If your check succeeds, the target is frightened until the end of your next turn. If your check fails, the target can't be frightened by you in this way for 1 hour.

```
name = 'Menacing'
description = "***Feat: Menacing.*** You become fearsome to others."
def prereq(npc): return True
def apply(npc):
    npc.CHA += 1

    npc.addskillorexpertise('Intimidation')

    npc.actions.append("***Attack: Demoralize.*** When you take the Attack action on your turn, you can replace one attack with an attempt to demoralize one humanoid you can see within 30 feet of you that can see and hear you. Make a Charisma (Intimidation) check contested by the target's Wisdom (Insight) check. If your check succeeds, the target is frightened until the end of your next turn. If your check fails, the target can't be frightened by you in this way for 1 hour.")
```

