# Mystic Order: Order of the Avatar
Mystics of the Order of the Avatar delve into the world of emotion, mastering their inner life to such an extent that they can manipulate and amplify the emotions of others with the same ease that an artist shapes clay. Known as Avatars, these mystics vary from tyrants to inspiring leaders who are loved by their followers.

Avatars can bring out extreme emotions in the people around them. For their allies, they can lend hope, ferocity, and courage, transforming a fighting band into a deadly, unified force. For their enemies, they bring fear, disgust, and trepidation that can make even the most hardened veteran act like a shaky rookie.

The Heart of the Council of Seers in Zhi is always a mystic of the Order of the Avatar; their abilities to inspire and evoke emotion makes them the most common spokesperson to the people of Zhi, and they often serve as the interlocutor between the Council and visitors.

```
name = 'Order of the Avatar'
description = "***Mystic Order: Order of the Avatar.*** Mystics of the Order of the Avatar delve into the world of emotion, mastering their inner life to such an extent that they can manipulate and amplify the emotions of others with the same ease that an artist shapes clay. Known as Avatars, these mystics vary from tyrants to inspiring leaders who are loved by their followers."
```

## Bonus Disciplines
*1st-level Order of the Avatar feature*

You learn two additional psionic disciplines of your choice. They must be chosen from among the Avatar disciplines.

```
def level1(npc):
    allclasses['Mystic'].choosediscipline(npc, avatardisciplines)
    allclasses['Mystic'].choosediscipline(npc, avatardisciplines)
```

## Armor Training
*1st-level Order of the Avatar feature*

You gain proficiency with medium armor and shields.

```
    for arm in armor['medium'] | armor['shields']:
        npc.proficiencies.append(arm)
```

## Avatar of Battle
*3rd-level Order of the Avatar feature*

You project an inspiring aura. While you aren't incapacitated, each ally within 30 feet of you who can see you gains a +2 bonus to initiative rolls.

```
def level3(npc):
    npc.traits.append("***Avatar of Battle.*** While you aren't incapacitated, each ally within 30 feet of you who can see you gains a +2 bonus to initiative rolls.")
```

## Avatar of Healing
*6th-level Order of the Avatar feature*

You project an aura of resilience. While you aren't incapacitated, each ally within 30 feet of you who can see you regains additional hit points equal to your Intelligence modifier (minimum of 0) whenever they regain hit points from a psionic discipline.

```
def level6(npc):
    npc.traits.append("***Avatar of Healing.*** While you aren't incapacitated, each ally within 30 feet of you who can see you regains additional hit points equal to your Intelligence modifier (minimum of 0) whenever they regain hit points from a psionic discipline.")
```

## Avatar of Speed
*14th-level Order of the Avatar feature*

You project an aura of speed. While you aren't incapacitated, any ally within 30 feet of you who can see you can take the Dash action as a bonus action.

```
def level14(npc):
    npc.traits.append("***Avatar of Speed.*** While you aren't incapacitated, any ally within 30 feet of you who can see you can take the Dash action as a bonus action.")
```

## Avatar Psionic Discplines

* [crown of despair](../../Magic/Disciplines/crown-of-despair.md)
* [crown of disgust](../../Magic/Disciplines/crown-of-disgust.md)
* [crown of rage](../../Magic/Disciplines/crown-of-rage.md)
* [mantle of command](../../Magic/Disciplines/mantle-of-command.md)
* [mantle of courage](../../Magic/Disciplines/mantle-of-courage.md)
* [mantle of fear](../../Magic/Disciplines/mantle-of-fear.md)
* [mantle of fury](../../Magic/Disciplines/mantle-of-fury.md)
* [mantle of joy](../../Magic/Disciplines/mantle-of-joy.md)

```
def crownofdespair(npc):
    npc.bonusactions.append("***Psychic Focus: Crown of Despair.*** While focused on this discipline, you have advantage on Charisma (Intimidation) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Crowned in Sorrow (1–7 psi).*** One creature you can see within 60 feet of you must make a Charisma saving throw. On a failed save, it takes 1d8 psychic damage per psi point spent, and it can’t take reactions until the start of its next turn. On a successful save, it takes half as much damage.")

    npc.actions.append("***Call to Inaction (2 psi; concentration, 10 min.).*** If you spend 1 minute conversing with a creature, you can attempt to seed it with overwhelming ennui. At the end of the minute, you can use an action to force the creature to make a Wisdom saving throw. The save automatically succeeds if the target is immune to being charmed. On a failed save, it sits and is incapacitated until your concentration ends. This effect immediately ends if the target or any ally it can see is attacked or takes damage. On a successful save, the creature is unaffected and has no inkling of your attempt to bend its will.")

    npc.actions.append("***Visions of Despair (3 psi).*** You force one creature you can see within 60 feet of you to make a Charisma saving throw. On a failed save, it takes 3d6 psychic damage, and its speed is reduced to 0 until the end of its next turn. On a successful save, it takes half as much damage. You can increase the damage by 1d6 per additional psi point spent on it.")

    npc.actions.append("***Dolorous Mind (5 psi; concentration, 1 min.).*** You choose one creature you can see within 60 feet of you. It must succeed on a Charisma saving throw, or it is incapacitated and has a speed of 0 until your concentration ends. It can repeat this saving throw at the end of each of its turns, ending the effect on itself on a success.")

def crownofdisgust(npc):
    npc.bonusactions.append("***Psychic Focus: Crown of Disgust.*** While you are focused on this discipline, the area in a 5-foot radius around you is difficult terrain for any enemy that isn’t immune to being frightened. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Eye of Horror (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must make a Charisma saving throw. On a failed save, it takes 1d6 psychic damage per psi point spent and can’t move closer to you until the end of its next turn. On a successful save, it takes half as much damage.")

    npc.actions.append("***Wall of Repulsion (3 psi; concentration, 10 min.).*** You create an invisible, insubstantial wall of energy within 60 feet of you that is up to 30 feet long, 10 feet high, and 1 foot thick. The wall lasts until your concentration ends. Any creature attempting to move through it must make a Wisdom saving throw. On a failed save, a creature can’t move through the wall until the start of its next turn. On a successful save, the creature can pass through it. A creature must make this save whenever it attempts to pass through the wall, whether willingly or unwillingly.")

    npc.actions.append("***Visions of Disgust (5 psi; concentration, 1 min.).*** Choose one creature you can see within 60 feet of you. The target must make a Wisdom saving throw. On a failed save, you cause that creature to regard all other beings as horrid, alien entities, and it takes 5d6 psychic damage, and until your concentration ends, it takes 1d6 psychic damage per creature within 5 feet of it at the end of each of its turns. On a successful save, the target takes only half the initial damage and suffers none of the other effects.")

    npc.actions.append("***World of Horror (7 psi; concentration, 1 min.).*** As an action, choose up to six creatures within 60 feet of you. Each target must make a Charisma saving throw. On a failed save, a target takes 8d6 psychic damage, and it is frightened until your concentration ends. On a successful save, a target takes half as much damage. While frightened by this effect, a target’s speed is reduced to 0, and the target can use its action, and any bonus action it might have, only to make melee attacks. The frightened target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.")

def crownofrage(npc):
    npc.bonusactions.append("***Psychic Focus: Crown of Rage.*** While you are focused on this discipline, any enemy within 5 feet of you that makes a melee attack roll against creatures other than you does so with disadvantage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Primal Fury (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must succeed on a Charisma saving throw or take 1d6 psychic damage per psi point spent on this ability and immediately use its reaction to move its speed in a straight line toward its nearest enemy. The save automatically succeeds if the target is immune to being charmed.")

    npc.actions.append("***Fighting Words (2 psi; concentration, 10 min.).*** If you spend 1 minute conversing with a creature, you can attempt to leave a simmering violence in its mind. At the end of the minute, you can use an action to force the creature to make a Wisdom saving throw to resist feeling violent urges against one creature you describe to it or name. The save automatically succeeds if the target is immune to being charmed. On a failed save, the target attacks the chosen creature if it sees that creature before your concentration ends, using weapons or spells against a creature it was already hostile toward or unarmed strikes against an ally or a creature it was neutral toward. Once the fight starts, it continues to attack for 5 rounds before this effect ends. This effect immediately ends if the target or any ally it can see is attacked or takes damage from any creature other than the one it has been incited against. On a successful save, the creature is unaffected and has no inkling of your attempt to bend its will.")

    npc.bonusactions.append("***Mindless Courage (2 psi).*** Choose one creature you can see within 60 feet of you. The target must succeed on a Wisdom saving throw or, until the end of your next turn, you cause that creature's bloodlust to overcome its sense of preservation and it can’t willingly move unless its movement brings it closer to its nearest enemy that it can see. The save automatically succeeds if the target is immune to being charmed.")

    npc.bonusactions.append("***Punishing Fury (5 psi; concentration, 1 min.).*** Choose one creature you can see within 60 feet of you. The target must succeed on a Wisdom saving throw or, until your concentration ends, you cause that creature's rage to grow so hot that it attacks without heeding its own safety, and any creature within 5 feet of it can use a reaction to make a melee attack against it whenever the target makes a melee attack. The save automatically succeeds if the target is immune to being charmed.")

def mantleofcommand(npc):
    npc.reactions.append("***Psychic Focus: Mantle of Command.*** While focused on this discipline, when you end your turn and didn’t move during it, you allow one ally you can see within 30 feet of you to move up to half their speed, following a path of your choice. To move in this way, the ally mustn’t be incapacitated. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Coordinated Movement (2 psi).*** Choose up to five allies you can see within 60 feet of you. Each of those allies can use their reaction to move up to half their speed, following a path of your choice.")

    npc.actions.append("***Commander’s Sight (2 psi; concentration, 1 rnd.).*** Choose one creature you can see within 60 feet of you. Until the start of your next turn, your allies have advantage on attack rolls against that target.")

    npc.actions.append("***Command to Strike (3 psi).*** Choose one ally you can see within 60 feet of you. That ally can use their reaction to immediately take the Attack action. You choose the targets.")

    npc.actions.append("***Strategic Mind (5 psi; concentration, 1 min.).*** You exert an aura of trust and command that unites your allies into a cohesive unit. Until your concentration ends, any ally within 60 feet of you on their turn can, as a bonus action, take the Dash or Disengage action or roll a d4 and add the number rolled to each attack roll they make that turn.")

    npc.actions.append("***Overwhelming Attack (7 psi).*** Choose up to five allies you can see within 60 feet of you. Each of those allies can use their reaction to take the Attack action. You choose the targets of the attacks.")

def mantleofcourage(npc):
    npc.bonusactions.append("***Psychic Focus: Mantle of Courage.*** While focused on this discipline, you and allies within 10 feet of you who can see you have advantage on saving throws against being frightened. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Incite Courage (2 psi).*** Choose up to six creatures you can see within 60 feet of you. If any of those creatures is frightened, that condition ends on that creature.")

    npc.bonusactions.append("***Aura of Victory (1–7 psi; concentration, 10 min.).*** You project psionic energy until your concentration ends. The energy fortifies you and your allies when your enemies are felled; whenever an enemy you can see is reduced to 0 hit points, you and each of your allies within 30 feet of you gain temporary hit points equal to double the psi points spent to activate this effect.")

    npc.actions.append("***Pillar of Confidence (6 psi; concentration, 1 rnd.).*** You and up to five creatures you can see within 60 feet of you each gain one extra action to use on your individual turns. The action goes away if not used before the end of your next turn. the action can be used only to make one weapon attack or to take the Dash or Disengage action.")

def mantleoffear(npc):
    npc.bonusactions.append("***Psychic Focus: Mantle of Fear.*** While focused on this discipline, you have advantage on Charisma (Intimidation) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Incite Fear (2 psi; concentration, 1 min.).*** Choose one creature you can see within 60 feet of you. The target must succeed on a Wisdom saving throw or become frightened of you until your concentration ends. Whenever the frightened target ends its turn in a location where it can’t see you, it can repeat the saving throw, ending the effect on itself on a success.")

    npc.bonusactions.append("***Unsettling Aura (3 psi; concentration, 1 hr.).*** You cloak yourself in unsettling psychic energy. Until your concentration ends, any enemy within 60 feet of you that can see you must spend 1 extra foot of movement for every foot it moves toward you. A creature ignores this effect if immune to being frightened.")

    npc.actions.append("***Incite Panic (5 psi; concentration, 1 min.).*** Choose up to eight creatures you can see within 90 feet of you that can see you. At the start of each of a target’s turns before your concentration ends, the target must make a Wisdom saving throw. On a failed save, the target is frightened until the start of its next turn, and you roll a die. If you roll an odd number, the frightened target moves half its speed in a random direction and takes no action on that turn, other than to scream in terror. If you roll an even number, the frightened target makes one melee attack against a random target within its reach. If there is no such target, it moves half its speed in a random direction and takes no action on that turn. This effect ends on a target if it succeeds on three saving throws against it.")

def mantleoffury(npc):
    npc.bonusactions.append("***Psychic Focus: Mantle of Fury.*** While focused on this discipline in combat, you and any ally who starts their turn within 10 feet of you gains a 5-foot increase to their walking speed during that turn. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Incite Fury (2 psi; concentration, 1 min.).*** Choose up to three allies you can see within 60 feet of you (you can choose yourself in place of one of the allies). Until your concentration ends, each target can roll a d4 when rolling damage for a melee weapon attack and add the number rolled to the damage roll.")

    npc.bonusactions.append("***Mindless Charge (2 psi).*** Choose up to three creatures you can see within 60 feet of you. Each target can immediately use its reaction to move up to its speed in a straight line toward its nearest enemy.")

    npc.bonusactions.append("***Aura of Bloodletting (3 psi; concentration, 1 min.).*** You unleash an aura of rage. Until your concentration ends, you and any creature within 60 feet of you has advantage on melee attack rolls.")

    npc.actions.append("***Overwhelming Fury (5 psi; concentration, 1 min.).*** You flood rage into one creature you can see within 60 feet of you. The target must succeed on a Charisma saving throw, or it can use its actions only to make melee attacks until your concentration ends. It can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.")

def mantleofjoy(npc):
    npc.bonusactions.append("***Psychic Focus: Mantle of Joy.*** While focused on this discipline, you have advantage on Charisma (Persuasion) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Soothing Presence (1–7 psi).*** Choose up to three creatures you can see within 60 feet of you. Each target gains 3 temporary hit points per psi point spent on this effect.")

    npc.bonusactions.append("***Comforting Aura (2 psi; concentration, 1 min.).*** Choose up to three allies you can see (you can choose yourself in place of one of the allies). Until your concentration ends, each target can roll a d4 when making a saving throw and add the number rolled to the total.")

    npc.bonusactions.append("***Aura of Jubilation (3 psi; concentration, 1 min.).*** You radiate a distracting mirth until your concentration ends. Each creature within 60 feet of you that can see you suffers disadvantage on any checks using the Perception and Investigation skills.")

    npc.bonusactions.append("***Beacon of Recovery (5 psi).*** You and up to five allies you can see within 60 feet of you can immediately make saving throws against every effect they’re suffering that allows a save at the start or end of their turns.")

avatardisciplines = {
    'Crown of Despair' : crownofdespair,
    'Crown of Disgust' : crownofdisgust,
    'Crown of Rage' : crownofrage,
    'Mantle of Command': mantleofcommand,
    'Mantle of Courage': mantleofcourage,
    'Mantle of Fear': mantleoffear,
    'Mantle of Fury': mantleoffury,
    'Mantle of Joy': mantleofjoy
}
for ad in avatardisciplines:
    allclasses['Mystic'].disciplines[ad] = avatardisciplines[ad]
```
