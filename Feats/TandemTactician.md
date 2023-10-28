## Tandem Tactician
Your presence in a scrap tends to elevate your comrades. You gain the following benefits:

* You can use the Help action as a bonus action.
* When you use the Help action to aid an ally in attacking a creature, increase the range of the Help action by 10 feet. Additionally, you can help two allies targeting the same creature within range when you use the Help action this way. 

```
name = 'Tandem Tactician'
description = "***Feat: Tandem Tactician.*** Your presence in a scrap tends to elevate your comrades."
def prereq(npc): return True
def apply(npc):
    npc.bonusactions.append("***Tandem Tactician.*** You can use the Help action as a bonus action. When you use the Help action to aid an ally in attacking a creature, increase the range of the Help action by 10 feet. Additionally, you can help two allies targeting the same creature within range when you use the Help action this way.")
```
