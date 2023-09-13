# Wood Elf
Wood elves and high elves are, by this point in Azgaarnoth's history, fairly well intermixed and are found in most locations all across Azgaarnoth; at this point in their evolution, no non-elf can tell the difference between them.

* **Elf Weapon Training**. You have proficiency with the longsword, shortsword, shortbow, and longbow.

* **Fleet of Foot**. Your base walking speed increases to 35 feet.

* **Mask of the Wild**. You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.

```
name = 'Wood'
description = "***Elvish Heritage: Wood Elf.*** One of your parents was a Wood Elf."
def level0(npc):
  npc.proficiencies.append("Longsword")
  npc.proficiencies.append("Shortsword")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.speed['walking'] = 35

  npc.traits.append("***Mask of the Wild.*** You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")
```
