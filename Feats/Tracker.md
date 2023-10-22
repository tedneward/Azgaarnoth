## Tracker
You have spent time hunting creatures and honed your skills, gaining the following benefits:

* Increase your Wisdom score by 1, to a maximum of 20.
* You learn the [hunter's mark](../Magic/Spells/hunters-mark.md) spell. You can cast it once without expending a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast the spell using any spell slots you have. Wisdom is your spellcasting ability for this spell.
* You have advantage on Wisdom (Survival) checks to track creatures.

```
name = 'Tracker'
description = "***Feat: Tracker.*** You have spent time hunting creatures and honed your skills."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    spellcasting = innatecaster(npc, 'WIS', "Tracker")
    spellcasting.perday[1].append("hunter's mark")

    npc.traits.append("***Tracker.*** You have advantage on Wisdom (Survival) checks to track creatures.")
```

