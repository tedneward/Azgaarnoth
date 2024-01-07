# [Orc](../Creatures/Orcs.md)
Orcs are burly raiders with prominent lower canines that resemble tusks. They gather in tribes, eager to prove their strength against all comers. In the past, that meant looking to satisfy their bloodlust by slaying any humanoids that stood against them; among many of the tribes, however, a more nuanced philosophy--that of facing and overcoming obstacles of all sorts, not just other humanoids--has allowed them to assume a place next to other races in (relative) peace.

```
name = 'Orc'
description = "***Race: Orc.*** Orcs are burly raiders with prominent lower canines that resemble tusks. They gather in tribes, eager to prove their strength against all comers. In the past, that meant looking to satisfy their bloodlust by slaying any humanoids that stood against them; among many of the tribes, however, a more nuanced philosophy--that of facing and overcoming obstacles of all sorts, not just other humanoids--has allowed them to assume a place next to other races in (relative) peace."
type = 'humanoid'
```

* **Ability Score Increase.** Your Strength score increases by 2, your Constitution score increases by 1, and your Intelligence score is reduced by 2.

```
def level0(npc):
    npc.STR += 2
    npc.CON += 1
    npc.INT -= 2
```

* **Age.** Orcs reach adulthood at age 12 and live up to 50 years.

* **Alignment.** Orcs are vicious raiders, who believe that the world should be theirs. They also respect strength above all else and believe the strong must bully the weak to ensure that weakness does not spread like a disease. They are usually chaotic evil.

* **Size.** Orcs are usually over 6 feet tall and weigh between 230 and 280 pounds. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed.** Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision.** You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Aggressive.** As a bonus action, you can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.

```
    npc.bonusactions.append("***Aggressive.*** You can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.")
```

* **Relentless Endurance**. When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest.

```
    npc.traits.append("***Relentless Endurance (Recharges on long rest).*** When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead.")
```

* **Menacing.** You are proficient in the Intimidation skill.

```
    npc.skills.append("Intimidation")
```

* **Powerful Build.** You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.

```
    npc.traits.append("***Powerful Build.*** You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.")
```

* **Languages.** You can speak, read, and write Common and Orc.

```
    npc.languages.append("Common")
    npc.languages.append("Orcish")
```

## Orc Names
