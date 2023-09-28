## Bloodline of Levistus
Frozen Stygia is ruled by Levistus, an archdevil known for offering bargains to those who face an inescapable doom.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Legacy of Stygia**. You know the Ray of Frost cantrip. Once you reach 3rd level, you can cast the Armor of Agathys spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Levistus'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Levistus.*** Frozen Stygia is ruled by Levistus, an archdevil known for offering bargains to those who face an inescapable doom.")

    npc.CON += 1

    spellcasting = innatecaster(npc, 'CHA', "Levistus Tiefling")
    spellcasting.cantripsknown.append('ray of frost')

def level3(npc):
    npc.spellcasting['Levistus Tiefling'].perday[1] = ['armor of agathys']

def level5(npc):
    npc.spellcasting['Levistus Tiefling'].perday[1].append('darkness')
```
