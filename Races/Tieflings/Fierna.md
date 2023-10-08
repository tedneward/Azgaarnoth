## Bloodline of Fierna
A master manipulator, Fierna grants tieftings tied to her forceful personalities.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Legacy of Phlegethos**. You know the [friends](https://www.dndbeyond.com/spells/friends)cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Suggestion spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Fierna'
description = "***Tiefling Bloodline of Fierna.*** A master manipulator, Fierna grants tieftings tied to her forceful personalities."
def level0(npc):
    npc.WIS += 1

    spellcasting = innatecaster(npc, 'CHA', "Fierna Tiefling")
    spellcasting.cantripsknown.append('friends')

def level3(npc):
    npc.spellcasting['Fierna Tiefling'].perday[1] = ['charm person']

def level5(npc):
    npc.spellcasting['Fierna Tiefling'].perday[1].append('suggestion')
```

