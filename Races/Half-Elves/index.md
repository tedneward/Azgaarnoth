# Half-Elves
*see [Half-Elves](../../Creatures/Humans.md#half-elf) for more details*

Half-Elves....

```
name = 'Half-Elf'
description = "***Race: Half-Elf.*** "
type = 'humanoid'
```

* **Ability Score Increase**. Your Charisma score increases by 2, and two other ability scores of your choice each increase by 1.

* **Age**. Half-elves age at much the same rate as humans, reaching adulthood at the age of 20. They live much longer than humans, however, often exceeding 180 years.

* **Alignment**. Half-elves share the chaotic bent of their elven heritage. They both value personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others' demands, and sometimes prove unreliable, or at least unpredictable. They are good and evil in equal numbers, a trait they share with their human parents.

* **Size**. Half-elves are more or less the same size as humans, ranging from 5 to 6 feet tall. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. Thanks to your elven heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Fey Ancestry**. You have advantage on saving throws against being charmed, and magic can't put you to sleep.

* **Languages**. You can read, speak, and write Common, Elven, and one language of your choice.

* **Elf Heritage.** Choose one of the following elvish subraces as your elvish parent's heritage:

  * [Mixed](Mixed.md)
  * [Bright Elf](Bright.md)
  * [Fey Elf](Fey.md)
  * [High Elf](High.md)
  * [Wood Elf](Wood.md)
  * [Dark Elf](Dark.md)
  * [Wild Elf](Wild.md)
  * [Shadow Elf](Shadow.md)
  * [Sea Elf](Sea.md) Your elvish parent came from Sea Elf (*maerach*) stock. You have a swimming speed of 30 feet.

  You may also be Dragonmarked:

  * [Mark of Detection](Detection.md)
  * [Mark of Storm](Storm.md)

```
def level0(npc):
    npc.CHA += 2
    npc.abilityscoreimprovement()
    npc.abilityscoreimprovement()

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.traits.append(traits['fey-ancestry'])

    npc.languages.append('Common')
    npc.languages.append('Elvish')
    npc.languages.append('CHOOSE')
```
