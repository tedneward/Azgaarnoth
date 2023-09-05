# Scourge Aasimar
Scourge aasimar are imbued with a divine energy that blazes intensely within them. It feeds a powerful desire to destroy evil — a desire that is, at its best, unflinching and, at its worst, all-consuming. Many scourge aasimar wear masks to block out the world and focus on containing this power, unmasking themselves only in battle.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Radiant Consumption**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing a searing light to radiate from you, pour out of your eyes and mouth, and threaten to char you.
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you shed bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of your turns, you and each creature within 10 feet of you take radiant damage equal to half your level (rounded up). In addition, once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.

```
name = 'Scourge'

def level0(npc): 
    npc.description.append("***Scourge Aasimar.*** ...")

    npc.CON += 1

def level3(npc): 
    npc.actions.append("***Radiant Consumption (Recharges after long rest).*** The aasimar can unleash the divine energy within it, causing a searing light to radiate from it, pouring out of its eyes and mouth. Its transformation lasts for 1 minute or until it ends it as a bonus action. During this time, the aasimar sheds bright light in a 10-foot radius and dim light for an additional 10 feet, and at the end of each of its turns, the aasimar and each creature within 10 feet of you take radiant damage equal to half its level (rounded up). In addition, once on each of its turns, the aasimar can deal extra radiant damage (equaling its level) to one target when it deals damage with an attack or a spell.")
```
