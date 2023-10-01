# [Lizardfolk](../Creatures/Lizardfolk.md)

```
name = 'Lizardfolk'
description = "***Race: Lizardfolk.*** "
type = 'humanoid'
```

* **Ability Score Increase**. Your Constitution score increase by 2, and your Wisdom score increases by 1.

* **Age**. Lizardfolk reach maturity around age 14 and rarely live longer than 60 years.

* **Alignment**. Most lizardfolk are neutral. They see the world as a place of predators and prey, where life and death are natural processes. They wish only to survive, and prefer to leave other creatures to their own devices.

* **Size**. Lizardfolk are a little bulkier and taller than humans, and their colorful frills make them appear even larger. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet, and you have a swimming speed of 30 feet.

* **Bite**. Your fanged maw is a natural weapon, which you can use to make unarmed strikes. If you hit with it, you deal piercing damage equal to 1d6 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

* **Cunning Artisan**. As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size Small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan's tools, such as leatherworker's tools.

* **Hold Breath**. You can hold your breath for up to 15 minutes at a time.

* **Hunter's Lore**. You gain proficiency with two of the following skills of your choice: Animal Handling, Nature, Perception, Stealth, and Survival.

* **Natural Armor**. You have tough, scaly skin. When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.

* **Hungry Jaws**. In battle, you can throw yourself into a vicious feeding frenzy. As a bonus action, you can make a special attack with your bite. If the attack hits, it deals its normal damage, and you gain temporary hit points (minimum of 1) equal to your Constitution modifier, and you can't use this trait again until you finish a short or long rest.

* **Languages**. You can speak, read, and write Common and Draconic.

```
def level0(npc):
    npc.CON += 2
    npc.WIS += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.speed['swimming'] = 30

    npc.defer(lambda npc: npc.actions.append(f"***Bite.*** Melee Weapon Attack: {npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d6 + {npc.STRbonus()} piercing damage."))

    npc.traits.append("***Cunning Artisan.*** As part of a short rest, you can harvest bone and hide from a slain beast, construct, dragon, monstrosity, or plant creature of size Small or larger to create one of the following items: a shield, a club, a javelin, or 1d4 darts or blowgun needles. To use this trait, you need a blade, such as a dagger, or appropriate artisan's tools, such as leatherworker's tools.")

    npc.traits.append("***Hold Breath.*** You can hold your breath for up to 15 minutes at a time.")

    chooseskill(npc, ['Animal Handling', 'Nature', 'Perception', 'Stealth', 'Survival'])
    chooseskill(npc, ['Animal Handling', 'Nature', 'Perception', 'Stealth', 'Survival'])

    npc.armorclass['natural armor'] = 13

    npc.defer(lambda npc: npc.bonusactions.append(f"***Hungry Jaws (Recharges on short or long rest).*** You can make a special attack with your bite. If the attack hits, it deals its normal damage, and you gain {npc.CONbonus()} temporary hit points."))

    npc.languages.append('Common')
    npc.languages.append('Draconic')
```