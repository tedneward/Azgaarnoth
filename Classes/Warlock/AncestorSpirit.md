# Otherworldly Patron: Ancestor Spirit
Your patron is an undead spirit (or collection thereof) that refuses to pass on from the material plane. In most cases, spirits that take an interest in the living to this extent are related to their scions, hence the coining of the term ancestor spirit to describe this relationship. Often ascribed prophetic abilities, many cultures engage in ancestor worship in the hope of attracting the attention of their long-dead relative(s). Your ancestor spirits might vary from culture to culture as screaming banshees, frightening ghosts, or mischievous poltergeists.

```
name = 'Ancestor Spirit'
description = "***Otherworldly Patron: Ancestor Spirit.*** Your patron is an undead spirit (or collection thereof) that refuses to pass on from the material plane. In most cases, spirits that take an interest in the living to this extent are related to their scions, hence the coining of the term ancestor spirit to describe this relationship. Often ascribed prophetic abilities, many cultures engage in ancestor worship in the hope of attracting the attention of their long-dead relative(s). Your ancestor spirits might vary from culture to culture as screaming banshees, frightening ghosts, or mischievous poltergeists."
```

## Expanded Spell List
The Ancestor lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock list for you.

Spell Level | Spells
----------- | ----------
1st | [unseen servant](../../Magic/Spells/unseen-servant.md), [detect evil and good](../../Magic/Spells/detect-evil-and-good.md)
2nd | [augury](../../Magic/Spells/augury.md), [see invisibility](../../Magic/Spells/see-invisibility.md)
3rd | [speak with dead](../../Magic/Spells/speak-with-dead.md), [spirit guardians](../../Magic/Spells/spirit-guardians.md)
4th | [divination](../../Magic/Spells/divination.md), [guardian of faith](../../Magic/Spells/guardian-of-faith.md)
5th | [legend lore](../../Magic/Spells/legend-lore.md), [raise dead](../../Magic/Spells/raise-dead.md)

## Voice of the Oracle
*1st-level Ancestor Spirit feature*

You may spend a bonus action to call on your ancestors, augmenting your presence with their wisdom and authority. When you activate this ability, choose Persuasion, Deception or Intimidation. For the next minute, skill checks you make of the chosen kind are made at advantage. During this time, your eyes roll back into your head, and your voice is echoed by a whispering chorus audible out to 10 feet from you. You must finish a short or long rest before using this ability again.

```
def level1(npc):
    npc.bonusactions.append("***Voice of the Oracle (Recharges on short or long rest).*** You call on your ancestors, augmenting your presence with their wisdom and authority. When you activate this ability, choose Persuasion, Deception or Intimidation. For the next minute, skill checks you make of the chosen kind are made at advantage. During this time, your eyes roll back into your head, and your voice is echoed by a whispering chorus audible out to 10 feet from you.")
```

## Bonus Cantrip
*1st-level Ancestor Spirit feature*

You gain the [guidance](../../Magic/Spells/guidance.md) and [message](../../Magic/Spells/message.md) cantrips. They count as warlock cantrips for you, but they don't count against your number of cantrips known.

```
    npc.pactmagic.cantripsknown.append('guidance')
    npc.pactmagic.cantripsknown.append('message')
```

## Prescience
*6th-level Ancestor Spirit feature*

Your ancestors watch for danger on your behalf. If you would be surprised, you can spend your reaction before initiative is rolled to warn everyone nearby in a rousing cry. Anyone within 30 feet that can hear your words is no longer surprised. You must finish a short or long rest before using this ability again.

```
def level6(npc):
    npc.reactions.append("***Prescience (Recharges on short or long rest).*** If you would be surprised, before initiative is rolled you warn everyone nearby in a rousing cry. Anyone within 30 feet that can hear your words is no longer surprised. You must finish a short or long rest before using this ability again.")
```

## The Second Sight
*10th-level Ancestor Spirit feature*

Your patron opens your eyes to the spiritual demimonde. You can see into the Ethereal plane out to 60 feet, and can see invisible creatures.

```
def level10(npc):
    npc.senses['Ethereal'] = 60
    npc.traits.append("***Second Sight.*** You can see into the Ethereal plane out to 60 feet, and can see invisible creatures.")
```

## Supernatural Intuition
*14th-level Ancestor Spirit feature*

Your ancestors bring their centuries of prior experience to bear scrutinising your fledgling predictions. If a divination spell would provide false information, either to the intrinsic nature of the spell, or a masking effect such as Nystul's Magic Aura, you become aware that the result is false, though not necessarily why.

> **Boons**
> The Ancestor is likely to bestow a pact boon upon the warlock that had a significance to them in life. They might give a warlock their own spellbook written in a cramped hand, or the same familiar which served them during their time with the living. For a more morbid tone, consider sending Pact of the Chain warlocks a crawling claw familiar from the ancestor's corpse.

```
def level14(npc):
    npc.traits.append("***Supernatural Intuition.*** Your ancestors bring their centuries of prior experience to bear scrutinising your fledgling predictions. If a divination spell would provide false information, either to the intrinsic nature of the spell, or a masking effect such as Nystul's Magic Aura, you become aware that the result is false, though not necessarily why.")
```
