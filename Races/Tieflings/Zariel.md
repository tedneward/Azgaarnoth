## Bloodline of Zariel
Tieflings with a blood tie to Zariel are stronger than the typical tiefling and receive magical abilities that aid them in battle.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Legacy of Avernus**. You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Searing Smite spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Branding Smite spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Zariel'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Zariel.*** Tieflings with a blood tie to Zariel are stronger than the typical tiefling and receive magical abilities that aid them in battle.")

    npc.STR += 1

    spellcasting = innatecaster(npc, 'CHA', name + " Tiefling")
    spellcasting.cantripsknown.append('thaumaturgy')

def level3(npc):
    npc.spellcasting[name + ' Tiefling'].perday[1] = [ 'searing smite' ]

def level5(npc):
    npc.spellcasting[name + ' Tiefling'].perday[1].append('branding smite')
```
