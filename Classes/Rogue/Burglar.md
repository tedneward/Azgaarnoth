# Roguish Archetype: Burglar
Most burglars are much more than robbers in the night. They have their sights on much more than the baubles and trinkets that they would get out of a neighbor's safe, or even than the treasures they would find in a noble's vault. Burglars aspire for hoards of legendary proportion: ancient tombs containing kingly treasure, the lost riches of a dwarven city, or even a dragon's hoard. The challenge is every bit as rewarding as the loot, and many a burglar has gotten caught only because they chose one challenge too far, not because they needed the money, but because they wanted to astound with their skill.

```
name = 'Burglar'
description = "***Roguish Archetype: Burglar.*** Most burglars are much more than robbers in the night. They have their sights on much more than the baubles and trinkets that they would get out of a neighbor's safe, or even than the treasures they would find in a noble's vault. Burglars aspire for hoards of legendary proportion: ancient tombs containing kingly treasure, the lost riches of a dwarven city, or even a dragon's hoard. The challenge is every bit as rewarding as the loot, and many a burglar has gotten caught only because they chose one challenge too far, not because they needed the money, but because they wanted to astound with their skill."
```

## Darkvision
*3rd=level Burglar feature*

You are used to working in dark conditions, because of the nature of your work. You gain darkvision out to 30 feet. If you already have darkvision, its range extends by 30 feet.

```
def level3(npc):
    if 'darkvision' in npc.senses: npc.senses['darkvision'] += 30
    else: npc.senses['darkvision'] = 30
```

## Detect Treasure
*3rd-level Burglar feature*

The nature of your work has also gifted you with the ability to innately sense the location of treasure near you. You can use an action to detect the location of Medium or smaller objects that are worth 100 gp or more, out to a range of 30 feet, for the next 10 minutes. 

This ability can penetrate most barriers, but is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt. 

When you use this ability, you cannot do so again until you finish a long rest.

```
    npc.actions.append("***Detect Treasure (Recharges on long rest).*** You can detect the location of Medium or smaller objects that are worth 100 gp or more, out to a range of 30 feet, for the next 10 minutes. This ability can penetrate most barriers, but is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt.")
```

## Deep Pockets
*9th-level Burglar feature*

You have learned to magically enhance your pockets or other containers to contain all of the loot you carry. During a long rest, you can enchant one container on your person, usually a pocket or backpack, but other containers can work with the DM's consent. This container becomes the equivalent of a bag of holding for you.

You can enchant a different container over the course of a long rest. If you do so, the previous container loses its magic.

If the container is filled above its capacity, if there are still items in the container when you enchant a different one, or if the container is targeted by a spell such as dispel magic or antimagic field, all of its contents spill out around you, landing in an empty adjacent space.

When you reach 17th level, you can have two containers enchanted simultaneously.

```
def level9(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Deep Pockets.*** During a long rest, you can enchant {'one container' if npc.levels() < 17 else 'two containers'} on your person, usually a pocket or backpack that becomes the equivalent of a *bag of holding* for you. You can enchant a different container over the course of a long rest. If you do so, the first container loses its magic. If the container is filled above its capacity, if there are still items in the container when you enchant a different one, or if the container is targeted by a spell such as dispel magic or antimagic field, all of its contents spill out around you, landing in an empty adjacent space."))
```

## Trap Sense
*13th-level Burglar feature*

You have enough experience fighting through dungeons to know that monsters aren't the only threat, so you are always on your toes. You gain the following benefits:

* If you succeed on an Investigation ability check to determine how a trap works by 5 or more, you and your allies can safely bypass the trap without triggering or disarming it.
* You have advantage on saving throws against traps and their effects.
* Traps make attack rolls against you with disadvantage.

```
def level13(npc):
    npc.traits.append("***Trap Sense: Investigation.*** If you succeed on an Investigation ability check to determine how a trap works by 5 or more, you and your allies can safely bypass the trap without triggering or disarming it.")

    npc.traits.append("***Trap Sense: Evasion.*** You have advantage on saving throws against traps and their effects.")

    npc.traits.append("***Trap Sense: Dodge.*** Traps make attack rolls against you with disadvantage.")
```

## Disappear
*17th-level Burglar feature*

You have gained the ability to make yourself disappear from sight. You can cast [greater invisibility](../../Magic/Spells/greater-invisibility.md) once without expending a spell slot. Once you cast the spell in this way, you cannot do so again until you finish a long rest.

```
def level17(npc):
    npc.traits.append(f"***Disappear (Recharges on long rest).*** You have gained the ability to make yourself disappear from sight. You can cast {spelllinkify('greater invisibility')} once without expending a spell slot.")
```
