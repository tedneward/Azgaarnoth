## Outlands Envoy
*Prerequisite: 4th Level, [Scion of the Outer Planes Feat](ScionoftheOuterPlanes.md)*

You have spent significant time in Sigil or elsewhere in the Outlands, the crossroads of the multiverse. Being steeped in converging planar energies grants you these benefits:

* **Ability Score Increase.** Increase an ability score of your choice by 1, to a maximum of 20.

* **Crossroads Emissary.** You learn the [Misty Step](../Magic/Spells/misty-step.md) and [Tongues](../Magic/Spells/tongues.md) spells. You can cast each spell once using this feat without a spell slot, and you must finish a long rest before you can cast that spell in this way again. When you cast tongues using this feat, you require no material components. You can also cast these spells using spell slots you have of the appropriate level. The spell’s spellcasting ability is the one chosen when you gained the Scion of the Outer Planes feat.

```
name = 'Outlands Envoy'
description = "***Feat: Outlands Envoy.*** You have spent significant time in Sigil or elsewhere in the Outlands, the crossroads of the multiverse."
def prereq(npc):
    if npc.levels() < 4: return False
    if "Scion of the Outer Planes" not in npc.feats: return False
    return True

def apply(npc):
    chooseability(npc)
    npc.spellcasting['Scion'].spellsalwaysprepared.append("misty step")
    npc.spellcasting['Scion'].spellsalwaysprepared.append("tongues")
```
