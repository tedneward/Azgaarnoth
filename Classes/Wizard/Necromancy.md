# Arcane Tradition: School of Necromancy
Necromancers explore the cosmic forces of life, death, and undeath. As you focus your studies in this tradition, you learn to manipulate the energy that animates all living things. As you progress, you learn to sap the life force from a creature as your magic destroys its body, transforming that vital energy into magical power you can manipulate.

Most people see necromancers as menacing, or even villainous, due to the close association with death. Not all necromancers are evil, but the forces they manipulate are considered taboo by many societies.

Necromancers are rumored to be highly concentrated in [Dradehalia](../../Nations/Dradehalia.md), but a fair number are also members of several [mage schools](../../Organizations/MageSchools/index.md).

```
name = 'Necromancy'
description = "***Arcane Tradition: School of Necromancy.*** Necromancers explore the cosmic forces of life, death, and undeath. As you focus your studies in this tradition, you learn to manipulate the energy that animates all living things. As you progress, you learn to sap the life force from a creature as your magic destroys its body, transforming that vital energy into magical power you can manipulate."
```

## Necromancy Savant
*2nd-level Necromancy feature*

The gold and time you must spend to copy a Necromancy spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Necromancy Savant.*** The gold and time you must spend to copy a Necromancy spell into your spellbook is halved.")
```

## Grim Harvest
*2nd-level Necromancy feature*

You gain the ability to reap life energy from creatures you kill with your spells. Once per turn when you kill one or more creatures with a spell of 1st level or higher, you regain hit points equal to twice the spell's level, or three times its level if the spell belongs to the School of Necromancy. You don't gain this benefit for killing constructs or undead.

```
    npc.traits.append("***Grim Harvest.*** Once per turn when you kill one or more creatures with a spell of 1st level or higher, you regain hit points equal to twice the spell's level, or three times its level if the spell belongs to the School of Necromancy. You don't gain this benefit for killing constructs or undead.")
```

## Undead Thralls
*6th-level Necromancy feature*

You add the [animate dead](../../Magic/Spells/animate-dead.md) spell to your spellbook if it is not there already. When you cast [animate dead](../../Magic/Spells/animate-dead.md), you can target one additional corpse or pile of bones, creating another zombie or skeleton, as appropriate.

Whenever you create an undead using a necromancy spell, it has additional benefits:

* The creature's hit point maximum is increased by an amount equal to your wizard level.

* The creature adds your proficiency bonus to its weapon damage rolls.

```
def level6(npc):
    npc.spellcasting['Wizard'].spellbook.append('animate dead')
    npc.defer(lambda npc: npc.traits.append(f"***Undead Thralls.*** When you cast {spelllinkify('animate dead')}, you can target one additional corpse or pile of bones, creating another zombie or skeleton, as appropriate. Additionally, henever you create an undead using a necromancy spell, it has additional benefits: The creature's hit point maximum is increased by {npc.levels('Wizard')} and it adds {npc.proficiencybonus()} to its weapon damage rolls.") )
```

## Inured to Undeath
*10th-level Necromancy feature*

You have resistance to necrotic damage, and your hit point maximum can't be reduced. You have spent so much time dealing with undead and the forces that animate them that you have become inured to some of their worst effects.

```
def level10(npc):
    npc.damageresistances.append('necrotic')
    npc.traits.append("***Inured to Undeath.*** Your hit point maximum can't be reduced by necrotic affects.")
```

## Command Undead
*14th-level Necromancy feature*

You can use magic to bring undead under your control, even those created by other wizards. As an action, you can choose one undead that you can see within 60 feet of you. That creature must make a Charisma saving throw against your wizard spell save DC. If it succeeds, you can't use this feature on it again. If it fails, it becomes friendly to you and obeys your commands until you use this feature again.

Intelligent undead are harder to control in this way. If the target has an Intelligence of 8 or higher, it has advantage on the saving throw. If it fails the saving throw and has an Intelligence of 12 or higher, it can repeat the saving throw at the end of every hour until it succeeds and breaks free.

```
def level14(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Command Undead.*** Choose one undead that you can see within 60 feet of you. That creature must make a Charisma saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}). If it succeeds, you can't use this feature on it again. If it fails, it becomes friendly to you and obeys your commands until you use this feature again. Intelligent undead are harder to control in this way. If the target has an Intelligence of 8 or higher, it has advantage on the saving throw. If it fails the saving throw and has an Intelligence of 12 or higher, it can repeat the saving throw at the end of every hour until it succeeds and breaks free.") )
```
