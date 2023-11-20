# Bardic College: College of Dragonsong
It is said that the dragons taught the first bards of this college the songs and secrets directly, shortly before they faded into obscurity after the Fall. Others say that the metallic dragons return periodically, polymorphed, to teach bards the ways of this college before returning back into mystery. Others believe that the college is entirely the work of chromatic dragons and the [Cult of the Wyrm](../../Organizations/CultOfTheWyrm.md), particularly since some of the bards who study this college espouse ideals that are far from those demonstrated by the [Draconic Orders](../../Organizations/MilitantOrders/DraconicOrder).

Depending on the society, bards who are members of this college are regarded with either awe or fear. Barbarian tribes in particular seem to hold them in high esteem, while many human settlements will hardly listen to a single tune from them. Both perspectives are fair, as a bard of the College of Dragonsong could go either way. A villainous bard has the potential to rule through oppression and fear, emulating a draconic tyrant, while a heroic bard has the potential to protect with the determination of a benevolent metallic dragon.

```
name = 'College of Dragonsong'
description = "***Bardic College: College of Dragonsong.*** Depending on the society, bards who are members of this college are regarded with either awe or fear. Barbarian tribes in particular seem to hold them in high esteem, while many human settlements will hardly listen to a single tune from them. Both perspectives are fair, as a bard of the College of Dragonsong could go either way. A villainous bard has the potential to rule through oppression and fear, emulating a draconic tyrant, while a heroic bard has the potential to protect with the determination of a benevolent metallic dragon."
```

## Song of Strength
*3rd-level College of Dragonsong feature*

You learn to imbue yourself and your allies with great physical power. As a bonus action, you can expend one Bardic Inspiration to sing the dragonsong of strength. Choose a number of creatures up to your Charisma modifier, within 60 feet of you that can hear you. Those creatures have their Strength score increased by 2. This lasts for as long as you maintain concentration (as if concentrating on a spell), for up to one minute.

The amount of the Strength bonus increases as you gain levels in this class, increasing to +4 at 6th level, and +5 at 14th level. This ability cannot increase a creature's Strength score over 22.

```
def level3(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Song of Strength.*** You expend one Bardic Inspiration to sing the dragonsong of strength. Choose up to {npc.CHAbonus()} creatures within 60 feet of you that can hear you. Those creatures have their Strength score increased by {2 if npc.levels('Bard') < 6 else 4 if npc.levels('Bard') < 14 else 5}. This ability cannot increase a creature's Strength score over 22. This lasts for as long as you maintain concentration (as if concentrating on a spell), for up to one minute.") )
```

## Song of Compulsion
*3rd-level College of Dragonsong feature*

You can attempt to persuade a group of creatures to act in a certain way. As an action, you can expend one Bardic Inspiration to sing the dragonsong of compulsion. Choose a number of creatures up to your Charisma modifier, within 60 feet of you and that can hear you. Each of those creatures must succeed on a Wisdom saving throw against your spell save DC or be affected as if by a [suggestion](../../Magic/Spells/suggestion.md) spell. A creature who succeeds this saving throw has no idea that you tried to influence it.

```
    npc.defer(lambda npc: npc.actions.append(f"***Song of Compulsion.*** You expend one Bardic Inspiration to sing the dragonsong of compulsion. Choose up to {npc.CHAbonus()} creatures within 60 feet of you that can hear you. Each of those creatures must succeed on a Wisdom saving throw (DC {8 + npc.CHAbonus() + npc.proficiencybonus}) or be affected as if by a {spelllinkify('suggestion')} spell. A creature who succeeds this saving throw has no idea that you tried to influence it.") )
```

## Song of Fear
*6th-level College of Dragonsong feature*

Your dragonsong can inspire fear in your enemies. You can use an action to invoke the dragonsong of fear. When you do so, choose a number of creatures up to your Charisma modifier, within 60 feet of you and that can hear you. Each of those creatures must succeed on a Wisdom saving throw against your spell save DC or be affected as if by a fear spell.

Once you invoke this dragonsong, you cannot do so again until you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Song of Fear (Recharges on long rest).*** Choose up to {npc.CHAbonus()} creatures within 60 feet of you that can hear you. Each of those creatures must succeed on a Wisdom saving throw (DC {8 + npc.CHAbonus() + npc.proficiencybonus}) or be affected as if by a {spelllinkify('fear')} spell.") )
```

## Song of Flight
*14th-level College of Dragonsong feature*

You can use your dragonsong to grant yourself and your allies flight. You can use an action to invoke the dragonsong of flight. When you do so, you cast fly on yourself and a number of creatures up to your Charisma modifier that are within 30 feet of you and that can hear you.

Once you invoke this dragonsong, you cannot do so again until you finish a long rest.

```
def level14(npc):
    npc.defer(lambda npc: npc.actions.append("***Song of Flight (Recharges on long rest).*** You cast {spelllinkify('fly')} on yourself and up to {npc.CHAbonus()} other creatures that are within 30 feet of you and can hear you.") )
```
