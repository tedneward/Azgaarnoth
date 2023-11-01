# Monastic Tradition: Way of the Sun Soul
Monks of the Way of the Sun Soul learn to channel their own life energy into searing bolts of light. They teach that meditation can unlock the ability to unleash the indomitable light shed by the soul of every living creature.

Many of these monks are found in the desert of [Al'Uma](../../Geography/AlUma.md), both for the metaphorical light of the Prophet and/or his Disciple, as well as for the presence of the sun itself.

```
name = 'Way of the Sun Soul'
description = "***Monastic Tradition: Way of the Sun Soul.*** Monks of the Way of the Sun Soul learn to channel their own life energy into searing bolts of light. They teach that meditation can unlock the ability to unleash the indomitable light shed by the soul of every living creature."
```

## Radiant Sun Bolt
*3rd-level Way of the Sun Soul feature*

You can hurl searing bolts of magical radiance.

You gain a new attack option that you can use with the Attack action. This special attack is a ranged spell attack with a range of 30 feet. You are proficient with it, and you add your Dexterity modifier to its attack and damage rolls. Its damage is radiant, and its damage die is a d4. This die changes as you gain monk levels, as shown in the Martial Arts column of the Monk table.

```
def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Radiant Sun Bolt.*** *Ranged Spell Attack:* +{npc.proficiencybonus() + npc.DEXbonus()} to hit, range 30, one target. Hit: 1d{npc.martialartsdie} + {npc.DEXbonus()} radiant damage.") )
```

When you take the Attack action on your turn and use this special attack as part of it, you can spend 1 ki point to make the special attack twice as a bonus action.

```
    npc.bonusactions.append("***Radiant Sun Bolt.*** You spend 1 ki point to make another Radiant Sun Bolt attack when you take the Attack action on your turn and use your Radiant Sun Bolt as one of the attacks.")
```

When you gain the Extra Attack feature, this special attack can be used for any of the attacks you make as part of the Attack action.

## Searing Arc Strike
*6th-level Way of the Sun Soul feature*

You gain the ability to channel your ki into searing waves of energy. Immediately after you take the Attack action on your turn, you can spend 2 ki points to cast the Burning Hands spell as a bonus action.

You can spend additional ki points to cast Burning Hands as a higher level spell. Each additional ki point you spend increases the spell's level by 1. The maximum number of ki points (2 plus any additional points) that you can spend on the spell equals half your monk level.

```
def level6(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Searing Arc Strike.*** You spend 2 ki points to cast  {spelllinkify('burning hands')} immediately after you take the Attack action on your turn. You can spend additional ki points to cast it at a higher level, 1 ki point increasing the spell's level by 1, up to a maximum total ki point cost of {npc.levels('Monk') // 2}.") )
```

## Searing Sunburst
*11th-level Way of the Sun Soul feature*

You gain the ability to create an orb of light that erupts into a devastating explosion. As an action, you magically create an orb and hurl it at a point you choose within 150 feet, where it erupts into a sphere of radiant light for a brief but deadly instant.

Each creature in that 20-foot-radius sphere must succeed on a Constitution saving throw or take 2d6 radiant damage. A creature doesn't need to make the save if the creature is behind total cover that is opaque.

You can increase the sphere's damage by spending ki points. Each point you spend, up to a maximum of 3, increases the damage by 2d6.

```
def level11(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Searing Sunburst.*** You magically create an orb and hurl it at a point you choose within 150 feet, where it erupts into a sphere of radiant light for a brief but deadly instant. Each creature in that 20-foot-radius sphere must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()})or take 2d6 radiant damage. A creature doesn't need to make the save if the creature is behind total cover that is opaque. You can increase the sphere's damage by spending ki points; each point you spend, up to a maximum of 3, increases the damage by 2d6.") )
```

## Sun Shield
*17th-level Way of the Sun Soul feature*

You become wreathed in a luminous, magical aura. You shed bright light in a 30-foot radius and dim light for an additional 30 feet. You can extinguish or restore the light as a bonus action.

If a creature hits you with a melee attack while this light shines, you can use your reaction to deal radiant damage to the creature. The radiant damage equals 5 + your Wisdom modifier.

```
def level17(npc):
    npc.traits.append("***Sun Shield.*** You become wreathed in a luminous, magical aura. You shed bright light in a 30-foot radius and dim light for an additional 30 feet.")
    npc.bonusactions.append("***Restore/Extinguish Sun Shield.***")
    npc.defer(lambda npc: npc.reactions.append("***Sun Shield.*** If a creature hits you with a melee attack while your Sun Shield is active, you can use your reaction to deal {5 + npc.WISbonus()} radiant damage to the creature.") )
```
