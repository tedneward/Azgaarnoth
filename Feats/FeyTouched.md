## Fey Touched
Your exposure to the Feywild or one of its denizens has left a magical mark on you. You gain the following benefits:

* Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.
* You learn the [misty step](http://azgaarnoth.tedneward.com/magic/spells/misty-step) spell and one 1st-level spell of your choice. The 1st-level spell must be from the divination or enchantment school of magic. You can cast each of these spells without expending a spell slot. Once you cast either of these spells in this way, you can't cast that spell in this way again until you finish a long rest. You can also cast these spells using spell slots you have of the appropriate level. The spells' spellcasting ability is the ability increased by this feat.

```
name = 'Fey-Touched'
description = "***Feat: Fey-Touched.*** Your exposure to the Feywild or one of its denizens has left a magical mark on you."
def prereq(npc): return True
def apply(npc):
    ability = choose("Choose one: ", ['INT', 'WIS','CHA'])
    if ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    else: npc.CHA += 1

    spellcasting = innatecaster(npc, ability, name)
    spellcasting.perday[1] = ['misty step', 'CHOOSE-1st-divination-or-enchantment']
```
