## Burglar
You pride yourself on your quickness and your close study of certain clandestine activities. You gain the following benefits:

* Increase your Dexterity score by 1, to a maximum of 20.
* You gain proficiency with thieves' tools. If you are already proficient with them, you add double your proficiency bonus to checks you make with them.

```
name = 'Burglar'
description = "***Feat: Burglar.*** You pride yourself on your quickness and your close study of certain clandestine activities."
def prereq(npc): return True
def apply(npc):
    npc.DEX += 1

    npc.addskillorexpertise("Thieves' tools")
```
