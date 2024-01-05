# Sorcerer
Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces. No one chooses sorcery; the power chooses the sorcerer.

*You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.*

```
name = 'Sorcerer'
description = "***Class: Sorcerer.*** Sorcerers carry a magical birthright conferred upon them by an exotic bloodline, some otherworldly influence, or exposure to unknown cosmic forces. No one chooses sorcery; the power chooses the sorcerer."
```

## Class Features
As a sorcerer, you gain the following class features.

Level|Proficiency Bonus|Sorcery Points|Cantrips Known|Spells Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|--------------|------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2| -|4| 2|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Sorcerous Origin](#sorcerous-origin)
2nd  |+2| 2|4| 3|3|-|-|-|-|-|-|-|-|[Font of Magic](#font-of-magic)
3rd  |+2| 3|4| 4|4|2|-|-|-|-|-|-|-|[Metamagic](#metamagic)
4th  |+2| 4|5| 5|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
5th  |+3| 5|5| 6|4|3|2|-|-|-|-|-|-|
6th  |+3| 6|5| 7|4|3|3|-|-|-|-|-|-|[Sorcerous Origin](#sorcerous-origin) feature
7th  |+3| 7|5| 8|4|3|3|1|-|-|-|-|-|
8th  |+3| 8|5| 9|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
9th  |+4| 9|5|10|4|3|3|3|1|-|-|-|-|
10th |+4|10|6|11|4|3|3|3|2|-|-|-|-|[Metamagic](#metamagic)
11th |+4|11|6|12|4|3|3|3|2|1|-|-|-|
12th |+4|12|6|12|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|13|6|13|4|3|3|3|2|1|1|-|-|
14th |+5|14|6|13|4|3|3|3|2|1|1|-|-|[Sorcerous Origin](#sorcerous-origin) feature
15th |+5|15|6|14|4|3|3|3|2|1|1|1|-|
16th |+5|16|6|14|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|17|6|15|4|3|3|3|2|1|1|1|1|[Metamagic](#metamagic)
18th |+6|18|6|15|4|3|3|3|3|1|1|1|1|[Sorcerous Origin](#sorcerous-origin) feature
19th |+6|19|6|15|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|20|6|15|4|3|3|3|3|2|2|1|1|[Sorcerous Restoration](#sorcerous-restoration)

### Hit Points
**Hit Dice**: 1d6 per sorcerer level

**Hit Points at 1st Level**: 6 + your Constitution modifier

**Hit Points at Higher Levels**: 1d6 (or 4) + your Constitution modifier per sorcerer level after 1st

```
def everylevel(npc): npc.hits('d6')
```

### Proficiencies
**Armor**: None

**Weapons**: Daggers, darts, slings, quarterstaffs, light crossbows

**Tools**: None

**Saving Throws**: Constitution, Charisma

**Skills**: Choose two from Arcana, Deception, Insight, Intimidation, Persuasion, and Religion

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:
* (a) a light crossbow and 20 bolts or (b) any simple weapon
* (a) a component pouch or (b) an arcane focus
* (a) a dungeoneer's pack or (b) an explorer's pack
* Two daggers

```
def level1(npc):
    npc.savingthrows.append("CHA")
    npc.savingthrows.append("CON")

    for wpn in ['Dagger', 'Dart', 'Sling', 'Quarterstaff', 'Light crossbow']:
        npc.proficiencies.append(wpn)

    skills = ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']
    chooseskill(npc, skills)
    chooseskill(npc, skills)

    npc.equipment.append("Light crossbow and 20 bolts OR any simple weapon")
    npc.equipment.append("Component pouch OR an arcane focus")
    npc.equipment.append("Dungeoneer's pack, or explorer's pack")
    npc.equipment.append("Two daggers")
```

## Spellcasting
An event in your past, or in the life of a parent or ancestor, left an indelible mark on you, infusing you with arcane magic. This font of magic, whatever its origin, fuels your spells.

### Cantrips
At 1st level, you know four cantrips of your choice from the sorcerer spell list. You learn additional sorcerer cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Sorcerer table.

### Spell Slots
The Sorcerer table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these sorcerer spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

For example, if you know the 1st-level spell Burning Hands and have a 1st-level and a 2nd-level spell slot available, you can cast Burning Hands using either slot.

### Spell Versatility
Whenever you finish a long rest, you can replace one spell you learned from this Spellcasting feature with another spell from the sorcerer spell list. The new spell must be the same level as the spell you replace.

### Spells Known of 1st Level and Higher
You know two 1st-level spells of your choice from the sorcerer spell list.

The Spells Known column of the Sorcerer table shows when you learn more sorcerer spells of your choice. Each of these spells must be of a level for which you have spell slots. For instance, when you reach 3rd level in this class, you can learn one new spell of 1st or 2nd level.

Additionally, when you gain a level in this class, you can choose one of the sorcerer spells you know and replace it with another spell from the sorcerer spell list, which also must be of a level for which you have spell slots.

Note that there are vastly more sorcerer spells in the universe than what a sorcerer knows. The list at the end of this class description is a list of all the commonly-known sorcerer spells, and a sorcerer is free to choose from anything on this list (within the scope of these rules). A sorcerer can learn new spells and add to their list of known spells, either by being the target of a given spell (including being targeted by it) once for each level of the spell (so a 5th-level spell will require seeing it cast 5 times to be able to reverse-engineer it), or by being taught it by one who already knows how to cast it.

### Spellcasting Ability
Charisma is your spellcasting ability for your sorcerer spells, since the power of your magic relies on your ability to project your will into the world. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a sorcerer spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier

**Spell attack modifier** = your proficiency bonus + your Charisma modifier

### Spellcasting Focus
You can use an arcane focus as a spellcasting focus for your sorcerer spells.

```
    spellcasting = fullcaster(npc, 'CHA', 'Sorcerer')
    def setmaxspellsknown(npc): 
        level = npc.levels('Sorcerer')
        if level < 12: spellcasting.maxspellsknown = level + 1
        elif level < 13: spellcasting.maxspellsknown = 12
        elif level < 15: spellcasting.maxspellsknown = 13
        elif level < 17: spellcasting.maxspellsknown = 14
        else: spellcasting.maxspellsknown = 15
    npc.defer(lambda npc: setmaxspellsknown(npc) )
    def setmaxcantripsknown(npc):
        level = npc.levels('Sorcerer')
        if level < 4: spellcasting.maxcantripsknown = 4 
        elif level < 10: spellcasting.maxcantripsknown = 5
        else: spellcasting.maxcantripsknown = 6
    npc.defer(lambda npc: setmaxcantripsknown(npc) )
```


## Sorcerous Origin
Choose a sorcerous origin, which describes the source of your innate magical power:

Some have been touched by external forces in some way:

* [Aberrant Mind](AberrantMind.md) sorcerers have been touched by creatures of the astral deep.
* [Clockwork Soul](ClockworkSoul.md) sorcerers means the powers of neutrality call to you.
* [Divine Soul](DivineSoul.md) sorcerers have found favor with celestial beings.
* [Etched Soul](EtchedSoul.md) sorcerers have magic that comes from an ancient or powerful text.
* [Evil Star](EvilStar.md) sorcerers were born under an evil star, and it gives them power.
* [Green Star](GreenStar.md) sorcerers feel the power of an ancient stone of power in their blood somehow.
* [Lunar](Lunar.md) sorcerers feel the power of the moon(s) above them.
* [Phoenix](Phoenix.md) sorcerers have the power of the ancient phoenix within them.
* [Shadow](Shadow.md) sorcerers have been touched by the Shadowfell.

Others have arcane power flowing through their bloodline:

* [Arcane Anomaly](ArcaneAnomaly.md) sorcerers are of a tainted bloodline with sinister potential.
* [Arcane Legacy](ArcaneLegacy.md) sorcerers have a long bloodline of powerful arcane users.
* [Draconic Bloodline](DraconicBloodline.md) suggests that the dragons, somewhere, somewhen, fit into your family tree; sometimes, this can come about because you have a [dragonmarked](../../Races/Dragonmarked.md) ancestor somewhere in your family line.
* [Elemancy](Elemancy.md) sorcerers have the raw power of the elements coursing through them.
* [Giant Soul](GiantSoul.md) sorcerers have ancient giantish blood within them.

Some have found sources of power that they tap for arcane use:

* [Blood](Blood.md) is the magic within all, and you use none more than your own.
* [Channeler](Channeler.md) sorcerers are those who have an innate gift to absorb the raw power of magic and turn it to their own ends.
* [Firespeaker](Firespeaker.md), [Seacaller](Seacaller.md), [Stoneshaper](Stoneshaper.md), and [Windtalker](Windtalker.md) sorcerers hear one of the Elemental Planes in their soul, through the elements all around them, guiding them.
* [Psionic Soul](PsionicSoul.md) sorcerers have touched the power of the mind. 
* [Storm](Storm.md) sorcerers feel the power of the storm, and are extremely common (and valued) among the *al'maera* of the [Al'Uma](../../Cultures/AlUma.md).
* [Wild Magic](WildMagic.md) sorcerers wrestle with power beyond control.

And some are just... weird:

* [Soulless](Soulless.md) sorcerers have no soul. At all.

Your choice grants you features when you choose it at 1st level and again at 6th, 14th, and 18th level. Note that some Sorcerous Origins will not be widely accepted, and may cause you to generate adverse reactions in those you meet during your time.

```
    # Choose subclass
    (_, subclass) = choose("Choose a Sorcerous Origin:", subclasses)
    npc.subclasses[allclasses['Sorcerer']] = subclass
    npc.description.append(subclass.description)
```

## Font of Magic
*2nd-level sorcerer feature*

You tap into a deep wellspring of magic within yourself. This wellspring is represented by sorcery points, which allow you to create a variety of magical effects.

### Sorcery Points
You have 2 sorcery points, and you gain more as you reach higher levels, as shown in the Sorcery Points column of the Sorcerer table. You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest.

### Flexible Casting
You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points. You learn other ways to use your sorcery points as you reach higher levels.

***Creating Spell Slots.*** You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The Creating Spell Slots table shows the cost of creating a spell slot of a given level. You can create spell slots no higher in level than 5th. The created spell slots vanish at the end of a long rest.

**Creating Spell Slots**

Spell Slot Level|Sorcery Point Cost
----------------|------------------
1st | 2
2nd | 3
3rd | 5
4th | 6
5th | 7

***Converting a Spell Slot to Sorcery Points.*** As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level.

***Empowering Reserves.*** When you make an ability check on your turn, you can spend 2 sorcery points to gain advantage on the check.

***Imbuing Touch.*** As an action, you can touch one nonmagical weapon and spend 2 sorcery points to imbue it with magic for 1 minute. For the duration, the weapon is considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.

***Sorcerous Fortitude.*** As an action, you can spend any number of sorcery points to roll a d4 for each point expended. You gain a number of temporary hit points equal to the total rolled.

```
def level2(npc):
    def calculatesorcerypoints(npc):
        npc.spellcasting['Sorcerer'].sorcerypoints = npc.levels('Sorcerer')
        npc.traits.append(f"***Font of Magic (Recharges on long rest).*** You have {npc.spellcasting['Sorcerer'].sorcerypoints} sorcery points.")
    npc.defer(lambda npc: calculatesorcerypoints(npc) )

    npc.traits.append("***Font of Magic: Empowering Reserves.*** When you make an ability check on your turn, you can spend 2 sorcery points to gain advantage on the check.")

    npc.bonusactions.append("***Font of Magic: Create.*** You expend sorcery points to create a spell slot. 2 points creates a 1st-level slot, 3 creates a 2nd, 5 creates a 3rd, 6 creates a 4th, and 7 points creates a 5th-level slot.")

    npc.bonusactions.append("***Font of Magic: Convert.*** You expend one spell slot and gain a number of sorcery points equal to the slot's level.")

    npc.actions.append("***Font of Magic: Sorcerous Fortitude.*** You spend any number of sorcery points to roll a d4 for each point expended. You gain a number of temporary hit points equal to the total.")
```

## Metamagic
*3rd-level sorcerer feature*

You gain the ability to twist your spells to suit your needs. You gain two of the following Metamagic options of your choice. You gain another one at 10th and 17th level.

You can use only one Metamagic option on a spell when you cast it, unless otherwise noted.

* **Careful Spell**
  When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell's full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your Charisma modifier (minimum of one creature). A chosen creature automatically succeeds on its saving throw against the spell.

```
def carefulspell(npc):
    npc.defer(lambda npc: npc.traits.append("***Metamagic: Careful Spell.*** You spend 1 sorcery point and choose up to {npc.CHAbonus()} creatures. A chosen creature automatically succeeds on its saving throw against the spell.") )
```

* **Distant Spell**
  When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the range of the spell.

  When you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet.

```
def distantspell(npc):
    npc.traits.append("***Metamagic: Distant Spell.*** You spend 1 sorcery point to either double the range of the spell (if it has a range of 5 feet or greater) or give it a range of 30 feet (if it is a touch spell).")
```

* **Elemental Spell** 
  When you cast a spell that deals a type of damage from the following list, you can spend 1 sorcery point to change that damage type to one of the other listed types: acid, cold, fire, lightning, thunder.

```
def elementalspell(npc):
    npc.traits.append("***Metamagic: Elemental Spell.*** You spend 1 sorcery point to change the damage type from one of these types into one of the other listed types: acid, cold, fire, lightning, thunder.")
```

* **Empowered Spell**
  When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls.

  You can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell.

```
def empoweredspell(npc):
    npc.defer(lambda npc: npc.traits.append("***Metamagic: You spend 1 sorcery point to reroll up to {npc.CHAbonus()} damage dice. You must use the new rolls. You can use this even if you have already used a different Metamagic option during the casting of the spell.") )
```

* **Extended Spell**
  When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours.

```
def extendedspell(npc):
    npc.traits.append("***Metamagic: Extended Spell.*** You spend 1 sorcery point to double the duration of a spell (that has a duration of 1 minute or longer), to a maximum of 24 hours.")
```

* **Heightened Spell**
  When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell.

```
def heightenedspell(npc):
    npc.traits.append("***Metamagic: Heightened Spell.*** When you cast a spell that forces a creature to make a saving throw to resist its effects, you spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell.")
```

* **Quickened Spell**
  When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting.

```
def quickenedspell(npc):
    npc.traits.append("***Metamagic: Quickened Spell.*** You spend 2 sorcery points to change a spell with a casting time of 1 action to be a casting time of 1 bonus action for this casting.")
```

* **Seeking Spell**
  When you cast a spell that requires you to make a spell attack roll or that forces a target to make a Dexterity saving throw, you can spend 1 sorcery point to ignore the effects of half- and three-quarters cover against targets of the spell.

```
def seekingspell(npc):
    npc.traits.append("***Metamagic: Seeking Spell.*** You spend 1 sorcery point to ignore half- and three-quarters cover for targets of a spell that requires you to make a spell attack roll or that forces a target to make a Dexteriy saving throw.")
```

* **Subtle Spell**
  When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components.

```
def subtlespell(npc):
    npc.traits.append("***Metamagic: Subtle Spell.*** You spend 1 sorcery point to cast a spell without any somatic or verbal components for this casting.")
```

* **Twinned Spell**
  When you cast a spell that targets only one creature and doesn't have a range of self, you can spend a number of sorcery points equal to the spell's level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip). To be eligible for Twinned Spell, a spell must be incapable of targeting more than one creature at the spell's current level.

```
def twinnedspell(npc):
    npc.traits.append("***Metamagic: Twinned Spell.*** You spend a number of sorcery points equal to the spell's level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip). To be eligible for Twinned Spell, the spell must target only one creature, doesn't have a range of self, and be incapable of targeting more than one creature at the spell's current level.")
```

* **Unerring Spell**
  If you make an attack roll for a spell and miss, you can spend 2 sorcery points to reroll the attack roll. You must use the result of the second roll.
  
  You can use Unerring Spell even if you have already used a different Metamagic option during the casting of the spell.

```
def unerringspell(npc):
    npc.traits.append("***Metamagic: Unerring Spell.*** You spend 2 sorcery points to reroll an attack roll for a spell that missed. You must use the result of the second roll. You can use Unerring Spell even if you have already used a different Metamagic option during the casting of the spell.")
```

```
metamagic = {
    'Careful Spell' : carefulspell,
    'Distant Spell' : distantspell,
    'Elemental Spell' : elementalspell,
    'Empowered Spell' : empoweredspell,
    'Extended Spell' : extendedspell,
    'Heightened Spell' : heightenedspell,
    'Quickened Spell' : quickenedspell,
    'Seeking Spell' : seekingspell,
    'Subtle Spell' : subtlespell,
    'Twinned Spell' : twinnedspell,
    'Unerring Spell' : unerringspell
}
def choosemetamagic(npc):
    (metaname, metafn) = choose("Choose a Metamagic option: ", metamagic)
    if getattr(npc, "metamagic", None) == None:
        npc.metamagic = []
    npc.metamagic.append(metaname)
    metafn(npc)
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

## Sorcerous Restoration
*20th-level sorcerer feature*

You regain 4 expended sorcery points whenever you finish a short rest.

---

# "Core" Sorcerer Spells
This is the list of spells all sorcerers have access to know. These spells are always accessible to the sorcerer to "know" (as part of their [Spells Known](#spell-versatility)). Some of the [mage schools](../../Organizations/MageSchools/index.md) know sorcerer spells that are not on this list, and those schools can (and frequently do) share those secrets with other sorcerers... for a price.

## Cantrips
* [acid splash](../../Magic/Spells/acid-splash.md)
* [blade ward](../../Magic/Spells/blade-ward.md)
* [chill touch](../../Magic/Spells/chill-touch.md)
* [dancing lights](../../Magic/Spells/dancing-lights.md)
* [fire bolt](../../Magic/Spells/fire-bolt.md)
* [friends](../../Magic/Spells/friends.md)
* [light](../../Magic/Spells/light.md)
* [mage hand](../../Magic/Spells/mage-hand.md)
* [mending](../../Magic/Spells/mending.md)
* [message](../../Magic/Spells/message.md)
* [minor illusion](../../Magic/Spells/minor-illusion.md)
* [poison spray](../../Magic/Spells/poison-spray.md)
* [prestidigitation](../../Magic/Spells/prestidigitation.md)
* [ray of frost](../../Magic/Spells/ray-of-frost.md)
* [shocking grasp](../../Magic/Spells/shocking-grasp.md)
* [true strike](../../Magic/Spells/true-strike.md)

## 1st Level
* [burning hands](../../Magic/Spells/burning-hands.md)
* [charm person](../../Magic/Spells/charm-person.md)
* [chromatic orb](../../Magic/Spells/chromatic-orb.md)
* [color spray](../../Magic/Spells/color-spray.md)
* [comprehend languages](../../Magic/Spells/comprehend-languages.md)
* [detect magic](../../Magic/Spells/detect-magic.md)
* [disguise self](../../Magic/Spells/disguise-self.md)
* [expeditious retreat](../../Magic/Spells/expeditious-retreat.md)
* [false life](../../Magic/Spells/false-life.md)
* [feather fall](../../Magic/Spells/feather-fall.md)
* [flash](../../Magic/Spells/flash.md)
* [fog cloud](../../Magic/Spells/fog-cloud.md)
* [jump](../../Magic/Spells/jump.md)
* [mage armor](../../Magic/Spells/mage-armor.md)
* [magic missile](../../Magic/Spells/magic-missile.md)
* [ray of sickness](../../Magic/Spells/ray-of-sickness.md)
* [shield](../../Magic/Spells/shield.md)
* [silent image](../../Magic/Spells/silent-image.md)
* [sleep](../../Magic/Spells/sleep.md)
* [thunderwave](../../Magic/Spells/thunderwave.md)
* [witch bolt](../../Magic/Spells/witch-bolt.md)

## 2nd Level
* [alter self](../../Magic/Spells/alter-self.md)
* [blindness/deafness](../../Magic/Spells/blindness-deafness.md)
* [blur](../../Magic/Spells/blur.md)
* [cloud of daggers](../../Magic/Spells/cloud-of-daggers.md)
* [crown of madness](../../Magic/Spells/crown-of-madness.md)
* [darkness](../../Magic/Spells/darkness.md)
* [darkvision](../../Magic/Spells/darkvision.md)
* [detect thoughts](../../Magic/Spells/detect-thoughts.md)
* [enhance ability](../../Magic/Spells/enhance-ability.md)
* [enlarge/reduce](../../Magic/Spells/enlarge-reduce.md)
* [gust of wind](../../Magic/Spells/gust-of-wind.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [invisibility](../../Magic/Spells/invisibility.md)
* [knock](../../Magic/Spells/knock.md)
* [levitate](../../Magic/Spells/levitate.md)
* [mirror image](../../Magic/Spells/mirror-image.md)
* [misty step](../../Magic/Spells/misty-step.md)
* [phantasmal force](../../Magic/Spells/phantasmal-force.md)
* [scorching ray](../../Magic/Spells/scorching-ray.md)
* [see invisibility](../../Magic/Spells/see-invisibility.md)
* [shatter](../../Magic/Spells/shatter.md)
* [spider climb](../../Magic/Spells/spider-climb.md)
* [suggestion](../../Magic/Spells/suggestion.md)
* [web](../../Magic/Spells/web.md)

## 3rd Level
* [blink](../../Magic/Spells/blink.md)
* [clairvoyance](../../Magic/Spells/clarivoyance.md)
* [counterspell](../../Magic/Spells/counterspell.md)
* [daylight](../../Magic/Spells/daylight.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [fear](../../Magic/Spells/fear.md)
* [fireball](../../Magic/Spells/fireball.md)
* [fly](../../Magic/Spells/fly.md)
* [gaseous form](../../Magic/Spells/gaseous-form.md)
* [haste](../../Magic/Spells/haste.md)
* [hypnotic pattern](../../Magic/Spells/hypnotic-pattern.md)
* [lightning bolt](../../Magic/Spells/lightning-bolt.md)
* [major image](../../Magic/Spells/major-image.md)
* [protection from energy](../../Magic/Spells/protection-from-energy.md)
* [sleet storm](../../Magic/Spells/sleet-storm.md)
* [slow](../../Magic/Spells/slow.md)
* [stinking cloud](../../Magic/Spells/stinking-cloud.md)
* [tongues](../../Magic/Spells/tongues.md)
* [water breathing](../../Magic/Spells/water-breathing.md) (ritual)
* [water walk](../../Magic/Spells/water-walk.md) (ritual)

## 4th Level
* Banishment
* Blight
* Confusion
* Dimension Door
* Dominate Beast
* Greater Invisibility
* Ice Storm
* Polymorph
* Stoneskin
* Wall of Fire

## 5th Level
* [animate objects](../../Magic/Spells/animate-objects.md)
* Cloudkill
* Cone of Cold
* Creation
* Dominate Person
* Hold Monster
* Insect Plague
* Seeming
* Telekinesis
* Teleportation Circle
* [wall of stone](../../Magic/Spells/wall-of-stone.md)

## 6th Level
* Arcane Gate
* Chain Lightning
* Circle of Death
* Disintegrate
* Eyebite
* Globe of Invulnerability
* Mass Suggestion
* Move Earth
* Sunbeam
* True Seeing

## 7th Level
* Delayed Blast Fireball
* Etherealness
* Finger of Death
* Fire Storm
* Plane Shift
* Prismatic Spray
* Reverse Gravity
* Teleport

## 8th Level
* Dominate Monster
* Earthquake
* Incendiary Cloud
* Power Word: Stun
* Sunburst

## 9th Level
* Gate
* Meteor Swarm
* Power Word: Kill
* Time Stop
* Wish
