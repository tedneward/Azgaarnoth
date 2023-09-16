# Gith
Within Azgaarnoth, gith are thought to be [elves](Elves/index.md) captured by the illithids very early in the days of the [Eldar](../History/Eldar.md) and never rescued. Once secured, the illithids examined their captive elves (and dwarves), and then subsequently genetically or behaviorally altered them into their current form. By the time the gith--named after the leader who led them in revolt--staged their successful rebellion against their illithid masters, the connection between elf and gith had long been lost to history. Despite that long and painful distance, genetically the two races seem to recognize one another. 

For whatever reason, both [githyanki](../Creatures/Githyanki.md) and [githzerai](../Creatures/Githzerai.md) trod carefully around elves, preferring to be cautious around one another. It is rumored that the [Dread Emperor](../People/DreadEmperor.md) has sought an alliance with the githyanki for centuries; rumors also contend that the [Draconic Order](../Organizations/MilitantOrders/DraconicOrder/index.md) has made a deal with the githzerai: a secret safe monastery within Azgaarnoth (to train both young githzerai as well as promising mortal monks), in exchange for information and/or introductions to "psionic dragons". The reasons for the Order's interest in these dragons, if true, are fairly obvious.

```
name = 'Githzerai'
description = "***Race: Githzerai.*** Githzerai were elves captured by mind flayers. Tortured and experimented on by the illithids, the githzerai later rebelled and won their freedom. These tall, gaunt folk have potent psionic powers and dwell, for the most part, on the Astral Plane."
type = 'humanoid'
```

## Githzerai
* **Ability Score Increase**. Your Intelligence score increases by 1 and your Wisdom score increases by 2.

* **Age**. Gith reach adulthood in their late teens and live for about a century.

* **Size**. Gith are taller and leaner than humans, with most a slender 6 feet in height. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Languages**. You can speak, read, and write Common and Gith.

* **Alignment**. Githzerai tend toward lawful neutral. Their rigorous training in psychic abilities requires an implacable mental discipline.

* **Mental Discipline**. You have advantage on saving throws against the charmed and frightened conditions.

* **Githzerai Psionics**. You know the [mage hand](../Magic/Spells/mage-hand.md) cantrip, and the hand is invisible when you cast the cantrip with this trait.

  When you reach 3rd level, you can cast the [shield](../Magic/Spells/shield.md) spell once with this trait, and you regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast the [detect thoughts](../Magic/Spells/detect-thoughts.md) spell once with this trait, and you regain the ability to do so when you finish a long rest.

  Wisdom is your spellcasting ability for these spells. When you cast them with this trait, they don't require components.

```
def level0(npc):
    npc.WIS += 2
    npc.INT += 1
    
    npc.speed['walking'] = 30

    npc.languages.append('Common')
    npc.languages.append('Gith')

    npc.traits.append("***Mental Discipline.*** You have advantage on saving throws against the charmed and frightened conditions.")
    npc.newspellcasting('Githzerai', 'WIS').cantripsknown.append('mage hand')

def level3(npc):
    npc.spellcasting['Githzerai'].spells[1].append("shield")
    npc.spellcasting['Githzerai'].slots = [ 1 ]

def level5(npc):
    npc.spellcasting['Githzerai'].spells[2].append("detect thoughts")
    npc.spellcasting['Githzerai'].slots = [ 1,1 ]
```
