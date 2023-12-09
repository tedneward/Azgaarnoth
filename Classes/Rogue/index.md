# Rogue
Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful adventuring party.

```
name = 'Rogue'
description = "***Class: Rogue.*** Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful adventuring party."
```

*You must have a Dexterity score of 13 or higher in order to multiclass in or out of this class.*

Level|Proficiency Bonus|Sneak Attack|Features
-----|-----------------|------------|--------
1st  |+2|1d6|[Expertise](#expertise), [Sneak Attack](#sneak-attack), [Thieves' Cant](#thieves-cant)
2nd  |+2|1d6|[Cunning Action](#cunning-action)
3rd  |+2|2d6|[Roguish Archetype](#roguish-archetype)
4th  |+2|2d6|[Ability Score Improvement](#ability-score-improvement)
5th  |+3|3d6|[Uncanny Dodge](#uncanny-dodge)
6th  |+3|3d6|[Expertise](#expertise)
7th  |+3|4d6|[Evasion](#evasion)
8th  |+3|4d6|[Ability Score Improvement](#ability-score-improvement)
9th  |+4|5d6|[Roguish Archetype feature](#roguish-archetype)
10th |+4|5d6|[Ability Score Improvement](#ability-score-improvement)
11th |+4|6d6|[Reliable Talent](#reliable-talent)
12th |+4|6d6|[Ability Score Improvement](#ability-score-improvement)
13th |+5|7d6|[Roguish Archetype feature](#roguish-archetype)
14th |+5|7d6|[Blindsense](#blindsense)
15th |+5|8d6|[Slippery Mind](#slippery-mind)
16th |+5|8d6|[Ability Score Improvement](#ability-score-improvement)
17th |+6|9d6|[Roguish Archetype feature](#roguish-archetype)
18th |+6|9d6|[Elusive](#elusive)
19th |+6|10d6|[Ability Score Improvement](#ability-score-improvement)
20th |+6|10d6|[Stroke of Luck](#stroke-of-luck)

As a rogue, you gain the following class features.

## Hit Points
**Hit Dice**: 1d8 per rogue level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per rogue level after 1st

```
def everylevel(npc): npc.hits('d8')
```

## Proficiencies
**Armor**: Light armor

**Weapons**: Simple weapons, hand crossbows, longswords, rapiers, shortswords

**Tools**: Thieves' tools

**Saving Throws**: Dexterity, Intelligence

**Skills**: Choose four from Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation, Perception, Performance, Persuasion, Sleight of Hand, and Stealth

```
def level1(npc):
    for arm in armor['light']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)
    npc.proficiencies.append('Hand crossbow')
    npc.proficiencies.append('Longsword')
    npc.proficiencies.append('Rapier')
    npc.proficiencies.append('Shortsword')
    npc.proficiencies.append("Thieves' tools")

    npc.savingthrows.append('DEX')
    npc.savingthrows.append('INT')

    thiefskills = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']
    chooseskill(npc, thiefskills)
    chooseskill(npc, thiefskills)
    chooseskill(npc, thiefskills)
    chooseskill(npc, thiefskills)
```

## Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a rapier or (b) a shortsword
* (a) a shortbow and quiver of 20 arrows or (b) a shortsword
* (a) a burglar's pack, (b) dungeoneer's pack, or (c) an explorer's pack
* Leather armor, two daggers, and thieves' tools

```
    npc.equipment.append("Rapier OR shortsword")
    npc.equipment.append("Shortbow and 20 arrows")
    npc.equipment.append("Burglar's pack, dungeoneer's pack, or explorer's pack")
    npc.armorclass['Leather armor'] = 11
    npc.equipment.append("2 daggers")
    npc.equipment.append("Thieves' tools")
```

## Thieves' Cant
*1st-level rogue feature*

During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly.

In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.

```
    npc.languages.append("Thieves' Cant")
```

## Sneak Attack
*1st-level rogue feature*

You know how to strike subtly and exploit a foe's distraction. Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon.

You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.

The amount of the extra damage increases as you gain levels in this class, as shown in the Sneak Attack column of the Rogue table.

```
    # Sneak Attack
    npc.defer(lambda npc: npc.traits.append(f"***Sneak Attack.*** Once per turn, you can deal an extra {(npc.levels(name) + 1) // 2}d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll."))
```


## Expertise
*1st-level rogue feature*

Choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.

At 6th level, you can choose two more of your proficiencies (in skills or with thieves' tools) to gain this benefit.

```
    # Expertise
    exp1 = choose("Choose an Expertise: ", npc.skills + ["Thieves' Tools"])
    exp2 = choose("Choose an Expertise: ", npc.skills + ["Thieves' Tools"])
    npc.expertises = [ exp1, exp2 ]

def level6(npc):
    exp1 = choose("Choose an Expertise: ", npc.skills + ["Thieves' Tools"])
    exp2 = choose("Choose an Expertise: ", npc.skills + ["Thieves' Tools"])
    npc.expertises += [ exp1, exp2 ]
```

## Cunning Action
*2nd-level rogue feature*

Your quick thinking and agility allow you to move and act quickly. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action.

You may also your Cunning Action to carefully aim your next attack. As a bonus action, you give yourself advantage on your next attack roll on the current turn. You can use this bonus action only if you haven't moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.

```
def level2(npc):
    npc.bonusactions.append("***Cunning Action.*** You can take a bonus action on each of your turns in combat to take the Dash, Disengage, or Hide action. You may also your Cunning Action to carefully aim your next attack. As a bonus action, you give yourself advantage on your next attack roll on the current turn. You can use this bonus action only if you haven't moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.")
```

## Roguish Archetype
*3rd-level rogue feature*

You choose an archetype that you emulate in the exercise of your rogue abilities:

* [Arcane Trickster](ArcaneTrickster.md)
* [Assassin](Assassin.md)
* [Burglar](Burglar.md)
* [Inquisitive](Inquisitive.md)
* [Inquisitor](Inquisitor.md)
* [Mastermind](Mastermind.md)
* [Phantom](Phantom.md)
* [Scout](Scout.md)
* [Serpent Assassin](SerpentAssassin.md)
* [Soulknife](Soulknife.md)
* [Swashbuckler](Swashbuckler.md)
* [Thief](Thief.md)
* [Thought Eater](ThoughtEater.md)
* [Trapper](Trapper.md)

Your archetype choice grants you features at 3rd level and then again at 9th, 13th, and 17th level.

```
def level3(npc):
    (_, subclass) = choose("Choose a subclass: ", subclasses)
    npc.subclasses[allclasses['Rogue']] = subclass
    npc.description.append(subclass.description)
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 10th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level10(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Uncanny Dodge
*5th-level rogue feature*

When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you.

```
def level5(npc):
    npc.reactions.append("***Uncanny Dodge.*** When an attacker that you can see hits you with an attack, you can halve the attack's damage against you.")
```

## Evasion
*7th-level rogue feature*

You can nimbly dodge out of the way of certain area effects, such as a red dragon's fiery breath or an [ice storm]() spell. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.

```
def level7(npc):
    npc.traits.append("***Evasion.*** When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")
```

## Reliable Talent
*11th-level rogue feature*

You have refined your chosen skills until they approach perfection. Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.

```
def level11(npc):
    npc.traits.append("***Reliable Talent.*** Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.")
```

## Blindsense
*14th-level rogue feature*

If you are able to hear, you are aware of the location of any hidden or invisible creature within 10 feet of you.

```
def level14(npc):
    npc.senses['blindsense'] = 10
```

## Slippery Mind
*15th-level rogue feature*

You have acquired greater mental strength. You gain proficiency in Wisdom saving throws.

```
def level15(npc):
    npc.savingthrows.append('WIS')
```

## Elusive
*18th-level rogue feature*

You are so evasive that attackers rarely gain the upper hand against you. No attack roll has advantage against you while you aren't incapacitated.

```
def level18(npc):
    npc.traits.append("***Elusive.*** No attack roll has advantage against you while you aren't incapacitated.")
```

## Stroke of Luck
*20th-level rogue feature*

You have an uncanny knack for succeeding when you need to. If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level20(npc):
    npc.traits.append("***Stroke of Luck (Recharges on short or long rest).*** If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20.")
```
