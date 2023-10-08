## Charger
When you use your action to Dash, you can use a bonus action to make one melee weapon attack or to shove a creature. If you move at least 10 feet in a straight line immediately before taking this bonus action, you either gain a +5 bonus to the attack's damage roll (if you chose to make a melee attack and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed).

```
name = 'Charger'
description = "***Feat: Charger.*** You learn to move fast."
def prereq(npc): return True
def apply(npc):
    npc.bonusactions.append("***Charger.*** When you use your action to Dash, you can make one melee weapon attack or shove a creature. If you move at least 10 feet in a straight line before taking the bonus action, you either gain a +5 bonus to the attack's damage roll (if you chose to make a melee attack and hit) or push the target up to 10 feet away from you (if you chose to shove and you succeed).")
```
