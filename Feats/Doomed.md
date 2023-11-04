## Doomed
*Prerequisite: must have backstory elements and DM's approval to take this feat*

You are not long for this world though you have no idea of this fate. Despite your abilities as an adventurer, you are not a part of this world's great stories, and you will soon exit the stage, but perhaps not before a grand finale. You gain the following benefits and drawbacks:

* You can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1.
* You gain the same benefits as those granted by the [Lucky](#lucky) feat. You can have both this feat and that one.
* You can be critically hit by attacks on a roll of 19-20.
* You have disadvantage on death saving throws, and other creatures have disadvantage on checks made to stabilize you. If you die, you cannot be resurrected by any means. While dying in combat, fate itself seems to compel enemies to go out of their way to quickly finish you off.
* If you die, your allies will be inspired by your courage. When you do so, you may choose any number of creatures who can see or hear you. Those creatures gain temporary hit points equal to three times your level.

```
name = 'Doomed'
description = "***Feat: Doomed.*** You are not long for this world though you have no idea of this fate. Despite your abilities as an adventurer, you are not a part of this world's great stories, and you will soon exit the stage, but perhaps not before a grand finale."
def prereq(npc): return True
def apply(npc):
    chooseability(npc)
    chooseability(npc)

    npc.traits.append("***Doomed.*** You can be critically hit by attacks on a roll of 19-20.You have disadvantage on death saving throws, and other creatures have disadvantage on checks made to stabilize you. If you die, you cannot be resurrected by any means. While dying in combat, fate itself seems to compel enemies to go out of their way to quickly finish you off. If you die, your allies will be inspired by your courage. When you do so, you may choose any number of creatures who can see or hear you. Those creatures gain temporary hit points equal to three times your level.")
```
