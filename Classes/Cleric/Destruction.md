# Divine Domain: Destruction
Gods of destruction are typically evil--or at the very least selfish--and revel in widespread and wanton destruction of things. Nothing is too great to be destroyed. Whether it's tearing down a building, collapsing a cave system, bringing walls tumbling down, or triggering an avalanche, destruction clerics live for that precise moment when it all begins to collapse.

This domain is available to clerics of [Cyric](../../Religions/Pantheon/Cyric.md), [Hextor](../../Religions/Pantheon/Hextor.md), ...

```
name = 'Destruction'
description = "***Divine Domain: Destruction.*** Gods of destruction are typically evil--or at the very least selfish--and revel in widespread and wanton destruction of things. Nothing is too great to be destroyed. Whether it's tearing down a building, collapsing a cave system, bringing walls tumbling down, or triggering an avalanche, destruction clerics live for that precise moment when it all begins to collapse."
```

## Domain Spells

Cleric Level | Spells
------------ | ------
1st	| [divine favor](../../Magic/Spells/divine-favor.md), [wrathful smite](../../Magic/Spells/wrathful-smite.md)
3rd	| [enlarge/reduce](../../Magic/Spells/enlarge-reduce.md), [shatter](../../Magic/Spells/shatter.md)
5th	| [fireball](../../Magic/Spells/fireball.md), [lightning bolt](../../Magic/Spells/lightning-bolt.md)
7th	| [ice storm](../../Magic/Spells/ice-storm.md), [staggering smite](../../Magic/Spells/staggering-smite.md)
9th	| [mass inflict wounds](../../Magic/Spells/mass-inflict-wounds.md), [wave of obliteration](../../Magic/Spells/wave-of-obliteration.md)

```
domainspells = {
    1: ['divine favor', 'wrathful smite'],
    3: ['enlarge-reduce', 'shatter'],
    5: ['fireball', 'lightning bolt'],
    7: ['ice storm', 'staggering smite'],
    9: ['mass inflict wounds', 'wave of obliteration']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(spellcasting.casterclass) >= 1: results += domainspells[1]
        if npc.levels(spellcasting.casterclass) >= 3: results += domainspells[3]
        if npc.levels(spellcasting.casterclass) >= 5: results += domainspells[5]
        if npc.levels(spellcasting.casterclass) >= 7: results += domainspells[7]
        if npc.levels(spellcasting.casterclass) >= 9: results += domainspells[9]
        spellcasting.spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```

## Bonus Proficiencies
*1st-level Destruction domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for prof in weapons['martial-melee'] | weapons['martial-ranged'] | armor['heavy']:
        npc.proficiencies.append(prof)
```

## Destructive Smite
*1st-level Destruction domain feature*

When you hit a creature with a melee weapon attack, you can expend one spell slot to deal thunder damage to the target, in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8.

```
    npc.actions.append("***Destructive Smite.*** When you hit a creature with a melee weapon attack, you can expend one spell slot to deal thunder damage to the target, in addition to the weapon's damage. The extra damage is 2d8 for a 1st-level spell slot, plus 1d8 for each spell level higher than 1st, to a maximum of 5d8.")
```

## Channel Divinity: Sundering Invocation
*2nd-level Destruction domain feature*

You can use your Channel Divinity to channel destructive energy.

As an action, you touch a creature or a an unattended object within reach. A creature must make a Constitution saving throw, taking 5 times your cleric level thunder damage on a failed saving throw and half as much on a successful one. An unattended object takes 5 times your cleric level thunder damage.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Sundering Invocation.*** You touch a creature or an unattended object within reach. A creature must make a Constitution saving throw, taking {5 * npc.levels('Cleric')} thunder damage on a failed saving throw and half as much on a successful one. An unattended object takes {5 * npc.levels('Cleric')} thunder damage.") )
```

## Appetite for Destruction
*6th-level Destruction domain feature*

Your destructive acts fuel further expressions of devastation. If you kill a creature or destroy an object with a weapon attack, you can use your bonus action to immediately make one additional weapon attack.

```
def level6(npc):
    npc.bonusactions.append("***Appetite for Destruction.*** If you kill a creature or destroy an object with a weapon attack, you make one additional weapon attack.")
```

## Divine Strike
*8th-level Destruction domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 thunder damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} force damage to the target.") )
```

## Destructive Touch
*17th-level Destruction domain feature*

You can utterly destroy an enemy with just a touch. As an action, touch one creature. That creature must make a Constitution saving throw. The DC for this saving throw is your cleric spell save DC. On a failed save, the creature dies, and its body and everything it is wearing and carrying, except magic items, are reduced to a pile of fine gray dust. The creature can be restored to life only by means of a true resurrection or a wish spell. On a successful save, the creature takes 10d6 force damage. If this damage reduces the target to 0 hit points, it dies and is disintegrated as if it had failed its save against your Destructive Touch.

Once you use this feature, you can't use it again until after you complete a long rest.

```
def level17(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Destructive Touch.*** Touch one creature. That creature must make a Constitution saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}). On a failed save, the creature dies, and its body and everything it is wearing and carrying, except magic items, are reduced to a pile of fine gray dust. The creature can be restored to life only by means of a {spelllinkify('true resurrection')} or a {spelllinkify('wish')} spell. On a successful save, the creature takes 10d6 force damage. If this damage reduces the target to 0 hit points, it dies and is disintegrated as if it had failed its save against your Destructive Touch.") )
```
