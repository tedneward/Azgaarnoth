# Sorcerous Origin: Blood Magic
Your magic is the magic within all living blood--and you use none more often than your own. It comes naturally to you, and you find that your blood is strong, and getting stronger the more you draw on its magical power. Most who have their blood continually tapped for magic begin to suffer illness and frailty, but your blood is different in some way. Perhaps your blood is growing stronger the way warriors train their muscles, or perhaps your blood carries a gift made for blood magic itself. Whatever it is, you feel your heartbeat grow stronger and louder with every growth in sanguine power.

```
name = 'Blood'
description = "***Sorcerous Origin: Blood Magic.*** Your magic is the magic within all living blood - and you use none more often than your own. It comes naturally to you, and you find that your blood is strong, and getting stronger the more you draw on its magical power. Most who have their blood continually tapped for magic begin to suffer illness and frailty, but your blood is different in some way. Perhaps your blood is growing stronger the way warriors train their muscles, or perhaps your blood carries a gift made for blood magic itself. Whatever it is, you feel your heartbeat grow stronger and louder with every growth in sanguine power."
```

## Blood Magic
*1st-level Blood Magic feature*

You invoke blood magic to gain supernatural powers.

```
def level1(npc):
```

**Blood Pool.** You have a number of blood points determined by your sorcerer level. You can have more blood points than shown on the table for your level. These points automatically regenerate after a long rest.

Level | Blood Points
----- | ------------
1-4   | 1
5-8   | 2
9-12  | 3
13-16 | 4
17-20 | 5

Additionally, you can use a bonus action to call upon the power of blood by either inflicting a minor or severe wound upon yourself.

**Minor Wound.** Inflicting a minor wound requires the expenditure of 1 hit die and 1d8 hit points, granting you gain 1 blood point.

**Severe Wound.** Inflicting a severe wound requires the expenditure of 2 hit dice and 2d8 hit points, granting you gain 2 blood points.

Willing creatures can offer up their blood, so long as they are within 5 feet of you when you perform the bonus action. Charmed creatures will always be willing, and this effect does not count as "damage" or an "attack" for purposes of ending the charmed effect.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Blood Magic.*** You call upon the power of blood by either inflicting a minor (expend 1 hit die and 1d8 hit points, gain {'1 blood point' if npc.levels('Wizard') < 14 else '2 blood points'}) or severe wound (expend 2 hit dice and 2d8 hit points, gain {'2' if npc.levels('Wizard') < 14 else '4'} blood points) upon yourself or upon a willing creature within 5 feet of you. Charmed creatures will always be willing, and this effect does not count as damage or an attack for purposes of ending the charmed effect.") )
```

## Hematurgy
*1st-level Blood Magic feature*

You can spend blood points to make the next sorcerer spell you cast on this turn a *blood*-tagged spell, and it does not require a spell slot if it would normally expend a spell slot of a spell level equal to or less than the number of blood points you expended on this feature this turn. You cannot use this feature to cast a spell at a level higher than you have spell slots for (expended or otherwise).

You also gain the ability to expend your life force more directly in the pursuit of powerful magic. As a bonus action on your tum, you can choose to expend any number of blood points you have, gaining 1 sorcery point for each blood point expended. This feature cannot increase your current sorcery point total above the maximum for your level.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Hematurgy: Bloodcasting (Recharges on long rest).*** You can spend blood points to make the next sorcerer spell you cast on this turn a *blood*-tagged spell, and it does not require a spell slot if it would normally expend a spell slot of a spell level equal to or less than the number of blood points you expended on this feature this turn. You cannot use this feature to cast a spell at a level higher than you have spell slots for (expended or otherwise).") )

    npc.defer(lambda npc: npc.bonusactions.append(f"***Hematurgy: Boosted Magic (Recharges on long rest).*** You choose to expend any number of hit dice you have, gaining 1 sorcery point for each hit die expended. This feature cannot increase your current sorcery point total above the maximum for your level. You can't expend more than {npc.levels('Sorcerer') // 2} hit dice using Hematurgy before finishing a long rest.") )
```

## Blood Effect
*1st-level Bloodmancer feature*

While you possess one or more blood points, you gain the following features:

* **Armor of Vitality.** When you do not wear armor, your AC equals 13 + your Constitution modifier.

* **Lifeblood.** You gain advantage on your first death saving throw of the day.

```
    def assignac(npc):
        npc.armorclass['Blood Magic'] = 13 + npc.CONbonus()
    npc.defer(lambda npc: assignac(npc) )
    npc.defer(lambda npc: npc.traits.append(f"***Blood Magic: Armor of Vitality.*** While you possess one or more blood points, and you do not wear armor, your AC is {13 + npc.CONbonus()}.") )
    npc.defer(lambda npc: npc.traits.append(f"***Blood Magic: Lifeblood.*** While you possess one or more blood points, you gain advantage on your death saving throws.") )
```

Furthermore, as a bonus action you can expend blood points to perform the following blood effects:

* **Blood Agony.** When you hit a creature with a melee or spell attack, you can expend 1 or more blood points to deal psychic damage to the target, in addition to the damage of the attack. The extra damage is 1d6 for 1 blood point, plus 1d6 for each additional blood point, to a maximum of 5d6.
    At 14th level, increase the damage die of Blood Agony to a d8.

* **Blood Sense.** The sound of blood pumping in the veins of the living registers upon your senses like a soothing rhythm upon your being. Expend 1 blood point as an action to focus your awareness upon the immediate area to reveal the presence of living creatures. Until the end of your next turn, you know the location of any beast, giant, or humanoid, within 60 feet that is not behind total cover. You know the type (humanoid, fey, beast, etc) of any being whose presence you sense, but not the identity of the creature. Constructs and undead will not register on your Blood Sense.

* **Fortitude of Blood.** Expend 1 blood point as a bonus action to gain a bonus to Constitution saving throws, which lasts for 1 minute, equal to your Intelligence modifier (minimum of +1). You can invoke this ritual twice. Afterward, you cannot perform it again until you finish a short or long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Blood Magic: Blood Agony.*** When you hit a creature with a melee or spell attack, you expend 1 or more blood points to deal psychic damage to the target, in addition to the damage of the attack. The extra damage is 1{'d6' if npc.levels('Wizard') < 14 else 'd8'} for 1 blood point, plus 1{'d6' if npc.levels('Wizard') < 14 else 'd8'} for each additional blood point, to a maximum of 5{'d6' if npc.levels('Wizard') < 14 else 'd8'}.") )
    npc.bonusactions.append("***Blood Magic: Blood Sense.*** Expend 1 blood point as an action to focus your awareness upon the immediate area to reveal the presence of living creatures. Until the end of your next turn, you know the location of any beast, giant, or humanoid, within 60 feet that is not behind total cover. You know the type of any being whose presence you sense, but not the identity of the creature.")
    npc.defer(lambda npc: npc.bonusactions.append("***Blood Magic: Fortitude of Blood (2/Recharges on short or long rest).*** Expend 1 blood point as a bonus action to gain a +{npc.INTbonus()} bonus to Constitution saving throws, which lasts for 1 minute. You can invoke this ritual twice. Afterward, you cannot perform it again until you finish a short or long rest.") )
```

## Bleed Magic
*6th-level Blood Magic feature*

You gain the ability to cast spells when you are wounded, turning the blood spilt from your veins into magic as you bleed. When you take slashing, bludgeoning, or piercing damage, you can spend 2 sorcery points and use your Reaction to cast one *blood*-tagged spell that would normally require an action or bonus action to cast. You cast this spell after you take the damage. You may use this feature even if you have cast a spell on both your action and bonus action.

```
def level6(npc):
    npc.traits.append("***Resistent Blood.*** You gain advantage on saving throws made to resist *blood*-tagged spells and to resist poison.")

    npc.reactions.append("***Bleed Magic.*** When you take slashing, bludgeoning, or piercing damage, you spend 2 sorcery points to cast one *blood*-tagged spell that would normally require an action or bonus action to cast. You cast this spell after you take the damage.")
```

## Crimson Power
*14th-level Blood Magic feature*

You learn how to make use of the blood your enemies have already spilled from you to strengthen your magic beyond its normal limits even as your blood magically shields you from harm. While you have no more than half your hit points left, and you roll damage for a sorcerer spell that you cast, you add your proficiency bonus as bonus damage. You can only add this bonus damage once per turn.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Crimson Power.*** While you have no more than half your hit points left, when you roll damage for a sorcerer spell that you cast, you add {npc.proficiencybonus()} as bonus damage. You can only add this bonus damage once per turn.") )
```

## Sanguine Storm
*18th-level Blood Magic feature*

You learn how to force your magic into the body of a mortally wounded creature with such ease and force as to create an explosion of magic. When you deal damage to a creature and reduce it to 0 hit points, you can spend 2 sorcery points to cause the creature to explode violently. The target fails one death saving throw automatically. Each creature within a 15-foot sphere centered on the target must make a Constitution saving throw. On a failed saving throw, a creature takes 7d6 necrotic damage and is [necrotized](../../Conditions/Necrotized.md) for 1 minute. On a successful saving throw, a creature only takes half damage.

For the purpose of any other Sorcerer class feature, you treat each explosion from this class feature as if it were a Necromancy spell that you know as a sorcerer.

```
def level18(npc):
    npc.traits.append("***Sanguine Storm.*** When you deal damage to a creature and reduce it to 0 hit points, you can spend 2 sorcery points to cause the creature to explode violently. The target fails one death saving throw automatically. Each creature within a 15-foot sphere centered on the target must make a Constitution saving throw. On a failed saving throw, a creature takes 7d6 necrotic damage and is [necrotized](http://azgaarnoth.tedneward.com/conditions/Necrotized). On a successful saving throw, a creature takes half damage. For the purpose of any other Sorcerer class feature, you treat each explosion from this class feature as if it were a Necromancy spell that you know as a sorcerer.")
```
