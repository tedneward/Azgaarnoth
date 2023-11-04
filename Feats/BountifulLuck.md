## Bountiful Luck
*Prerequisite: Halfling*

Your people have extraordinary luck, which you have learned to mystically lend to your companions whenever you see them falter. You're not sure how you do it, you just wish it, and it happens. Surely a sign of fortune's favor!

When an ally you can see within 30 feet of you rolls a 1 on the d20 for an attack roll, an ability check, or a saving throw, you can use your reaction to let the ally reroll the die. The ally must use the new roll.

When you use this ability, you can't use your Lucky racial trait before the end of your next turn.

```
name = 'Bountiful Luck'
description = "***Feat: Bountiful Luck.*** Your people have extraordinary luck, which you have learned to mystically lend to your companions whenever you see them falter. You're not sure how you do it, you just wish it, and it happens. Surely a sign of fortune's favor!"
def prereq(npc): return True if npc.race.name == 'Halfling' else False
def apply(npc):
    npc.reactions.append("***Bountiful Luck.*** When an ally you can see within 30 feet of you rolls a 1 on the d20 for an attack roll, an ability check, or a saving throw, you can let the ally reroll the die. The ally must use the new roll. When you use this ability, you can't use your Lucky racial trait before the end of your next turn.")
```
