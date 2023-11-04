# [Goblins](../Creatures/Goblins.md)
Originally a subterranean folk that came to Azgaarnoth as part of the Hordes, goblins can now be found in every corner of Azgaarnoth, often beside their bugbear and hobgoblin kin. Goblins hae thrived in dangerous environments thanks to a special knack for finding the weak spots in foes larger than themselves and for getting out of trouble. Originally the lackeys and servants of their larger goblinoid kin, now many goblins pursue their own destinies, escaping the plots of archfey, gods, and would-be warlords.

* **Ability Score Increase.** Your Dexterity score increases by 2, and your Constitution score increases by 1.

* **Age.** Goblins reach adulthood at age 8 and live up to 60 years.

* **Alignment.** Goblins are typically neutral evil, as they care only for their own needs. A few goblins might tend toward good or neutrality, but only rarely.

* **Size.** Goblins are between 3 and 4 feet tall and weigh between 40 and 80 pounds. Your size is Small.

* **Speed.** Your base walking speed is 30 feet.

* **Darkvision.** You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Fury of the Small.** When you damage a creature with an attack or a spell and the creature's size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your level. You can use this trait a number of times equal to your proficiency bonus, regaining all expended uses when you finish a long rest, and you can use it no more than once per turn.

* **Fey Ancestry.** You have advantage on saving throws you make to avoid or end the charmed condition on yourself.

* **Nimble Escape.** You can take the Disengage or Hide action as a bonus action on each of your turns.

* **Languages.** You can speak, read, and write Common and Goblin.

```
name = 'Goblin'
description = "***Race: Goblin.*** Originally a subterranean folk that came to Azgaarnoth as part of the Hordes, goblins can now be found in every corner of Azgaarnoth, often beside their bugbear and hobgoblin kin. Goblins hae thrived in dangerous environments thanks to a special knack for finding the weak spots in foes larger than themselves and for getting out of trouble. Originally the lackeys and servants of their larger goblinoid kin, now many goblins pursue their own destinies, escaping the plots of archfey, gods, and would-be warlords."
type = 'humanoid'
def level0(npc):
    npc.DEX += 2
    npc.CON += 1

    npc.size = 'Small'

    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.traits.append(traits['fey-ancestry'])
    
    npc.defer(lambda npc: npc.traits.append(f"***Fury of the Small ({npc.proficiencybonus()}/Recharges on long rest).*** When you damage a creature with an attack or a spell and the creature's size is larger than yours, you can cause the attack or spell to deal {npc.levels()} extra damage to the creature. You can use this trait no more than once per turn."))

    npc.bonusactions.append("***Nimble Escape.*** You can take the Disengage or Hide action as a bonus action on each of your turns.")

    npc.languages.append("Common")
    npc.languages.append("Goblin")
```

