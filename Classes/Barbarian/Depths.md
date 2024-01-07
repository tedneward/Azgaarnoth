# Primal Path: Path of the Depths
Encounters with the terrors of the deep can break the minds of the weak-willed, but some forge their trauma into weapons never seen above the waves. The barbarian who walks this path has survived such an encounter and has gained extraordinary abilities from the experience. These barbarians are always (almost without exception) of the *al'maera* of the [Al'Uma](../../Religions/AlUma.md), and are often sworn to destroy some enemy of the [Undersea](../../Geography/Undersea.md), most often the one that caused the trauma to the barbarian in the first place.

```
name = 'Depths'
description = "***Primal Path: Path of the Depths.*** Encounters with the terrors of the deep can break the minds of the weak-willed, but some forge their trauma into weapons never seen above the waves. The barbarian who walks this path has survived such an encounter and has gained extraordinary abilities from the experience."
```

## Gift of the Drowned Ones
*3rd-level Path of the Depths feature*

You gain a swimming speed equal to your walking speed and gain the ability to breathe underwater.

```
def level3(npc):
    npc.speed['swimming'] = npc.speed['walking']
    npc.traits.append(traits['amphibious'])
```

## Dredge Line
*3rd-level Path of the Depths feature*

You manifest an extra appendage when you enter your rage. This weapon can appear as a kraken tentacle, a giant anchor, preternatural jaws, or something else based on your history.

As a bonus action, you can use this appendage to strike at one creature of your choice that you can see within 15 feet. The target must succeed on a Strength saving throw (DC equal to 8 + your proficiency bonus + your Strength modifier) or be pulled up to 10 feet in a straight line towards you.

```
    npc.traits.append("***Dredge Line.*** You manifest an extra appendage when you enter your rage. This weapon can appear as a kraken tentacle, a giant anchor, preternatural jaws, or something else based on your history.")
    npc.defer(lambda npc: npc.bonusactions.append("***Dredge Line Attack.*** You use your Dredge Line appendage to attack. The target must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}) or be pulled up to 10 feet in a straight line towards you.") )
```

## Ghostwater Dive
*6th-level Path of the Depths feature*

You can burst into water then materialize somewhere else as an action. You magically teleport along with any equipment you are wearing or carrying, up to 30 feet to an unoccupied space you can see. Before or after teleporting, you can make one attack, as part of your action. Moving in this way does not provoke opportunity attacks.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Ghostwater Dive.*** You magically teleport along with any equipment you are wearing or carrying, up to 30 feet to an unoccupied space you can see. Before or after teleporting, you can make one attack, as part of your action. Moving in this way does not provoke opportunity attacks.{'' if npc.levels('Barbarian') < 14 else ' When you appear all creatures within 10 feet of you must make a Strength saving throw. On a failed save a creature takes 3d6 force damage and is knocked prone. On a successful save, a creature takes half damage and is not knocked prone.'}") )
```

## Manifestations of the Deep
*10th-level Path of the Depths feature*

You can manifest additional adaptations of the deep. Select one of the below adaptations you manifest, during a long rest you may replace your chosen manifestation with a new option from this list.

***Eyes of the Deep*** You gain the ability to use echolocation. When you do so, you cast the true seeing spell, without using a spell slot or material components. After you cast a spell in this way, you can't use this feature again until you finish a short or long rest.

***Arms of the Deep*** While raging, you now manifest two magical appendages, which may be tentacles, chains and anchors, animated rigging, or another grasping arm of your choice. When you use your dredge line ability, you can attempt a grapple with each of your appendages.

***Heart of the Deep*** Now on your turn, you can use a bonus action to gain temporary hit points equal to 1d12 + your barbarian level. Once you use this feature, you must finish a short or long rest before you can use it again.

***Soul of the Deep*** You are now immune to all effects that would cause you to be charmed or frightened.

***Armor of the Deep*** Your skin hardens increasing your Armor Class by 1.

```
def level10(npc):
    npc.traits.append("***Manifestations of the Deep.*** Select one of the below adaptations you manifest: **Eyes of the Deep.** You gain the ability to use echolocation. When you do so, you cast the true seeing spell, without using a spell slot or material components. After you cast a spell in this way, you can't use this feature again until you finish a short or long rest. **Arms of the Deep.** While raging, you now manifest two magical appendages, which may be tentacles, chains and anchors, animated rigging, or another grasping arm of your choice. When you use your dredge line ability, you can attempt a grapple with each of your appendages. **Heart of the Deep.** Now on your turn, you can use a bonus action to gain temporary hit points equal to 1d12 + your barbarian level. Once you use this feature, you must finish a short or long rest before you can use it again. **Soul of the Deep** You are now immune to all effects that would cause you to be charmed or frightened.**Armor of the Deep** Your skin hardens increasing your Armor Class by 1.")
```

## Depth Charge
*14th-level Path of the Depths feature*

When you use your Ghostwater Dive ability, you can choose to appear with a wave of tidal force. When you appear all creatures within 10 feet of you must make a Strength saving throw. On a failed save a creature takes 3d6 force damage and is knocked prone. On a successful save, a creature takes half damage and is not knocked prone.
