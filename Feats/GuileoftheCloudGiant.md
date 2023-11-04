## Guile of the Cloud Giant
*Prerequisite: 4th Level, [Strike of the Giants (Cloud Giant) Feat](#strike-of-the-giants)*

You've manifested the airy speech and magic emblematic of cloud giants, granting you the following benefits:

* **Ability Score Increase.** Increase your Dexterity, Constitution, or Charisma score by 1, to a maximum of 20.
* **Cloudy Escape.** When a creature you can see hits you with an attack roll, you can use your reaction to give yourself resistance to that attack's damage. You then teleport to an unoccupied space that you can see within 30 feet of yourself. You can use this reaction a number of times equal to half your proficiency bonus (rounded up), and you regain all expended uses when you finish a long rest.

```
name = 'Guile of the Cloud Giant'
description = "***Feat: Guile of the Cloud Giant.*** You've manifested the airy speech and magic emblematic of cloud giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    ability = chooseability(npc, ['DEX', 'CON', 'CHA'])

    npc.defer(lambda npc: npc.reactions.append(f"***Cloudy Escape ({(npc.proficiencybonus() // 2) + 1}/Recharges on long rest).*** When a creature you can see hits you with an attack roll, you give yourself resistance to that attack's damage. You then teleport to an unoccupied space that you can see within 30 feet of yourself.") )
```

