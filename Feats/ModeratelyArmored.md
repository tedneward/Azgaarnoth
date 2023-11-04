## Moderately Armored
*Prerequisite: Proficiency with light armor*

You have trained to master the use of medium armor and shields, gaining the following benefits:

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* You gain proficiency with medium armor and shields.

```
name = 'Moderately Armored'
description = "***Feat: Moderately Armored.*** You have trained to master the use of medium armor and shields."
def prereq(npc): 
    if 'Padded armor' in npc.proficiencies or 'Leather armor' in npc.proficiencies or 'Studded leather armor' in npc.proficiencies:
        return True
    else:
        return False

def apply(npc):
    chooseability(npc, ['STR', 'DEX'])

    for arm in armor['medium'] | armor['shields']:
        npc.proficiencies.append(arm)
```

