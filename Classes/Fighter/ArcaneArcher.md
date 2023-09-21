# Martial Archetype: Arcane Archer
An Arcane Archer studies a unique elven method of archery that weaves magic into attacks to produce supernatural effects. Among elves, Arcane Archers are some of their most elite warriors. These archers stand watch over the fringes of elven domains, keeping a keen eye out for trespassers and using magic-infused arrows to defeat monsters and invaders before they can reach elven settlements. Over the centuries, the methods of these elf archers have been learned by members of other races who can also balance arcane aptitude with archery.

```
name = 'Arcane Archer'
description = "***Martial Archetype: Arcane Archer.*** An Arcane Archer studies a unique elven method of archery that weaves magic into attacks to produce supernatural effects. Among elves, Arcane Archers are some of their most elite warriors. These archers stand watch over the fringes of elven domains, keeping a keen eye out for trespassers and using magic-infused arrows to defeat monsters and invaders before they can reach elven settlements. Over the centuries, the methods of these elf archers have been learned by members of other races who can also balance arcane aptitude with archery."
```

## Magic Arrow
*3rd-level Arcane Archer feature*

You gain the ability to infuse arrows with magic. Whenever you fire a nonmagical arrow from a shortbow or longbow, you can make it a magic arrow, with a +1 bonus to the attack and damage rolls. The magic fades from the arrow immediately after it hits or misses its target.

```
def level3(npc):
    npc.traits.append("***Magic Arrow.*** Whenever you fire a nonmagical arrow from a shortbow or longbow, you can make it a magic arrow, with a +1 bonus to the attack and damage rolls. The magic fades from the arrow immediately after it hits or misses its target.")
```

## Arcane Shot
*3rd-level Arcane Archer feature*

You learn to unleash special magical effects with some of your shots. When you gain this feature, you learn two Arcane Shot options of your choice (see the "Arcane Shot Options" section below).

Once per turn when you fire a magic arrow from a shortbow or longbow as part of the Attack action, you can apply one of your Arcane Shot options to that arrow. You decide to use the option when the arrow hits, unless the option doesn't involve an attack roll. You have two uses of this ability, and you regain all expended uses of it when you finish a short or long rest. You gain an additional Arcane Shot option of your choice when you reach certain levels in this class: 7th, 10th, 15th, and 18th level. Each option also improves when you become an 18th-level fighter.

```
    npc.defer(lambda npc: npc.traits.append(f"***Arcane Shot ({npc.arcaneshot['uses']}/Recharges on short or long rest).*** Once per turn when you fire a magic arrow from a shortbow or longbow as part of the Attack action, you can apply one of your Arcane Shot options to that arrow. You decide to use the option when the arrow hits, unless the option doesn't involve an attack roll."))
    choosearcaneshot(npc)
    choosearcaneshot(npc)
```

## Arcane Archer's Lore
*3rd-level Arcane Archer feature*

You learn magical theory or some of the secrets of nature--typical for practitioners of this elven martial tradition. You gain proficiency in either the Arcana or the Nature skill.

```
    chooseskill(npc, ['Arcana', 'Nature'])
```

## Curving Shot
*7th-level Arcane Archer feature*

You learn how to direct an errant arrow toward a new target. When you make an attack roll with a magic arrow and miss, you can use a bonus action to reroll the attack roll against a different target within 60 feet of the original target.

```
def level7(npc):
    npc.bonusactions.append("***Curving Shot.*** When you make an attack roll with a magic arrow and miss, you can use a bonus action to reroll the attack roll against a different target within 60 feet of the original target.")
    choosearcaneshot(npc)
    npc.arcaneshot['uses'] = 3

def level10(npc):
    choosearcaneshot(npc)
```

## Ever-Ready Shot
*15th-level Arcane Archer feature*

Your magical archery is ever available to you when you need it most. If you roll initiative and have no uses of Arcane Shot remaining, you regain one use of it.

```
def level15(npc):
    npc.traits.append("***Ever-Ready Shot.*** If you roll initiative and have no uses of Arcane Shot remaining, you regain one use of it.")
    choosearcaneshot(npc)
    npc.arcaneshot['uses'] = 4
```

## Arcane Shot Options
The Arcane Shot feature lets you choose options for it at certain levels. The options are presented here in alphabetical order. They are all magical effects, and each one is associated with one of the schools of magic.

If an option requires a saving throw, your Arcane Shot save DC equals 8 + your proficiency bonus + your Intelligence modifier.

* **Banishing Arrow.** You use abjuration magic to try to temporarily banish your target to a harmless location in the Feywild. If the arrow hits a creature, the target must also succeed on a Charisma saving throw or be banished. While banished in this way, its speed is 0, and it is incapacitated. At the end of its next turn, the target reappears in the space it vacated or in the nearest unoccupied space if that space is occupied.
  After you reach 18th level in this class, a target also takes 2d6 force damage when the arrow hits it.

```
def banishingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Banishing Arrow.*** If the arrow hits a creature, the target takes the usual damage, {'plus 2d6 force damage, ' if npc.levels('Fighter') > 17 else ''}and must also succeed on a Charisma saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or be banished. While banished in this way, its speed is 0, and it is incapacitated. At the end of its next turn, the target reappears in the space it vacated or in the nearest unoccupied space if that space is occupied."))
```

* **Brute Bane Arrow**. You weave necromantic magic into your arrow. If the arrow hits a creature, the target takes an extra 2d6 necrotic damage, and it must make a Constitution saving throw. On a failed save, the damage of the target's attacks is halved until the start of your next turn.
  The necrotic damage increases to 4d6 when you reach 18th level in this class.

```
def brutebanearrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Brute Bane Arrow.*** If the arrow hits a creature, the target takes the usual damage, plus {'2d6' if npc.levels('Fighter') < 18 else '4d6'} necrotic damage, and must also succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}). On a failed save, the damage of the target's attacks is halved until the start of your next turn."))
```

* **Bursting Arrow**. You imbue your arrow with a blast of force energy drawn from the school of evocation. If the arrow hits a creature, the target and each creature within 10 feet of it also take 2d6 force damage each.
  The force damage increases to 4d6 when you reach 18th level in this class.

```
def burstingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Bursting Arrow.*** If the arrow hits a creature, the target takes the usual damage, and it and each creature within 10 feet of it takes {'2d6' if npc.levels('Fighter') < 18 else '4d6'} force damage each."))
```

* **Grasping Arrow**. When this arrow strikes its target, conjuration magic creates grasping, poisonous brambles, which wrap around the target. If the arrow hits a creature, the target takes an extra 2d6 poison damage, its speed is reduced by 10 feet, and it takes 2d6 slashing damage the first time on each turn it moves 1 foot or more without teleporting. The target or any creature that can reach it can use its action to remove the brambles with a successful Strength (Athletics) check against your Arcane Shot save DC. Otherwise, the brambles last for 1 minute or until you use this option again.
  The poison and slashing damage both increase to 4d6 when you reach 18th level in this class.

```
def graspingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Grasping Arrow.*** When this arrow strikes its target, conjuration magic creates grasping, poisonous brambles, which wrap around the target. If the arrow hits a creature, the target takes an extra {'2d6' if npc.levels('Fighter') < 18 else '4d6'} poison damage, its speed is reduced by 10 feet, and it takes {'2d6' if npc.levels('Fighter') < 18 else '4d6'} slashing damage the first time on each turn it moves 1 foot or more without teleporting. The target or any creature that can reach it can use its action to remove the brambles with a successful Strength (Athletics) check (DC {8 + npc.proficiencybonus() + npc.INTbonus()}). Otherwise, the brambles last for 1 minute or until you use this option again."))
```

* **Mind-Scrambling Arrow**. Your enchantment magic causes this arrow to temporarily beguile its target. Choose one of your allies within 30 feet of the target. If the arrow hits a creature, the target takes an extra 2d6 psychic damage, and it must succeed on a Wisdom saving throw or it can't attack the chosen ally or include that ally in a harmful area of effect until the start of your next turn. This effect ends early if the chosen ally deals any damage to the target.
  The psychic damage increases to 4d6 when you reach 18th level in this class.

```
def mindscramblingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Mind-Scrambling Arrow.*** Choose one of your allies within 30 feet of the target. If the arrow hits a creature, the target takes an extra {'2d6' if npc.levels('Fighter') < 18 else '4d6'} psychic damage, and it must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or it can't attack the chosen ally or include that ally in a harmful area of effect until the start of your next turn. This effect ends early if the chosen ally deals any damage to the target."))
```

* **Piercing Arrow**. You use transmutation magic to give your arrow an ethereal quality. When you use this option, you don't make an attack roll for the attack. Instead, the arrow fires forward in a line that is 1 foot wide and 30 feet long, before disappearing. The arrow passes harmlessly through objects, ignoring cover. Each creature in that line must make a Dexterity saving throw. On a failed save, a target takes damage as if it were hit by the arrow, plus an extra 1d6 piercing damage. On a successful save, a target takes half as much damage.
  The piercing damage increases to 2d6 when you reach 18th level in this class.

```
def piercingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Piercing Arrow.*** When you use this option, you don't make an attack roll for the attack. Instead, the arrow fires forward in a line that is 1 foot wide and 30 feet long, before disappearing. The arrow passes harmlessly through objects, ignoring cover. Each creature in that line must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}). On a failed save, a target takes damage as if it were hit by the arrow, plus an extra {'1d6' if npc.levels('Fighter') < 18 else '2d6'} piercing damage. On a successful save, a target takes half as much damage."))
```

* **Seeking Arrow**. Using divination magic, you grant your arrow the ability to seek out your target, allowing the arrow to curve and twist its path in search of its prey. When you use this option, you don't make an attack roll for the attack. Instead, choose one creature you have seen in the past minute. The arrow flies toward that creature, moving around corners if necessary and ignoring three-quarters cover and half cover. If the target is within the weapon's range and there is a path large enough for the arrow to travel to the target, the target must make a Dexterity saving throw. On a failed save, it takes damage as if it were hit by the arrow, plus an extra 1d6 force damage, and you learn the target's current location. On a successful save, the target takes half as much damage, and you don't learn its location.
  The force damage increases to 2d6 when you reach 18th level in this class.

```
def seekingarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Seeking Arrow.*** Using divination magic, you grant your arrow the ability to seek out your target, allowing the arrow to curve and twist its path in search of its prey. When you use this option, you don't make an attack roll for the attack. Instead, choose one creature you have seen in the past minute. The arrow flies toward that creature, moving around corners if necessary and ignoring three-quarters cover and half cover. If the target is within the weapon's range and there is a path large enough for the arrow to travel to the target, the target must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}). On a failed save, it takes damage as if it were hit by the arrow, plus an extra {'1d6' if npc.levels('Fighter') < 18 else '2d6'} force damage, and you learn the target's current location. On a successful save, the target takes half as much damage, and you don't learn its location."))
```

* **Shadow Arrow**. You weave illusion magic into your arrow, causing it to occlude your foe's vision with shadows. If the arrow hits a creature, the target takes an extra 2d6 psychic damage, and it must succeed on a Wisdom saving throw or be unable to see anything farther than 5 feet away until the start of your next turn. 
  The psychic damage increases to 4d6 when you reach 18th level in this class.

```
def shadowarrow(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Shadow Arrow.*** If the arrow hits a creature, the target takes the usual damage, plus {'2d6' if npc.levels('Fighter') < 18 else '4d6'} psychic damage, and must also succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or be unable to see anything farther than 5 feet away until the start of your next turn."))
```

```
arcaneshots = {
    'Banishing Arrow': banishingarrow,
    'Brute Bane Arrow': brutebanearrow,
    'Bursting Arrow': burstingarrow,
    'Grasping Arrow': graspingarrow,
    'Mind-Scrambling Arrow': mindscramblingarrow,
    'Piercing Arrow': piercingarrow,
    'Seeking Arrow': seekingarrow,
    'Shadow Arrow': shadowarrow
}
def choosearcaneshot(npc):
    if getattr(npc, "arcaneshot", None) == None:
        npc.arcaneshot = {
            'uses': 2,
            'options': []
        }
    
    shotlist = arcaneshots
    for (shot, shotfn) in shotlist.items():
        if shot in npc.arcaneshot['options']:
            shotlist.remove(shot)
    (shotname, shotfn) = choose("Choose an Arcane Shot option: ", shotlist)
    shotfn(npc)
```
