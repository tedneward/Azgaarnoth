## Skulker
*Prerequisite: Dexterity 13 or higher*

You are an expert at slinking through shadows. You gain the following benefits:

* You can try to hide when you are lightly obscured from the creature from which you are hiding.
* When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position.
* Dim light doesn't impose disadvantage on your Wisdom (Perception) checks relying on sight.

```
name = 'Skulker'
description = "***Feat: Skulker.*** You are an expert at slinking through shadows."
def prereq(npc): return npc.DEX >= 13
def apply(npc):
    npc.traits.append("***Skulker.*** You can try to hide when you are lightly obscured from the creature from which you are hiding. When you are hidden from a creature and miss it with a ranged weapon attack, making the attack doesn't reveal your position. Dim light doesn't impose disadvantage on your Wisdom (Perception) checks relying on sight.")
```
