# Divine Domain: Ocean
Clerics of Gods who control the waves and tides, as well as the beasts who dwell within the depths of the sea draw power from this domain.

```
name = 'Ocean'
description = "***Divine Domain: Ocean.*** ... "
```

## Domain Spells
*1st-level Ocean Domain feature*

You gain domain spells at the cleric levels listed in the Tempest Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Ocean Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [fog cloud](../../Magic/Spells/fog-cloud.md), [create or destroy water](../../Magic/Spells/create-or-destroy-water.md) 
3rd	| [misty step](../../Magic/Spells/misty-step.md), [chilling scythe](../../Magic/Spells/chilling-scythe.md)
5th	| [tidal wave](../../Magic/Spells/tidal-wave.md), [water breathing](../../Magic/Spells/water-breathing.md)
7th	| [control water](../../Magic/Spells/control-weather.md), [watery sphere](../../Magic/Spells/watery-sphere.md)
9th	| [maelstrom](../../Magic/Spells/maelstrom.md), [control winds](../../Magic/Spells/control-winds.md)

```
domainspells = {
    1: ['fog cloud', 'create or destroy water'],
    3: ['misty step', 'chilling scythe'],
    5: ['tidal wave', 'water breathing'],
    7: ['control water', 'watery sphere'],
    9: ['maelstrom', 'control winds']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(baseclass.name) >= 1: results += domainspells[1]
        if npc.levels(baseclass.name) >= 3: results += domainspells[3]
        if npc.levels(baseclass.name) >= 5: results += domainspells[5]
        if npc.levels(baseclass.name) >= 7: results += domainspells[7]
        if npc.levels(baseclass.name) >= 9: results += domainspells[9]
        npc.spellcasting[baseclass.name].spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```

## Bonus Proficiency
*1st-level Ocean Domain feature*

You gain proficiency with the trident and can choose that as your starting equipment.

```
    npc.proficiencies.append("Trident")
```

## Sea priest
*1st-level Ocean Domain feature*

You gain a swimming speed equal to your base walking speed while wearing armor weighing less than 35lbs (for medium creatures- 25lbs for small creatures) or no armor and while not using a shield.

```
    npc.speed['swimming'] = npc.speed['walking']
```

## Wrath Of The Wave
*1st-level Ocean Domain feature*

You can torrentuously rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw. The creature takes 2d6 cold damage on a failed saving throw and is pushed back 10 feet, and half as much damage (and is not pushed) on a successful one. You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.speed['swimming'] = npc.speed['walking']

    npc.defer(lambda npc: npc.reactions.append(f"***Wrath of the Wave ({npc.WISbonus() if npc.WISbonus() > 0 else 1}/Recharge on long rest).*** When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw (DC {npc.spellcasting[baseclass.name].spellsavedc()}). The creature takes 2d6 cold damage on a failed saving throw and is pushed back 10 feet, and half as much damage (and is not pushed) on a successful one."))
```

## Channel Divinity: Torrential Wrath
*2nd-level Ocean Domain feature*

You can use your Channel Divinity to wield the power of the waves with unchecked ferocity.

As an action, you present your holy symbol and invoke the name of your deity. A forceful 10-foot-high wave of cold water erupts in a 30ft-radius circle around you. All creatures within the circle must succeed on a Strength saving throw or take xd6 cold and xd6 bludgeoning damage and be pushed back 10 feet and knocked prone. (x equals your proficiency bonus) Creatures take half as much damage and are not pushed and knocked down on a successful saving throw. Creatures of the Huge size and larger are not pushed back and knocked prone. You must not be in the air when you do this.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Torrential Wrath.*** A forceful {'10' if npc.levels(baseclass) < 17 else '20'}-foot-high wave of cold water erupts in a {'30' if npc.levels(baseclass) < 17 else '60'}ft-radius circle around you. All creatures within the circle must succeed on a Strength saving throw or take {npc.proficiencybonus()}d6 cold and {npc.proficiencybonus()}d6 bludgeoning damage and be pushed back {'10' if npc.levels(baseclass) < 17 else '15'} feet and knocked prone. Creatures take half as much damage and are not pushed and knocked down on a successful saving throw. Creatures of the {'Huge' if npc.levels(baseclass) < 17 else 'Gargantuan'} size and larger are not pushed back and knocked prone. You must not be in the air when you do this."))
```

## Divine Strike
At 8th level, you gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 cold damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1' if npc.levels(baseclass) < 14 else '2'}d8 cold damage to the target."))
```

## Seablooded
At 17th level, you have can breathe water as well as air. Your swim speed increases by 15 feet. When you use your Torrential Wrath feature, the effect's radius is extended to 60 feet, the wave is 20 feet tall and the distance creatures are pushed back increases to 15 feet. Huge creatures can now be pushed and knocked prone by this feature.

```
def level17(npc):
    npc.traits.append(traits['amphibious'])
    npc.speed['swimming'] += 15
```
