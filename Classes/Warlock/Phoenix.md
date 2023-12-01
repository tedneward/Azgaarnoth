# Otherworldly Patron: Great Phoenix
The source of your power is the cosmic force and greatest of winged creatures, the mighty Phoenix. A Phoenix often approaches those who have suffered, and overcome great trauma. They are noble creatures who do not easily pick the side of evil, but also respect and reward wrathful passion. Those that make a pact with a Phoenix are likely to be emotionally volatile, and unconcerned with consequence. The price phoenixes usually require from their warlocks is change. A Phoenix might demand a warlock to work towards the destruction of a corrupt government, in order to interpose a new order from its ashes. As far as warlock patrons go, the Phoenix is less prone to long term schemes. A goal a Phoenix had in mind might no longer interest it on a frequent, almost random basis.

```
name = 'Phoenix'
description = "***Otherworldly Patron: Great Phoenix.*** The source of your power is the cosmic force and greatest of winged creatures, the mighty Phoenix. A Phoenix often approaches those who have suffered, and overcome great trauma. They are noble creatures who do not easily pick the side of evil, but also respect and reward wrathful passion. Those that make a pact with a Phoenix are likely to be emotionally volatile, and unconcerned with consequence. The price phoenixes usually require from their warlocks is change. A Phoenix might demand a warlock to work towards the destruction of a corrupt government, in order to interpose a new order from its ashes. As far as warlock patrons go, the Phoenix is less prone to long term schemes. A goal a Phoenix had in mind might no longer interest it on a frequent, almost random basis."
```

## Expanded Spell List
At the following levels these spells become available for you to select as warlock spells

**Phoenix Spells**

Spell Level|Spells
-------------|------
1st | Burning hands, Purify food and drink
2nd | Continual flame, Dragons breath, Scorching ray
3rd | Fireball, Revivify
4th | Elemental Bane, Wall of Fire
5th | Immolation, Reincarnate

```
def level1(npc):
    npc.traits.append(f"***Expanded Spell List.*** The following spells are added to the warlock spell list for you: 1st: {spelllinkify('burning hands')}, {spelllinkify('purify food and drink')}; 2nd: {spelllinkify('continual flame')}, {spelllinkify('dragons breath')}, {spelllinkify('scorching ray')}; 3rd: {spelllinkify('fireball')}, {spelllinkify('revivify')}; 4th: {spelllinkify('elemental bane')}, {spelllinkify('wall of fire')}; 5th: {spelllinkify('immolation')}, {spelllinkify('reincarnate')}")
```

## Phoenix Cantrips
*1st-level Phoenix patron feature*

You gain the cantrip [control flames](../../Magic/Spells/control-flames.md), this does not count against the amount of cantrips you know. You may also replace the cantrip "Eldritch Blast" with the "Firebolt" cantrip, if you take an invocation that alters Eldritch Blast, it instead can be applied to your Firebolt cantrip. You can take both Eldritch Blast and Firebolt, but you must choose which one your Eldritch Invocations will affect when you gain the invocation. You can take the same invocation twice if you wish for both cantrips to recieve the effect.

```
    npc.pactmagic.cantripsknown.append('control flames')
```

## Fires of the Phoenix
*1st-level Phoenix patron feature*

You have a measure of aptitude with your patron's flames. Any time you cast a spell of first level or higher that deals fire damage you may choose to roll one hit dice. You can choose to add this roll to your spell's damage, or heal yourself that amount. You must choose which of these features to use before you make an attack roll, or before a creature makes a saving throw to resist your spell. When you roll a hit dice using this feature it is expended as if you used it during a short rest.

```
    npc.traits.append("***Fires of the Phoenix.*** Any time you cast a spell of first level or higher that deals fire damage you may choose to roll one hit dice. You can choose to add this roll to your spell's damage, or heal yourself that amount. You must choose which of these features to use before you make an attack roll, or before a creature makes a saving throw to resist your spell. When you roll a hit dice using this feature it is expended as if you used it during a short rest.")
```

## Soul Fire
*6th-level Phoenix patron feature*

You can use your own vitality to power your flames. You can cast a 1st- or 2nd-level spell that deals fire damage without using a spell slot. To do so you must sacrifice an amount of hitpoints equal to the spells level x 10, this damage is necrotic damage and cannot be reduced in any way. The spell can only be cast at its default level. 

In addition, any time you roll hit dice to heal yourself, the result cannot be lower than half the hit dice maximum roll (4 on a d8). You can use your "Fires of the Phoenix" ability in conjunction with spells cast this way.

```
def level6(npc):
    npc.actions.append("***Soul Fire.*** You can cast a 1st- or 2nd-level spell that deals fire damage without using a spell slot. To do so you must sacrifice an amount of hit points equal to the spells level x 10. This damage is necrotic damage and cannot be reduced in any way. The spell can only be cast at its default level.")
    npc.traits.append("***Soul Fire.*** Any time you roll hit dice to heal yourself, the result cannot be lower than half the hit dice maximum roll (4 on a d8). You can use Fires of the Phoenix in conjunction with spells cast this way.")
```

## Arcane Blaze
*6th-level Phoenix patron feature*

You may pick two spells from any spell list that deal fire damage and can cast them using a warlock spell slot. These spells do not count against your spells known, and they do count as warlock spells. You may replace one of these spells with a different one at 7th and 9th level. in addition, when you choose your mystic arcanum at 11th, 13th, 15th, and 17th level they may also be from any classes spell list, as long as they deal fire damage.

```
    npc.pactmagic.spellsknown.append("CHOOSE any fire spell")
    npc.pactmagic.spellsknown.append("CHOOSE any fire spell")
```

## Rise From The Ashes
*10th-level Phoenix patron feature*

If you die you can be reborn from fire. At the moment of your death your corpse (if one exists) bursts violently into flames. All creatures within 20 feet of your corpse must make a dexterity saving throw equal to your spell save DC, taking 6d6 fire damage on a failed save, half on a success. Your corpse is reduced to ashes. In 1d4 days you will be returned to life as if by the reincarnate spell in the current location of your ashes. If your ashes are scattered or destroyed the amount of time it takes to return to life is doubled, and you resurrect in the exact location you died. You are returned to life with half of your maximum hitpoints, and half of your warlock spell slots (rounded down) once you are brought back to life this way, you cannot use this feature for another 1d6+6 days. Any other creatures that are killed by the fire damage of this ability are resurrected in the same way.

```
def level10(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Rise From the Ashes (Recharges in 1d6 +6 days).*** At the moment of your death your corpse (if one exists) bursts violently into flames. All creatures within 20 feet of your corpse must make a Dexterity saving throw (DC {npc.pactmagic.spellsavedc()}), taking 6d6 fire damage on a failed save, half on a success. Your corpse is reduced to ashes. In 1d4 days you will be returned to life as if by the {spelllinkify('reincarnate')} spell in the current location of your ashes. If your ashes are scattered or destroyed the amount of time it takes to return to life is doubled, and you resurrect in the exact location you died. You are returned to life with {npc.hitpoints // 2} hit points, and half of your warlock spell slots (rounded down). Any other creatures that are killed by the fire damage of this ability are resurrected in the same way.") )
```

## Phoenix Flight
*14th-level Phoenix patron feature*

You may use an action to sprout wings of flame from your back. The wings last one hour, or until you dismiss them. While your wings are active you gain a flying speed of 50 feet and resistance to fire damage. Hostile creatures within 15 feet of you take 1d4 fire damage at the start of their turn, or when they enter the range for the first time. Allied creatures within range (including yourself) are healed 1d4 points at the start of their turns or when they first enter the aura. While This ability is active you can cast third level spells using your Soul Fire ability. If you die while this feature is active you resurrect using your Rise From The Ashes feature immediately, if it is available to you. You must finish a long rest before using this feature again.

```
def level14(npc):
    npc.actions.append("***Phoenix Flight (Recharges on long rest).*** You sprout wings of flame from your back. The wings last one hour, or until you dismiss them. While your wings are active you gain a flying speed of 50 feet and resistance to fire damage. Hostile creatures within 15 feet of you take 1d4 fire damage at the start of their turn, or when they enter the range for the first time. Allied creatures within range (including yourself) are healed 1d4 points at the start of their turns or when they first enter the aura. While this ability is active you can cast third level spells using Soul Fire. If you die while this feature is active you resurrect using Rise From The Ashes immediately, if it is available to you.")
```
