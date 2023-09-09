## Stout Halflings
As a stout halfling, you’re hardier than average and have some resistance to poison. Some say that stouts have dwarven blood.

**Ability Score Increase.** Your Constitution score increases by 1.

**Stout Resilience.** You have advantage on saving throws against poison, and you have resistance against poison damage.

```
name = 'Stout'
description = "***Stout Halfling.***"
def level0(npc):
    npc.CON += 1
    npc.damageresistances.append('poison')
    npc.traits.append("***Stout Resilience.*** You have advantage on saving throws against poison.")
```

