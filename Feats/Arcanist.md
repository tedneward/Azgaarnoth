## Arcanist
You study the arcane arts, gaining the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the Arcana skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You learn the [prestidigitation](../Magic/Spells/prestidigitation.md) and [detect magic](../Magic/Spells/detect-magic.md) spells. You can cast [detect magic](../Magic/Spells/detect-magic.md) once without expending a spell slot, and you regain the ability to do so when you finish a long rest.

Note that if you choose to be a member of a [Mage School](../Organizations/MageSchools/index.md), your cantrip and 1st-level spell may vary, according to the DM.

```
name = 'Arcanist'
description = "***Feat: Arcanist.*** You study the arcane arts. (If you are a member of a mage school, your cantrip and spell may be different than these given.)"
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    npc.addskillorexpertise("Arcana")
    
    spellcasting = innatecaster(npc, 'CHA', name)
    spellcasting.cantripsknown.append('prestidigitation')
    spellcasting.perday[1] = ['detect magic']
```
