# Divine Domain: Pain
Pain. All creatures know pain, and all pay homage to it with their tears, and their whispered pleas that they be spared it. Pain is not just physical - in fact, the adherents of gods who grant this portfolio understand that physical pain is perhaps the least dangerous of its brothers and sisters. Priests who exercise this domain use it with precision to achieve their goals, bring the world a catharsis which it has long been denied.

This domain is available to followers of [Diancecht](../../Religions/Pantheon/Diancecht.md), [Sekolah](../../Religions/Pantheon/Sekolah.md), ...

```
name = 'Pain'
description = "***Divine Domain: Pain.*** Pain. All creatures know pain, and all pay homage to it with their tears, and their whispered pleas that they be spared it. Pain is not just physical - in fact, the adherents of gods who grant this portfolio understand that physical pain is perhaps the least dangerous of its brothers and sisters. Priests who exercise this domain use it with precision to achieve their goals, bring the world a catharsis which it has long been denied."
```

## Domain spells
You gain domain spells at the cleric levels listed in the Pain Domain Spells table. See the Divine Domain class feature for how domain spells work.

Cleric Level | Pain Domain Spells
------------ | ------------------
1st | [bane](../../Magic/Spells/bane.md), [hellish rebuke](../../Magic/Spells/hellish-rebuke.md)
3rd | [cloud of daggers](../../Magic/Spells/cloud-of-daggers.md), [heat metal](../../Magic/Spells/heat-metal.md)
5th | [bestow curse](../../Magic/Spells/bestow-curse.md), [fear](../../Magic/Spells/fear.md)
7th | [phantasmal killer](../../Magic/Spells/phantasmal-killer.md), [staggering smite](../../Magic/Spells/staggering-smite.md)
9th | [synaptic static](../../Magic/Spells/synaptic-static.md), [geas](../../Magic/Spells/geas.md)

```
domainspells = {
    1: ['bane', 'hellish rebuke'],
    3: ['cloud of daggers', 'heat metal'],
    5: ['bestow curse', 'fear'],
    7: ['phatasmal killer', 'staggering smite'],
    9: ['synaptic static', 'geas']
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

## Sting
*1st-level Pain domain feature*

You can jab a creature with a distracting sting to foil their spellcasting. When a creature you can see within 30 feet of you attempts to cast a spell, you can use your reaction to force that creature to make a concentration saving throw at disadvantage. On a failed saving throw, the spell fails and is wasted. You can use this ability a number of times equal to your Wisdom modifier. Uses of this ability recharge at the end of a long rest.

```
    npc.defer(lambda npc: npc.reactions.append("***Sting ({npc.WISbonus()}/Recharges on long rest).*** When a creature you can see within 30 feet of you attempts to cast a spell, you force that creature to make a concentration saving throw at disadvantage. On a failed saving throw, the spell fails and {'is wasted' if npc.levels('Cleric') < 17 else 'backlashes on the caster, dealing 1d6 psychic damage to them per level of the spell being cast'}.") )
```

## Channel Divinity: Excrutiating Pain
*2nd-level Pain domain feature*

You can use your Channel Divinity to bombard a creature with pain. As an action, you present your holy symbol and target a creature you can see within 60 feet. That creature must succeed on a Constitution saving throw or become wracked with devastasting pain, whether that be physical or emotional. While the target is affected, any speed it has can be no higher than 10 feet. The target also has disadvantage on attack rolls, ability checks, and saving throws, other than Constitution saving throws. Finally, if the target tries to cast a spell, it must first succeed on a Constitution saving throw, or the casting fails and the spell is wasted. This effect lasts for 1 minute.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append("***Channel Divinity: Excrutiating Pain.*** Present your holy symbol and target a creature you can see within 60 feet. That creature must succeed on a Constitution saving throw (DC {spellcasting.spellsavedc()}) or become wracked with devastasting pain, whether that be physical or emotional. While the target is affected, any speed it has can be no higher than 10 feet. The target also has disadvantage on attack rolls, ability checks, and saving throws, other than Constitution saving throws. Finally, if the target tries to cast a spell, it must first succeed on a Constitution saving throw, or the casting fails and the spell is wasted. This effect lasts for 1 minute.") )
```

## Agony Pulse
*6th-level Pain domain feature*

You can project your pain outwards from yourself in a pulse of invasive energy. As an action, you emit a wave of pain that travels outwards to 30 feet of you. Each creature in the area immediately awakens if asleep, and must make a concentration saving throw to maintain any spells they are concentrating on. Additonally, creatures under the influence of any mind-affecting magic may attempt another saving throw against that magic. You can use this ability a number of times equal to your Wisdom modifier. Uses of this ability recharge at the end of a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append("***Agony Pulse ({npc.WISbonus()}/Recharges on long rest).*** You emit a wave of pain that travels outwards to 30 feet of you. Each creature in the area immediately awakens if asleep, and must make a concentration saving throw to maintain any spells they are concentrating on. Additonally, creatures under the influence of any mind-affecting magic may attempt another saving throw against that magic.") )
```

## Potent Spellcasting
*8th-level Pain domain feature*

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.traits.append("***Potent Spellcasting.*** You add your Wisdom modifier to the damage you deal with any cleric cantrip.")
```

## Hexing Vexation
*17th-level Pain domain feature*

When a creature fails to cast a spell due to your Sting feature, the failed spell backlashes on the caster, dealing 1d6 psychic damage to them per level of the spell being cast.
