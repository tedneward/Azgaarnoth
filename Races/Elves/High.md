# High Elf
High elves and wood elves are, by this point in Azgaarnoth's history, fairly well intermixed and are found in most locations all across Azgaarnoth; at this point in their evolution, no non-elf can tell the difference between them.

* **Ability Score Increase**. Your Intelligence score increases by 1.

* **Cantrip**. You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.

* **Elf Weapon Training**. You have proficiency with the longsword, shortsword, shortbow, and longbow.

* **Extra Language**. You can read, speak, and write one additional language of your choice.

```
name = 'High'
description = "***Subrace: High Elf.*** High elves and wood elves are, by this point in Azgaarnoth's history, fairly well intermixed and are found in most locations all across Azgaarnoth; at this point in their evolution, no non-elf can tell the difference between them."
def level0(npc):
  npc.INT += 1

  spellcasting = innatecaster(npc, 'INT', "High Elf")
  spellcasting.cantripsknown.append("CHOOSE-Wizard")

  npc.proficiencies.append("Longsword")
  npc.proficiencies.append("Shortsword")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.languages.append("CHOOSE")
```
