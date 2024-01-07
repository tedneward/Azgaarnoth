# Primal Path: Path of the Berserker
For some barbarians, rage is a means to an end – that end being violence. The Path of the Berserker is a path of untrammeled fury, slick with blood. As you enter the berserker's rage, you thrill in the chaos of battle, heedless of your own health or well-being. This path is actually a very common path for barbarians who join up with one of the [Mercenary Companies](../../Organizations/MercCompanies/index.md).

```
name = 'Berserker'
description = "***Primal Path: Path of the Berserker.*** For some barbarians, rage is a means to an end -- that end being violence. The Path of the Berserker is a path of untrammeled fury, slick with blood. As you enter the berserker's rage, you thrill in the chaos of battle, heedless of your own health or well-being."
```

## Frenzy
*3rd-level Path of the Berserker feature*

You can go into a frenzy when you rage. If you do so, for the duration of your rage you can make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion.

```
def level3(npc):
    npc.bonusactions.append("***Frenzy.*** For the duration of your rage you make a single melee weapon attack as a bonus action on each of your turns after this one. When your rage ends, you suffer one level of exhaustion.")
```

## Mindless Rage
*6th-level Path of the Berserker feature*

You can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage.

```
def level5(npc):
    npc.traits.append("***Mindless Rage.*** You can't be charmed or frightened while raging. If you are charmed or frightened when you enter your rage, the effect is suspended for the duration of the rage.")
```

## Intimidating Presence
*10th-level Path of the Berserker feature*

You can use your action to frighten someone with your menacing presence. When you do so, choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you.

If the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours.

```
def level10(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Intimidating Presence.*** Choose one creature that you can see within 30 feet of you. If the creature can see or hear you, it must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or be frightened of you until the end of your next turn. On subsequent turns, you can use your action to extend the duration of this effect on the frightened creature until the end of your next turn. This effect ends if the creature ends its turn out of line of sight or more than 60 feet away from you. If the creature succeeds on its saving throw, you can't use this feature on that creature again for 24 hours.") )
```

## Retaliation
*14th-level Path of the Berserker feature*

When you take damage from a creature that is within 5 feet of you, you can use your reaction to make a melee weapon attack against that creature.

```
def level14(npc):
    npc.reactions.append("***Retaliation.*** When you take damage from a creature that is within 5 feet of you, you make a melee weapon attack against that creature.")
```
