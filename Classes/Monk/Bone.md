# Monastic Tradition: Way of Bone
The Way of Bone teaches that the body and soul must be flexible and enduring, weathering the ravages of time and surviving whatever harrowing forces the universe deigns to lay in our path. Monks of this discipline have control over their bones, using them for both offense and defence.

```
name = 'Way of Bone'
description = "***Monastic Tradition: Way of Bone.*** The Way of Bone teaches that the body and soul must be flexible and enduring, weathering the ravages of time and surviving whatever harrowing forces the universe deigns to lay in our path. Monks of this discipline have control over their bones, using them for both offense and defence."
```

## Bone Shard
*3rd-level Way of Bone feature*

You learn to create lethal shards of bone with which to strike down your enemies. When you would draw a weapon, you can instead extrude an osseous shard from your body, which detaches into your grasp. This shard is treated as a dagger.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Bone Shard.*** When you would draw a weapon, you can instead extrude an osseous shard from your body, which detaches into your grasp. This shard is treated as a dagger.{ 'Your bone shards count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.' if npc.levels('Monk') > 5 else ''}") )
```

## Marrow Storm
*3rd-level Way of Bone feature*

Immediately after you take the Attack action on your turn, you can spend 1 ki point to make a number of thrown weapon strikes equal to your proficiency bonus as a bonus action. If you would make an attack using this feature and you have no weapon drawn, you may draw one reflexively for no cost.

```
    npc.defer(lambda npc: npc.actions.append(f"***Ki: Marrow Storm.*** Immediately after you take the Attack action on your turn, you can spend 1 ki point to make {npc.proficiencybonus()} thrown weapon strikes. (*Ranged Weapon Attack* +{npc.proficiencybonus() + npc.DEXbonus()} to hit, range 60, one target. Hit: 1d{npc.martialartsdie} + {npc.DEXbonus()} bludgeoning damage.{' This attack is considered magical for purposes of overcoming resistance and immunity to nonmagical attacks and damage.' if npc.levels('Monk') > 5 else ''}) If you would make an attack using this feature and you have no weapon drawn, you may draw one reflexively for no cost.") )
```

## Sharper shards
*6th-level Way of Bone feature*

Your bone shards count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage, and their damage is increased in line with the damage dealt by your unarmed strikes.

## Exoskeleton
*11th-level Way of Bone feature*

You can push your skeleton outside your body, forming a bony cage around your vulnerable insides. Your armor class increases to 19 unless it was already higher, and you are immune to critical hits. You can activate and end this effect as an action.

```
def level11(npc):
    npc.actions.append("***Exoskeleton.*** You can push your skeleton outside your body, forming a bony cage around your vulnerable insides. Your armor class increases to 19 unless it was already higher, and you are immune to critical hits.")
```

## Eternal Life
*17th-level Way of Bone feature*

You can rid yourself entirely of your flesh based vulnerabilities, investing your soul entirely in your skeleton. Your flesh and organs fall away from your body, and you gain the benefits of your exoskeleton permanently. In addition, you can no longer die of old age.

```
def level17(npc):
    npc.traits.append("***Eternal Life.*** You can rid yourself entirely of your flesh based vulnerabilities, investing your soul entirely in your skeleton. Your flesh and organs fall away from your body, and you gain the benefits of your Exoskeleton permanently. In addition, you can no longer die of old age.")
```
