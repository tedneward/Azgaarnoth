# Arcane Tradition: Aeromancy
Aeromancers are masters of the wind. They learn to manipulate and harness the wind, sky, clouds, the weather and more. Aeromancers know that wind powers so much of the natural world, from weather to erosion, and the power that can be harnessed from the pure element of air is a formidable ally to add to any wizard's arsenal. With the control of air, a wizard can push and devastate their foes, or breathe life back into their allies when they need it the most. The sheer strength of will that aeromancers possess is not to be taken lightly.

```
name = 'Aeromancy'
description = "***Arcane Tradition: Aeromancy.*** Aeromancers are masters of the wind. They learn to manipulate and harness the wind, sky, clouds, the weather and more. Aeromancers know that wind powers so much of the natural world, from weather to erosion, and the power that can be harnessed from the pure element of air is a formidable ally to add to any wizard's arsenal. With the control of air, a wizard can push and devastate their foes, or breathe life back into their allies when they need it the most. The sheer strength of will that aeromancers possess is not to be taken lightly."
```

## Adept of the Wind
*2nd-level Aeromancy feature*

You learn to manipulate the air around your body with every movement you make. 

You gain proficiency in the Acrobatics skill if you don't already have it. You seem to always have an airy breeze about you, and your movement speed increases by 5 feet.

In addition, the [wind walk](../../Magic/Spells/wind-walk.md) and [wind wall](../../Magic/Spells/wind-wall.md) spells are added to the wizard spell list for you.

```
def level2(npc):
    npc.speed['walking'] += 5
    npc.skills.append('Acrobatics')
    npc.spellbook.append('wind walk')
    npc.spellbook.append('wind wall')
```

## Wind Lift
*6th-level Aeromancy feature*

You add [levitate](../../Magic/Spells/levitate.md) to your spellbook, if you don't already have it. Whenever you cast [levitate](../../Magic/Spells/levitate.md), you can choose one additional target. Both targets must be within 10 feet of each other. A gentle draft of wind aids you in levitating both targets.  Additionally, if you are not a target of your *levitate* spell, you have advantage on Constitution saving throws made to maintain concentration on the spell.

```
def level6(npc):
    npc.spellbook.append('levitate')
    npc.traits.append(f"***Wind Lift.*** Whenever you cast {spelllinkify('levitate')}, you can choose one additional target. Both targets must be within 10 feet of each other. A gentle draft of wind aids you in levitating both targets.  Additionally, if you are not a target of your {spelllinkify('levitate')} spell, you have advantage on Constitution saving throws made to maintain concentration on the spell.")
```

## Breeze Walk
*10th-level Aeromancy feature*

You can call upon the wind to help aid you in your travels. Whenever you use windbased magic (such as the [wind wall](../../Magic/Spells/wind-wall.md) spell) the winds come to your aid. For 1 minute after casting a windbased spell of 1st-level or higher, your movement speed increases by 10 feet. Your movement is unaffected by difficult terrain. Additionally, you do not take falling damage, and you can not be knocked prone.

```
def level10(npc):
    npc.traits.append("***Breeze Walk.*** For 1 minute after casting a wind- or air-based spell of 1st-level or higher, your movement speed increases by 10 feet. Your movement is unaffected by difficult terrain. Additionally, you do not take falling damage, and you can not be knocked prone.")
```

## Wings of Air
*14th-level Aeromancy feature*

You gain the ability to sprout a pair of wings that look as if they are made of swirling clouds and feathers. As a bonus action, you can cause the wings to sprout from your back, giving you a flying speed of 40 feet. The wings last for 1 hour or until you use your bonus action to dismiss them. You can use this feature twice, regaining expended uses of this ability after completing a long rest.

```
def level14(npc):
    npc.bonusactions.append("***Wings of Air (2/Recharges on long rest).*** You cause wings (that look as if they are made of swirling clouds and feathers) to sprout from your back, giving you a flying speed of 40 feet. The wings last for 1 hour or until you use your bonus action to dismiss them.")
```

