## Water
Water genasi descend from marids, aquatic genies from the Elemental Plane of Water. Water genasi are perfectly suited to life underwater and carry the power of the waves inside themselves.

Their skin is often shades of blue or green, sometimes a blend of the two. If they have a human skin tone, there is a glistening texture that catches the light, like water droplets or nearly invisible fish scales. Their hair can resemble seaweed, waving as if in a current, or it can even be like water itself.

**Acid Resistance.** You have resistance to acid damage.

**Call to the Wave.** You know the [Acid Splash](../../Magic/Spells/acid-splash.md) cantrip. 

Starting at 3rd level, you can cast the [Create or Destroy Water](../../Magic/Spells/create-or-destroy-water.md) spell with this trait. 

Starting at 5th level, you can also cast the [Water Walk](../../Magic/Spells/water-walk.md) spell with this trait, without requiring a material component. 

Once you cast Create or Destroy Water or Water Walk with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level.

Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).

**Languages.** Your character can speak, read, and write Common and Aquan.

```
name = 'Water'
def level0(npc):
    npc.description.append("***Subrace: Water.*** Water genasi descend from marids, aquatic genies from the Elemental Plane of Water. Water genasi are perfectly suited to life underwater and carry the power of the waves inside themselves.")

    npc.damageresistances.append('acid')

    npc.water = choose("Choose a spellcasting ability: ", ['INT', 'WIS', 'CHA'])
    npc.cantripsknown.append('acid splash')

    npc.languages.append('Common')
    npc.languages.append('Aquan')

def level3(npc):
    npc.actions.append(f"***Call to the Wave (Recharges on long rest).*** You can cast {spelllinkify('create or destroy water')} using {npc.water} as your spellcasting ability. You can also use spell slots to cast this.")

def level5(npc):
    npc.actions.append(f"***Improved Reach to the Blaze (Recharges on long rest).*** You can cast {spelllinkify('create or destroy water')} or {spelllinkify('water walk')} using {npc.water} as your spellcasting ability. You can also use spell slots to cast these.")
```
