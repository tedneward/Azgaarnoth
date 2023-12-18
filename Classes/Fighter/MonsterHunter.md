# Martial Archetype: Monster Hunter
As an archetypal Monster Hunter, you are an expert at defeating supernatural threats. Typically mentored by an older, experienced Monster Hunter, you learn to overcome a variety of unnatural defenses and attacks, including those of undead, lycanthropes, and other creatures of horror. Most Monster Hunters end up joining the [Slayer Conclave](../../Organization/MerchantGuilds/SlayerConclave.md) at some point (and some leave it again when they tire of it).

Note that some races may consider other races to be "supernatural threats".

```
name = 'Monster Hunter'
description = "***Martial Archetype: Monster Hunter.*** As an archetypal Monster Hunter, you are an expert at defeating supernatural threats. Typically mentored by an older, experienced Monster Hunter, you learn to overcome a variety of unnatural defenses and attacks, including those of undead, lycanthropes, and other creatures of horror."
```

## Bonus Proficiencies
*3rd-level Monster Hunter feature*

You gain proficiency in two of the following skills of your choice: Arcana, History, Insight, Investigation, Nature, or Perception. You can gain proficiency with a tool of your choice in place of one skill choice.

```
def level3(npc):
    chooseskill(npc, ['Arcana', 'History', 'Insight', 'Investigation', 'Nature', 'Perception'])
    chooseskill(npc, tools['artisan'])
```

## Combat Superiority
*3rd-level Monster Hunter feature*

You gain a set of abilities that are fueled by special dice called superiority dice.

***Superiority Dice.*** You have four superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest.

You gain another superiority die at 7th level and one more at 15th level.

You can expend superiority dice to gain a number of different benefits:

* **Precision Attack**. When you make a weapon attack against a creature, you can expend one superiority die to add it to the attack roll. You can use this ability before or after making the attack roll, but before any of the effects of the attack are applied.

* **Sharpened Attack**. When you damage a creature with a weapon attack, you can expend one superiority die to add it to the damage roll. You can use this ability after rolling damage. If the attack causes the target to make a Constitution saving throw to maintain concentration, it has disadvantage on that save.

* **Sharpened Senses**. When you make a Wisdom (Perception) check to detect a hidden creature or object, or a Wisdom (Insight) check to determine if someone is lying to you, you can expend one superiority die to add it to the roll. You can use this feature after seeing the total but before learning if you succeeded or failed.

* **Superior Willpower**. When you make an Intelligence, a Wisdom, or a Charisma saving throw, you can expend one superiority die to add it to the roll. You can use this feature only before you learn if the save succeeded or failed.

```
    npc.superioritydicetype = 'd8'
    npc.superioritydice = 4

    npc.defer(lambda npc: npc.traits.append(f"***Superiority Dice (Recharges on short or long rest).*** You have {npc.superioritydice} superiority dice, which are {npc.superioritydicetype}s.{' When you roll initiative and have no superiority dice remaining, you regain one superiority die.' if npc.levels('Fighter') >= 15 else ''} A superiority die is expended when you use it. You can expend superiority dice to exercise your Precision Attack, Sharpened Attack, Sharpened Senses, or Superior Willpower features."))
    npc.traits.append("***Precision Attack.*** When you make a weapon attack against a creature, you can expend one superiority die to add it to the attack roll. You can use this ability before or after making the attack roll, but before any of the effects of the attack are applied. ")
    npc.traits.append(f"***Sharpened Attack**. When you damage a creature with a weapon attack, you can expend {'one' if npc.levels('Fighter') < 7 else 'up to two'} superiority {'die' if npc.levels('Fighter') < 7 else 'dice'} to add it to the damage roll. You can use this ability after rolling damage. {'If the target of your attack is an aberration, a fey, a fiend, or an undead, you deal maximum damage with both dice, instead of rolling them. ' if npc.levels('Fighter') >= 7 else ''}If the attack causes the target to make a Constitution saving throw to maintain concentration, it has disadvantage on that save.")
    npc.traits.append("***Sharpened Senses**. When you make a Wisdom (Perception) check to detect a hidden creature or object, or a Wisdom (Insight) check to determine if someone is lying to you, you can expend one superiority die to add it to the roll. You can use this feature after seeing the total but before learning if you succeeded or failed.")
    npc.traits.append("***Superior Willpower**. When you make an Intelligence, a Wisdom, or a Charisma saving throw, you can expend one superiority die to add it to the roll. You can use this feature only before you learn if the save succeeded or failed.")
```

## Hunter's Mysticism
*3rd-level Monster Hunter feature*

Your study of the supernatural gives you a limited ability to use magic. You can cast [detect magic](http://azgaarnoth.tedneward.com/magic/spells/detect-magic) as a ritual. You can cast [Protection from Evil and Good](http://azgaarnoth.tedneward.com/magic/spells/protection-from-evil-and-good), but you cannot cast it again with this feature until you finish a long rest. Wisdom is your spellcasting ability for these spells.

```
    npc.traits.append(f"***Hunter's Mysticism (Recharges on long rest).*** Your study of the supernatural gives you a limited ability to use magic. You can cast {spelllinkify('detect magic')} as a ritual at will. You can cast {spelllinkify('protection from evil and good')} once until you finish a long rest. Wisdom is your spellcasting ability for these spells.")
```

In addition, you gain the ability to speak one of the following languages of your choice: Abyssal, Celestial, or Infernal.

```
    npc.languages.append(choose("Choose a language: ", ['Abyssal', 'Celestial', 'Infernal']))
```

## Monster Slayer
*7th-level Monster Hunter feature*

Whenever you expend superiority dice to add to a damage roll, you can expend up to two dice instead of just one, adding both to the roll. Both dice are expended as normal. If the target of your attack is an aberration, a fey, a fiend, or an undead, you deal maximum damage with both dice, instead of rolling them.

```
def level7(npc):
    npc.superioritydice += 1
```

## Improved Combat Superiority
*10th-level Monster Hunter feature*

At 10th level, your superiority dice turn into d10s. At 18th level, they turn into d12s.

```
def level10(npc):
        npc.superioritydicetype = 'd10'
```

## Relentless
*15th-level Monster Hunter feature*

When you roll initiative and have no superiority dice remaining, you regain one superiority die.

```
def level15(npc):
    npc.superioritydice += 1

def level18(npc):
        npc.superioritydicetype = 'd12'
```
