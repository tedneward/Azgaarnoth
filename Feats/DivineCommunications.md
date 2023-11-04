## Divine Communications
*Prerequisite: 4th Level, [Divinely Favored Feat](#divinely-favored)*

Your connection to your god deepens, granting you these benefits:

* **Ability Score Increase**. Increase the ability score of the spellcasting ability chosen when you gained the Divinely Favored feat by 1, to a maximum of 20.
* **Celestial Tongues**. You learn to speak, read, and write Celestial, and two other languages of your choice.
* **Divine Omens**. You can cast the [augury](../Magic/Spells/augury.md) and [commune](../Magic/Spells/commune.md) spell without a spell slot, and you must finish 1d4 long rests before you can cast it in this way again. You can also cast the spell using spell slots you have of the appropriate level. The spell's spellcasting ability is the one chosen when you gained the Divinely Favored feat.

```
name = 'Divine Communications'
description = "***Feat: Divine Communications.*** You connection to your god deepens."
def prereq(npc):
    return npc.levels() >= 4 and "Divinely Favored" in npc.feats
def apply(npc):
    if npc.divinefavor == 'INT': npc.INT += 1
    elif npc.divinefavor == 'WIS': npc.WIS += 1
    elif npc.divinefavor == 'CHA': npc.CHA += 1
    else: error(f"WTF?!? Unrecognized divine favor: {npc.divinefavor}")

    npc.languages.append("Celestial")
    npc.languages.append("CHOOSE")
    npc.langauges.apoend("CHOOSE")

    spellcasting = npc.spellcasting['Divinely Favored']
    spellcasting.spellsknown.append('augury')
    spellcasting.spellsknown.append('commune')
```
