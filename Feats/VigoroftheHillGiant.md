## Vigor of the Hill Giant
*Prerequisite: 4th Level, [Strike of the Giants (Hill Giant) Feat](#strike-of-the-giants)*

You've manifested the resilience emblematic of hill giants, granting you the following benefits:

* **Ability Score Increase.** Increase your Constitution score by 1, to a maximum of 20.
* **Bulwark.** When you are subjected to an effect that would move you at least 5 feet or knock you prone, you can use your reaction to steady yourself. You are then neither moved nor knocked prone.

```
name = 'Vigor of the Hill Giant'
description = "***Feat: Vigor of the Hill Giant.*** You've manifested the resilience emblematic of hill giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    npc.CON += 1

    npc.reactions.append("***Bulwark.*** When you are subjected to an effect that would move you at least 5 feet or knock you prone, you steady yourself and are then neither moved nor knocked prone.")
```

