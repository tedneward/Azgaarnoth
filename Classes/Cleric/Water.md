# Divine Domain: Water
Deities of water value ideals of purity, vitality, serenity, flexibility, and perseverance. Clerics of such deities seek to protect bodies of water and the communities around them. They might hunt monstrosities that corrupt and taint sources of water, or work to bring water to communities in need of it.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Brigantia](../../Religions/Pantheon/Brigantia.md), ...

```
name = 'Water'
description = "***Divine Domain: Water.*** Deities of water value ideals of purity, vitality, serenity, flexibility, and perseverance. Clerics of such deities seek to protect bodies of water and the communities around them. They might hunt monstrosities that corrupt and taint sources of water, or work to bring water to communities in need of it."
```

**Water Domain Spells**

Cleric Level | Spells
------------ | ---------
1st | [create or destroy water](../../Magic/Spells/create-or-destroy-water.md), [fog cloud](../../Magic/Spells/fog-cloud.md)
3rd | [protection from poison](../../Magic/Spells/protection-from-poison.md), [lesser restoration](../../Magic/Spells/lesser-restoration.md)
5th | [wall of water](../../Magic/Spells/wall-of-water.md), [water breathing](../../Magic/Spells/water-breathing.md)
7th | [control water](../../Magic/Spells/control-water.md), [watery sphere](../../Magic/Spells/watery-sphere.md)
9th | [maelstrom](../../Magic/Spells/maelstrom.md), [greater restoration](../../Magic/Spells/greater-restoration.md)

```
domainspells = {
    1: ['create or destroy water', 'fog cloud'],
    3: ['protection from poison', 'lesser restoration'],
    5: ['wall of water', 'water breathing'],
    7: ['control water', 'watery sphere'],
    9: ['maelstrom', 'greater restoration']
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

## Bonus Cantrips
*1st-level Water domain feature*

You gain the [shape water](../../Magic/Spells/shape-water.md) and [ray of frost](../../Magic/Spells/ray-of-frost.md) cantrips. For you, these cantrips count as cleric cantrips.

```
    spellcasting.cantripsknown.append('shape water')
    spellcasting.cantripsknown.append('ray of frost')
```

## Divine Dew
*1st-level Water domain feature*

You can conjure blessed water to improve your vitality. As a bonus action, you can grant yourself or a creature you can see within 30 feet temporary hit points equal to twice your cleric level. These hit points last up to 1 hour.

You can use this feature a number of times equal to your wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Divine Dew ({npc.WISbonus()}/Recharges on long rest).*** You grant yourself or a creature you can see within 30 feet {npc.levels('Cleric') * 2} temporary hit points. These hit points last up to 1 hour.") )
```

## Channel Divinity: Misty Shroud
*2nd-level Water domain feature*

You can use your Channel Divinity to cloak yourself and allies in a protective mist.

As an action, you present your holy symbol, and a cold fog swirls around you for 1 round. Friendly creatures within 30 feet of you may immediately use a reaction to move up to half of their speed. Hostile creatures within 30 feet of you are unable to take reactions for the duration. The fog spreads around corners.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Misty Shroud.*** You present your holy symbol, and a cold fog swirls around you for 1 round. Friendly creatures within 30 feet of you may immediately use a reaction to move up to half of their speed. Hostile creatures within 30 feet of you are unable to take reactions for the duration. The fog spreads around corners.")
```

## Blessings of Water
*6th-level Water domain feature*

You can protect yourself and allies from fire and acid with a veil of water.

When a creature, including yourself, gains temporary hit points from a spell you cast, or a Cleric class feature you use, that creature also gains resistance to fire and acid damage while any of the temporary hit points remain.

```
def level6(npc):
    npc.traits.append("***Blessings of Water.*** When a creature, including yourself, gains temporary hit points from a spell you cast, or a Cleric class feature you use, that creature also gains resistance to fire and acid damage while any of the temporary hit points remain.")
```

## Potent Spellcasting
*8th-level Water domain feature*

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.traits.append("You add your Wisdom modifier to the damage you deal with any cleric cantrip.")
```

## Warding Rains
*17th-level Water domain feature*

You can use your action to conjure a divine rain that surrounds you in a 20-foot radius for 1 minute or until you dismiss it with another action. You and friendly creatures within the rain gain a +2 bonus to saving throws.

Unprotected flames in the area are doused.

```
def level17(npc):
    npc.actions.append("***Warding Rains.*** You conjure a divine rain that surrounds you in a 20-foot radius for 1 minute or until you dismiss it with another action. You and friendly creatures within the rain gain a +2 bonus to saving throws. Unprotected flames in the area are doused.")
```
