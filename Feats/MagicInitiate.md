## Magic Initiate
Choose a class: bard, cleric, druid, sorcerer, warlock, or wizard. You learn two cantrips of your choice from that class's spell list. In addition, choose one 1st-level spell to learn from that same list. Using this feat, you can cast that spell once at its lowest level, and you must finish a long rest before you can cast it in this way again.

Your spellcasting ability for these spells depends on the class you chose: Charisma for bard, sorcerer, or warlock; Wisdom for cleric or druid; or Intelligence for wizard.

```
name = 'Magic Initiate'
description = "***Feat: Magic Initiate.*** You understand some of the fundamentals of spellcasting above and beyond any formal training."
def prereq(npc): return True
def apply(npc):
    miclass = choose("Choose a class: ", ['Bard', 'Cleric', 'Druid', 'Sorcerer', 'Warlock', 'Wizard'])
    ability = 'CHA' if miclass in ['Bard','Sorcerer','Warlock'] else 'WIS' if miclass in ['Cleric', 'Druid'] else 'INT'

    spellcasting = innatecaster(npc, ability, name)
    spellcasting.maxcantripsknown = 2
    spellcasting.perday[1] = [f'CHOOSE-1st-level-{miclass}']
```
