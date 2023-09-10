## Bloodline of Dispater
The great city of Dis occupies most of Hell's second layer. It is a place where secrets are uncovered and shared with the highest bidder, making tieflings tied to Dispater excellent spies and infiltrators.

* **Ability Score Increase**. Your Dexterity score increases by 1.

* **Legacy of Dis**. You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Detect Thoughts spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Dispater'
description = "***Tiefling Bloodline of Dispater.*** The great city of Dis occupies most of Hell's second layer. It is a place where secrets are uncovered and shared with the highest bidder, making tieflings tied to Dispater excellent spies and infiltrators."
def level0(npc):
    npc.DEX += 1

    npc.cantripsknown.append('thaumaturgy')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('disguise self') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('disguise self')} as a 2nd-level spell or {spelllinkify('detect thoughts')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
