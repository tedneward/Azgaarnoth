# Arcane Tradition: Kinetics
Among the most in tune with how the Weave can enhance movement, the kineticist focuses on magic used to manipulate space, and movement within it. Telekinesis, teleportation, and enhanced movement are all among this wizard's storehouse, and they are valuable assets in any army or adventuring party, helping to ensure movement over great distances in a short period of time.

Kineticists are often found in the [Shining Door](../../Organizations/MageSchools/ShiningDoor.md) school, and often contract out to [mercenary companies](../../Organizations/MercCompanies/index.md). 

```
name = 'Kinetics'
description = "***Arcane Tradition: Kinetics.*** Among the most in tune with how the Weave can enhance movement, the kineticist focuses on magic used to manipulate space, and movement within it. Telekinesis, teleportation, and enhanced movement are all among this wizard's storehouse, and they are valuable assets in any army or adventuring party, helping to ensure movement over great distances in a short period of time."
```

## Spell-Powered Avoidance
*2nd-level Kinetics feature*

Your movement speed increases by 5 feet. When you cast a spell, you can use your reaction to move 5 feet without provoking an opportunity attack.

```
def level2(npc):
    npc.speed['walking'] += 5
    npc.reactions.append("***Spell-Powered Avoidance.*** When you cast a spell, you move 5 feet without provoking an opportunity attack.")
```

## Stronghand Magic
*2nd-level Kinetics feature*

You know the [mage hand](../../Magic/Spells/mage-hand.md) cantrip and it doesn't count against the number of cantrips you know. The range of your [mage hand](../../Magic/Spells/mage-hand.md) increases to 60 feet, and it can carry up to 20 pounds.

```
    npc.spellcasting['Wizard'].cantripsknown.append('mage hand')
    npc.traits.append("***Stronghand Magic.*** The range of your *mage hand* spell increases to 60 feet, and it can carry up to 20 pounds.")
```

## Evasive Maneuver
*6th-level Kinetics feature*

You are more connected with the Weave, sensing which pathways are most easily traversed. As a reaction, when you are targeted by a spell attack or area of effect spell, you can use your reaction to cast [misty step](../../Magic/Spells/misty-step.md). If you were targeted by a melee attack or touch spell, the attack misses. If you were targeted by a ranged attack, the attacker has disadvantage, or they can choose a different target. You regain the use of this ability after finishing a short rest.

```
def level6(npc):
    npc.reactions.append(f"***Evasive Maneuver (Recharges on short rest).*** when you are targeted by a spell attack or area of effect spell, you use {spelllinkify('misty step')}. If you were targeted by a melee attack or touch spell, the attack misses. If you were targeted by a ranged attack, the attacker has disadvantage, or they can choose a different target.")
```

## Transportive Assault
*10th-level Kinetics feature*

When you cast [misty step](../../Magic/Spells/misty-step.md), you can bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you when you cast this spell. When you cast [misty step](../../Magic/Spells/misty-step.md), [dimension door](../../Magic/Spells/dimension-door.md), or any other spell that transports you across a distance, and you end in a space that is within five feet of any enemy, you or the creature you transported can use a reaction to make a single attack with a weapon you are holding, against the adjacent creature.

```
def level10(npc):
    npc.traits.append("***Transportive Assault.*** When you cast {spelllinkify('misty step')}, you can bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you when you cast this spell.")
    npc.reactions.append(f"***Transportive Assault.*** When you cast {spelllinkify('misty step')}, {spelllinkify('dimension door')}, or any other spell that transports you across a distance, and you end in a space that is within five feet of any enemy, you or the creature you transported can use a reaction to make a single attack with a weapon you are holding, against the adjacent creature.")
```

## Innate Transportation
*14th-level Kinetics feature*

Your [mage hand](../../Magic/Spells/mage-hand.md) can wield a single light melee weapon. As a bonus action, you can move the hand up to 30 feet to a location within range, or order it to attack. It is proficient with the same weapons that you have proficiency with and it has the same attack and damage bonuses that you have. When you use [misty step](../../Magic/Spells/misty-step.md), [dimension door](../../Magic/Spells/dimension-door.md), or similar spells, your mage hand is transported with you and appears in your space.

Finally, you can cast [misty step](../../Magic/Spells/misty-step.md) twice without using a spell slot, and [dimension door](../../Magic/Spells/dimension-door.md) once without expending a spell slot. You regain the ability to cast these two spells in this way when you finish a long rest.

```
def level14(npc):
    npc.bonusactions.append("***Innate Transportation.*** Your {spelllinkify('mage hand')} can wield a single light melee weapon, which you can move up to 30 feet to a location within range, or order it to attack. It is proficient with the same weapons that you have proficiency with, and it has the same attack and damage bonuses that you have. When you use {spelllinkify('misty step')}, {spelllinkify('dimension door')}, or similar spells, your mage hand is transported with you and appears in your space.")
    npc.actions.append("***Innate Transportation (Recharges on long rest).*** You can cast {spelllinkify('misty step')} twice without using a spell slot, and {spelllinkify('dimension door')} once without expending a spell slot.")
```

---

# Kinetic Spells

## Cantrips
* [fleet foot](../../Magic/Spells/fleet-foot.md)

## 2nd-level
* [elastic tether](../../Magic/Spells/elastic-tether.md)

## 3rd-lvel
* [portal sense](../../Magic/Spells/portal-sense.md)

## 8th-level
* [reverse teleportation](../../Magic/Spells/reverse-teleportation.md)

