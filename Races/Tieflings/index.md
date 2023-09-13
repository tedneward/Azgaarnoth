# Tiefling

* **Ability Score Increase**. Your Charisma score increases by 2. (This is true of all tieflings, regardless of bloodline.)

* **Age** Tieflings mature at the same rate as humans but live a few years longer.

* **Alignment** Tieflings might not have an innate tendency toward evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment.

* **Size** Tieflings are about the same size and build as humans. Your size is Medium.

* **Speed** Your base walking speed is 30 feet.

* **Darkvision** Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

* **Hellish Resistance** You have resistance to fire damage.

* **Languages** You can speak, read, and write Common and Infernal.

```
name = 'Tiefling'
description = "***Race: Tiefling.*** "
type = 'humanoid/abyssal'
def level0(npc):
    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.CHA += 2

    npc.senses['darkvision'] = 60

    npc.damageresistances.append('fire')

    npc.languages.append('Common')
    npc.languages.append('Infernal')
```

## Tiefling Bloodlines

Tieflings have a number of bloodlines (subraces), all depending on their infernal heritage:

* [Asmodeus](Asmodeus.md)
* [Baalzebul](Baalzebul.md)
* [Dispater](Dispater.md)
* [Fierna](Fierna.md)
* [Glasya](Glasya.md)
* [Levistus](Levistus.md)
* [Mammon](Mammon.md)
* [Mephistopheles](Mephistopheles.md)
* [Zariel](Zariel.md)

Some tieflings have a less-noble bloodline, but still inherit infernal characteristics:

* [Devil's Tongue](DevilsTongue.md)
* [Winged](Winged.md)
