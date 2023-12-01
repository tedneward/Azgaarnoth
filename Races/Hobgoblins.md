# Hobgoblins
[Hobgoblins](../Creatures/Hobgoblins.md) are large goblinoids with dark orange or red-orange skin. A hobgoblin measures virtue by physical strength and martial prowess, caring about nothing except skill and cunning in battle.

```
name = 'Hobgoblin'
description = "***Race: Hobgoblin.*** Hobgoblins are large goblinoids with dark orange or red-orange skin. A hobgoblin measures virtue by physical strength and martial prowess, caring about nothing except skill and cunning in battle."
type = 'humanoid'

def level0(npc):
```

* **Ability Score Increase**. Your Constitution score increases by 2, and your Intelligence score increases by 1.

```
    npc.CON += 2
    npc.INT += 1
```

* **Age**. Hobgoblins mature at the same rate as humans and have lifespans similar in length to theirs.

* **Alignment**. Hobgoblin society is built on fidelity to a rigid, unforgiving code of conduct. As such, they tend toward lawful evil or lawful neutral. Lawful good hobgoblins are less common in the Ulmhorde, but in Yithi and Zhi, they're the norm.

* **Size**. Hobgoblins are between 5 and 6 feet tall and weigh between 150 and 200 pounds. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed**. Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Martial Training**. You are proficient with two martial weapons of your choice and with light armor.

```
    wpn = choose("Choose a martial weapon: ", weapons['martial-melee'] | weapons['martial-ranged'])
    npc.proficiencies.append(wpn[0])
    wpn = choose("Choose a martial weapon: ", weapons['martial-melee'] | weapons['martial-ranged'])
    npc.proficiencies.append(wpn[0])
    for arm in armor['light']:
        npc.proficiencies.append(arm)
```

* **Saving Face**. Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.

```
    npc.traits.append("***Saving Face (Recharges on short or long rest).*** If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5).")
```

* **Languages**. You can speak, read, and write Common and Goblin.

```
    npc.languages.append('Common')
    npc.languages.append('Goblin')
```
