## Keen Mind
You have a mind that can track time, direction, and detail with uncanny precision. You gain the following benefits.

* Increase your Intelligence score by 1, to a maximum of 20.
* You always know which way is north.
* You always know the number of hours left before the next sunrise or sunset.
* You can accurately recall anything you have seen or heard within the past month.

```
name = 'Keen Mind'
description = "***Feat: Keen Mind.*** You have a mind that can track time, direction, and detail with uncanny precision."
def prereq(npc): return True
def apply(npc):
    npc.INT += 1

    npc.traits.append("***Keen Mind.*** You always know which way is north, the number of hours left before the next sunrise or sunset, and you can accurately recall anything you have seen or heard within the past month.")
```
