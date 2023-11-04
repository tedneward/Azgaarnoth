## Squat Nimbleness
*Prerequisite: Dwarf or other Small race*

You are uncommonly nimble for your race. You gain the following benefits:

* Increase your Strength or Dexterity score by 1, to a maximum of 20.
* Increase your walking speed by 5 feet.
* You gain proficiency in the Acrobatics or Athletics skill (your choice).
* You have advantage on any Strength (Athletics) or Dexterity (Acrobatics) check you make to escape from being grappled.

```
name = 'Squat Nimbleness'
description = "***Feat: Squat Nimbleness.*** You are uncommonly nimble for your race."
def prereq(npc):
    return npc.size == 'Small'
def apply(npc):
    npc.STR += 1
    npc.DEX += 1

    npc.speed['walking'] += 5
    
    npc.proficiencies.append(choose("Choose a proficiency: ", ['Acrobatics', 'Athletics']))

    npc.traits.append("***Squat Nimbleness.*** You have advantage on any Strength (Athletics) or Dexterity (Acrobatics) check you make to escape from being grappled.")
```
