# Dark Elf (*drow*)
One of your parents was a [Dark Elf](../Elves/Dark.md).

* ***Drow* Magic**. You know the [dancing lights](../../Magic/Spells/dancing-lights.md) cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.

```
name = 'Dark'
description = "***Elvish Heritage: Dark Elf.*** One of your parents was a Dark Elf."
def level0(npc):
    spellcasting = innatecaster(npc, 'CHA', 'Dark Elf')
    spellcasting.cantripsknown.append('dancing lights')

def level3(npc):
  npc.spellcasting['Dark Elf'].perday[1] = ['faerie fire']

def level5(npc):
  npc.spellcasting['Dark Elf'].perday[1].append('darkness')
```
