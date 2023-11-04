## Master of Disguise
You have honed your ability to shape your personality and to read the personalities of others. You gain the following benefits:

* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency with the disguise kit. If you are already proficient with it, you add double your proficiency bonus to checks you make with it.
* If you spend 1 hour observing a creature, you can then spend 8 hours crafting a disguise you can quickly don to mimic that creature. Making the disguise requires a disguise kit. You must make checks as normal to disguise yourself, but you can assume the disguise as an action.

```
name = 'Master of Disguise'
description = "***Feat: Master of Disguise.*** You have honed your ability to shape your personality and to read the personalities of others."
def prereq(npc): return True
def apply(npc):
    npc.CHA += 1
    
    npc.addskillorexpertise('Disguise Kit')
    
    npc.traits.append("***Careful Observation.*** If you spend 1 hour observing a creature, you can then spend 8 hours crafting a disguise you can quickly don to mimic that creature. Making the disguise requires a disguise kit. You must make checks as normal to disguise yourself, but you can assume the disguise as an action.")
```
