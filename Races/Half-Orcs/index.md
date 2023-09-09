# Half-Orcs
When alliances between humans and orcs are sealed by marriages, half-orcs are born. Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals. Some venture into the world to prove their worth among humans and other more civilized races. Many of these become adventurers, achieving greatness for their mighty deeds and notoriety for their barbaric customs and savage fury.

Half-orcs may be [dragonmarked](Dragonmarked.md) with the Mark of Finding; see that entry for more details.

```
name = 'Half-Orc'
description = "***Race: Half-Orc.*** When alliances between humans and orcs are sealed by marriages, half-orcs are born. Some half-orcs rise to become proud chiefs of orc tribes, their human blood giving them an edge over their full-blooded orc rivals. Some venture into the world to prove their worth among humans and other more civilized races. Many of these become adventurers, achieving greatness for their mighty deeds and notoriety for their barbaric customs, savage fury, and impressive cunning."
```

```
def level0(npc0):
```

* **Ability Score Increase**. Your Strength score increases by 2, and your Constitution score increases by 1.

```
    npc.STR += 1
    npc.CON += 1
```

* **Age**. Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years.

* **Alignment**. Half-orcs inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-orcs raised among orcs and willing to live out their lives among them are usually evil.

* **Size**. Half-orcs are somewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed**. Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision**. Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Menacing**. You gain proficiency in the Intimidation skill.

```
    npc.skills.append("Intimidation")
```

* **Relentless Endurance**. When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.

```
    npc.traits.append("***Relentless Endurance (Recharges on long rest.)*** When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead.")
```

* **Savage Attacks**. When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.

```
    npc.traits.append("***Savage Attacks.*** When you score a critical hit with a melee weapon attack, you can roll one of the weapon's damage dice one additional time and add it to the extra damage of the critical hit.")
```

* **Languages**. You can speak, read, and write Common and Orc. Orc is a harsh, grating language with hard consonants. It has no script of its own but is written in the Dwarvish script.

```
    npc.languages.append('Common')
    npc.languages.append('Orcish')
```
