# Roguish Archetype: Mastermind
Your focus is on people and on the influence and secrets they have. Many spies, courtiers, and schemers follow this archetype, leading lives of intrigue. Words are your weapons as often as knives or poison, and secrets and favors are some of your favorite treasures.

```
name = 'Mastermind'
description = "***Roguish Archetype: Mastermind.*** Your focus is on people and on the influence and secrets they have. Many spies, courtiers, and schemers follow this archetype, leading lives of intrigue. Words are your weapons as often as knives or poison, and secrets and favors are some of your favorite treasures."
```

## Master of Intrigue
*3rd-level Mastermind feature* 

You gain proficiency with the disguise kit, the forgery kit, and one gaming set of your choice. You also learn two languages of your choice.

Additionally, you can unerringly mimic the speech patterns and accent of a creature that you hear speak for at least 1 minute, enabling you to pass yourself off as a native speaker of a particular land, provided that you know the language.

```
def level3(npc):
    npc.proficiencies.append("Disguise kit")
    npc.proficiencies.append("Forgery kit")
    npc.proficiencies.append("CHOOSE-One gaming set")
    npc.languages.append("CHOOSE")
    npc.languages.append("CHOOSE")
    npc.traits.append("***Master of Intrigue.*** You can unerringly mimic the speech patterns and accent of a creature that you hear speak for at least 1 minute, enabling you to pass yourself off as a native speaker of a particular land, provided that you know the language.")
```

## Master of Tactics
*3rd-level Mastermind feature* 

You can use the Help action as a bonus action. Additionally, when you use the Help action to aid an ally in attacking a creature, the target of that attack can be within 30 feet of you, rather than 5 feet of you, if the target can see or hear you.

```
    npc.bonusactions.append("***Help.*** You can perform the Help action. Additionally, when you do this to aid an ally in attacking a creature, the target of that attack can be within 30 feet of you, rather than 5 feet of you, if the target can see or hear you.")
```

## Insightful Manipulator
*9th-level Mastermind feature* 

If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice:

* Intelligence score
* Wisdom score
* Charisma score
* Class levels (if any)

At the DM's option, you might also realize you know a piece of the creature's history or one of its personality traits, if it has any.

```
def level9(npc):
    npc.traits.append("***Insightful Manipulator.*** If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Intelligence score; Wisdom score; Charisma score; Class levels (if any). At the DM's option, you might also realize you know a piece of the creature's history or one of its personality traits, if it has any.")
```

## Misdirection
*13th-level Mastermind feature* 

You can sometimes cause another creature to suffer an attack meant for you. When you are targeted by an attack while a creature within 5 feet of you is granting you cover against that attack, you can use your reaction to have the attack target that creature instead of you.

```
def level13(npc):
    npc.reactions.append("***Misdirection.*** When you are targeted by an attack while a creature within 5 feet of you is granting you cover against that attack, you can use your reaction to have the attack target that creature instead of you.")
```

## Soul of Deceit
*17th-level Mastermind feature* 

Your thoughts can't be read by telepathy or other means, unless you allow it. You can present false thoughts by making a Charisma (Deception) check contested by the mind reader's Wisdom (Insight) check.

Additionally, no matter what you say, magic that would determine if you are telling the truth indicates you are being truthful if you so choose, and you can't be compelled to tell the truth by magic.

```
def level17(npc):
    npc.traits.append("***Soul of Deceit.*** Your thoughts can't be read by telepathy or other means, unless you allow it. You can present false thoughts by making a Charisma (Deception) check contested by the mind reader's Wisdom (Insight) check. Additionally, no matter what you say, magic that would determine if you are telling the truth indicates you are being truthful if you so choose, and you can't be compelled to tell the truth by magic.")
```
