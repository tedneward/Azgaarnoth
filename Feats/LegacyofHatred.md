## Legacy of Hatred
*Prerequisites: Gnoll, Int 13+*

You have long battled your race's ancient foes, and know their treacherous ways.

You gain a +1 racial bonus on attack rolls and a +1 dodge bonus to AC against elves, dwarves, and humans.

```
name = 'Legacy of Hatred'
description = "***Feat: Legacy of Hatred.*** You have long battled your race's ancient foes, and know their treacherous ways."
def prereq(npc): return npc.race.name == 'Gnoll' and npc.INT >= 13
def apply(npc):
    npc.traits.append("***Legacy of Hatred.*** You gain a +1 bonus on attack rolls and a +1 bonus to AC when fighting against elves, dwarves, and humans.")
```
