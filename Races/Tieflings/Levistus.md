## Bloodline of Levistus
Frozen Stygia is ruled by Levistus, an archdevil known for offering bargains to those who face an inescapable doom.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Legacy of Stygia**. You know the Ray of Frost cantrip. Once you reach 3rd level, you can cast the Armor of Agathys spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Levistus'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Levistus.*** Frozen Stygia is ruled by Levistus, an archdevil known for offering bargains to those who face an inescapable doom.")

    npc.CON += 1

    npc.cantripsknown.append('ray of frost')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('armor of agathys') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace(f"***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('armor of agathys')} as a 2nd-level spell or {spelllinkify('darkness')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
