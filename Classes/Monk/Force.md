# Monastic Tradition: Way of the Binding Force
Your monastic tradition centers around a mysterious and powerful force that binds together all living things. As a follower of this tradition, you learn to manipulate the binding force to manipulate the minds of others, move objects, or to wreak havoc upon your foes in combat. Monks of this tradition believe that the Force That Binds Us All is a force more powerful than even the gods, and that it guides and shapes the direction of the world is subtle ways. Their job, then, is to listen to the Will of the Binding Force (which they will often refer to as just "the Will"), and heed the guidance it offers on the path it wants the world to take ("the Way").

Some scholars believe that the Way of the Binding Force is an offshoot of [mystics](../Mystic.md) and their psionic abilities, others suggest that Force monks tap into the power of arcana (or divinity), while still others believe it to be an entirely different sort of power altogether. Force monks often travel alone, seeking to dispense justice in matters that find them, or sometimes taking on matters that they perceive require correction. Not openly good, but certainly not evil, the Way of the Binding Force almost seems Druidic in its belief system, yet, as Force monks will be quick to point out, "even Nature must find its Way within the Will of the Binding Force".

```
name = 'Way of the Binding Force'
description = "***Monastic Tradition: Way of the Binding Force.*** Your monastic tradition centers around a mysterious and powerful force that binds together all living things. As a follower of this tradition, you learn to manipulate the binding force to manipulate the minds of others, move objects, or to wreak havoc upon your foes in combat. Monks of this tradition believe that the Force That Binds Us All is a force more powerful than even the gods, and that it guides and shapes the direction of the world is subtle ways. Their job, then, is to listen to the Will of the Binding Force (which they will often refer to as just \"the Will\"), and heed the guidance it offers on the path it wants the world to take (\"the Way\")."
```

## Disciple of the Binding Force
*3rd-level Way of the Binding Force feature*

You learn magical disciplines that harness the power that interconnects all living things. A discipline requires you to spend ki points each time you use it.

You know the Forceful Abilities discipline and one other force discipline of your choice. You learn one additional discipline of your choice at 6th, 11th, and 17th level.

Whenever you learn a new discipline, you can also replace one discipline that you already know with a different discipline.

```
def level3(npc):
    npc.forcedisciplines = ['Forceful Abilities']
    forcefulabilities(npc)
    choosediscipline(npc)

def level6(npc):
    choosediscipline(npc)

def level11(npc):
    choosediscipline(npc)

def level17(npc):
    choosediscipline(npc)
```

### Casting Discipline Spells
Some disciplines allow you to cast spells. To cast one of these spells, you use its casting time and other rules, but you don't need to provide material components for it.

Once you reach 5th level in this class, you can spend additional ki points to increase the level of a discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as catapult does. The spell's level increases by 1 for each additional ki point you spend. For example, if you are a 5th-level monk and use Forceful Throw to cast [catapult](../../Magic/Spells/catapult.md), you can spend 3 ki points to cast it as a 2nd-level spell (the discipline's base cost of 2 ki points plus 1). The maximum number of ki points you can spend to cast a spell in this way (including its base ki point cost and any additional ki points you spend to increase its level) is determined by your monk level, as shown in the Spells and Ki Points table.

**Spells and Ki Points**

Monk Levels|Maximum Ki Points for a Spell
-----------|-------------------
5th–8th|3
9th–12th|4
13th–16th|5
17th–20th|6

```
def level5(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Enhanced Discipline Spells.*** You can spend up to {3 if npc.levels('Monk') < 8 else 4 if npc.levels('Monk') < 12 else 5 if npc.levels('Monk') < 16 else 6} ki points to increase the level of a discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as catapult does. The spell's level increases by 1 for each additional ki point you spend. This maximum includes the base ki point cost as well as any additional ki points you spend to increase its level.") )
```

## Force Disciplines
The force disciplines are presented in alphabetical order. If a discipline requires a level, you must be that level in this class to learn the discipline.

**Controlling Grasp (17th Level Required).** You can spend 6 ki points to cast [telekinesis](../../Magic/Spells/telekinesis.md).

```
def controllinggrasp(npc):
    npc.actions.append(f"***Force Discipline: Controlling Grasp.*** You can spend 6 ki points to cast {spelllinkify('telekinesis')}.")
```

**Constricting Grasp (6th Level Required).** You can spend 3 ki points to cast [hold person](../../Magic/Spells/hold-person.md).

```
def constrictinggrasp(npc):
    npc.actions.append(f"***Force Discipline: Controlling Grasp.*** You can spend 3 ki points to cast {spelllinkify('hold person')}.")
```

**Empowered Weapon.** As a bonus action, you can expend 2 ki points to channel the binding force into one monk weapon you're holding. For the next 1 minute, you deal an extra 1d6 radiant damage to any target you hit with the weapon. If the weapon isn't magical, it becomes a magic weapon for the spell's duration.

```
def empoweredweapon(npc):
    npc.bonusactions.append("***Force Discipline: Empowered Weapon.*** You can expend 2 ki points to channel the binding force into one monk weapon you're holding. For the next 1 minute, you deal an extra 1d6 radiant damage to any target you hit with the weapon, and the weapon becomes magical if it isn't already for the spell's duration.")
```

**Extraordinary Speed (11th Level Required).** You can spend 4 ki points to cast [haste](../../Magic/Spells/haste.md), targeting yourself.

```
def extraordinaryspeed(npc):
    npc.actions.append(f"***Force Discipline: Extraordinary Speed.*** You can spend 4 ki points to cast {spelllinkify('haste')}, targeting yourself.")
```

**Far-Reaching Voice (11th Level Required).** You can spend 4 ki points to cast [sending](../../Magic/Spells/sending.md).

```
def farreachingvoice(npc):
    npc.actions.append(f"***Force Discipline: Far-Reaching Voice.*** You can spend 4 ki points to cast {spelllinkify('sending')}.")
```

**Focused Mind Trick (6th Level Required).** You can spend 3 ki points to cast [suggestion](../../Magic/Spells/suggestion.md).

```
def focusedmindtrick(npc):
    npc.actions.append(f"***Force Discipline: Focused Mind Trick.*** You can spend 3 ki points to cast {spelllinkify('suggestion')}.")
```

**Forceful Abilities.** You can use your action and your understanding of the binding force to create one of the following effects at a point you can see within range:

* One Medium or smaller creature that you choose must succeed on a Strength saving throw or be pushed up to 5 feet away from you.
* You create a small blast of force capable of moving one object that is neither held nor carried and that weighs no more than 5 pounds. The object is pushed up to 10 feet away from you. It isn't pushed with enough force to cause damage.
* You create a harmless sensory affect, such as causing leaves to rustle, shutters to slam shut, or your clothing to ripple.

```
def forcefulabilities(npc):
    npc.actions.append("***Force Discipline: Forceful Abilities.*** You can use your action and your understanding of the binding force to create one of the following effects at a point you can see within range: one Medium or smaller creature that you choose must succeed on a Strength saving throw or be pushed up to 5 feet away from you; you create a small blast of force capable of moving one object that is neither held nor carried and that weighs no more than 5 pounds. The object is pushed up to 10 feet away from you. It isn't pushed with enough force to cause damage; you create a harmless sensory affect, such as causing leaves to rustle, shutters to slam shut, or your clothing to ripple.")
```

**Forceful Move.** You can spend 2 ki points as an action to use an unseen wave of force to push or pull a creature either toward you or to the ground. A creature that you can see within 30 feet of you must make a Strength saving throw. On a failed save the creature takes 3d10 force damage, plus an extra 1d10 force damage for each additional ki point you spend, and you can either knock the target prone, push it up to 25 feet away from you, or pull it up to 25 feet away toward you. On a successful save, the creature takes half as much damage and you don't move it or knock it prone.

```
def forcefulmove(npc):
    npc.defer(lambda npc: npc.actions.append("***Force Discipline: Forceful Move.*** You can spend 2 ki points to use an unseen wave of force to pull a creature either toward you or to the ground. A creature that you can see within 30 feet of you must make a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}). On a failed save the creature takes 3d10 force damage, plus an extra 1d10 force damage for each additional ki point you spend, and you can either knock the target prone or pull it up to 25 feet away toward you. On a successful save, the creature takes half as much damage and you don't pull it or knock it prone.") )
```

**Forceful Returning.** Immediately after you make a ranged weapon attack with a thrown monk weapon, you can spend a ki point to manipulate the binding force and cause that weapon to fly back to your hand.

```
def forcefulreturning(npc):
    npc.traits.append("***Force Discipline: Forceful Returning.*** Immediately after you make a ranged weapon attack with a thrown monk weapon, you can spend a ki point to manipulate the binding force and cause that weapon to fly back to your hand.")
```

**Forceful Throw.** You can spend 2 ki points to cast [catapult](../../Magic/Spells/catapult.md).

```
def forcefulthrow(npc):
    npc.actions.append("***Force Discipline: Forceful Throw.*** You can spend 2 ki points to cast {spelllinkify('catapult')}.")
```

**Mind Domination (17th Level Required).** You can spend 6 ki points to cast [dominate person](../../Magic/Spells/dominate-person.md).

```
def minddomination(npc):
    npc.actions.append("***Force Discipline: Mind Domination.*** You can spend 6 ki points to cast {spelllinkify('dominate person;)}.")
```

**Mind Trick.** You can spend 2 ki points to cast [charm person](../../Magic/Spells/charm-person.md).

```
def mindtrick(npc):
    npc.actions.append("***Force Discipline: Mind Trick.*** You can spend 2 ki points to cast {spelllinkify('charm person')}.")
```

**Mystic Senses (17th Level Required).** You can spend 5 ki points to cast [locate creature](../../Magic/Spells/locate-creature.md).

```
def mysticsenses(npc):
    npc.actions.append("***Force Discipline: Mystic Senses.*** You can spend 5 ki points to cast {spelllinkify('locate creature')}.")
```

**Powerful Mind Trick (17th Level Required).** You can spend 5 ki points to cast [charm monster](../../Magic/Spells/charm-monster.md).

```
def powerfulmindtrick(npc):
    npc.actions.append("***Force Discipline: Powerful Mind Trick.*** You can spend 5 ki points to cast {spelllinkify('charm monster')}.")
```

**Spirit Lightning. (11th Level Required).** You can spend 4 ki points to cast [lightning bolt](../../Magic/Spells/lightning-bolt.md).

```
def spiritlightning(npc):
    npc.actions.append("***Force Discipline: Spirit Lightning.*** You can spend 4 ki points to cast {spelllinkify('lightning bolt')}.")
```

**Supernatural Agility.** You can spend 2 ki points to cast either [jump](../../Magic/Spells/jump.md) or [longstrider](../../Magic/Spells/longstrider.md), targeting yourself.

```
def supernaturalagility(npc):
    npc.actions.append("***Force Discipline: Supernatural Agility.*** You can spend 2 ki points to cast either {spelllinkify('jump')} or {spelllinkify('longstrider')}, targeting yourself.")
```

```
disciplines = {
    'Controlling Grasp': [17, controllinggrasp],
    'Constricting Grasp': [6, constrictinggrasp],
    'Empowered Weapon': [0, empoweredweapon],
    'Extraordinary Speed': [11, extraordinaryspeed],
    'Far-Reaching Voice': [11, farreachingvoice],
    'Focused Mind Trick': [6, focusedmindtrick],
    'Forceful Abilities': [0, forcefulabilities],
    'Forceful Move': [0, forcefulmove],
    'Forceful Returning': [0, forcefulreturning],
    'Forceful Throw': [0, forcefulthrow],
    'Mind Domination': [17, minddomination],
    'Mind Trick': [0, mindtrick],
    'Mystic Senses': [17, mysticsenses],
    'Powerful Mind Trick': [17, powerfulmindtrick],
    'Spirit Lightning': [11, spiritlightning],
    'Supernatural Agility': [0, supernaturalagility]
}
def choosediscipline(npc):
    availdisciplines = {}
    for (dname, dlist) in disciplines.items():
        if dname not in npc.forcedisciplines:
            if npc.levels('Monk') >= dlist[0]:
                availdisciplines[dname] = dlist[1]
    (chosenname, chosenfn) = choose("Choose a force discipline: ", availdisciplines)
    npc.forcedisciplines.append(chosenname)
    chosenfn(npc)
```
