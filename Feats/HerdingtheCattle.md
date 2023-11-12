## Herding the Cattle
*Prerequisites: Confusing Onslaught feat, Int 13+*

You panic your foes and lead them right to the slaughter.

Panicked creatures moving into or out of your threatened area incur attacks of opportunity.

```
name = 'Herding the Cattle'
description = "***Feat: Herding the Cattle.*** You panic your foes and lead them right to the slaughter."
def prereq(npc): return "Confusing Onslaught" in npc.feats and npc.INT >= 13
def apply(npc):
    npc.traits.append("***Herding the Cattle.*** Panicked creatures moving into or out of your threatened area incur attacks of opportunity.")
```
