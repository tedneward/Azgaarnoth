## Artificer Initiate
You've learned some of an [artificer](../Classes/Artificer.md)'s inventiveness, granting you the following benefits:

* You learn one cantrip of your choice from the artificer spell list, and you learn one 1st-level spell of your choice from that list. Intelligence is your spellcasting ability for these spells. Whenever you gain a level, you can replace one of these spells with another spell of the same level from the artificer spell list.
* You can cast this feat's 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have.
* You gain proficiency with one type of artisan's tools of your choice, and you can use that type of tool as a spellcasting focus for any spell you cast that uses Intelligence as its spellcasting ability.

```
name = 'Artificer Initiate'
description = "***Feat: Artificer Initiate.*** You've learned some of an artificer's inventiveness."
def prereq(npc): return True
def apply(npc):
    spellcasting = halfcaster(npc, 'INT')
    spellcasting.cantripsknown.append("CHOOSE-Artificer")
    spellcasting.maxcantripsknown = 1
    spellcasting.spells[1] = "CHOOSE-Artificer"
    spellcasting.slots = [ 1 ]

    npc.proficiencies.append("Artisan's Tools")
    npc.spellcasting['Artificer Initiate'] = spellcasting    
```
