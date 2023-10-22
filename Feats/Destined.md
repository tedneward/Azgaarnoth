## Destined
*Prerequisite: must have backstory elements and DM's approval to take this feat*

You are part of a tapestry of purpose beyond your reckoning, and you are destined for great things, not to be stymied by the whims of luck or karma. You know that you will leave a mark on the story that unfolds around you, and perhaps even on the world.

You gain the following benefits:

* You increase one ability score of your choice by 1.
* Choose two backgrounds that are different than the one you started with. You gain those backgrounds' features in addition to your original background feature. This does not grant you additional proficiencies or equipment.
* You have 3 destiny points. When you make an ability check and see the total but before you know the result of the check, you can spend 1 Destiny Point to change the number you rolled on the d20 to 15. You cannot use this to alter a check that affects a spell (such as for telekinesis or counterspell), a check that affects a grapple, or a Concentration check.
* You regain all expended Destiny Points when you finish a long rest.

```
name = 'Destined'
description = "***Feat: Destined.*** You are part of a tapestry of purpose beyond your reckoning, and you are destined for great things, not to be stymied by the whims of luck or karma. You know that you will leave a mark on the story that unfolds around you, and perhaps even on the world."
def prereq(npc): return True
def apply(npc):
    chooseability(npc)

    npc.traits.append("***Destined.*** Choose two backgrounds that are different than the one you started with. You gain those backgrounds' features in addition to your original background feature. This does not grant you additional proficiencies or equipment.")
    npc.traits.append("***Destiny Points (Recharges on long rest).*** You have 3 destiny points. When you make an ability check and see the total but before you know the result of the check, you can spend 1 Destiny Point to change the number you rolled on the d20 to 15. You cannot use this to alter a check that affects a spell, a check that affects a grapple, or a Concentration check.")
```
