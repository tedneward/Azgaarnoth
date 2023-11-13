## Savage Charge
*Prerequisites: Must have Bite attack*

You know how to time your movement to get a nip in.

You can make a Bite attack as a bonus action at the end of a Dash action.

```
name = 'Savage Charge'
description = "***Feat: Savage Charge.*** You know how to time your movement to get a nip in."
def prereq(npc):
    for act in npc.actions:
        if act[0:len("***Bite")] == "***Bite": return true
    for act in npc.bonusactions:
        if act[0:len("***Bite")] == "***Bite": return true
    for act in npc.reactions:
        if act[0:len("***Bite")] == "***Bite": return true
    return False
def apply(npc):
    npc.bonusactions.append("***Savage Charge.*** You make a Bite attack at the end of a Dash action.")
```
