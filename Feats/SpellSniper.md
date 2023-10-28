## Spell Sniper
*Prerequisite: The ability to cast at least one spell*

You have learned techniques to enhance your attacks with certain kinds of spells, gaining the following benefits:

* When you cast a spell that requires you to make an attack roll, the spell's range is doubled.
* Your ranged spell attacks ignore half cover and three-quarters cover.
* You learn one cantrip that requires an attack roll. Choose the cantrip from the bard, cleric, druid, sorcerer, warlock, or wizard spell list. Your spellcasting ability for this cantrip depends on the spell list you chose from: Charisma for bard, sorcerer, and warlock; Wisdom for cleric or druid; or Intelligence for wizard.

```
name = 'Spell Sniper'
description = "***Feat: Spell Sniper.*** You have learned techniques to enhance your attacks with certain kinds of spells."
def prereq(npc): return len(npc.spellcasting) > 0
def apply(npc):
    npc.traits.append("***Spell Sniper.*** When you cast a spell that requires you to make an attack roll, the spell's range is doubled. Your ranged spell attacks ignore half cover and three-quarters cover.")
    spelllist = choose("Choose ", ['Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'])
    ability = ""
    if spelllist == 'Bard' or spelllist == 'Sorcerer' or spelllist == 'Warlock':
        ability = 'CHA'
    elif spelllist == 'Wizard':
        ability = 'INT'
    else:
        ability = 'WIS'
    spellcasting = innatecaster(npc, ability, name)
    spellcasting.cantripsknown.append(f"CHOOSE-{spelllist}")
```
