## Brawny
You become stronger, gaining the following benefits:

* Increase your Strength score by 1, to a maximum of 20.
* You gain proficiency in the Athletics skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You count as if you were one size larger for the purpose of determining your carrying capacity.

```
name = 'Brawny'
description = "***Feat: Brawny.*** You are stronger."
def prereq(npc): return True
def apply(npc):
    npc.STR += 1

    npc.addskillorexpertise("Athletics")

    npc.traits.append("***Brawny.*** You count as if you were one size larger for the purpose of determining your carrying capacity.")
```
