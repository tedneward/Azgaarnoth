# Monk
Monks are united in their ability to magically harness the energy that flows in their bodies. Whether channeled as a striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a monk does.

```
name = 'Monk'
description = "***Class: Monk.*** Monks are united in their ability to magically harness the energy that flows in their bodies. Whether channeled as a striking display of combat prowess or a subtler focus of defensive ability and speed, this energy infuses all that a monk does."
```

## Class Features
As a monk, you gain the following class features.

Level|Proficiency Bonus|Martial Arts|Ki Points|Unarmored Movement|Features
-----|-----------------|------------|---------|------------------|--------
1st  |+2               |1d4         |–        |–      |[Unarmored Defense](#unarmored-defense), [Martial Arts](#martial-arts)
2nd  |+2               |1d4         |2        |+10 ft.|[Ki](#ki), [Unarmored Movement](#unarmored-movement)
3rd  |+2               |1d4         |3        |+10 ft.|[Monastic Tradition](#monastic-tradition), [Deflect Missiles](#deflect-missiles)
4th  |+2               |1d4         |4        |+10 ft.|Ability Score Improvement, [Slow Fall](#slow-fall)
5th  |+3               |1d6         |5        |+10 ft.|[Extra Attack](#extra-attack), [Stunning Strike](#stunning-strike)
6th  |+3               |1d6         |6        |+15 ft.|[Ki-Empowered Strikes](#ki-empowered-strikes), Monastic Tradition feature
7th  |+3               |1d6         |7        |+15 ft.|[Evasion](#evasion), [Stillness of Mind](#stillness-of-mind)
8th  |+3               |1d6         |8        |+15 ft.|Ability Score Improvement
9th  |+4               |1d6         |9        |+15 ft.|[Unarmored Movement](#unarmored-movement) improvement
10th |+4               |1d6         |10       |+20 ft.|[Purity of Body](#purity-of-body)
11th |+4               |1d8         |11       |+20 ft.|Monastic Tradition feature
12th |+4               |1d8         |12       |+20 ft.|Ability Score Improvement
13th |+5               |1d8         |13       |+20 ft.|[Tongue of the Sun and Moon](#tongue-of-the-sun-and-moon)
14th |+5               |1d8         |14       |+25 ft.|[Diamond Soul](#diamond-soul)
15th |+5               |1d8         |15       |+25 ft.|[Timeless Body](#timeless-body)
16th |+5               |1d8         |16       |+25 ft.|Ability Score Improvement
17th |+6               |1d10        |17       |+25 ft.|Monastic Tradition feature
18th |+6               |1d10        |18       |+30 ft.|[Empty Body](#empty-body)
19th |+6               |1d10        |19       |+30 ft.|Ability Score Improvement
20th |+6               |1d10        |20       |+30 ft.|[Perfect Self](#perfect-self)

### Hit Points
**Hit Dice**: 1d8 per monk level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per monk level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: None

**Weapons**: Simple weapons, shortswords

**Tools**: Choose one type of artisan's tools or one musical instrument

**Saving Throws**: Strength, Dexterity

**Skills**: Choose two from Acrobatics, Athletics, History, Insight, Religion, and Stealth

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a shortsword or (b) any simple weapon
* (a) a dungeoneer's pack or (b) an explorer's pack
* 10 darts

```
def level1(npc):
    npc.savingthrows.append("STR")
    npc.savingthrows.append("DEX")

    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)
    npc.proficiencies.append("Shortsword")
    npc.proficiencies.append("One type of artisan's tools or musical instrument")

    skills = ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth']
    chooseskill(npc, skills)
    chooseskill(npc, skills)

    npc.equipment.append("Shortsword OR simple weapon")
    npc.equipment.append("10 darts")
    npc.equipment.append("Dungeoneer's pack, or explorer's pack")
```

## Unarmored Defense
*1st-level monk feature*

While you are wearing no armor and not wielding a shield, your AC equals 10 + your Dexterity modifier + your Wisdom modifier.

```
    def acadjust(npc):
        npc.armorclass['Unarmored Defense'] = (10 + npc.WISbonus())
    npc.defer(lambda npc: acadjust(npc))
```

## Martial Arts
*1st-level monk feature*

Your practice of martial arts gives you master of combat styles that use unarmed strikes and monk weapons, which are shortswords and any simple melee weapons that don't have the two-handed or heavy property.

You gain the following benefits while you are unarmed or wielding only monk weapons and you aren't wearing armor or wielding a shield:

* You can use Dexterity instead of Strength for the attack and damage rolls of your unarmed strikes and monk weapons.

* You can roll a d4 in place of the normal damage of your unarmed strike or monk weapon. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.

* When you use the Attack action with an unarmed strike or a monk weapon on your turn, you can make one unarmed strike as a bonus action. For example, if you take the Attack action and attack with a quarterstaff, you can also make an unarmed strike as a bonus action, assuming you haven't already taken a bonus action this turn.

Certain monasteries use specialized forms of the monk weapons. For example, you might use a club that is two lengths of wood connected by a short chain (called a nunchaku) or a sickle with a shorter, straighter blade (called a kama). Whatever name you use for a monk weapon, you can use the game statistics provided for the weapon on the Weapons page.

```
    def madie(npc):
        npc.martialartsdie = '4' if npc.levels('Monk') < 5 else '6' if npc.levels('Monk') < 11 else '8' if npc.levels('Monk') < 17 else '10'
    npc.defer(lambda npc: madie(npc))

    npc.bonusactions.append("***Martial Arts.*** When you use the Attack action with an Unarmed Strike or a monk weapon on your turn, you can make an additional Unarmed Strike.")

    npc.defer(lambda npc: npc.actions.append(f"***Unarmed Strike.*** *Melee Weapon Attack:* +{npc.proficiencybonus() + npc.DEXbonus()} to hit, reach 5 ft., one target. Hit: 1d{npc.martialartsdie} + {npc.DEXbonus()} bludgeoning damage.{' This attack is considered magical for purposes of overcoming resistance and immunity to nonmagical attacks and damage.' if npc.levels('Monk') > 5 else ''}"))
```

## Dedicated Weapon
*2nd-level optional monk feature*

You train yourself to use a variety of weapons as monk weapons, not just simple melee weapons and shortswords. Whenever you finish a short or long rest, you can touch one weapon, focus your ki on it, and then count that weapon as a monk weapon until you use this feature again.

The chosen weapon must meet these criteria:

* The weapon must be a simple or martial weapon.
* You must be proficient with it.
* It must lack the heavy and special properties.

```
def level2(npc):
    npc.traits.append("***Dedicated Weapon.*** Whenever you finish a short or long rest, you can touch one weapon (which must be a simple or martial weapon, one you are proficient in, and lacks the heavy and special properties), focus your ki on it, and then count that weapon as a monk weapon until you use this feature again.")
```

## Ki
*2nd-level monk feature*

Your training allows you to harness the mystic energy of ki. Your access to this energy is represented by a number of ki points. Your monk level determines the number of points you have, as shown in the Ki Points column of the Monk table.

You can spend these points to fuel various ki features. You start knowing three such features: Flurry of Blows, Patient Defense, and Step of the Wind. You learn more ki features as you gain levels in this class.

When you spend a ki point, it is unavailable until you finish a short or long rest, at the end of which you draw all of your expended ki back into yourself. You must spend at least 30 minutes of the rest meditating to regain your ki points.

Some of your ki features require your target to make a saving throw to resist the feature's effects. The saving throw DC is calculated as follows:

**Ki save DC** = 8 + your proficiency bonus + your Wisdom modifier

* **Flurry of Blows.** Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.

* **Patient Defense.** You can spend 1 ki point to take the Dodge action as a bonus action on your turn.

* **Step of the Wind.** You can spend 1 ki point to take the Disengage or Dash action as a bonus action on your turn, and your jump distance is doubled for the turn.

```
    npc.defer(lambda npc: npc.traits.append(f"***Ki ({npc.levels('Monk')} points/Recharges on short or long rest).*** Ki save DC {8 + npc.proficiencybonus() + npc.WISbonus()}.") )

    npc.bonusactions.append("***Ki: Flurry of Blows.*** Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two Unarmed Strikes.")

    npc.bonusactions.append("***Ki: Patient Defense.*** You can spend 1 ki point to take the Dodge action.")

    npc.bonusactions.append("***Ki: Step of the Wind.*** You can spend 1 ki point to take the Disengage or Dash action. Your jump distance is doubled for the turn.")
```

## Unarmored Movement
*2nd-level monk feature*

Your speed increases by 10 feet while you are not wearing armor or wielding a shield. This bonus increases when you reach certain monk levels, as shown in the Monk table.

At 9th level, you gain the ability to move along vertical surfaces and across liquids on your turn without falling during the move.

```
    def speedadjustment(npc):
        npc.speed['walking'] += (10 if npc.levels('Monk') < 6 else 15 if npc.levels('Monk') < 10 else 20 if npc.levels('Monk') < 14 else 25 if npc.levels('Monk') < 18 else 30)

    npc.defer(lambda npc: speedadjustment(npc))
```

## Ki-fueled Attack
*3rd-level monk optional feature*

If you spend 1 ki point or more as part of your action on your turn, you can make one attack with an unarmed strike or a monk weapon as a bonus action before the end of the turn.

```
def level3(npc):
    npc.bonusactions.append("***Ki-fueled Attack.*** If you spent 1 ki point or more as part of your action, you can make on Unarmed Strike or attack with a monk weapon.")
```

## Monastic Tradition
*3rd-level monk feature*

You commit yourself to a monastic tradition:

* [Ascendant Dragon](AscendantDragon.md)
* [Astral Self](AstralSelf.md)
* [Binding Force](Force.md)
* [Bone](Bone.md)
* [Dragon](Dragon.md)
* [Drunken Master](DrunkenMaster.md)
* [Flesh](Flesh.md)
* [Four Elements](FourElements.md)
* [Kensei](Kensai.md)
* [Long Death](LongDeath.md)
* [Mercy](Mercy.md)
* [Open Hand](OpenHand.md)
* [Shadow](Shadow.md)
* [Soul Knife](SoulKnife.md)
* [Sun Soul](SunSoul.md)
* [Tranquility](Tranquility.md)
* [Weave](Weave.md)

Your tradition grants you features at 3rd level and again at 6th, 11th, and 17th level.

```
def level3(npc):
    # Choose subclass
    (_, subclass) = choose("Choose a Monastic Tradition:", subclasses)
    npc.subclasses[allclasses['Monk']] = subclass
    npc.description.append(subclass.description)
```


## Deflect Missiles
*3rd-level monk feature*

You can use your reaction to deflect or catch the missile when you are hit by a ranged weapon attack. When you do so, the damage you take from the attack is reduced by 1d10 + your Dexterity modifier + your monk level.

If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack with a range of 20/60 using the weapon or piece of ammunition you just caught, as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Deflect Missiles.*** When you are hit by a ranged weapon attack, you deflect or catch the missile, reducing the damage you take from the attack by 1d10 + {npc.DEXbonus() + npc.levels('Monk')}. If you reduce the damage to 0, you can catch the missile if it is small enough for you to hold in one hand and you have at least one hand free. If you catch a missile in this way, you can spend 1 ki point to make a ranged attack using the weapon or piece of ammunition you just caught (*Ranged Weapon Attack* +{npc.proficiencybonus() + npc.DEXbonus()} to hit, range 20/60, one target. Hit: 1d{npc.martialartsdie} + {npc.DEXbonus()} damage of the ammunition's type), as part of the same reaction. You make this attack with proficiency, regardless of your weapon proficiencies, and the missile counts as a monk weapon for the attack.") )
```

## Slow Fall
*4th-level monk feature*

You can use your reaction when you fall to reduce any falling damage you take by an amount equal to five times your monk level.

```
def level4(npc): 
    abilityscoreimprovement(npc)
    npc.defer(lambda npc: npc.reactions.append(f"***Slow Fall.*** Reduce any falling damage you take by {5 * npc.levels('Monk')}."))
```

## Quickened Healing
*4th-level monk optional feature*

As an action, you can spend 2 ki points and roll a Martial Arts die. You regain a number of hit points equal to the number rolled plus your proficiency bonus.

```
    npc.defer(lambda npc: npc.actions.append(f"***Ki: Quickened Healing.*** You can spend 2 ki points and regain 1d{npc.martialartsdie} + {npc.proficiencybonus()} hit points.") )
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Focused Aim
*5th-level monk optional feature*

When you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit. 

```
def level5(npc):
    npc.traits.append("***Ki: Focused Aim.*** When you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit.")
```

## Extra Attack
*5th-level monk feature*

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
    npc.actions.append("***Multiattack.*** You can attack twice whenever you take the Attack action on your turn.")
```

## Stunning Strike
*5th-level monk feature*

You can interfere with the flow of ki in an opponent's body. When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw or be stunned until the end of your next turn.

```
    npc.traits.append("***Ki: Stunning Strike.*** When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a Constitution saving throw (against your Ki save DC) or be stunned until the end of your next turn.")
```

## Ki-Empowered Strikes
*6th-level monk feature*

Your unarmed strikes count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.

## Evasion
*7th-level monk feature*

Your instinctive agility lets you dodge out of the way of certain area effects, such as a blue dragon's lightning breath or a fireball spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.

```
def level7(npc):
    npc.traits.append("***Evasion.*** When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")
```

## Stillness of Mind
*7th-level monk feature*

You can use your action to end one effect on yourself that is causing you to be charmed or frightened.

```
    npc.actions.append("***Stillness of Mind.*** You can end one effect on yourself that is causing you to be charmed or frightened.")
```

## Purity of Body
*10th-level monk feature*

Your mastery of the ki flowing through you makes you immune to disease and poison.

```
def level10(npc):
    npc.traits.append("***Purity of Body.*** You are immune to disease and poison.")
    npc.damageimmunities.append('poison')
    npc.conditionimmunities.append('diseased')
```

## Tongue of the Sun and Moon
*13th-level monk feature*

You learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say.

```
def level13(npc):
    npc.traits.append("***Tongue of the Sun and Moon.*** You learn to touch the ki of other minds so that you understand all spoken languages. Moreover, any creature that can understand a language can understand what you say.")
```

## Diamond Soul
*14th-level monk feature*

Your mastery of ki grants you proficiency in all saving throws.

Additionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result.

```
def level14(npc):
    if 'CON' not in npc.savingthrows: npc.savingthrows.append('CON')
    if 'INT' not in npc.savingthrows: npc.savingthrows.append('INT')
    if 'WIS' not in npc.savingthrows: npc.savingthrows.append('WIS')
    if 'CHA' not in npc.savingthrows: npc.savingthrows.append('CHA')

    npc.traits.append("***Ki: Diamond Soul.*** Whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result.")
```

## Timeless Body
*15th-level monk feature*

Your ki sustains you so that you suffer none of the frailty of old age, and you can't be aged magically. You can still die of old age, however. In addition, you no longer need food or water.

```
def level15(npc):
    npc.traits.append("***Timeless Body.*** You suffer none of the frailty of old age, and cannot be aged magically. In addition, you no longer need food or water.")
```

## Empty Body
*18th-level monk feature*

You can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage.

Additionally, you can spend 8 ki points to cast the Astral Projection spell, without needing material components. When you do so, you can't take any other creatures with you.

```
def level18(npc):
    npc.actions.append(f"***Ki: Empty Body.*** You can spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage. You can spend 8 ki points to cast {spelllinkify('astral projection')} without needing material components; when you do so, you can't take any other creatures with you.")
```

## Perfect Self
*20th-level monk feature*

When you roll for initiative and have no ki points remaining, you regain 4 ki points.

```
def level20(npc):
    npc.traits.append("***Perfect Self.*** When you roll for initiative and have no ki points remaining, you regain 4 ki points.")
```