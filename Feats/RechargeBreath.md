## Recharge Breath
*Prerequisite: must have a breath weapon*

After you use your innate breath weapon, you may roll a d6 at the beginning of each of your turns. On a 6, your breath weapon is recharged. If your breath already recharges on a 6, it instead recharges on a 5 or a 6. You may take this feat up to two times, but the recharge cannot go below 5.

```
name = 'Recharge Breath'
description = "***Feat: Recharge Breath.*** You have learned more stamina with your breath weapon."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Recharge Breath.*** After you use your innate breath weapon, you may roll a d6 at the beginning of each of your turns. On a 6, your breath weapon is recharged. If your breath already recharges on a 6, it instead recharges on a 5 or a 6. You may take this feat up to two times, but the recharge cannot go below 5.")

#    def breathweaponenhance(npc):
#        for it in npc.actions:
#            if it[0:len("***Breath Weapon")] == "***Breath Weapon":
#    npc.defer(lambda npc: )
```
