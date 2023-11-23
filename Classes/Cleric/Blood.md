# Divine Domain: Blood
Followers of the Blood domain are not as concerned with worshiping the spirit of any particular god, but instead more concerned with worshiping the divinity in the self. Some don't even believe in the gods. 

```
name = 'Blood'
description = "***Divine Domain: Blood.*** Followers of the Blood domain are not as concerned with worshiping the spirit of any particular god, but instead more concerned with worshiping the divinity in the self. The inherent power in blood, that life-carrying substance that courses through all living things, that is the main interest to those of the Blood domain. Some don't even believe in the gods."
```

## Domain Spells
A Blood Domain Cleric gains the following spells as Domain Spells at the allotted levels:

**Blood Domain Spells**

Cleric Level | Spells
------------ | ------
1st	 | [hellish rebuke](../../Magic/Spells/hellish-rebuke.md), [inflict wounds](../../Magic/Spells/inflict-wounds.md)
3rd	 | [hold person](../../Magic/Spells/hold-person.md), [enhance ability](../../Magic/Spells/enhance-ability.md)
5th	 | [revivify](../../Magic/Spells/revivify.md), [animate dead](../../Magic/Spells/animal-friendship.md)
7th	 | [death ward](../../Magic/Spells/death-ward.md), [locate creature](../../Magic/Spells/locate-creature.md)
9th	 | [greater restoration](../../Magic/Spells/greater-restoration.md), [raise dead](../../Magic/Spells/raise-dead.md)

```
domainspells = {
    1: ['hellish rebuke', 'inflict wounds'],
    3: ['hold person', 'enhance ability'],
    5: ['revivify', 'animate dead'],
    7: ['death ward', 'locate creature'],
    9: ['greater restoration', 'raise dead']
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
*1st-level Blood domain feature*

You gain proficiency in heavy armor.

```
    for arm in armor['heavy']:
        npc.proficiencies.append(arm)
```

## Blood Magic
*1st-level Blood domain feature*

When you cast a spell, you can take 1d4+4 necrotic damage per spell level (which cannot be reduced) to cast the spell without a spell slot. When you do so, you can ignore all material components of the spell, even if it has a cost and/or is consumed, and if the spell deals damage, you may add your Wisdom modifier to that damage. 

If you cast a damaging spell, you can reduce your own health by any amount (separate from the casting damage if you use that instead of a spell slot) to add the same amount of damage to the spell. 

When you touch a creature, you can reduce your own health by any amount to heal that creature for the same amount of health as a bonus action.

If you are dropped to 0 hit points from this feature, the spell goes off before you drop unconscious. The self-inflicted damage cannot be made non-lethal unless you are under the effect of another spell or ability, but it also cannot break your concentration.

```
    npc.defer(lambda npc: npc.traits.append("***Blood Magic.*** When you cast a spell, you can take 1d4+4 necrotic damage per spell level (which cannot be reduced) to cast the spell without a spell slot. When you do so, you can ignore all material components of the spell, even if it has a cost and/or is consumed, and if the spell deals damage, you may add {npc.WISbonus()} to that damage. If you cast a damaging spell, you can reduce your own health by any amount (separate from the casting damage if you use that instead of a spell slot) to add the same amount of damage to the spell. If you are dropped to 0 hit points from this feature, the spell goes off before you drop unconscious. The self-inflicted damage cannot be made non-lethal unless you are under the effect of another spell or ability, but it also cannot break your concentration.") )

    npc.bonusactions.append("***Blood Magic.*** When you touch a creature, you can reduce your own health by any amount to heal that creature for the same amount of health.")
```

## Channel Divinity: Blood Drain
*2nd-level Blood domain feature*

As an action, you can spend one of your channel divinity to make a melee spell attack on an enemy within 5 feet of you, dealing 2d4+4 necrotic necrotic damage on a hit. (You choose between radiant and necrotic damage when you reach level 6.) You gain the same amount in healing.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append("***Channel Divinity: Blood Drain.*** you can spend one of your channel divinity to make a melee spell attack on an enemy within 5 feet of you, dealing 2d4+4 {'necrotic' if npc.levels('Cleric') < 6 else 'necrotic or radiant (your choice)'} damage on a hit. You gain the same amount in healing.") )
```

## Chanel Divinity: Flare Divinity
*2nd-level Blood domain feature*

As an action, you can expend one use of Channel Divinity to stir the divine spark within you, aiding you in your endeavors. When you do this, choose one of the following effects:

* Advantage on saving throws
* Advantage on weapon and unarmed attacks
* Advantage on skill checks
* To-hit spells deal half damage on a miss

For a number of turns equal to your Wisdom modifier, you gain the chosen benefit. (If skill checks is chosen and the check requires more time, the advantage is still used for that one check) Additionally with that benefit, your cantrips which require a saving throw to negate damage instead half damage for the duration.

At level 6, you may use this ability on one target creature you can touch instead of yourself, using their Wisdom modifier.

```
    npc.defer(lambda npc: npc.actions.append("***Channel Divinity: Flare Divinity.*** For {npc.WISbonus()} turns, you {'' if npc.levels('Cleric') < 6 else ' or one creature you can touch'} gain one of the following benefits: Advantage on saving throws; Advantage on weapon and unarmed attacks; Advantage on skill checks; To-hit spells deal half-damage on a miss. In addition, any cantrips you cast that require a saving throw to negate damage instead do half-damage on a failed saving throw for the duration.") )
```

## Potent Spellcasting
*8th-level Blood domain feature*

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Potent Spellcasting.*** You add {npc.WISbonus()} to the damage you deal with any cleric cantrip.") )
```

## Divine Undeath
*17th-level Blood domain feature*

Those who you return to life are raised as more powerful beings than they were before. If you cast any spell that returns a creature to life, you can choose for that creature to become immune to poison damage, the Poisoned condition, and any other types of poison. They are also resistant to necrotic damage, and can add their Wisdom modifier to death saving throws if they choose. A creature can only gain these benefits once, but they are permanent. 

After you gain this feature, the first time you die as a result of your Blood Magic, you come back to life in 24 hours with full hit points and the above features. You may only return to life this way once, and only if you were reduced to 0 hit points by Blood Magic with no failed death saving throws which originated from a creature attacking you or forcing you to fail one.

```
def level17(npc):
    npc.traits.append("***Divine Undeath: Raise Life.*** Those who you return to life are raised as more powerful beings than they were before. If you cast any spell that returns a creature to life, you can choose for that creature to become immune to poison damage, the Poisoned condition, and any other types of poison. They are also resistant to necrotic damage, and can add their Wisdom modifier to death saving throws if they choose. A creature can only gain these benefits once, but they are permanent.")

    npc.traits.append("***Divine Undeath: Back from the Dead.*** The first time you die as a result of your Blood Magic, you come back to life in 24 hours with full hit points and the above features. You may only return to life this way once, and only if you were reduced to 0 hit points by Blood Magic with no failed death saving throws which originated from a creature attacking you or forcing you to fail one.")
```