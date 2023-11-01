## Divinely Favored
A god has chosen you to carry a spark of their divine power.

You learn the [thaumaturgy](../Magic/Spells/thaumaturgy.md) cantrip and one 1st-level spell based on the alignment of your character, as specified in the below table:

Alignment	| 1st-level Spells
--------- | --------------
Evil | Choose one 1st-level Warlock or Wizard spell.
Good | Choose one 1st-level Cleric or Wizard spell.
Neutral | Choose one 1st-level Druid or Wizard spell.

You can cast the chosen 1st-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have.

Your spellcasting ability for this feat's spells is Intelligence, Wisdom, or Charisma (choose when you select this feat).

In addition, you can use a holy symbol as a spellcasting focus for any spell you cast that uses the spellcasting ability you choose when you select this feat.

```
name = 'Divinely Favored'
description = "***Feat: Divinely Favored.*** A god has chosen you to carry a spark of their divine power."
def prereq(npc): return True
def apply(npc):
    spellclass = choose("Choose your spell type: ", ['Cleric', 'Druid', 'Warlock', 'Wizard'])
    npc.divinefavor = choose("Choose your attribute: ", ['INT', 'WIS', 'CHA'])
    spellcasting = innatecaster(npc, npc.divinefavor, name)
    spellcasting.cantripsknown = [ 'thaumaturgy' ]
    spellcasting.casterclass = spellclass
    spellcasting.perday[1] = [ f'CHOOSE-{spellclass}-1st' ]

    npc.traits.append(f"***Divine Favor.*** You can use a holy symbol as a spellcasting focus for any spell you cast that uses {npc.divinefavor}.")
```
