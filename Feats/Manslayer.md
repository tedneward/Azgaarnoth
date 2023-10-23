## Manslayer
*Prerequisites: Must have slain 100+ HD worth of humans*

Your name alone brings cold creeping fear to the humans who hear it.

Humans suffer a -2 penalty on all saves against fear when within 30' of you. In addition, you gain a +2 circumstance bonus on all attempts to Intimidate humans.

```
name = 'Manslayer'
description = "***Feat: Manslayer.*** Your name alone brings cold creeping fear to the humans who hear it."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Manslayer.*** Humans suffer a -2 penalty on all saves against fear when within 30' of you. In addition, you gain a +2 circumstance bonus on all attempts to Intimidate humans.")
```
