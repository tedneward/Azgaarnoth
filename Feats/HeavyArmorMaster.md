## Heavy Armor Master
*Prerequisite: Proficiency with heavy armor*

You can use your armor to deflect strikes that would kill others. You gain the following benefits:

* Increase your Strength score by 1, to a maximum of 20.
* While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical weapons is reduced by 3.

```
name = 'Heavy Armor Master'
description = "***Feat: Heavy Armor Master.*** You can use your heavy armor to deflect strikes that would kill others."
def prereq(npc): 
    for arm in armor['heavy']:
        if arm in npc.proficiencies:
            return True
    return False

def apply(npc):
    npc.STR += 1

    npc.traits.append("***Heavy Armor Master.*** While you are wearing heavy armor, bludgeoning, piercing, and slashing damage that you take from nonmagical weapons is reduced by 3.")
```
