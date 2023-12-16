# Bardic College: College of Secrets
There are many organizations that act in secrecy. From [Rogues' Guilds](../../Organizations/RoguesGuilds/) and spy rings to cults, rebellions and the [Order of the Copper Dragon](../../Organizations/MilitantOrders/DraconicOrder/Copper.md), all these secret societies need operatives and leaders like you. Your chosen group taught you the value of loyalty and secrecy, and how to command fear and respect, whether by magic or other means. The key to your success and survival is an unmatched understanding of the psychology and culture of those around you.

```
name = 'College of Secrets'
description = "***Bardic College: College of Secrets.*** There are many organizations that act in secrecy. All these secret societies need operatives and leaders like you. Your chosen group taught you the value of loyalty and secrecy, and how to command fear and respect, whether by magic or other means. The key to your success and survival is an unmatched understanding of the psychology and culture of those around you."
```

## Blood Initiation
*3rd-level College of Secrets feature*

You have been fully initiated as a member of your secret society, and you have been trained in all their mysterious ways. They in turn expect your loyalty and secrecy, but this gives you several benefits. You gain proficiency with your choice of one of the following skills: Deception, Intimidation, Performance, Persuasion, Sleight of Hand, or Stealth. You also gain proficiency with your choice of one of the following tools: disguise kit, forgery kit, poisoner's kit, or thieves' tools.

In addition, you can communicate wordlessly with any other member of your secret society who can see you. If you can see them, they can communicate back. This is not telepathy, but a combination of gesture and innuendo that no one outside of your group can perceive without some kind of magical insight.

```
def level3(npc):
    choice = choose("Choose one: ", ['Deception', 'Intimidation', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth'])
    npc.proficiencies.append(choice)
    choice = choose("Choose one: ", ["Disguise kit", "Forgery kit", "Poisoner's kit", "Thieves' tools"])
    npc.proficiencies.append(choice)
    npc.traits.append("***Blood Initiation.*** You can communicate wordlessly with any other member of your secret society who can see you. If you can see them, they can communicate back. This is not telepathy, but a combination of gesture and innuendo that no one outside of your group can perceive without some kind of magical insight.")
```

## Predatory Insight
*3rd-level College of Secrets feature*

You learn the [hunter's mark](../../Magic/Spells/hunters-mark.md) spell. You also learn the [vicious mockery](../../Magic/Spells/vicious-mockery.md) cantrip if you don't already know it. These do not count against the total number of spells or cantrips you can know as a bard. When an ally attacks a creature that is the subject of your hunter's mark, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and adding the result to the ally's attack roll. If the ally hits, they inflict additional damage equal to your Charisma modifier.

```
    npc.spellcasting['Bard'].cantripsknown.append('vicious mockery')
    npc.spellcasting['Bard'].spellsknown.append('hunters mark')
    npc.defer(lambda npc: npc.reactions.append("***Predatory Insight.*** When an ally attacks a creature that is the subject of your *hunter's mark*, you expand one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and adding the result to the ally's attack roll. If the ally hits, they inflict {npc.CHAbonus()} additional damage.") )
```

## Grim Mockery
*6th-level College of Secrets feature*

You can use what seems like gentle teasing, a polite word of caution, or even just a look to communicate a terrifying threat. When you cast the [vicious mockery](../../Magic/Spells/vicious-mockery.md) cantrip, you add your Charisma modifier to the damage roll. In addition, at 14th level, when you successfully strike an opponent with an attack, you can cast vicious mockery as a bonus action, targeting only the opponent you struck.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Grim Mockery.*** When you cast {spelllinkify('vicious mockery')}, you add {npc.CHAbonus()} to the damage roll") )
```

## Dangerous Secrets
*14th-level College of Secrets feature*

If you spend at least 1 minute observing or interacting with a creature outside combat, you can expend one of your uses of Bardic Inspiration to cast the detect thoughts spell on that creature while you are interacting with it without using a spell slot, as long as it is not hostile to you. When you cast detect thoughts in this way, if you choose to probe deeply into that creature's thoughts, you roll the Bardic Inspiration die you expended and subtract the result from the target's Wisdom saving throw roll. On a failed save, the target is not aware you are probing its mind.

In addition, when you roll an ability check or saving throw to resist any attempt to discern information about you, your plans, your location, or your thoughts, you have advantage on that roll. This includes effects that would read your thoughts or compel you to speak the truth. If you succeed on your roll, you can cast vicious mockery as a reaction, targeting the source of the attempt to discern the information.

```
def level14(npc):
    npc.bonusactions.append(f"***Grim Mockery.*** When you successfully strike an opponent with an attack, you cast {spelllinkify('vicious mockery')}, targeting only the opponent you struck.")

    npc.defer(lambda npc: npc.traits.append(f"***Dangerous Secrets.*** If you spend at least 1 minute observing or interacting with a creature outside combat, you can expend one of your uses of Bardic Inspiration to cast the {spelllinkify('detect thoughts')} spell on that creature while you are interacting with it without using a spell slot, as long as it is not hostile to you. When you cast *detect thoughts* in this way, if you choose to probe deeply into that creature's thoughts, you roll the Bardic Inspiration die you expended and subtract the result from the target's Wisdom saving throw roll. On a failed save, the target is not aware you are probing its mind. In addition, when you roll an ability check or saving throw to resist any attempt to discern information about you, your plans, your location, or your thoughts, you have advantage on that roll. This includes effects that would read your thoughts or compel you to speak the truth. If you succeed on your roll, you can cast {spelllinkify('vicious mockery')} as a reaction, targeting the source of the attempt to discern the information.") )
```
