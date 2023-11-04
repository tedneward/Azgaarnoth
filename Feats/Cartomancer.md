## Cartomancer
*Prerequisite: 4th Level; [Sorcerer](../Classes/Sorcerer.md), [Warlock](../Classes/Warlock.md), or [Wizard](../Classes/Wizard.md) Class*

You have learned to channel your magic through a deck of playing cards, granting you these benefits:

* **Card Focus.** You can use a deck of cards as your spellcasting focus. When you use the deck as a focus to cast a spell that deals damage, roll a d4. You gain a bonus to one damage roll of the spell equal to the number rolled. This bonus applies to one creature of your choice that you can see damaged by the spell; you can use this benefit a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.
* **Card Tricks.** You learn the [prestidigitation](../Magic/Spells/prestidigitation.md) cantrip and can use it to create illusions that duplicate the effects of stage magic. When you use [prestidigitation](../Magic/Spells/prestidigitation.md) in this way, you can conceal the verbal and somatic components of the spell as mundane conversation and card-handling.
* **Hidden Ace.** When you finish a long rest, you can choose one spell you know and imbue it into a card; the chosen spell must have a casting time of 1 action, and its level must be less than or equal to your proficiency bonus. While the card is imbued with the spell, you can use your bonus action to flourish the card and cast the spell within. The card then immediately loses its magic.

```
name = 'Cartomancer'
description = "***Feat: Cartomancer.*** You have learned to channel your magic through a deck of playing cards."
def prereq(npc):
    return npc.levels() > 4 and (
        npc.levels('Sorcerer') > 0 or
        npc.levels('Warlock') > 0 or
        npc.levels('Wizard') > 0
    )
def apply(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Card Focus ({npc.proficiencybonus()}/Recharges on long rest).*** You can use a deck of cards as your spellcasting focus. When you use the deck as a focus to cast a spell that deals damage, roll a d4. You gain a bonus to one damage roll of the spell equal to the number rolled. This bonus applies to one creature of your choice that you can see damaged by the spell.") )
    npc.traits.append(f"***Card Tricks.*** You know the {spelllinkify('prestidigitation')} cantrip and can use it to create illusions that duplicate the effects of stage magic. When you do this, you can conceal the verbal and somatic component of the spell as mundane conversation and card-handling.")
    npc.defer(lambda npc: npc.traits.append("***Ace Preparation.*** When you finish a long rest, you can choose one spell you know and imbue it into a card for use with your Hidden Ace feature; the chosen spell must have a casting time of 1 action, and its level must be {npc.proficiencybonus()} or less.") )
    npc.bonusactions.append("***Hidden Ace.*** You flourish the card prepared by your Ace Preparation and cast the spell within. The card then immediately loses its magic.")
```
