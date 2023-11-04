## Fury of the Frost Giant
*Prerequisite: 4th Level, [Strike of the Giants (Frost Giant) Feat](#strike-of-the-giants)*

You've manifested the icy might emblematic of frost giants, granting you the following benefits:

* **Ability Score Increase.** Increase your Strength, Constitution, or Wisdom score by 1, to a maximum of 20.
* **Born of Ice.** You have resistance to cold damage.
* **Frigid Retaliation.** Immediately after a creature you can see within 30 feet of you hits you with an attack roll and deals damage, you can use your reaction to retaliate with a conjured blast of ice. The creature must make a Constitution saving throw (DC equals 8 + your proficiency bonus + the modifier of the ability increased by this feat). On a failed save, it takes 1d8 + your proficiency bonus cold damage, and its speed is halved until the end of its next turn. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Fury of the Frost Giant'
description = "***Feat: Fury of the Frost Giant.*** You've manifested the icy might emblematic of frost giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    ability = chooseability(npc, ['STR', 'CON', 'WIS'])

    npc.damageresistances.append('cold')

    npc.defer(lambda npc: npc.reactions.append(f"***Frigid Retaliation ({npc.proficiencybonus()}/Recharges on long rest).*** Immediately after a creature you can see within 30 feet of you hits you with an attack roll and deals damage, you can retaliate with a conjured blast of ice. The creature must make a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(ability)}). On a failed save, a creature takes 1d8 + {npc.proficiencybonus()} cold damage, and its speed is halved until the end of its next turn.") )
```

