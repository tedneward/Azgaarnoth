# Air Genasi
Air genasi resemble djinn, the genies of the Elemental Plane of Air. Embodying many of the airy traits of their otherworldly ancestors, air genasi can draw upon their connection to the winds.

Air genasi’s skin tones include many shades of blue, along with the full range of human skin tones, with bluish or ashen casts. Sometimes their skin is marked by lines that seem like cracks with bluish-white energy spilling out. An air genasi’s hair might blow in a phantom wind or be made entirely of clouds or vapor.

**Speed.** Your walking speed is 35 feet.

**Unending Breath.** You can hold your breath indefinitely while you’re not incapacitated.

**Lightning Resistance.** You have resistance to lightning damage.

**Mingle with the Wind.** You know the [Shocking Grasp](../../Magic/Spells/shocking-grasp.md) cantrip. 

Starting at 3rd level, you can cast the [Feather Fall](../../Magic/Spells/feather-fall.md) spell with this trait, without requiring a material component. 

Starting at 5th level, you can also cast the [Levitate](../../Magic/Spells/levitate.md) spell with this trait, without requiring a material component. 

Once you cast Feather Fall or Levitate with this trait, you can’t cast that spell with it again until you finish a long rest. You can also cast either of those spells using any spell slots you have of the appropriate level. 

Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).

**Languages.** Your character can speak, read, and write Common and Aeral that you and your DM agree is appropriate for the character.

```
name = 'Air'
def level0(npc):
    npc.description.append("***Subrace: Air.*** Air genasi resemble djinn, the genies of the Elemental Plane of Air. Embodying many of the airy traits of their otherworldly ancestors, air genasi can draw upon their connection to the winds.")

    npc.speed['walking'] = 35

    npc.traits.append("***Unending Breath.*** You can hold your breath indefinitely while you’re not incapacitated.")
    npc.damageresistances.append("lightning")

    npc.mingleability = choose("Choose your spellcasting ability for Mingle with the Wind: ", ['INT', 'WIS', 'CHA'])

    npc.cantripsknown.append('shocking grasp')

    npc.languages.append('Common')
    npc.languages.append('Aeral')

def level3(npc):
    npc.actions.append(f"***Mingle with the Wind (Recharges on long rest).*** You can cast {spelllinkify('feather fall')}. {npc.mingleability} is your spellcasting ability for this spell.")

def level5(npc):
    replace("***Mingle with the Wind", npc.actions, f"***Mingle with the Wind (Recharges on long rest).*** You can cast {spelllinkify('feather fall')} and/or {spelllinkify('levitate')} once each. {npc.mingleability} is your spellcasting ability for these spells.")
```
