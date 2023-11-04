## Survivalist
You master wilderness lore, gaining the following benefits:

* Increase your Wisdom score by 1, to a maximum of 20.
* You gain proficiency in the Survival skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You learn the [alarm]() spell. You can cast it once without expending a spell slot, and you regain the ability to do so when you finish a long rest.

```
name = 'Survivalist'
description = "***Feat: Survivalist.*** You master wildnerness lore."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1
    npc.addskillorexpertise('Survival')
    spellcasting = innatecaster(npc, 'WIS', name)
    spellcasting.perday[1] = [ "alarm" ]
```
