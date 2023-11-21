# Divine Domain: Air
Free-willed and adventurous, these Clerics worship the deities of the Air, always letting the ever-flowing winds guide them in their lives.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md),  [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), ...

```
name = 'Air'
description = "***Divine Domain: Air.*** Free-willed and adventurous, these Clerics worship the deities of the Air, always letting the ever-flowing winds guide them in their lives."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Air Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Air Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [skywrite](../../Magic/Spells/skywrite.md), [feather fall](../../Magic/Spells/feather-fall.md)
3rd	| [warding wind](../../Magic/Spells/warding-wind.md), [dust devil](../../Magic/Spells/dust-devil.md)
5th	| [wind wall](../../Magic/Spells/wind-wall.md), [haste](../../Magic/Spells/haste.md)
7th	| [gust of wind](../../Magic/Spells/gust-of-wind.md), [storm sphere](../../Magic/Spells/storm-sphere.md)
9th	| [control winds](../../Magic/Spells/control-winds.md), [wind walk](../../Magic/Spells/wind-walk.md)

```
domainspells = {
    1: ['skywrite', 'feather fall'],
    3: ['warding wind', 'dust devil'],
    5: ['wind wall', 'haste'],
    7: ['gust of wind', 'storm sphere'],
    9: ['control winds', 'wind walk']
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

## Bonus Cantrip
*1st-level Air Domain feature*

You gain the [gust](../../Magic/Spells/gust.md) cantrip if you don't already know it. This cantrip counts as a cleric cantrip for you, but it doesn't count against the number of cleric cantrips you know.

```
    spellcasting.cantripsknown.append('gust')
```

## Bonus Proficiencies
*1st-level Air Domain feature*

You also gain proficiency in Acrobatics and Insight skills.

```
    npc.proficiencies.append('Acrobatics')
    npc.proficiencies.append('Insight')
```

## Speedy Senses
*1st-level Air Domain feature*

Your senses become attuned to the wind. You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Dodge action.

```
    npc.bonusactions.append("***Speedy Senses.*** You can Dash, Disengage, or Dodge.")
```

## Channel Divinity: Godspeed
*2nd-level Air Domain feature*

Your Channel Divinity feature allows you to call upon the winds to embody you. For one hour, your flying and walking speeds increase by 10 feet and you gain a +1 bonus to your AC. If you don't have flying speed you gain 10 feet flying speed.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Godspeed.*** For one hour, your flying and walking speeds increase by 10 feet and you gain a +1 bonus to your AC. If you don't have flying speed you gain 10 feet flying speed.")
```

## Light as a Feather
*6th-level Air Domain feature*

You can nimbly dodge out of the way of certain area Effects, such as a red dragon's fiery breath or an Ice Storm spell. When you are subjected to an Effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.

```
def level6(npc):
    npc.traits.append("***Light as a Feather.*** When you are subjected to an Effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")
```

## Divine Strike
*8th-level Air Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 force damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} force damage to the target.") )
```

## Wrath of Wind
*17th-level Air Domain feature*

You can harness the full potential of the winds. As a bonus action, you become a paragon of the wind and for the next minute you gain the following benefits:

* Your movement speed is doubled, and you have a flying speed equal to your doubled movement speed.
* Attacks made against you have disadvantage on the roll.
* You can use your action to cast the [Whirlwind](../../Magic/Spells/whirlwind.md) spell without using a spell slot. (You can only have one Whirlwind active at a time.)

Once you use this feature, you can't use it again until you finish a long rest.

```
def level17(npc):
    npc.bonusactions.append(f"***Wrath of Wind (Recharges on long rest).*** You become a paragon of the wind and for the next minute you gain the following benefits: Your movement speed is doubled, and you have a flying speed equal to your doubled movement speed; Attacks made against you have disadvantage on the roll; You can use your action to cast {spelllinkify('whirlwind')} without using a spell slot. (You can only have one *whirlwind* active at a time.)")
```
