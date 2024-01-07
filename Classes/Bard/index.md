# Bard
Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the magic they contain.

```
name = 'Bard'
description = "***Class: Bard.*** Whether scholar, skald, or scoundrel, a bard weaves magic through words and music to inspire allies, demoralize foes, manipulate minds, create illusions, and even heal wounds. The bard is a master of song, speech, and the magic they contain."
```

## Class Features
As a bard, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|Spells Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|------------|---|---|---|---|---|---|---|---|---|--------
 1st |+2|2| 4|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Bardic Inspiration](#bardic-inspiration) (d6)
 2nd |+2|2| 5|3|-|-|-|-|-|-|-|-|[Jack of All Trades](#jack-of-all-trades), [Song of Rest](#song-of-rest) (d6)
 3rd |+2|2| 6|4|2|-|-|-|-|-|-|-|[Bard College](#bard-college), [Expertise](#expertise)
 4th |+2|3| 7|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
 5th |+3|3| 8|4|3|2|-|-|-|-|-|-|[Bardic Inspiration](#bardic-inspiration) (d8), [Font of Inspiration](#font-of-inspiration)
 6th |+3|3| 9|4|3|3|-|-|-|-|-|-|[Countercharm](#countercharm), [Bard College](#bard-college) feature
 7th |+3|3|10|4|3|3|1|-|-|-|-|-|
 8th |+3|3|11|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
 9th |+4|3|12|4|3|3|3|1|-|-|-|-|[Song of Rest](#song-of-rest) (d8)
10th |+4|4|14|4|3|3|3|2|-|-|-|-|[Bardic Inspiration](#bardic-inspiration) (d10), [Expertise](#expertise), [Magical Secrets](#magical-secrets)
11th |+4|4|15|4|3|3|3|2|1|-|-|-|
12th |+4|4|15|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|4|16|4|3|3|3|2|1|1|-|-|[Song of Rest](#song-of-rest) (d10)
14th |+5|4|18|4|3|3|3|2|1|1|-|-|[Magical Secrets](#magical-secrets), [Bard College](#bard-college) feature
15th |+5|4|19|4|3|3|3|2|1|1|1|-|[Bardic Inspiration](#bardic-inspiration) (d12)
16th |+5|4|19|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|4|20|4|3|3|3|2|1|1|1|1|[Song of Rest](#song-of-rest) (d12)
18th |+6|4|22|4|3|3|3|3|1|1|1|1|[Magical Secrets](#magical-secrets)
19th |+6|4|22|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|4|22|4|3|3|3|3|2|2|1|1|[Superior Inspiration](#superior-inspiration)

### Hit Points
**Hit Dice**: 1d8 per bard level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per bard level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor

**Weapons**: Simple weapons, hand crossbows, longswords, rapiers, shortswords

**Tools**: Three musical instruments of your choice

**Saving Throws**: Dexterity, Charisma

**Skills**: Choose any three

```
def level1(npc):
    npc.savingthrows.append("DEX")
    npc.savingthrows.append("CHA")

    for arm in armor['light']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)
    npc.proficiencies.append('Hand crossbow')
    npc.proficiencies.append('Longsword')
    npc.proficiencies.append('Shortsword')
    npc.proficiencies.append('Rapier')

    npc.proficiencies.append(choose("Choose an instrument: ", tools['musical']))
    npc.proficiencies.append(choose("Choose an instrument: ", tools['musical']))
    npc.proficiencies.append(choose("Choose an instrument: ", tools['musical']))

    chooseskill(npc)
    chooseskill(npc)
    chooseskill(npc)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a rapier, (b) a longsword, or (c) any simple weapon
* (a) a diplomat's pack or (b) an entertainer's pack
* (a) a lute or (b) any other musical instrument
* Leather armor and a dagger

```
    npc.armorclass['Leather armor'] = 11
    npc.equipment.append("Rapier OR Longsword OR any simple weapon")
    npc.equipment.append("Dagger")
    npc.equipment.append("Diplomat's pack OR Entertainer's pack")
    npc.equipment.append("Lute OR other musical instrument")
```

## Spellcasting
*1st-level bard feature*

You have learned to untangle and reshape the fabric of reality in harmony with your wishes and music. Your spells are part of your vast repertoire, magic that you can tune to different situations.

### Cantrips
You know two cantrips of your choice from the bard spell list. You learn additional bard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Bard table.

### Spell Slots
The Bard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest. For example, if you know the 1st-level spell Cure Wounds and have a 1st-level and a 2nd-level spell slot available, you can cast Cure Wounds using either slot.

### Spells Known of 1st Level and Higher
You know four 1st-level spells of your choice from the bard spell list.

The Spells Known column of the Bard table shows when you learn more bard spells of your choice. Each of these spells must be of a level for which you have spell slots, as shown on the table. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the bard spells you know and replace it with another spell from the bard spell list, which also must be of a level for which you have spell slots.

### Spellcasting Ability
Charisma is your spellcasting ability for your bard spells. Your magic comes from the heart and soul you pour into the performance of your music or oration. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a bard spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier

**Spell attack modifier** = your proficiency bonus + your Charisma modifier

### Ritual Casting
You can cast any bard spell you know as a ritual if that spell has the ritual tag.

### Spellcasting Focus
You can use a musical instrument as a spellcasting focus for your bard spells.

### Spell Versatility
Whenever you finish a long rest, you can replace one spell you learned from this Spellcasting feature with another spell from the bard spell list. The new spell must be the same level as the spell you replace.

```
    sc = fullcaster(npc, 'CHA', 'Bard')
    sc.casterclass = allclasses['Bard']

    def spellcasting(npc): 
        npc.spellcasting[name].maxcantripsknown = 3 if npc.levels(name) < 4 else 4 if npc.levels(name) < 10 else 5
        match npc.levels(name):
            case 1: npc.spellcasting[name].spellsprepared = 4
            case 2: npc.spellcasting[name].spellsprepared = 5
            case 3: npc.spellcasting[name].spellsprepared = 6
            case 4: npc.spellcasting[name].spellsprepared = 7
            case 5: npc.spellcasting[name].spellsprepared = 8
            case 6: npc.spellcasting[name].spellsprepared = 9
            case 7: npc.spellcasting[name].spellsprepared = 10
            case 8: npc.spellcasting[name].spellsprepared = 11
            case 9: npc.spellcasting[name].spellsprepared = 12
            case 10: npc.spellcasting[name].spellsprepared = 14
            case 11 | 12: npc.spellcasting[name].spellsprepared = 15
            case 13: npc.spellcasting[name].spellsprepared = 16
            case 14: npc.spellcasting[name].spellsprepared = 18
            case 15: npc.spellcasting[name].spellsprepared = 19
            case 16 | 17: npc.spellcasting[name].spellsprepared = 20
            case 18 | 19 | 20: npc.spellcasting[name].spellsprepared = 22

        npc.spellcasting[name].spellsprepared += npc.WISbonus()

    npc.defer(lambda npc: spellcasting(npc))
```

## Bardic Inspiration
*1st-level bard feature*

You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one [Bardic Inspiration](#bardic-inspiration) die, a d6.

Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the [Bardic Inspiration](#bardic-inspiration) die, but must decide before the DM says whether the roll succeeds or fails. Once the [Bardic Inspiration](#bardic-inspiration) die is rolled, it is lost. A creature can have only one [Bardic Inspiration](#bardic-inspiration) die at a time.

If a creature has a [Bardic Inspiration](#bardic-inspiration) die from you and casts a spell, the creature can roll that die and add the number rolled to one damage or healing roll of the spell. The [Bardic Inspiration](#bardic-inspiration) die is then lost.

You can use this feature a number of times equal to your Charisma modifier (a minimum of once). You regain any expended uses when you finish a long rest.

Your [Bardic Inspiration](#bardic-inspiration) die changes when you reach certain levels in this class. The die becomes a d8 at 5th level, a d10 at 10th level, and a d12 at 15th level.

```
    def bardicdie(npc):
        npc.bardicinspirationdie = 6 if npc.levels('Bard') < 5 else 8 if npc.levels('Bard') < 10 else 10 if npc.levels('Bard') < 15 else 12

    npc.defer(lambda npc: bardicdie(npc) )
    npc.defer(lambda npc: npc.traits.append(f"***Bardic Inspiration ({npc.CHAbonus()} dice/Recharges on {'long' if npc.levels('Bard') < 5 else 'short or long'} rest).*** You can inspire others through stirring words or music."))
    npc.defer(lambda npc: npc.bonusactions.append(f"***Bardic Inspiration: Inspiration.*** Choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die (d{npc.bardicinspirationdie}).") )
```

## Magical Inspiration
*2nd-level bard feature*

If a creature has a [Bardic Inspiration](#bardic-inspiration) die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The [Bardic Inspiration](#bardic-inspiration) die is then lost.

```
def level2(npc):
    npc.traits.append("***Magical Inspiration.*** If a creature has a Bardic Inspiration die from you and casts a spell that restores hit points or deals damage, the creature can roll that die and choose a target affected by the spell. Add the number rolled as a bonus to the hit points regained or the damage dealt. The Bardic Inspiration die is then lost.")
```

## Jack of All Trades
*2nd-level bard feature*

You can add half your proficiency bonus, rounded down, to any ability check you make that doesn't already include your proficiency bonus.

```
    npc.defer(lambda npc: npc.traits.append(f"***Jack of All Trades.*** You can add {npc.proficiencybonus() // 2} to any ability check you make that doesn't already include your proficiency bonus.") )
```

## Song of Rest
*2nd-level bard feature*

You can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.

```
    npc.traits.append("***Song of Rest.*** If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra 1d6 hit points.")
```

## Bard College
*3rd-level bard feature*

You delve into the advanced techniques of a [bard college](#bard-college) of your choice:

* [Creation](Creation.md)
* [Dragonsong](Dragonsong.md)
* [Eloquence](Eloquence.md)
* [Glamour](Glamour.md)
* [Lore](Lore.md)
* [Ravens](Ravens.md)
* [Satire](Satire.md)
* [Secrets](Secrets.md)
* [Spirits](Spirits.md)
* [Swords](Swords.md)
* [Valor](Valor.md)
* [Whispers](Whispers.md)

Your choice grants you features at 3rd level and again at 6th and 14th level.

```
def level3(npc):
    (_, subclass) = choose("Choose a college: ", subclasses)
    npc.subclasses[allclasses['Bard']] = subclass
    npc.description.append(subclass.description)
```

## Expertise
*3rd-level bard feature*

Choose two of your skill proficiencies. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.

At 10th level, you can choose another two skill proficiencies to gain this benefit.

```
    npc.expertises.append(choose("Choose one of your skills: ", npc.skills) )
    npc.expertises.append(choose("Choose one of your skills: ", npc.skills) )
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Bardic Versatility
Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can do one of the following, representing a change in focus as you use your (#ability-score-improvement)skills and magic:

* Replace one of the skills you chose for the [Expertise](#expertise) feature with one of your other skill proficiencies that isn't benefiting from [Expertise](#expertise).
* Replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the bard spell list.

## Font of Inspiration
*5th-level bard feature*

Beginning when you reach 5th level, you regain all of your expended uses of [Bardic Inspiration](#bardic-inspiration) when you finish a short or long rest.

## Countercharm
*6th-level bard feature*

You gain the ability to use musical notes or words of power to disrupt mind-influencing effects. As an action, you can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).

```
def level6(npc):
    npc.actions.append("***Countercharm.*** You can start a performance that lasts until the end of your next turn. During that time, you and any friendly creatures within 30 feet of you have advantage on saving throws against being frightened or charmed. A creature must be able to hear you to gain this benefit. The performance ends early if you are incapacitated or silenced or if you voluntarily end it (no action required).")
```

## Magical Secrets
*10th-level bard feature*

You have plundered magical knowledge from a wide spectrum of disciplines. Choose two spells from any classes, including this one. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip.

The chosen spells count as bard spells for you and are included in the number in the Spells Known column of the Bard table.

You learn two additional spells from any class at 14th level and again at 18th level.

```
def level10(npc):
    npc.traits.append("***Magical Secrets.*** You have plundered magical knowledge from a wide spectrum of disciplines. Two of your known spells at 10th level, two more at 14th level, and two more at 18th level can be from any classes, including this one.")
```

## Superior Inspiration
At 20th level, when you roll initiative and have no uses of [Bardic Inspiration](#bardic-inspiration) left, you regain one use.

```
def level20(npc):
    npc.traits.append("***Superior Inspiration.*** When you roll initiative and have no uses of Bardic Inspiration left, you regain one use.")
```

---

# "Core" Bard Spells
The following spells listed are available to all bards throughout Azgaarnoth; this is not the complete list of all bard spells, however. Certain colleges may have additional spells that are only known to their members, and many bardic spells have been lost in the past. Bards can learn new spells by visiting foreign colleges to learn from bards who know the new spells, uncovering new books of bardic lore in ancient ruins, traveling with other bards of different backgrounds, or study with other arcane scholars and "re-develop" the bardic understanding of the new spell.

> ### GM Notes
> In other words, it's really the DM's choice about when, where, and how to add new spells to a bard's "known" list;  the bard may need to do some in-game activity or adventure to obtain them.

## Cantrips
* [dancing lights](../../Magic/Spells/dancing-lights.md)
* [light](../../Magic/Spells/light.md)
* [mage hand](../../Magic/Spells/mage-hand.md)
* [mending](../../Magic/Spells/mending.md)
* [message](../../Magic/Spells/message.md)
* [minor illusion](../../Magic/Spells/minor-illusion.md)
* [prestidigitation](../../Magic/Spells/prestidigitation.md)
* [true strike](../../Magic/Spells/true-strike.md)
* [vicious mockery](../../Magic/Spells/vicious-mockery.md)

## 1st Level
* [animal friendship](../../Magic/Spells/animal-friendship.md)
* [bane](../../Magic/Spells/bane.md)
* [charm person](../../Magic/Spells/charm-person.md)
* [comprehend languages](../../Magic/Spells/comprehend-languages.md)
* [cure wounds](../../Magic/Spells/cure-wounds.md)
* [detect magic](../../Magic/Spells/detect-magic.md)
* [disguise self](../../Magic/Spells/disguise-self.md)
* [faerie fire](../../Magic/Spells/faerie-fire.md)
* [feather fall](../../Magic/Spells/feather-fall.md)
* [healing word](../../Magic/Spells/healing-word.md)
* [heroism](../../Magic/Spells/heroism.md)
* [identify](../../Magic/Spells/identify.md)
* [illusory script](../../Magic/Spells/illusory-script.md)
* [longstrider](../../Magic/Spells/longstrider.md)
* [silent image](../../Magic/Spells/silent-image.md)
* [sleep](../../Magic/Spells/sleep.md)
* [speak with animals](../../Magic/Spells/speak-with-animals.md)
* [thunderwave](../../Magic/Spells/thunderwave.md)
* [unseen servant](../../Magic/Spells/unseen-servant.md)

## 2nd Level
* [animal messenger](../../Magic/Spells/animal-messenger.md)
* [blindness/deafness](../../Magic/Spells/blindness-deafness.md)
* [calm emotions](../../Magic/Spells/calm-emotions.md)
* [detect thoughts](../../Magic/Spells/detect-thoughts.md)
* [enhance ability](../../Magic/Spells/enhance-ability.md)
* [enthrall](../../Magic/Spells/enthrall.md)
* [heat metal](../../Magic/Spells/heat-metal.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [invisibility](../../Magic/Spells/invisibility.md)
* [knock](../../Magic/Spells/knock.md)
* [lesser restoration](../../Magic/Spells/lesser-restoration.md)
* [locate animals or plants](../../Magic/Spells/locate-animals-or-plants.md)
* [locate object](../../Magic/Spells/locate-object.md)
* [magic mouth](../../Magic/Spells/magic-mouth.md) (ritual)
* [see invisibility](../../Magic/Spells/see-invisibility.md)
* [shatter](../../Magic/Spells/shatter.md)
* [silence](../../Magic/Spells/silence.md)
* [suggestion](../../Magic/Spells/suggestion.md)
* [zone of truth](../../Magic/Spells/zone-of-truth.md)

## 3rd Level
* [bestow curse](../../Magic/Spells/bestow-curse.md)
* [clairvoyance](../../Magic/Spells/clarivoyance.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [fear](../../Magic/Spells/fear.md)
* [glyph of warding](../../Magic/Spells/glyph-of-warding.md)
* [hypnotic pattern](../../Magic/Spells/hypnotic-pattern.md)
* [major image](../../Magic/Spells/major-image.md)
* [nondetection](../../Magic/Spells/nondetection.md)
* [plant growth](../../Magic/Spells/plant-growth.md)
* [sending](../../Magic/Spells/sending.md)
* [speak with dead](../../Magic/Spells/speak-with-dead.md)
* [speak with plants](../../Magic/Spells/speak-with-plants.md)
* [stinking cloud](../../Magic/Spells/stinking-cloud.md)
* [tongues](../../Magic/Spells/tongues.md)

## 4th Level
* [compulsion](../../Magic/Spells/compulsion.md)
* [confusion](../../Magic/Spells/confusion.md)
* [dimension door](../../Magic/Spells/dimension-door.md)
* [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
* [greater invisibility](../../Magic/Spells/greater-invisibility.md)
* [hallucinatory terrain](../../Magic/Spells/hallucinatory-terrain.md)
* [locate creature](../../Magic/Spells/locate-creature.md)
* [polymorph](../../Magic/Spells/polymorph.md)

## 5th Level
* [animate objects](../../Magic/Spells/animate-objects.md)
* [awaken](../../Magic/Spells/awaken.md)
* [dominate person](../../Magic/Spells/dominate-person.md)
* [dream](../../Magic/Spells/dream.md)
* [geas](../../Magic/Spells/geas.md)
* [greater restoration](../../Magic/Spells/greater-restoration.md)
* [hold monster](../../Magic/Spells/hold-monster.md)
* [legend lore](../../Magic/Spells/legend-lore.md)
* [mass cure wounds](../../Magic/Spells/mass-cure-wounds.md)
* [mislead](../../Magic/Spells/mislead.md)
* [modify memory](../../Magic/Spells/modify-memory.md)
* [planar binding](../../Magic/Spells/planar-binding.md)
* [raise dead](../../Magic/Spells/raise-dead.md)
* [scrying](../../Magic/Spells/scrying.md)
* [seeming](../../Magic/Spells/seeming.md)
* [teleportation circle](../../Magic/Spells/teleportation-circle.md)

## 6th Level
* [eyebite](../../Magic/Spells/eyebite.md)
* [find the path](../../Magic/Spells/find-the-path.md)
* [guards and wards](../../Magic/Spells/guards-and-wards.md)
* [mass suggestion](../../Magic/Spells/mass-suggestion.md)
* [otto's irresistible dance](../../Magic/Spells/ottos-irresistable-dance.md)
* [programmed illusion](../../Magic/Spells/programmed-illusion.md)
* [true seeing](../../Magic/Spells/true-seeing.md)

## 7th Level
* [etherealness](../../Magic/Spells/etherealness.md)
* [forcecage](../../Magic/Spells/forcecage.md)
* [mirage arcane](../../Magic/Spells/mirage-arcane.md)
* [mordenkainen's sword](../../Magic/Spells/mordenkainens-sword.md)
* [project image](../../Magic/Spells/project-image.md)
* [regenerate](../../Magic/Spells/regenerate.md)
* [resurrection](../../Magic/Spells/resurrection.md)
* [symbol](../../Magic/Spells/symbol.md)
* [teleport](../../Magic/Spells/teleport.md)

## 8th Level
* [dominate monster](../../Magic/Spells/dominate-monster.md)
* [feeblemind](../../Magic/Spells/feeblemind.md)
* [glibness](../../Magic/Spells/glibness.md)
* [mind blank](../../Magic/Spells/mind-blank.md)
* [power word: stun](../../Magic/Spells/power-word-stun.md)

## 9th Level
* [foresight](../../Magic/Spells/foresight.md)
* [power word: kill](../../Magic/Spells/power-word-kill.md)
* [true polymorph](../../Magic/Spells/true-polymorph.md)

