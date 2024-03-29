# Earth Genasi
Tracing their ancestry to dao, the genies of the Elemental Plane of Earth, earth genasi inherit dao’s steadfast strength and control over earth.

An earth genasi’s skin can be the colors of stone and earth or a human skin tone with glittering sparkles like gem dust. Some earth genasi have lines marking their skin like cracks, either showing glimmering gemlike veins or a dim, yellowish glow. Earth genasi hair can appear carved of stone or crystal or resemble strands of spun metal.

***Earth Walk.*** You can move across difficult terrain without expending extra movement if you are using your walking speed on the ground or a floor.

***Merge with Stone.*** You know the [Blade Ward](../../Magic/Spells/blade-ward.md) cantrip. You can cast it as normal, and you can also cast it as a bonus action a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest.

Starting at 5th level, you can cast the [Pass Without Trace](../../Magic/Spells/pass-without-trace.md) spell with this trait, without requiring a material component. Once you cast that spell with this trait, you can’t do so again until you finish a long rest. You can also cast it using any spell slots you have of 2nd level or higher.

Intelligence, Wisdom, or Charisma is your spellcasting ability for these spells when you cast them with this trait (choose when you select this race).

***Earthen Resilience.*** You have advantage on saving throws against poison, you have resistance to poison damage, and you can't be petrified. Also, while you are buried or burrowing in earth, you don't need to breathe.

***Languages.*** Your character can speak, read, and write Common and Terran.

```
name = 'Earth'
description = "***Earth Genasi.*** Tracing their ancestry to dao, the genies of the Elemental Plane of Earth, earth genasi inherit dao’s steadfast strength and control over earth."
def level0(npc):
    npc.traits.append("***Earth Walk.*** You can move across difficult terrain without expending extra movement if you are using your walking speed on the ground or a floor.")

    npc.damageresistances.append("poison")
    npc.conditionimmunities.append("petrified")

    npc.traits.append("***Earthen Resilience.*** You have advantage on saving throws against poison, and while you are buried or burrowing in earth, you don't need to breathe.")

    mergeability = choose("Choose your innate spellcasting ability: ", ['INT', 'WIS', 'CHA'])
    npc.defer(lambda npc: npc.bonusactions.append(f"***Merge with Stone ({npc.proficiencybonus()}/Recharges on long rest).*** You can cast {spelllinkify('blade ward')}."))

    ability = choose("Choose Genasi spellcasting ability: ", ['INT', 'WIS', 'CHA'])
    spellcasting = innatecaster(npc, ability, 'Earth Genasi')
    spellcasting.cantripsknown.append('blade ward')

    npc.languages.append('Common')
    npc.languages.append('Terran')

def level5(npc):
    npc.spellcasting['Earth Genasi'].perday[1] = [ 'pass without trace' ]
```
