# Divine Domain: Sea
Clerics who serve deities of the sea act as both guides and guardians. The ocean is one of the most terrifying places in existence, due to what lies both above and below the water's surface. Clerics of the sea deities bring peace to sailors and calm the wrath of the waves.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), ...

```
name = 'Sea'
description = "***Divine Domain: Sea.*** Clerics who serve deities of the sea act as both guides and guardians. The ocean is one of the most terrifying places in existence, due to what lies both above and below the water's surface. Clerics of the sea deities bring peace to sailors and calm the wrath of the waves."
```

**Sea Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [create or destroy water](../../Magic/Spells/create-or-destroy-water.md), [fog cloud](../../Magic/Spells/fog-cloud.md)
3rd	| [gust of wind](../../Magic/Spells/gust-of-wind.md), [misty step](../../Magic/Spells/misty-step.md)
5th	| [tidal wave](../../Magic/Spells/tidal-wave.md), [wall of water](../../Magic/Spells/wall-of-water.md)
7th	| [control water](../../Magic/Spells/control-water.md), [watery sphere](../../Magic/Spells/watery-sphere.md)
9th	| [conjure elemental](../../Magic/Spells/conjure-elemental.md), [maelstrom](../../Magic/Spells/maelstrom.md)

```
domainspells = {
    1: ['create or destroy water', 'fog cloud'],
    3: ['gust of wind', 'misty step'],
    5: ['tidal wave', 'wall of water'],
    7: ['control water', 'watery sphere'],
    9: ['conjure elemental', 'maelstrom']
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
*1st-level Sea domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for prof in weapons['martial-melee'] | weapons['martial-ranged'] | armor['heavy']:
        npc.proficiencies.append(prof)
```

## Wayfaring Worshiper
*1st-level Sea domain feature*

You gain a swimming speed equal to your walking speed. You also learn the [shape water](../../Magic/Spells/shape-water.md) cantrip, or one other cleric cantrip if you already knew it.

```
    npc.speed['swimming'] = npc.speed['walking']
    spellcasting.cantripsknown.append('shape water')
```

## Channel Divinity: Rising Tide
*2nd-level Sea domain feature*

You can use your Channel Divinity to summon a thrashing tide in battle.

As an action, you present your holy symbol, and a raging torrent appears around you. The torrent is centered on you, has a 30ft radius, and is filled with pouring rain and crashing waves. The sphere moves with you, and it lasts for 1 minute or until you fall unconscious or die. The torrent is difficult terrain, and ranged attack rolls have disadvantage.

You can designate a number of creatures up to your proficiency bonus that are immune to the torrent's effects.

This effect works underwater, as the area becomes a whirlpool.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Rising Tide.*** you present your holy symbol, and a raging torrent appears around you. The torrent is centered on you, has a 30ft radius, and is filled with pouring rain and crashing waves. The sphere moves with you, and it lasts for 1 minute or until you fall unconscious or die. The torrent is difficult terrain, and ranged attack rolls have disadvantage. You can designate {npc.proficiencybonus()} creatures that are immune to the torrent's effects. This effect works underwater, as the area becomes a whirlpool.") )
```

## Snatching Undertow
*6th-level Sea domain feature*

You can create an overpowering current that pulls your foes down. As a bonus action, you can force a number of creatures up to your Wisdom modifier that are in your rising tide to make a Strength saving throw. On a failure, they are knocked prone.

If a target is submerged, when you use this ability, their movement speed becomes 0 until the end of their next turn.

```
def level6(npc):
    npc.bonusactions.append("***Snatching Undertow.*** You force up to {npc.WISbonus()} creatures that are in your Rising Tide to make a Strength saving throw. On a failure, they are knocked prone. If a target is submerged, when you use this ability, their movement speed becomes 0 until the end of their next turn.")
```

## Prayers of the Deep
*6th-level Sea domain feature*

You can breathe air and water, and gain resistance to cold damage.

```
    npc.traits.append("***Prayers of the Deep.*** You can breathe air or water.")
    npc.damageresistances.append('cold')
```

## Divine Strike
*8th-level Sea domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 cold damage. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} force damage to the target.") )
```

## Wrath of the Sea
*17th-level Sea domain feature*

You call forth the rage of the ocean to devour your enemies. When a hostile creature enters your torrent for the first time on a turn, or starts its turn there, they take cold damage equal to half your Cleric level.

```
def level17(npc):
    npc.defer(lambda npc: npc.traits.append("***Wrath of the Sea.*** When a hostile creature enters your torrent for the first time on a turn, or starts its turn there, they take {npc.levels('Cleric') // 2} cold damage.") )
```
