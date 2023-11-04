# Monastic Tradition: Way of the Weave
The Weave is a fabric of magic that underlies the planes and is arguably the source of power for all arcane magic. Monks of the Way of the Weave have, through their manipulation of ki, discovered how to tap into the Weave and channel its energy to cast spells. While many monks use this deep understanding of the Weave to explore the secrets of the multiverse, some Way of the Weave monks choose to wield this arcane power against their foes.

This is probably one of the most public of the monastic traditions in Azgaarnoth, as nearly all of the [mage schools](../../Organizations/MageSchools/index.md) make use of Weave monks as bodyguards, assistants, and companions. It is not entirely clear what the monks get out of the partnership, however, though speculation is rife. To join one of the Weave monks, however, is simple: walk up to any Weave monk, ask how to join, and instructions will be made clear (usually a small quest to test the sincerity of the request, followed by directions to a monastery somewhere on the continent). Regardless of whatever other agreements mage schools have with Weave monks, the one consistent factor is that the Way of the Weave is always open to new students, of any race, at any time. It is for this reason, as well, that any race found anywhere on Azgaarnoth can be accepted as a Weave monk--human, Firstborn, Created, Horde, even Undersea, all are welcome, embraced, and taught.

## Spellcasting
*3rd-level Way of the Weave feature*

You gain the ability to cast spells from the sorcerer spell list.

**Way of the Weave Spellcasting**

Level|Cantrips Known|Spells Known|1st|2nd|3rd|4th
-----|--------------|------------|---|---|---|---
3rd  | 2| 3 | 2| --| --| --
4th  | 2| 4 | 3| --| --| --
5th  | 2| 4 | 3| --| --| --
6th  | 2| 4 | 3| --| --| --
7th  | 2| 5 | 4| 2| --| --
8th  | 2| 6 | 4| 2| --| --
9th  | 2| 6 | 4| 2| --| --
10th | 3| 7 | 4| 3| --| --
11th | 3| 8 | 4| 3| --| --
12th | 3| 8 | 4| 3| --| --
13th | 3| 9 | 4| 3| 2| --
14th | 3|10 | 4| 3| 2| --
15th | 3|10 | 4| 3| 2| --
16th | 3|11 | 4| 3| 3| --
17th | 3|11 | 4| 3| 3| --
18th | 3|11 | 4| 3| 3| --
19th | 3|12 | 4| 3| 3| 1
20th | 3|13 | 4| 3| 3| 1

### Cantrips
You learn two cantrips of your choice from the sorcerer spell list. At 10th level you learn another cantrip from the sorcerer spell list.

### Spell Slots
The Way of the Weave Spellcasting table shows how many spell slots you have to cast your spells of 1st-level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. 

### Spells Known of 1st-Level and Higher
You know three 1st-level sorcerer spells of your choice, two of which must be from the evocation or transmutation spells on the sorcerer spell list.

The Spells Known column of the Way of the Weave Spellcasting table shows when you learn more sorcerer spells of 1st level or higher. Each of these spells must be an evocation or transmutation spell of your choice and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the sorcerer spells you know with another spell of your choice from the sorcerer spell list. The new spell must be of a level for which you have spell slots, and it must be an evocation or transmutation spell, unless you're replacing the spell you gained at 8th, 14th, or 20th level.

### Spellcasting Ability
Wisdom is your spellcasting ability for your sorcerer spells, since you learn your spells through repeated meditation and enlightenment. You use your Wisdom whenever a spell refers to your spellcasting ability.

In addition, you use your Wisdom modifier when setting the saving throw DC for a sorcerer spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

```
def level3(npc):
    spellcasting = halfcaster(npc, 'WIS', 'Way of the Weave')
    spellcasting.casterclass = allclasses['Monk']
    spellcasting.maxcantripsknown = 2
    spellcasting.maxspellsknown = 3
    spellcasting.spellsknown = ['CHOOSE-Evocation/Transmutation Sorcerer', 'CHOOSE-Evocation/Transmutation Sorcerer', 'CHOOSE-Sorcerer']
```


## Flurry of Spells
*6th-level Way of the Weave feature*

Immediately after you use your action to cast a cantrip on your turn, you can spend 1 ki point to make two Unarmed Strikes as a bonus action.

```
def level6(npc):
    npc.bonusactions.append("***Ki: Flurry of Spells.*** Immediately after you use your action to cast a cantrip on your turn, you can spend 1 ki point to make two Unarmed Strikes.")
```

## Weave-Infused Ki
*11th-level Way of the Weave feature*

You can transform your ki points into one spell slot as a bonus action on your turn. The created spell slots vanish at the end of a long rest. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 4th.

**Creating Spell Slots**

Spell Slot Level|Ki Point Cost
----------------|-------------
1st| 2
2nd| 3
3rd| 5
4th| 6

```
def level11(npc):
    npc.bonusactions.append("***Ki: Weave-Infused Ki.*** You can transform 2 ki points into a 1st-level spell slot, 3 into a 2nd, 5 into a 3rd, or 6 into a 4th.")
```

## Spell Strike
*17th-level Way of the Weave feature*

When you hit another creature with a melee weapon attack, you can spend a number of ki points equal to the amount shown on the Creating Spell Slots table to cast a spell of the corresponding level. You do not need to expend a spell slot to do this.

The struck creature serves as the point of origin for the spell. The target automatically fails the saving throw for the spell, if it has one, but any other creature that would be effected by the spell is entitled to the appropriate saving throws.

```
def level17(npc):
    npc.actions.append("***Spell Strike.*** When you hit another creature with a melee weapon attack, you can spend a number of ki points (as described by Weave-Infused Ki) to cast a spell of that level without needing to expend a spell slot to do this. The struck creature serves as the point of origin for the spell. The target automatically fails the saving throw for the spell, if it has one, but any other creature that would be effected by the spell is entitled to the appropriate saving throws.")
```
