# Fighter Martial Archetype: Samurai
The Samurai is a fighter who draws on an implacable fighting spirit to overcome enemies. A samurai's resolve is nearly unbreakable, and the enemies in a samurai's path have two choices: yield or die fighting.

The *samurai* were originally a tribe of fighters of the Hordes who were well known among their enemies as being particularly difficult to fight. Over time, the *samurai* (or, in their original tongue, Samam'ur'hai) came to be respected by their foes both for their implacable will and their sense of honor regarding defeated enemies. After some years, several of their mortal opponents took up the same credo, adopting the name of that tribe in homage, and the two sides found kinship in their shared code. In time, the Samam'ur'hai were wiped out during the Yithi Campaigns, but by then the tradition had taken root, and served as the foundations for what would later come to be known as the [Mercenary Code](../../Organizations/MercCompanies/Code.md).

Many in the west who follow the code of the *samurai* have no idea that they do so in homage to that Hordish tribe.

Many of the [dueling colleges](../../Organizations/DuelingCollege.md) in [Yithi](../../Nations/Yithi.md) and [Zhi](../../Nations/Zhi.md) provide instruction in the way of the *samurai*, and several schools in [Liria](../../Nations/Liria.md) and [Travenia](../../Nations/Travenia.md) are openly accepting teachers of it as well.

```
name = 'Samurai'
def level3(npc):
    npc.description.append("***Subclass: Samurai.*** The Samurai is a fighter who draws on an implacable fighting spirit to overcome enemies. A samurai's resolve is nearly unbreakable, and the enemies in a samurai's path have two choices: yield or die fighting.")
```

## Bonus Proficiency
*3rd-level Samurai feature*
When you choose this archetype at 3rd level, you gain proficiency in one of the following skills of your choice: History, Insight, Performance, or Persuasion. Alternatively, you learn one language of your choice.

```
    npc.skills.append(choose("Choose a proficiency: ", ['History', 'Insight', 'Performance', 'Persuasion']))
```

## Fighting Spirit
*3rd-level Samurai feature*
Your intensity in battle can shield you and help you strike true. As a bonus action on your turn, you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain 5 temporary hit points. The number of hit points increases when you reach certain levels in this class, increasing to 10 at 10th level and 15 at 15th level.

You can use this feature three times. You regain all expended uses of it when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Fighting Spirit (3/Recharges on long rest).*** you can give yourself advantage on all weapon attack rolls until the end of the current turn. When you do so, you also gain {5 if npc.levels('Fighter') < 10 else 10 if npc.levels('Fighter') < 15 else 15} temporary hit points."))
```

## Elegant Courtier
*7th-level Samurai feature*
Your discipline and attention to detail allow you to excel in social situations. Whenever you make a Charisma (Persuasion) check, you gain a bonus to the check equal to your Wisdom modifier.

Your self-control also causes you to gain proficiency in Wisdom saving throws. If you already have this proficiency, you instead gain proficiency in Intelligence of Charisma saving throws (your choice).

```
def level7(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Elegant Courier.*** Whenever you make a Charisma (Persuasion) check, you gain a +{npc.WISbonus()} bonus."))

    if 'WIS' in npc.savingthrows:
        npc.savingthrows.append("Choose a saving throw: ", ['INT', 'CHA'])
    else:
        npc.savingthrows.append('WIS')
```

## Tireless Spirit
*10th-level Samurai feature*
When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use.

```
def level10(npc):
    npc.traits.append("***Tireless Spirit.*** When you roll initiative and have no uses of Fighting Spirit remaining, you regain one use.")
```

## Rapid Strike
*15th-level Samurai feature*
You learn to trade accuracy for swift strikes. If you take the Attack action on your turn and have advantage on an attack roll against against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn.

```
def level15(npc):
    npc.traits.append("***Rapid Strike.*** If you take the Attack action on your turn and have advantage on an attack roll against against one of the targets, you can forgo the advantage for that roll to make an additional weapon attack against that target, as part of the same action. You can do so no more than once per turn.")
```

## Strength Before Death
*18th-level Samurai feature*
Your fighting spirit can delay the grasp of death. If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level18(npc):
    npc.reactions.append("***Strength Before Death (Recharges on long rest).*** If you take damage that reduces you to 0 hit points, you can use your reaction to delay falling unconscious, and you can immediately take an extra turn. While you have 0 hit points during that extra turn, taking damage causes death saving throw failures as normal, and three death saving throw failures can still kill you. When the extra turn ends, you fall unconscious if you still have 0 hit points.")
```
