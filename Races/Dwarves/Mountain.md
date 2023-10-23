# Mountain Dwarf
The hill and mountain dwarves are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the hills as part of their guild/clan, and mountain dwarves are often found in mountains for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them.

* **Ability Score Increase**. Your Strength score increases by 2.

* **Dwarven Armor Training**. You have proficiency with light and medium armor.

```
name = 'Mountain'
description = "***Subrace: Mountain Dwarf.*** The hill and mountain dwarves are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the hills as part of their guild/clan, and mountain dwarves are often found in mountains for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them."

def level0(npc): 
    npc.STR += 2

    for arm in armor['light'] | armor['medium']:
        npc.proficiencies.append(arm)
```
