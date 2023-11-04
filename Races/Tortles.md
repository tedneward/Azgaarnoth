# [Tortles](../Creatures/Tortles.md)
Tortles have a saying: "We wear our homes on our backs." These turtle folk live on many worlds, most often journeying up and down coasts, along waterways, and across the sea. Tortles don't have a unified story of how they were created, but they all have a sense of being mystically connected to the natural world. Carrying their shelter on their backs gives tortles a special feeling of security wherever they go, for even if they visit a far, unknown country, they have a place to lay their heads.

Tortles exhibit the same range of coloration and patterns found among turtles, and many tortles enjoy adorning their shells in distinctive ways.

* **Ability Score Increase**. Your Strength score increases by 2, and your Wisdom score increases by 1.

* **Age**. Young tortles crawl for a few weeks after birth before learning to walk on two legs. They reach adulthood by the age of 15 and live an average of 50 years.

* **Alignment**. Tortles tend to lead orderly, ritualistic lives. They develop customs and routines, becoming more set in their ways as they age. Most are lawful good. A few can be selfish and greedy, tending more toward evil, but it's unusual for a tortle to shuck off order in favor of chaos.

* **Size**. Tortle adults stand 5 to 6 feet tall and average 450 pounds. THeir shells account for roughly one-third of their weight. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Claws**. Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

* **Hold Breath**. You can hold your breath for up to 1 hour at a time. Tortles aren't natural swimmers, but they can remain underwater for some time before needing to come up for air.

* **Natural Armor**. Due to your shell and the shape of your body, you are ill-suited to wearing armor. Your shell provides ample protection, however; it gives you a base AC of 17 (your Dexterity modifier doesn't affect this number). You gain no benefit from wearing armor, but if you are using a shield, you can apply the shield's bonus as normal.

* **Shell Defense**. You can withdraw into your shell as an action. Until you emerge, you gain a +4 bonus to AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can't increase, you have disadvantage on Dexterity saving throws, you can't take reactions, and the only action you can take is a bonus action to emerge from your shell.

* **Survival Instinct**. You gain proficiency in the Survival skill. Tortles have finely honed survival instincts.

* **Languages**. You can speak, read, and write Common and Aquan.

```
name = 'Tortle'
description = "***Race: Tortle.*** Tortles have a saying: \"We wear our homes on our backs.\" These turtle folk live on many worlds, most often journeying up and down coasts, along waterways, and across the sea. Tortles don't have a unified story of how they were created, but they all have a sense of being mystically connected to the natural world. Carrying their shelter on their backs gives tortles a special feeling of security wherever they go, for even if they visit a far, unknown country, they have a place to lay their heads. Tortles exhibit the same range of coloration and patterns found among turtles, and many tortles enjoy adorning their shells in distinctive ways."
type = 'humanoid'
def level0(npc):
    npc.STR += 2
    npc.WIS += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.defer(lambda npc: npc.actions.append("***Claws.*** *Melee Weapon Attack*: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft, one target. Hit: 1d6 + {npc.STRbonus()} slashing damage.") )

    npc.traits.append("***Hold Breath.*** You can hold your breath for up to 1 hour at a time. Tortles aren't natural swimmers, but they can remain underwater for some time before needing to come up for air.")

    npc.armorclass['natural armor'] = 17

    npc.actions.append("***Shell Defense.*** You can withdraw into your shell. Until you emerge, you gain a +4 bonus to AC, and you have advantage on Strength and Constitution saving throws. While in your shell, you are prone, your speed is 0 and can't increase, you have disadvantage on Dexterity saving throws, you can't take reactions, and the only action you can take is a bonus action to emerge from your shell.")

    npc.skills.append('Survival')

    npc.languages.append('Common')
    npc.languages.append('Aquan')
```
