## Adept of the Mage School
*Prerequisite: 4th Level, [Arcanist feat](Arcanist.md), member of [a mage school](../Organizations/MageSchools/index.md)*

Your ambition and loyalty to the school has been recognized, granting you these benefits:

* **Heightened Magic.** You learn one 2nd-level spell of your choice. The 2nd-level spell must be from the spells available to your school. You can cast this feat's 2nd-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast this spell using spell slots you have of the appropriate level.

* If the school itself doesn't specify an ability for its Adepts, then choose one of the following:

    * **Life Channel.** You can channel your lifeforce into the power of your magic. When a creature you can see within 60 feet of you fails on a saving throw against a spell you cast, you can expend a number of Hit Dice equal to the level of the spell. Roll a number of Hit Dice equal to half the number of Hit Dice expended (rounded up) and the damage the triggering creature takes increases by an amount equal to the total rolled of those dice.
    * **Magical Balance.** When you make an attack roll, an ability check, or a saving throw, and roll a 9 or lower on the d20, you can use your reaction to balance fate and treat the roll as a 10. You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.
    * **Protective Ward.** When you or a creature you can see within 30 feet of you takes damage, you can use your reaction to expend a spell slot and weave protective magic around the target. Roll a number of d4s equal to the level of the spell slot expended and reduce the damage the target takes by the total rolled on those dice + your spellcasting ability modifier.

```
name = 'Adept of the Mage School'
description = "***Feat: Adept of the Mage School.*** Your ambition and loyalty to the school has been recognized. (Must be a member of a mage school.)"
def prereq(npc):
    if npc.levels() < 4: return False
    if 'Arcanist' not in npc.feats: return False
    return True

def apply(npc):
    npc.traits.append("***Heightened Magic.*** You learn one 2nd-level spell of your choice. The 2nd-level spell must be from the spells available to your school. You can cast this feat's 2nd-level spell without a spell slot, and you must finish a long rest before you can cast it in this way again. You can also cast this spell using spell slots you have of the appropriate level.")
    npc.traits.append("***Mage School Ability.*** CHOOSE: Life Channel (You can channel your lifeforce into the power of your magic. When a creature you can see within 60 feet of you fails on a saving throw against a spell you cast, you can expend a number of Hit Dice equal to the level of the spell. Roll a number of Hit Dice equal to half the number of Hit Dice expended (rounded up) and the damage the triggering creature takes increases by an amount equal to the total rolled of those dice.), Magical Balance(When you make an attack roll, an ability check, or a saving throw, and roll a 9 or lower on the d20, you can use your reaction to balance fate and treat the roll as a 10. You can use this reaction a number of times equal to your), or Protective Ward (When you or a creature you can see within 30 feet of you takes damage, you can use your reaction to expend a spell slot and weave protective magic around the target. Roll a number of d4s equal to the level of the spell slot expended and reduce the damage the target takes by the total rolled on those dice + your spellcasting ability modifier.), or use one from the mage school.")
```
