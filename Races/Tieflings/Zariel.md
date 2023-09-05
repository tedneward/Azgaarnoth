## Bloodline of Zariel
Tieflings with a blood tie to Zariel are stronger than the typical tiefling and receive magical abilities that aid them in battle.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Legacy of Avernus**. You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Searing Smite spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Zariel'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Zariel.*** Tieflings with a blood tie to Zariel are stronger than the typical tiefling and receive magical abilities that aid them in battle.")

    npc.STR += 1

    npc.cantripsknown.append('thaumaturgy')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('searing smite') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('searing smite')} as a 2nd-level spell or {spelllinkify('branding smite')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
