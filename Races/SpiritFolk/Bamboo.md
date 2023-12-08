# Bamboo Spirit Folk
Bamboo Spirit Folk are intimately tied to the serene bamboo groves that dot the landscape. They are masters of patience and resilience, emulating the bamboo’s flexibility and strength.

**Ability Score Increase.** Your Constitution score increases by 1.

**Bamboo Resilience.** You have advantage on saving throws against being poisoned, and you have resistance to poison damage.

**Bamboo Stride.** You can move through difficult terrain made of plants, such as dense undergrowth and overgrown areas, without spending extra movement.

```
name = 'Bamboo'
description = "***Bamboo Spirit Folk.*** Bamboo Spirit Folk are intimately tied to the serene bamboo groves that dot the landscape. They are masters of patience and resilience, emulating the bamboo’s flexibility and strength."
def level0(npc):
    npc.CON += 1
    npc.damageresistances.append('poison')
    npc.traits.append("***Bamboo Resilience.*** You have advantage on saving throws against being poisoned.")
    npc.traits.append("***Bamboo Stride.*** You can move through difficult terrain made of plants, such as dense undergrowth and overgrown areas, without spending extra movement.")
```
