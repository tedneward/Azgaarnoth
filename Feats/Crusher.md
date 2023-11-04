## Crusher
You are practiced in the art of crushing your enemies, granting you the following benefits:

* Increase your Strength or Dexterity by 1, to a maximum of 20.
* Once per turn, when you hit a creature with an attack that deals bludgeoning damage, you can move it 5 feet to an unoccupied space, provided the target is no more than one size larger than you.
* When you score a critical hit that deals bludgeoning damage to a creature, attack rolls against that creature are made with advantage until the end of your next turn.

```
name = 'Crusher'
description = "***Feat: Crusher.*** You are practiced in the art of crushing your enemies."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR', 'DEX'])

    npc.traits.append("***Crusher.*** Once per turn, when you hit a creature with an attack that deals bludgeoning damage, you can move it 5 feet to an unoccupied space, provided the target is no more than one size larger than you.")
    npc.traits.append("***Crusher.*** When you score a critical hit that deals bludgeoning damage to a creature, attack rolls against that creature are made with advantage until the end of your next turn.")
```

