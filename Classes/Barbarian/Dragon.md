# Primal Path: Path of the Dragon
All barbarians harbor within them the rage that grants them superior strength, constitution, and speed. For barbarians who follow the Path of the Dragon, that rage is the fiery wrath of a red dragon, the bestial cold of a white dragon, or fury that in some way encapsulates the rage of dragons.

```
name = 'Dragon'
description = "***Primal Path: Path of the Dragon.*** All barbarians harbor within them the rage that grants them superior strength, constitution, and speed. For barbarians who follow the Path of the Dragon, that rage is the fiery wrath of a red dragon, the bestial cold of a white dragon, or fury that in some way encapsulates the rage of dragons."
```

These barbarians are always associated with cells of the [Cult of the Wyrm](../../Organizations/CultOfTheWyrm.md). Their zealousness for dragonkind is the seed of their power, from which their dragonlike rage stems. Most Path of the Dragon barbarians have an evil streak in their nature, though a few have managed to tame the chromatic tendencies and use their rage to good ends.

## Dragon's Rage
*3rd-level Path of the Dragon feature*

Your rage emulates the wrath of a powerful dragon. Choose one of the following options:

* **Black Dragon**. While you are raging, you gain the ability to breathe underwater and you gain a swimming speed of 30 feet. If you already have a swimming speed, it increases to 30 feet, unless it was already faster.

* **Blue Dragon**. While you are raging, your strikes are empowered with lightning. On each of your turns, the first time that you hit with a weapon attack, that attack deals extra lightning damage equal to 1d6 + your barbarian level.

* **Green Dragon**. While you are raging, your movement speed increases by 10 feet, and difficult terrain composed of natural materials such as plants, earth, and water doesn't cost you extra movement.

* **Red Dragon**. While you are raging, your strikes are empowered with fire. On each of your turns, the first time that you hit with a weapon attack, that attack deals extra fire damage equal to 1d6 + your barbarian level.

* **White Dragon**. While you are raging, your weapon attacks score a critical hit on a roll of 19 or 20.

```
def level3(npc):
    npc.dragonchoice = choose("Choose a draconic type: ", ['Black', 'Blue', 'Green', 'Red', 'White'])
    if npc.dragonchoice == 'Black':
        npc.traits.append("***Dragon's Rage.*** While you are raging, you gain the ability to breathe underwater and you gain a swimming speed of 30 feet. If you already have a swimming speed, it increases to 30 feet, unless it was already faster.")
    elif npc.dragonchoice == 'Blue':
        npc.defer(lambda npc: npc.traits.append("***Dragon's Rage.*** While you are raging, your strikes are empowered with lightning. On each of your turns, the first time that you hit with a weapon attack, that attack deals 1d6 + {npc.levels('Barbarian')} extra lightning damage.") )
    elif npc.dragonchoice == 'Green':
        npc.traits.append("***Dragon's Rage.*** While you are raging, your movement speed increases by 10 feet, and difficult terrain composed of natural materials such as plants, earth, and water doesn't cost you extra movement.")
    elif npc.dragonchoice == 'Red':
        npc.defer(lambda npc: npc.traits.append("***Dragon's Rage.*** While you are raging, your strikes are empowered with fire. On each of your turns, the first time that you hit with a weapon attack, that attack deals 1d6 + {npc.levels('Barbarian')} extra fire damage.") )
    elif npc.dragonchoice == 'White':
        npc.traits.append("***Dragon's Rage.*** While you are raging, your weapon attacks score a critical hit on a roll of 19 or 20.")
```

## Dragon's Armor
*6th-level Path of the Dragon feature*

You gain resistance to a damage type determined by the dragon type you chose at 3rd level. You do not need to be raging to have this resistance.

* **Black Dragon**. You gain resistance to acid damage.
* **Blue Dragon**. You gain resistance to lightning damage.
* **Green Dragon**. You gain resistance to poison damage.
* **Red Dragon**. You gain resistance to fire damage.
* **White Dragon**. You gain resistance to cold damage.

Moreover, while you are raging, you can develop dragon scales to shield you from attack. While you are raging, if you are hit by an attack, you can use your reaction to add your Charisma modifier to your AC for that attack, potentially causing the attack to miss. To gain this bonus, you cannot be wearing armor. You can use this feature only once per rage.

```
def level6(npc):
    if npc.dragonchoice == 'Black':
        npc.damageresistances.append("acid")
    elif npc.dragonchoice == 'Blue':
        npc.damageresistances.append("lightning")
    elif npc.dragonchoice == 'Green':
        npc.damageresistances.append("poison")
    elif npc.dragonchoice == 'Red':
        npc.damageresistances.append("fire")
    elif npc.dragonchoice == 'White':
        npc.damageresistances.append("cold")

    npc.defer(lambda npc: npc.reactions.append(f"***Dragon's Armor (1/Rage).*** You add {npc.CHAbonus()} to your AC for that attack, potentially causing the attack to miss. To gain this bonus, you cannot be wearing armor.") )
```

## Fearsome Roar
*10th-level Path of the Dragon feature*

Whenever you enter your rage, you can choose to unleash a fearsome roar. If you do so, every creature of your choice within 60 feet of you that can see you must make a Wisdom saving throw. The DC for this saving throw equals 8 + your proficiency bonus + your Charisma modifier. On a failed save, a creature is frightened of you. An affected creature can attempt the saving throw again at the end of each of its turns, ending the effect on itself on a success. The effect ends early if your rage ends.

```
def level10(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Fearsome Roar.*** Whenever you enter your rage, you can choose to unleash a fearsome roar. If you do so, every creature of your choice within 60 feet of you that can see you must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}). On a failed save, a creature is frightened of you. An affected creature can attempt the saving throw again at the end of each of its turns, ending the effect on itself on a success. The effect ends early if your rage ends.") )
```

## Dragon's Flight
*14th-level Path of the Dragon feature*

Whenever you enter your rage, you also sprout a pair of spectral draconic wings. These wings grant you a flying speed of 30 feet, however you do not have the ability to sustain flight. You cannot end your turn in the air; if you do, you fall. The wings disappear when your rage ends.

```
def level14(npc):
    npc.traits.append("***Dragon's Flight.*** Whenever you enter your rage, you also sprout a pair of spectral draconic wings. These wings grant you a flying speed of 30 feet, however you do not have the ability to sustain flight. You cannot end your turn in the air; if you do, you fall. The wings disappear when your rage ends.")
```
