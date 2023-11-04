## Flyby
*Prerequisite: Aerial mounted combat, or some form of flight*

You have learned how to attack while moving swiftly through the air. As a result, if you move and attack a creature, you may use Disengage as a bonus action to avoid a reaction melee attack from the target.

```
name = 'Flyby'
description = "***Feat: Flyby.*** You have learned how to attack while moving swiftly through the air."
def prereq(npc): return True
def apply(npc):
    npc.bonusactions.append("***Flyby.*** You use Disengage and avoid a reaction melee attack from the target.")
```
