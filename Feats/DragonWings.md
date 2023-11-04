## Dragon Wings
*Prerequisite: Dragonborn, Half-Dragon*

You sprout draconic wings. With your wings, you have a flying speed of 20 feet if you aren't wearing heavy armor and aren't exceeding your carrying capacity.

```
name = 'Dragon Wings'
description = "***Feat: Dragon Wings.*** You sprout draconic wings."
def prereq(npc):
    if npc.race.name == 'Dragonborn':
        return True
    elif npc.race.name == 'Half-Dragon':
        return True
    else:
        return False
def apply(npc):
    npc.speed['flying'] = 20
    npc.traits.append("***Dragon Wings.*** With your wings, you have a flying speed of 20 feet if you aren't wearing heavy armor and aren't exceeding your carrying capacity.")
```

