## Perceptive
You hone your senses until they become razor sharp. You gain the following benefits:

* Increase your Wisdom score by 1, to a maximum of 20.
* You gain proficiency in the Perception skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* Being in a lightly obscured area doesn't impose disadvantage on your Wisdom (Perception) checks if you can both see and hear.

```
name = 'Perceptive'
description = "***Feat: Perceptive.*** You hone your senses until they become razor sharp."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    npc.addskillorexpertise('Perception')

    npc.traits.append("***Perceptive.*** Being in a lightly obscured area doesn't impose disadvantage on your Wisdom (Perception) checks if you can both see and hear.")
```

