# Roguish Archetype: Divine Agent
In secrecy and shadows, divine agents work to further the agendas of the gods. Although divine agents dedicate their service to a deity in a similar way to clerics, they are generally above many of the normal rules and conventions of the church. Usually, they answer only to their deity and use divine magic and blessings to augment their roguish skills.

```
name = 'Divine Agent'
description = "***Roguish Archetype: Divine Agent.*** In secrecy and shadows, divine agents work to further the agendas of the gods. Although divine agents dedicate their service to a deity in a similar way to clerics, they are generally above many of the normal rules and conventions of the church. Usually, they answer only to their deity and use divine magic and blessings to augment their roguish skills."
```

## Spellcasting
When you reach 3rd level, you gain the ability to cast spells from the cleric spell list.

**Cantrips.** You learn three cantrips: guidance and two other cantrips of your choice from the cleric spell list. At 10th level you learn another cantrip from the cleric spell list.

**Spell Slots.** The Divine Agent Spellcasting table shows how many spell slots you have to cast your spells of 1st-level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

**Spells Known of 1st-Level and Higher.** You know three 1st-level cleric spells of your choice, two of which must be from the abjuration and divination spells on the cleric spell list.

The Spells Known column of the Divine Agent Spellcasting table shows when you learn more cleric spells of 1st level or higher. Each of these spells must be an abjuration or divination spell of your choice and must be of a level for which you have spell slots. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic.

Whenever you gain a level in this class, you can replace one of the cleric spells you know with another spell of your choice from the cleric spell list. The new spell must be of a level for which you have spell slots, and it must be an abjuration or divination spell, unless you're replacing the spell you gained at 8th, 14th, or 20th level.

**Spellcasting Ability.** Wisdom is your spellcasting ability for your cleric spells, since you learn your spells through your intimate understanding of the divine. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

**Divine Agent Spellcasting**
Rogue Level | Cantrips Known | Spells Known | 1st|2nd|3rd|4th
------------|----------------|--------------|----|---|---|---
3rd|3|3|2|--|--|--
4th|3|4|3|--|--|--
5th|3|4|3|--|--|--
6th|3|4|3|--|--|--
7th|3|5|4|2|--|--
8th|3|6|4|2|--|--
9th|3|6|4|2|--|--
10th|4|7|4|3|--|--
11th|4|8|4|3|--|--
12th|4|8|4|3|--|--
13th|4|9|4|3|2|--
14th|4|10|4|3|2|--
15th|4|10|4|3|2|--
16th|4|11|4|3|3|--
17th|4|11|4|3|3|--
18th|4|11|4|3|3|--
19th|4|12|4|3|3|1
20th|4|13|4|3|3|1

```
def level3(npc):
    domain = choose("Choose a domain: ", classes['Cleric'].subclasses)
    dname = domain.name; domain.name = 'DivineAgent-' + dname

    spellcasting = npc.newspellcasting(name, 'WIS')
    spellcasting.casterclass = baseclass
    npc.spellcasting[name].cantripsknown.append("guidance")

    npc.spellcasting[name].maxcantripsknown = 3
    npc.spellcasting[name].maxspellsknown = 3
    npc.spellcasting[name].slottable = {
        3: [ 2 ], 
        4: [ 3 ],
        5: [ 3 ],
        6: [ 3 ],
        7: [ 4, 2 ],
        8: [ 4, 2 ],
        9: [ 4, 2 ],
        10: [ 4, 3 ] ,
        11: [ 4, 3 ],
        12: [ 4, 3 ],
        13: [ 4, 3, 2 ],
        14: [ 4, 3, 2 ],
        15: [ 4, 3, 2 ],
        16: [ 4, 3, 3 ],
        17: [ 4, 3, 3 ],
        18: [ 4, 3, 3 ],
        19: [ 4, 3, 3, 1 ],
        20: [ 4, 3, 3, 1 ]
    }

def level4(npc):
    npc.spellcasting[name].maxspellsknown = 4

def level7(npc):
    npc.spellcasting[name].maxspellsknown = 5

def level8(npc):
    npc.spellcasting[name].maxspellsknown = 6

def level10(npc):
    npc.spellcasting[name].maxcantripsknown = 4
    npc.spellcasting[name].maxspellsknown = 7

def level11(npc):
    npc.spellcasting[name].maxspellsknown = 8

def level13(npc):
    npc.spellcasting[name].maxspellsknown = 9

def level14(npc):
    npc.spellcasting[name].maxspellsknown = 10

def level16(npc):
    npc.spellcasting[name].maxspellsknown = 11

def level19(npc):
    npc.spellcasting[name].maxspellsknown = 12

def level14(npc):
    npc.spellcasting[name].maxspellsknown = 13
```

## Agent of the Divines
Starting at 3rd level, choose a domain from your chosen deity's list of eligible domains, you gain the 1st-level benefits of that domain as if you were a 1st-level cleric. However, you do not gain any armor proficiencies from this domain.

## Favor of the Gods
At 9th level, you gain the Lucky feat. If you already have the Lucky feat, you instead gain an additional two luck points.

## Divine Strike
Starting at 13th level, once on each of your turns when you hit a creature with a weapon attack you can cause the attack to deal an extra 2d6 radiant damage to the target.

## Vessel of the Many Forms
At 17th level, your deity has bestowed the power upon you to take many different faces and forms to assist you in doing their bidding. You can cast [alter self](../../Magic/Spells/alter-self.md) at will, without expending a spell slot.

For you, this spell does not require concentration and lasts until it is dispelled.
