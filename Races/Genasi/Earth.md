# Earth Genasi
Tracing their ancestry to dao, the genies of the Elemental Plane of Earth, earth genasi inherit dao’s steadfast strength and control over earth.

An earth genasi’s skin can be the colors of stone and earth or a human skin tone with glittering sparkles like gem dust. Some earth genasi have lines marking their skin like cracks, either showing glimmering gemlike veins or a dim, yellowish glow. Earth genasi hair can appear carved of stone or crystal or resemble strands of spun metal.

**Earth Walk.** You can move across difficult terrain without expending extra movement if you are using your walking speed on the ground or a floor.

**Merge with Stone.** You know the [Blade Ward](../../Magic/Spells/blade-ward.md) cantrip. You can cast it as normal, and you can also cast it as a bonus action a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest.
Starting at 5th level, you can cast the [Pass Without Trace](../../Magic/Spells/pass-without-trace.md) spell with this trait, without requiring a material component. Once you cast that spell with this trait, you can’t do so again until you finish a long rest. You can also cast it using any spell slots you have of 2nd level or higher.
Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).

**Languages.** Your character can speak, read, and write Common and Terran.

```
name = 'Earth'
description = "***Earth Genasi.*** Tracing their ancestry to dao, the genies of the Elemental Plane of Earth, earth genasi inherit dao’s steadfast strength and control over earth."
def level0(npc):
    npc.traits.append("***Earth Walk.*** You can move across difficult terrain without expending extra movement if you are using your walking speed on the ground or a floor.")

    mergeability = choose("Choose your spellcasting ability for Merge with Stone: ", ['INT', 'WIS', 'CHA'])

    npc.newspellcasting('Genasi', choose("Choose Genasi spellcasting ability: ", ['INT', 'WIS', 'CHA']))

    npc.spellcasting['Genasi'].cantripsknown.append('blade ward')

    npc.languages.append('Common')
    npc.languages.append('Terran')

def level5(npc):
    npc.spellcasting['Genasi'].spells[2].append('pass without trace')
    npc.spellcasting['Genasi'].slots = [ 0, 1 ]
```
