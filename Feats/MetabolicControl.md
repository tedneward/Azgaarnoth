## Metabolic Control
*Prerequisite*: Psionic Talent feature or Wild Talent feat

You have refined psionic control over your body's functions. You gain the following benefits:

* Increase your Strength, Dexterity, or Constitution score by 1, to a maximum of 20.
* If your Psionic Talent die is available, you can take an action to channel your psionic power to nourish yourself for the next 24 hours, as if you consumed sufficient food and water for a day. When you take this action, your Psionic Talent die decreases by one die size.
* If your Psionic Talent die is available, you can meditate for 1 minute, at the end of which you gain the benefits of finishing a short rest, and your Psionic Talent die decreases by one die size. You can't meditate in this way again until you finish a long rest.

```
name = 'Metabolic Control'
description = "***Feat: Metabolic Control.*** You have refined psionic control over your body's functions."
def prereq(npc): return getattr(npc, 'psionicdie', None) != None
def apply(npc):
    ability = chooseability(npc, ['STR','DEX','CON'])

    npc.actions.append("***Psychic Nourishment.*** You channel your psionic power, decreasting your Psionic Talent die, to nourish yourself for the next 24 hours, as if you consumed sufficient food and water for a day. (You cannot take this action if your Psionic Talent die is unavailable.)")
    npc.traits.append("***Psychic Rest (Recharges on long rest).*** If your Psionic Talent die is available, you can meditate for 1 minute, at the end of which you gain the benefits of finishing a short rest, and your Psionic Talent die decreases by one die size. You can't meditate in this way again until you finish a long rest.")
```
