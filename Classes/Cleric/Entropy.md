# Divine Domain: Entropy
All things must end. All creatures born into the planes of existence have some awareness of this fact from birth, and it comprises one of the most fundamental truths of reality. As such, many gods have nothing to do with entropy--yet those clerics who choose this domain still have their faith rewarded (in the form of spells).

```
name = 'Entropy'
description = "***Divine Domain: Entropy.*** All things must end. All creatures born into the planes of existence have some awareness of this fact from birth, and it comprises one of the most fundamental truths of reality. As such, many gods have nothing to do with entropy--yet those clerics who choose this domain still have their faith rewarded (in the form of spells)."
```

## Domain spells
You gain domain spells at the cleric levels listed in the Entropy Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Entropy Domain Spells**

Cleric Level | Entropy Domain Spells
------------ | ---------------------
1st | [inflict wounds](../../Magic/Spells/inflict-wounds.md), [thunderwave](../../Magic/Spells/thunderwave.md)
3rd | [shatter](../../Magic/Spells/shatter.md), [darkness](../../Magic/Spells/darkness.md)
5th | [life transference](../../Magic/Spells/life-transference.md), [vampiric touch](../../Magic/Spells/vampiric-touch.md)
7th | [blight](../../Magic/Spells/blight.md), [sickening radiance](../../Magic/Spells/sickening-radiance.md)
9th | [negative energy flood](../../Magic/Spells/negative-energy-flood.md), [antilife shell](../../Magic/Spells/antilife-shell.md)

```
domainspells = {
    1: ['inflict wounds', 'thunderwave'],
    3: ['shatter', 'darkness'],
    5: ['life transference', 'vampiric touch'],
    7: ['blight', 'sickening radiance'],
    9: ['negative energy flood', 'antilife shell']
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

## Rust Ward
*1st-level Entropy domain feature*

Your entropic magic wears away at the weapons of your assailants. When a creature hits you with a melee weapon attack, after dealing damage the weapon takes a permanent and cumulative −1 penalty to damage rolls. If its penalty drops to −5, the weapon is destroyed. Nonmagical ammunition made of metal that hits you is destroyed after dealing damage.

```
    npc.defer(lambda npc: npc.traits.append(f"***Rust Ward.*** When a creature hits you with a melee weapon attack, after dealing damage the weapon takes a permanent and cumulative −1 penalty to damage rolls. If its penalty drops to −5, the weapon is destroyed. Nonmagical ammunition made of metal that hits you is destroyed after dealing damage.") )
```

## Channel Divinity: Dissolution
*2nd-level Entropy domain feature*

You can use your Channel Divinity to disintegrate physical objects. As an action, you present your holy symbol, and condemn an object within 5 feet of you that isn't being worn or carried. You can also target a 5 foot square section of a larger object, such as a wall. The chosen object disintegrates into a pile of dust.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Dissolution.*** You present your holy symbol, and condemn {'an object not being worn or carried within 5 feet of you' if npc.levels('Cleric') < 17 else 'all objects not being worn or carried within 10 feet of you'}. You can also target a 5 foot square section of a larger object, such as a wall. The chosen object disintegrates into a pile of dust.")
```

## Entropic Gyre
*6th-level Entropy domain feature*

Your presence becomes anathema to all things of beauty and permanence. Magical objects are now affected by your Rust Ward and Channel Divinity features.

In addition, when you strike a creature with a melee attack, any armor or shield that creature is wearing takes a permanent and cumulative −1 penalty to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to a +0 bonus is destroyed.

```
def level6(npc):
    npc.traits.append("***Entropic Gyre.*** Your presence becomes anathema to all things of beauty and permanence. Magical objects are now affected by your Rust Ward and Channel Divinity features. In addition, when you strike a creature with a melee attack, any armor or shield that creature is wearing takes a permanent and cumulative −1 penalty to the AC it offers. Armor reduced to an AC of 10 or a shield that drops to a +0 bonus is destroyed.")
```

## Divine Strike
*8th-level Entropy domain feature*

You gain the ability to infuse your weapon strikes with entropic energy. Once on each of the cleric's turns when he or she hits a creature with a weapon attack, the cleric can cause the attack to deal an extra 1d8 necrotic damage to the target. 

When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} thunder damage to the target.") )
```

## Radial Decomposition
*17th-level Entropy domain feature*

You can use your Dissolution feature to affect all objects within 10 feet of you that aren't being worn or carried.
