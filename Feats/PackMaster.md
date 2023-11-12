## Pack Master
*Prerequisites: Gnoll, 4th-level*

When taking down prey, the gnolls would surround dangerous opponents, rendering them ineffective in combat.

When flanking an opponent, you gain a +1 bonus to armor class against that opponent for each other gnoll (or other packmate) that is also flanking the opponent.

```
name = 'Pack Master'
description = "***Feat: Pack Master.*** When taking down prey, the gnolls would surround dangerous opponents, rendering them ineffective in combat."
def prereq(npc): return npc.race.name == 'Gnoll' and npc.levels() >= 4
def apply(npc):
    npc.traits.append("***Pack Master.*** When flanking an opponent, you gain a +1 bonus to armor class against that opponent for each other gnoll (or other packmate) that is also flanking the opponent.")
```
