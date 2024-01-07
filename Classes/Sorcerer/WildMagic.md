# Sorcerous Origin: Wild Magic
Your innate magic comes from the wild forces of chaos that underlie the order of creation. When you tap into your power, this chaos builds within and around you, yearning for any chance to slip into the world and take form--sometimes beneficial, sometimes harmful, sometimes just... weird.

You might have endured exposure to some form of raw magic, perhaps through a planar portal leading to Limbo, the Elemental Planes, or the mysterious Far Realm. Perhaps you were blessed by a powerful fey creature or marked by a demon. Or your magic could be a fluke of your birth, with no apparent cause or reason. However it came to be, this chaotic magic churns within you, waiting for any outlet.

```
name = 'Wild Magic'
description = "***Sorcerous Origin: Wild Magic.*** Your innate magic comes from the raw primordial cosmic force that underlies magic and the order of creation. When you tap into your power, this chaos builds within and around you, yearning for any chance to slip into the world and take form--sometimes beneficial, sometimes harmful, sometimes just... weird."
```

## Wild Magic Surge
*1st-level Wild Magic feature*

Your spellcasting can unleash surges of untamed magic. Immediately after you cast a sorcerer spell of 1st level or higher, roll a d20. If you roll a 1, roll on the [Individual Wild Magic Surge table](../../Magic/Wild.md#wild-magic-surge) to create a random magical effect. If you don't get a 1, the target goes up by a value equal to the level of the spell slot used; thus, after casting a *magic missile* spell with a 2nd-level slot, the next time, if you roll a 1 to 3, a surge happens. This represents the Wild Magic building inside you. Once a surge happens, reset this target number to 1.

```
def level1(npc):
    npc.traits.append("***Wild Magic Surge.*** Immediately after you cast a sorcerer spell of 1st level or higher, roll a d20. If you roll a 1, roll on the [Individual Wild Magic Surge table](http://azgaarnoth.tedneward.com/magic/wild/#wild-magic-surge) to create a random magical effect. If you don't get a 1, the target goes up by a value equal to the level of the spell slot used; thus, after casting a *magic missile* spell with a 2nd-level slot, the next time, if you roll a 1 to 3, a surge happens. This represents the Wild Magic building inside you. Once a surge happens, reset this target number to 1.")
```

## Tides of Chaos
*1st-level Wild Magic feature*

You can manipulate the forces of chance and chaos to gain advantage on one attack roll, ability check, or saving throw. Once you do so, you must finish a long rest before you can use this feature again.

Any time before you regain the use of this feature, the DM can have you roll on the [Individual Wild Magic Surge table](../../Magic/Wild.md#wild-magic-surge) immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature.

```
    npc.traits.append("***Tides of Chaos (Recharges on long rest or surge).*** You gain advantage on one attack roll, ability check, or saving throw. Any time before you regain the use of this feature, the DM can have you roll on the [Individual Wild Magic Surge table](http://azgaarnoth.tedneward.com/magic/wild/#wild-magic-surge) immediately after you cast a sorcerer spell of 1st level or higher. You then regain the use of this feature.")
```

## Embracing the Chaos
*6th-level Wild Magic feature*

Any time you are in a [wild magic zone](../../Magic/Wild.md#wild-magic-zones), when you cast a spell, roll a d20 and add your spell attack bonus; if it is above 25, you cast the spell without needing to use a spell slot. Doing this immediately triggers an [Area Wild Magic Surge](../../Magic/Wild.md#wild-magic-surge), however.

```
def level6(npc):
    npc.traits.append("***Embracing the Chaos.*** Any time you are in a [wild magic zone](http://azgaarnoth.tedneward.com/magic/wild/#wild-magic-zones), when you cast a spell, roll a d20 and add your spell attack bonus; if it is above 25, you cast the spell without needing to use a spell slot. Doing this immediately triggers an [Area Wild Magic Surge](http://azgaarnoth.tedneward.com/magic/wild/#wild-magic-surge), however.")
```

## Bend Luck
*6th-level Wild Magic feature*

You have the ability to twist fate using your wild magic. When another creature you can see makes an attack roll, an ability check, or a saving throw, you can use your reaction and spend 2 sorcery points to roll 1d4 and apply the number rolled as a bonus or penalty (your choice) to the creature's roll. You can do so after the creature rolls but before any effects of the roll occur.

```
    npc.reactions.append("***Bend Luck.*** When another creature you can see makes an attack roll, an ability check, or a saving throw, you spend 2 sorcery points to roll 1d4 and apply the number rolled as a bonus or penalty (your choice) to the creature's roll. You can do so after the creature rolls but before any effects of the roll occur.")
```

## Controlled Chaos
*14th-level Wild Magic feature*

You gain a modicum of control over the surges of your wild magic. Whenever you roll on the [Individual Wild Magic Surge table](../../Magic/Wild.md#wild-magic-surge), you can roll twice and use either number.

```
def level14(npc):
    npc.traits.append("***Controlled Chaos.*** You gain a modicum of control over the surges of your wild magic. Whenever you roll on the [Individual Wild Magic Surge table](../../Magic/Wild.md#wild-magic-surge), you can roll twice and use either number.")
```

## Chaotic Recovery
*14th-level Wild Magic feature*

While within a wild magic zone, you can spend an action and 1 sorcery point to gain back a spent spell slot; roll a d20 and add your spell attack bonus; if it is above 15 + the level of the spell slot you are trying to recover, you have recovered that spell slot. If the roll fails, the sorcery point is still spent.

```
    npc.actions.append("***Chaotic Recovery.*** While within a wild magic zone, you spend 1 sorcery point to gain back a spent spell slot. Roll a d20 and add your spell attack bonus; if it is above 15 + the level of the spell slot you are trying to recover, you have recovered that spell slot. If the roll fails, the sorcery point is still spent.")
```

## Spell Bombardment
*18th-level Wild Magic feature*

The harmful energy of your spells intensifies. When you roll damage for a spell and roll the highest number possible on any of the dice, choose one of those dice, roll it again and add that roll to the damage. You can use the feature only once per turn.

```
def level18(npc):
    npc.traits.append("***Spell Bombardment (1/turn).*** When you roll damage for a spell and roll the highest number possible on any of the dice, choose one of those dice, roll it again and add that roll to the damage.")
```
