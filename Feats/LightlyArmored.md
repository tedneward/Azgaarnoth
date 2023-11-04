## Lightly Armored
You have trained to master the use of light armor, gaining the following benefits.

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* You gain proficiency with light armor.

```
name = 'Lightly Armored'
description = "***Feat: Lightly Armored.*** You have trained to master the use of light armor."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR','DEX'])

    for arm in armor['light']:
        npc.proficiencies.append(arm)
```

