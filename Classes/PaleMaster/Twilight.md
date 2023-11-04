# Deathless Axiom: Elegy of Twilight
In an attempt to become one with the darkness itself, twilight pale masters devote their research to shadows and wraiths.

Their haunting devotion gives them unique abilities unavailable to other pale masters, ones which allow them to become a terrifying form partially illuminated by the moon's eerie gaze.

```
name = 'Twilight'
description = "***Deathless Axiom: Elegy of Twilight.*** In an attempt to become one with the darkness itself, twilight pale masters devote their research to shadows and wraiths. Their haunting devotion gives them unique abilities unavailable to other pale masters, ones which allow them to become a terrifying form partially illuminated by the moon's eerie gaze."
```

## Undead Graft: Umbral Arm
*3rd-level Elegy of Twilight feature*

You infuse the pores of your arm with small traces of necrotic energies that manifest and wreath your arm in shadow.

Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells with it and perform the somatic components of spells even when you have weapons or a shield in one or both hands. Additionally, you may attack with your graft as if it were a simple weapon with which you are proficient. To do so, you make a melee spell attack against a creature, dealing 1d8 necrotic damage on a hit.

```
def level3(npc):
    npc.traits.append("***Umbral Arm.*** You infuse the pores of your arm with small traces of necrotic energies that manifest and wreath your arm in shadow. Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells with it and perform the somatic components of spells even when you have weapons or a shield in one or both hands.")

    npc.defer(lambda npc: npc.actions.append(f"***Umbral Arm.*** *Melee Spell Attack:* +{npc.proficiencybonus() + npc.STRbonus() + (0 if npc.levels('Pale Master') < 6 else 1 if npc.levels('Pale Master') < 12 else 2 if npc.levels('Pale Master') < 17 else 3)} to hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + (0 if npc.levels('Pale Master') < 6 else 1 if npc.levels('Pale Master') < 12 else 2 if npc.levels('Pale Master') < 17 else 3)} necrotic damage.") )
```

At 6th level, your graft gains a +1 bonus to melee attacks and damage rolls. This increases to a +2 bonus at 12th level and a +3 bonus at 17th level.

## Summon Shadow
*3rd-level Elegy of Twilight feature*

You are able to assert your control over shadows that lurk in the dark.

While in dim light or darkness, you spend 1 minute conjuring a [shadow](../../Creatures/Shadow.md) from the darkness. Roll initiative for the shadow, which has its own turns. It obeys your verbal commands and is under your control for 10 minutes, at which point it vanishes. You can only have one shadow summoned at a time. If a shadow under your control dies, 10 minutes pass, or you dismiss it as an action, you cannot use this feature again until you complete a long rest.

```
    npc.actions.append("***Summon Shadow (Recharges on long rest).*** While in dim light or darkness, you spend 1 minute conjuring a [shadow](http://azgaarnoth.tedneward.com/Creatures/Undead/Shadow/) from the darkness. Roll initiative for the shadow, which has its own turns. It obeys your verbal commands and is under your control for 10 minutes, at which point it vanishes. You can only have one shadow summoned at a time. It remains until it dies, 10 minutes pass, or you dismiss it as an action.")
```

## Fearful Touch
*6th-level Elegy of Twilight feature*

When you hit a creature with a melee spell attack from your undead graft, you can instill irrational terror. The target takes an additional 2d8 necrotic damage and must succeed on a Wisdom saving throw or become frightened for 1 minute. A creature frightened in this manner must take the Dash action and move away from you by the safest available route on each of its turns. If there is nowhere to move, the creature stays in its current location, but takes 2d8 necrotic damage.

You can use this feature once per long rest at 6th level. You gain an additional use at 12th level and again at 17th level. 

Expended uses are regained when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Fearful Touch ({'' if npc.levels('Pale Master') < 12 else '2/' if npc.levels('Pale Master') < 17 else '3/'}Recharges on long rest).*** When you hit a creature with a melee spell attack from your Undead Graft, you can instill irrational terror. The target takes an additional 2d8 necrotic damage and must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()} ) or become frightened for 1 minute. A creature frightened in this manner must take the Dash action and move away from you by the safest available route on each of its turns. If there is nowhere to move, the creature stays in its current location, but takes 2d8 necrotic damage.") )
```

## Insatiable Horror
*6th-level Elegy of Twilight feature*

You can cast the fear spell using one of your spell slots, but it does not count towards your number of prepared spells. When you cast fear, each target makes the Wisdom saving throw with disadvantage.

```
    npc.traits.append(f"***Insatiable Horror.*** You add the {spelllinkify('fear')} spell to your list of prepared spells, but it does not count towards your limit. When you cast it, each target makes the Wisdom saving throw with disadvantage.")
```

## Undead Cohort: Wraith
*10th-level Elegy of Twilight feature*

You are able to taint the soul of a recently slain creature. You choose the corpse of a creature that has died in the last 24 hour and infuse it with necrotic energy, causing its soul to rise as a [wraith](../../Creatures/Undead/Wraith.md) under your control.

The wraith dissipates when it drops to 0 hit points or when 1-hour passes. The wraith is friendly to you and your companions for the duration. Roll initiative for the wraith, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the wraith, it defends itself from hostile creatures but otherwise takes no actions.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level10(npc):
    npc.actions.append("***Undead Cohort: Wraith (Recharges on long rest).*** You choose the corpse of a creature that has died in the last 24 hour and infuse it with necrotic energy, causing its soul to rise as a wraith under your control. The wraith dissipates when it drops to 0 hit points or when 1-hour passes. The wraith is friendly to you and your companions for the duration. Roll initiative for the wraith, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the wraith, it defends itself from hostile creatures but otherwise takes no actions.")
```

## Terror in the Night
*14th-level Elegy of Twilight feature*

Your research has led to a profound breakthrough, allowing you to become one with the darkness.

While in an area of dim light or darkness, you can meld with the shadows for 1 hour. While melded, you gain advantage on Dexterity (Stealth) checks, can take the Hide action as a bonus action, and are able to move through a space as narrow as 1 inch wide without squeezing. You retain all of your normal statistics and abilities while melded. You can move through areas of sunlight while melded, but suffer disadvantage on attack rolls, ability checks, and saving throws while in sunlight. Ending your turn in sunlight ends the melded condition.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level14(npc):
    npc.actions.append("***Terror in the Night (Recharges on short or long rest).*** While in an area of dim light or darkness, you can meld with the shadows for 1 hour. While melded, you gain advantage on Dexterity (Stealth) checks, can take the Hide action as a bonus action, and are able to move through a space as narrow as 1 inch wide without squeezing. You retain all of your normal statistics and abilities while melded. You can move through areas of sunlight while melded, but suffer disadvantage on attack rolls, ability checks, and saving throws while in sunlight. Ending your turn in sunlight ends the condition.")
```