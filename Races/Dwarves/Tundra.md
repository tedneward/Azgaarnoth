# Tundra Dwarf
In the farthest icy reaches of the world in southernmost Dradehalia and Chidia, where hordes of humanoid barbarians rove in bands hunting massive blubbery beasts and battling the environment itself, the sturdy tundra dwarves can be found eking out a stable life together. Many clans of tundra dwarves live in strongholds of stone or ice, often underground, but some clans make their way as nomads across the tundra, keeping warm with fur tents and animal blubber.

As a tundra dwarf, you owe your heartiness and endurance in the cold to your dwarven ancestors who first settled in the frozen tundras. Tundra dwarves usually have white or blond hair, but some have orange hair, and brown hair is uncommon but not especially rare. They are slightly tall for dwarves, with mostly pale skin and blue eyes. Some clans of tundra dwarves are exceptions, with mostly tan skin, black or white hair, and brown eyes.

***Ability Score Increase.*** Your Strength score or your Wisdom score increases by 1 (your choice).

***Cold Resistance.*** You have resistance to cold damage.

***Icecunning.*** Your dwarf Stonecunning trait also applies to checks about the origin of ice carvings.

***Snow Treader.*** You can move across icy or snowy difficult terrain without expending extra movement, and you have advantage on saving throws to avoid hazards caused by frozen ground, such as falling prone.

```
name = 'Tundra'
description = "***Subrace: Tundra Dwarf.*** You owe your heartiness and endurance in the cold to your dwarven ancestors who first settled in the frozen tundras. Tundra dwarves usually have white or blond hair, but some have orange hair, and brown hair is uncommon but not especially rare. They are slightly tall for dwarves, with mostly pale skin and blue eyes. Some clans of tundra dwarves are exceptions, with mostly tan skin, black or white hair, and brown eyes."

def level0(npc): 
    choice = choose("Choose one: ", ['STR','WIS'])
    if choice == 'STR': npc.STR += 1
    else npc.WIS += 1

    npc.damageresistances.append('cold')

    npc.traits.append("***Icecunning.*** Your dwarf Stonecunning trait also applies to checks about the origin of ice carvings.")

    npc.traits.append("***Snow Treader.*** You can move across icy or snowy difficult terrain without expending extra movement, and you have advantage on saving throws to avoid hazards caused by frozen ground, such as falling prone.")
```
