## Telepathic Bond
*Prerequisite*: Telepathic feat in two creatures

You form a deep, mind-linked bond with another Telepathic creature. You each gain the following benefits:

* Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 21.
* So long as you are each within 60 feet of each other, you may communicate without requiring speech (or even air).
* When in combat, each of you rolls Initiative, but you share the higher of the two Initiative die rolls.
* You may pool your Psionic Talent dice.

If one of the bond dies, the other faces deep anguish, insanity, and often death.

```
name = 'Telepathic Bond'
description = "***Feat: Telepathic Bond.*** You form a deep, mind-linked bond with another Telepathic creature."
def prereq(npc): return 'Telepathic' in npc.feats
def apply(npc):
    chooseability(npc, ['INT', 'WIS', 'CHA'])

    npc.traits.append("***Telepathic Bond.*** So long as you are within 60 feet of your Telepathic Bond pair, you may communicate without requiring speech (or even air).")
    npc.traits.append("***Shared Initiative.*** When in combat with your Telepathic Bond pair, each of you rolls Initiative, but you share the higher of the two Initiative die rolls.")
    npc.traits.append("***Shared Psionics.*** You may pool your Psionic Talent dice with your Telepathic Bond pair.")
```
