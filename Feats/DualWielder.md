## Dual Wielder
You master fighting with two weapons, gaining the following benefits:

* You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand.
* You can use two-weapon fighting even when the one handed melee weapons you are wielding aren't light.
* You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one.

```
name = 'Dual Wielder'
description = "***Feat: Dual Wielder.*** You have mastered fighting with two weapons."
def prereq(npc): return True
def apply(npc):
    npc.armorclass['Dual wielder'] = 1
    npc.traits.append("***Dual Wielder.*** You gain a +1 bonus to AC while you are wielding a separate melee weapon in each hand. You can use two-weapon fighting even when the one handed melee weapons you are wielding aren't light. You can draw or stow two one-handed weapons when you would normally be able to draw or stow only one.")
```
