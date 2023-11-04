## Acrobat
You become more nimble, gaining the following benefits:

* Increase your Dexterity score by 1, to a maximum of 20.
* You gain proficiency in the Acrobatics skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* As a bonus action, you can make a DC 15 Dexterity (Acrobatics) check. If you succeed, difficult terrain doesn't cost you extra movement until the end of the current turn.

```
name = 'Acrobat'
description = "***Feat: Acrobat.*** You become more nimble."
def prereq(npc): return True
def apply(npc): 
    npc.DEX += 1

    npc.addskillorexpertise("Acrobatics")

    npc.bonusactions.append("***Acrobat.*** You can make a DC 15 Dexterity (Acrobatics) check. If you succeed, difficult terrain doesn't cost you extra movement until the end of the current turn.")
```
