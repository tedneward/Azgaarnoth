## Blood Crazed
*Prerequisite: Con 13+*

When in the depths of pain and madness you gain a savage strength.

* When suffering enough damage to be 50% or less of your normal hit points, you gain a +2 morale bonus to damage.

```
name = 'Blood Crazed'
description = "***Feat: Blood Crazed.*** When in the depths of pain and madness you gain a savage strength."
def prereq(npc): return npc.CON >= 13
def apply(npc):
    npc.traits.append("***Blood Crazed.*** When suffering enough damage to be 50% or less of your normal hit points, you gain +2 to damage due to morale.")
```
