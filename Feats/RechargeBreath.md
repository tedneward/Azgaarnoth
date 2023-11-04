## Recharge Breath
*Prerequisite: must have a breath weapon*

After you use your innate breath weapon, you may roll a d6 at the beginning of each of your turns. On a 6, your breath weapon is recharged. If your breath already recharges on a 6, it instead recharges on a 5 or a 6. You may take this feat up to two times, but the recharge cannot go below 5.

```
name = 'Recharge Breath'
description = "***Feat: Recharge Breath.*** You have learned more stamina with your breath weapon."
def prereq(npc):
    for act in npc.actions:
        if act[0:len("***Breath Weapon")] == '***Breath Weapon':
            return True
    return False
def apply(npc):
    if 'Recharge Breath' in npc.feats:
        npc.actions.append("***Breath Weapon Recharge.*** After you use your innate breath weapon, you may roll a d6 at the beginning of each of your turns. On a 5 or 6, your breath weapon is recharged.")
    else:
        npc.actions.append("***Breath Weapon Recharge.*** After you use your innate breath weapon, you may roll a d6 at the beginning of each of your turns. On a 6, your breath weapon is recharged. If your breath already recharges on a 6, it instead recharges on a 5 or a 6. You may take this feat up to two times, but the recharge cannot go below 5.")
```
