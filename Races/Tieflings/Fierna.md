## Bloodline of Fierna
A master manipulator, Fierna grants tieftings tied to her forceful personalities.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Legacy of Phlegethos**. You know the [friends](https://www.dndbeyond.com/spells/friends)cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Suggestion spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Fierna'
def level0(npc):
    npc.description.append("***Tiefling Bloodline of Fierna.*** A master manipulator, Fierna grants tieftings tied to her forceful personalities.")

    npc.WIS += 1

    npc.cantripsknown.append('friends')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('charm person') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('charm person')} as a 2nd-level spell or {spelllinkify('suggestion')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```

