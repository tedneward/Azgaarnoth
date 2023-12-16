# Arcane Tradition: War Magic
Followers of this tradition are known as war mages. They see their magic as both a weapon and armor, a resource superior to any piece of steel. War mages act fast in battle, using their spells to seize tactical control of a situation. Their spells strike hard, while their defensive skills foil their opponents' attempts to counterattack. War mages are also adept at turning other spellcasters' magical energy against them.

A variety of arcane colleges (most notably the [Fiery Fist](../../Organizations/MageSchools/FieryFist.md) and [Crimson Sun](../../Organizations/MageSchools/CrimsonSun.md) schools) specialize in training wizards for war. The tradition of War Magic blends principles of evocation and abjuration, rather than specializing in either of those schools. It teaches techniques that empower a caster's spells, while also providing methods for wizards to bolster their own defenses.

```
name = 'War Magic'
description = "***Arcane Tradition: War Magic.*** Followers of this tradition are known as war mages. They see their magic as both a weapon and armor, a resource superior to any piece of steel. War mages act fast in battle, using their spells to seize tactical control of a situation. Their spells strike hard, while their defensive skills foil their opponents' attempts to counterattack. War mages are also adept at turning other spellcasters' magical energy against them."
```

## Arcane Deflection
*2nd-level War Magic feature*

You have learned to weave your magic to fortify yourself against harm. When you are hit by an attack or you fail a saving throw, you can use your reaction to gain a +2 bonus to your AC against that attack or a +4 bonus to that saving throw.

When you use this feature, you can't cast spells other than cantrips until the end of your next turn.

```
def level2(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Arcane Deflection.*** When you are hit by an attack or you fail a saving throw, you gain a +2 bonus to your AC against that attack or a +4 bonus to that saving throw. When you use this feature, you can't cast spells other than cantrips until the end of your next turn.{'' if npc.levels('Wizard') < 14 else ' You cause magical energy to arc from you, causing up to three creatures of your choice within 60 feet of you to each take' + str(npc.levels('Wizard') // 2) + ' force damage.'}") )
```

## Tactical Wit
*2nd-level War Magic feature*

Your keen ability to assess tactical situations allows you to act quickly in battle. You can give yourself a bonus to your initiative rolls equal to your Intelligence modifier.

```
    npc.defer(lambda npc: npc.traits.append(f"***Tactical Wit.*** You have a +{npc.INTbonus()} bonus to your initiative rolls.") )
```

## Power Surge
*6th-level War Magic feature*

You can store magical energy within yourself to later empower your damaging spells.

You can store a maximum number of power surges equal to your Intelligence modifier (minimum of one). Whenever you finish a long rest, your number of power surges resets to one. Whenever you successfully end a spell with Dispel Magic or Counterspell, you gain one power surge, as you steal magic from the spell you foiled. If you end a short rest with no power surges, you gain one power surge.

Once per turn when you deal damage to a creature or object with a wizard spell, you can spend one power surge to deal extra force damage to that target. The extra damage equals half your wizard level.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Power Surge.*** Once per turn when you deal damage to a creature or object with a wizard spell, you can spend one power surge to deal {npc.levels('Wizard') // 2} extra force damage to that target. You can store a maximum number of {npc.INTbonus()} power surges. Whenever you finish a long rest, your number of power surges resets to one. Whenever you successfully end a spell with {spelllinkify('dispel magic')} or {spelllinkify('counterspell')}, you gain one power surge, as you steal magic from the spell you foiled. If you end a short rest with no power surges, you gain one power surge.") )
```

## Durable Magic
*10th-level War Magic feature*

The magic you channel helps ward off harm. While you maintain concentration on a spell, you have a +2 bonus to AC and all saving throws.

```
def level10(npc):
    npc.traits.append("***Durable Magic.*** While you maintain concentration on a spell, you have a +2 bonus to AC and all saving throws.")
```

## Deflecting Shroud
*14th-level War Magic feature*

Your Arcane Deflection becomes infused with deadly magic. When you use your Arcane Deflection feature, you can cause magical energy to arc from you. Up to three creatures of your choice within 60 feet of you each take force damage equal to half your wizard level.

