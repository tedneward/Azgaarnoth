# Cleric
Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic.

Several major [religions](../../Religions/index.md) dot the surface of Azgaarnoth, each with its own set of domains and unique abilities. You may wish to take a look at these before making any particular choices about your cleric's domains and characteristics.

```
name = 'Cleric'
description = "***Class: Cleric.*** Clerics are intermediaries between the mortal world and the distant planes of the gods. As varied as the gods they serve, clerics strive to embody the handiwork of their deities. No ordinary priest, a cleric is imbued with divine magic."
```

## Class features
As a cleric, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|3|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Divine Domain](#divine-domain)
2nd  |+2|3|3|-|-|-|-|-|-|-|-|[Channel Divinity](#channel-divinity) (x1), [Divine Domain](#divine-domain) feature
3rd  |+2|3|4|2|-|-|-|-|-|-|-|
4th  |+2|4|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement)
5th  |+3|4|4|3|2|-|-|-|-|-|-|[Destroy Undead](#destroy-undead) (CR 1/2)
6th  |+3|4|4|3|3|-|-|-|-|-|-|[Channel Divinity](#channel-divinity) (x2), [Divine Domain](#divine-domain) feature
7th  |+3|4|4|3|3|1|-|-|-|-|-|
8th  |+3|4|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement), [Destroy Undead](#destroy-undead) (CR 1), [Divine Domain](#divine-domain) feature
9th  |+4|4|4|3|3|3|1|-|-|-|-|
10th |+4|5|4|3|3|3|2|-|-|-|-|[Divine Intervention](#divine-intervention)
11th |+4|5|4|3|3|3|2|1|-|-|-|[Destroy Undead](#destroy-undead) (CR 2)
12th |+4|5|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement)
13th |+5|5|4|3|3|3|2|1|1|-|-|
14th |+5|5|4|3|3|3|2|1|1|-|-|[Destroy Undead](#destroy-undead) (CR 3)
15th |+5|5|4|3|3|3|2|1|1|1|-|
16th |+5|5|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement)
17th |+6|5|4|3|3|3|2|1|1|1|1|[Destroy Undead](#destroy-undead) (CR 4), [Divine Domain](#divine-domain) feature
18th |+6|5|4|3|3|3|3|1|1|1|1|[Channel Divinity](#channel-divinity) (x3)
19th |+6|5|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement)
20th |+6|5|4|3|3|3|3|2|2|1|1|[Divine Intervention](#divine-intervention) improvement

### Hit Points
**Hit Dice**: 1d8 per cleric level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per cleric level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor, medium armor, shields

**Weapons**: All simple weapons

**Tools**: None

**Saving Throws**: Wisdom, Charisma

**Skills**: Choose two from History, Insight, Medicine, Persuasion, and Religion

```
def level1(npc):
    for arm in armor['light'] | armor['medium'] | armor['shields']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)

    npc.savingthrows.append('WIS')
    npc.savingthrows.append('CHA')

    skillchoices = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
    chooseskill(npc, skillchoices)
    chooseskill(npc, skillchoices)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a mace or (b) a warhammer (if proficient)
* (a) scale mail, (b) leather armor, or (c) chain mail (if proficient)
* (a) a light crossbow and 20 bolts or (b) any simple weapon
* (a) a priest's pack or (b) an explorer's pack
* A shield and a holy symbol

```
    npc.equipment.append("Mace")
    npc.armorclass['Scale mail'] = 14
    npc.equipment.append("Light crossbow and 20 bolts")
    npc.equipment.append("Priest's pack")
    npc.equipment.append("Shield")
    npc.equipment.append("Holy symbol")
```

## Spellcasting
*1st-level cleric feature*

As a conduit for divine power, you can cast cleric spells.

### Cantrips
At 1st level, you know three cantrips of your choice from the cleric spell list. You learn additional cleric cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Cleric table.

### Cantrip Versatility
Whenever you gain a level in this class, you can replace one cantrip you learned from this Spellcasting feature with another cantrip from the cleric spell list.

### Spell Slots
The Cleric table shows how many spell slots you have to cast your spells of lst level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of cleric spells that are available for you to cast, choosing from the cleric spell list available. (Note that at the DM's discretion, not all cleric spells in the world may be available to you.) When you do so, choose a number of cleric spells equal to your Wisdom modifier + your cleric level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you are a 3rd-level cleric, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell *cure wounds*, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of cleric spells requires time spent in prayer and meditation: at least 1 minute per spell level for each spell on your list.

### Spellcasting Ability
Wisdom is your spellcasting ability for your cleric spells. The power of your spells comes from your devotion to your deity. You use your Wisdom whenever a cleric spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a cleric spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

```
    sc = fullcaster(npc, 'WIS', 'Cleric')
    sc.casterclass = allclasses['Cleric']

    def spellcasting(npc): 
        npc.spellcasting[name].maxcantripsknown = 3 if npc.levels(name) < 4 else 4 if npc.levels(name) < 10 else 5
        npc.spellcasting[name].spellsprepared = npc.levels(name) + npc.WISbonus()

    npc.defer(lambda npc: spellcasting(npc))
```

### Ritual Casting
You can cast a cleric spell as a ritual if that spell has the ritual tag and you have the spell prepared.

### Spellcasting Focus
You can use a holy symbol as a spellcasting focus for your cleric spells.

## Divine Domain
*1st-level cleric feature*

Choose one domain, or choose a [diety or religion](../../Religions/index.md) and select one of their domains:

* [Air](Air.md)
* [Arcana](Arcana.md)
* [Cat](Cat.md)
* [Chaos](Chaos.md)
* [Cold](Cold.md)
* [Dark](Dark.md)
* [Death](Death.md)
* [Desire](Desire.md)
* [Destruction](Destruction.md)
* [Dragon](Dragon.md)
* [Earth](Earth.md)
* [Fertility](Fertility.md)
* [Fire](Fire.md)
* [Forge](Forge.md)
* [Grave](Grave.md)
* [Healing](Healing.md)
* [Hearth](Hearth.md)
* [Illusion](Illusion.md)
* [Knowledge](Knowledge.md)
* [Life](Life.md)
* [Light](Light.md)
* [Luck](Luck.md)
* [Madness](Madness.md)
* [Moon](Moon.md)
* [Nature](Nature.md)
* [Night](Night.md)
* [Ocean](Ocean.md)
* [Order](Order.md)
* [Pain](Pain.md)
* [Peace](Peace.md)
* [Plague](Plague.md)
* [Protection](Protection.md)
* [Sea](Sea.md)
* [Shadow](Shadow.md)
* [Tempest](Tempest.md)
* [Time](Time.md)
* [Trickery](Trickery.md)
* [Twilight](Twilight.md)
* [Vengeance](Vengeance.md)
* [War](War.md)
* [Water](Water.md)

Alternatively, there are some "concepts" beyond the simple "deity worship" that--somehow--yield divine power and benefits:

* [Abandoned](Abandoned.md): Abandoned clerics borrow divine power from other gods and clerics in the universe.
* [Blood](Blood.md): Blood clerics use the divine power present in each of us to power their spells.
* [Defier](Defier.md): 
* [Entropy](Entropy.md): Entropy clerics use the divine power that comes from the entropy in the universe.
* [Phoenix](Phoenix.md): Phoenix clerics tap into a raw cosmic force (the Phoenix). 
* [Unity](Unity.md): Unity clerics borrow the divine power that generates when a group of diverse beings collectively share in an unshakable belief in one another.
* [Zeal](Zeal.md): Zeal clerics believe not in the domain of their deity, but in the rabid belief that their deity's way is superior to all others.

Your choice grants you domain spells and other features when you choose it at 1st level. It also grants you additional ways to use [Channel Divinity](#channel-divinity) when you gain that feature at 2nd level, and additional benefits at 6th, 8th, and 17th levels.

```
    (_, subclass) = choose("Choose a domain: ", subclasses)
    npc.subclasses[allclasses['Cleric']] = subclass
    npc.description.append(subclass.description)
    subclass.spellcasting = npc.spellcasting[name]
```

## Domain Spells
*1st-level cleric feature*

Each domain has a list of spells--its domain spells that you gain at the cleric levels noted in the domain description. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day.

If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

## Channel Divinity
*2nd-level cleric feature*

You gain the ability to channel divine energy directly from your deity, using that energy to fuel magical effects. You start with three such effects: Turn Undead, Harness Divine Power, and an effect determined by your domain. Some domains grant you additional effects as you advance in levels, as noted in the domain description.

When you use your [Channel Divinity](#channel-divinity), you choose which effect to create. You must then finish a short or long rest to use your [Channel Divinity](#channel-divinity) again.

Some [Channel Divinity](#channel-divinity) effects require saving throws. When you use such an effect from this class, the DC equals your cleric spell save DC.

Beginning at 6th level, you can use your [Channel Divinity](#channel-divinity) twice between rests, and beginning at 18th level, you can use it three times between rests. When you finish a short or long rest, you regain your expended uses.

```
def level2(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Channel Divinity ({'' if npc.levels('Cleric') < 6 else '2/' if npc.levels('Cleric') < 18 else '3/'}Recharges on short or long rest).*** See below for the details of each use."))
```

## Channel Divinity: Turn Undead
*2nd-level cleric feature*

As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

```
    npc.actions.append("***Channel Divinity: Turn Undead.*** You can use one of your uses of Channel Divinity to turn undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.")
```

## Channel Divinity: Harness Divine Power
*2nd-level cleric feature*

You can expend a use of your [Channel Divinity](#channel-divinity) to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up). The number of times you can use this feature is based on the level you've reached in this class: 2nd level, once; 6th level, twice; and 18th level, thrice. You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Channel Divinity: Harness Divine Power.*** You can expend a use of your Channel Divinity to regain one expended spell slot, the level of which can be no higher than {(npc.proficiencybonus() // 2) + 1}."))
```

## [Ability Score Improvement](#ability-score-improvement)
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): abilityscoreimprovement(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Cantrip Versatility
*4th-level cleric feature*

Whenever you reach a level in this class that grants the [Ability Score Improvement](#ability-score-improvement) feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the cleric spell list. 

## Destroy Undead
*5th-level cleric feature*

When an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below a certain threshold, as shown below:

**Destroy Undead Table**

Cleric Level | Destroys Undead of CR ...
-------------|--------------------------
5th | 1/2 or lower
8th | 1 or lower
11th| 2 or lower
14th| 3 or lower
17th| 4 or lower

```
def level5(npc):
    npc.defer(lambda npc: replace("***Channel Divinity: Turn Undead.***", npc.actions, f" You can use one of your uses of Channel Divinity to turn undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, if it is a CR of {'1/2' if npc.levels('Cleric') < 8 else '1' if npc.levels('Cleric') < 11 else '2' if npc.levels('Cleric') < 14 else '3' if npc.levels('Cleric') < 17 else '4'} or lower it is destroyed; otherwise it is turned for 1 minute or until it takes any damage.A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action."))
```

## Divine Intervention
*10th-level cleric feature*

You can call on your deity to intervene on your behalf when your need is great.

Imploring your deity's aid requires you to use your action. Describe the assistance you seek, and roll percentile dice. If you roll a number equal to or lower than your cleric level, your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise, you can use it again after you finish a long rest.

At 20th level, your call for intervention succeeds automatically, no roll required.

```
def level10(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Divine Intervention (Recharges on long rest/7 days).*** Describe the assistance you seek, and {'roll percentile dice. If you roll a number equal to or lower than ' + len(npc.levels('Cleric')) + ', ' if npc.levels('Cleric') < 20 else ''}your deity intervenes. The DM chooses the nature of the intervention; the effect of any cleric spell or cleric domain spell would be appropriate. If your deity intervenes, you can't use this feature again for 7 days. Otherwise you can use it again after you finish a long rest."))
```

---

# "Core" Cleric Spells
The following spells listed are available to all clerics throughout Azgaarnoth; this is not the complete list of all cleric spells, however. Certain domains may have additional spells that are only known to their clergy. Clerics learn new spells by visiting foreign temples, uncovering domain-relevant prayer books in ancient ruins, or even beseeching their gods/goddesses for new knowledge, and so on.

> ### GM Notes
> These are all the spells found in the *Player's Handbook*, with no additions. In game terms, these spells are common spells, and are always accessible (subject to domain restrictions) for preparation.


## Cantrips
* [guidance](../../Magic/Spells/guidance.md)
* [light](../../Magic/Spells/light.md)
* [mending](../../Magic/Spells/mending.md)
* [resistance](../../Magic/Spells/resistance.md)
* [sacred flame](../../Magic/Spells/sacred-flame.md)
* [spare the dying](../../Magic/Spells/spare-the-dying.md)
* [thaumaturgy](../../Magic/Spells/thaumaturgy.md)

## 1st Level
* [bane](../../Magic/Spells/bane.md)
* [bless](../../Magic/Spells/bless.md)
* [command](../../Magic/Spells/command.md)
* [create or destroy water](../../Magic/Spells/create-or-destroy-water.md)
* [cure wounds](../../Magic/Spells/cure-wounds.md)
* [detect evil and good](../../Magic/Spells/detect-evil-and-good.md)
* [detect magic](../../Magic/Spells/detect-magic.md)
* [detect poison and disease](../../Magic/Spells/detect-poison-and-disease.md)
* [guiding bolt](../../Magic/Spells/guiding-bolt.md)
* [healing word](../../Magic/Spells/healing-word.md)
* [inflict wounds](../../Magic/Spells/inflict-wounds.md)
* [protection from evil and good](../../Magic/Spells/protection-from-evil-and-good.md)
* [purify food and drink](../../Magic/Spells/purify-food-and-drink.md)
* [sanctuary](../../Magic/Spells/sanctuary.md)
* [shield of faith](../../Magic/Spells/shield-of-faith.md)

## 2nd Level
* [aid](../../Magic/Spells/aid.md)
* [augury](../../Magic/Spells/augury.md)
* [blindness/deafness](../../Magic/Spells/blindness-deafness.md)
* [calm emotions](../../Magic/Spells/calm-emotions.md)
* [continual flame](../../Magic/Spells/continual-flame.md)
* [enhance ability](../../Magic/Spells/enhance-ability.md)
* [find traps](../../Magic/Spells/find-traps.md)
* [gentle repose](../../Magic/Spells/gentle-repose.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [lesser restoration](../../Magic/Spells/lesser-restoration.md)
* [locate object](../../Magic/Spells/locate-object.md)
* [prayer of healing](../../Magic/Spells/prayer-of-healing.md)
* [protection from poison](../../Magic/Spells/protection-from-poison.md)
* [silence](../../Magic/Spells/silence.md)
* [spiritual weapon](../../Magic/Spells/spiritual-weapon.md)
* [warding bond](../../Magic/Spells/warding-bond.md)
* [zone of truth](../../Magic/Spells/zone-of-truth.md)

## 3rd Level
* [animate dead](../../Magic/Spells/animate-dead.md)
* [beacon of hope](../../Magic/Spells/beacon-of-hope.md)
* [bestow curse](../../Magic/Spells/bestow-curse.md)
* [clairvoyance](../../Magic/Spells/clarivoyance.md)
* [create food and water](../../Magic/Spells/create-food-and-water.md)
* [daylight](../../Magic/Spells/daylight.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [glyph of warding](../../Magic/Spells/glyph-of-warding.md)
* [magic circle](../../Magic/Spells/magic-circle.md)
* [mass healing word](../../Magic/Spells/mass-healing-word.md)
* [mass shield](../../Magic/Spells/mass-shield.md)
* [meld into stone](../../Magic/Spells/meld-into-stone.md)
* [protection from energy](../../Magic/Spells/protection-from-energy.md)
* [remove curse](../../Magic/Spells/remove-curse.md)
* [revivify](../../Magic/Spells/revivify.md)
* [sending](../../Magic/Spells/sending.md)
* [speak with dead](../../Magic/Spells/speak-with-dead.md)
* [spirit guardians](../../Magic/Spells/spirit-guardians.md)
* [tongues](../../Magic/Spells/tongues.md)
* [water walk](../../Magic/Spells/water-walk.md) (ritual)

## 4th Level
* [banishment](../../Magic/Spells/banishment.md)
* [control water](../../Magic/Spells/control-water.md)
* [death ward](../../Magic/Spells/death-ward.md)
* [divination](../../Magic/Spells/divination.md)
* [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
* [guardian of faith](../../Magic/Spells/guardian-of-faith.md)
* [locate creature](../../Magic/Spells/locate-creature.md)
* [stone shape](../../Magic/Spells/stone-shape.md)

## 5th Level
* [commune](../../Magic/Spells/commune.md)
* [contagion](../../Magic/Spells/contagion.md)
* [dispel evil and good](../../Magic/Spells/dispel-evil-and-good.md)
* [flame strike](../../Magic/Spells/flame-strike.md)
* [geas](../../Magic/Spells/geas.md)
* [greater restoration](../../Magic/Spells/greater-restoration.md)
* [hallow](../../Magic/Spells/hallow.md)
* [insect plague](../../Magic/Spells/insect-plague.md)
* [legend lore](../../Magic/Spells/legend-lore.md)
* [mass cure wounds](../../Magic/Spells/mass-cure-wounds.md)
* [planar binding](../../Magic/Spells/planar-binding.md)
* [raise dead](../../Magic/Spells/raise-dead.md)
* [scrying](../../Magic/Spells/scrying.md)

## 6th Level
* [blade barrier](../../Magic/Spells/blade-barrier.md)
* [create undead](../../Magic/Spells/create-undead.md)
* [find the path](../../Magic/Spells/find-the-path.md)
* [forbiddance](../../Magic/Spells/forbiddance.md)
* [harm](../../Magic/Spells/harm.md)
* [heal](../../Magic/Spells/heal.md)
* [heroes' feast](../../Magic/Spells/heroes-feast.md)
* [planar ally](../../Magic/Spells/planar-ally.md)
* [true seeing](../../Magic/Spells/true-seeing.md)
* [word of recall](../../Magic/Spells/word-of-recall.md)

## 7th Level
* [conjure celestial](../../Magic/Spells/conjure-celestial.md)
* [divine word](../../Magic/Spells/divine-word.md)
* [etherealness](../../Magic/Spells/etherealness.md)
* [fire storm](../../Magic/Spells/fire-storm.md)
* [plane shift](../../Magic/Spells/plane-shift.md)
* [regenerate](../../Magic/Spells/regenerate.md)
* [resurrection](../../Magic/Spells/resurrection.md)
* [symbol](../../Magic/Spells/symbol.md)

## 8th Level
* [antimagic field](../../Magic/Spells/antimagic-field.md)
* [control weather](../../Magic/Spells/control-weather.md)
* [earthquake](../../Magic/Spells/earthquake.md)
* [holy aura](../../Magic/Spells/holy-aura.md)

## 9th Level
* [astral projection](../../Magic/Spells/astral-projection.md)
* [gate](../../Magic/Spells/gate.md)
* [mass heal](../../Magic/Spells/mass-heal.md)
* [true resurrection](../../Magic/Spells/true-resurrection.md)

