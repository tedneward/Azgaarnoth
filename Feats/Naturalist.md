## Naturalist
Your extensive study of nature rewards you with the following benefits:

* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in the Nature skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You learn the [druidcraft](../Magic/Spells/druidcraft.md) and [detect poison and disease](../Magic/Spells/detect-poison-and-disease.md) spells. You can cast [detect poison and disease]() once without expending a spell slot, and you regain the ability to do so when you finish a long rest.

```
name = 'Naturalist'
description = "***Feat: Naturalist.*** You have made an extensive study of nature."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    npc.addskillorexpertise('Nature')

    spellcasting = innatecaster(npc, 'WIS', name)
    spellcasting.perday['atwill'] = ['druidcraft']
    spellcasting.perday[1] = ['detect poison and disease']
```

