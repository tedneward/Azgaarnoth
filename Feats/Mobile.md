## Mobile
You are exceptionally speedy and agile. You gain the following benefits:

* Your speed increases by 10 feet.
* When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.
* When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not.

```
name = 'Mobile'
description = "***Feat: Mobile.*** You are exceptionally speedy and agile."
def prereq(npc): return True
def apply(npc):
    npc.speed['walking'] += 10
    npc.actions.append("***Mobile Dash.*** When you use the Dash action, difficult terrain doesn't cost you extra movement on that turn.")
    npc.actions.append("***Mobile Attack.*** When you make a melee attack against a creature, you don't provoke opportunity attacks from that creature for the rest of the turn, whether you hit or not.")
```
