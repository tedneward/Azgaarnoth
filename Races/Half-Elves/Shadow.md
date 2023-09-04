# Shadow Elves (*shadar-kai*)
One of your parents was a Shadow Elf.

* **Necrotic Resistance**. You have resistance to necrotic damage.

* **Blessing of the Raven Queen**. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest. Starting at 3rd level, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.

```
name = 'Shadow'
def level0(npc):
  npc.description.append("***Elvish Heritage: Shadow Elf.*** One of your parents was a Shadow Elf.")

  npc.damageresistances.append('necrotic')

  npc.bonusactions.append("***Blessing of the Raven Queen (Recharges on long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see.")

def level3(npc):
    replace("***Blessing of the Raven Queen", npc.bonusactions, "***Blessing of the Raven Queen (Recharges on long rest).*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. When you do, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent.")
```
