# Divine Domain: Cat
The [deity of the tabaxi](../../Religions/Pantheon/CatLord.md) is a fickle entity, as befits the patron of cats. The tabaxi believe that the Cat Lord wanders the world, watching over them and intervening in their affairs as needed. The tabaxi value knowledge above all other currency. This otherwise serious pursuit is tempered by their playful curiosity and molded by their tendency to switch obsessions unexpectedly, without warning. Clerics of the Cat Lord are rare and are typically mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They are equally likely to be by your side up until the moment trouble begins as scoundrels, gamblers, rebels, and liberators. Their clerics are a disruptive force in the world, puncturing pride, mocking tyrants, stealing from the rich, freeing captives, and flouting hollow traditions. 

Clerics of the Cat Domain are almost exclusively found within the tribes of the exotic cat-like Tabaxi. These Clerics are extremely rare and are in very high standing within the Tabaxi culture and they serve as spiritual leaders but also as fearsome defenders of the land. Contrary to the heavily armored clerics of other domains, Cat Domain Clerics either wear light armor or no armor at all,  counting instead on the blessings of the Cat Lord to protect them. These Clerics almost never use a shield, instead preferring to use light weapons to remain mobile.

```
name = 'Cat'
description = "***Divine Domain: Cat.*** Clerics of the Cat Lord are rare and are typically mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They are equally likely to be by your side up until the moment trouble begins as scoundrels, gamblers, rebels, and liberators. Their clerics are a disruptive force in the world, puncturing pride, mocking tyrants, stealing from the rich, freeing captives, and flouting hollow traditions."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Cat Lord Domain Spells table. See the Divine Domain class feature for how domain spells work. These spells represent your quest for knowledge and information as well as your penchant for causing mischief.

**Cat Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [identify](../../Magic/Spells/identify.md), [divine favor](../../Magic/Spells/divine-favor.md)
3rd	| [pass without trace](../../Magic/Spells/pass-without-trace.md), [augury](../../Magic/Spells/augury.md)
5th	| [dispel magic](../../Magic/Spells/dispel-magic.md), [nondetection](../../Magic/Spells/nondetection.md)
7th	| [dimension door](../../Magic/Spells/dimension-door.md), [confusion](../../Magic/Spells/confusion.md)
9th	| [modify memory](../../Magic/Spells/modify-memory.md), [legend lore](../../Magic/Spells/legend-lore.md)

```
domainspells = {
    1: ['identify', 'divine favor'],
    3: ['pass without trace', 'augury'],
    5: ['dispel magic', 'nondetection'],
    7: ['dimension door', 'confusion'],
    9: ['modify memory', 'legend lore']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(spellcasting.casterclass) >= 1: results += domainspells[1]
        if npc.levels(spellcasting.casterclass) >= 3: results += domainspells[3]
        if npc.levels(spellcasting.casterclass) >= 5: results += domainspells[5]
        if npc.levels(spellcasting.casterclass) >= 7: results += domainspells[7]
        if npc.levels(spellcasting.casterclass) >= 9: results += domainspells[9]
        spellcasting.spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```

## Driven By Curiosity
*1st-level Cat Domain feature*

Your training and travelling have taught you two languages of your choice. You also become proficient in your choice of two of the following skills: Arcana, History, Nature, or Religion.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills.

```
    npc.languages.append("CHOOSE")
    npc.languages.append("CHOOSE")
    npc.expertises.append(choose("Choose an expertise: ", ['Arcana', 'History', 'Nature', 'Religion']))
    npc.expertises.append(choose("Choose an expertise: ", ['Arcana', 'History', 'Nature', 'Religion']))
```

## Channel Divinity: Underfoot
*2nd-level Cat Domain feature*

Starting at 2nd level, you can use your Channel Divinity to create an clowder of fey spirit cats.

As an action, you create a clowder (basically, a swarm) of illusory cats that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The clowder appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the clowder up to 30 feet to a space you can see, but it must remain within 120 feet of you.

For the duration, you can cast spells as though you were in the clowder's space, but you must use your own senses. Additionally, when both you and your clowder are within 5 feet of a creature that can see the illusion, the creature has disadvantage on attack rolls against you, due to the distraction of the clowder.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Underfoot.*** You create a clowder (basically, a swarm) of illusory cats that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The clowder appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the clowder up to 30 feet to a space you can see, but it must remain within 120 feet of you. For the duration, you can cast spells as though you were in the clowder's space, but you must use your own senses. Additionally, when both you and your clowder are within 5 feet of a creature that can see the illusion, the creature has disadvantage on attack rolls against you, due to the distraction of the clowder.{' If your clowder of illusory cats is within 5 feet of a creature that makes an attack roll against a target other than you, you may use your reaction to impose disadvantage on the roll. Also, if a creature is within 5 feet of your clowder and makes a saving throw, you may use your reaction to impose disadvantage on the roll.' if npc.levels('Cleric') >=6 else ''}") )
```

## Improved Under Foot
*6th-level Cat Domain feature*

Your clowder of illusory cats is even more Under Foot and troublesome.

If your clowder of illusory cats is within 5 feet of a creature that makes an attack roll against a target other than you, you may use your reaction to impose disadvantage on the roll. Also, if a creature is within 5 feet of your clowder and makes a saving throw, you may use your reaction to impose disadvantage on the roll.

## Divine Strike
*8th-level Cat Domain feature*

You gain the ability to infuse your weapon strikes with the merciless fury of the Cat Lord. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {1 if npc.levels('Cleric') < 14 else 2}d8 damage of the same type dealt by the weapon to the target.") )
```

## Spirit of the Cat Lord
*17th-level Cat Domain feature*

At 17th level you gain +2 to AC, +10 ft movement speed and a climb speed equal to your walking speed. You can take the dodge action as a bonus action. If you dodge an attack, you may use your reaction to move up to half of your speed without taking attacks of opportunity. Additionally, after a dodge, the attacking creature must make a Dexterity save or fall prone. The DC for this save is 8 + proficiency + Dex mod. You need to be wearing no or light armor to gain these benefits.

```
def level17(npc):
    npc.armorclass['Spirit of the Cat Lord'] = 2
    npc.speed['walking'] += 10
    npc.speed['climbing'] = npc.speed['walking']
    npc.defer(lambda npc: npc.bonusactions.append("***Spirit of the Cat Lord: Dodge.*** You take the Dodge action. After a dodge, the attacking creature must make a Dexterity save (DC {8 + npc.proficiencybonus() + npc.DEXbonus()} )or fall prone.") )
    npc.reactions.append("***Spirit of the Cat Lord: Scamper.*** If you dodge an attack, you may move up to half of your speed without taking attacks of opportunity. ")
    npc.traits.append("***Spirit of the Cat Lord.*** You need to be wearing no or light armor to gain these benefits.")
```
