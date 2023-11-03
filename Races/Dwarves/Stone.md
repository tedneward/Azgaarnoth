# Stone Dwarf
As a stone dwarf, you exist between the realm of dwarf and elemental earth. Despite their hardened biology and immunity to poisons, stone dwarves are made of brittle and crumbly rock, and aren't much physically tougher than a regular dwarf. They also weigh more than the average dwarf, since their stony flesh is heavier than regular flesh. They often have moss, lichen, or vines growing where a normal dwarf would grow hair, but otherwise look like living, moving statues carved to resemble normal dwarves.

Deep in the Underdark, clans of dwarves with deeper magical and genetic ties to the very elemental power of Earth reside. These stones dwarves are made of living stone instead of flesh. They still eat, drink, and breathe the way a dwarf of flesh does, and they grow and age the same as other dwarves, but their organs are stone, and they have no blood at all to poison. A stone dwarf's brain is made of electrified copper, and this enables some of them to think more quickly than a brain of flesh. 

***Ability Score Increase.*** Your Strength score or your Intelligence score increases by 1 (your choice).

***Elemental Hybrid.*** You have two creature types: humanoid (dwarf) and elemental (earth). You can be affected by a game effect if it works on either of your creature types.

***Stone Body.*** When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.

In addition, your earthen metabolism grants you the following benefits:

* You are immune to poison and the poisoned condition.
* You have no blood and you cannot be petrified.
* You have advantage on saving throws made against disease.

```
name = 'Stone'
description = "***Subrace: Stone Dwarf.*** Despite their hardened biology and immunity to poisons, stone dwarves are made of brittle and crumbly rock, and aren't much physically tougher than a regular dwarf. They also weigh more than the average dwarf, since their stony flesh is heavier than regular flesh. They often have moss, lichen, or vines growing where a normal dwarf would grow hair, but otherwise look like living, moving statues carved to resemble normal dwarves."

def level0(npc): 
    choice = choose("Choose one: ", ['STR','INT'])
    if choice == 'STR': npc.STR += 1
    else npc.INT += 1

    npc.type = 'humanoid/elemental'
    npc.traits.append("***Elemental Hybrid.*** You have two creature types: humanoid (dwarf) and elemental (earth). You can be affected by a game effect if it works on either of your creature types.")

    npc.traits.append("***Stone Body.*** When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor. In addition, you have no blood, and you have advantage on saving throws against disease.")
    npc.armorclass['natural armor'] = 13

    npc.damageimmunities.append("poison")
    npc.conditionimmunities.append("poisoned")
    npc.conditionimmunities.append("petrified")
```
