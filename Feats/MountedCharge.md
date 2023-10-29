## Mounted Charge
*Prerequisite: Mounted Combatant*

As a mounted combatant, you have learned how to charge past an opponent and execute your attacks (including those of your mount) and pass the target without triggering attacks of opportunity.

```
name = 'Mounted Charge'
description = "***Feat: Mounted Charge.*** You have learned new skills as a mounted combatant."
def prereq(npc): return "Mounted Combatant" in npc.feats
def apply(npc):
    npc.actions.append("***Mounted Charge.*** You charge past an opponent and execute your attacks (including those of your mount) and pass the target without triggering attacks of opportunity.")
```
