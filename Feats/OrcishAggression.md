## Orcish Aggression
*Prerequisite: Orcish heritage (Half-orc, Orc)*

As a bonus action, you can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.

```
name = 'Orcish Aggression'
description = "***Feat: Orcish Aggression.*** You are filled with aggression and a willingness to use it in combat."
def prereq(npc): return npc.race.name == 'Orc' or npc.race.name == 'Half-Orc'
def apply(npc):
    npc.bonusactions.append("***Orcish Aggression.*** You can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.")
```
