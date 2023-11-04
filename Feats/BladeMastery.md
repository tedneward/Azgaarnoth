## Blade Mastery
You master the shortsword, longsword, scimitar, rapier, and greatsword. You gain the following benefits when using any of them:

* You gain a +1 bonus to attack rolls you make with the weapon.
* On your turn, you can use your reaction to assume a parrying stance, provided you have the weapon in hand. Doing so grants a +1 bonus to your AC until the start of your next turn or until you're not holding the weapon.
* When you make an opportunity attack with the weapon, you have advantage on the attack roll.

```
name = 'Blade Mastery'
description = "***Feat: Blade Mastery.*** You master the shortsowrd, longsword, scimitar, rapier, and greatsword."
def prereq(npc): return True
def apply(npc):
    npc.actions.append("***TODO: Apply +1 to any attack rolls with shortsword, longsword, scimitar, rapier, and greatsword.")
    npc.reactions.append("***Blade Mastery: Parry.*** You can assume a parrying stance, provided you have the weapon in hand; doing so grants a +1 bonus to AC until the start of your next turn or until you're not holding the weapon.")
    npc.reactions.append("***Blade Mastery: Opportunity Attack.*** When you make an opportunity attack with a blade, you have advantage on the attack roll.")
```
