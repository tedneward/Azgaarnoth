# Wizard
Wizards are supreme magic-users, defined and united as a class by the spells they cast. Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, brute-force mind control, and much more.

You must have an Intelligence score of 13 or higher in order to multiclass in or out of this class.

```
name = 'Wizard'
description = "***Class: Wizard.*** Wizards are supreme magic-users, defined and united as a class by the spells they cast. Drawing on the subtle weave of magic that permeates the cosmos, wizards cast spells of explosive fire, arcing lightning, subtle deception, brute-force mind control, and much more."
```

## Class Features
As a wizard, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|3|2|-|-|-|-|-|-|-|-|[Spellcasting](#spellcasting), [Arcane Recovery](#arcane-recovery)
2nd  |+2|3|3|-|-|-|-|-|-|-|-|[Arcane Tradition](#arcane-tradition)
3rd  |+2|3|4|2|-|-|-|-|-|-|-|
4th  |+2|4|4|3|-|-|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
5th  |+3|4|4|3|2|-|-|-|-|-|-|
6th  |+3|4|4|3|3|-|-|-|-|-|-|[Arcane Tradition](#arcane-tradition) feature
7th  |+3|4|4|3|3|1|-|-|-|-|-|
8th  |+3|4|4|3|3|2|-|-|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
9th  |+4|4|4|3|3|3|1|-|-|-|-|
10th |+4|5|4|3|3|3|2|-|-|-|-|[Arcane Tradition](#arcane-tradition) feature
11th |+4|5|4|3|3|3|2|1|-|-|-|
12th |+4|5|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|5|4|3|3|3|2|1|1|-|-|
14th |+5|5|4|3|3|3|2|1|1|-|-|[Arcane Tradition](#arcane-tradition) feature
15th |+5|5|4|3|3|3|2|1|1|1|-|
16th |+5|5|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|5|4|3|3|3|2|1|1|1|1|
18th |+6|5|4|3|3|3|3|1|1|1|1|[Spell Mastery](#spell-mastery)
19th |+6|5|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|5|4|3|3|3|3|2|2|1|1|[Signature Spells](#signature-spells)

### Hit Points
**Hit Dice**: 1d6 per wizard level

**Hit Points at 1st Level**: 6 + your Constitution modifier

**Hit Points at Higher Levels**: 1d6 (or 4) + your Constitution modifier per wizard level after 1st

```
def everylevel(npc): npc.hits('d6')
```

### Proficiencies
**Armor**: None

**Weapons**: Daggers, darts, slings, quarterstaffs, light crossbows

**Tools**: None

**Saving Throws**: Intelligence, Wisdom

**Skills**: Choose two from Arcana, History, Insight, Investigation, Medicine, and Religion

```
def level1(npc):
    npc.savingthrows.append("WIS")
    npc.savingthrows.append("INT")

    for wpn in ['Dagger', 'Dart', 'Sling', 'Quarterstaff', 'Light crossbow']:
        npc.proficiencies.append(wpn)

    skills = ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion']
    chooseskill(npc, skills)
    chooseskill(npc, skills)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:
* (a) a quarterstaff or (b) a dagger
* (a) a component pouch or (b) an arcane focus
* (a) a scholar's pack or (b) an explorer's pack
* A spellbook

```
    npc.equipment.append("Quarterstaff OR dagger")
    npc.equipment.append("Component pouch OR Arcane focus")
    npc.equipment.append("Scholar's pack OR Explorer's pack")
```

## Spellcasting
*1st-level wizard feature*

As a student of arcane magic, you have a spellbook containing spells that show the first glimmerings of your true power.

```
    spellcasting = fullcaster(npc, 'INT', 'Wizard')
```

### Cantrips
At 1st level, you know three cantrips of your choice from the wizard spell list. You learn additional wizard cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Wizard table.

```
    def setmaxknowncantrips(npc):
        spellcasting.maxcantripsknown = 3 if npc.levels('Wizard') < 4 else 4 if npc.levels('Wizard') < 10 else 5
    npc.defer(lambda npc: setmaxknowncantrips(npc) )
```

### Cantrip Versatility
Whenever you gain a level in this class, you can replace one cantrip you learned from this Spellcasting with another cantrip from the wizard spell list. 

### Spellbook
At 1st level, you have a spellbook containing six 1st-level wizard spells of your choice.

The spells that you add to your spellbook as you gain levels reflect the arcane research you conduct on your own, as well as intellectual breakthroughs you have had about the nature of the multiverse. You might find other spells during your adventures. You could discover a spell recorded on a scroll in an evil wizard's chest, for example, or in a dusty tome in an ancient library.

***Copying a Spell into the Book.*** When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a level for which you have spell slots and if you can spare the time to decipher and copy it.

Copying a spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation.

For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.

***Replacing the Book.*** You can copy a spell from your own spellbook into another book--for example, if you want to make a backup copy of your spellbook. This is just like copying a new spell into your spellbook, but faster and easier, since you understand your own notation and already know how to cast the spell. You need spend only 1 hour and 10 gp for each level of the copied spell.

If you lose your spellbook, you can use the same procedure to transcribe the spells that you have prepared into a new spellbook. Filling out the remainder of your spellbook requires you to find new spells to do so, as normal. For this reason, many wizards keep backup spellbooks in a safe place.

***The Book's Appearance.*** Your spellbook is a unique compilation of spells, with its own decorative flourishes and margin notes. It might be a plain, functional leather volume that you received as a gift from your master, a finely bound gilt-edged tome you found in an ancient library or even a loose collection of notes scrounged together after you lost your previous spellbook in a mishap.

There is no limit to the number of spells in a wizard's spellbook, and many wizards of great experience and renown have not just one spellbook, but vast libraries. These are guarded fiercely, and many a powerful wizard's library has served as the core nucleus (and monetary source) of a new [mage school](../../Organizations/MageSchools/index.md)'s spell library.

Wizards are free to copy any arcane (wizard) spell into their spellbook, regardless of arcane tradition or mage school affiliation.

```
    npc.equipment.append("***Spellbook.*** When you find a wizard spell of 1st level or higher, you can add it to your spellbook if it is of a level for which you have spell slots; the process takes 2 hours and costs 50 gp per level of spell.Once you have spent this time and money, you can prepare the spell just like your other spells. Copying a spell from your spellbook into another spellbook costs half this amount (in time and gold), since you know it already.")

    def spellbookspells(npc):
        spelllist = ','.join(npc.spellcasting['Wizard'].spellbook)
        return spelllist
    npc.defer(lambda npc: npc.traits.append(f"***Spellbook.*** Contents: {spellbookspells(npc)}") )
```

### Preparing and Casting Spells
The Wizard table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of wizard spells that are available for you to cast. To do so, choose a number of wizard spells from your spellbook equal to your Intelligence modifier + your wizard level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you're a 3rd-level wizard, you have four 1st-1evel and two 2nd-level spell slots. With an Intelligence of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination, chosen from your spellbook. If you prepare the 1st-level spell [magic missile](../../Magic/Spells/magic-missile.md), you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of wizard spells requires time spent studying your spellbook and memorizing the incantiations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list.

### Spellcasting Ability
Intelligence is your spellcasting ability for your wizard spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a wizard spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Intelligence modifier

**Spell attack modifier** = your proficiency bonus + your Intelligence modifier

### Ritual Casting
You can cast a wizard spell as a ritual if that spell has the *ritual* tag and you have the spell in your spellbook. You don't need to have the spell prepared.

### Spellcasting Focus
You can use an arcane focus as a spellcasting focus for your wizard spells.

### Learning Spells of 1st Level and Higher
Each time you gain a wizard level, you can add two wizard spells of your choice to your spellbook from the list below--these are "common spells" found all across the world and easily obtained. Each of these spells must be of a level for which you have spell slots, as shown on the Wizard table. On your adventures, you might find other spells that you can add to your spellbook. More exclusive and/or rare spells will only be able to be obtained from adventuring sources.

```
    def setprepared(npc): 
        npc.spellcasting[name].spellsprepared = npc.INTbonus() + npc.levels('Wizard')
    npc.defer(lambda npc: setprepared(npc) )
    spellcasting.spellbook = []
```

## Arcane Recovery
*1st-level wizard feature*

You have learned to regain some of your magical energy by studying your spellbook. Once per day when you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your wizard level (rounded up), and none of the slots can be 6th level or higher.

For example, if you're a 4th-level wizard, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level spell slot or two 1st-level spell slots.

```
    npc.defer(lambda npc: npc.traits.append(f"***Arcane Recovery.*** Once per day when you finish a short rest, you can recover up to {(npc.levels('Wizard') // 2) + (npc.levels('Wizard') % 2)} levels of expended spell slots, none of which can be 6th level or higher.") )
```

## Arcane Tradition
*2nd-level wizard feature*

You choose an arcane tradition. Some are formally taught in mage schools:

* [Abjuration](./Abjuration.md)
* [Arcanist](./Arcanist.md)
* [Artillerist](./Artillerist.md)
* [Astromancy](./Astromancy.md)
* [Battle Magi](./BattleMagi.md)
* [Binder](./Binder.md)
* [Conjuration](./Conjuration.md)
* [Dimensionalism](./Dimensionalism.md)
* [Divination](./Divination.md)
* [Divinity](./Divinity.md)
* [Evocation](./Evocation.md)
* [Ferromancy](./Ferromancy.md)
* [Fleuremancy](./Fleuremancy.md)
* [Floramancy](./Floramancy.md)
* [Geomancy](./Geomancy.md)
* [Green Star](./GreenStar.md)
* [Hydromancy](./Hydromancy.md)
* [Illusion](./Illusion.md)
* [Incantation](./Incantation.md)
* [Jaunter](./Jaunter.md)
* [Kinetics](./Kinetics.md)
* [Lore Mastery](./LoreMastery.md)
* [Mentalism](./Mentalism.md)
* [Psionics](./Psionics.md)
* [Pyromancy](./Pyromancy.md)
* [Reanimation](./Reanimation.md)
* [Runecraft](./Runecraft.md)
* [Scrymancy](./Scrymancy.md)
* [Soulbinding](./Soulbinding.md)
* [Spectral Agent](SpectralAgent.md)
* [Symbarch](./Symbarch.md)
* [Theurgy](./Theurgy.md)
* [Transmutation](./Transmutation.md)
* [War Magic](./WarMagic.md)

Your choice grants yous at 2nd level and again at 6th, 10th, and 14th level.

Note that many of the [Mage Schools](../../Organizations/MageSchools/index.md) have their own, unique, arcane traditions; being a part of that tradition will tie you to that school in some capacity or as part of your history. However, while many mage schools have an (exclusive) arcane tradition, not all arcane traditions belong exclusively to a mage school. 

Note that many mage schools will shun contact with those who are not of their mage school while other schools are fine with other schools but shun those who are not part of *any* mage school (calling them "wilders"). Some schools look to recruit from the unaffiliated, while still others recognize the unaffiliated as great sources of inspiration.

There are some arcane traditions which choose to not follow the mage school tradition:

* [Ancient Magic](./AncientMagic.md): These magi are those that have discovered some scrap of Eldar lore that has led to deep insights into how Eldar magic worked. They are often highly jealous of their discoveries, and refuse to share their secrets except with a precious few (usually only an apprentice).
* [Arcane Experimenter](./ArcaneExperimenter.md): Arcane experimenters are often too fast and loose with rules (and concerns for safety) for the comfort of other casters. They are always willing to take on new students to help them with their experiments, but apprentices often find out (too late) that the job comes with a hefty amount of risk.
* [Bladesinger](./Bladesinger.md): Bladesingers are generally taught in one-on-one master/apprentice relationships, and not in formal schools anymore. Some Bladesingers in permanent residence at a [dueling college](../../Organizations/DuelingColleges/index.md) will take on apprentices, but these are almost always one-on-one pairings.
* [Hedge Magi](./HedgeMagi.md): Often called "wilders" by those in mage schools, hedge magi are those magi who come to understand magic on their own terms rather than be "constrained" by the rules, traditions, or politics of a mage school.
* [Nethermancers](./Nethermancy.md): Many nethermancers study alone, but some will form small cells that vaguely resemble a [school](../../Organizations/MageSchools/Nethermancers.md) for a period of time. While nethermancers are not persecuted like some other magi, many commoners 
* [Onomancers](./Onomancy.md): The study of true names is not one to be done collectively.
* [Voidmancy](./Voidmancy.md): Voidmancers draw from powers that many (most) others would prefer left entirely alone. Voidmancers aren't banished or illegal like Enchanters, Bloodmancers, or Hemonacers, but are often judged "questionable", like Necromancers, and often made out to be the villain when anything arcane goes wrong nearby. Some Voidmancers find a home in a school, but others prefer solitude and take few apprentices.

... and there are those mage schools that choose not (or dare not) practice openly:

* [Bloodmancers](./Bloodmancer.md): Those who draw power from life's blood can expect to be persecuted on sight.
* [Emomancy](./Emomancy.md) and [Enchantment](./Enchantment.md): Those wizards who manipulate the emotional spectrum are widely distrusted all across Azgaarnoth. Those who would study it will need to find an existing master Emomancer or Enchanter to pursue this tradition. That's never stopped those who want to study the power of mortal emotion, however--just made them harder to find.
* [Necromancy](./Necromancy.md): Like all things related to the undead, necromancers often need to practice their skills in secret. However, several necromantic mage schools do operate in the open, either because they have political protection, or because their self-imposed oaths provide some degree of guarantee to the locals (such as the [Night's Blessing](../../Organizations/MageSchools/NightsBlessing.md) school, which studies necromancy as part of its pursuit of the studies of life and healing).

Those who would study with any of these shunned traditions must typically search for a master at great length, and often must keep moving from town to town lest they be discovered and "dealt with" by the locals.

### Arcane Tradition Spells
As a mage grows in skill, they will need to look for opportunities to gain new spells in their spellbook. Often a mage will return to their school or former master to have an opportunity to gain new spells, if they are on good terms with them. However, doing so too often can feel a touch degrading, and many schools (and masters) will demand new spells in turn as trade. 

Note that many spells in use across the Azgaarnothian lands are "restricted", in the sense that those who know those spells are reluctant to allow the spell's text to be in the hands of "just anyone". Any spell listed [below](#core-wizard-spells) (which includes all those listed in the *Player's Handbook*) is considered a "core" spell and thus easily accessible to any Wizard; any spell not listed there is "restricted" and therefore must be obtained through some alternative means. (*GM Note: This is one of the primary uses of the [Mage Schools](../../Organizations/MageSchools/index.md), to serve as a source for restricted spells.*) Different mage schools will have different rules, guidelines, or prices for their restricted spells.

For those magi that are not a part of a school, obtaining spells is trickier. Some schools or magi will be happy to trade spells in a spellbook with one another if they are of the same or similar mindset (tradition). Some will do so for money. Some will require a "favor", others might refuse until persuaded. Others will share spells only with others of their hidden faction--meaning a spellcaster will need to find others like them in order to gain acces to the "good stuff".

For those magi who are part of a shunned tradition, new spells must almost always be found "in the wild" via lost spellbooks, spell scrolls, 

```
def level2(npc):
    # Choose subclass
    (_, subclass) = choose("Choose an Arcane Tradition:", subclasses)
    npc.subclasses[allclasses['Wizard']] = subclass
    npc.description.append(subclass.description)
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

## Spell Mastery
*18th-level wizard feature*

You have achieved such mastery over certain spells that you can cast them at will. Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.

By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.

```
def level18(npc):
    npc.traits.append("***Spell Mastery.*** You can cast the (Choose a 1st-level wizard spell and a 2nd-level wizard spell that are in your spellbook) spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal.")
```

## Signature Spells
*20th-level wizard feature*

You gain mastery over two powerful spells and can cast them with little effort. Choose two 3rd-level wizard spells in your spellbook as your signature spells. You always have these spells prepared, they don't count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or long rest.

If you want to cast either spell at a higher level, you must expend a spell slot as normal.

```
def level20(npc):
    npc.traits.append("***Signature Spells (Each recharges on short or long rest).*** You always have the spells (Choose two 3rd-level wizard spells in your spellbook) prepared, they don't count against the number of spells you have prepared, and you can cast each of them once at 3rd level without expending a spell slot. When you do so, you can't do so again until you finish a short or long rest. If you want to cast either spell at a higher level, you must expend a spell slot as normal.")
```

---

# "Core" Wizard Spells
This is a list of the spells accessible to any wizard throughout Azgaarnoth (under most normal circumstances--it is possible, for example, that a wizard character came to power outside of any of the normal backgrounds thus has a very paltry spellbook to start as a handicap). 

> ### GM Notes
> These are all the spells found in the *Player's Handbook*, with few additions. In game terms, these spells are common spells as classified by the [White Winds](../../Organizations/MageSchools/WhiteWinds.md) school, and are always accessible for copy into a wizard's spellbook for a nominal fee.

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
* [alarm](../../Magic/Spells/alarm.md)
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
* [find familiar](../../Magic/Spells/find-familiar.md)
* [fog cloud](../../Magic/Spells/fog-cloud.md)
* [grease](../../Magic/Spells/grease.md)
* [identify](../../Magic/Spells/identify.md)
* [illusory script](../../Magic/Spells/illusory-script.md)
* [jump](../../Magic/Spells/jump.md)
* [longstrider](../../Magic/Spells/longstrider.md)
* [mage armor](../../Magic/Spells/mage-armor.md)
* [magic missile](../../Magic/Spells/magic-missile.md)
* [protection from evil and good](../../Magic/Spells/protection-from-evil-and-good.md)
* [ray of sickness](../../Magic/Spells/ray-of-sickness.md)
* [shield](../../Magic/Spells/shield.md)
* [silent image](../../Magic/Spells/silent-image.md)
* [sleep](../../Magic/Spells/sleep.md)
* [tasha's hideous laughter](../../Magic/Spells/tashas-hideous-laughter.md)
* [tenser's floating disk](../../Magic/Spells/tensers-floating-disk.md)
* [thunderwave](../../Magic/Spells/thunderwave.md)
* [unseen servant](../../Magic/Spells/unseen-servant.md)
* [witch bolt](../../Magic/Spells/witch-bolt.md)

## 2nd Level
* [alter self](../../Magic/Spells/alter-self.md)
* [arcane lock](../../Magic/Spells/arcane-lock.md)
* [blindness/deafness](../../Magic/Spells/blindness-deafness.md)
* [blur](../../Magic/Spells/blur.md)
* [cloud of daggers](../../Magic/Spells/cloud-of-daggers.md)
* [continual flame](../../Magic/Spells/continual-flame.md)
* [crown of madness](../../Magic/Spells/crown-of-madness.md)
* [darkness](../../Magic/Spells/darkness.md)
* [darkvision](../../Magic/Spells/darkvision.md)
* [detect thoughts](../../Magic/Spells/detect-thoughts.md)
* [enlarge/reduce](../../Magic/Spells/enlarge-reduce.md)
* [flaming sphere](../../Magic/Spells/flaming-sphere.md)
* [gentle repose](../../Magic/Spells/gentle-repose.md)
* [gust of wind](../../Magic/Spells/gust-of-wind.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [invisibility](../../Magic/Spells/invisibility.md)
* [knock](../../Magic/Spells/knock.md)
* [levitate](../../Magic/Spells/levitate.md)
* [locate object](../../Magic/Spells/locate-object.md)
* [magic mouth](../../Magic/Spells/magic-mouth) (ritual.md)
* [magic weapon](../../Magic/Spells/magic-weapon.md)
* [Melf's acid arrow](../../Magic/Spells/melfs-acid-arrow.md)
* [mirror image](../../Magic/Spells/mirror-image.md)
* [misty step](../../Magic/Spells/misty-step.md)
* [Nystul's magic aura](../../Magic/Spells/nystuls-magic-aura.md)
* [phantasmal force](../../Magic/Spells/phantasmal-force.md)
* [ray of enfeeblement](../../Magic/Spells/ray-of-enfeeblement.md)
* [rope trick](../../Magic/Spells/rope-trick.md)
* [scorching ray](../../Magic/Spells/scorching-ray.md)
* [see invisibility](../../Magic/Spells/see-invisibility.md)
* [shatter](../../Magic/Spells/shatter.md)
* [spider climb](../../Magic/Spells/spider-climb.md)
* [suggestion](../../Magic/Spells/suggestion.md)
* [web](../../Magic/Spells/web.md)

## 3rd Level
* [animate dead](../../Magic/Spells/animate-dead.md)
* [bestow curse](../../Magic/Spells/bestow-curse.md)
* [blink](../../Magic/Spells/blink.md)
* [clairvoyance](../../Magic/Spells/clarivoyance.md)
* [counterspell](../../Magic/Spells/counterspell.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [fear](../../Magic/Spells/fear.md)
* [feign death](../../Magic/Spells/feign-death.md)
* [fireball](../../Magic/Spells/fireball.md)
* [fly](../../Magic/Spells/fly.md)
* [gaseous form](../../Magic/Spells/gaseous-form.md)
* [glyph of warding](../../Magic/Spells/glyph-of-warding.md)
* [haste](../../Magic/Spells/haste.md)
* [hypnotic pattern](../../Magic/Spells/hypnotic-pattern.md)
* [leomund's tiny hut](../../Magic/Spells/leomunds-tiny-hut.md)
* [lightning bolt](../../Magic/Spells/lightning-bolt.md)
* [magic circle](../../Magic/Spells/magic-circle.md)
* [major image](../../Magic/Spells/major-image.md)
* [nondetection](../../Magic/Spells/nondetection.md)
* [phantom steed](../../Magic/Spells/phantom-steed.md)
* [protection from energy](../../Magic/Spells/protection-from-energy.md)
* [remove curse](../../Magic/Spells/remove-curse.md)
* [sending](../../Magic/Spells/sending.md)
* [sleet storm](../../Magic/Spells/sleet-storm.md)
* [slow](../../Magic/Spells/slow.md)
* [stinking cloud](../../Magic/Spells/stinking-cloud.md)
* [tongues](../../Magic/Spells/tongues.md)
* [vampiric touch](../../Magic/Spells/vampiric-touch.md)
* [water breathing](../../Magic/Spells/water-breathing.md) (ritual)

## 4th Level
* [arcane eye](../../Magic/Spells/arcane-eye.md)
* [banishment](../../Magic/Spells/banishment.md)
* [blight](../../Magic/Spells/blight.md)
* [confusion](../../Magic/Spells/confusion.md)
* [conjure minor elementals](../../Magic/Spells/conjure-minor-elementals.md)
* [control water](../../Magic/Spells/control-water.md)
* [dimension door](../../Magic/Spells/dimension-door.md)
* [Evard's black tentacles](../../Magic/Spells/evards-black-tentacles.md)
* [fabricate](../../Magic/Spells/fabricate.md)
* [fire shield](../../Magic/Spells/fire-shield.md)
* [greater invisibility](../../Magic/Spells/greater-invisibility.md)
* [hallucinatory terrain](../../Magic/Spells/hallucinatory-terrain.md)
* [ice storm](../../Magic/Spells/ice-storm.md)
* [Leomund's secret chest](../../Magic/Spells/leomunds-secret-chest.md)
* [locate creature](../../Magic/Spells/locate-creature.md)
* [Mordenkainen's faithful hound](../../Magic/Spells/mordenkainens-faithful-hound.md)
* [Mordenkainen's private sanctum](../../Magic/Spells/mordenkainens-private-sanctum.md)
* [Otiluke's resilient sphere](../../Magic/Spells/otilukes-resilient-sphere.md)
* [phantasmal killer](../../Magic/Spells/phantasmal-killer.md)
* [polymorph](../../Magic/Spells/polymorph.md)
* [stone shape](../../Magic/Spells/stone-shape.md)
* [stoneskin](../../Magic/Spells/stoneskin.md)
* [wall of fire](../../Magic/Spells/wall-of-fire.md)

## 5th Level
* [animate objects](../../Magic/Spells/animate-objects.md)
* [Bigby's hand](../../Magic/Spells/bigbys-hand.md)
* [cloudkill](../../Magic/Spells/cloudkill.md)
* [cone of cold](../../Magic/Spells/cone-of-cold.md)
* [conjure elemental](../../Magic/Spells/conjure-elemental.md)
* [contact other plane](../../Magic/Spells/contact-other-plane.md)
* [creation](../../Magic/Spells/creation.md)
* [dominate person](../../Magic/Spells/dominate-person.md)
* [dream](../../Magic/Spells/dream.md)
* [geas](../../Magic/Spells/geas.md)
* [hold monster](../../Magic/Spells/hold-monster.md)
* [legend lore](../../Magic/Spells/legend-lore.md)
* [mislead](../../Magic/Spells/mislead.md)
* [modify memory](../../Magic/Spells/modify-memory.md)
* [passwall](../../Magic/Spells/passwall.md)
* [planar binding](../../Magic/Spells/planar-binding.md)
* [Rary's telepathic bond](../../Magic/Spells/rarys-telepathic-bond.md)
* [scrying](../../Magic/Spells/scrying.md)
* [seeming](../../Magic/Spells/seeming.md)
* [telekinesis](../../Magic/Spells/telekinesis.md)
* [teleportation circle](../../Magic/Spells/teleportation-circle.md)
* [wall of force](../../Magic/Spells/wall-of-force.md)
* [wall of stone](../../Magic/Spells/wall-of-stone.md)

## 6th Level
* Arcane Gate
* Chain Lightning
* Circle of Death
* Contingency
* Create Undead
* Disintegrate
* Drawmij's Instant Summons
* Eyebite
* Flesh to Stone
* Globe of Invulnerability
* Guards and Wards
* Magic Jar
* Mass Suggestion
* Move Earth
* Otiluke's Freezing Sphere
* Otto's Irresistible Dance
* Programmed Illusion
* Sunbeam
* True Seeing
* Wall of Ice

## 7th Level
* Delayed Blast Fireball
* Etherealness
* Finger of Death
* Forcecage
* Mirage Arcane
* Mordenkainen's Magnificent Mansion
* Mordenkainen's Sword
* Plane Shift
* Prismatic Spray
* Project Image
* Reverse Gravity
* Sequester
* Simulacrum
* Symbol
* Teleport

## 8th Level
* Antimagic Field
* Antipathy/Sympathy
* Clone
* Control Weather
* Demiplane
* Dominate Monster
* Feeblemind
* Incendiary Cloud
* Maze
* Mind Blank
* Power Word: Stun
* Sunburst
* Telepathy

## 9th Level
* [astral projection](../../Magic/Spells/astral-projection.md)
* [foresight](../../Magic/Spells/foresight.md)
* Gate
* Imprisonment
* Meteor Swarm
* Power Word: Kill
* Prismatic Wall
* Shapechange
* Time Stop
* True Polymorph
* Weird
* Wish
