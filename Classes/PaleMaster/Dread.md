# Deathless Axiom: Elegy of Dread
The Elegy of Dread personifies the feeling of unease that accompanies the mention of creatures that populates this elegy's lore. Driven to feast off the blood and fear of living creatures, vampires will go to any lengths to ensure their survival throughout eternity. This primal instinct is inherited by the pale masters who study the elegy of dread. Seeking out blood and using it as a catalyst to strengthen their incantations and eventually themselves is their ultimate goal.

```
name = 'Dread'
description = "***Deathless Axiom: Elegy of Dread.*** The Elegy of Dread personifies the feeling of unease that accompanies the mention of creatures that populates this elegy's lore. Driven to feast off the blood and fear of living creatures, vampires will go to any lengths to ensure their survival throughout eternity. This primal instinct is inherited by the pale masters who study the elegy of dread. Seeking out blood and using it as a catalyst to strengthen their incantations and eventually themselves is their ultimate goal."
```

## Undead Graft: Vampiric Fangs
*3rd-level Elegy of Dread feature*

You remove all of your teeth and replace them with fangs infused with necrotic energy.

Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells and perform the somatic components of spells even when you have weapons or a shield in one or both hands. Additionally, you may attack with your graft as if it were a simple weapon with which you are proficient. To do so, you make a melee spell attack against a creature, dealing 1d8 necrotic damage on a hit.

At 6th level, your graft gains a +1 bonus to melee attacks and damage rolls. This increases to a +2 bonus at 12th level and a +3 bonus at 17th level.

```
def level3(npc):
    npc.defer(lambda npc: npc.actions.append("***Bite: Vampiric Fangs.*** *Melee Weapon Attack:* +{} to hit, reach 5ft., one target. Hit: 1d8 + {} necrotic damage") )
    npc.traits.append("***Vampiric Fangs.*** You remove all of your teeth and replace them with fangs infused with necrotic energy. Your undead graft becomes a spellcasting focus for your magic, allowing you to cast spells and perform the somatic components of spells even when you have weapons or a shield in one or both hands. Additionally, you may attack with your graft as if it were a simple weapon with which you are proficient. To do so, you make a melee spell attack against a creature, dealing 1d8 necrotic damage on a hit.{'' if npc.levels('Pale Master') < 6 else ''}")
```

## Summon Bats
*3rd-level Elegy of Dread feature*

You are able to assert your control over those which feed in the night.

You to spend 1 minute creating an offering of blood, which calls forth a [swarm of bats](../../Creatures/Bats.md#swarm-of-bats). The swarm is under your control for 24 hours, after which it stops obeying any command you've given it. To maintain the control of the swarm for another 24 hours, you must spend 1 minute creating another offering of blood before the current 24-hour period ends. You may only control one swarm of bats in this manner at a time. If a swarm of bats under your control dies your you dismiss them as an action, you cannot use this feature again until you complete a long rest.

```
    npc.traits.append("***Summon Bats (Recharges on long rest).*** You to spend 1 minute creating an offering of blood, which calls forth a [swarm of bats](http://azgaarnoth.tedneward.com/creatures/Bats.md#swarm-of-bats). The swarm is under your control for 24 hours, after which it stops obeying any command you've given it. To maintain the control of the swarm for another 24 hours, you must spend 1 minute creating another offering of blood before the current 24-hour period ends. You may only control one swarm of bats in this manner at a time. If a swarm of bats under your control dies your you dismiss them as an action, you cannot use this feature again until you complete a long rest.")
```

## Draining Touch
*6th-level Elegy of Dread feature*

When you hit a creature with a melee spell attack from your undead graft, you can drain the very life-force that sustains it. The target takes an additional 2d8 necrotic damage and becomes grappled. A grappled creature can use its action to attempt to break free (escape DC is contested by your spellcasting modifier).

Additionally, while the target is grappled in this manner, you regain hit points equal to half the amount of necrotic damage dealt to it by attacks with your undead graft, which includes the initial attack.

You can use this feature once per long rest at 6th level. You gain an additional use at 12th level and again at 17th level.

Expended uses are regained when you finish a long rest.

## Out for Blood
*6th-level Elegy of Dread feature*

You can cast the vampiric touch spell using one of your spell slots, but it does not count towards your number of prepared spells. When you cast vampiric touch, each creature hit with a melee spell attack with the spell deals maximum damage to the target, and you regain hit points equal to the total amount of necrotic damage dealt, instead of half.

## Undead Cohort: Vampiric Mist
*10th-level Elegy of Dread feature*

You are able to taint the soul of a recently slain creature. You choose the corpse of a creature that has died in the last 24 hour and bite it with your undead graft, infusing it with necrotic energy and causing its soul to rise as a vampiric mist under your control. The vampiric mist dissipates when it drops to 0 hit points or when 1-hour passes. The vampiric mist is friendly to you and your companions for the duration.

Roll initiative for the vampiric mist, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the vampiric mist, it defends itself from hostile creatures but otherwise takes no actions. The DM has the vampiric mist's statistics.

Once you use this feature, you can't use it again until you finish a long rest.

## Cursed Blood
*14th-level Elegy of Dread feature*

You can bite a humanoid with your undead graft by making a melee spell attack and bestow a curse into the open wound. 

When a creature's blood is cursed, it can't regain hit points for the next 30 days. When the creature completes a long rest while cursed, it takes 19 (3d12) necrotic damage as their toxic blood begins to coagulate. A remove curse spell ends this effect.

If a creature dies while under the effects of cursed blood, they become a vampire spawn under your control 1d10 days after it dies. The vampire spawn turns to ash when it drops to 0 hit points. Roll initiative for the vampire spawn, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). You can only control one vampire spawn at a time with this feature. If you bite another humanoid and it turns into a vamipre spawn, the current vampire spawn under your control turns to ash. The DM has the vampire spawn's statistics.

Once you use this feature, you can't use it again until you finish a long rest.

