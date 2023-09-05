### Bloodline of Asmodeus
The tieflings connected to Nessus command the power of fire and darkness, guided by a keener than normal intellect, as befits those linked to Asmodeus himself.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Infernal Legacy** You know the Thaumaturgy cantrip. Once you reach 3rd level, you can cast the Hellish Rebuke spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Darkness spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Asmodeus'
def level0(npc):
    npc.description.append("**Bloodline of Asmodeus.** The tieflings connected to Nessus command the power of fire and darkness, guided by a keener than normal intellect, as befits those linked to Asmodeus himself.")

    npc.INT += 1
    npc.cantripsknown.append('thaumaturgy')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('hellish rebuke') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('hellish rebuke')} as a 2nd-level spell or {spelllinkify('darkness')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
