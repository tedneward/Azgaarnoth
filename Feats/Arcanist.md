## Arcanist
You study the arcane arts, gaining the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the Arcana skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You learn the [prestidigitation](../Magic/Spells/prestidigitation.md) and [detect magic](../Magic/Spells/detect-magic.md) spells. You can cast [detect magic](../Magic/Spells/detect-magic.md) once without expending a spell slot, and you regain the ability to do so when you finish a long rest.

Note that if you choose to be a member of a [Mage School](../Organizations/MageSchools/index.md), your cantrip and 1st-level spell may vary, according to the DM.

```
name = 'Arcanist'
description = "***Feat: Arcanist.*** You study the arcane arts."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1
    if "Arcana" in npc.skills:
        npc.traits.append("***Arcanist.*** You add twice your proficiency bonus to Intelligence (Arcana) checks.")
    else:
        npc.skills.append("Arcana")
    
    spellcasting = npc.newspellcasting('Arcanist', 'INT')
    spellcasting.cantripsknown.append('prestidigitation')
    spellcasting.spells[1].append('detect magic')
    spellcasting.slots = [ 1 ]
```
