## Quick-Fingered
Your nimble fingers and agility let you perform sleight of hand. You gain the following benefits:

* Increase your Dexterity score by 1, to a maximum of 20.
* You gain proficiency in the Sleight of Hand skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* As a bonus action, you can make a Dexterity (Sleight of Hand) check to plant something on someone else, conceal an object on a creature, lift a purse, or take something from a pocket, even in the middle of combat.

```
name = 'Quick-Fingered'
description = "***Feat: Quick-Fingered.*** Your nimble fingers and agility let you perform sleight of hand."
def prereq(npc): return True
def apply(npc):
    npc.DEX += 1
    npc.addskillorexpertise('Sleight of Hand')
    npc.bonusactions.append("***Quick Fingers.*** You can make a Dexterity (Sleight of Hand) check to plant something on someone else, conceal an object on a creature, lift a purse, or take something from a pocket, even in the middle of combat.")
```
