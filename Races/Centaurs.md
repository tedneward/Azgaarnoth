# [Centaurs](../Creatures/Centaur.md)

```
name = 'Centaur'
description = "***Race: Centaur.***"
type = 'humanoid/fey'

def level0(npc):
```

* **Ability Score Increase**. Your Strength score increases by 2, and your Wisdom score increases by 1.

```
    npc.STR += 2
    npc.WIS += 1
```

* **Age**. Centaurs mature and age at about the same rate as humans.

* **Alignment**. Centaurs are inclined toward neutrality.

* **Size**. Your size is Large; you tower over most other humanoids.

```
    npc.size = 'Large'
```

* **Speed**. Your base walking speed is 50 feet.

```
    npc.speed['walking'] = 50
```

* **Fey**. You are considered fey and humanoid.

* **Charge**. If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can use your bonus action to make a hoof attack.

```
    npc.bonusactions.append("***Charge.*** If you move at least 30 feet straight toward a target and then hit it with a melee weapon attack on the same turn, you can use your bonus action to make a hoof attack.")
```

* **Hooves**. Your hooves are natural melee weapons, with which you're proficient. If you hit with a hoof, the target takes bludgeoning damage equal to 1d4 + your Strength modifier.

```
    npc.defer(lambda npc: npc.actions.append(f"***Hooves.*** Melee Weapon Attack: {npc.STRbonus() + npc.proficiencybonus()} to hit, reach 5 ft, one target. Hit: 1d4 + {npc.STRbonus()}."))
```

* **Equine Build**. Any climb that requires hands and feet is especially difficult for you because of your hooves. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.

```
    npc.traits.append("***Equine Build.*** In addition, any climb that requires hands and feet is especially difficult for you because of your hooves. When you make such a climb, each foot of movement costs you 4 extra feet, instead of the normal 1 extra foot.")
```

* **Survivor**. You have proficiency in one of the following skills: Animal Handling, Medicine, Nature, or Survival.

```
    chooseskill(npc, ['Animal Handling', 'Medicine', 'Nature', 'Survival'])
```

* **Languages**. You can speak, read, and write Common and Sylvan.

```
    npc.languages.append('Common')
    npc.languages.append('Sylvan')
```
