## Fell Handed
You master the handaxe, battleaxe, greataxe, warhammer, and maul. You gain the following benefits when using any of them:

* You gain a +1 bonus to attack rolls you make with the weapon.
* Whenever you have advantage on a melee attack roll you make with the weapon and hit, you can also knock the target prone if the lower of the two d20 rolls would also hit the target.
* Whenever you have disadvantage on a melee attack roll you make with the weapon, the target takes bludgeoning damage equal to your Strength modifier (minimum of 0) if the attack misses but the higher of the two d20 rolls would have hit.
* If you use the Help action to aid an ally's melee attack while you're wielding the weapon, you knock the target's shield aside momentarily. In addition to the ally gaining advantage on the attack roll, the ally gains a +2 bonus to the roll if the target is using a shield

```
name = 'Fell Handed'
description = "***Feat: Fell Handed.*** You master the handaxe, battleaxe, greataxe, warhammer, and maul."
def prereq(npc): return True
def apply(npc):
    npc.actions.append("***Fell Handed.*** You gain a +1 attack bonus to attack rolls you make with handaxe, battleaxe, greataxe, warhammer, or maul. Whenever you have advantage on a melee attack roll you make with one of these weapons and hit, you can also knock the target prone if the lower of the two d20 rolls would also hit the target. Whenever you have disadvantage on a melee attack roll you make with one of these weapons, the target takes bludgeoning damage equal to your Strength modifier (minimum of 0) if the attack misses but the higher of the two d20 rolls would have hit.")
    npc.actions.append("***Fell Help.*** If you use the Help action to aid an ally's melee attack while you're wielding a handaxe, battleaxe, greataxe, warhammer, or maul, you knock the target's shield aside momentarily. In addition to the ally gaining advantage on the attack roll, the ally gains a +2 bonus to the roll if the target is using a shield.")
```
