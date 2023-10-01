## Tough
Your hit point maximum increases by an amount equal to twice your level when you gain this feat. Whenever you gain a level thereafter, your hit point maximum increases by an additional 2 hit points

```
name = 'Tough'
description = "***Feat: Tough.*** You are harder to kill."
def prereq(npc): return True
def apply(npc):
    print("Taking this feat at level " + str(npc.levels()))
    npc.hitpoints += npc.levels() * 2
    def hitpointadjustment(npc): npc.hitpoints += (2 * npc.levels())
    npc.defer(lambda npc: hitpointadjustment(npc))
```
