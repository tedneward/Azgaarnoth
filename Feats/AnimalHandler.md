## Animal Handler
You master the techniques needed to train and handle animals. You gain the following benefits.

* Increase your Wisdom score by 1, to a maximum of 20.
* You gain proficiency in the Animal Handling skill. If you are already proficient in the skill, you add double your proficiency bonus to checks you make with it.
* You can use a bonus action on your turn to command one friendly beast within 60 feet of you that can hear you and that isn't currently following the command of someone else. You decide now what action the beast will take and where it will move during its next turn, or you issue a general command that lasts for 1 minute, such as to guard a particular area.

```
name = 'Animal Handler'
description = "***Feat: Animal Handler.*** You master the techniques needed to train and handle animals."
def prereq(npc): return True
def apply(npc):
    npc.WIS += 1

    npc.addskillorexpertise("Animal Handling")

    npc.bonusactions.append("***Animal Handling.*** You can command one friendly beast within 60 feet of you that can hear you and that isn't currently following the command of someone else. You decide now what action the beast will take and where it will move during its next turn, or you issue a general command that lasts for 1 minute, such as to guard a particular area.")
```
