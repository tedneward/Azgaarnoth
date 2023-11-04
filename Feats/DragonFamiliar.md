## Dragon Familiar
*Prerequisite: must be a spellcaster with the ability to have a familiar, such as a [Warlock: Pact of the Chain](../Classes/Warlock/index.md#pact-boon) or a wizard with the [find familiar](../Magic/Spells/find-familiar.md) spell.*

Your familiar can take the form of a dragon wyrmling. You may use the rules for keeping a psuedodragon as a familiar for your wyrmling, at the DM's discretion. The dragon you choose must be within one step of your alignment, and can have a Challenge Rating as high as your character level divided by 4. The DM has the dragon's statistics. 

If you take this feat, decide with your DM how you met your dragon familiar. Why did she agree to accompany you? What are her bonds and flaws?

Eventually, the dragon's nature will require her to leave and seek her own fortune. This time may be years down the road, but it is inevitable. Worse, she might die in combat. When that time comes, discuss with your DM how to resolve this conflict of character. Consider keeping this feat in the form of a dragon friend whom you can count on for help or advice, or consider choosing a new feat when your wyrmling leaves (or dies).

```
name = 'Dragon Familiar'
description = "***Feat: Dragon Familiar.*** Your familiar can take the form of a dragon wyrmling."
def prereq(npc): return True
def apply(npc):
    npc.defer(lambda npc: npc.traits.append("***Dragon Familiar.*** Your familiar can take the form of a dragon wyrmling. You may use the rules for keeping a psuedodragon as a familiar for your wyrmling, at the DM's discretion. The dragon you choose must be within one step of your alignment, and can have a Challenge Rating as high as {npc.levels() // 4}.") )
```
