## Gourmand
You have mastered a variety of special recipes, allowing you to prepare exotic dishes with useful effects. You gain the following benefits:

* Increase your Constitution score by 1, to a maximum of 20.
* You gain proficiency with cook's utensils. If you are already proficient with them, you add double your proficiency bonus to checks you make with them.
* As an action, you can inspect a drink or plate of food within 5 feet of you and determine whether it is poisoned, provided that you can see and smell it.
* During a long rest, you can prepare and serve a meal that helps you and your allies recover from the rigors of adventuring, provided you have suitable food, cook's utensils, and other supplies on hand. The meal serves up to six people, and each person who eats it regains two additional Hit Dice at the end of the long rest. In addition, those who partake of the meal have advantage on Constitution saving throws against disease for the next 24 hours.

```
name = 'Gourmand'
description = "***Feat: Gourmand.*** You have mastered a variety of special recipes, allowing you to prepare exotic dishes with useful effects."
def prereq(npc): return True
def apply(npc):
    npc.CON += 1

    npc.addskillorexpertise("Cook's utensils")
    
    npc.actions.append("***Gourmand: Inspect.*** You inspect a drink or plate of food within 5 feet of you and determine whether it is poisoned, provided that you can see and smell it.")

    npc.traits.append("***Gourmand: Serve.*** During a long rest, you can prepare and serve a meal that helps you and your allies recover from the rigors of adventuring, provided you have suitable food, cook's utensils, and other supplies on hand. The meal serves up to six people, and each person who eats it regains two additional Hit Dice at the end of the long rest. In addition, those who partake of the meal have advantage on Constitution saving throws against disease for the next 24 hours.")
```
