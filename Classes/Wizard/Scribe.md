# Arcane Tradition: Scribe
Magic of the book--that's what many spellcasters call wizardry. The name is apt, given how much time wizards spend poring over their spellbooks, penning theories about the nature of magic, and exploring the farthest recesses of libraries. It's rare to see a wizard traveling without books and scrolls sprouting from their bags, and a wizard would go to great lengths to plumb an archive of ancient knowledge.

Among wizards, the Scriveners school is the most bookish. Its primary mission: recording discoveries (particularly those magical in nature) in tomes and scrolls so that wizardry can flourish. And while every wizard values their spellbook, a Scrivener dedicates themself to magically awakening their book, turning it into a trusted companion. All wizards study their spellbooks, but a scribe talks to theirs.

```
name = 'Scribe'
description = "***Arcane Tradition: Scribe.*** Among wizards, the Scriveners school is the most bookish. Its primary mission: recording discoveries (particularly those magical in nature) in tomes and scrolls so that wizardry can flourish. And while every wizard values their spellbook, a Scrivener dedicates themself to magically awakening their book, turning it into a trusted companion. All wizards study their spellbooks, but a scribe talks to theirs."
```

## Wizardly Quill
*2nd-level Order of Scribes feature*

As a bonus action, you can magically create a Tiny quill in your free hand. The magic quill has the following properties:

* The quill doesn't require ink. When you write with it, it produces ink in a color of your choice on the writing surface.
* The gold and time you must spend to copy a spell into your spellbook are halved if you use the quill for the transcription.
* You can erase anything you write with the quill if you wave the feather over the text as a bonus action, provided the text is within 5 feet of you.

This quill disappears if you create another one or if you die.

```
def level2(npc):
    npc.bonusactions.append("***Wizardly Quill.*** You magically create a Tiny quill in your free hand. The quill doesn't require ink. When you write with it, it produces ink in a color of your choice on the writing surface. The gold and time you must spend to copy a spell into your spellbook are halved if you use the quill for the transcription. You can erase anything you write with the quill if you wave the feather over the text as a bonus action, provided the text is within 5 feet of you. This quill disappears if you create another one or if you die.")
```

## Awakened Spellbook
*2nd-level Order of Scribes feature*

Using specially prepared inks and ancient incantations passed down by your wizardly order, you have awakened an arcane sentience within your spellbook.

While you are holding the book, it grants you the following benefits:

* You can use the book as a spellcasting focus for your wizard spells.
* When you cast a wizard spell with a spell slot, you can temporarily replace its damage type with the damage type of another spell in your spellbook, as your spellbook magically alters the spell's formula for this casting.
* When you cast a wizard spell as a ritual, you can use the spell's normal casting time, rather than adding 10 minutes to it. Once you use this benefit, you can't do so again until you finish a long rest.

If necessary, you can replace the book over the course of a short rest by using your Wizardly Quill to write arcane sigils in a blank book or a magic spellbook to which you're attuned. At the end of the rest, your spellbook's consciousness is summoned into the new book, which the consciousness transforms into your spellbook, along with all its spells. If the previous book still existed somewhere, all the spells vanish from its pages.

```
    npc.equipment.append("***Awakened Spellbook.*** You have awakened arcane sentience within your spellbook. If necessary, you can replace the book over the course of a short rest by using your Wizardly Quill to write arcane sigils in a blank book or a magic spellbook to which you're attuned. At the end of the rest, your spellbook's consciousness is summoned into the new book, which the consciousness transforms into your spellbook, along with all its spells. If the previous book still existed somewhere, all the spells vanish from its pages.")
    npc.traits.append("***Awakened Spellbook.*** While you are holding your Awakened Spellbook, you can use the book as a spellcasting focus for your wizard spells. When you cast a wizard spell with a spell slot, you can temporarily replace its damage type with the damage type of another spell in your spellbook, as your spellbook magically alters the spell's formula for this casting. When you cast a wizard spell as a ritual, you can use the spell's normal casting time, rather than adding 10 minutes to it. Once you use this benefit, you can't do so again until you finish a long rest.")
```

## Master Scrivener
*6th-level Order of Scribes feature*

Whenever you finish a long rest, you can create one magic scroll by touching your Wizardly Quill to a blank piece of paper or parchment and causing one spell from your Awakened Spellbook to be copied onto the scroll. The spellbook must be within 5 feet of you when you make the scroll.

The chosen spell must be of 1st or 2nd level and must have a casting time of 1 action. Once in the scroll, the spell's power is enhanced, counting as one level higher than normal. You can cast the spell from the scroll by reading it as an action. The scroll is unintelligible to anyone else, and the spell vanishes from the scroll when you cast it or when you finish your next long rest.

You are also adept at crafting spell scrolls, which are described in chapter 7 of the Dungeon Master's Guide. The gold and time you must spend to make such a scroll are halved if you use your Wizardly Quill.

```
def level6(npc):
    npc.traits.append("***Master Scrivener.*** Whenever you finish a long rest, you can create one magic scroll by touching your Wizardly Quill to a blank piece of paper or parchment and causing one spell from your Awakened Spellbook to be copied onto the scroll. The spellbook must be within 5 feet of you when you make the scroll. The chosen spell must be of 1st or 2nd level and must have a casting time of 1 action. Once in the scroll, the spell's power is enhanced, counting as one level higher than normal. You can cast the spell from the scroll by reading it as an action. The scroll is unintelligible to anyone else, and the spell vanishes from the scroll when you cast it or when you finish your next long rest. You are also adept at crafting spell scrolls. The gold and time you must spend to make such a scroll are halved if you use your Wizardly Quill.")
```

## Manifest Mind
*10th-level Order of Scribes feature*

You are now able to conjure forth the mind of your Awakened Spellbook. As a bonus action while the book is on your person, you can cause the mind to manifest as a Tiny spectral construct, hovering in an unoccupied space of your choice within 60 feet of you. This presence is intangible and doesn't occupy its space, and it sheds dim light in a 10-foot radius. It looks like a ghostly tome, a cascade of text, or a scholar from the past (your choice). The spectral mind has a number of hit points equal to your wizard level plus your Intelligence modifier, and it uses your Armor Class and saving throw modifiers.

While manifested, the spectral mind can hear and see, and it has darkvision with a range of 60 feet. As an action, you can hear and see using the its senses, instead of your own, until your concentration ends (as if concentrating on a spell).

Whenever you cast a wizard spell on your turn, you can cast it as if you were in the spectral mind's space, instead of your own, using its senses. You can do so a number of times per day equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

As a bonus action, you can cause the spectral mind to hover up to 30 feet to an unoccupied space that you or it can see. It can pass through creatures but not objects. The spectral mind stops manifesting if it is ever more than 300 feet away from you, if it drops to 0 hit points, if you die, or if you dismiss it as a bonus action.

```
def level10(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Manifest Mind.*** While the book is on your person, you can cause the mind to manifest as a Tiny spectral construct, hovering in an unoccupied space of your choice within 60 feet of you. This presence is intangible and doesn't occupy its space, and it sheds dim light in a 10-foot radius. It looks like a ghostly tome, a cascade of text, or a scholar from the past (your choice). The spectral mind has {npc.levels('Wizard') + npc.INTbonus()} hit points, and it uses your Armor Class and saving throw modifiers. While manifested, the spectral mind can hear and see, and it has darkvision with a range of 60 feet.") )

    npc.actions.append("***Manifest Mind: Remote View.*** While your spellbook's spectral mind is manifested, you can hear and see using the its senses, instead of your own, until your concentration ends (as if concentrating on a spell).")
    
    npc.defer(lambda npc: npc.traits.append(f"***Manifest Mind: Remote Cast ({npc.proficiencybonus()}/Recharges on long rest).*** Whenever you cast a wizard spell on your turn, you can cast it as if you were in your spellbook's manifested spectral mind's space, instead of your own, using its senses. You can do so a number of times per day equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.") )
```

## One with the Word
*14th-level Order of Scribes feature*

Your connection to your Awakened Spellbook has become so profound that your soul has become entwined with it. While you are holding the book and its spectral mind is manifest, you can take an action to cause the two of you to teleport, swapping places. You can teleport in this way a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

Moreover, if you die but at least one spell remains in your Awakened Spellbook, you can return to life 1 minute later within 5 feet of the book. You revive with 1 hit point. Then roll 3d6. The book loses spells of your choice that have a combined spell level equal to that roll or higher. For example, if the roll's total is 9, spells vanish from the book that have a combined level of at least 9, which could mean one 9th-level spell, three 3rd-level spells, or some other combination.

Thereafter, you are incapable of casting the lost spells, even if you find them on a scroll or in another spellbook. The only way to restore your ability to cast one of the lost spells is through the [wish](../../Magic/Spells/wish.md) spell, which can restore one spell to the book per casting.

```
def level14(npc):
    npc.defer(lambda npc: npc.actions.append(f"***One with the Word ({npc.proficiencybonus()}/Recharges on long rest).*** While you are holding the book and its spectral mind is manifest, you cause the two of you to teleport, swapping places. Moreover, if you die but at least one spell remains in your Awakened Spellbook, you can return to life 1 minute later within 5 feet of the book. You revive with 1 hit point. Then roll 3d6. The book loses spells of your choice that have a combined spell level equal to that roll or higher. Thereafter, you are incapable of casting the lost spells, even if you find them on a scroll or in another spellbook. The only way to restore your ability to cast one of the lost spells is through the {spelllinkify('wish')} spell, which can restore one spell to the book per casting.") )
```
