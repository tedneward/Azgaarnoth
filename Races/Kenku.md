# [Kenku](../Creatures/Kenku.md)
Kenku adventurers are usually the survivors of a flock that has sustained heavy losses, or a rare kenku who has grown weary of a life of crime. These kenku are more ambitious and daring than their fellows. Others strike out on their own in search of the secrets of flight, to master magic, or to uncover the secret of their curse and find a method to break it.

Kenku adventurers, despite their relative independence, still have a tendency to seek out a companion to emulate and follow. A kenku loves to mimic the voice and words of its chosen companion.

> **ROLEPLAYING A KENKU**: If you’re playing a kenku, constant attempts to mimic noises can come across as confusing or irritating rather than entertaining. You can just as easily describe the sounds your character makes and what they mean. Be clear about your character’s intentions unless you’re deliberately aiming for inscrutable or mysterious.

> You might say, "Snapper makes the noise of a hammer slowly and rhythmically tapping a stone to show how bored he is. He plays with his dagger and studies the Lords’ Alliance agent sitting at the bar." Creating a vocabulary of noises for the other players to decode might sound like fun, but it can prove distracting and could slow down the game.

```
name = 'Kenku'
description = "***Race: Kenku.*** "
type = 'humanoid'
```

## Kenku Traits
Your kenku character has the following racial traits.

* **Ability Score Increase.** Your Dexterity score increases by 2, and your Wisdom score increases by 1.

* **Age.** Kenku have shorter lifespans than humans. They reach maturity at about 12 years old and can live to 60.

* **Size.** Kenku are around 5 feet tall and weigh between 90 and 120 pounds. Your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Expert Forgery.** You can duplicate other creatures’ handwriting and craftwork. You have advantage on all checks made to produce forgeries or duplicates of existing objects.

* **Kenku Training.** You are proficient in your choice of two of the following skills: Acrobatics, Deception, Stealth, and Sleight of Hand.

* **Mimicry.** You can mimic sounds you have heard, including voices. A creature that hears the sounds you make can tell they are imitations with a successful Wisdom (Insight) check opposed by your Charisma (Deception) check.

* **Languages.** You can read and write Common and Auran, but you can speak only by using your Mimicry trait.

```
def level0(npc):
    npc.DEX += 2
    npc.WIS += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.traits.append("***Expert Forgery.*** You can duplicate other creatures’ handwriting and craftwork. You have advantage on all checks made to produce forgeries or duplicates of existing objects.")

    npc.skills.append(choose("Choose a skill: ", ['Acrobatics', 'Deception', 'Stealth', 'Sleight of Hand']))
    npc.skills.append(choose("Choose a skill: ", ['Acrobatics', 'Deception', 'Stealth', 'Sleight of Hand']))

    npc.traits.append("***Mimicry.*** You can mimic sounds you have heard, including voices. A creature that hears the sounds you make can tell they are imitations with a successful Wisdom (Insight) check opposed by your Charisma (Deception) check.")

    npc.languages.append('Common')
    npc.languages.append('Auran')
```