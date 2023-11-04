## Fey Teleportation
*Prerequisite: Elf (high)*

Your study of high elven lore has unlocked fey power that few other elves possess, except your eladrin cousins. Drawing on your fey ancestry, you can momentarily stride through the Feywild to shorten your path from one place to another. You gain the following benefits:

* Increase your Intelligence or Charisma score by 1, to a maximum of 20.
* You learn to speak, read, and write Sylvan
* You learn the [misty step](http://azgaarnoth.tedneward.com/magic/spells/misty-step) spell and can cast it once without expending a spell slot. You regain the ability to cast it in this way when you finish a short or long rest. Intelligence is your spellcasting ability for this spell.

```
name = 'Fey Teleportation'
description = "***Feat: Fey Teleportation.*** Your study of high elven lore has unlocked fey power that few other elves possess, except your eladrin cousins."
def prereq(npc): return npc.race.name == 'Elf' and npc.subrace.name == 'High'
def apply(npc):
    ability = choose("Choose one: ", ['INT', 'CHA'])
    if ability == 'INT': npc.INT += 1
    else: npc.CHA += 1

    npc.languages.append("Sylvan")

    spellcasting == innatecaster(npc, 'INT', name)
    spellcasting.perday[1] = ['misty step']
```
