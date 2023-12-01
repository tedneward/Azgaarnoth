# Divine Domain: Earth
*Deep underground, a dwarf swings its pick and shatters stones and prays to find diamonds, rubies, gold, and more. Up on the surface, a farmer digs through rocky soil and prays to find good loam beneath it. On the elemental plane of earth, earthen plates move to crush a visiting mortal who prays for deliverance.*

Clerics of the earth domain are closely tied to soil and stone. Stones can make an implacable obstacle for good or ill. With power over earth you can smash through these obstacles when used for ill purposes and strengthen them when used for good ones. You can use magic to bend the earth to your bending or to break it when it is defiant.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Daghda](../../Religions/Pantheon/Daghda.md), ...

```
name = 'Earth'
description = "***Divine Domain: Earth.*** Clerics of the earth domain are closely tied to soil and stone. Stones can make an implacable obstacle for good or ill. With power over earth you can smash through these obstacles when used for ill purposes and strengthen them when used for good ones. You can use magic to bend the earth to your bending or to break it when it is defiant."
```

**Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [earth tremor](../../Magic/Spells/earth-tremor.md), [shield](../../Magic/Spells/shield.md)
3rd	| [magic weapon](../../Magic/Spells/magic-weapon.md), [maximilian's earthen grasp](../../Magic/Spells/maximilians-earthen-grasp.md)
5th	| [erupting earth](../../Magic/Spells/erupting-earth.md), [meld into stone](../../Magic/Spells/meld-into-stone.md)
7th	| [stone shape](../../Magic/Spells/stone-shape.md), [stoneskin](../../Magic/Spells/stoneskin.md)
9th	| [transmute rock](../../Magic/Spells/transmute-rock.md), [wall of stone](../../Magic/Spells/wall-of-stone.md)

```
domainspells = {
    1: ['earth tremor', 'shield'],
    3: ['magic weapon', 'maximilians earthen grasp'],
    5: ['erupting earth', 'meld into stone'],
    7: ['stone shape', 'stoneskin'],
    9: ['transmute rock', 'wall of stone']
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

## Bonus Proficiency
*1st-level Earth domain feature*

You gain proficiency with martial weapons. You also learn to read, speak, and write Terran.

```
    for prof in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(prof)

    npc.languages.append('Terran')
```

## Bonus Cantrip
*1st-level Earth domain feature*

You learn the [mold earth](../../Magic/Spells/mold-earth.md) cantrip. It counts as a cleric spell for you.

```
    spellcasting.cantripsknown.append('mold earth')
```

## Tunnel Vision
*1st-level Earth domain feature*

You gain darkvision out to a range of 120 feet. If you already have darkvision, its range increases by 60 feet. You also ignore the sunlight sensitivity trait if you have it. While you are underground your darkvision is in full color instead of in shades of grey.

```
    if 'darkvision' in npc.senses:
        npc.senses['darkvision'] += 60
    else:
        npc.senses['darkvision'] = 120
    npc.traits.append("***Tunnel Vision.*** While you are underground your darkvision is in full color instead of in shades of grey.")
    for tra in npc.traits:
        if tra[0:len('***Sunlight Sensitivity')] == "***Sunlight Sensitivity":
            npc.traits.remove(tra)
```

## Channel Divinity: Adamantine Self
*2nd-level Earth domain feature*

You can use your Channel Divinity to increase your defensive and offensive power for a short time.

As an action, you present your holy symbol and magically conjure forth minerals that coat you and your weapons. For 1 minute, any weapon you wield counts as adamantine for the purpose of overcoming damage resistance and automatically scores a critical hit when it hits an object. Additionally, any critical hits scored against you during that minute are instead treated as normal hits.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Adamantine Self.*** You present your holy symbol and magically conjure forth minerals that coat you and your weapons. For 1 minute, any weapon you wield counts as adamantine for the purpose of overcoming damage resistance and automatically scores a critical hit when it hits an object. Additionally, any critical hits scored against you during that minute are instead treated as normal hits.")
```

## Rock Solid
*6th-level Earth domain feature*

You become as implacable as a boulder. When an effect would cause you to move against your will, you can use your reaction to reduce that movement by up to 10 feet. Additionally, when you make a Constitution saving throw to maintain your concentration on a cleric spell you cast, you can add your Wisdom modifier to the result.

```
def level6(npc):
    npc.defer(lambda npc: npc.reactions.append("***Rock Solid.*** When an effect would cause you to move against your will, you can use your reaction to reduce that movement by up to 10 feet. Additionally, when you make a Constitution saving throw to maintain your concentration on a cleric spell you cast, you can add {npc.WISbonus()} to the result.") )
```

## Divine Strike
*8th-level Earth domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 thunder damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} thunder damage to the target.") )
```

## Creature of the Earth
*17th-level Earth domain feature*

You can burrow through sand, mud, ice, and nonmagical stone with a burrowing speed equal to your walking speed. Moving through stone in this way counts as moving through difficult terrain. You leave a passage behind you as you burrow large enough for a creature of your size to fit through without squeezing. You also have tremorsense out to 30 feet which allows you to detect and pinpoint the origin of vibrations within a specific radius, provided that you and the source of the vibrations are in contact with the same ground or substance. Tremorsense can't be used to detect flying or incorporeal creatures.

```
def level17(npc):
    npc.speed['burrow'] = npc.speed['walking']
    npc.traits.append("***Creature of the Earth.*** Moving through stone when burrowing counts as moving through difficult terrain. You leave a passage behind you as you burrow large enough for a creature of your size to fit through without squeezing.")
    npc.senses['tremorsense'] = 30
```
