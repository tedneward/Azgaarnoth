# Sorcerous Origin: Arcane Anomaly
Your ancestors dabbled in magic they should not have, and encountered a magical anomaly of dreadful power. Their mistake has tainted your bloodline with sinister potential, and the natural forces of the world reject your presence with extreme prejudice, recognising the danger of the magic coursing through you as a thread to the very fabric of what is. The cataclysm percolating in your blood can manifest in a number of peculiar ways:

1d6 | Arcane Anomaly Quirks
--- | ----------------------
1 | The earth rejects you, and your footprints leave a scar on the land wherever you walk.
2 | Light cannot abide you. You are always shrouded in dim light.
3 | The water will not touch you, and rain slides away from you. You can walk on water.
4 | The air cannot suffer your presence, and grows still around you.
5 | Fire hates you. You always feel cold and you have resistance to fire damage.
6 | Your spells leave a pale aftertrace in the air, like a scar on the weave of magic itself.

```
name = 'Arcane Anomaly'
description = "***Sorcerous Origin: Arcane Anomaly.*** Your ancestors dabbled in magic they should not have, and encountered a magical anomaly of dreadful power. Their mistake has tainted your bloodline with sinister potential, and the natural forces of the world reject your presence with extreme prejudice, recognising the danger of the magic coursing through you as a thread to the very fabric of what is."

quirks = [
    "The earth rejects you, and your footprints leave a scar on the land wherever you walk.",
    "Light cannot abide you. You are always shrouded in dim light.",
    "The water will not touch you, and rain slides away from you. You can walk on water.",
    "The air cannot suffer your presence, and grows still around you.",
    "Fire hates you. You always feel cold and you have resistance to fire damage.",
    "Your spells leave a pale aftertrace in the air, like a scar on the weave of magic itself."
]
```

## Magical Leakage
*1st-level Arcane Anomaly feature*

Your spells pull apart the threads of magical energy around you, tearing at the weave and emitting harmful energies. When you cast a spell of 1st level, each creature within 5 feet of you takes 1d6 force damage. The radius and damage of this effect increases by 5 feet for every spell level above first.

```
def level1(npc):
    npc.description.append(f"***Arcane Anomaly.*** ${random(quirks)}")

    npc.traits.append("***Magical Leakage.*** When you cast a spell of 1st level, each creature within 5 feet of you takes 1d6 force damage. The radius and damage of this effect increases by 5 feet for every spell level above first.")
```

## Devastation Corona
*6th-level Arcane Anomaly feature*

You can invoke the magic of your bloodline to amplify the destructive power of spells nearby. As a bonus action, you can spend 3 sorcery points to emit an aura spreading out to 30 feet from your location and moves to remain centered on you and lasts for 1 minute. Any creature damaged by your magic inside the aura takes the maximum damage possible from that instance.

```
def level6(npc):
    npc.bonusactions.append("***Devastation Corona.*** You spend 3 sorcery points to emit an aura spreading out to 30 feet from your location and moves to remain centered on you and lasts for 1 minute. Any creature damaged by your magic inside the aura takes the maximum damage possible from that instance.")
```

## Resonance
*14th-level Arcane Anomaly feature*

Your spells leave a mark in the firmament which hums with potential. When you cast a damaging spell, there is a 1 in 6 chance on Initiative Count 20 of the next round that the spell repeats itself targeting the same area of effect and with the same point of origin as when you previously cast it. Resonance has no effect on any spell which does not target an area of effect.

```
def level14(npc):
    npc.traits.append("***Resonance.*** When you cast a damaging spell, there is a 1 in 6 chance on Initiative Count 20 of the next round that the spell repeats itself targeting the same area of effect and with the same point of origin as when you previously cast it. Resonance has no effect on any spell which does not target an area of effect.")
```

## Reality Tear
*18th-level Arcane Anomaly feature*

Your magic has the potential to rip holes in existence. When you use your Metamagic feature, roll a d20. On a result of 19 or 20, a [sphere of annihilation](../../Magic/Items/sphere-of-annihiliation.md) forms adjacent to the target of the spell. The sphere remains for 1 minute before vanishing. You can spend a sorcery point to maintain and control the sphere for 1 minute.

```
def level18(npc):
    npc.traits.append("***Reality Tear.*** When you use your Metamagic feature, roll a d20. On a result of 19 or 20, a [sphere of annihilation](http://azgaarnoth.tedneward.com/magic/items/sphere-of-annihiliation/) forms adjacent to the target of the spell. The sphere remains for 1 minute before vanishing. You can spend a sorcery point to maintain and control the sphere for 1 hour.")
```
