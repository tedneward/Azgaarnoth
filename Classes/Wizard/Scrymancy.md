# Arcane Tradition: Scrymancy
The scrymancers are the spies amongst the wizarding schools. While not as adroit with a blade as their roguish counterparts, they have just as many tools to stay out of sight. Focused on gathering information they can use to expand their spell list and help their allies gain a tactical advantage, these divination-leaning wizards are readily employed by any entity that values security, knowledge, or tracking.

Scrymancers are highly sought after by a variety of parties: in addition to the [Silent Tower](../../Organizations/MageSchools/SilentTower.md) school, the [Noble Houses](../../Organizations/Houses/Houses.md) seek scrymancers to gain an upper hand on their rivals (and allies) in the Great Game, [Rogues Guilds](../../Organizations/RoguesGuilds/RoguesGuilds.md) are always looking for those that can help them plan a job, [Militant Orders](../../Organizations/MilitantOrders/MilitantOrders.md) and [Mercenary Companies](../../Organizations/MercCompanies/MercCompanies.md) often need up-to-the-moment intelligence, and so on.  

```
name = 'Scrymancy'
description = "***Arcane Tradition: Scrymancy.*** The scrymancers are the spies amongst the wizarding schools. While not as adroit with a blade as their roguish counterparts, they have just as many tools to stay out of sight. Focused on gathering information they can use to expand their spell list and help their allies gain a tactical advantage, these divination-leaning wizards are readily employed by any entity that values security, knowledge, or tracking."
```

## Eyes That See
*2nd-level Scrymancy feature*

You learn little tricks to see the hidden. You add the [faerie fire](../../Magic/Spells/faerie-fire.md) spell to your spellbook.

```
def level2(npc):
    npc.spellbook.append('faerie fire')
```

## Stealthy Casting
*2nd-level Scrymancy feature*

You've learned how to cast spells without being detected. As part of casting a spell, you can make a Dexterity (Stealth) check. All creatures with a passive Perception lower than the total of your roll do not notice you casting the spell. You gain proficiency in the Stealth skill if you don't already have it, and casting a spell only reveals your position if you inflict damage on a creature or object.

```
    npc.traits.append("***Stealthy Casting.*** As part of casting a spell, you can make a Dexterity (Stealth) check. All creatures with a passive Perception lower than the total of your roll do not notice you casting the spell. Casting a spell only reveals your position if you inflict damage on a creature or object.")
    
    if 'Stealth' not in npc.proficiencies:
        npc.proficiencies.append('Stealth')
```

## The power of Sight
*6th-level Scrymancy feature*

When you use a divination spell to detect a creature you wouldn't otherwise be able to see or hear, you also gain a glimpse into the creature's mind. You gain a vague notion of their current motivation or goal.

For the next 8 hours, you have advantage on Charisma (Persuasion), Charisma (Intimidation), and Charisma (Deception) checks against that creature. You can only affect one creature at a time with this feature, and targeting a new creature with this feature ends the effect on the current creature.

```
def level6(npc):
    npc.traits.append("***Power of Sight.*** When you use a divination spell to detect a creature you wouldn't otherwise be able to see or hear, you also gain a glimpse into the creature's mind. You gain a vague notion of their current motivation or goal. For the next 8 hours, you have advantage on Charisma (Persuasion), Charisma (Intimidation), and Charisma (Deception) checks against that creature. You can only affect one creature at a time with this feature, and targeting a new creature with this feature ends the effect on the current creature.")
```

## Your Sight is Mine
*10th-level Scrymancy feature*

When a creature fails a saving throw against a spell you cast, you can use a bonus action to force the creature to make a Constitution saving throw or be blinded for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. You can use this ability a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses of this ability when you finish a long rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Your Sight is Mine ({npc.INTbonus()}/Recharges on long rest).*** When a creature fails a saving throw against a spell you cast, you force the creature to make a Constitution saving throw or be blinded for 1 minute. The creature can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.") )
```

## Eyes of the Magi
*14th-level Scrymancy feature*

Your spells fuel your perception. When you cast a divination spell, for 1 minute, you gain truesight out to a range of 60 feet. You also gain advantage on Wisdom (Perception) checks for that duration. Alternatively, you can transfer this power to another creature that you can touch, but only one creature can benefit from this effect at a time. You cannot use this ability again until you finish a short or long rest.

```
def level14(npc):
    npc.traits.append("***Eyes of the Magi (Recharges on short or long rest).*** When you cast a divination spell, for 1 minute, you gain truesight out to a range of 60 feet. You also gain advantage on Wisdom (Perception) checks for that duration. Alternatively, you can transfer this power to another creature that you can touch, but only one creature can benefit from this effect at a time.")
```

---

# Scrymancy Spells

## Cantrips
* [piercing vision](../../Magic/Spells/piercing-vision.md)

## 3rd-level
* [x-ray vision](../../Magic/Spells/x-ray-vision.md)

## 6th-level
* [greater darkness](../../Magic/Spells/greater-darkness.md)

## 7th-level
* [predict action](../../Magic/Spells/predict-action.md)

## 8th-level
* [greater telepathic bond](../../Magic/Spells/greater-telepathic-bond.md)

