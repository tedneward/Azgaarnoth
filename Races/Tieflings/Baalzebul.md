### Bloodline of Baalzebul
The crumbling realm of Maladomini is ruled by Baalzebul, who excels at corrupting those whose minor sins can be transformed into acts of damnation. Tieflings linked to this archdevil can corrupt others both physically and psychically.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Legacy of Maladomini** Once you reach 3rd level, you can cast the [Ray of Sickness](https://www.dndbeyond.com/spells/ray-of-sickness) spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the [Crown of Madness](https://www.dndbeyond.com/spells/crown-of-madness) spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.


```
name = 'Baalzebul'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Baalzebul.*** The crumbling realm of Maladomini is ruled by Baalzebul, who excels at corrupting those whose minor sins can be transformed into acts of damnation. Tieflings linked to this archdevil can corrupt others both physically and psychically.")

    npc.INT += 1

    npc.cantripsknown.append("thaumaturgy")

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('ray of sickness') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('ray of sickness')} as a 2nd-level spell or {spelllinkify('crown of madness')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
