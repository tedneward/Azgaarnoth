# Velobarn

In an ancient legend, an entire town was slaughtered (by either the Eldar or the Hordes, the legends aren't clear on who the perpetrator of the crime was), only to be returned back to "life" as undead. While the original town inhabitants were eventually all returned to the peace of death, the act opened up a strange pathway, such that periodically someone is born with a strange genetic legacy, that of the undead. Regardless of their original race, once these traits manifest, they are known as Velobarn.

At some point in their life, typically at the age when one of their original race reaches maturity, the undead nature of their legacy becomes more apparent and they manifest the physical attributes and signs of being velobarn. Many communities reject velobarn, exiling them to a life of lonely wandering. Some velobarn discover others of their kind, and gather in communities, often in places where other humanoids struggle to survive.

***Ability Score Increase***. Yuo can increase one ability by 2 and another by 1.

***Age.*** You are essentially immortal, frozen in the age you were when your velobarn traits manifested.

***Alignment.*** Your people vary widely in alignment, tending towards lawful. The Accursed and the Blessed tends toward good, while the Burning and the Vengeful towards evil. The Dulled are typically true neutral.

***Size.*** Your size is Medium (though Small-sized velobarn are not unhead of).

***Speed.*** You move more slowly than other humanoids. You have a base walking speed of 25 feet.

***Languages.*** You can read, write, and speak Common.

## Traits

***Undead Nature.*** You count as both undead and humanoid. In addition, you have no need for food or drink, and you need not sleep. You must, however, still rest for at least four hours per day, or your form begins to break down in a manner similar to that of exhaustion.

***Decaying Body.*** Your body is always partialy decaying, giving you resistance to necrotic damage. In addition, you can will yourself to reverse this powerful decay. As an action, you can expend any number of hit dice and roll them, gaining temporary hit points equal to the total.

```
name = 'Velobarn'
description = "***Race: Velobarn.*** "
type = 'humanoid/undead'
def level0(npc):
    npc.size = choose("Choose your size: ", ['Small', 'Medium'])

    npc.speed['walking'] = 25

    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    ability = choose("Choose an ability to improve by 2: ", abilities)
    if ability == 'STR': npc.STR += 2
    elif ability == 'DEX': npc.DEX += 2
    elif ability == 'CON': npc.CON += 2
    elif ability == 'INT': npc.INT += 2
    elif ability == 'WIS': npc.WIS += 2
    elif ability == 'CHA': npc.CHA += 2

    ability = choose("Choose an ability to improve by 1: ", abilities)
    if ability == 'STR': npc.STR += 1
    elif ability == 'DEX': npc.DEX += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    elif ability == 'CHA': npc.CHA += 1

    npc.languages.append('Common')

    npc.traits.append("***Undead Nature.*** You have no need for food or drink, and you need not sleep. You must, however, still rest for at least four hours per day, or your form begins to break down in a manner similar to that of exhaustion.")

    npc.damageresistances.append("necrotic")

    npc.actions.append("***Decaying Body (Recharges on short rest).*** You can expend any number of hit dice and roll them, gaining temporary hit points equal to the total.")
```

## Velobarn Histories

Velobarn each have a history to their state, classified as subraces:

* [The Accursed]()
* [The Blessed]()
* [The Burning]()
* [The Dulled]()
* [The Escaped]()
* [The Plagued]()
* 