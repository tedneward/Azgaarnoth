# Roguish Archetype: Swashbuckler
You focus your training on the art of the blade, relying on speed, elegance, and charisma in equal parts. While other warriors are  brutes clad in heavy armor, your method of fighting looks more like performance. A swashbuckler excels in single combat, and can fight with two weapons while safely darting away from an opponent. Swashbucklers are especially talented at making difficult maneuvers to escape enemies or attack from an unexpected direction.

Swashbucklers are frequently found in the [dueling colleges](../../Organizations/DuelingColleges.md), either competing or practicing when they're not out engaging in other more roguish activities. (They are rogues, after all.) Many swashbucklers also find themselves employed as guards at sea for the various [Merchant Guilds](../../Organizations/MerchantGuilds/MerchantGuilds.md). A great number of the [Sea Reavers](../../Organizations/MercCompanies/SeaReavers.md) are of this archetype, as well.

```
name = 'Swashbuckler'
description = "***Roguish Archetype: Swashbuckler.*** You focus your training on the art of the blade, relying on speed, elegance, and charisma in equal parts. While other warriors are  brutes clad in heavy armor, your method of fighting looks more like performance. A swashbuckler excels in single combat, and can fight with two weapons while safely darting away from an opponent. Swashbucklers are especially talented at making difficult maneuvers to escape enemies or attack from an unexpected direction."
```

## Fancy Footwork
*3rd-level Swashbuckler feature*

You are a continuous blur of motion in battle as you dart in, attack, and slip away to safety. During your turn, if you make a melee attack against a creature, that creature cannot make opportunity attacks against you for the rest of your turn.

```
def level3(npc):
    npc.traits.append("***Fancy Footwork.*** During your turn, if you make a melee attack against a creature, that creature cannot make opportunity attacks against you for the rest of your turn.")
```

## *Toujours l'Audace*
*3rd-level Swashbuckler feature*

Your unmistakable confidence propels you into battle. You add your Charisma modifier to your initiative rolls. In addition, you can use Sneak Attack with any melee attack made against a target that has none of your allies adjacent to it.

```
    npc.traits.append("***Always Audacious.*** You add your Charisma modifier to your initiative rolls.")
```

## Panache
*9th-level Swashbuckler feature*

Your charm becomes as sharp and dangerous as your blade. As an action, you can make a Charisma (Persuasion) check contested by a creature's Wisdom (Insight) check. The creature must be able to hear you, and the two of you must share a language.

If you succeed on the check and the creature is hostile, it must target you with any attacks it makes and cannot willingly move farther away from you. This effect lasts for 1 minute or until you move more than 60 feet away from the target.

If you succeed on the check and the creature is not hostile, it is charmed by you for 1 minute. While charmed, it regards you as a friendly acquaintance.

```
def level9(npc):
    npc.actions.append("***Panache.*** You can make a Charisma (Persuasion) check contested by a creature's Wisdom (Insight) check. The creature must be able to hear you, and the two of you must share a language. If you succeed on the check and the creature is hostile, it must target you with any attacks it makes and cannot willingly move farther away from you. This effect lasts for 1 minute or until you move more than 60 feet away from the target. If you succeed on the check and the creature is not hostile, it is charmed by you for 1 minute. While charmed, it regards you as a friendly acquaintance.")
```

## Elegant Maneuver
*13th-level Swashbuckler feature*

You complete difficult maneuvers with practiced ease. You can use a bonus action to gain advantage on the next Dexterity (Acrobatics) or Strength (Athletics) check you make on your turn.

```
def level13(npc):
    npc.bonusactions.append("***Elegant Maneuver.*** You gain advantage on the next Dexterity (Acrobatics) or Strength (Athletics) check you make on your turn.")
```

## Master Duelist
*17th-level Swashbuckler feature*

Your mastery of the blade lets you turn failure to success in combat. If you miss with an attack, you can choose to roll the attack again with advantage. Once you use this ability, you cannot use it again until you finish a short or long rest.

```
def level17(npc):
    npc.actions.append("***Master Duelist (Recharges on short or long rest).*** If you miss with an attack, you can choose to roll the attack again with advantage.")
```
