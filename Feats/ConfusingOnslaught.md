## Confusing Onslaught
*Prerequisites: Chaotic alignment, Gnoll*

The gnolls charge, howling wildly and their chaotic attack confuses their opponents.

If you move up to your full movement before taking an Attack/Multiattack/Extra Attacks action, you gain advantage on the attack(s).

```
name = 'Confusing Onslaught'
description = "***Feat: Confusing Onslaught.*** Your chaotic attack confuses your opponents."
def prereq(npc): return npc.race.name == 'Gnoll'
def apply(npc):
    npc.traits.append("***Confusing Onslaught.*** If you move up to your full movement before taking an Attack/Multiattack/Extra Attacks action, you gain advantage on the attack(s).")
```
