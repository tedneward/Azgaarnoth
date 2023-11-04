# Mystic Order: Order of the Awakened
Mystics dedicated to the Order of the Awakened seek to unlock the full potential of the mind. By transcending the physical, the Awakened hope to attain a state of being focused on pure intellect and mental energy. 

The Awakened are skilled at bending minds and unleashing devastating psionic attacks, and they can read the secrets of the world through psionic energy. Awakened mystics who take to adventuring excel at unraveling mysteries, solving puzzles, and defeating monsters by turning them into unwilling pawns.

```
name = 'Order of the Awakened'
description = "***Mystic Order: Order of the Awakened.*** Mystics dedicated to the Order of the Awakened seek to unlock the full potential of the mind. By transcending the physical, the Awakened hope to attain a state of being focused on pure intellect and mental energy."
```

## Bonus Disciplines
*1st-level Order of the Awakened feature*

You learn two additional psionic disciplines of your choice. They must be chosen from among the Awakened disciplines.

```
def level1(npc):
    allclasses['Mystic'].choosediscipline(npc, awakeneddisciplines)
    allclasses['Mystic'].choosediscipline(npc, awakeneddisciplines)
```

## Awakened Talent
*1st-level Order of the Awakened feature*

You gain proficiency with two of the following skills of your choice: Animal Handling, Deception, Insight, Intimidation, Investigation, Perception, and Persuasion.

```
    chooseskill(npc, ['Animal Handling', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion'])
    chooseskill(npc, ['Animal Handling', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion'])
```

## Psionic Investigation
*3rd-level Order of the Awakened feature*

You can focus your mind to read the psionic imprint left on an object. If you hold an object and concentrate on it for 10 minutes (as if concentrating on a psionic discipline), you learn a few basic facts about it. You gain a mental image from the object's point of view, showing the last creature to hold the object within the past 24 hours.

You also learn of any events that have occurred within 20 feet of the object within the past hour. The events you perceive unfold from the object's perspective. You see and hear such events as if you were there, but can't use other senses.

Additionally, you can embed an intangible psionic sensor within the object. For the next 24 hours, you can use an action to learn the object's location relative to you (its distance and direction) and to look at the object's surroundings from its point of view as if you were there. This perception lasts until the start of your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level3(npc):
    npc.actions.append("***Psionic Investigation (Recharges on short or long rest).*** You can focus your mind to read the psionic imprint left on an object. If you hold an object and concentrate on it for 10 minutes (as if concentrating on a psionic discipline), you learn a few basic facts about it. You gain a mental image from the object's point of view, showing the last creature to hold the object within the past 24 hours. You also learn of any events that have occurred within 20 feet of the object within the past hour. The events you perceive unfold from the object's perspective. You see and hear such events as if you were there, but can't use other senses.Additionally, you can embed an intangible psionic sensor within the object. For the next 24 hours, you can use an action to learn the object's location relative to you (its distance and direction) and to look at the object's surroundings from its point of view as if you were there. This perception lasts until the start of your next turn.")
```

## Psionic Surge
*6th-level Order of the Awakened feature*

You can overload your psychic focus to batter down an opponent's defenses. You can impose disadvantage on a target's saving throw against a discipline or talent you use, but at the cost of using your psychic focus. Your psychic focus immediately ends if it's active, and you can't use it until you finish a short or long rest.

You can't use this feature if you can't use your psychic focus.

```
def level6(npc):
    npc.traits.append("***Psionic Surge.*** You can overload your psychic focus to batter down an opponent's defenses. You can impose disadvantage on a target's saving throw against a discipline or talent you use, but at the cost of using your psychic focus. Your psychic focus immediately ends if it's active, and you can't use it until you finish a short or long rest. You can't use this feature if you can't use your psychic focus.")
```

## Spectral Form
*14th-level Order of the Awakened feature*

You gain the ability to become a ghostly figure of psionic energy. As an action, you can transform into a transparent, ghostly version of yourself. While in this form, you have resistance to all damage, move at half speed, and can pass through objects and creatures while moving but can't willingly end your movement in their spaces. The form lasts for 10 minutes or until you use an action to end it.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level14(npc):
    npc.actions.append("***Spectral Form (Recharges on long rest).*** You transform into a transparent, ghostly version of yourself. While in this form, you have resistance to all damage, move at half speed, and can pass through objects and creatures while moving but can't willingly end your movement in their spaces. The form lasts for 10 minutes or until you use an action to end it.")
```

## Awakened Psionic Disciplines

* [aura sight](Disciplines/aura-sight.md)
* [intellect fortress](Disciplines/intellect-fortress.md)
* [mantle of awe](Disciplines/mantle-of-awe.md)
* [precognition](Disciplines/precognition.md)
* [psychic assault](Disciplines/psychic-assault.md) 
* [psychic disruption](Disciplines/psychic-disruption.md)
* [psychic inquisition](Disciplines/psychic-inquisition.md)
* [psychic phantoms](Disciplines/psychic-phantoms.md)
* [telepathic contact](Disciplines/telepathic-contact.md)


```
def aurasight(npc):
    npc.bonusactions.append("***Psychic Focus: Aura Sight.*** While focused on this discipline, you have advantage on Wisdom (Insight) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Assess Foe (2 psi).*** You analyze the aura of one creature you see. You learn its current hit point total and all its immunities, resistances, and vulnerabilities.")

    npc.bonusactions.append("***Read Moods (2 psi).*** You learn a one-word summary of the emotional state of up to six creatures you can see, such as happy, confused, afraid, or violent.")

    npc.actions.append("***View Aura (3 psi; concentration, 1 hr.).*** You study one creature's aura. Until your concentration ends, while you can see the target, you learn if it's under the effect of any magical or psionic effects, its current hit point total, and its basic emotional state. While this effect lasts, you have advantage on Wisdom (Insight) and Charisma checks you make against it.")

    npc.bonusactions.append("***Perceive the Unseen (5 psi; concentration, 1 min.).*** You gain the ability to see auras even of invisible or hidden creatures. Until your concentration ends, you can see all creatures, including hidden and invisible ones, regardless of lighting conditions.")

def intellectfortress(npc):
    npc.bonusactions.append("***Psychic Focus: Intellect Fortress.*** While focused on this discipline, you gain resistance to psychic damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.reactions.append("***Psychic Backlash (2 psi).*** You impose disadvantage on an attack roll against you if you can see the attacker. If the attack still hits you, the attacker takes 2d10 psychic damage.")

    npc.reactions.append("***Psychic Parry (1–7 psi).*** When you make an Intelligence, a Wisdom, or a Charisma saving throw, you gain a +1 bonus to that saving throw for each psi point you spend on this ability. You can use this ability after rolling the die but before suffering the results.")

    npc.actions.append("***Psychic Redoubt (5 psi; concentration, 10 min.).*** You create a field of protective psychic energy. Choose any number of creatures within 30 feet of you. Until your concentration ends, each target has resistance to psychic damage and advantage on Intelligence, Wisdom, and Charisma saving throws.")

def mantleofawe(npc):
    npc.bonusactions.append("***Psychic Focus: Mantle of Awe.*** While focused on this discipline, you gain a bonus to Charisma checks. The bonus equals half your Intelligence modifier (minimum of +1). The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Charming Presence (1–7 psi).*** You exert an aura of sympathetic power. Roll 2d8 per psi point spent on this ability; the total is how many hit points worth of creatures this option can affect. Creatures within 30 feet of you are affected in ascending order of their hit point maximums, ignoring incapacitated creatures, creatures immune to being charmed, and creatures engaged in combat. Starting with the creature that has the lowest hit point maximum, each creature affected by this option is charmed by you for 10 minutes, regarding you as a friendly acquaintance. Subtract each creature's hit point maximum from the total before moving on to the next creature. A creature's hit point maximum must be equal to or less than the remaining total for that creature to be affected.")

    npc.actions.append("***Center of Attention (2 psi; concentration, 1 min.).*** You exert an aura of power that grabs a creature's attention. Choose one creature you can see within 60 feet of you. It must make a Charisma saving throw. On a failed save, the creature is so thoroughly distracted by you that all other creatures are invisible to it until your concentration ends. This effect ends if the creature can no longer see or hear you or if it takes damage.")

    npc.actions.append("***Invoke Awe (7 psi; concentration, 10 min.).*** You exert an aura that inspires awe in others. Choose up to 5 creatures you can see within 60 feet of you. Each target must succeed on an Intelligence saving throw or be charmed by you until your concentration ends. While charmed, the target obeys all your verbal commands to the best of its ability and without doing anything obviously self-destructive. The charmed target will attack only creatures that it has seen attack you since it was charmed or that it was already hostile toward. At the end of each of its turns, it can repeat the saving throw, ending the effect on itself on a success.")

def precognition(npc):
    npc.bonusactions.append("***Psychic Focus: Precognition.*** While focused on this discipline, you have advantage on initiative rolls. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Precognitive Hunch (2 psi; concentration, 1 min.).*** You open yourself to receive momentary insights that improve your odds of success; until your concentration ends, whenever you make an attack roll, a saving throw, or an ability check, you roll a d4 and add it to the total.")

    npc.reactions.append("***All-Around Sight (3 psi).*** In response to an attack hitting you, you impose disadvantage on that attack roll, possibly causing it to miss.")

    npc.actions.append("***Danger Sense (5 psi; concentration, 8 hr.).*** You create a psychic model of reality in your mind and set it to show you a few seconds into the future. Until your concentration ends, you can't be surprised, attack rolls against you can't gain advantage, and you gain a +10 bonus to initiative.")

    npc.traits.append("***Victory Before Battle (7 psi).*** When you roll initiative, you can use this ability to grant yourself and up to five creatures of your choice within 60 feet of you a +10 bonus to initiative.")

def psychicassault(npc):
    npc.bonusactions.append("***Psychic Focus: Psychic Assault.*** While focused on this discipline, you gain a +2 bonus to damage rolls with psionic talents that deal psychic damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Psionic Blast (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target takes 1d8 psychic damage per psi point spent on this ability.")

    npc.actions.append("***Ego Whip (3 psi).*** Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, the creature takes 3d8 psychic damage, and it is filled with self-doubt, leaving it able to use its action on its next turn only to take the Dodge, Disengage, or Hide action. On a successful saving throw, it takes half damage.")

    npc.actions.append("***Id Insinuation (5 psi).*** Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, the creature takes 5d8 psychic damage, and it goes into a fury, as its id runs rampant. On its next turn, it can use its action only to take the Dodge or Attack action. On a successful save, it takes half damage.")

    npc.actions.append("***Psychic Blast (6 psi).*** You unleash devastating psychic energy in a 60-foot cone. Each creature in that area must make an Intelligence saving throw, taking 8d8 psychic damage on a failed save, or half damage on a successful one. You can increase the damage by 2d8 if you spend 1 more psi point on this ability.")

    npc.actions.append("***Psychic Crush (7 psi).*** You create a 20-foot cube of psychic energy within 120 feet of you. Each creature in that area must make an Intelligence saving throw. On a failed save, a target takes 8d8 psychic damage and is stunned until the end of your next turn. On a successful save, a target takes half damage.")

def psychicdisruption(npc):
    npc.bonusactions.append("***Psychic Focus: Psychic Disruption.*** While focused on this discipline, you have advantage on Charisma (Deception) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Distracting Haze (1–7 psi; concentration, 1 min.).*** Choose one creature you can see within 60 feet of you. That creature must make an Intelligence saving throw. On a failed save, it takes 1d10 psychic damage per psi point spent and can't see anything more than 10 feet from it until your concentration ends. On a successful save, it takes half as much damage.")

    npc.actions.append("***Daze (3 psi).*** Choose one creature you can see within 60 feet of you. That creature must make an Intelligence saving throw. On a failed save, the target is incapacitated until the end of your next turn or until it takes any damage.")

    npc.actions.append("***Mind Storm (5 psi).*** Choose a point you can see within 60 feet of you. Each creature in a 20-foot-radius sphere centered on that point must make a Wisdom saving throw. On a failed save, a target takes 6d8 psychic damage and suffers disadvantage on all saving throws until the end of your next turn. On a successful save, a creature takes half as much damage. You can increase the damage by 1d6 per additional psi point spent on this ability.")

def psychicinquisition(npc):
    npc.bonusactions.append("***Psychic Focus: Psychic Inquisition.*** While focused on this discipline, you know when a creature communicating with you via telepathy is lying. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Hammer of Inquisition (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, it takes 1d10 psychic damage per psi point spent and suffers disadvantage on its next Wisdom saving throw before the end of your next turn. On a successful save, it takes half as much damage.")

    npc.actions.append("***Forceful Query (2 psi).*** You ask a question of one creature that can see and hear you within 30 feet of you. The question must be phrased so that it can be answered with a yes or no, otherwise this ability fails. The target must succeed on a Wisdom saving throw, or it replies with a truthful answer. A creature is immune to this ability if it is immune to being charmed.")

    npc.traits.append("***Ransack Mind (5 psi; concentration, 1 hr.).*** While you concentrate on this ability, you probe one creature's mind. The creature must remain within 30 feet of you, and you must be able to see it. If you reach the ability's full duration (1 hour), the target must make three Intelligence saving throws, and you learn information from it based on the number of saving throws it fails: With one failed saving throw, you learn its key memories from the past 12 hours; With two failed saving throws, you learn its key memories from the past 24 hours; With three failed saving throws, you learn its key memories from the past 48 hours.")

    npc.traits.append("***Phantom Idea (6 psi; concentration, 1 hr.).*** While you concentrate on this ability, you probe one creature's mind. The creature must remain within 30 feet of you, and you must be able to see it. If you reach the ability's full duration (1 hour), the target must make three Intelligence saving throws, and you plant a memory or an idea in it, which lasts for a number of hours based on the number of saving throws it fails (With one failed saving throw, the idea or memory lasts for the next 4 hours; With two failed saving throws, it lasts for 24 hours; With three failed saving throws, it lasts for 48 hours.). You choose whether the idea or memory is trivial (such as \"I had porridge for breakfast\" or \"Ale is the worst\") or personality-defining (\"I failed to save my village from orc marauders and am therefore a coward\" or \"Magic is a scourge, so I renounce it\").")

def psychicphantoms(npc):
    npc.bonusactions.append("***Psychic Focus: Psychic Phantoms.*** While focused on this discipline, you have advantage on Charisma (Deception) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Distracting Figment (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, it takes 1d10 psychic damage per psi point spent and thinks it perceives a threatening creature just out of its sight; until the end of your next turn, it can't use reactions, and melee attack rolls against it have advantage. On a successful save, it takes half as much damage.")

    npc.actions.append("***Phantom Foe (3 psi; concentration, 1 min.).*** Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, it perceives a horrid creature adjacent to it until your concentration ends. During this time, the target can't take reactions, and it takes 1d8 psychic damage at the start of each of its turns. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. You can increase the damage by 1d8 for each additional psi point spent on the ability.")

    npc.actions.append("***Phantom Betrayal (5 psi; concentration, 1 min.).*** You plant delusional paranoia in a creature's mind. Choose one creature you can see within 60 feet of you. The target must succeed on an Intelligence saving throw, or until your concentration ends, it must target its allies with attacks and other damaging effects. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. A creature is immune to this ability if it is immune to being charmed.")

    npc.actions.append("***Phantom Riches (7 psi; concentration, 1 min.).*** You plant the phantom of a greatly desired object in a creature's mind. Choose one creature you can see within 60 feet of you. The target must make an Intelligence saving throw. On a failed save, you gain partial control over the target's behavior until your concentration ends; the target moves as you wish on each of its turns, as it thinks it pursues the phantom object it desires. If it hasn't taken damage since its last turn, it can use its action only to admire the object you created in its perception. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success.")

def telepathiccontact(npc):
    npc.bonusactions.append("***Psychic Focus: Telepathic Contact.*** While focused on this discipline, you gain the ability to use your Telepathy class feature with up to six creatures at once. If you don't have that feature from the mystic class, you instead gain it while focused on this discipline. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Exacting Query (2 psi).*** You target one creature you can communicate with via telepathy. The target must make an Intelligence saving throw. On a failed save, the target truthfully answers one question you ask it via telepathy. On a successful save, the target is unaffected, and you can't use this ability on it again until you finish a long rest. A creature is immune to this ability if it is immune to being charmed.")

    npc.actions.append("***Occluded Mind (2 psi).*** You target one creature you can communicate with via telepathy. The target must make an Intelligence saving throw. On a failed save, the target believes one statement of your choice for the next 5 minutes that you communicate to it via telepathy. The statement can be up to ten words long, and it must describe you or a creature or an object the target can see. On a successful save, the target is unaffected, and you can't use this ability on it again until you finish a long rest. A creature is immune to this ability if it is immune to being charmed.")

    npc.actions.append("***Broken Will (5 psi).*** You target one creature you can communicate with via telepathy. The target must make an Intelligence saving throw. On a failed save, you choose the target's movement and action on its next turn. On a successful save, the target is unaffected, and you can't use this ability on it again until you finish a long rest. A creature is immune to this ability if it is immune to being charmed.")

    npc.actions.append("***Psychic Grip (6 psi; concentration, 1 min.).*** You target one creature you can see within 60 feet of you. The target must succeed on an Intelligence saving throw, or it is paralyzed until your concentration ends. At the end of each of its turns, it can repeat the saving throw. On a success, this effect ends. On a failure, you can use your reaction to force the target to move up to half its speed, even though it's paralyzed.")

    npc.actions.append("***Psychic Domination (7 psi; concentration, 1 min.).*** You target one creature you can see within 60 feet of you. The target must succeed on an Intelligence saving throw, or you choose the creature's actions and movement on its turns until your concentration ends. At the end of each of its turns, it can repeat the saving throw, ending the effect on itself on a success. A creature is immune to this ability if it is immune to being charmed.")

awakeneddisciplines = {
    'Aura Sight': aurasight,
    'Intellect Fortress': intellectfortress,
    'Mantle of Awe': mantleofawe,
    'Precognition': precognition,
    'Psychic Assault': psychicassault,
    'Psychic Disruption': psychicdisruption,
    'Psychic Inquisition': psychicinquisition,
    'Psychic Phantoms': psychicphantoms,
    'Telepathic Contact': telepathiccontact
}
for ad in awakeneddisciplines:
    allclasses['Mystic'].disciplines[ad] = awakeneddisciplines[ad]
```
