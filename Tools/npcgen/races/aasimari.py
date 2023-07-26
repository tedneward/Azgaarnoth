"""
# Aasimari

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

## Aasimar Transformations

### Protector Aasimar
Protector aasimar are charged by the powers of good to guard the weak, to strike at evil wherever it arises, and to stand vigilant against the darkness. From a young age, a protector aasimar receives advice and directives that urge to stand against evil.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Radiant Soul**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.
  
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.
  
  Once you use this trait, you can't use it again until you finish a long rest.

### Scourge Aasimar
Scourge aasimar are imbued with a divine energy that blazes intensely within them. It feeds a powerful desire to destroy evil — a desire that is, at its best, unflinching and, at its worst, all-consuming. Many scourge aasimar wear masks to block out the world and focus on containing this power, unmasking themselves only in battle.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Radiant Consumption**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.

### Fallen Aasimar
An aasimar who was touched by dark powers as a youth or who turns to evil in early adulthood can become one of the fallen — a group of aasimar whose inner light has been replaced by shadow.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Necrotic Shroud**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn.

  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.
"""

name = 'Aasimari'
def apply_race(npc):
    npc.CHA += 2

    npc.race = 'Aasimar'
    npc.size = 'Medium'
    npc.speed = '30ft'

    npc.features.append("**Darkvision**. Blessed with a radiant soul, your vision can easily cut through darkness. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")

    npc.resistances.append('necrotic')
    npc.resistances.append('radiant')

    npc.actions.append("**Healing Hands.** As an action, you can touch a creature and cause it to regain a number of hit points equal to your level. Once you use this trait, you can't use it again until you finish a long rest.")
    npc.actions.append("**Light Bearer.** You know the [light](https://www.dndbeyond.com/spells/light) cantrip. Charisma is your spellcasting ability for it.")

    npc.languages.append("Common")
    npc.languages.append("Celestial")

subraces = ['Protector', 'Scourge', 'Fallen']
def apply_subrace(which, npc):
    if which == subraces[0]:
        npc.description.append("Protector aasimar are charged by the powers of good to guard the weak, to strike at evil wherever it arises, and to stand vigilant against the darkness. From a young age, a protector aasimar receives advice and directives that urge to stand against evil.")
        npc.WIS += 1
        npc.features.append("**Radiant Soul.** Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
    elif which == subraces[1]:
        npc.description.append("Scourge aasimar are imbued with a divine energy that blazes intensely within them. It feeds a powerful desire to destroy evil — a desire that is, at its best, unflinching and, at its worst, all-consuming. Many scourge aasimar wear masks to block out the world and focus on containing this power, unmasking themselves only in battle.")
        npc.CON += 1
        npc.features.append("**Radiant Consumption.** Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
    elif which == subraces[2]:
        replace('**Light Bearer.**', npc.actions, "**Shadow Bearer.** You know the [chill touch]() cantrip. Charisma is your spellcasting ability for it.")
        npc.description.append("An aasimar who was touched by dark powers as a youth or who turns to evil in early adulthood can become one of the fallen — a group of aasimar whose inner light has been replaced by shadow.")
        npc.STR += 1
        npc.actions.append("**Necrotic Shroud.** Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn.\nYour transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.\nOnce you use this trait, you can't use it again until you finish a long rest.")
    else:
        raise 'Invalid Aasimari subrace: ' + which
    npc.subrace = which
