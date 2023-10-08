## Cohort of Chaos
*Prerequisite: 4th Level, [Scion of the Outer Planes (Chaotic Outer Plane) Feat](#scion-of-the-outer-planes)*

You can channel the cosmic forces of chaos that drive the multiverse toward both freedom and disarray. Your actions are still yours to choose, but you gain these benefits:

* **Ability Score Increase**. Increase an ability score of your choice by 1, to a maximum of 20.

* **Chaotic Flare**. When you roll a 1 or a 20 on an attack roll or a saving throw, the magic of chaos flows through you. Roll on the Chaotic Flares table to determine what happens. A flare lasts until the end of your next turn, and a new flare can't occur until after the first flare ends.

d4 | Flare
-- | -----
1  | **Disruption Field**. Waves of energy ripple in a 10-foot sphere centered on you. Every creature other than you that starts its turn in that area, or that moves into that area for the first time on a turn, takes 1d8 force damage.
2  | **Battle Fury**. A creature of your choice that you can see is filled with reckless fury. The creature has advantage on attack rolls and disadvantage on ability checks.
3  | **Unbound**. When you move, you can use some or all of your walking speed to teleport once, along with any equipment you're wearing or carrying, up to the distance used to an unoccupied space that you can see.
4  | **Wailing Winds**. Howling winds swirl around you in a 60-foot radius. You and any creature in that radius has disadvantage on Wisdom saving throws.

You can also forcibly release a chaotic flare as a bonus action, rolling on the table as normal to determine the effects. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Cohort of Chaos'
description = "***Feat: Cohort of Chaos.*** You can channel the cosmic forces of chaos that drive the multiverse toward both freedom and disarray."
def prereq(npc):
    if npc.levels() < 4: return False
    if 'Scion of the Outer Planes' not in npc.feats: return False
    return True
    
def apply(npc):
    orderability = chooseability(npc)
    npc.defer(lambda npc: npc.traits.append(f"***Chaos Flare.*** When you roll a 1 or a 20 on an attack roll or a saving throw, the magic of chaos flows through you. A flare lasts until the end of your next turn, and a new flare can't occur until after the first flare ends. Roll a d4: **1. Disruption Field.** Waves of energy ripple in a 10-foot sphere centered on you. Every creature other than you that starts its turn in that area, or that moves into that area for the first time on a turn, takes 1d8 force damage. **2. Battle Fury.** A creature of your choice that you can see is filled with reckless fury. The creature has advantage on attack rolls and disadvantage on ability checks. **3. Unbound.** When you move, you can use some or all of your walking speed to teleport once, along with any equipment you're wearing or carrying, up to the distance used to an unoccupied space that you can see. **4. Wailing Winds.** Howling winds swirl around you in a 60-foot radius. You and any creature in that radius has disadvantage on Wisdom saving throws."))
    npc.bonusactions.append("***Chaos Flare ({npc.proficiencybonus()}/Recharges on long rest).*** You can also forcibly release a Chaos Flare, rolling as per the trait.")
```

