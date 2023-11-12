## Stench of Death
*Prerequisites: Gnoll*

Known to languish in piles of filth and carrion, gnolls sometimes reek of things worse than urine.

You exude a terrible scent as a 15-foot aura that nearly every other creature finds repulsive. All living creatures (except those with the stench aura ability) within the aura must succeed at a Fortitude saving throw (DC 10 + 1/2 the gnoll's character level + Constitution modifier) or be sickened for 5 rounds. Creatures that succeed at the saving throw cannot be sickened by the same creature's stench aura for 24 hours. A [neutralize poison](../Magic/Spells/neutralize-poison.md) spell or similar effect removes the effect from the sickened creature. This is a poison effect.

```
name = 'Stench of Death'
description = "***Feat: Stench of Death.*** Known to languish in piles of filth and carrion, gnolls sometimes reek of things worse than urine."
def prereq(npc): return npc.race.name == 'Gnoll'
def apply(npc):
    npc.defer(lambda npc: npc.traits.append("***Stench of Death.*** You exude a terrible scent as a 15-foot aura that nearly every other creature finds repulsive. All living creatures (except those with the stench aura ability) within the aura must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + (npc.levels() // 2)}) or be sickened for 5 rounds. Creatures that succeed at the saving throw cannot be sickened by the same creature's stench aura for 24 hours. A {spelllinkify('neutralize poison')} spell or similar effect removes the effect from the sickened creature. This is a poison effect.") )
```
