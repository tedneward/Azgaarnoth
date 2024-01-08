# Sorcerous Origin: Divine Soul
Sometimes the spark of magic that fuels a sorcerer comes from a divine source that glimmers within the soul. Having such a blessed soul is a sign that your innate magic might come from a distant but powerful familial connection to a divine being. Perhaps your ancestor was an angel, transformed into a mortal and sent to fight in a god's name. Or your birth might align with an ancient prophecy, marking you as a servant of the gods or a chosen vessel of divine magic.

A Divine Soul, with natural magnetism, is seen as a threat by some religious hierarchies. As an outsider who commands celestial power, these sorcerers can undermine the existing order by claiming a direct tie to the divine. In some cultures, only those who can claim the power of a Divine Soul may command religious power. In these lands, ecclesiastical positions are dominated by a few bloodlines and preserved over generations.

```
name = 'Divine Soul'
description = "***Sorcerous Origin: Divine Soul.*** Sometimes the spark of magic that fuels a sorcerer comes from a divine source that glimmers within the soul. Having such a blessed soul is a sign that your innate magic might come from a distant but powerful familial connection to a divine being. Perhaps your ancestor was an angel, transformed into a mortal and sent to fight in a god's name. Or your birth might align with an ancient prophecy, marking you as a servant of the gods or a chosen vessel of divine magic."
```

## Divine Magic
*1st-level Divine Soul feature*

Your link to the divine allows you to learn spells normally associated with the cleric class. When your Spellcasting feature lets you learn a sorcerer cantrip or a sorcerer spell of 1st level or higher, you can choose the new spell from the cleric spell list or the sorcerer spell list. You must otherwise obey all the restrictions for selecting the spell, and it becomes a sorcerer spell for you.

In addition, choose an affinity for the source of your divine power: good, evil, law, chaos, or neutrality. You learn an additional spell based on that affinity, as shown below. It is a sorcerer spell for you, but it doesn't count against your number of sorcerer spells known. If you later replace this spell, you must replace it with a spell from the cleric spell list.

Affinity | Spell
-------- | -----
Good | Cure Wounds
Evil | Inflict Wounds
Law | Bless
Chaos | Bane
Neutrality | Protection from Evil and Good

```
def level1(npc):
    npc.divineaffinity = choose("Choose an a divine affinity?", ['Good', 'Evil', 'Law', 'Chaos', 'Neutrality'])
    if npc.divineaffinity == 'Good':
        npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('cure wounds')
    elif npc.divineaffinity == 'Evil':
        npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('inflict wounds')
    elif npc.divineaffinity == 'Law':
        npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('bless')
    elif npc.divineaffinity == 'Chaos':
        npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('bane')
    elif npc.divineaffinity == 'Neutrality':
        npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('protection from evil and good')
    else:
        print("Error!")
```

## Favored by the Gods
*1st-level Divine Soul feature*

Divine power guards your destiny. If you fail a saving throw or miss with an attack roll, you can roll 2d4 and add it to the total, possibly changing the outcome.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
    npc.traits.append("***Favored by the Gods (Recharges on short or long rest).*** If you fail a saving throw or miss with an attack roll, you can roll 2d4 and add it to the total, possibly changing the outcome.")
```

## Empowered Healing
*6th-level Divine Soul feature*

The divine energy coursing through you can empower healing spells. Whenever you or an ally within 5 feet of you rolls dice to determine the number of hit points a spell restores, you can spend 1 sorcery point to reroll any number of those dice once, provided you aren't incapacitated. You can use this feature only once per turn.

```
def level6(npc):
    npc.traits.append("***Empowered Healing (1/turn).*** Whenever you or an ally within 5 feet of you rolls dice to determine the number of hit points a spell restores, you can spend 1 sorcery point to reroll any number of those dice once, provided you aren't incapacitated.")
```

## Angelic Form
*14th-level Divine Soul feature*

You can use a bonus action to manifest a pair of spectral wings from your back. While the wings are present, you have a flying speed of 30 feet. The wings last until you're incapacitated, you die, or you dismiss them as a bonus action.

The affinity you chose for your Divine Magic feature determines the appearance of the spectral wings: eagle wings for good or law, bat wings for evil or chaos, and dragonfly wings for neutrality.

```
def level14(npc):
    npc.bonusactions.append("***Angelic Form.*** You manifest a pair of spectral wings from your back. While the wings are present, you have a flying speed of 30 feet. The wings last until you're incapacitated, you die, or you dismiss them as a bonus action.")
```

## Unearthly Recovery
*18th-level Divine Soul feature*

You gain the ability to overcome grievous injuries. As a bonus action when you have fewer than half of your hit points remaining, you can regain a number of hit points equal to half your hit point maximum.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level18(npc):
    npc.bonusactions.append("***Unearthly Recovery (Recharges on long rest).*** When you have fewer than half of your hit points remaining, you can regain a number of hit points equal to half your hit point maximum.")
```
