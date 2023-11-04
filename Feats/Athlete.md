## Athlete
You have undergone extensive physical training to gain the following benefits:

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* When you are prone, standing up uses only 5 feet of your movement.
* Climbing doesn't cost you extra movement.
* You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet.

```
name = 'Athlete'
description = "***Feat: Athlete.*** You have undergone extensive physical training."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR', 'DEX'])

    npc.speed['climbing'] = npc.speed['walking']
    npc.traits.append("***Athletic.*** When you are prone, standing up uses only 5 feet of your movement. You can make a running long jump or a running high jump after moving only 5 feet on foot, rather than 10 feet.")
```
