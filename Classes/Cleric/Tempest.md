# Divine Domain: Tempest
Clerics of the Tempest domain find power and beauty in the wracking storms that batter coastlines and bring the seas to rage. They are often themselves of a fierce temper, some ready to embrace that temper at the first moment, others requiring longer provocation, but once provoked, their wrath knows no limits.

This is a domain granted by the [*al'maeran* tradition](../../Religions/AlUma.md#almaeran-cleric),the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Leriya](../../Religions/Trinitarian.md#leriya), [Auril](../../Religions/Pantheon/Auril.md), [Gruumsh](../../Religions/Pantheon/Gruumsh.md), [Sekolah](../../Religions/Pantheon/Sekolah.md), ...

```
name = 'Tempest'
description = "***Divine Domain: Tempest.*** Clerics of the Tempest domain find power and beauty in the wracking storms that batter coastlines and bring the seas to rage. They are often themselves of a fierce temper, some ready to embrace that temper at the first moment, others requiring longer provocation, but once provoked, their wrath knows no limits."
```

## Domain Spells
*1st-level Tempest Domain feature*

You gain domain spells at the cleric levels listed in the Tempest Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Tempest Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [Fog Cloud](../../Magic/Spells/fog-cloud.md), [Thunderwave](../../Magic/Spells/thunderwave.md)
3rd	| [Gust of Wind](../../Magic/Spells/gust-of-wind.md), [Shatter](../../Magic/Spells/shatter.md)
5th	| [Call Lightning](../../Magic/Spells/call-lightning.md), [Sleet Storm](../../Magic/Spells/sleet-storm.md)
7th	| [Control Water](../../Magic/Spells/control-water.md), [Ice Storm](../../Magic/Spells/ice-storm.md)
9th	| [Destructive Wave](../../Magic/Spells/destructive-wave.md), [Insect Plague](../../Magic/Spells/insect-plague.md)

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
def level1(npc):
    npc.defer(lambda npc: domainspellsforlevel(npc))
```

## Bonus Proficiencies
*1st-level Tempest Domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
    for arm in armor['heavy']:
        npc.proficiencies.append(arm)
```

## Wrath of the Storm
*1st-level Tempest Domain feature*

You can thunderously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Wrath of the Storm ({'1' if npc.WISbonus() < 1 else str(npc.WISbonus())}/Recharges on long rest).*** When a creature within 5 feet of you that you can see hits you with an attack, you can cause the creature to make a Dexterity saving throw (DC {npc.spellcasting['Cleric'].spellsavedc()}). The creature takes 2d8 lightning or thunder damage (your choice) on a failed saving throw, and half as much damage on a successful one."))
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
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} thunder damage to the target."))
```

## Stormborn
*17th-level Tempest Domain feature*

You have a flying speed equal to your current walking speed whenever you are not underground or indoors.

```
def level17(npc):
    npc.speed['flying'] = npc.speed['walking']
    npc.traits.append("***Stormborn.*** You can only fly whenever you are not underground or indoors; you must have a clear view of the sky..")
```
