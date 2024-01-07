## Defensive Duelist
*Prerequisite: Dexterity 13 or higher*

You have learned how to use finesse weapons to defend yourself more effectively.

When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can use your reaction to add your proficiency bonus to your AC for that attack, potentially causing the attack to miss you.

```
name = 'Defensive Duelist'
description = "***Feat: Defensive Duelist.*** You have learned how to use finesse weapons to defend yourself more effectively."
def prereq(npc): return npc.DEX >= 13
def apply(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Defensive Parry.*** When you are wielding a finesse weapon with which you are proficient and another creature hits you with a melee attack, you can add +{npc.proficiencybonus()} to your AC for that attack, potentially causing the attack to miss you.") )
```
