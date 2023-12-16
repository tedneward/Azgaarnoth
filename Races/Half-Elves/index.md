# Half-Elves
Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves. Some half-elves live among humans, set apart by their emotional and physical differences, watching friends and loved ones age while time barely touches them. Others live with the elves, growing restless as they reach adulthood in the timeless elven realms, while their peers continue to live as children. Many half-elves, unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life.

```
name = 'Half-Elf'
description = "***Race: Half-Elf.*** Walking in two worlds but truly belonging to neither, half-elves combine what some say are the best qualities of their elf and human parents: human curiosity, inventiveness, and ambition tempered by the refined senses, love of nature, and artistic tastes of the elves. Some half-elves live among humans, set apart by their emotional and physical differences, watching friends and loved ones age while time barely touches them. Others live with the elves, growing restless as they reach adulthood in the timeless elven realms, while their peers continue to live as children. Many half-elves, unable to fit into either society, choose lives of solitary wandering or join with other misfits and outcasts in the adventuring life."
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
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    for _ in range(0, 2):
        ability = choose("Choose an ability to improve: ", abilities)
        if ability == 'STR': npc.STR += 1
        elif ability == 'DEX': npc.DEX += 1
        elif ability == 'CON': npc.CON += 1
        elif ability == 'INT': npc.INT += 1
        elif ability == 'WIS': npc.WIS += 1
        elif ability == 'CHA': npc.CHA += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.traits.append(traits['fey-ancestry'])

    npc.languages.append('Common')
    npc.languages.append('Elvish')
    npc.languages.append('CHOOSE')
```
