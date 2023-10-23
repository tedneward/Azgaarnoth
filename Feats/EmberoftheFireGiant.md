## Ember of the Fire Giant
*Prerequisite: 4th Level, Strike of the Giants (Fire Giant) Feat*

You've manifested the fiery combat emblematic of fire giants, granting you the following benefits:

* **Ability Score Increase**. Increase your Strength, Constitution, or Wisdom score by 1, to a maximum of 20.
* **Born of Flame**. You have resistance to fire damage.
* **Searing Ignition**. When you take the Attack action on your turn, you can replace a single attack with a magical burst of flame. Each creature of your choice within 15 feet of you that can see you must make a Dexterity saving throw (DC equals 8 + your proficiency bonus + the modifier of the ability increased by this feat). On a failed save, a creature takes fire damage equal to 1d8 + your proficiency bonus, and it is blinded until the start of your next turn. On a successful save, the creature takes half as much damage and isn't blinded. You can use your Searing Ignition a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Ember of the Fire Giant'
description = "***Feat: Ember of the Fire Giant.*** You've manifested the fiery combat emblematic of fire giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    ability = chooseability(npc, ['STR', 'CON', 'WIS'])
    npc.damageresistances.append('fire')
    npc.defer(lambda npc: npc.actions.append(f"***Attack: Searing Ignition ({npc.proficiencybonus()}/Recharges on long rest).*** When you take the Attack action on your turn, you can replace a single attack with a magical burst of flame. Each creature of your choice within 15 feet of you that can see you must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(ability)}). On a failed save, a creature takes 1d8 + {npc.proficiencybonus()} fire damage, and it is blinded until the start of your next turn. On a successful save, the creature takes half damage and isn't blinded.") )
```
