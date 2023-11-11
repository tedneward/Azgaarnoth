## Vicious Bite
*Prerequisites: Str 13+, gnoll*

You have developed a ferocious bite that even other gnolls fear.

You can make a Bite attack as a bonus action.

```
name = 'Vicious Bite'
description = "***Feat: Vicious Bite.*** You have developed a ferocious bite attack that even other gnolls fear."
def prereq(npc): return npc.race.name == 'Gnoll' and npc.STR >= 13
def apply(npc):
    npc.bonusactions.append("***Vicious Bite.*** You make one Bite attack.")
```
