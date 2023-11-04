## Historian
Your study of history rewards you with the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the History skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* When you take the Help action to aid another creature's ability check, you can make a DC 15 Intelligence (History) check. On a success, that creature's check gains a bonus equal to your proficiency bonus, as you share pertinent advice and historical examples. To receive this bonus, the creature must be able to understand what you're saying.

```
name = 'Historian'
description = "***Feat: Historian.*** Your study of history rewards you with benefits."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1
    npc.addskillorexpertise("History")
    npc.defer(lambda npc: npc.actions.append("***Help.*** When you aid another creature's ability check, you can make a DC 15 Intelligence (History) check. On success, the creature's check gains a +{npc.proficiencybonus()} bonus as you share pertinent advice and historical examples, but to receive this bonus, the creature must be able to understand what you're saying.") )
```
