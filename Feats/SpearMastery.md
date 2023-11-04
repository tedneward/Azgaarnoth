## Spear Mastery
Though the spear is a simple weapon to learn, it rewards you for the time you have taken to master it. You gain the following benefits:

* You gain a +1 bonus to attack rolls you make with a spear.
* When you use a spear, its damage die changes from a d6 to a d8, and from a d8 to a d10 when wielded with two hands. (This benefit has no effect if another feature has already improved the weapon's die.)
* You can set your spear to receive a charge. As a bonus action, choose a creature you can see that is at least 20 feet away from you. If that creatures moves within your spear's reach on its next turn, you can make a melee attack against it with your spear as a reaction. If the attack hits, the target takes an extra 1d8 piercing damage, or an extra 1d10 piercing damage if you wield the spear with two hands. You can't use this ability if the creature used the Disengage action before moving.
* As a bonus action on your turn, you can increase your reach with a spear by 5 feet for the rest of your turn.

```
name = 'Spear Mastery'
description = "***Feat: Spear Mastery.*** Though the spear is a simple weapon to learn, it rewards you for the time you have taken to master it."
def prereq(npc): return True
def apply(npc):
    npc.actions.append("***TODO: Spear attack gains +1 bonus. Damage die changes from d6 to d8 (one-handed) or d8 to d10 (two-handed).")
    npc.bonusactions.append("***Spear Mastery: Receive Charge.*** Choose a creature you can see that is at least 20 feet away from you. If that creatures moves within your spear's reach on its next turn, you can make a melee attack against it with your spear as a reaction. If the attack hits, the target takes an extra 1d8 piercing damage, or an extra 1d10 piercing damage if you wield the spear with two hands. You can't use this ability if the creature used the Disengage action before moving.")
    npc.bonusactions.append("***Spear Mastery: Increase Reach.*** You can increase your reach with a spear by 5 feet for the rest of your turn.")
```
