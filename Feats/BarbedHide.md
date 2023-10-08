## Barbed Hide
*Prerequisite: The ability to cast at least one spell*

You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following benefits:

* When you cast a spell that requires you to make an attack roll, the spell's range is doubled.
* Your ranged spell attacks ignore half cover and three-quarters cover.
* You learn one cantrip that requires an attack roll. Choose the cantrip from the bard, cleric, druid, sorcerer, warlock, or wizard spell list. Your spellcasting ability for this cantrip depends on the spell list you chose from: Charisma for bard, sorcerer, and warlock; Wisdom for cleric or druid; or Intelligence for wizard.

```
name = 'Barbed Hide'
description = "***Feat: Barbed Hide.*** You have learned techniques to enhance your attacks with certain kinds of spells."
def prereq(npc): return len(npc.spellcasting.keys()) > 0
def apply(npc):
    npc.traits.append("***Barbed Hide. When you cast a spell that requires you to make an attack roll, the spell's range is doubled. These attacks ignore half- and three-quarters cover.")
    npc.description.append("***TODO: Choose cantrip that requires an attack roll, from Bard, Cleric, Druid, Sorcerer, Warlock, or Wizard spell lists. Your spellcasting ability for this cantrip depends on the spell list: CHA for Bard/Sorcerer/Warlock; WIS for Cleric or Druid; INT for Wizard.")
```
