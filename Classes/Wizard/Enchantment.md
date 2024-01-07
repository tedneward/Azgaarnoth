# Arcane Tradition: School of Enchantment
As a member of the School of Enchantment, you have honed your ability to magically entrance and beguile other people and monsters. Some enchanters are peacemakers who bewitch the violent to lay down their arms and charm the cruel into showing mercy. Others are tyrants who magically bind the unwilling into their service. Most enchanters fall somewhere in between.

Enchanters are widely distrusted all across Azgaarnoth, and are the only major arcane tradition that do not have their own [Mage School](../../Organizations/MageSchools/index.md) focusing on that tradition. However, enchanters are stil quite common in other schools; many, for example, find themselves quietly welcome amongst the [MindMage](../../Organizations/MageSchools/MindMage.md) school, and many more are welcome to use their talents on behalf of the [Dread Emperor](../../People/DreadEmperor.md).

```
name = 'Enchantment'
description = "***Arcane Tradition: School of Enchantment.*** As a member of the School of Enchantment, you have honed your ability to magically entrance and beguile other people and monsters. Some enchanters are peacemakers who bewitch the violent to lay down their arms and charm the cruel into showing mercy. Others are tyrants who magically bind the unwilling into their service. Most enchanters fall somewhere in between."
```

## Enchantment Savant
*2nd-level Enchantment feature*

The gold and time you must spend to copy a Enchantment spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Enchantment Savant.*** The gold and time you must spend to copy an Enchantment spell into your spellbook is halved.")
```

## Hypnotic Gaze
*2nd-level Enchantment feature*

Your soft words and enchanting gaze can magically enthrall another creature. As an action, choose one creature that you can see within 5 feet of you. If the target can see or hear you, it must succeed on a Wisdom saving throw against your wizard spell save DC or be charmed by you until the end of your next turn. The charmed creature's speed drops to 0, and the creature is incapacitated and visibly dazed.

On subsequent turns, you can use your action to maintain this effect, extending its duration until the end of your next turn. However, the effect ends if you move more than 5 feet away from the creature, if the creature can neither see nor hear you, or if the creature takes damage.

Once the effect ends, or if the creature succeeds on its initial saving throw against this effect, you can't use this feature on that creature again until you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Hypnotic Gaze.*** Choose one creature that you can see within 5 feet of you. If the target can see or hear you, it must succeed on a Wisdom saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}) or be charmed by you until the end of your next turn. The charmed creature's speed drops to 0, and the creature is incapacitated and visibly dazed. On subsequent turns, you can use your action to maintain this effect, extending its duration until the end of your next turn. However, the effect ends if you move more than 5 feet away from the creature, if the creature can neither see nor hear you, or if the creature takes damage. Once the effect ends, or if the creature succeeds on its initial saving throw against this effect, you can't use this feature on that creature again until you finish a long rest.") )
```

## Instinctive Charm
*6th-level Enchantment feature*

When a creature you can see within 30 feet of you makes an attack roll against you, you can use your reaction to divert the attack, provided that another creature is within the attack's range. The attacker must make a Wisdom saving throw against your wizard spell save DC. On a failed save, the attacker must target the creature that is closest to it, not including you or itself. If multiple creatures are closest, the attacker chooses which one to target.

On a successful save, you can't use this feature on the attacker again until you finish a long rest.

You must choose to use this feature before knowing whether the attack hits or misses. Creatures that can't be charmed are immune to this effect.

```
def level6(npc):
    npc.reactions.append(f"***Instinctive Charm.*** When a creature you can see within 30 feet of you makes an attack roll against you, you divert the attack, provided that another creature is within the attack's range. The attacker must make a Wisdom saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}). On a failed save, the attacker must target the creature that is closest to it, not including you or itself. If multiple creatures are closest, the attacker chooses which one to target. On a successful save, you can't use this feature on the attacker again until you finish a long rest. You must choose to use this feature before knowing whether the attack hits or misses. Creatures that can't be charmed are immune to this effect.")
```

## Split Enchantment
*10th-level Enchantment feature*

When you cast an enchantment spell of 1st level or higher that targets only one creature, you can have it target a second creature.

```
def level10(npc):
    npc.traits.append("***Split Enchantment.*** When you cast an enchantment spell of 1st level or higher that targets only one creature, you can have it target a second creature.")
```

## Alter Memories
*14th-level Enchantment feature*

You gain the ability to make a creature unaware of your magical influence on it. When you cast an enchantment spell to charm one or more creatures, you can alter one creature's understanding so that it remains unaware of being charmed.

Additionally, once before the spell expires, you can use your action to try to make the chosen creature forget some of the time it spent charmed. The creature must succeed on an Intelligence saving throw against your wizard spell save DC or lose a number of hours of its memories equal to 1 + your Charisma modifier (minimum 1). You can make the creature forget less time, and the amount of time can't exceed the duration of your enchantment spell.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Alter Memories.*** When you cast an enchantment spell to charm one or more creatures, you can alter one creature's understanding so that it remains unaware of being charmed. Additionally, once before the spell expires, you can use your action to try to make the chosen creature forget some of the time it spent charmed. The creature must succeed on an Intelligence saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}) or lose {1 + npc.CHAbonus()} hours of its memories. You can make the creature forget less time, and the amount of time can't exceed the duration of your enchantment spell.") )
```
