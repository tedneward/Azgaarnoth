## Chef
Time and effort spent mastering the culinary arts has paid off. You gain the following benefits:

* Increase your Constitution or Wisdom score by 1, to a maximum of 20.
* You gain proficiency with cook's utensils if you don't already have it.
* As part of a short rest, you can cook special food, provided you have ingredients and cook's utensils on hand. You can prepare enough of this food for a number of creatures equal to 4 + your proficiency bonus. At the end of the short rest, any creature who eats the food and spends one or more Hit Dice to regain hit points regains an extra 1d8 hit points.
* With one hour of work or when you finish a long rest, you can cook a number of treats equal to your proficiency bonus. These special treats last 8 hours after being made. A creature can use a bonus action to eat one of those treats to gain temporary hit points equal to your proficiency bonus.

```
name = 'Chef'
description = "***Feat: Chef.*** Time and effort spent mastering the culinary arts has paid off."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['CON', 'WIS'])

    npc.proficiencies.append("Cook's utensils")

    npc.defer(lambda npc: npc.traits.append(f"***Chef: Short rest.*** You can cook special food, provided you have ingredients and cook's utensils on hand. You can prepare enough of this food for {4 + npc.proficiencybonus()} creatures. At the end of the short rest, any creature who eats the food and spends one or more Hit Dice to regain hit points regains an extra 1d8 hit points.") )
    
    npc.defer(lambda npc: npc.traits.append(f"***Chef: Long rest.*** With one hour of work or when you finish a long rest, you can cook {npc.proficiencybonus()} treats. These special treats last 8 hours after being made. Any creature eating one of those treats (using a bonus action) gains {npc.proficiencybonus()} temporary hit points.") )
```
