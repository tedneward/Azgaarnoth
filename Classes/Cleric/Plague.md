# Divine Domain: Plague
Clerics of the Plague domain are conduits of disease, decay, and pestilence. They wield the power of sickness to weaken their enemies and bring suffering to those who oppose them.

This domain is available to followers of ...

```
name = 'Plague'
description = "***Divine Domain: Plague.*** Clerics of the Plague domain are conduits of disease, decay, and pestilence. They wield the power of sickness to weaken their enemies and bring suffering to those who oppose them."
```

## Domain spells
You gain domain spells at the cleric levels listed in the Pain Domain Spells table. See the Divine Domain class feature for how domain spells work.

Cleric Level | Plague Domain Spells
------------ | ------------------
1st | ray of sickness, inflict wounds
3rd | cloud of daggers, blindness/deafness
5th | stinking cloud, contagion
7th | blight, confusion
9th | insect plague, cloudkill

Additionally, you learn the [poison spray](../../Magic/Spells/poison-spray.md) cantrip, which counts as a cleric cantrip for you.

```
domainspells = {
    1: ['ray of sickness', 'inflict wounds'],
    3: ['cloud of daggers', 'blindness-deafnes'],
    5: ['stinking cloud', 'contagion'],
    7: ['blight', 'confusion'],
    9: ['insect plague', 'cloudkill']
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

    spellcasting.cantripsknown.append('poison spray')
```

## Bonus Proficiency
*1st-level Plague domain feature*

You gain proficiency in the Medicine skill.

```
    npc.proficiencies.append('Medicine')
```

## Plaguebearer
*1st-level Plague domain feature*

Your touch can inflict disease. When you hit a creature with a melee attack, you can choose to inflict a disease on the target. The target must succeed on a Constitution saving throw or become infected with a disease of your choice from the [list of Tier 1 diseases](../../Conditions/Diseased.md#tier-one-diseases).

```
    npc.defer(lambda npc: npc.traits.append(f"***Plaguebearer.*** When you hit a creature with a melee attack, you can choose to inflict a disease on the target. The target must succeed on a Constitution saving throw (DC {spellcasting.spellsavedc()}) or become infected with a disease of your choice from the [list of Tier 1 diseases](http://azgaarnoth.tedneward.com/conditions/diseased/#tier-one-diseases).") )
```

## Channel Divinity: Plague’s Embrace
*2nd-level Plague domain feature*

You can use your Channel Divinity to invoke the power of pestilence. As an action, you present your holy symbol and select a creature you can see within 30 feet of you. The target must make a Constitution saving throw or be affected by a [Tier 1 disease of your choice](../../Conditions/Diseased.md#tier-one-diseases). The target can repeat the saving throw at the end of each of its turns, ending the effect on a success.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Plague's Embrace.*** You present your holy symbol and select a creature you can see within 30 feet of you. The target must make a Constitution saving throw (DC {spellcasting.spellsavedc()}) or be affected by a [Tier 1 disease of your choice](http://azgaarnoth.tedneward.com/conditions/diseased/#tier-one-diseases). The target can repeat the saving throw at the end of each of its turns, ending the effect on a success.") )
```

## Aura of Decay
*6th-level Plague domain feature*

You emanate an aura of decay that weakens your enemies. The aura extends 10 feet from you, and any enemy creature that starts its turn within this aura takes necrotic damage equal to your cleric level. This damage ignores resistance and immunity to necrotic damage.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Aura of Decay.*** You emanate an aura of decay that extends 10 feet from you, and any enemy creature that starts its turn within this aura takes {npc.levels('Cleric')} necrotic damage. This damage ignores resistance and immunity to necrotic damage.") )
```

## Divine Strike
*8th-level Plague Domain feature*

You gain the ability to infuse your weapon strikes with necrotic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 necrotic damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} necrotic damage to the target.") )
```

## Epidemic Infusion
*17th-level Plague domain feature*

Your mastery of diseases reaches its peak. As an action, you can choose a number of creatures equal to your Wisdom modifier within 60 feet of you and infuse them with contagious diseases. Each target must make a Constitution saving throw. On a failed save, a target is affected by a disease of your choice from the [Tier-2 list of diseases](../../Magic/Conditions/Diseased.md#tier-two-diseases). On a successful save, a target is unaffected. Once you use this feature, you can’t use it again until you finish a long rest.

```
def level17(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Epidemic Infusion.*** You choose {npc.WISbonus()} creatures within 60 feet of you and infuse them with contagious diseases. Each target must make a Constitution saving throw (DC {spellcasting.spellsavedc()}). On a failed save, a target is affected by a disease of your choice from the [Tier-2 list of diseases](https://azgaarnoth.tedneward.com/conditions/diseased/#tier-two-diseases). On a successful save, a target is unaffected.") )
```
