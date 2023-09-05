## Bloodline of Mephistopheles
In the frozen realm of Cania, Mephistopheles offers arcane power to those who entreat with him. Tieflings linked to him master some arcane magic.

* **Ability Score Increase**. Your Intelligence score increases by 1.

* **Legacy of Cania**. You know the [mage hand](https://www.dndbeyond.com/spells/mage-hand) cantrip. Once you reach 3rd level, you can cast the Burning Hands spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Flame Blade spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Mephistopheles'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Mephistopheles.*** In the frozen realm of Cania, Mephistopheles offers arcane power to those who entreat with him. Tieflings linked to him master some arcane magic.")

    npc.INT += 1

    npc.cantripsknown.append('mage hand')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('burning hands') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('burning hands')} as a 2nd-level spell or {spelllinkify('flame blade')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
