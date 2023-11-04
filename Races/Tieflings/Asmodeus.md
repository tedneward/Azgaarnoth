### Bloodline of Asmodeus
The tieflings connected to Nessus command the power of fire and darkness, guided by a keener than normal intellect, as befits those linked to Asmodeus himself.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Infernal Legacy** You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Asmodeus'
description = "***Bloodline of Asmodeus.*** The tieflings connected to Nessus command the power of fire and darkness, guided by a keener than normal intellect, as befits those linked to Asmodeus himself."
def level0(npc):
    npc.INT += 1
    spellcasting = innatecaster(npc, 'INT', "Asmodeus Tiefling")
    spellcasting.cantripsknown.append("thaumaturgy")

def level3(npc):
    npc.spellcasting['Asmodeus Tiefling'].preday[1] = []
    npc.spellcasting['Asmodeus Tiefling'].preday[1].append('hellish rebuke')

def level5(npc):
    npc.spellcasting['Asmodeus Tiefling'].preday[1].append('darkness')
```
