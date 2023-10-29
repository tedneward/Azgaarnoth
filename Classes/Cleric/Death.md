# Divine Domain: Death
The Death domain is concerned with the forces that cause death, as well as the negative energy that gives rise to undead creatures. While many of the deities who serve as patrons to Death Clerics are evil and seek the absence of life, others are simply stewards of the realm of the dead. Some are even prone to carefully balance life against death, intervening when too much life threatens an ecosystem and death must be brought to bring things back into careful equilibrium.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Arawn](../../Religions/Pantheon/Arawn.md), ...

```
name = 'Death'
description = "***Divine Domain: Death.*** The Death domain is concerned with the forces that cause death, as well as the negative energy that gives rise to undead creatures. While many of the deities who serve as patrons to Death Clerics are evil and seek the absence of life, others are simply stewards of the realm of the dead. Some are even prone to carefully balance life against death, intervening when too much life threatens an ecosystem and death must be brought to bring things back into careful equilibrium."
```

## Domain Spells
*1st-level Death Domain feature* 

You gain domain spells at the cleric levels listed in the Death Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Death Domain Spells**

Cleric Level | Spells
------------ | ------
1st | [false life](../../Magic/Spells/false-life.md), [ray of sickness](../../Magic/Spells/ray-of-sickness.md)
3rd	| [blindness/deafness](../../Magic/Spells/blindness-deafness.md), [ray of enfeeblement](../../Magic/Spells/ray-of-enfeeblement.md)
5th	| [animate dead](../../Magic/Spells/animate-dead.md), [vampiric touch](../../Magic/Spells/vampiric-touch.md)
7th | [blight](../../Magic/Spells/blight.md), [death ward](../../Magic/Spells/death-ward.md)
9th | [antilife shell](../../Magic/Spells/antilife-shell.md), [cloudkill](../../Magic/Spells/cloudkill.md)

```
domainspells = {
    1: ['false life', 'ray of sickness'],
    3: ['blindness-deafness', 'ray of enfeeblement'],
    5: ['animate dead', 'vampiric touch'],
    7: ['blight', 'death ward'],
    9: ['antilife shell', 'cloudkill']
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
*1st-level Death Domain feature* 

You gain proficiency with martial weapons.

```
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
```

## Reaper
*1st-level Death Domain feature* 

You learn one necromancy cantrip of your choice from any spell list. When you cast a necromancy cantrip that normally targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other.

```
    npc.spellcasting[baseclass.name].cantripsknown.append("CHOOSE-necromancy")
    npc.defer(lambda npc: npc.traits.append(f"***Reaper.*** When you cast a necromancy {'cantrip' if npc.levels('Cleric') < 17 else 'cantrip or 1st through 5th level spell'} that normally targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other. If the spell consumes its material components, you must provide them for each target.") )
```

## Channel Divinity: Touch of Death
*2nd-level Death Domain feature* 

You can use Channel Divinity to destroy another creature's life force by touch. When you hit a creature with a melee attack, you can use Channel Divinity to deal extra necrotic damage to the target. The damage equals 5 + twice your cleric level.

```
def level2(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Channel Divinity: Touch of Death.*** When you hit a creature with a melee attack, you can use Channel Divinity to deal {5 + (2 * npc.levels('Cleric'))} extra necrotic damage to the target.{' This ignores resistance to necrotic damage.' if npc.levels('Cleric') >= 6 else ''}") )
```

## Inescapable Destruction
*6th-level Death Domain feature* 

Your ability to channel negative energy becomes more potent. Necrotic damage dealt by your cleric spells and Channel Divinity options ignores resistance to necrotic damage.

```
def level6(npc):
    npc.traits.append("***Inescapable Destruction.*** Necrotic damage dealt by your cleric spells ignore resistance to necrotic damage.")
```

## Divine Strike
*8th-level Death Domain feature* 

You gain the ability to infuse your weapon strikes with necrotic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an a 1d8 necrotic damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you cause the attack to deal an extra {'1' if npc.levels('Cleric') < 14 else '2'}d8 necrotic damage to the target.") )
```

## Improved Reaper
*17th-level Death Domain feature* 

When you cast a necromancy spell of 1st through 5th level that targets only one creature, the spell can instead target two creatures within range and within 5 feet of each other. If the spell consumes its material components, you must provide them for each target.
