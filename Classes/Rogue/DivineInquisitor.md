# Roguish Archetype: Divine Inquisitor
Grim and determined, the inquisitor roots out enemies of the faith and faithful ─ both mundane and supernatural, using trickery and guile when righteousness and purity is not enough. Although inquisitors are dedicated to a deity, they are above many of the normal rules and conventions of the church. They answer to their deity and their own sense of justice alone, and are willing to take extreme measures to meet their goals.

Inquisitors tend to move from place to place, chasing down enemies and researching emerging threats. As a result, they often travel with others, if for no other reason than to mask their presence. Inquisitors work with members of their faith whenever possible, but even such allies are not above suspicion.

An inquisitor is often seen as a divine assassin, an exorcist, and a heretic hunter, but they can be so much more.

```
name = 'Divine Inquisitor'
description = "***Roguish Archetype: Divine Inquisitor.*** Grim and determined, the inquisitor roots out enemies of the faith and faithful ─ both mundane and supernatural, using trickery and guile when righteousness and purity is not enough. Although inquisitors are dedicated to a deity, they are above many of the normal rules and conventions of the church. They answer to their deity and their own sense of justice alone, and are willing to take extreme measures to meet their goals."
```

## Bonus Proficiencies
*3rd-level Divine Inquisitor feature*

You gain proficiency with heavy crossbows, whips, and Religion.

```
def level3(npc):
    npc.proficiencies.append("Heavy crossbow")
    npc.proficiencies.append("Whip")
    npc.skills.append("Religion")
```

## Channel Divinity: Judgment
*3rd-level Divine Inquisitor feature*

You gain the following Channel Divinity option.

When you use your Channel Divinity, you must finish a short or long rest to use your Channel Divinity again.

***Judgment.*** As a bonus action, you present your holy symbol and pronounce judgment upon your foes. One target of your choice that you can see within 60 feet of you becomes the target of your Judgment, and is branded with a faintly glowing sign reminiscent to your deity's holy symbol.

For 1 minute, against the target of your Judgment, you don't need advantage on your attack roll or an enemy of the target within 5 feet of it to use your Sneak Attack. The extra damage from your Sneak Attack against the target of your Judgment is radiant damage (unless another type of damage would be more appropriate for your diety). All the other rules for the Sneak Attack class feature still apply to you.

```
    npc.bonusactions.append("***Channel Divinity: Judgment.*** You present your holy symbol and pronounce judgment upon your foes. One target of your choice that you can see within 60 feet of you becomes the target of your Judgment, and is branded with a faintly glowing sign reminiscent to your deity's holy symbol. For 1 minute, against the target of your Judgment, you don't need advantage on your attack roll or an enemy of the target within 5 feet of it to use your Sneak Attack. The extra damage from your Sneak Attack against the target of your Judgment is radiant damage. All the other rules for the Sneak Attack class feature still apply to you.")
```

## Spellcasting
*3rd-level Divine Inquisitor feature*

You gain the ability to cast spells according to the table below.

Class Level|Cantrips Known|Spells Known|1st|2nd|3rd|4th
-----------|--------------|------------|---|---|---|---
3rd|3|3|2|─|─|─
4th|3|4|3|─|─|─ 
5th|3|4|3|─|─|─ 
6th|3|4|3|─|─|─ 
7th|3|5|4|2|─|─ 
8th|3|6|4|2|─|─ 
9th|3|6|4|2|─|─ 
10th|4|7|4|3|─|─ 
11th|4|8|4|3|─|─ 
12th|4|8|4|3|─|─ 
13th|4|9|4|3|2|─ 
14th|4|10|4|3|2|─ 
15th|4|10|4|3|2|─ 
16th|4|11|4|3|3|─ 
17th|4|11|4|3|3|─ 
18th|4|11|4|3|3|─ 
19th|4|12|4|3|3|1 
20th|4|13|4|3|3|1

### Cantrips
You learn Vicious Mockery as a cleric cantrip, and two cantrips of your choice from the cleric spell list.

You learn another cleric cantrip of your choice at 10th level.

### Spells Known of 1st-Level and Higher
You know three 1st-level cleric spells of your choice, two of which you must choose from the abjuration and divination spells on the cleric spell list. The Spells column of the Inquisitor Spellcasting table shows when you learn more cleric spells of 1st level or higher. Each of these spells must be an abjuration or divination spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level. The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the cleric spells you know with another spell of your choice from the cleric spell list. The new spell must be of a level for which you have spell slots, and it must be an abjuration or divination spell, unless you're replacing the spell you gained at 8th, 14th, or 20th level.

### Spellcasting Ability.
Wisdom is your spellcasting ability for your cleric spells, since you learn your spells through conviction and prayer. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier.

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier.

### Ritual Casting
You can cast a cleric spell you know as a ritual if that spell has the ritual tag.

### Spellcasting Focus
You use a holy symbol as a spellcasting focus for your cleric spells.

```
    spellcasting = halfcaster(npc, 'WIS', name)
    spellcasting.casterclass = allclasses['Rogue']

    spellcasting.cantripsknown.append("mage hand")
    spellcasting.maxcantripsknown = 3
    spellcasting.maxspellsknown = 3

    spellcasting.cantripsknown.append("vicious mockery")
    spellcasting.maxcantripsknown = 3
    spellcasting.maxspellsknown = 3

def level4(npc):
    npc.spellcasting[name].maxspellsknown = 4

def level7(npc):
    npc.spellcasting[name].maxspellsknown = 5

def level8(npc):
    npc.spellcasting[name].maxspellsknown = 6

def level10(npc):
    npc.spellcasting[name].maxcantripsknown = 4
    npc.spellcasting[name].maxspellsknown = 7

def level11(npc):
    npc.spellcasting[name].maxspellsknown = 8

def level13(npc):
    npc.spellcasting[name].maxspellsknown = 9

def level14(npc):
    npc.spellcasting[name].maxspellsknown = 10

def level16(npc):
    npc.spellcasting[name].maxspellsknown = 11

def level19(npc):
    npc.spellcasting[name].maxspellsknown = 12

def level20(npc):
    npc.spellcasting[name].maxspellsknown = 13
```

## Occult Lore
*9th-level Divine Inquisitor feature*

Your knowledge of the occult gives you an edge in revealing threats to your faith and society. You have advantage on Insight and Investigation checks to reveal the deception and disguises of fey, fiends, shapechangers, and undead, as well as heretics (subject to DM discretion).

```
def level9(npc):
    npc.traits.append("***Occult Lore.*** You have advantage on Insight and Investigation checks to reveal the deception and disguises of fey, fiends, shapechangers, and undead, as well as heretics (subject to DM discretion).")
```

## Greater Judgment
*13th-level Divine Inquisitor feature*

Your Judgment grows stronger and you ignore any damage resistances the target of your judgment might have, and treat any of its damage immunities as damage resistances instead. This ability does not overlap with itself. Also, you can now use your Judgment even if you don't have a line of sight to your target, as long as you know the target's location.

In addition, if your target is invisible or shapechanged when you use the Judgment, it must make a Wisdom saving throw at the start of each of its turns. On a failure either effect is suppressed until the Judgment ends, and the target cannot turn invisible or change shape for the duration.

```
def level13(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Greater Judgment.*** Your Judgment grows stronger and you ignore any damage resistances the target of your judgment might have, and treat any of its damage immunities as damage resistances instead. This ability does not overlap with itself. Also, you can now use your Judgment even if you don't have a line of sight to your target, as long as you know the target's location. In addition, if your target is invisible or shapechanged when you use the Judgment, it must make a Wisdom saving throw (DC {npc.spellcasting[name].spellsavedc()}) at the start of each of its turns. On a failure either effect is suppressed until the Judgment ends, and the target cannot turn invisible or change shape for the duration."))
```

## Final Judgment
*17th-level Divine Inquisitor feature*

As an Action on your turn, you pray to your deity for a final judgment. This ends the Judgment on your target, but it must succeed on a Charisma Saving Throw against your Spell save DC. On a failed save, the target takes radiant damage equal to double your sneak attack damage. On a successful save the target takes only half damage.

You can use this ability once before you must finish a long rest to be able to use it again.

```
def level17(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Final Judgment (Recharges on long rest).*** You pray to your deity for a final judgment. This ends the Judgment on your target, but it must succeed on a Charisma Saving Throw against DC {npc.spellcasting[name].spellsavedc()}. On a failed save, the target takes radiant damage equal to double your sneak attack damage. On a successful save the target takes only half damage."))
```
