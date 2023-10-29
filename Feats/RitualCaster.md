## Ritual Caster
*Prerequisite: Intelligence or Wisdom of 13 or higher*

You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them.

When you choose this feat, you acquire a ritual book holding two 1st-level spells of your choice. Choose one of the following classes: bard, cleric, druid, sorcerer, warlock, or wizard. You must choose your spells from that class's spell list, and the spells you choose must have the ritual tag. The class you choose also determines your spellcasting ability for these spells: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard.

If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, you might be able to add it to your ritual book. The spell must be on the spell list for the class you chose, the spell's level can be no higher than half your level (rounded up), and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents the material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it.

```
name = 'Ritual Caster'
description = "***Feat: Ritual Caster.*** You have learned a number of spells that you can cast as rituals. These spells are written in a ritual book, which you must have in hand while casting one of them."
def prereq(npc): return npc.INT >= 13 or npc.WIS >= 13
def apply(npc):
    spelllist = choose("Choose ", ['Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'])
    ability = ""
    if (spelllist == 'Bard') or (spelllist == 'Sorcerer') or (spelllist == 'Warlock'):
        ability = 'CHA'
    elif spelllist == 'Wizard':
        ability = 'INT'
    elif (spelllist == 'Cleric') or (spelllist == 'Druid'):
        ability = 'WIS'
    else:
        error("WTF?!?")

    npc.defer(lambda npc: npc.traits.append(f"***Ritual Caster.*** If you come across a spell in written form, such as a magical spell scroll or a wizard's spellbook, you might be able to add it to your ritual book. The spell must be on the {spelllist} spell list, the spell's level can be no higher than {(npc.levels() // 2) + 1}, and it must have the ritual tag. The process of copying the spell into your ritual book takes 2 hours per level of the spell, and costs 50 gp per level. The cost represents the material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it.") )

    spellcasting = innatecaster(npc, ability, name)
    spellcasting.spells[1] = ['CHOOSE', 'CHOOSE']
```
