# [Aasimari](../Creatures/Aasimari.md)

```
name = 'Aasimar'
type = 'humanoid, celestial'
subraces = {}
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

## Aasimar Transformations

### Protector Aasimar
Protector aasimar are charged by the powers of good to guard the weak, to strike at evil wherever it arises, and to stand vigilant against the darkness. From a young age, a protector aasimar receives advice and directives that urge to stand against evil.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Radiant Soul**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.
  
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.
  
  Once you use this trait, you can't use it again until you finish a long rest.

```
def protector_level0(npc): npc.WIS += 1
def protector_level3(npc): npc.actions.append("***Radiant Soul (Recharges after long rest).*** The aasimar can unleash the divine energy within itself, causing its eyes to glimmer and two luminous, incorporeal wings to sprout from its back. This transformation lasts for 1 minute or until the aasimar ends it as a bonus action. During it, the aasimar has a flying speed of 30 feet, and once on each of its turns, you can deal extra radiant damage (equal to its level) to one target when it deals damage to it with an attack or a spell.")

subraces['protector'] = {
    'name' : "Protector",
    'level0' : protector_level0,
    'level3' : protector_level3
}
```

---

### Scourge Aasimar
Scourge aasimar are imbued with a divine energy that blazes intensely within them. It feeds a powerful desire to destroy evil — a desire that is, at its best, unflinching and, at its worst, all-consuming. Many scourge aasimar wear masks to block out the world and focus on containing this power, unmasking themselves only in battle.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Radiant Consumption**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.

```
def scourge():
    def level0(npc): 
        npc.CON += 1
    
    def level3(npc): 
        npc.actions.append("***Radiant Consumption (Recharges after long rest).*** The aasimar can unleash the divine energy within it, causing a searing light to radiate from it, pouring out of its eyes and mouth. Its transformation lasts for 1 minute or until it ends it as a bonus action. During this time, the aasimar sheds bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of its turns, the aasimar and each creature within 10 feet of you take radiant damage equal to half its level (rounded up). In addition, once on each of its turns, the aasimar can deal extra radiant damage (equaling its level) to one target when it deals damage with an attack or a spell.")

    return {
        'name' : "Scourge",
        'level0' : scourge_level0,
        'level3' : scourge_level3
    }

subraces['scourge'] = scourge()
```

---

### Fallen Aasimar
An aasimar who was touched by dark powers as a youth or who turns to evil in early adulthood can become one of the fallen — a group of aasimar whose inner light has been replaced by shadow.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Necrotic Shroud**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn.

  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.

```
def fallen(): 
    def level0(npc): 
        npc.STR += 1

    def level3(npc): 
        npc.actions.append("***Necrotic Shroud (Recharges after long rest).*** ")

    return {
        'name' : "Fallen",
        'level0' : level0,
        'level3' : level3
    }

subraces['fallen'] = fallen()
```