## Theologian
Your extensive study of religion rewards you with the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the Religion skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You learn the [thaumaturgy](../Magic/Spells/thaumaturgy.md) and [detect evil and good](../Magic/Spells/detect-evil-and-good.md) spells. You can cast [detect evil and good](../Magic/Spells/detect-evil-and-good.md) once without expending a spell slot, and you regain the ability to do so when you finish a long rest.

```
name = 'Theologian'
description = "***Feat: Theologian.*** You have made an extensive study of religion."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    npc.addskillorexpertise('Religion')

    spellcasting = innatecaster(npc, 'INT', name)
    spellcasting.cantripsknown.append("thaumaturgy")
    spellcasting.perday[1] = [ "detect evil and good" ]
```
