## Stealthy
You know how best to hide. You gain the following benefits:

* Increase your Dexterity score by 1, to a maximum of 20.
* You gain proficiency in the Stealth skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* If you are hidden, you can move up to 10 feet in the open without revealing yourself if you end the move in a position where you're not clearly visible.

```
name = 'Stealthy'
description = "***Feat: Stealthy.*** You know how best to hide."
def prereq(npc): return True
def apply(npc):
    npc.DEX += 1
    npc.addskillorexpertise('Stealth')
    npc.traits.append("***Stealthy.*** If you are hidden, you can move up to 10 feet in the open without revealing yourself if you end the move in a position where you're not clearly visible.")
```
