## Defensive Duelist
*Prerequisite: Dexterity 13 or higher*

When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you.

```
name = 'Defensive Duelist'
description = "***Feat: Defensive Duelist.***"
def prereq(npc): return npc.DEX >= 13
def apply(npc):
    npc.reactions.append("***Defensive Parry.*** When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you.")
```
