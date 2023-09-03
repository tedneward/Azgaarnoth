# [Aasimari](../Creatures/Aasimari.md)

```
name = 'Aasimar'
type = 'humanoid, celestial'
```

* **Ability Score Increase**. Your Charisma score increases by 2.

* **Age**. Aasimar mature at the same rate as humans, but they can live up to 160 years.

* **Alignment**. Imbued with celestial power, most aasimar are good. Outcast aasimar are most often neutral or even evil.

* **Size**. Aasimar have the same range of height and weight as humans. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. Blessed with a radiant soul, your vision can easily cut through darkness. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Celestial Resistance**. You have resistance to necrotic damage and radiant damage.

* **Healing Hands**. As an action, you can touch a creature and cause it to regain a number of hit points equal to your level. Once you use this trait, you can't use it again until you finish a long rest.

* **Light Bearer**. You know the [light](https://www.dndbeyond.com/spells/light) cantrip. Charisma is your spellcasting ability for it.

* **Languages**. You can speak, read, and write Common and Celestial.

```
def level0(npc):
    npc.CHA += 2
    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.senses['darkvision'] = '60ft'
    npc.resistances.append('necrotic')
    npc.actions.append('***Healing Hands (Recharges after long rest).*** You can touch a creature and cause it to regain a number of hit points equal to your level.')
    npc.cantripsknown.append('light')
    npc.spellcastingattribute = 'Charisma'
    npc.languages.append('Common')
    npc.languages.append('Celestial')
```

## Aasimari Transformations
Aasimar often transform into one of three forms, depending on their personal views on the world; these are the "subraces" for aasimar characters:

* [Fallen](Fallen.md)
* [Protector](Protector.md)
* [Scourge](Scourge.md)

