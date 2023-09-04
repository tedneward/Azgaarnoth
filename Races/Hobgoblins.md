# Hobgoblins

```
name = 'Hobgoblin'
type = 'humanoid'
```

* **Ability Score Increase**. Your Constitution score increases by 2, and your Intelligence score increases by 1.

* **Age**. Hobgoblins mature at the same rate as humans and have lifespans similar in length to theirs.

* **Alignment**. Hobgoblin society is built on fidelity to a rigid, unforgiving code of conduct. As such, they tend toward lawful evil or lawful neutral. Lawful good hobgoblins are not unknown, but generally have converted to a good ethos due to events in their past.

* **Size**. Hobgoblins are between 5 and 6 feet tall and weigh between 150 and 200 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Martial Training**. You are proficient with two martial weapons of your choice and with light armor.

* **Saving Face**. Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.

* **Languages**. You can speak, read, and write Common and Goblin.

```
def level0(npc):
    npc.size = 'Medium'
    npc.speed['walking'] = 30

    # Ability Score Increase
    npc.CON += 2
    npc.INT += 1

    npc.senses['darkvision'] = 60

    npc.traits.append("***Saving Face.*** Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.")

    npc.proficiencies.append('Martial weapon')
    npc.proficiencies.append('Martial weapon')
    npc.proficiencies.append('Light armor')

    npc.languages.append('Common')
    npc.languages.append('Goblin')

    npc.description.append('***Race: Hobgoblin.***')
```