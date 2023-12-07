# Arcane Tradition: School of Divination
The counsel of a diviner is sought by royalty and commoners alike, for all seek a clearer understanding of the past, present, and future. As a diviner, you strive to part the veils of space, time, and consciousness so that you can see clearly. You work to master spells of discernment, remote viewing, supernatural knowledge, and foresight.

Many diviners are a part of the [Silent Tower](../../Organizations/MageSchools/SilentTower.md) and [Spinning Hands](../../Organizations/MageSchools/SpinningHands.md) schools, and often contract out as paid advisers to the various [noble Houses](../../Organizations/Houses/index.md). Many [mercenary companies](../../Organizations/MercCompanies/index.md) use diviners for reconaissance purposes, as do many [militant orders](../../Organizations/MilitantOrders/index.md). Diviners who are hard on their luck can also always find employment in a [rogues guild](../../Organizations/RoguesGuilds/index.md), helping to scout a score ahead of time.

```
name = 'Divination'
description = "***Arcane Tradition: School of Divination.*** The counsel of a diviner is sought by royalty and commoners alike, for all seek a clearer understanding of the past, present, and future. As a diviner, you strive to part the veils of space, time, and consciousness so that you can see clearly. You work to master spells of discernment, remote viewing, supernatural knowledge, and foresight."
```

## Divination Savant
*2nd-level Divination feature*

The gold and time you must spend to copy a Divination spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Divination Savant.*** The gold and time you must spend to copy a Divination spell into your spellbook is halved.")
```

## Portent
*2nd-level Divination feature*

Glimpses of the future begin to press in on your awareness. When you finish a long rest, roll two d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn.

Each foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls.

```
    npc.defer(lambda npc: npc.traits.append(f"***Portent.*** When you finish a long rest, roll {'two' if npc.levels('Wizard') < 14 else 'three'} d20s and record the numbers rolled. You can replace any attack roll, saving throw, or ability check made by you or a creature that you can see with one of these foretelling rolls. You must choose to do so before the roll, and you can replace a roll in this way only once per turn. Each foretelling roll can be used only once. When you finish a long rest, you lose any unused foretelling rolls.") )
```

## Expert Divination
*6th-level Divination feature*

Casting divination spells comes so easily to you that it expends only a fraction of your spellcasting efforts. When you cast a divination spell of 2nd level or higher using a spell slot, you regain one expended spell slot. The slot you regain must be of a level lower than the spell you cast and can't be higher than 5th level.

```
def level6(npc):
    npc.traits.append("***Expert Divination.*** When you cast a divination spell of 2nd level or higher using a spell slot, you regain one expended spell slot. The slot you regain must be of a level lower than the spell you cast and can't be higher than 5th level.")
```

## The Third Eye
*10th-level Divination feature*

You can use your action to increase your powers of perception. When you do so, choose one of the following benefits, which lasts until you are incapacitated or you take a short or long rest. You can't use the feature again until you finish a short or long rest.

***Darkvision.*** You gain darkvision out to a range of 60 feet.

***Ethereal Sight.*** You can see into the Ethereal Plane within 60 feet of you.

***Greater Comprehension.*** You can read any language.

***See Invisibility.*** You can see invisible creatures and objects within 10 feet of you that are within line of sight.

```
def level10(npc):
    npc.actions.append("***Third Eye (Recharges on short or long rest).*** Choose one of the following benefits, which lasts until you are incapacitated or you take a short or long rest: **Darkvision.** You gain darkvision out to a range of 60 feet.**Ethereal Sight.** You can see into the Ethereal Plane within 60 feet of you.**Greater Comprehension.** You can read any language. **See Invisibility.** You can see invisible creatures and objects within 10 feet of you that are within line of sight.")
```

## Greater Portent
*14th-level Divination feature*

The visions in your dreams intensify and paint a more accurate picture in your mind of what is to come. You roll three d20s for your Portent feature, rather than two.
