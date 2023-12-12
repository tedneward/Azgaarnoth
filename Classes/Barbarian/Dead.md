# Primal Path: Path of the Dead
Barbarians who walk the Path of Death tread the forbidden road that straddles the lands of the living and the dead. Warriors who walk this path gain strange and unnerving abilities, and are found more commonly in societies near Shadow Crossings, where the need for those who can calm the unquiet dead is great indeed.

```
name = 'Dead'
description = "***Primal Path: Path of the Dead.*** Barbarians who walk the Path of Death tread the forbidden road that straddles the lands of the living and the dead. Warriors who walk this path gain strange and unnerving abilities, and are found more commonly in societies near Shadow Crossings, where the need for those who can calm the unquiet dead is great indeed."
```

## The Boundary
*3rd-level Path of the Dead feature*

Your Rage opens your eyes to the world of the dead. Your eyes gain a supernatural aspect of your choice whilst raging, and you can see or interact with immaterial spirits as if they were on the material plane. For the duration of your rage, your attacks count as magical for the purposes of damaging undead creatures.

Whilst in this state, you are semi-immaterial, and can pass through material objects using your movement at a rate of 1 foot for every 5 feet of movement expended (though you may not end your movement inside an object - if you do so, you are ejected and take 4d10 force damage).

```
def level3(npc):
    npc.traits.append("***The Boundary.*** For the duration of your rage, your attacks count as magical for the purposes of damaging undead creatures. Whilst in this state, you are semi-immaterial, and can pass through material objects using your movement at a rate of 1 foot for every 5 feet of movement expended (though you may not end your movement inside an object - if you do so, you are ejected and take 4d10 force damage).")
```

## Army of the Fallen
*6th-level Path of the Dead feature*

You shine like a beacon in the afterlife and your slain enemies rise again to fight under your banner. When you slay a Medium or smaller living creature whilst raging, that creature rises as a [Zombie](../../Creatures/Undead/Zombie.md) or a [Skeleton](../../Creatures/Undead/Skeletons.md#skeleton) under your control on initiative count 20 of the next round. The assembled dead act on your turn, and attack the nearest hostile creature.

There is no limit to the number of undead you can create in this way, but when your rage ends, any undead raised by this ability become corpses once more.

```
def level6(npc):
    npc.traits.append("***Army of the Fallen.*** When you slay a medium or smaller living creature whilst raging, that creature rises as a zombie or a skeleton under your control on initiative count 20 of the next round. The assembled dead act on your turn, and attack the nearest hostile creature.There is no limit to the number of undead you can creature in this way, but when your rage ends, any undead raised by this ability become corpses once more.")
```

## The Halls of my Ancestors
*10th-level Path of the Dead feature*

You can enter a trance in order to speak to the dead who would not otherwise deign to answer the call. You can cast speak with dead as a ritual, but you are not restricted to creatures that have died within the last 10 days.

```
def level10(npc):
    npc.traits.append(f"***The Halls of My Ancestors.*** You can cast {spelllinkify('speak with dead')} as a ritual, but you are not restricted to creatures that have died within the last 10 days.")
```

## Eternal Rest
*14th-level Path of the Dead feature*

Your attacks can rend the very souls of the creatures you strike, sending the dead howling back to oblivion, and the living to eternal rest. 

When you reduce a creature to 0 hit points whilst raging, you can choose to send that creature to Eternal Rest. Any creature sent to Eternal Rest dies instantly, and cannot be raised from the dead, reincarnated, or contacted after death by any means. Additionally, the creature cannot return as a ghost, and their body cannot be animated as a corporeal undead.

```
def level14(npc):
    npc.traits.append("***Eternal Rest.*** When you reduce a creature to 0 hit points whilst raging, you can choose to send that creature to Eternal Rest. Any creature sent to Eternal Rest dies instantly, and cannot be raised from the dead, reincarnated, or contacted after death by any means. Additionally, the creature cannot return as a ghost, and their body cannot be animated as a corporeal undead.")
```
