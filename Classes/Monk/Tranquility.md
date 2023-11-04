# Monastic Tradition: Way of Tranquility
Monks of the Way of Tranquility see violence as a last resort. They use diplomacy, mercy, and understanding to resolve conflicts. If pushed, though, they are capable warriors who can bring an end to the unjust or cruel folk who refuse to listen to reason. When adventuring, these monks make excellent diplomats. They are also skilled in the healing arts, and can preserve their allies in the face of daunting foes. They often act as intermediaries in conflicts, and have a well-known tenet to their Code that demands they heal any who ask, regardless of ethos, so long as they are not personally threatened.

Many monks of Tranquility are members of the [Order of the Silver Dragon](../../Organizations/DraconicOrder/Silver.md). Those who are not of the Silver often wear white robes and carry a intertwined snake staff, the symbol of their order, are revered everywhere they travel when among the civilized lands, and no civilized creature on Azgaarnoth will deliberately attack a monk of Mercy without extreme provocation. Tranquility monks maintain a monastery--what they call a *hospital*--in the capital of every nation of Azgaarnoth. Less frequently, Tranquility monks will travel with caravans and merchants, offering healing to those in need where they find them; however, they are extremely reluctant to travel alone or without guardians. Monks of Tranquility will accept any who seek to join their Order, and often those traveling with a Tranquility monk are novitiates who have not yet taken their Vows at a *hospital*.

Monks of Tranquility are frequently confused with Monks of Mercy and most creatures provide both the same degree of respect. Monks of Mercy and Tranquility are fierce opponents to one another, however, and often refuse to be within eyeshot/earshot of one another.

```
name = 'Way of Tranquility'
description = "***Monastic Tradition: Way of Tranquility.*** Monks of the Way of Tranquility see violence as a last resort. They use diplomacy, mercy, and understanding to resolve conflicts. If pushed, though, they are capable warriors who can bring an end to the unjust or cruel folk who refuse to listen to reason."
```

## Path of Tranquility
*3rd-level Way of Tranquility feature*

You can become an island of calm in even the most chaotic of situations. With this feature, you can cast the Sanctuary spell on yourself, no material component required, and it lasts up to 8 hours. Its saving throw DC equals 8 + your proficiency bonus + your Wisdom modifier. A creature that succeeds on the save is immune to this effect for 1 hour.

Once you cast the spell in this way, you can't do so again for 1 minute.

```
def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Path of Tranquility.*** You can cast {spelllinkify('sanctuary')} on yourself, no material component required, and it lasts up to 8 hours. Its saving throw DC is {8 + npc.proficiencybonus() + npc.WISbonus()}, and a creature that succeeds on the save is immune to this effect for 1 hour.") )
```

## Healing Hands
*3rd-level Way of Tranquility feature*

Your mystical touch can heal wounds. You have a pool of magical healing power that replenishes when you take a long rest. With that pool, you can restore a total number of hit points equal to your monk level × 10.

As an action, you can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in the pool.

Instead of healing the creature, you can expend 5 hit points from your pool of healing to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Healing Hands, expending hit points separately for each one.

When you use your Flurry of Blows, you can replace one of the unarmed strikes with a use of this feature.

This feature has no effect on undead and constructs.

```
    npc.defer(lambda npc: npc.traits.append(f"***Healing Hands (Recharges on long rest).*** You have a pool of magical healing power containing {npc.levels('Monk') * 10} hit points.") )
    npc.actions.append("***Healing Hands.*** You can touch a creature and draw power from the pool to restore a number of hit points to that creature, up to the maximum amount remaining in the pool. Alternatively, yuo can expend 5 points from the pool to cure the target of one disease or neutralize one poison affecting it. You can cure multiple diseases and neutralize multiple poisons with a single use of Healing Hands, expending points separately for each one. When you use your Flurry of Blows, you can replace one of the Unarmed Strikes with a use of this feature.")
```

## Emissary of Peace
*6th-level Way of Tranquility feature*

You gain the ability to diffuse violent situations. Whenever you make a Charisma check to calm violent emotions or to counsel peace, you have advantage on the roll. You must make this entreaty in good faith; it doesn't apply if proficiency in the Deception or Intimidation skill applies to your check.

You also gain proficiency in the Performance or Persuasion skill (choose one).

```
def level6(npc):
    npc.traits.append("***Emissary of Peace.*** Whenever you make a Charisma check to calm violent emotions or to counsel peace, you have advantage on the roll. You must make this entreaty in good faith; it doesn't apply if proficiency in the Deception or Intimidation skill applies to your check.")
    chooseskill(npc, ['Performance', 'Persuasion'])
```

## Douse the Flames of War
*11th-level Way of Tranquility feature*

You gain the ability to temporarily extinguish a creature's violent impulses. As an action, you can touch a creature, and it must make a Wisdom saving throw with a DC equal to 8 + your proficiency bonus + your Wisdom modifier. The target automatically succeeds if it's missing any of its hit points. If the target fails the save, it can't attack for 1 minute. During that time, it also can't cast spells that deal damage or that force someone to make a saving throw.

This effect ends if the target is attacked, takes damage, or is forced to make a saving throw or if the target witnesses any of those things happening to its allies.

```
def level11(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Douse the Flames of War.*** You can touch a creature, and it must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}). The target automatically succeeds if it's missing any of its hit points. If the target fails the save, it can't attack for 1 minute. During that time, it also can't cast spells that deal damage or that force someone to make a saving throw. This effect ends if the target is attacked, takes damage, or is forced to make a saving throw or if the target witnesses any of those things happening to its allies.") )
```

## Anger of a Gentle Soul
*17th-level Way of Tranquility feature*

You gain the ability to visit vengeance on someone who fells others. If you see a creature reduce another creature to 0 hit points, you can use your reaction to grant yourself a bonus to all damage rolls against the aggressor until the end of your next turn. The bonus equals your monk level.

Once you use this ability, you can't use it again until you finish a short or long rest.

```
def level17(npc):
    npc.defer(lambda npc: npc.reactions.append("***Anger of a Gentle Soul (Recharges on short or long rest).*** If you see a creature reduce another creature to 0 hit points, you can use your reaction to grant yourself a +{npc.levels('Monk')} bonus to all damage rolls against the aggressor until the end of your next turn. Once you use this ability, you can't use it again until you finish a short or long rest.") )
```
