## Tavern Brawler
Accustomed to the rough-and-tumble fighting using whatever weapons happen to be at hand, you gain the following benefits:

* Increase your Strength or Consititution score by 1, to a maximum of 20.
* You are proficient with improvised weapons.
* Your unarmed strike uses a d4 for damage.
* When you hit a creature with an unarmed strike or an improvised weapon on your turn, you can use a bonus action to attempt to grapple the target.

```
name = 'Tavern Brawler'
description = "***Feat: Tavern Brawler.*** You are accustomed to the rough-and-tumble fighting using whatever weapons happen to be at hand."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR', 'CON'])
    npc.proficiencies.append("Improvised weapons")
    npc.defer(lambda npc: npc.actions.append(f"***Unarmed Strike.*** *Melee weapon attack*, +{npc.proficiencybonus() + npc.STRbonus()}, reach 5 ft., one target. Hit d4 + {npc.STRbonus()} bludgeoning damage.") )
    npc.bonusactions.append("***Tavern Brawler: Grappler.*** When you hit a creature with an Unarmed Strike or an improvised weapon on your turn, you grapple the target.")
```
