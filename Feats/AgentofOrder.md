## Agent of Order
*Prerequisite: 4th Level, [Scion of the Outer Planes (Lawful Outer Plane) Feat](#scion-of-the-outer-planes)*

You can channel cosmic forces of order that lock the multiverse into patterns. Your actions are your own to choose, but these forces grant you the following benefits:

* Increase an ability score of your choice by 1, to a maximum of 20.
* **Stasis Strike.** Once per turn when you damage a creature you can see within 60 feet of yourself, you can deal an extra 1d8 force damage to the target, and it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + the modifier of the ability score increased by this feat) or be restrained by spectral bindings until the start of your next turn. These bindings manifest as chains, gears, encasing stone, or some other symbol of stasis. You can use this benefit a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Agent of Order'
description = "***Feat: Agent of Order.*** You can channel cosmic forces of order that lock the multiverse into patterns."
def prereq(npc):
    if npc.levels() < 4: return False
    if 'Scion of the Outer Planes' not in npc.feats: return False
    return True
    
def apply(npc):
    orderability = chooseability(npc)
    npc.defer(lambda npc: npc.traits.append(f"***Stasis Strike ({npc.proficiencybonus()}/Recharges on long rest).*** Once per turn when you damage a creature you can see within 60 feet of yourself, you can deal an extra 1d8 force damage to the target, and it must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(orderability)}) or be restrained by spectral bindings until the start of your next turn. These bindings manifest as chains, gears, encasing stone, or some other symbol of stasis.") )
```
