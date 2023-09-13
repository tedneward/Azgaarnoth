# Fire Genasi
Descended from efreet, the genies of the Elemental Plane of Fire, fire genasi channel the flamboyant and often destructive nature of flame. They show their heritage in their skin tones, which can range from deep charcoal to shades of red and orange. Some bear skin tones common to humanity but with fiery marks, such as slowly swirling lights under their skin that resemble embers or glowing red lines tracing over their bodies like cracks. Fire genasi hair can resemble threads of fire or sooty smoke.

**Fire Resistance.** You have resistance to fire damage.

**Reach to the Blaze.** You know the [Produce Flame](../../Magic/Spells/produce-flame.md) cantrip. 

Starting at 3rd level, you can cast the [Burning Hands](../../Magic/Spells/burning-hands.md) spell with this trait.

Starting at 5th level, you can also cast the [Flame Blade](../../Magic/Spells/flame-blade.md) spell with this trait, without requiring a material component. 

Once you cast Burning Hands or Flame Blade with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level.

Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).

**Languages.** Your character can speak, read, and write Common and Pyro.

```
name = 'Fire'
description = "***Fire Genasi.*** Descended from efreet, the genies of the Elemental Plane of Fire, fire genasi channel the flamboyant and often destructive nature of flame. They show their heritage in their skin tones, which can range from deep charcoal to shades of red and orange. Some bear skin tones common to humanity but with fiery marks, such as slowly swirling lights under their skin that resemble embers or glowing red lines tracing over their bodies like cracks. Fire genasi hair can resemble threads of fire or sooty smoke."
def level0(npc):
    npc.damageresistances.append('fire')

    npc.newspellcasting('Genasi', choose("Choose a spellcasting ability: ", ['INT', 'WIS', 'CHA'])).cantripsknown.append('produce flame')

    npc.languages.append('Common')
    npc.languages.append('Pyro')

def level3(npc):
    npc.spellcasting['Genasi'].spells[1].append('burning hands')
    npc.spellcasting['Genasi'].slots = [ 1 ]

def level5(npc):
    npc.spellcasting['Genasi'].spells[1].append('flame blade')
    npc.spellcasting['Genasi'].slots = [ 1, 1 ]
```
