# Arcane Tradition: School of Abjuration
The School of Abjuration emphasizes magic that blocks, banishes, or protects. Detractors of this school say that its tradition is about denial, negation rather than positive assertion. You understand, however, that ending harmful effects, protecting the weak, and banishing evil influences is anything but a philosophical void. It is a proud and respected vocation.

Called abjurers, members of this school are sought when baleful spirits require exorcism, when important locations must be guarded against magical spying, and when portals to other planes of existence must be closed.

Abjurers are found fairly equally among all the [Mage Schools](../../Organizations/MageSchools/index.md) (particularly since every school can use with a reinforced room in which to practice dangerous spells!), but more of them gather within the halls of the [High Tower](../../Organizations/MageSchools/HighTower.md) than any other. Many of them also find their way into [mercenary companies](../../Organizations/MercCompanies/index.md) as bodyguards and/or "unit shields" against violent magic. Still others are attached to royal courts and [noble houses](../../Organizations/Houses/index.md), providing safety and privacy when nobility needs (or desires) it.

```
name = 'Abjuration'
description = "***Arcane Tradition: School of Abjuration.*** The School of Abjuration emphasizes magic that blocks, banishes, or protects. Detractors of this school say that its tradition is about denial, negation rather than positive assertion. You understand, however, that ending harmful effects, protecting the weak, and banishing evil influences is anything but a philosophical void. It is a proud and respected vocation. Called abjurers, members of this school are sought when baleful spirits require exorcism, when important locations must be guarded against magical spying, and when portals to other planes of existence must be closed."
```

## Abjuration Savant
*2nd-level School of Abjuration feature*

The gold and time you must spend to copy a abjuration spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Abjuration Savant.*** The gold and time you must spend to copy a abjuration spell into your spellbook is halved.")
```

## Arcane Ward
*2nd-level School of Abjuration feature*

You can weave magic around yourself for protection. When you cast an abjuration spell of 1st level or higher, you can simultaneously use a strand of the spell's magic to create a magical ward on yourself that lasts until you finish a long rest. The ward has hit points equal to twice your wizard level + your Intelligence modifier. Whenever you take damage, the ward takes the damage instead. If this damage reduces the ward to 0 hit points, you take any remaining damage.

While the ward has 0 hit points, it can't absorb damage, but its magic remains. Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.

Once you create the ward, you can't create it again until you finish a long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Arcane Ward (Recharges on long rest).*** When you cast an abjuration spell of 1st level or higher, you can simultaneously use a strand of the spell's magic to create a magical ward on yourself that lasts until you finish a long rest. The ward has {npc.INTbonus() + (npc.levels('Wizard') * 2)} hit points. Whenever you take damage, the ward takes the damage instead. If this damage reduces the ward to 0 hit points, you take any remaining damage. While the ward has 0 hit points, it can't absorb damage, but its magic remains. Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell.") )
```

## Projected Ward
*6th-level School of Abjuration feature*

When a creature that you can see within 30 feet of you takes damage, you can use your reaction to cause your Arcane Ward to absorb that damage. If this damage reduces the ward to 0 hit points, the warded creature takes any remaining damage.

```
def level6(npc):
    npc.reactions.append("***Projected Ward.*** When a creature that you can see within 30 feet of you takes damage, you cause your Arcane Ward to absorb that damage. If this damage reduces the ward to 0 hit points, the warded creature takes any remaining damage.")
```

## Improved Abjuration
*10th-level School of Abjuration feature*

When you cast an abjuration spell that requires you to make an ability check as a part of casting that spell (as in [counterspell](../../Magic/Spells/counterspell.md) and [dispel magic](../../Magic/Spells/dispel-magic.md)), you add your proficiency bonus to that ability check.

```
def level10(npc):
    npc.traits.append(f"***Improved Abjuration.*** When you cast an abjuration spell that requires you to make an ability check as a part of casting that spell (as in {spelllinkify('counterspell')} and {spelllinkify('dispel magic')}), you add your proficiency bonus to that ability check.")
```

## Spell Resistance
*14th-level School of Abjuration feature*

You have advantage on saving throws against spells.

Furthermore, you have resistance against the damage of spells.

```
def level14(npc):
    npc.traits.append("***Spell Resistance.*** You have advantage on saving throws against spells. Furthermore, you have resistance against the damage of spells.")
```
