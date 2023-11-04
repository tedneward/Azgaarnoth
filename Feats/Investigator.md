## Investigator
You have an eye for detail and can pick out the smallest clues. You gain the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the Investigation skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You can take the Search action as a bonus action.

```
name = 'Investigator'
description = "***Feat: Investigator.*** You have an eye for detail and can pick out the smallest clues."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    npc.addskillorexpertise('Investigation')

    npc.bonusactions.append("***Investigative Search.*** You can take the Search action as a bonus action.")
```

