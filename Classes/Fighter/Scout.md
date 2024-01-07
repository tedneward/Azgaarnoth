# Martial Archetype: Scout
The archetypal scout excels at finding safe passage through dangerous regions. Scouts usually favor light armor and ranged weapons, but they are comfortable using heavier gear when faced with intense fighting.

```
name = 'Scout'
description = "***Martial Archetype: Scout.*** The archetypal scout excels at finding safe passage through dangerous regions. Scouts usually favor light armor and ranged weapons, but they are comfortable using heavier gear when faced with intense fighting."
```

## Bonus Proficiencies
*3rd-level Scout feature*

You gain proficiency in three of the following skills of your choice: Acrobatics, Athletics, Investigation, Medicine, Nature, Perception, Stealth, or Survival. You can choose to gain proficiency with thieves' tools in place of one skill choice.

```
def level3(npc):
    npc.proficiencies.append(choose("Choose a proficiency: ", ['Acrobatics', 'Athletics', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Stealth', 'Survival', "Thieves' tools"]))
    npc.proficiencies.append(choose("Choose a proficiency: ", ['Acrobatics', 'Athletics', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Stealth', 'Survival', "Thieves' tools"]))
    npc.proficiencies.append(choose("Choose a proficiency: ", ['Acrobatics', 'Athletics', 'Investigation', 'Medicine', 'Nature', 'Perception', 'Stealth', 'Survival', "Thieves' tools"]))
```

## Combat Superiority
*3rd-level Scout feature*

You gain a set of abilities that are fueled by special dice called superiority dice.

***Superiority Dice.*** You have four superiority dice, which are d8s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a long or short rest.

You gain another superiority die at 7th level and one more at 15th level.

Using Superiority Dice. You can expend superiority dice to gain a number of different benefits:

* **Survival Superiority**. When you make a check that allows you to apply your proficiency in Athletics, Nature, Perception, Stealth, or Survival, you can expend one superiority die to bolster the check. Add half the number rolled on the superiority die (rounding up) to your check. You apply this bonus after making the check but before learning if it was successful.

* **Precision Attack**. When you make a weapon attack against a creature, you can expend one superiority die to add it to the attack roll. You can use this ability before or after making the attack roll, but before any of the effects of the attack are applied.

* **Scout's Evasion**. If you are hit by an attack while wearing light or medium armor, you can expend one superiority die as a reaction, adding the number rolled to your AC. If the attack still hits, you take half damage from it.

```
    npc.superioritydicetype = 'd8'
    npc.superioritydice = 4

    npc.defer(lambda npc: npc.traits.append(f"***Superiority Dice (Recharges on short or long rest).*** You have {npc.superioritydice} superiority dice, which are {npc.superioritydicetype}s.{' When you roll initiative and have no superiority dice remaining, you regain one superiority die.' if npc.levels('Fighter') >= 15 else ''}"))

    npc.traits.append("***Superiority Dice: Survival Superiority.*** When you make a check that allows you to apply your proficiency in Athletics, Nature, Perception, Stealth, or Survival, you can expend one superiority die to bolster the check. Add half the number rolled on the superiority die (rounding up) to your check. You apply this bonus after making the check but before learning if it was successful.")

    npc.traits.append("***Superiority Dice: Precision Attack**. When you make a weapon attack against a creature, you can expend one superiority die to add it to the attack roll. You can use this ability before or after making the attack roll, but before any of the effects of the attack are applied.")

    npc.traits.append("***Superiority Dice: Scout's Evasion.*** If you are hit by an attack while wearing light or medium armor, you can expend one superiority die as a reaction, adding the number rolled to your AC. If the attack still hits, you take half damage from it.")
```

## Natural Explorer
*3rd-level Scout feature*

You are a master of navigating the natural world, and you react with swift and decisive action when attacked. This grants you the following benefits:

* You ignore difficult terrain.

* You have advantage on initiative rolls.

* On your first turn during combat, you have advantage on attack rolls against creatures that have not yet acted.

In addition, you are skilled at navigating the wilderness. You gain the following benefits when traveling for an hour or more:

* Difficult terrain doesn't slow your group's travel.

* Your group can't become lost except by magical means.

* Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger. You always have advantage on Perception checks when attempting to perceive danger.

* If you are traveling alone, you can move stealthily at a normal pace.

* When you forage, you find twice as much food as you normally would.

* While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.

```
def level3(npc):
    npc.traits.append("***Natural Explorer: Strider.*** You ignore difficult terrain.")
    npc.traits.append("***Natural Explorer: Alert.*** You have advantage on initiative rolls.")
    npc.traits.append("***Natural Explorer: Striker.*** On your first turn during combat, you have advantage on attack rolls against creatures that have not yet acted.")
    npc.traits.append("***Natural Explorer: Navigator.*** Difficult terrain doesn't slow your group's travel. Your group can't become lost except by magical means. Even when you are engaged in another activity while traveling (such as foraging, navigating, or tracking), you remain alert to danger. You always have advantage on Perception checks when attempting to perceive danger. If you are traveling alone, you can move stealthily at a normal pace. When you forage, you find twice as much food as you normally would. While tracking other creatures, you also learn their exact number, their sizes, and how long ago they passed through the area.")
```

## Improved Combat Superiority
*10th-level Scout feature*

Your superiority dice turn into d10s. At 18th level, they turn into d12s.

```
def level10(npc):
    npc.superioritydicetype = 'd10'
def level18(npc):
    npc.superioritydicetype = 'd12'
```

## Relentless
*15th-level Scout feature*

When you roll initiative and have no superiority dice remaining, you regain 1 superiority die.
