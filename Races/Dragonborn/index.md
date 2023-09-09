# Dragonborn
*see [Dragonborn](../Creatures/Dragonborn.md) for more details*

```
name = 'Dragonborn'
description = "***Race: Dragonborn.*** "
type = 'humanoid'
```

* **Ability Score increase**. Your Strength score increases by 2, and your Charisma score increases by 1.

* **Age**. Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.

* **Alignment**. Dragonborn tend towards extremes, making a conscious choice for one side or the other between Good and Evil (represented by Bahamut and Tiamat, respectively). More side with Bahamut than Tiamat (whose non-dragon followers are mostly kobolds), but villainous dragonborn can be quite terrible indeed. However, some dragonborn seek to distance themselves from their draconic heritage, and eschew the worship of either the Platinum or Chromatic Dragon, and instead prefer to dedicate themselves to another of the gods; in fact, many dragonborn find the all-encompassing [Kaevar](../Religions/KaevarianChurch.md) to be most comfortable.

* **Size**. Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Languages**. You can read, speak, and write Common and Draconic.

```
def level0(npc):
    npc.STR += 2
    npc.CHA += 1
    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.languages.append('Common')
    npc.languages.append('Draconic')
```

## Draconic Ancestry
You are distantly related to a particular kind of dragon. Choose a type of dragon; this determines a variety of characteristics about your abilities.

Dragonborn of chromatic colors are often chaotic, prone to violence, and sometimes selfish.

* [Black](Black.md)
* [Blue](Blue.md)
* [Brown](Brown.md)
* [Gray](Gray.md)
* [Green](Green.md)
* [Red](Red.md)
* [White](White.md)

Dragonborn of gemstone colors are often quiet, contemplative, and aloof.



Dragonborn of metallic colors are often law-abiding, slow to anger, and sometimes so noble you want to punch them in their perfect teeth.

* [Bronze](Bronze.md)
* [Brass](Brass.md)
* [Copper](Copper.md)
* [Gold](Gold.md)
* [Silver](Silver.md)
* [Steel](Steel.md)
