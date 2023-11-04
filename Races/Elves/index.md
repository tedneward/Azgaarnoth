# [Elves](../Creatures/Elves.md)
Elves may be [dragonmarked](Dragonmarked.md) with the Mark of Shadow; see that entry for details.

```
name = 'Elf'
description = "***Race: Elf.*** Elves are almost as diverse as humans in their occupations, entertainments, and while most elves have a strong familial tie between them, numerous elves have wandered away from home to make their mark within the world, then to return and take up familial responsibilities. Elves revere their familial ancestors, and will often have a shrine to a favored ancestor, but elves do not see their familial ancestors as gods, and many elves are quite comfortable serving in a religious order even as they put offerings to their revered ancestors out on important holidays."
type = 'humanoid'
```

* **Ability Score Increase**. Your Dexterity score increases by 2.

* **Age**. Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 25 and most can live to be 150 years old.

* **Alignment**. Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and are good more often than not.

* **Size**. Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Fey Ancestry**. You have advantage on saving throws against being charmed, and magic can't put you to sleep.

* **Trance**. Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.

* **Keen Senses**. You have proficiency in the Perception skill.

* **Languages**. You can speak, read, and write Common and Elven.

```
def level0(npc):
    npc.DEX += 2

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.traits.append(traits['fey-ancestry'])

    npc.conditionimmunities.append("sleep")

    npc.traits.append("***Trance.*** Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance'. While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.")

    npc.skills.append("Perception")

    npc.languages.append("Common")
    npc.languages.append("Elven")
```

Elves have a number of genetically-differentiated offshoots (subraces):

* [Bright Elves](Elves/Bright.md)
* [High Elves](Elves/High.md)
* [Wood Elves](Elves/Wood.md)
* [Fey Elves](Elves/Fey.md)
* [Winged Elves](Elves/Winged.md)
* [Wild Elves](Elves/Wild.md)
* [Sea Elves](Elves/Sea.md)
* [Shadow Elves](Elves/Shadow.md)
* [Dark Elves](Elves/Dark.md)

