# Wild Elves (*grugach*)
One of your parents was a Wild Elf.

* ***Grugach* Weapon Training**. You have proficiency with the spear, shortbow, longbow, and net.

* **Cantrip**. You know one cantrip of your choice from the druid spell list. Wisdom is your spellcasting ability for it.

```
name = 'Wild'
def level0(npc):
  npc.description.append("***Elvish Heritage: Wild Elf.*** One of your parents was a Wild Elf.")

  npc.proficiencies.append("Spear")
  npc.proficiencies.append("Net")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.traits.append("***Cantrip***. You know one cantrip of your choice from the Druid spell list. Wisdom is your spellcasting ability for it.")
```
