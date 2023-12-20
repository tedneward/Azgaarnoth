# Bardic College: College of Valor
Bards of the College of Valor are daring skalds whose tales keep alive the memory of the great heroes of the past, and thereby inspire a new generation of heroes. These bards gather in mead halls or around great bonfires to sing the deeds of the mighty, both past and present. They travel the land to witness great events firsthand and to ensure that the memory of those events doesn't pass from the world. With their songs, they inspire others to reach the same heights of accomplishment as the heroes of old.

```
name = 'College of Valor'
description = "***Bardic College: College of Valor.*** Bards of the College of Valor are daring skalds whose tales keep alive the memory of the great heroes of the past, and thereby inspire a new generation of heroes. These bards gather in mead halls or around great bonfires to sing the deeds of the mighty, both past and present. They travel the land to witness great events firsthand and to ensure that the memory of those events doesn't pass from the world. With their songs, they inspire others to reach the same heights of accomplishment as the heroes of old."
```

The College of Valor is one of the most-restrictive of the Bardic Colleges, and its most famous instance is found in [Flakew](../../Cities/Flakew.md) operated by the [Lirian Imperial Court](../../Nations/Liria.md). They are frequently charged with wandering the countryside and inspiring the people to press onwards in Liria's struggles to recover from the blows she has suffered since the [Fall of the Eldar](../../History/Ancient.md). Many of the other nations, including [Dradehalia](../../Nations/Dradehalia.md) have followed suit, and as such bards of this college but opposing nations have frequently gotten into "battles of the bards" in roadside taverns as each tries to out-inspire the other(s).

## Bonus Proficiencies
*3rd-level College of Valor feature*

You gain proficiency with medium armor, shields, and martial weapons.

```
def level3(npc):
    for arm in armor['medium'] | armor['shields']:
        npc.proficiencies.append(arm)
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
```

## Combat Inspiration
*3rd-level College of Valor feature*

You learn to inspire others in battle. A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses.

```
    npc.traits.append("***Combat Inspiration.*** A creature that has a Bardic Inspiration die from you can roll that die and add the number rolled to a weapon damage roll it just made. Alternatively, when an attack roll is made against the creature, it can use its reaction to roll the Bardic Inspiration die and add the number rolled to its AC against that attack, after seeing the roll but before knowing whether it hits or misses.")
```

## Extra Attack
*6th-level College of Valor feature*

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
def level6(npc):
    npc.actions.append("***Multiattack.*** You can attack twice when you take the Attack action on your turn.")
```

## Battle Magic
*14th-level College of Valor feature*

You have mastered the art of weaving spellcasting and weapon use into a single harmonious act. When you use your action to cast a bard spell, you can make one weapon attack as a bonus action.

```
def level14(npc):
    npc.bonusactions.append("***Battle Magic.*** When you use your action to cast a bard spell, you make one weapon attack.")
```

---

# Custom Bard Spells
The College of Valor has developed many spells for its bards to use.

* 1st: [vertigo palm]()
* 3rd: [deafening boom](), [song of mercy](), [thundering field]()
* 5th: [day sphere]()
* 7th: [far song]()