# Barbarian
Barbarians are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength.

```
name = 'Barbarian'
description = "***Class: Barbarian.*** Barbarians are defined by their rage: unbridled, unquenchable, and unthinking fury. More than a mere emotion, their anger is the ferocity of a cornered predator, the unrelenting assault of a storm, the churning turmoil of the sea. For some, their rage springs from a communion with fierce animal spirits. Others draw from a roiling reservoir of anger at a world full of pain. For every barbarian, rage is a power that fuels not just a battle frenzy but also uncanny reflexes, resilience, and feats of strength."
```

## Class features
As a barbarian, you gain the following class features.

Level|Proficiency Bonus|Rages|Rage Damage|Features
-----|-----------------|-----|-----------|--------
1st  |+2|2|+2|[Rage](#rage), [Unarmored Defense](#unarmored-defense)
2nd	 |+2|2|+2|[Reckless Attack](#reckless-attack)
3rd	 |+2|3|+2|[Primal Path](#primal-path)
4th	 |+2|3|+2|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)
5th	 |+3|3|+2|[Extra Attack](#extra-attack), [Instinctive Pounce](#instinctive-pounce)
6th	 |+3|4|+2|Path feature
7th	 |+3|4|+2|[Feral Instinct](#feral-instinct)
8th	 |+3|4|+2|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
9th	 |+4|4|+3|[Brutal Critical](#brutal-critical) (1 die)
10th |+4|4|+3|Path feature
11th |+4|4|+3|[Relentless Rage](#relentless-rage)
12th |+4|5|+3|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
13th |+5|5|+3|[Brutal Critical](#brutal-critical) (2 dice)
14th |+5|5|+3|Path feature
15th |+5|5|+3|[Persistent Rage](#persistent-rage)
16th |+5|5|+4|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
17th |+6|6|+4|[Brutal Critical](#brutal-critical) (3 dice)
18th |+6|6|+4|[Indomitable Might](#indomitable-might)
19th |+6|6|+4|[Ability Score Improvement](#ability-score-improvement) or [Feat](../../Feats/index.md)	
20th |+6|Unlimited|+4|[Primal Champion](#primal-champion)

### Hit Points
**Hit Dice**: 1d12 per barbarian level

**Hit Points at 1st Level**: 12 + your Constitution modifier

**Hit Points at Higher Levels**: 1d12 (or 7) + your Constitution modifier per barbarian level after 1st

```
def everylevel(npc): npc.hits('d12')
```

### Proficiencies
**Armor**: Light armor, medium armor, shields

**Weapons**: Simple weapons, martial weapons

**Tools**: None

**Saving Throws**: Strength, Constitution

**Skills**: Choose two from Animal Handling, Athletics, Intimidation, Nature, Perception, and Survival

```
def level1(npc):
    for arm in armor['light'] | armor['medium'] | armor['shields']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged'] | weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)

    npc.savingthrows.append("STR")
    npc.savingthrows.append("CON")

    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a greataxe or (b) any martial melee weapon
* (a) two handaxes or (b) any simple weapon
* An explorer's pack and four javelins

```
    npc.equipment.append("Greataxe OR any martial melee weapon")
    npc.equipment.append("Two handaxes OR any simple weapon")
    npc.equipment.append("Four javelins")
    npc.equipment.append("An explorer's pack")
```

## Rage
*1st-level barbarian feature*

In battle, you fight with primal ferocity. On your turn, you can enter a rage as a bonus action.

While raging, you gain the following benefits if you aren't wearing heavy armor:

* You have advantage on Strength checks and Strength saving throws.
* When you make a melee weapon attack using Strength, you gain a bonus to the damage roll that increases as you gain levels as a barbarian, as shown in the Rage Damage column of the Barbarian table.
* You have resistance to bludgeoning, piercing, and slashing damage.

If you are able to cast spells, you can't cast them or concentrate on them while raging.

Your rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends, and you haven't attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action.

Once you have raged the number of times shown for your barbarian level in the Rages column of the Barbarian table, you must finish a long rest before you can rage again.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Rage ({2 if npc.levels(name) < 3 else 3 if npc.levels(name) < 6 else 4 if npc.levels(name) < 12 else 5 if npc.levels(name) < 17 else 6}/Recharges on long rest).*** Your rage lasts for 1 minute. {'It ends early if you fall unconscious or if your turn ends and you have not attacked a hostile creature since your last turn or taken damage since then.' if npc.levels(name) < 15 else 'It ends early if you fall unconscious.'} You can end your rage on your turn as a bonus action. {'' if npc.levels(name) < 7 else ' You can move up to half your speed as part of this bonus action. '}If you aren't wearing heavy armor, you gain the following benefits: You have advantage on Strength checks and Strength saving throws; When you make a melee weapon attack using Strength, you gain a +{2 if npc.levels(name) < 9 else 3 if npc.levels(name) < 16 else 4} bonus to the damage roll; You have resistance to bludgeoning, piercing, and slashing damage.") )
```

## Unarmored Defense
*1st-level barbarian feature*

While you are not wearing any armor, your armor class equals 10 + your Dexterity modifier + your Constitution modifier. You can use a shield and still gain this benefit.

```
    def unarmoreddefense(npc): 
        npc.armorclass['Unarmored Defense'] = 10 + npc.DEXbonus() + npc.CONbonus()

    npc.defer(lambda npc: unarmoreddefense(npc))
```

## Survival Instincts
*2nd-level barbarian feature* 

You become proficient in your choice of two of the following skills: Animal Handling, Medicine, Nature, Perception, or Survival.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills.

```
def level2(npc):
    skill = choose("Choose a Survival Instinct: ", ['Animal Handling', 'Medicine', 'Nature', 'Perception', 'Survival'])
    npc.expertises.append(skill)
    skill = choose("Choose a Survival Instinct: ", ['Animal Handling', 'Medicine', 'Nature', 'Perception', 'Survival'])
    npc.expertises.append(skill)
```

## Reckless Attack
*2nd-level barbarian feature* 

You can throw aside all concern for defense to attack with fierce desperation. When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.

```
    npc.actions.append("***Reckless Attack.*** When you make your first attack on your turn, you can decide to attack recklessly. Doing so gives you advantage on melee weapon attack rolls using Strength during this turn, but attack rolls against you have advantage until your next turn.")
```

## Primal Knowledge
*3rd-level optional barbarian feature*

When you reach 3rd level and again at 10th level, you gain proficiency in one skill of your choice from the list of skills available to barbarians at 1st level.

```
def level3(npc):
    chooseskill(npc, ['Animal Handling','Athletics','Intimidation','Nature','Perception','Survival'])
```

## Primal Path
At 3rd level, you choose a path that shapes the nature of your rage:

* [Ancestral Guardian](./AncestralGuardian.md)
* [Beast](./Beast.md)
* [Berserker](./Berserker.md)
* [Blood Drinker](./BloodDrinker.md)
* [Dead](./Dead.md)
* [Depths](./Depths.md)
* [Dragon](./Dragon.md)
* [Rage Mage](./RageMage.md)
* [Storm Herald](./StormHerald.md)
* [Totem Warrior](./TotemWarrior.md)
* [Were-Beast](./Werebeast.md)
* [Wild Magic](./WildMagic.md)
* [Zealot](./Zealot.md)

Your choice grants you features at 3rd level and again at 6th, 10th, and 14th levels.

```
    (_, subclass) = choose("Choose a Primal Path: ", subclasses)
    npc.subclasses[allclasses[name]] = subclass
    npc.description.append(subclass.description)
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Extra Attack
*5th-level barbarian feature* 

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
def level5(npc):
    npc.actions.append("***Multiattack.*** You can attack twice, instead of once, whenever you take the Attack action on your turn.")
```

## Instinctive Pounce
*5th-level barbarian feature*

When a creature ends its turn within 15 feet of you, you can use your reaction to move up to half your speed to a space closer to the creature. This movement doesn't provoke opportunity attacks.

```
    npc.reactions.append("***Instinctive Pounce.*** When a creature ends its turn within 15 feet of you, you move up to half your speed to a space closer to the creature. This movement doesn't provoke opportunity attacks.")
```

## Feral Instinct
*7th-level barbarian feature*

Your instincts are so honed that you have advantage on initiative rolls.

Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.

```
def level7(npc):
    npc.traits.append("***Feral Instinct.*** You have advantage on initiative rolls. Additionally, if you are surprised at the beginning of combat and aren't incapacitated, you can act normally on your first turn, but only if you enter your rage before doing anything else on that turn.")
```

## Instinctive Pounce
*7th-level optional barbarian feature*

As part of the bonus action you take to enter your rage, you can move up to half your speed. 

## Brutal Critical
*9th-level barbarian feature*

Beginning at 9th level, you can roll one additional weapon damage die when determining the extra damage for a critical hit with a melee attack.

This increases to two additional dice at 13th level and three additional dice at 17th level.

```
def level9(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Brutal Critical.*** You roll {'one' if npc.levels(name) < 13 else 'two' if npc.levels(name) < 17 else 'three'} additional weapon damage {'die' if npc.levels(name) < 13 else 'dice'} when determining the extra damage for a critical hit with a melee attack.") )
```

## Relentless Rage
*11th-level barbarian feature*

Your rage can keep you fighting despite grievous wounds. If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead.

Each time you use this feature after the first, the DC increases by 5. When you finish a short or long rest, the DC resets to 10.

```
def level11(npc):
    npc.traits.append("***Relentless Rage (Resets on short or long rest).*** If you drop to 0 hit points while you're raging and don't die outright, you can make a DC 10 Constitution saving throw. If you succeed, you drop to 1 hit point instead. Each time you use this feature after the first, the DC increases by 5.")
```

## Persistent Rage
*15th-level barbarian feature*

Your rage is so fierce that it ends early only if you fall unconscious or if you choose to end it.

## Indomitable Might
*18th-level barbarian feature*

If your total for a Strength check is less than your Strength score, you can use that score in place of the total.

```
def level18(npc):
    npc.traits.append("***Indomitable Might.*** If your total for a Strength check is less than your Strength score, you can use that score in place of the total.")
```

## Primal Champion
*20th-level barbarian feature*

You embody the power of the wilds. Your Strength and Constitution scores increase by 4. Your maximum for those scores is now 24.

```
def level20(npc):
    npc.STR += 4
    npc.CON += 4
```