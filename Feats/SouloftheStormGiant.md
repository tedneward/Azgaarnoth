## Soul of the Storm Giant
*Prerequisite: 4th Level, [Strike of the Giants (Storm Giant) Feat](#strike-of-the-giants)*

You've manifested divination abilities and tempest magic emblematic of storm giants, granting you the following benefits:

* **Ability Score Increase.** Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.
* **Maelstrom Aura.** As a bonus action, you surround yourself in an aura of magical wind and lightning that extends 10 feet from you in every direction but not through total cover. The aura lasts until the start of your next turn or until you are incapacitated. While the aura is active, attack rolls against you have disadvantage, and whenever a creature starts its turn within the aura, you can force the creature to make a Strength saving throw (DC equals 8 + your proficiency bonus + the ability modifier of the score increased by this feat). On a failed save, the creature's speed is halved until the start of its next turn. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Soul of the Storm Giant'
description = "***Feat: Soul of the Storm Giant.*** You've manifested divination abilities and tempest magic emblematic of storm giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    ability = chooseability(npc, ['INT', 'WIS', 'CHA'])

    npc.defer(lambda npc: npc.bonusactions.append(f"***Maelstrom Aura ({npc.proficiencybonus()}/Recharges on long rest).*** You surround yourself in an aura of magical wind and lightning that extends 10 feet from you in every direction but not through total cover. The aura lasts until the start of your next turn or until you are incapacitated. While the aura is active, attack rolls against you have disadvantage, and whenever a creature starts its turn within the aura, you can force the creature to make a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(ability)}). On a failed save, the creature's speed is halved until the start of its next turn.") )
```

