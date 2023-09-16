# Githyanki
*see [Githyanki](../Creatures/Githyanki.md) for more details*

Within Azgaarnoth, gith are thought to be [elves](Elves.md) captured by the illithids very early in the days of the [Eldar](../History/Eldar.md) and never rescued. Once secured, the illithids examined their captive elves (and dwarves), and then subsequently genetically or behaviorally altered them into their current form. By the time the gith--named after the leader who led them in revolt--staged their successful rebellion against their illithid masters, the connection between elf and gith had long been lost to history. Despite that long and painful distance, genetically the two races seem to recognize one another. 

For whatever reason, both [githyanki](../Creatures/Githyanki.md) and [githzerai](../Creatures/Githzerai.md) trod carefully around elves, preferring to be cautious around one another. It is rumored that the [Dread Emperor](../People/DreadEmperor.md) has sought an alliance with the githyanki for centuries; rumors also contend that the [Draconic Order](../Organizations/MilitantOrders/DraconicOrder/index.md) has made a deal with the githzerai: a secret safe monastery within Azgaarnoth (to train both young githzerai as well as promising mortal monks), in exchange for information and/or introductions to "psionic dragons". The reasons for the Order's interest in these dragons, if true, are fairly obvious.

```
name = 'Githyanki'
description = "***Race: Githyanki.*** Githyanki were elves captured by mind flayers. Tortured and experimented on by the illithids, the githyanki later rebelled and won their freedom. These tall, gaunt folk have potent psionic powers and dwell, for the most part, on the Astral Plane."
type = 'humanoid'
```

* **Ability Score Increase**. Your Intelligence score increases by 1 and your Strength score increases by 2.

* **Age**. Gith reach adulthood in their late teens and live for about a century.

* **Size**. Gith are taller and leaner than humans, with most a slender 6 feet in height. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Languages**. You can speak, read, and write Common and Gith.

* **Alignment**. Githyanki tend toward lawful evil. They are aggressive and arrogant, and they remain the faithful servants of their lich-queen, Vlaakith. Renegade githyanki tend toward chaos.

* **Decadent Mastery**. You learn one language of your choice, and you are proficient with one skill or tool of your choice. In the timeless city of Tu'narath, githyanki have bountiful time to master odd bits of knowledge.

* **Martial Prodigy**. You are proficient with light and medium armor and with shortswords, longswords, and greatswords.

* **Githyanki Psionics**. You know the [mage hand](../Magic/Spells/mage-hand.md) cantrip, and the hand is invisible when you cast the cantrip with this trait.

  When you reach 3rd level, you can cast the [jump](../Magic/Spells/jump.md) spell once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the [misty step](../Magic/Spells/misty-step.md) spell once with this trait, and you regain the ability to do so when you finish a long rest.

  Intelligence is your spellcasting ability for these spells. When you cast them with this trait, they don't require components.

```
def level0(npc):
    npc.STR += 2
    npc.INT += 1

    npc.speed['walking'] = 30

    npc.languages.append('Common')
    npc.languages.append('Gith')
    npc.languages.append('CHOOSE')

    chooseskill(npc)
    
    npc.proficiencies.append('Light armor')
    npc.proficiencies.append('Medium armor')
    npc.proficiencies.append('Shortsword')
    npc.proficiencies.append('Longsword')
    npc.proficiencies.append('Greatsword')

    npc.newspellcasting('Githyanki', 'INT').cantripsknown.append('mage hand')

def level3(npc):
    npc.spellcasting['Githyanki'].spells[1].append('jump')
    npc.spellcasting['Githyanki'].slots = [ 1 ]

def level5(npc):
    npc.spellcasting['Githyanki'].spells[2].append('misty step')
    npc.spellcasting['Githyanki'].slots = [ 1, 1 ]
```
