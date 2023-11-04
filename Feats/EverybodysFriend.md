## Everybody's Friend
*Prerequisite: Half-elf*

You develop your magnetic personality to ease your way through the world. You gain the following benefits:

* Increase your Charisma score by 1, up to a maximum of 20.
* You gain proficiency in Deception and Persuasion skills. If you're already proficient in either skill, your proficiency bonus is doubled for any check you make with that skill.

```
name = "Everybody's Friend"
description = "***Feat: Everybody's Friend.*** You develop a magnetic personality to ease your way through the world."
def prereq(npc): return npc.race.name == 'Half-Elf'
def apply(npc):
    npc.CHA += 1

    npc.addskillorexpertise("Deception")
    npc.addskillorexpertise("Persuasion")
```
