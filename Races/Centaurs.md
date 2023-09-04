# [Centaurs](../Creatures/Centaur.md)

```
name = 'Centaur'
type = 'monstrosity'
```

* **Ability Score Increase**. Your Strength score increases by 2, and your Wisdom score increases by 1.

* **Age**. Centaurs mature and age at about the same rate as humans.

* **Alignment**. Centaurs are inclined toward neutrality.

* **Size**. Your size is Medium, yet you tower over most other humanoids.

* **Speed**. Your base walking speed is 50 feet.

* **Fey**. You are considered fey instead of humanoid.

* **Charge**. If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can use your bonus action to make a hoof attack.

* **Hooves**. Your hooves are natural melee weapons, with which you’re proficient. If you hit with a hoof, the target takes bludgeoning damage equal to 1d4 + your Strength modifier.

* **Equine Build**. You count as one size larger when determining your carrying capacity and the weight you can push or drag. In addition, any climb that requires hands and feet is especially difficult for you because of your hooves. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.

* **Survivor**. You have proficiency in one of the following skills: Animal Handling, Medicine, Nature, or Survival.

* **Languages**. You can speak, read, and write Common and Sylvan.

```
def level0(npc):
    npc.size = 'Large'
    npc.speed['walking'] = 50
    npc.defer(lambda npc: npc.actions.append("***Hooves.*** Melee Weapon Attack: {npc.STRbonus() + npc.proficiencybonus()} to hit, reach 5 ft, one target. Hit: 1d4 + {npc.STRbonus()}."))
    npc.bonusactions.append("***Charge.*** If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can use your bonus action to make a hoof attack.")
    npc.traits.append("***Equine Build.*** In addition, any climb that requires hands and feet is especially difficult for you because of your hooves. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.")
    npc.skills.append(choice("Choose one of these skills: ", ['Animal Handling', 'Medicine', 'Nature', 'Survival']))
    npc.languages.append('Common')
    npc.languages.append('Sylvan')
```
