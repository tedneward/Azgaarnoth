# Deathless Axiom: Elegy of Decay
Your study is focused on preserving the rotting dead. Elegy of Decay pale masters draw their strength from examining the mummified remains of corpses by instilling them with the foul mimicry of life. The propensity of preservation leads these pale masters to study this elegy, which focuses primarily on the mummy.

```
name = 'Decay'
description = "***Deathless Axiom: Elegy of Decay.*** Your study is focused on preserving the rotting dead. Elegy of Decay pale masters draw their strength from examining the mummified remains of corpses by instilling them with the foul mimicry of life. The propensity of preservation leads these pale masters to study this elegy, which focuses primarily on the mummy."
```

## Undead Graft: Withered Hand
*3rd-level Elegy of Decay feature*

You remove your hand and replace it with a mummified hand swathed in funeral wrappings.

Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells with it and perform the somatic components of spells even when you have weapons or a shield in one or both hands. Additionally, you may attack with your graft as if it were a simple weapon with which you are proficient. To do so, you make a melee spell attack against a creature, dealing 1d8 necrotic damage on a hit. 

At 6th level, your graft gains a +1 bonus to melee attack and damage rolls. This increases to a +2 bonus at 12th level and a +3 bonus at 17th level.

```
def level3(npc):
    npc.traits.append("***Undead Graft: Withered Hand.*** You remove your hand and replace it with a mummified hand swathed in funeral wrappings. Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells with it and perform the somatic components of spells even when you have weapons or a shield in one or both hands.")

    npc.defer(lambda npc: npc.actions.append("***Withered Hand.*** *Melee Spell Attack:* +{npc.proficiencybonus() + npc.STRbonus() + (0 if npc.levels('Pale Master') < 6 else 1 if npc.levels('Pale Master') < 12 else 2 if npc.levels('Pale Master') < 17 else 3)} to hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + (0 if npc.levels('Pale Master') < 6 else 1 if npc.levels('Pale Master') < 12 else 2 if npc.levels('Pale Master') < 17 else 3)} necrotic.") )
```

## Mummified Servant
*3rd-level Elegy of Decay feature*

You learn the [find familiar](../../Magic/Spells/find-familiar.md) spell and can cast it as a ritual. The spell doesn't count against your number of prepared spells.

When you cast the spell, you can choose only from the following withered creatures: bat, hound, or rat.

Additionally, when you take the attack action, you can forgo one of your own attacks to allow your familiar to make one attack of its own with its reaction.

```
    npc.traits.append(f"***Mummified Servant.*** You can cast the {spelllinkify('find familiar')} ritual. When you do, you can choose only from the following withered creatures: bat, hound, or rat.")
    npc.actions.append("***Attack.*** You can forgo one of your attacks to allow your familiar to make one attack of its own with its reaction.")
```

## Withering Touch
*6th-level Elegy of Decay feature*

When you hit a creature with a melee spell attack from your undead graft, you can cause the target's skin to begin to rot away. The target takes an additional 1d8 necrotic damage, 1d8 of poison damage, and must succeed on a Constitution saving throw or become poisoned. A creature poisoned in this manner remains poisoned until cured by magical means.

You can use this feature once per long rest at 6th level. You gain an additional use at 12th level and again at 17th level. Expended uses are regained when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.attacks.append("***Withering Touch ({'' if npc.levels('Pale Master') < 12 else '2/' if npc.levels('Pale Master') < 17 else '3/'}Recharges on long rest).*** When you hit a creature with a melee spell attack from your undead graft, you can cause the target's skin to begin to rot away. The target takes an additional 1d8 necrotic damage, 1d8 of poison damage, and must succeed on a Constitution saving throw or become poisoned. A creature poisoned in this manner remains poisoned until cured by magical means.") )
```

## Anneal Curse
*6th-level Elegy of Decay feature*

You can cast the [bestow curse](../../Magic/Spells/bestow-curse.md) spell using one of your spell slots, but it does not count towards your number of prepared spells. When you cast [bestow curse](../../Magic/Spells/bestow-curse.md), you may select two natures that the curse may take on instead of one. Both of these natures last for the duration. 

```
    npc.actions.append(f"***Anneal Curse.*** You can cast {spelllinkify('bestow curse')} using one of your spell slots, but it does not count towwards you number of prepared spells. When you do, you may select two natures that the curse may take on instead of one, both of which last for the duration.")
```

## Undead Cohort: Mummy
*10th-level Elegy of Decay feature*

You are able to taint the remains of a recently slain creature. You choose the corpse of a creature that has died in the last 24 hours and touch it with your undead graft, encasing it in funeral wrappings fused with necrotic energy and causing it to rise as a mummy under your control. The mummy turns to dust when it drops to 0 hit points or when 1 hour passes. The mummy is friendly to you and your companions for the duration. Roll initiative for the mummy, which has its own turns.

The mummy obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the mummy, it defends itself from hostile creatures but otherwise takes no actions. The DM has the mummy's statistics.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level10(npc):
    npc.actions.append("***Undead Cohort: Mummy (Recharges on long rest).*** You choose the corpse of a creature that has died in the last 24 hours and touch it with your undead graft, encasing it in funeral wrappings fused with necrotic energy and causing it to rise as a [mummy](http://azgaarnoth.tedneward.com/creatures/undead/mummy) under your control. The mummy turns to dust when it drops to 0 hit points or when 1 hour passes. The mummy is friendly to you and your companions for the duration. Roll initiative for the mummy, which has its own turns. The mummy obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the mummy, it defends itself from hostile creatures but otherwise takes no actions.")
```

## Putrescent Slam
*14th-level Elegy of Decay feature*

You gain the power to bestow mummy's rot. Make a melee spell attack against a creature. On a hit, the target takes 10 (3d6) bludgeoning damage, plus 10 (3d6) necrotic damage. If the target is a creature, it must succeed on a Constitution saving throw or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the remove curse spell or other magic. 

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level14(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Putrescent Slam (Recharges on short or long rest).*** *Melee Spell Attack:* +{npc.proficiencybonus() + npc.STRbonus()}, reach 5ft., one target. Hit: 3d6 bludgeoning damage, plus 3d6 necrotic damage. If the target is a creature, it must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or be cursed with mummy rot. The cursed target can't regain hit points, and its hit point maximum decreases by 10 (3d6) for every 24 hours that elapse. If the curse reduces the target's hit point maximum to 0, the target dies, and its body turns to dust. The curse lasts until removed by the {spelllinkify('remove curse')} spell or other magic.") )
```
