## Ancestral Relic
*Prerequisite: Must be 5th-level in at least one class, does not already possess an ancestral relic*

You own an ancestral heirloom and can invest it with increasing power. Choose a non-consumable item you own, and create a backstory for it (explaining how this item has once belonged to a member of your family and made its way you, or the item may have belonged to another person to whom you are somehow connected, such as another member of your religious order, and so on). 

At any time, you may retreat to a location important to your backstory (a consecrated location for paladins and clerics, for example, a lonely mountaintop for warlocks, a wizard's study within their tower, and so on) and spend time in prayer in order to awaken the spirits in your ancestral relic. This entitles you to examine a list of available magic properties determined by the DM for an item similar to this, and you may choose its new (magical) characteristics. If you are awakening an item that has already been awakened once, you may choose to keep existing enchantment(s) or replace them with new effect(s). 

Awakening an ancestral relic requires a sacrifice of valuables (DMs note: this can be gold or magic items worth the difference between the market price of the magic item your relic will become and the market price of the current item) and requires uninterrupted long rests (DMs note: 1 day per 1,000 gp value sacrificed) or the sacrifice is insufficient to awaken the spirits in the item. Those who are assisted by a [shaman](../Classes/Shaman/index.md) of the [Ancestors](../Classes/Shaman/Ancestors.md) find they will only need to spend half the time in meditation, as the shaman can actively engage in the proper negotiations with the ancestral spirits to enhance the process.

Once this is done, this item is attuned to you, even if it normally wouldn't require attunement.

**For example** a 4th-level paladin has a bastard sword she inherited from her grandfather. She makes sacrifices worth 2,000 gp and spends two days in prayer and fasting in the temple of Heironeous. When she emerges, her devotion has awakened the magic inherent in the blade, making it a +1 bastard sword. When she reaches 7th level, she once again retreats to the temple for 6 days, sacrificing items worth an additional 6,000 gp to make her weapon a +2 bastard sword (market price 8,000 gp). When she reaches 11th level, she can make it a +2 holy bastard sword by making sacrifices worth 24,000 gp (the difference between 32,000 and 8,000 gp) and spending 24 days in prayer. 

A character's level dictates the maximum value of his or her ancestral relic, as given by similar items' rarity. 5th-level, uncommon. 9th level, rare. 13th level, very rare. 17th level, legendary.

```
name = 'Ancestral Relic'
description = "***Feat: Ancestral Relic.*** You own an ancestral heirloom and invest it with increasing power."
def prereq(npc): return npc.levels() >= 3
def apply(npc):
    if npc.levels() < 9:
        npc.equipment.append("***Ancestral Relic: Uncommon.***")
    elif npc.levels() < 13:
        npc.equipment.append("***Ancestral Relic: Rare.***")
    elif npc.levels() < 17:
        npc.equipment.append("***Ancestral Relic: Very Rare.***")
    else:
        npc.equipment.append("***Ancestral Relic: Legendary.***")
```
