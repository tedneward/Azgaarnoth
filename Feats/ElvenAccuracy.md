## Elven Accuracy
*Prerequisite: Elf or half-elf*

The accuracy of elves is legendary, especially that of elf archers and spellcasters. You have uncanny aim with attacks that rely on precision rather than brute force. You gain the following benefits:

* Increase your Dexterity, Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20

* Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.

```
name = 'Elven Accuracy'
description = "***Feat: Elven Accuracy.*** The accuracy of elves is legendary, especially that of elf archers and spellcasters. You have uncanny aim with attacks that rely on precision rather than brute force."
def prereq(npc):
    if npc.race.name == 'Elf' or npc.race.name == 'Half-Elf': return True
    else: return False
def apply(npc):
    chooseability(npc, ['DEX','INT','WIS','CHA'])

    npc.traits.append("***Elven Accuracy.*** Whenever you have advantage on an attack roll using Dexterity, Intelligence, Wisdom, or Charisma, you can reroll one of the dice once.")
```
