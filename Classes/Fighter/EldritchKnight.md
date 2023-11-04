# Martial Archetype: Eldritch Knight
The archetypal Eldritch Knight combines the martial mastery common to all fighters with a careful study of magic. Eldritch Knights use magical techniques similar to those practiced by wizards. They focus their study on two of the eight schools of magic: abjuration and evocation. Abjuration spells grant an Eldritch Knight additional protection in battle, and evocation spells deal damage to many foes at once, extending the fighter's reach in combat. These knights learn a comparatively small number of spells, committing them to memory instead of keeping them in a spellbook.

Eldritch Knights are often found near or around [Mage Schools](../../Organizations/MageSchools/), particularly the [FieryFist](../../Organizations/MageSchools/FieryFirst.md) or [CrimsonSunrise](../../Organizations/MageSchools/CrimsonSunrise.md) schools; that said, there are dozens of mage schools that focus on combat magic, and an Eldritch Knight would be welcome in any of them.

```
name = 'Eldritch Knight'
description = "***Martial Archetype: Eldritch Knight.*** The archetypal Eldritch Knight combines the martial mastery common to all fighters with a careful study of magic. Eldritch Knights use magical techniques similar to those practiced by wizards. They focus their study on two of the eight schools of magic: abjuration and evocation. Abjuration spells grant an Eldritch Knight additional protection in battle, and evocation spells deal damage to many foes at once, extending the fighter's reach in combat. These knights learn a comparatively small number of spells, committing them to memory instead of keeping them in a spellbook."
```

## Spellcasting
*3rd-level Eldritch Knight feature*

You augment your martial prowess with the ability to cast spells.

### Cantrips
You learn two cantrips of your choice from the wizard spell list. You learn an additional wizard cantrip of your choice at 10th level.

### Spell Slots
The Eldritch Knight Spellcasting table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Shield and have a 1st-level and a 2nd-level spell slot available, you can cast Shield using either slot.

**Eldritch Knight Spellcasting**

Fighter Level|Cantrips Known|Spells Known|1st|2nd|3rd|4th
-------------|--------------|------------|---|---|---|---
3rd|2|3|2|-|-|-
4th|2|4|3|-|-|-
5th|2|4|3|-|-|-
6th|2|4|3|-|-|-
7th|2|5|4|2|-|-
8th|2|6|4|2|-|-
9th|2|6|4|2|-|-
10th|3|7|4|3|-|-
11th|3|8|4|3|-|-
12th|3|8|4|3|-|-
13th|3|9|4|3|2|-
14th|3|10|4|3|2|-
15th|3|10|4|3|2|-
16th|3|11|4|3|3|-
17th|3|11|4|3|3|-
18th|3|11|4|3|3|-
19th|3|12|4|3|3|1
20th|3|13|4|3|3|1


### Spells Known of 1st Level and Higher
You know three 1st-level wizard spells of your choice, two of which you must choose from the abjuration and evocation spells on the wizard spell list.

The Spells Known column of the Eldritch Knight Spellcasting table shows when you learn more wizard spells of 1st level or higher. Each of these spells must be an abjuration or evocation spell of your choice, and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the wizard spells you know with another spell of your choice from the wizard spell list. The new spell must be of a level for which you have spell slots, and it must be an abjuration or evocation spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level from any school of magic.

### Spellcasting Ability
Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Intelligence modifier

**Spell attack modifier** = your proficiency bonus + your Intelligence modifier

```
def level3(npc):
    spellcasting = halfcaster(npc, 'INT', name)
    spellcasting.casterclass = allclasses['Fighter']
    spellcasting.maxcantripsknown = 2
    spellcasting.maxspellsknown = 3
```

## Weapon Bond
*3rd-level Eldritch Knight feature*

You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.

Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand.

You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two.

```
    npc.traits.append("***Weapon Bond.*** You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond. Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand. You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two.")
    npc.bonusactions.append("***Summon Bonded Weapon.*** You can summon one of your bonded weapons, causing it to teleport instantly to your hand.")

def level4(npc):
    npc.spellcasting[name].maxspellsknown += 1
```

## War Magic
*7th-level Eldritch Knight feature*

When you use your action to cast a cantrip, you can make one weapon attack as a bonus action.

```
def level7(npc):
    npc.bonusactions.append("***War Magic.*** When you use your action to cast a cantrip, you can make one weapon attack as a bonus action.")
    npc.spellcasting[name].maxspellsknown += 1
def level8(npc):
    npc.spellcasting[name].maxspellsknown += 1
```

## Eldritch Strike
*10th-level Eldritch Knight feature*

You learn how to make your weapon strikes undercut a creature's resistance to your spells. When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn.

```
def level10(npc):
    npc.traits.append("***Eldritch Strike.*** When you hit a creature with a weapon attack, that creature has disadvantage on the next saving throw it makes against a spell you cast before the end of your next turn.")
    npc.spellcasting[name].maxspellsknown += 1

def level11(npc):
    npc.spellcasting[name].maxspellsknown += 1
def level13(npc):
    npc.spellcasting[name].maxspellsknown += 1
def level14(npc):
    npc.spellcasting[name].maxspellsknown += 1
```

## Arcane Charge
*15th-level Eldritch Knight feature*

You gain the ability to teleport up to 30 feet to an unoccupied space you can see when you use your Action Surge. You can teleport before or after the additional action.

```
def level15(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Action Surge ({'2/' if npc.levels('Fighter') > 16 else ''}Recharges on short or long rest).*** On your turn, you can take one additional action on top of your regular action and a possible bonus action."))


    npc.defer(lambda npc: replace("***Action Surge", npc.traits, f"({'2/' if npc.levels('Fighter') > 16 else ''}Recharges on short or long rest).*** On your turn, you can take one additional action on top of your regular action and a possible bonus action. When you use this, you can teleport up to 30 feet to an unoccupied space you can see. You can teleport before or after the additional action.") )

def level16(npc):
    npc.spellcasting[name].maxspellsknown += 1
```

## Improved War Magic
*18th-level Eldritch Knight feature*

When you use your action to cast a spell, you can make one weapon attack as a bonus action.

```
def level18(npc):
    replace("***War Magic", npc.bonusactions, ".*** When you use your action to cast a cantrip or spell, you can make one weapon attack as a bonus action.")
def level19(npc):
    npc.spellcasting[name].maxspellsknown += 1
def level20(npc):
    npc.spellcasting[name].maxspellsknown += 1
```
