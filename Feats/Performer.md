## Performer
You master performance so that you can command any stage. You gain the following benefits:

* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency in the Performance skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* While performing, you can try to distract one humanoid you can see who can see and hear you. Make a Charisma (Performance) check contested by the humanoid's Wisdom (Insight) check. If your check succeeds, you grab the humanoid's attention enough that it makes Wisdom (Perception) and Intelligence (Investigation) checks with disadvantage until you stop performing.

```
name = 'Performer'
description = "***Feat: Performer.*** You master performance so that you can command any stage."
def prereq(npc): return True
def apply(npc):
    npc.CHA += 1

    npc.addskillorexpertise('Performance')

    npc.traits.append("***Performer.*** While performing, you can try to distract one humanoid you can see who can see and hear you. Make a Charisma (Performance) check contested by the humanoid's Wisdom (Insight) check. If your check succeeds, you grab the humanoid's attention enough that it makes Wisdom (Perception) and Intelligence (Investigation) checks with disadvantage until you stop performing.")
```

