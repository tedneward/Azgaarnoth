# Divine Domain: Knowledge
The gods of knowledge value learning and understanding. Some teach that knowledge is to be gathered and shared in libraries and universities, or promote the practical knowledge of craft and invention. Some deities hoard knowledge and keep its secrets to themselves. And some promise their followers that they will gain tremendous power if they unlock the secrets of the multiverse. Followers of these gods study esoteric lore, collect old tomes, delve into the secret places of the earth, and learn all they can. Some gods of knowledge promote the practical knowledge of craft and invention, including smith deities.

This is a domain granted by [the Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Azuth](../../Religions/Pantheon/Azuth.md), [Bahamut](../../Religions/Pantheon/Bahamut.md), [Gond](../../Religions/Pantheon/Gond.md), [Lugh](../../Religions/Pantheon/Lugh.md), [Onatar](../../Religions/Pantheon/Onatar.md), ... 

name = 'Knowledge'
description = "***Divine Domain: Knowledge.*** The gods of knowledge value learning and understanding. Some teach that knowledge is to be gathered and shared in libraries and universities, or promote the practical knowledge of craft and invention. Some deities hoard knowledge and keep its secrets to themselves. And some promise their followers that they will gain tremendous power if they unlock the secrets of the multiverse. Followers of these gods study esoteric lore, collect old tomes, delve into the secret places of the earth, and learn all they can. Some gods of knowledge promote the practical knowledge of craft and invention, including smith deities."

## Domain Spells
*1st-level Knowledge domain feature*

You gain domain spells at the cleric levels listed in the Unity Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Knowledge Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [command](../../Magic/Spells/command.md), [identify](../../Magic/Spells/identify.md)
3rd	| [augury](../../Magic/Spells/augury.md), [suggestion](../../Magic/Spells/suggestion.md)
5th	| [nondetection](../../Magic/Spells/nondetection.md), [speak with dead](../../Magic/Spells/speak-with-dead.md)
7th	| [arcane eye](../../Magic/Spells/arcane-eye.md), [confusion](../../Magic/Spells/confusion.md)
9th	| [legend lore](../../Magic/Spells/legend-lore.md), [scrying](../../Magic/Spells/scrying.md)

```
domainspells = {
    1: ['command', 'identify'],
    3: ['augury', 'suggestion'],
    5: ['nondetection', 'speak with dead'],
    7: ['arcane eye', 'confusion'],
    9: ['legend lore', 'scrying']
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

## Blessings of Knowledge
*1st-level Knowledge domain feature*

You learn two languages of your choice. You also become proficient in your choice of two of the following skills: Arcana, History, Nature, or Religion.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills.

```
    npc.languages.append("CHOOSE")
    npc.languages.append("CHOOSE")
    npc.expertises.append(choose("Choose a skill", ['Arcana', 'History', 'Nature', 'Religion']))
    npc.expertises.append(choose("Choose a skill", ['Arcana', 'History', 'Nature', 'Religion']))
```

## Channel Divinity: Knowledge of the Ages
*2nd-level Knowledge domain feature*

You can use your Channel Divinity to tap into a divine well of knowledge. As an action, you choose one skill or tool. For 10 minutes, you have proficiency with the chosen skill or tool.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Knowledge of the Ages.*** You choose one skill or tool. For 10 minutes, you have proficiency with the chosen skill or tool.")
```

## Channel Divinity: Read Thoughts
*6th-level Knowledge domain feature*

You can use your Channel Divinity to read a creature's thoughts. You can then use your access to the creature's mind to command it.

As an action, choose one creature that you can see within 60 feet of you. That creature must make a Wisdom saving throw. If the creature succeeds on the saving throw, you can't use this feature on it again until you finish a long rest.

If the creature fails its save, you can read its surface thoughts (those foremost in its mind, reflecting its current emotions and what it ie actively thinking about) when it is within 60 feet of you. This effect lasts for 1 minute.

During that time, you can use your action to end this effect and cast [suggestion](../../Magic/Spells/suggestion.md) on the creature without expending a spell slot. The target automatically fails its saving throw against the spell.

```
def level6(npc):
    npc.actions.append(f"***Channel Divinity: Read Thoughts (Recharges on long rest).*** Choose one creature that you can see within 60 feet of you. That creature must make a Wisdom saving throw. If the creature succeeds on the saving throw, you can't use this feature on it again until you finish a long rest. If the creature fails its save, you can read its surface thoughts (those foremost in its mind, reflecting its current emotions and what it ie actively thinking about) when it is within 60 feet of you. This effect lasts for 1 minute. During that time, you can use your action to end this effect and cast the {spelllinkify('suggestion')} spell on the creature without expending a spell slot. The target automatically fails its saving throw against the spell.")
```

## Potent Spellcasting
*8th-level Knowledge domain feature*

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Potent Spellcasting.*** You add {npc.WISbonus()} to the damage you deal with any cleric cantrip.") )
```

## Visions of the Past
*17th-level Knowledge domain feature*

You can call up visions of the past that relate to an object you hold or your immediate surroundings. You spend at least 1 minute in meditation and prayer, then receive dreamlike, shadowy glimpses of recent events. You can meditate in this way for a number of minutes equal to your Wisdom score and must maintain concentration during that time, as if you were casting a spell.

Once you use this feature, you can't use it again until you finish a short or long rest.

***Object Reading.*** Holding an object as you meditate, you can see visions of the object's previous owner. After meditating for 1 minute, you learn how the owner acquired and lost the object, as well as the most recent significant event involving the object and that owner. If the object was owned by another creature in the recent past (within a number of days equal to your Wisdom score), you can spend 1 additional minute for each owner to learn the same information about that creature.

***Area Reading.*** As you meditate, you see visions of recent events in your immediate vicinity (a room, street, tunnel, clearing, or the like, up to a 50-foot cube), going back a number of days equal to your Wisdom score. For each minute you meditate, you learn about one significant event, beginning with the most recent. Significant events typically involve powerful emotions, such as battles and betrayals, marriages and murders, births and funerals. However, they might also include more mundane events that are nevertheless important in your current situation.

```
def level17(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Visions of the Past (Recharges on short or long rest).*** You spend at least 1 minute in meditation and prayer, then receive dreamlike, shadowy glimpses of recent events. You can meditate in this way for {npc.WIS} minutes and must maintain concentration during that time, as if you were casting a spell. **Object Reading.** Holding an object as you meditate, you can see visions of the object's previous owner. After meditating for 1 minute, you learn how the owner acquired and lost the object, as well as the most recent significant event involving the object and that owner. If the object was owned by another creature in the recent past (within {npc.WIS} days), you can spend 1 additional minute for each owner to learn the same information about that creature. **Area Reading.** As you meditate, you see visions of recent events in your immediate vicinity (a room, street, tunnel, clearing, or the like, up to a 50-foot cube), going back {npc.WIS} days. For each minute you meditate, you learn about one significant event, beginning with the most recent. Significant events typically involve powerful emotions, such as battles and betrayals, marriages and murders, births and funerals. However, they might also include more mundane events that are nevertheless important in your current situation.") )
```
