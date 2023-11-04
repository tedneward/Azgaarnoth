### Bloodline of Baalzebul
The crumbling realm of Maladomini is ruled by Baalzebul, who excels at corrupting those whose minor sins can be transformed into acts of damnation. Tieflings linked to this archdevil can corrupt others both physically and psychically.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Legacy of Maladomini** Once you reach 3rd level, you can cast the [Ray of Sickness](https://www.dndbeyond.com/spells/ray-of-sickness) spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the [Crown of Madness](https://www.dndbeyond.com/spells/crown-of-madness) spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.


```
name = 'Baalzebul'
description = "***Tiefling Bloodline of Baalzebul.*** The crumbling realm of Maladomini is ruled by Baalzebul, who excels at corrupting those whose minor sins can be transformed into acts of damnation. Tieflings linked to this archdevil can corrupt others both physically and psychically."
def level0(npc):
    npc.INT += 1

    spellcasting = innatecaster(npc, 'INT', "Baalzebul Tiefling")
    spellcasting.cantripsknown.append("thaumaturgy")

def level3(npc):
    npc.spellcasting['Baalzebul Tiefling'].perday[1] = []
    npc.spellcasting['Baalzebul Tiefling'].perday[1].append('ray of sickness')

def level5(npc):
    npc.spellcasting['Baalzebul Tiefling'].perday[1].append("crown of madness")
```
