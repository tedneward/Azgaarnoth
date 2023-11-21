## Improved Vicious Bite
*Prerequisites: Vicious Bite feat*

Some gnolls are famed for tearing out their opponent's throats with a single bite.

Your bite's critical hit range is 19-20 and deals x3 critical damage.

```
name = 'Improved Vicious Bite'
description = "***Feat: Improved Vicious Bite.*** Some gnolls are famed for tearing out their opponent's throats with a single bite."
def prereq(npc): return 'Vicious Bite' in npc.feats
def apply(npc):
    npc.traits.append("***Improved Vicious Bite.*** Your Bite attack's critical hit range is 19-20 and deals x3 critical damage.")
```
