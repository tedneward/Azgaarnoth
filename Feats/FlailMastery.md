## Flail Mastery
The flail is a tricky weapon to use, but you have spent countless hours mastering it. You gain the following benefits:

* You gain a +1 bonus to attack rolls you make with a flail.
* As a bonus action on your turn, you can prepare yourself to extend your flail to sweep over targets' shields. Until the end of this turn, your attack rolls with a flail gain a +2 bonus against any target using a shield.
* When you hit with an opportunity attack using a flail, the target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + your Strength modifier) or be knocked prone.

```
name = 'Flail Mastery'
description = "***Feat: Flail Mastery.*** The flail is a tricky weapon to use, but you have spent countless hours mastering it."
def prereq(npc): return True
def apply(npc):
    npc.actions.append("***Flail Mastery.*** You gain a +1 bonus to attack rolls you make with a flail.")

    npc.bonusactions.append("***Flail Mastery.*** You prepare yourself to extend your flail to sweep over targets' shields. Until the end of this turn, your attack rolls with a flail gain a +2 bonus against any target using a shield.")

    npc.defer(lambda npc: npc.actions.append(f"***FLail Mastery.*** When you hit with an opportunity attack using a flail, the target must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}) or be knocked prone.") )
```
