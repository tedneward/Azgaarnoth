### Winged Bloodline
Rather than magic, certain tieflings inherit the leathery wings of their devilish ancestors.

* **Ability Score Increase** Your Intelligence score increases by 1.
* **Winged** You have bat-like wings sprouting from your shoulders. You have a flying speed of 30 feet while you aren’t wearing heavy armor.

```
name = 'Winged'
def level0(npc):
    npc.description.append("***Tiefling Bloodline: Winged.*** Rather than magic, certain tieflings inherit the leathery wings of their devilish ancestors.")

    npc.INT += 1
    npc.traits.add("***Winged.*** You have a flying speed only while you aren't wearing heavy armor.")
    npc.speed['flying'] = 30
```
