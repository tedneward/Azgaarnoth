# Primal Path: Path of the Zealot
Some deities -- or some fiends, or even some tribal chieftains with some amount of divine power themselves -- inspire their followers to pitch themselves into a ferocious battle fury. These barbarians are zealots, warriors who channel their rage into powerful displays of divine power. These barbarians are quite common among the [Al'Uma](../../Cultures/AlUma.md), particularly among the nomads, but are also frequently bound to one of the [Pantheonic gods](../../Religions/Pantheon/index.md) or even, at times, the [Kaevarian Church](../../Religions/KaevarianChurch.md), though in the latter case usually in [Dradehalia](../../Nations/Dradehalia.md).

```
name = 'Zealot'
description = "***Primal Path: Path of the Zealot.*** Some deities -- or some fiends, or even some tribal chieftains with some amount of divine power themselves -- inspire their followers to pitch themselves into a ferocious battle fury. These barbarians are zealots, warriors who channel their rage into powerful displays of divine power."
```

## Divine Fury
*3rd-level Path of the Zealot feature*

You can channel divine fury into your weapon strikes. While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + half your Barbarian level. The extra damage is necrotic or radiant; you choose the type of damage when you gain this feature.

```
def level3(npc):
    npc.defer(lambda npc: npc.attacks.append(f"***Divine Fury.*** While you're raging, the first creature you hit on each of your turns with a weapon attack takes extra damage equal to 1d6 + {npc.levels(baseclass) // 2} necrotic/radiant damage. (choose the type of damage when you gain this feature.)") )
```

## Warrior of the Gods
*3rd-level Path of the Zealot feature*

Your soul is marked for endless battle. If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you.

```
    npc.traits.append("***Warrior of the Gods.*** If a spell, such as Raise Dead, has the sole effect of restoring you to life (but not undeath), the caster doesn't need material components to cast the spell on you.")
```

## Fanatical Focus
*6th-level Path of the Zealot feature*

The divine power that fuels your rage can protect you. If you fail a saving throw while raging, you can reroll it, and you must use the new roll. You can use this ability only once per rage.

```
def level6(npc):
    npc.traits.append("***Fanatical Focus (Recharges on entering rage). If you fail a saving throw while raging, you can reroll it, and you must use the new roll.")
```

## Zealous Presence
*10th-level Path of the Zealot feature*

You learn to channel divine power to inspire zealotry in others. As a bonus action, you unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level10(npc):
    npc.bonusactions.append("***Zealous Presence (Recharges on long rest).*** You unleash a battle cry infused with divine energy. Up to ten other creatures of your choice within 60 feet of you that can hear you gain advantage on attack rolls and saving throws until the start of your next turn.")
```

## Rage Beyond Death
*14th-level Path of the Zealot feature*

The divine power that fuels your rage allows you to shrug off fatal blows.

While you're raging, having 0 hit points doesn't knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don't die until your rage ends, and you die then only if you still have 0 hit points.

```
def level14(npc):
    npc.traits.append("***Rage Beyond Death.*** While you're raging, having 0 hit points doesn't knock you unconscious. You still must make death saving throws, and you suffer the normal effects of taking damage while at 0 hit points. However, if you would die due to failing death saving throws, you don't die until your rage ends, and you die then only if you still have 0 hit points.")
```