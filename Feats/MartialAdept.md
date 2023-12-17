## Martial Adept
You have martial training that allows you to perform special combat [maneuvers](../Classes/Fighter/Maneuvers.md). You gain the following benefits:

* You learn two [maneuvers](../Classes/Fighter/Maneuvers.md) of your choice . If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).
* You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it. You regain your expended superiority dice when you finish a short or long rest.

```
name = 'Martial Adept'
description = "***Feat: Martial Adept.*** You have martial training that allows you to perform special combat maneuvers."
def prereq(npc): return True
def apply(npc):
    if getattr(npc, "fightingmaneuvers", None) == None:
        allclasses['Fighter'].choosemaneuver(npc, 1, 'd6')
    else:
        npc.superioritydice += 1
        allclasses['Fighter'].choosemaneuver(npc)

    allclasses['Fighter'].choosemaneuver(npc)
```
