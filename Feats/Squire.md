## Squire
*Prerequisite: Member of a militant order, such as the [Draconic Order](../Organizations/DraconicOrder/DraconicOrder.md) or [Dread Knights](../Organizations/DreadOrder.md)*

Your training in the ways of your militant order grants you these benefits:

* **Martial Training.** You gain proficiency with medium armor and martial weapons.
* **Defensive Rider.** You have advantage on saving throws made to avoid falling off a mount.
* **Encouraging Rally.** When another creature you can see within 30 feet of you makes a saving throw, you can use your reaction to inspire them. If the target can hear you and understand you, it gains advantage on the saving throw. Once you use this reaction, you can't do so again until you finish a long rest.

```
name = 'Squire'
description = "***Feat: Squire.*** You've been trained in the ways of a militant order."
def prereq(npc): return True
def apply(npc):
    for arm in armor['medium']:
        npc.proficiencies.append(arm)
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
    npc.traits.append("***Defensive Rider.*** You have advantage on saving throws made to avoid falling off a mount.")
    npc.reactions.append("***Encouraging Rally (Recharges on long rest).*** When another creature you can see within 30 feet of you makes a saving throw, you can use your reaction to inspire them. If the target can hear you and understand you, it gains advantage on the saving throw.")
```
