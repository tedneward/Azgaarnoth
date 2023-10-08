# Martial Archetype: Elemental Blade
The Elemental Blade is a fighter with a special connection to primeval magic, allowing them to channel energy into their attacks and defense. Their power is neither arcane nor divine, but elemental--coming directly from the elemental planes themselves.

```
name = "Elemental Blade"
description = "***Martial Archetype: Elemental Blade.*** The Elemental Blade is a fighter with a special connection to primeval magic, allowing them to channel energy into their attacks and defense. Their power is neither arcane nor divine, but elemental--coming directly from the elemental planes themselves."
```

## Infuse Weapon with Energy
*3rd-level Elemental Blade feature*

You can infuse your weapon with the energy of your choice: acid, cold, fire, lightning, radiant, and thunder. Although the amount of damage you deal remains unchanged for the weapon you are using, the damage becomes the type of energy you have chosen. The weapon takes on the physical characteristics of that energy type (in other words, swords that are fire-infused appear to be flaming while those infused with cold look as though they are covered in frost, etc.), and they interact with the environment in the way in which that element would. For example, if your sword is infused with fire, touching it to a fallen troll prevents it from regenerating. If you infuse your weapon with cold and then submerge it in water, it begins turning to ice. You have damage resistance to the selected energy type when you are using this ability.

This effect lasts for ten rounds and you can use it twice per short rest.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Infuse Energy ({'2' if npc.levels('Fighter') < 7 else '3' if npc.levels('Fighter') < 15 else '4'}/Recharges on short rest).*** You can infuse your weapon with the energy of your choice: acid, cold, fire, lightning, radiant, and thunder. {'Although the amount of damage you deal remains unchanged for the weapon you are using,' if npc.levels('Fighter') < 7 else 'The damage is increased by 1d4 points and all' if npc.levels('Fighter') < 15 else 'The damage is increased by 1d6 points and all'} the damage becomes the type of energy you have chosen. The weapon takes on the physical characteristics of that energy type (in other words, swords that are fire-infused appear to be flaming while those infused with cold look as though they are covered in frost, etc.), and they interact with the environment in the way in which that element would. For example, if your sword is infused with fire, touching it to a fallen troll prevents it from regenerating. If you infuse your weapon with cold and then submerge it in water, it begins turning to ice. You have damage resistance to the selected energy type when you are using this ability. This effect lasts for {'ten' if npc.levels('Fighter') < 15 else 'fifteen'} rounds."))
```

## Additional Elemental Damage
*7th-level Elemental Blade feature*

Your elemental damage is increased to an additional 1d4 points matching the type of energy you infused the weapon with. It otherwise acts as the Infuse Weapon With Energy ability. This lasts for ten rounds, and it can be activated three times per short rest.

## Energy Ring
*10th-level Elemental Blade feature*

You can surround yourself in a ring of the energy of your choice. When a character attacks you, it must make a Dexterity save DC = 8 + your proficiency bonus + your Charisma modifier. This ability counts as a reaction. If it fails this check, the energy damages your opponent, dealing 1d8 points of damage plus your Charisma modifier. This effect lasts ten rounds and can be used three times per short rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Energy Ring (3/Recharges on short rest).*** You can surround yourself in a ring of the energy of your choice. When a character attacks you, it must make a Dexterity save (DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}). If it fails this check, the energy damages your opponent, dealing 1d8 + {npc.CHAbonus()}points of damage. This effect lasts ten rounds."))
```

## Elemental Damage Increase
*15th-level Elemental Blade feature*

The additional damage you deal when infusing your weapon with energy is increased to 1d6 points of damage. This now lasts for fifteen rounds and can be used four times per short rest.

## Permanent Infusion
*18th-level Elemental Blade feature*

You pick a type of energy, and you become permanently infused with it. At this time, the elemental damage on your weapon becomes permanent, as does the Energy Ring around you. You gain immunity to this energy type. Your body takes on some of the physical characteristics of the energy type (how this manifests is between you and your GM, but might involve eye or hair color that matches the energy type). You can temporarily change the type of energy you are infused with, but that effect lasts for fifteen rounds and can be done four times per short rest.

```
def level18(npc):
    energy = choose("Choose an energy type: ", ['acid', 'cold', 'fire', 'lightning', 'radiant', 'thunder'])
    npc.subclasses['Fighter'].energytype = energy
    npc.damageimmunities.append(energy)
    npc.traits.append("***Permanent Infusion.*** You are permanently infused with " + energy + " energy. At this time, the elemental damage on your weapon becomes permanent, as does the Energy Ring around you. You can temporarily change the type of energy you are infused with, but that effect lasts for fifteen rounds and can be done four times per short rest.")
```
