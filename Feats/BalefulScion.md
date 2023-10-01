## Baleful Scion
*Prerequisite: 4th Level, [Scion of the Outer Planes (Evil Outer Plane) Feat](ScionoftheOuterPlanes.md)*

You can channel cosmic forces of evil that cause pain but invigorate your being. You can choose your own actions despite this malign connection. You gain the following benefits:

* **Ability Score Increase**. Increase an ability score of your choice by 1, to a maximum of 20.
* **Life-Draining Grasp**. Once per turn, when you hit a creature with a melee weapon attack, you can also deal necrotic damage to it. The damage equals 1d6 + your proficiency bonus, and you regain a number of hit points equal to this necrotic damage dealt. You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Baleful Scion'
description = "***Feat: Baleful Scion.*** You can channel cosmic forces of evil that cause pain but invigorate your being."
def prereq(npc):
    if npc.levels() < 4: return False
    if 'Scion of the Outer Planes' not in npc.feats: return False
    return True
def apply(npc):
    chooseability(npc)
    npc.defer(lambda npc: npc.actions.append(f"***Life-Draining Grasp ({npc.proficiencybonus()}/Recharges on long rest).*** Once per turn, when you hit a creature with a melee weapon attack, you can also deal necrotic damage to it. The damage equals 1d6 + {npc.proficiencybonus()}, and you regain this number of hit points as well."))
```
