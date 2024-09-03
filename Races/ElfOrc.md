# Elforc

> Few races share a hatred of each other like the orcs and elves. In many ways they are opposites. One beautiful, the other grotesque. One strong, and one agile. One intelligent, one that could not think its way out of a parchment satchel. The truth is this contempt runs deeper than their differences, their blood and their history. This is a hatred that weeps from their very gods, and any pitiful creature born of an unthinkable union between them is doomed to a life of anguish.

> — Professor R. Bennett, human sage

> That was true, eons ago. Today, elves and orcs find they have more in common than not. At least, my parents found that to be the case, anyway.

> — Professors Allustria Tusktooth

Strong, agile and utterly unpredictable, an elforc is formidable yet often despised by both their parent races. Some find acceptance from their parents; others find only rejection. Unlike other mixed-parentage individuals, however, the elforc bloodline breeds true, and some number of villages along the traditional Eldar/Hordish borders (Yithi and Al'Uma, for example) are home to non-trivial communities of these strangely alluring-yet-intimidating folk.

***Dexterous Yet Durable.*** Elforcs are blessed with the beauty of elves, marred only by hardy build, jutting jaws, and/or prominent teeth of their orcish parentage. Elforcs stand between 6 to 7 feet tall, some bearing a lean, bulky appearance, though others have slim builds with their natural muscle wrapped tightly beneath the flesh. Their skin tones tend to reflect that of their elven parent tinged with a grayish, dulling hint.

There is an almost elegant quality to their purposeful movements, reminiscent of lion or tiger--powerful, yet precise and fluid. Elforcs are not as strong as full orcs, nor as agile as pure elves. Instead they embody a near-perfect balance between might and speed. 

They are impulsive and erratic, making them all but impossible to anticipate in battle; a trait which earns the respect of some of their parent races, if not their acceptance.

***Turmoil Within.*** Like most mixed-genetic bloodlines, the elforcs are a people that not only struggle with others, but also conflict with themselves. The whispers of the orc god Gruumsh do not directly reach their minds, kept at bay by their fey ancestry, yet his influence still burns in each and every Elforc. It's this influence with amplifies their already chaotic tendencies, a gift also of their elf blood, and sees them act on instinct--unpredictable but often reckless, sometimes with little regard for law and order, depending on their upbringing.

Misunderstood by their parents and almost every other race, including other part-orc people, elforcs feel most at ease among tieflings who know what is to be scorned by the masses. Many elforcs find a home among the slums of human cities or wander the lands as lone drifters. Those who come to accept elforcs find them to be both capable and efficient, often employing them as personal bodyguards, lethal assassins, bounty hunters or shock troops.

***Ability Score Increase***. Your Strength, Dexterity and Constitution score each increases by 1.

***Age.*** Elforcs combine the strange mixture of maturing quickly and yet living long lives. They reach adulthood by the age of 15, yet can live up to 150 years.

***Alignment.*** Nearly all elforcs are wildly chaotic, inheriting traits of chaos from both sides of their parentage. Elforcs can be of any alignment but they are almost always conflicted, particularly if their orcish parent embraced the violent traditions of the Hordes.

***Size.*** Your size is Medium.

***Speed.*** You have a base walking speed of 30 feet.

***Languages.*** You can read, write, and speak Common, Elvish, and Orc.

## Traits

***Darkvision.*** Thanks to both your elf and orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

***Elven Gift.*** The type of elf your elforc is descended from will determine what they have inherited:

* [Bright](Elves/Bright.md): ***Ancient Magic.*** Choose one of the following cantrips: [light](../../Magic/Spells/light.md), [dancing lights](../../Magic/Spells/dancing-lights.md), or [thaumaturgy](../../Magic/Spells/thaumaturgy.md). You know that cantrip, and Charisma is your spellcasting ability for it.
* [Dark](Elves/Dark.md): ***Drow Magic.*** You know the [dancing lights](../../Magic/Spells/dancing-lights.md) cantrip. When you reach 3rd level, you can cast [Faerie Fire](../../Magic/Spells/faerie-fire.md) once, and it recharges after a long rest. When you reach 5th level, you can cast [Darkness](../../Magic/Spells/darkness.md) once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.
* [Fey](Elves/Fey.md): ***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest.
* [High](Elves/High.md): ***High Magic.*** You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.
* [Sea](Elves/Sea.md): ***Child of the Sea.*** You have a swimming speed of 30 feet, and you can breathe air and water.
* [Shadow](Elves/Shadow.md): ***Necrotic Resistance.*** You have resistance to necrotic damage.
* [Wild](Elves/Wild.md): ***Wild Cantrip.*** You know one cantrip of your choice from the druid spell list. Wisdom is your spellcasting ability for it.
* [Wood](Elves/Wood.md): ***Mask of the Wild.*** You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.

For reasons as yet unknown, the union of Winged Elves and Orcs cannot produce children.

***Fey Ancestry.*** You have advantage on saving throws against being charmed, and magic can't put you to sleep.

***Aggression.*** As a bonus action, you can move up to your speed toward an enemy of your choice that you can see or hear. You must end this move closer to the enemy than you started.

***Erratic Dodge.*** Thanks to the deep chaos of your heritage, no enemy can predict you. You may use your reaction to either give yourself advantage on a Dexterity saving throw, or force a creature to reroll an attack against you, taking the lowest of the two rolls for their attack. You can use this trait once per short or long rest.

```
name = 'Elforc'
description = "***Race: Elforc.*** You are a genetic mix of both your elvish and orcish parent, an alluring combination of strength and grace wrapped in an enigma."
type = 'humanoid'
def level0(npc):
    npc.size = 'Medium'

    npc.speed['walking'] = 30

    npc.STR += 1
    npc.DEX += 1
    npc.CON += 1

    npc.languages.append('Common')
    npc.languages.append('Elvish')
    npc.languages.append('Orcish')


```