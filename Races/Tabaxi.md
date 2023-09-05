# [Tabaxi](../Creatures/Tabaxi.md)

***Tabaxi Traits.*** Your tabaxi character has the following racial traits.

* **Ability Score Increase.** Your Dexterity score increases by 2, and your Charisma score increases by 1.

* **Age.** Tabaxi have lifespans equivalent to humans.

* **Size.** Tabaxi are taller on average than humans and relatively slender. Your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Darkvision.** You have a cat’s keen senses, especially in the dark. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

* **Feline Agility.** Your reflexes and agility allow you to move with a burst of speed. When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can’t use it again until you move 0 feet on one of your turns.

* **Cat’s Claws.** Because of your claws, you have a climbing speed of 20 feet. In addition, your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

* **Cat’s Talent.** You have proficiency in the Perception and Stealth skills.

* **Languages.** You can speak, read, and write Common and one other language of your choice.

```
name = 'Tabaxi'
type = 'humanoid'
def level0(npc):
    npc.description.append("***Race: Tabaxi.*** Meow.")

    npc.DEX += 2
    npc.CHA += 1

    npc.size = 'Medium'
    npc.speed['walking'] = 30
    npc.speed['climbing'] = 20

    npc.senses['darkvision'] = 60

    npc.actions.append("***Feline Agility.*** When you move on your turn in combat, you can double your speed until the end of the turn. Once you use this trait, you can’t use it again until you move 0 feet on one of your turns.")

    npc.defer(npc.actions.append(f"***Claws.*** Melee Weapon... 1d4 + {npc.STRbonus()} slashing damage"))

    npc.skills.append('Perception')
    npc.skills.append('Stealth')

    npc.languages.append('Common')
    npc.languages.append('CHOOSE')
```

## Tabaxi Personality
A tabaxi might have motivations and quirks much different from a dwarf or an elf with a similar background. You can use the following tables to customize your character in addition to the trait, ideal, bond, and flaw from your background.

The Tabaxi Obsession table can help hone your character’s goals. For extra fun, roll a new result every few days that pass in the campaign to reflect your ever-changing curiosity.

**Tabaxi Obsessions**

d8 | My curiosity is currently fixed on ...
-- | --------------------------------------
1 | A god or planar entity
2 | A monster
3 | A lost civilization
4 | A wizard’s secrets
5 | A mundane item
6 | A magic item
7 | A location
8 | A legend or tale

**Tabaxi Quirks**

d10	| Quirk
--- | ----
1 | You miss your tropical home and complain endlessly about the freezing weather, even in summer.
2 | You never wear the same outfit twice, unless you absolutely must.
3 | You have a minor phobia of water and hate getting wet.
4 | Your tail always betrays your inner thoughts.
5 | You purr loudly when you are happy.
6 | You keep a small ball of yarn in your hand, which you constantly fidget with.
7 | You are always in debt, since you spend your gold on lavish parties and gifts for friends.
8 | When talking about something you’re obsessed with, you speak quickly and never pause and others can’t understand you.
9 | You are a font of random trivia from the lore and stories you have discovered.
10 | You can’t help but pocket interesting objects you come across.
