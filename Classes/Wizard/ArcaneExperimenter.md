# Arcane Tradition: Arcane Experimenter
The wizardry disciplines tend towards fastidious structure, dedicated study, and cautious experimentation. The formulas for new spells and magical items can take decades of research and testing before they are proven stable.But there are those who believe to truly learn, to truly understand, requires not only careful analysis but practice; even if that process is considered reckless. The quickest way to test if a spell formula works isn't to pore over it for months or years, assessing its flaws, but to simply try it in a variety of situations and environments, and against a variety of foes.

```
name = 'Arcane Experimenter'
description = "***Arcane Tradition: Arcane Experimenter.*** The wizardry disciplines tend towards fastidious structure, dedicated study, and cautious experimentation. The formulas for new spells and magical items can take decades of research and testing before they are proven stable.But there are those who believe to truly learn, to truly understand, requires not only careful analysis but practice; even if that process is considered reckless. The quickest way to test if a spell formula works isn't to pore over it for months or years, assessing its flaws, but to simply try it in a variety of situations and environments, and against a variety of foes."
```

## Experimenter's Kit
*2nd-level Arcane Experimenter feature*

At 2nd level, you gain proficiency with alchemist's supplies, a fundamental of arcane experimentation.

```
def level2(npc):
    npc.proficiencies.append("Alchemist's supplies")
```

## Arcane Superiority
*2nd-level Arcane Experimenter feature*

You push your magic further than other arcane traditions. What your magic lacks in elegance, it makes up for in power.

You learn arcane maneuvers that are fueled by special dice called superiority dice.

**Maneuvers**. You learn three arcane maneuvers of your choice. Many maneuvers enhance your spellcasting in some way. You can only use one maneuver per spell cast (maximum of 1 per turn).

You learn one additional maneuver of your choice at 6th level, 10th level, and 14th level. Each time you learn a new maneuver, you can choose one of the maneuvers you know and replace it with another maneuver from the list of maneuvers available to you.

**Superiority Dice**. You have four superiority dice, which are d6s. A superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest. You gain another superiority die at 7th level and one more at 15th level.

**Saving Throws**. Some of your arcane maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows:

**Maneuver save DC** = 8 + your proficiency bonus + your Intelligence modifier.

```
    npc.defer(lambda npc: npc.traits.append(f"***Superiority Dice.*** You have {'four' if npc.levels('Wizard') < 7 else 'five' if npc.levels('Wizard') < 15 else 'six'} superiority dice, which are {'d6' if npc.levels('Wizard') < 10 else 'd8' if npc.levels('Wizard') < 18 else 'd10'}s. A superiority die is expended when you use it. **Maneuver Save DC {8 + npc.proficiencybonus() + npc.INTbonus()}**") )

    npc.arcanemaneuvers = []
    choosearcanemaneuver(npc)
    choosearcanemaneuver(npc)
    choosearcanemaneuver(npc)
```

### Arcane Maneuvers
The maneuvers are presented in alphabetical order.

* **Arcane Stability**. If you are required to make a Constitution saving throw to maintain your concentration, as a reaction, you can expend one superiority die and add twice the number rolled on the superiority die to your saving throw. You apply this bonus after you roll the die, but before the outcome is determined.

```
def arcanestability(npc):
    npc.reactions.append("***Arcane Stability.*** When you are required to make a concentration check, you expend a superiority die and add twice the number rolled on the superiority die to your saving throw. You apply this bonus after you roll the die, but before the outcome is determined.")
```

* **Experimental Formula**. When you cast a spell that requires a saving throw, as a reaction, you can expend one superiority die and increase the spell save DC by half the number rolled on the superiority die (rounded down). You apply this bonus before the saving throw is rolled.

```
def experimentalformula(npc):
    npc.reactions.append("***Experimental Formula.*** When you cast a spell that requires a saving throw, you expend one superiority die and increase the spell save DC by half the number rolled on the superiority die (rounded down). You apply this bonus before the saving throw is rolled.")
```

* **Imbued Alacrity**. When you roll initiative, as a reaction, you can expend one superiority die and add the result of the superiority die to your initiative score. In addition, you gain bonus movement for the first round of combat equal to 5 feet x the result of the superiority die roll.

```
def imbuedalacrity(npc):
    npc.reactions.append("***Imbued Alacrity.*** When you roll initiative, you expend one superiority die and add the result of the superiority die to your initiative score. In addition, you gain bonus movement for the first round of combat equal to 5 feet x the result of the superiority die roll.")
```

* **Occult Insight**. When you make an Intelligence check, as a reaction, you can expend one superiority die and add the number rolled on the superiority die to your check. You apply this bonus after you roll the die, but before the outcome is determined.

```
def occultinsight(npc):
    npc.reactions.append("***Occult Insight.*** When you make an Intelligence check, you expend one superiority die and add the number rolled on the superiority die to your check. You apply this bonus after you roll the die, but before the outcome is determined.")
```

* **Power Surge**. When you hit a creature with an attack, or it fails a saving throw against a spell you cast, as a reaction, you can expend one superiority die and deal force damage equal to the result of the superiority die. If the spell affects more than one creature, you choose which creature takes the additional damage. At 11th level this additional damage becomes 2x the amount shown on the superiority die.

```
def powersurge(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Power Surge.*** When you hit a creature with an attack, or it fails a saving throw against a spell you cast, you expend one superiority die and deal force damage equal to {'the' if npc.levels('Wizard') < 11 else 'twice the'} result of the superiority die. If the spell affects more than one creature, you choose which creature takes the additional damage.") )
```

* **Spell Dispersal**. If you are required to make a saving throw against a spell or magical effect, as a reaction, you can expend one superiority die and add the number rolled on the superiority die to your saving throw. You apply this bonus after you roll the die, but before the outcome is determined.

```
def spelldispersal(npc):
    npc.reactions.append("***Spell Dispersal.*** If you are required to make a saving throw against a spell or magical effect, you expend one superiority die and add the number rolled on the superiority die to your saving throw. You apply this bonus after you roll the die, but before the outcome is determined.")
```

* **Weave Ward**. If you are hit by an attack whilst not wearing armor, as a reaction, you can expend one superiority die and add the number rolled to your AC until the end of this turn. If the attack still hits, you take half damage instead. You can apply this bonus after the die is rolled, but before the outcome is determined.

```
def weaveward(npc):
    npc.reactions.append("***Weave Ward.*** If you are hit by an attack whilst not wearing armor, you expend one superiority die and add the number rolled to your AC until the end of this turn. If the attack still hits, you take half damage instead. You can apply this bonus after the die is rolled, but before the outcome is determined.")
```

```
arcanemaneuvers = {
    'Arcane Stability': arcanestability,
    'Experimental Formula': experimentalformula,
    'Imbued Alacrity': imbuedalacrity,
    'Occult Insight': occultinsight,
    'Power Surge': powersurge,
    'Spell Dispersal': spelldispersal,
    'Weave Ward': weaveward
}
def choosearcanemaneuver(npc):
    available = {}
    for amname in arcanemaneuvers:
        if amname not in npc.arcanemaneuvers:
            available[amname] = arcanemaneuvers[amname]
    (name, fn) = choose("Choose an arcane maneuver: ", available)
    npc.arcanemaneuvers.append(name)
    fn(npc)
```

## Prepared Superiority
*6th-level Arcane Experimenter feature*

You gain the following abilities:

* If you roll a 20 on the die when making an Intelligence saving throw or an Intelligence ability check, you regain one superiority die.
* The first time you expand all of your highest level spell slots, you regain a superiority die. You cannot benefit from this ability again until you have completed a long rest.

```
def level6(npc):
    choosearcanemaneuver(npc)
    npc.traits.append("***Prepared Superiority.*** If you roll a 20 on the die when making an Intelligence saving throw or an Intelligence ability check, you regain one superiority die. The first time after a long rest that you expand all of your highest level spell slots, you regain a superiority die, and you cannot benefit from this ability again until you have completed a long rest.")
```

## Improved Superiority
*10th-level Arcane Experimenter feature*

Your superiority die changes when you reach certain levels in this class. The die becomes a d8 at 10th level, and a d10 at 18th level.

```
def level10(npc):
    choosearcanemaneuver(npc)
```

## Relentless
*14th-level Arcane Experimenter feature*

When you roll for initiative and have no superiority dice remaining, you regain 1 superiority die.

```
def level14(npc):
    choosearcanemaneuver(npc)
    npc.traits.append("***Relentless.*** When you roll for initiative and have no superiority dice remaining, you regain 1 superiority die.")
```

---

# Arcane Experimenter Unique Spells
These spells are known generally just to arcane experimenters.

## Cantrips

## 2nd-level
* [lesser charm of second chance](../../Magic/Spells/lesser-charm-of-second-chance.md)

## 3rd-level
* [ablative body ward](../../Magic/Spells/ablative-body-ward.md)

## 4th-level
* [greater charm of second chance](../../Magic/Spells/greater-charm-of-second-chance.md)

## 5th-level
* [prismatic-cloud](../../Magic/Spells/prismatic-cloud.md)
