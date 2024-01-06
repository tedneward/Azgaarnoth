# Sorcerous Origin: Blood Magic
Your magic is the magic within all living blood - and you use none more often than your own. It comes naturally to you, and you find that your blood is strong, and getting stronger the more you draw on its magical power. Most who have their blood continually tapped for magic begin to suffer illness and frailty, but your blood is different in some way. Perhaps your blood is growing stronger the way warriors train their muscles, or perhaps your blood carries a gift made for blood magic itself. Whatever it is, you feel your heartbeat grow stronger and louder with every growth in sanguine power.

```
name = 'Blood'
description = "***Sorcerous Origin: Blood Magic.*** Your magic is the magic within all living blood - and you use none more often than your own. It comes naturally to you, and you find that your blood is strong, and getting stronger the more you draw on its magical power. Most who have their blood continually tapped for magic begin to suffer illness and frailty, but your blood is different in some way. Perhaps your blood is growing stronger the way warriors train their muscles, or perhaps your blood carries a gift made for blood magic itself. Whatever it is, you feel your heartbeat grow stronger and louder with every growth in sanguine power."
```

## Resilient Blood
*1st-level Blood Magic feature*

Your blood is infused with resilient life energy, allowing you to draw more from that wellspring. You have one bonus sorcerer hit die. You gain another bonus hit die with the same rules at sorcerer levels 4, 8, 12, 16, and 20. These hit dice do not count for your hit point maximum.

In addition, when you finish a short rest, you can choose to regain hit points equal to your Constitution modifier + half your sorcerer level (minimum 1). Once you do so, you can't do so again until you finish a long rest.

When you reach 6th leveL you gain advantage on saving throws made to resist **Blood** spells and to resist poison.

```
def level1(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Resilient Blood.*** You have {(npc.levels('Sorcerer') // 4) + 1} bonus sorcerer hit dice. These hit dice do not count for your hit point maximum.") )
    npc.defer(lambda npc: npc.traits.append(f"***Resilient Recovery (Recharges on long rest).*** When you finish a short rest, you regain {npc.CONbonus() + ((npc.levels('Sorcerer') + 1) // 2)} hit points. Once you do so, you can't do so again until you finish a long rest.") )
```

## Hematurgy
*1st-level Blood Magic feature*

You gain the ability to cast beyond your limits by sacrificing the vital life force inside your own blood. As a bonus action on your turn, you can spill your own blood and spend up to 5 of your remaining hit dice, but instead of healing you take 1d8 damage per hit dice expended. This damage doesn't provoke concentration checks and ignores all resistances or immunities.

The next sorcerer spell you cast on this turn is also a **Blood** spell and does not require a spell slot if it would normally expend a spell slot of a spell level equal to or less than the number of hit dice you expended on this feature this turn. You cannot use this feature to cast a spell at a level higher than you have spell slots for (expended or otherwise).

You also gain the ability to expend your life force more directly in the pursuit of powerful magic. As a bonus action on your tum, you can choose to expend any number of hit dice you have, gaining 1 sorcery point for each hit die expended. This feature cannot increase your current sorcery point total above the maximum for your level.

You can't expend more hit dice using this feature than half your sorcerer level (minimum 1) before finishing a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Hematurgy: Bloodcasting (Recharges on long rest).*** You spill your own blood and spend up to 5 of your remaining hit dice, but instead of healing you take 1d8 damage per hit dice expended. This damage doesn't provoke concentration checks and ignores all resistances or immunities. The next sorcerer spell you cast on this turn is also a **Blood** spell and does not require a spell slot if it would normally expend a spell slot of a spell level equal to or less than the number of hit dice you expended on this feature this turn. You cannot use this feature to cast a spell at a level higher than you have spell slots for (expended or otherwise). You can't expend more than {npc.levels('Sorcerer') // 2} hit dice using Hematurgy before finishing a long rest.") )

    npc.defer(lambda npc: npc.bonusactions.append(f"***Hematurgy: Boosted Magic (Recharges on long rest).*** You choose to expend any number of hit dice you have, gaining 1 sorcery point for each hit die expended. This feature cannot increase your current sorcery point total above the maximum for your level. You can't expend more than {npc.levels('Sorcerer') // 2} hit dice using Hematurgy before finishing a long rest.") )
```

## Bleed Magic
*6th-level Blood Magic feature*

You gain the ability to cast spells when you are wounded, turning the blood spilt from your veins into magic as you bleed. When you take slashing, bludgeoning, or piercing damage, or damage from a Blood spell you can spend 2 sorcery points and use your reaction to cast one spell that would normally require an action or bonus action to cast. You cast this spell after you take the damage.

```
def level6(npc):
    npc.traits.append("***Resistent Blood.*** You gain advantage on saving throws made to resist **Blood** spells and to resist poison.")

    npc.reactions.append("***Bleed Magic.*** When you take slashing, bludgeoning, or piercing damage, or damage from a Blood spell, you spend 2 sorcery points to cast one spell that would normally require an action or bonus action to cast. You cast this spell after you take the damage.")
```

## Crimson Power
*14th-level Blood Magic feature*

You learn how to make use of the blood your enemies have already spilled from you to strengthen your magic beyond its normal limits even as your blood magically shields you from harm. While you have no more than half your hit points left, you gain a + 3 bonus to AC. When you have this bonus and you roll damage for a sorcerer spell that you cast, you add your proficiency bonus as bonus damage. You can only add this bonus damage once per turn.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Crimson Power.*** While you have no more than half your hit points left, you gain a + 3 bonus to AC. When you have this bonus and you roll damage for a sorcerer spell that you cast, you add {npc.proficiencybonus()} as bonus damage. You can only add this bonus damage once per turn.") )
```

## Sanguine Storm
*18th-level Blood Magic feature*

You learn how to force your magic into the body of a mortally wounded creature with such ease and force as to create an explosion of magic. When you deal damage to a creature and reduce it to 0 hit points, you can spend 2 sorcery points to cause the creature to explode violently. The target fails one death saving throw automatically. Each creature within a 15-foot sphere centered on the target must make a Constitution saving throw. On a failed saving throw, a creature takes 7d6 necrotic damage. On a successful saving throw, a creature takes half damage.

For the purpose of any other Sorcerer class feature, you treat each explosion from this class feature as if it were a Necromancy spell that you know as a sorcerer.

```
def level18(npc):
    npc.traits.append("***Sanguine Storm.*** When you deal damage to a creature and reduce it to 0 hit points, you can spend 2 sorcery points to cause the creature to explode violently. The target fails one death saving throw automatically. Each creature within a 15-foot sphere centered on the target must make a Constitution saving throw. On a failed saving throw, a creature takes 7d6 necrotic damage. On a successful saving throw, a creature takes half damage. For the purpose of any other Sorcerer class feature, you treat each explosion from this class feature as if it were a Necromancy spell that you know as a sorcerer.")
```
