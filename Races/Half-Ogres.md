# Half-Ogres
Few [half-ogres](../Creatures/Ogres.md#half-ogre) have a happy origin story, though there are those tales of the smooth-talking swashbuckler and the female ogre that loved him. More commonly, ogres find mates among orcs (whose offspring are called ogrillons), particularly among the Hordes; when the ogrillon cannot find a home among either the orc tribe or among ogres, the ogrillon often journeys out into the world to find its desinty.

```
name = 'Half-Ogre'
description = "***Race: Half-Ogre.*** "
type = 'humanoid'
```

* **Ability Score Increase.** Your Strength score increases by 4, your Constitution score increases by 1, and your Intelligence decreases by 2.

* **Age.** Half-ogres mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years.

* **Alignment.** Half-ogres inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-ogres raised among ogres and willing to live out their lives among them are usually evil.

* **Size.** Half-oogres are larger and bulkier than humans, and they range from 6 to well over 8 feet tall. Your size is Large.

* **Speed.** Your base walking speed is 30 feet.

* **Darkvision.** Thanks to your ogre blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Menacing.** You gain proficiency in the Intimidation skill.

* **Languages.** You can speak, read, and write Common and Orc. Orc is a harsh, grating language with hard consonants. It has no script of its own but is written in the Dwarvish script.

```
def level0(npc):
    npc.STR += 4
    npc.CON += 1
    npc.INT -= 2

    npc.size = 'Large'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 30

    npc.skills.append('Intimidation')

    npc.languages.append('Common')
    npc.languages.append('Orcish')
```
