# Wild Elves (*grugach*)
One of your parents was a Wild Elf.

* ***Grugach* Weapon Training**. You have proficiency with the spear, shortbow, longbow, and net.

* **Cantrip**. You know one cantrip of your choice from the druid spell list. Wisdom is your spellcasting ability for it.

```
name = 'Wild'
description = "***Elvish Heritage: Wild Elf.*** One of your parents was a Wild Elf."
def level0(npc):
  npc.proficiencies.append("Spear")
  npc.proficiencies.append("Net")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.newspellcasting('Wild Elf', 'WIS').cantripsknown.append("CHOOSE-Druid")
```
