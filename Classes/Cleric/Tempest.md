# Divine Domain: Tempest
This is a domain granted by the [*al'maeran* tradition](../../Religions/AlUma.md#almaeran-cleric),the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Auril](../../Religions/Pantheon/Auril.md), ...

```
name = 'Tempest'
description = "***Divine Domain: Tempest.*** "
```

## Domain Spells
*1st-level Tempest Domain feature*

You gain domain spells at the cleric levels listed in the Tempest Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Tempest Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| Fog Cloud, Thunderwave
3rd	| Gust of Wind, Shatter
5th	| Call Lightning, Sleet Storm
7th	|Control Water, Ice Storm
9th	|Destructive Wave, Insect Plague

```
domainspells = {
    1: ['fog cloud', 'thunderwave'],
    3: ['gust of wind', 'shatter'],
    5: ['call lightning', 'sleet storm'],
    7: ['control water', 'ice storm'],
    9: ['destructive wave', 'insect plague']
}
def domainspellsforlevel(npc):
    results = []
    if npc.levels('Cleric') >= 1: results += domainspells[1]
    if npc.levels('Cleric') >= 3: results += domainspells[3]
    if npc.levels('Cleric') >= 5: results += domainspells[5]
    if npc.levels('Cleric') >= 7: results += domainspells[7]
    if npc.levels('Cleric') >= 9: results += domainspells[9]
    npc.spellcasting['Cleric'].spellsalwaysprepared += results
```

## Bonus Proficiencies
*1st-level Tempest Domain feature*

You gain proficiency with martial weapons and heavy armor.

```
def level1(npc):
    npc.proficiencies.append("Martial weapons")
    npc.proficiencies.append("Heavy armor")
```

## Wrath of the Storm
*1st-level Tempest Domain feature*

You can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append("***Wrath of the Storm ({'1' if npc.WISbonus() < 1 else str(npc.WISbonus())}/Recharges on long rest).*** When a creature within 5 feet of you that you can see hits you with an attack, you can cause the creature to make a Dexterity saving throw (DC {npc.spellcasting['Cleric'].spellsavedc()}). The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one."))
```

## Channel Divinity: Destructive Wrath
*2nd level Tempest Domain feature*

You can use your Channel Divinity to wield the power of the storm with unchecked ferocity. When you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Destructive Wrath.*** When you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling.")
```

## Thunderous Strike
*6th-level Tempest Domain feature*

When you deal lightning damage to a Large or smaller creature, you can also push it up to 10 feet away from you.

```
def level6(npc):
    npc.traits.append("***Thunderous Strike.*** When you deal lightning damage to a Large or smaller creature, you can also push it up to 10 feet away from you.")
```

## Divine Strike
*8th-level Tempest Domain feature*

At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 thunder damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} thunder damage to the target.")
```

## Stormborn
At 17th level, you have a flying speed equal to your current walking speed whenever you are not underground or indoors.

```
def level17(npc):
    npc.speed['flying'] = npc.speed['walking']
    npc.traits.append("***Stormborn.*** You can only fly whenever you are not underground or indoors; you must have a clear view of the sky..")
```