# Otherworldly Patron: The Witch(es)
Your patron is a powerful hag, usually a Grandmother hag, or even a coven of hags, which has taken an interest in your life. Hags are defined by their love of misery in other creatures, which often means they will only take on students and warlocks when the net suffering to be gained in the long run seems more than likely to offset the inconvenience. Some hags will even go so far as to blackmail or bribe certain influential figures into accepting a warlock pact, as part of some grand unknowable scheme, or perhaps to complete a coven. All forms of hags are able to grant pacts in this manner, and on rare occasions an entire coven of lesser hags will use their magic to grant a warlock pact to some unfortunate individual.

```
name = 'Witch'
description = "***Otherworldly Patron: The Witch(es).*** Your patron is a powerful hag, usually a Grandmother hag, or even a coven of hags, which has taken an interest in your life. Hags are defined by their love of misery in other creatures, which often means they will only take on students and warlocks when the net suffering to be gained in the long run seems more than likely to offset the inconvenience. Some hags will even go so far as to blackmail or bribe certain influential figures into accepting a warlock pact, as part of some grand unknowable scheme, or perhaps to complete a coven. All forms of hags are able to grant pacts in this manner, and on rare occasions an entire coven of lesser hags will use their magic to grant a warlock pact to some unfortunate individual."
```

## Expanded Spell List
The Hag lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock list for you.

Spell Level | Spells
----------- | ---------
1st | speak with animals, sleep
2nd | pass without trace, alter self
3rd | bestow curse, tiny servant
4th | fabricate, polymorph
5th | animate objects, legend lore

```
def level1(npc):
    npc.traits.append(f"***Expanded Spell List.*** The following spells are added to the warlock list for you: 1st: {spelllinkify('speak with animals')}, {spelllinkify('sleep')}; 2nd: {spelllinkify('pass without trace')}, {spelllinkify('alter self')}; 3rd: {spelllinkify('bestow curse')}, {spelllinkify('tiny servant')}; 4th: {spelllinkify('fabricate')}, {spelllinkify('polymorph')}; 5th: {spelllinkify('animate objects')}, {spelllinkify('legend lore')}")
```

## Bonus Cantrips
*1st-level Witch feature*

You gain the [dancing lights](../../Magic/Spells/dancing-lights.md) and [vicious mockery](../../Magic/Spells/vicious-mockery.md) cantrips. They count as warlock cantrips for you, but they don't count against your number of cantrips known.

```
    npc.pactmagic.cantripsknown.append('dancing lights')
    npc.pactmagic.cantripsknown.append('vicious mockery')
    npc.traits.append("***Bonus Cantrips.*** *dancing lights* and *vicious mockery* do not count against your number of cantrips known.")
```

## Weird Magic
*1st-level Witch feature*

You are privy to many strange and unusual secrets of magic known only to the hag sisterhood. Once per day, you may cast a spell of a level you are able to cast from your class list that you do not know. You must use a spell slot and fulfil all other requirements. Casting this spell should involve some bizarre and unusual prop, such as releasing a swarm of bees for a cloud of daggers spell. Once you have cast a spell with this ability, you can never cast it again for any reason.

```
    npc.actions.append("***Weird Magic (1/Day).*** You may cast a spell of a level you are able to cast from your class list that you do not know. You must use a spell slot and fulfil all other requirements. Casting this spell should involve some bizarre and unusual prop, such as releasing a swarm of bees for a *cloud of daggers* spell. Once you have cast a spell with this ability, you can never cast it again for any reason.")
```

## Strange Conveyance
*6th-level Witch feature*

You learn to enchant an object to serve as your mount. You can choose an object as small as a broom up to the size of a cow, and enchanting that object takes 1 hour. When you straddle the object, it hovers beneath you and can be ridden in the air. The object has a flying speed of 50 feet. It can carry up to 400 pounds, but its flying speed becomes 30 feet while carrying over 200 pounds. It stops hovering when you land. You may only have one Strange Conveyance at any one time, and you may not create a new Conveyance whilst the other remains extant.

```
def level6(npc):
    npc.traits.append("***Strange Conveyance.*** You can choose an object as small as a broom up to the size of a cow, and enchanting that object takes 1 hour. When you straddle the object, it hovers beneath you and can be ridden in the air. The object has a flying speed of 50 feet. It can carry up to 400 pounds, but its flying speed becomes 30 feet while carrying over 200 pounds. It stops hovering when you land. You may only have one Strange Conveyance at any one time, and you may not create a new Conveyance whilst the other remains extant.")
```

## The Rule of Three
*10th-level Witch feature*

You understand the only rule that matters -- magic is stronger in threes. When you cast a spell, you may choose to cast it three times instead of once as part of the same action. You may choose new targets for these copies. You must finish a long rest before using this ability again. 

```
def level10(npc):
    npc.actions.append("***The Rule of Three (Recharges on long rest).*** When you cast a spell, you may choose to cast it three times instead of once as part of the same action. You may choose new targets for these copies.")
```

## Exit strategy
*14th-level Witch feature*

You develop an (almost) foolproof method to remove yourself from a dangerous situation, should the need arise. You can use an action to vanish in a suitably dramatic manner (perhaps into a cloud of smoke or a swarm of toads) reappearing 1d4 hours later in a place of emotional significance to you on the same plane of existence. If no such place exists, the DM decides where you appear.

```
def level14(npc):
    npc.actions.append("***Exit Strategy.*** You can use an action to vanish in a suitably dramatic manner (perhaps into a cloud of smoke or a swarm of toads) reappearing 1d4 hours later in a place of emotional significance to you on the same plane of existence. If no such place exists, the DM decides where you appear.")
```
