# Fighter
Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.

*You must have a Dexterity or Strength score of 13 or higher in order to multiclass in or out of this class.*

```
name = 'Fighter'
description = "***Class: Fighter.*** Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face."
```

Level|Proficiency Bonus|traits
-----|-----------------|--------
1st|+2|[Fighting Style](#fighting-style), [Second Wind](#second-wind)
2nd|+2|[Action Surge](#action-surge) (x1)
3rd|+2|[Martial Archetype](#martial-archetype)
4th|+2|[Ability Score Improvement](#ability-score-improvement)
5th|+3|[Extra Attack](#extra-attack) (x1)
6th|+3|[Ability Score Improvement](#ability-score-improvement)
7th|+3|[Martial Archetype feature](#martial-archetype)
8th|+3|[Ability Score Improvement](#ability-score-improvement)
9th|+4|[Indomitable](#indomitable) (x1)
10th|+4|[Martial Archetype feature](#martial-archetype)
11th|+4|[Extra Attack](#extra-attack) (x2)
12th|+4|[Ability Score Improvement](#ability-score-improvement)
13th|+5|[Indomitable](#indomitable) (x2)
14th|+5|[Ability Score Improvement](#ability-score-improvement)
15th|+5|[Martial Archetype feature](#martial-archetype)
16th|+5|[Ability Score Improvement](#ability-score-improvement)
17th|+6|[Action Surge](#action-surge) (x2), [Indomitable](#indomitable) (x3)
18th|+6|[Martial Archetype feature](#martial-archetype)
19th|+6|[Ability Score Improvement](#ability-score-improvement)
20th|+6|[Extra Attack](#extra-attack) (x3)

As a fighter, you gain the following class traits.

## Hit Points
**Hit Dice**: 1d10 per fighter level

**Hit Points at 1st Level**: 10 + your Constitution modifier

**Hit Points at Higher Levels**: 1d10 (or 6) + your Constitution modifier per fighter level after 1st

```
def everylevel(npc): npc.hits('d10')
```

## Proficiencies
**Armor**: All armor, shields

**Weapons**: Simple weapons, martial weapons

**Tools**: None

**Saving Throws**: Strength, Constitution

**Skills**: Choose two skills from Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, and Survival

Equipment

* (a) chain mail or (b) leather, longbow, and 20 arrows
* (a) a martial weapon and a shield or (b) two martial weapons
* (a) a light crossbow and 20 bolts or (b) two handaxes
* (a) a dungeoneer's pack or (b) an explorer's pack

```
def level1(npc):
    npc.savingthrows.append("STR")
    npc.savingthrows.append("CON")

    npc.proficiencies.append("All armor and shields")
    npc.proficiencies.append("Simple weapons")
    npc.proficiencies.append("Martial weapons")

    skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    chooseskill(npc, skills)
    chooseskill(npc, skills)

    npc.equipment.append("Martial weapon")
    npc.equipment.append("Shield OR martial weapon")
    npc.equipment.append("Light crossbow and 20 bolts OR two handaxes")
    npc.equipment.append("Dungeoneer's pack, or explorer's pack")
    npc.armorclass['Chain mail'] = 16
```


## Fighting Style
*1st-level fighter feature* 

You adopt a particular style of fighting as your specialty. Choose one of the [styles](Styles.md) available. You can't take a Fighting Style option more than once, even if you later get to choose again.

```
    style = choose("Choose a Fighting Style:", styles)
    npc.fightingstyle = style[0]
    (style[1])(npc)
```

## Second Wind
You have a limited well of stamina that you can draw on to protect yourself from harm. On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.

Once you use this feature, you must finish a short or long rest before you can use it again.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Second Wind (Recharges on short or long rest).*** On your turn, you can regain 1d10 + {npc.levels('Fighter')} hit points."))
```


## Action Surge
Starting at 2nd level, you can push yourself beyond your normal limits for a moment. On your turn, you can take one additional action on top of your regular action and a possible bonus action.

Once you use this feature, you must finish a short or long rest before you can use it again. Starting at 17th level, you can use it twice before a rest, but only once on the same turn.

```
def level2(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Action Surge ({'2/' if npc.levels('Fighter') > 16 else ''}Recharges on short or long rest).*** On your turn, you can take one additional action on top of your regular action and a possible bonus action."))
```

## Martial Archetype
At 3rd level, you choose an archetype that you strive to emulate in your combat styles and techniques:

* [Arcane Archer](ArcaneArcher.md)
* [Banneret](Banneret.md)
* [Battle Master](BattleMaster.md)
* [Blood Thrall](BloodThrall.md)
* [Brute](Brute.md)
* [Cavalier](Cavalier.md)
* [Champion](Champion.md)
* [Dervish](Dervish.md)
* [Dwarven Defender](Defender.md)
* [Dragon Knight](DragonKnight.md)
* [Dragon Slayer](DragonSlayer.md)
* [Dragoon](Dragoon.md)
* [Dreadnought](Dreadnought.md)
* [Duelist](Duelist.md)
* [Eldritch Knight](EldritchKnight.md)
* [Elemental Blade](ElementalBlade.md)
* [Ghost Warrior](GhostWarrior.md)
* [Hollow Knight](Hollow.md)
* [Monster Hunter](MonsterHunter.md)
* [Psi Knight](PsiKnight.md)
* [Rune Knight](RuneKnight.md)
* [Samurai](Samurai.md)
* [Scout](Scout.md)
* [Sharpshooter](Sharpshooter.md)
* [Stillmind Warrior](Stillmind.md)
* [Weapon Master](WeaponMaster.md)

The archetype you choose grants you traits at 3rd level and again at 7th, 10th, 15th, and 18th level.

```
def level3(npc):
    # Choose subclass
    (_, subclass) = choose("Choose a Martial Archetype:", subclasses)
    npc.subclasses[allclasses['Fighter']] = subclass
    npc.description.append(subclass.description)
```

## Ability Score Improvement
When you reach 4th level, and again at 6th, 8th, 12th, 14th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level6(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level14(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

### Martial Versatility
Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, as you shift the focus of your martial practice:

* Replace a fighting style you know with another fighting style available to fighters.
* If you know any maneuvers from the [Battle Master](BattleMaster.md) archetype, you can replace one maneuver you know with a different maneuver. 

## Extra Attack
Beginning at 5th level, you can attack twice, instead of once, whenever you take the Attack action on your turn.

The number of attacks increases to three when you reach 11th level in this class and to four when you reach 20th level in this class.

```
def level5(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Multiattack.*** You can attack {'twice' if npc.levels('Fighter') < 11 else '3 times' if npc.levels('Fighter') < 20 else 'four times'} whenever you take the Attack action on your turn."))
```

## Indomitable
Beginning at 9th level, you can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.

You can use this feature twice between long rests starting at 13th level and three times between long rests starting at 17th level.

```
def level9(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Indomitable ({'' if npc.levels('Fighter') < 13 else '2' if npc.levels('Fighter') < 17 else '3'}Recharges on long rest).*** You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest."))
```

```
# Eventually, these should be in the Styles.md file, and made available in this ("Fighter") module.
# Fighting Style
def archery(npc):
    npc.traits.append("***Fighting Style: Archery.*** You gain a +2 bonus to attack rolls you make with ranged weapons.")
def blindfighting(npc):
    npc.senses['blindsight'] = 10
def closequarters(npc):
    npc.traits.append("***Fighting Style: Close Quarters Shooter.*** When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.")
def defense(npc):
    npc.traits.append("***Fighting Style: Defense.*** While you are wearing armor, you gain a +1 bonus to AC.")
def dueling(npc):
    npc.armorclass['Dueling'] = 2
    npc.traits.append("***Fighting Style: Dueling.*** When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")
def greatweaponfighting(npc):
    npc.traits.append("***Fighting Style: Great Weapon Fighting.*** When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.")
def interception(npc):
    npc.defer(lambda npc: npc.reactions.append("***Fighting Style: Interception.*** When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can reduce the damage the target takes by 1d10 + {npc.proficiencybonus()}. You must be wielding a shield or a simple or martial weapon to use this reaction."))
def mariner(npc):
    npc.speed['swimming'] = npc.speed['walking']
    npc.speed['climbing'] = npc.speed['walking']
    npc.armorclass['Mariner'] = 1
def protection(npc):
    npc.reactions.append("***Fighting Style: Protection.*** When a creature you can see attacks a target other than you that is within 5 feet of you, and you are wielding a shield, you can impose disadvantage on the attack roll.")
def superiortechnique(npc):
    # TODO: Choose from battlemaster.py maneuvers[] list
    npc.traits.append("***Fighting Style: Superior Technique.*** You learn one maneuver of your choice from among those available to the [Battle Master](BattleMaster.md) archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice). \nYou gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it.  You regain your expended superiority dice when you finish a short or long rest.")
def thrownweapon(npc):
    npc.actions.append("***Fighting Style: Thrown Weapon Fighting.*** You can draw a weapon that has the 'thrown' property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll." )
def tunnelfighter(npc):
    npc.bonusactions.append("***Fighting Style: Tunnel Fighter.*** You can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.")
def twoweapon(npc):
    npc.actions.append("***Fighting Style: Two-Weapon Fighting.*** When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")
def unarmedfighting(npc):
    npc.defer(lambda npc: npc.actions.append("***Fighting Style: Unarmed Fighting.*** Your unarmed strikes can deal 1d6 + {npc.STRbonus()} bludgeoning damage on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."))
styles = {
    'Archery': archery,
    'Blind': blindfighting,
    'Close Quarters Shooter': closequarters,
    'Defense': defense,
    'Dueling': dueling,
    'Great Weapon': greatweaponfighting, 
    'Interception': interception,
    'Mariner': mariner,
    'Protection': protection,
    'Superior Technique': superiortechnique,
    'Thrown Weapon': thrownweapon,
    'Tunnel Fighter': tunnelfighter,
    'Two-Weapon': twoweapon,
    'Unarmed': unarmedfighting
}
```
