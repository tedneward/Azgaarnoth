# Pale Master
> Kneeling down beside the skeletal remains left behind in the aftermath of conflict, the elderly human begins to cast an incantation. The man's irises lose their color and his pupils constrict for a moment. To the horror of his companions, the mindless undead they fought so hard so defeat just moments ago rise up to walk among the living once again, but this time as an army of the dead under their comrade's control. 

The Pale Master is a magic user obsessed with the study of life and death and with harnessing this newfound knowledge to raise an unending cohort of the dead to do their bidding.

> Stretching out a mummified hand wrapped in funeral dressings, the young gnome touches a corpse long since perished. Spectral bandages begin to form around the lifeless body until it is completely covered. As the process is completed, necrotic energies flow through the cadaver, causing it to twitch and contort its form as it rises to its feet; the foul mimicry of life coursing through its now sentient form.

The secrets of necromancy not only allow them to be successful in this quest, but also give them insight into how they can bolster their own form with gifts from the undead, permanently granting them powers of undeath.

> A frenzied undead creature lumbers toward a stoic halfdrow. As the zombie is about to tear into her, she calmly touches its forehead with her own skeletal appendage. The creature turns its rage-fueled eyes back towards the others of its pack, compelled to protect the one it previously sought to feed upon.

Typically those who are capable of performing [undead grafts](/Magic/UndeadGrafts.md) are pale masters.

```
name = 'Pale Master'
description = "***Class: Pale Master.*** The Pale Master is a magic user obsessed with the study of life and death and with harnessing this newfound knowledge to raise an unending cohort of the dead to do their bidding.The secrets of necromancy not only allow them to be successful in this quest, but also give them insight into how they can bolster their own form with gifts from the undead, permanently granting them powers of undeath."
```

## Pre-eminence in Necromancy
Pale Masters are arcane casters who draw upon necromantic lore that provides a macabre power all its own. Some aspire to live forever, effectively becoming immortal. Others are fascinated with death and the fate of souls that are unable to pass into the afterlife. Some pale masters seek to gain power through raising an army of once fallen soldiers to continue the battle once more.

With this obsession to learn every shred of obscure knowledge surrounding the necromantic arts, a sacrifice happens as the pale master tends to become uninterested in other types of magic, except for a select few spells they feel can help them achieve their goals faster. As a result, pale masters have a smaller subset of arcane spells to draw upon when compared to their other arcane brethren. This lack of breadth is offset by the unique abilities they gain while studying their undead subjects.

## Class features
As a pale master, you gain the following class features.

Level|Proficiency Bonus|Creations Known|Macabre Enchantments|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|---------------|--------------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|--|--| 3| 2|--|--|--|--|--|--|--|--|[Spellcasting](#spellcasting), [Aspect of the Dead](#aspect-of-the-dead), [Undead Affinity](#undead-affinity)
2nd  |+2| 3| 2| 3| 3|--|--|--|--|--|--|--|--|[Macabre Creations](#macabre-creations)
3rd  |+2| 3| 2| 3| 4| 2|--|--|--|--|--|--|--|[Deathless Axiom](#deathless-axiom)
4th  |+2| 4| 2| 3| 4| 3|--|--|--|--|--|--|--|Ability Score Improvement
5th  |+3| 4| 2| 4| 4| 3| 2|--|--|--|--|--|--|[Raise Incorporeal Undead](#raise-incorporeal-undead)
6th  |+3| 4| 2| 4| 4| 3| 3|--|--|--|--|--|--|Deathless Axiom feature
7th  |+3| 5| 3| 4| 4| 3| 3| 1|--|--|--|--|--|-
8th  |+3| 5| 3| 4| 4| 3| 3| 2|--|--|--|--|--|Ability Score Improvement
9th  |+4| 5| 3| 4| 4| 3| 3| 3| 1|--|--|--|--|--
10th |+4| 5| 3| 4| 4| 3| 3| 3| 2|--|--|--|--|[Undead Cohort](#undead-cohort)
11th |+4| 6| 3| 4| 4| 3| 3| 3| 2| 1|--|--|--|--
12th |+4| 6| 3| 4| 4| 3| 3| 3| 2| 1|--|--|--|Ability Score Improvement
13th |+5| 6| 4| 5| 4| 3| 3| 3| 2| 1| 1|--|--|--
14th |+5| 6| 4| 5| 4| 3| 3| 3| 2| 1| 1|--|--|Deathless Axiom feature
15th |+5| 6| 4| 5| 4| 3| 3| 3| 2| 1| 1| 1|--|--
16th |+5| 7| 4| 5| 4| 3| 3| 3| 2| 1| 1| 1|--|Ability Score Improvement
17th |+6| 7| 4| 5| 4| 3| 3| 3| 2| 1| 1| 1| 1|--
18th |+6| 7| 4| 5| 4| 3| 3| 3| 3| 1| 1| 1| 1|[Necromastery](#necromastery)
19th |+6| 7| 5| 5| 4| 3| 3| 3| 3| 2| 1| 1| 1|Ability Score Improvement
20th |+6| 7| 5| 5| 4| 3| 3| 3| 3| 2| 2| 1| 1|[Amaranthine Shroud](#amaranthine-shroud)

```
# Creations Known, Macabre Enchantments, Cantrips
palemastertable = {
     1: [0, 0, 3],
     2: [3, 2, 3],
     3: [3, 2, 3],
     4: [4, 2, 3],
     5: [4, 2, 4],
     6: [4, 2, 4],
     7: [5, 3, 4],
     8: [5, 3, 4],
     9: [5, 3, 4],
    10: [5, 3, 4],
    11: [6, 3, 4],
    12: [6, 3, 4],
    13: [6, 4, 5],
    14: [6, 4, 5],
    15: [6, 4, 5],
    16: [7, 4, 5],
    17: [7, 4, 5],
    18: [7, 4, 5],
    19: [7, 5, 5],
    20: [7, 5, 5]
}
```

### Hit Points
**Hit Dice**: 1d8 per pale master level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per pale master level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: light armor

**Weapons**: Daggers, light hammers, sickles, quarterstaffs

**Tools**: None

**Saving Throws**: Constitution, Intelligence

**Skills**: Choose two from Arcana, Deception, History, Intimidation, Investigation, Religion, and Stealth

```
def level1(npc):
    for arm in armor['light']:
        npc.proficiencies.append(arm)
    npc.proficiencies.append("Dagger")
    npc.proficiencies.append("Light hammer")
    npc.proficiencies.append("Sickle")
    npc.proficiencies.append("Quarterstaff")

    npc.savingthrows.append("CON")
    npc.savingthrows.append("INT")

    npc.skills.append(choose("Choose a skill:", ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Religion', 'Stealth']))
    npc.skills.append(choose("Choose a skill:", ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Religion', 'Stealth']))
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:
* (a) a sickle or (b) a quarterstaff
* (a) a component pouch or (b) an arcane focus
* (a) a scholar's pack or (b) a priest's pack
* A grimoire

```
    npc.equipment.append("Sickle OR Quarterstaff")
    npc.equipment.append("Component pouch OR Arcane focus")
    npc.equipment.append("Scholar's pack OR Priest's pack")
    npc.equipment.append("A grimoire")
```

## Spellcasting
*1st-level Pale Master feature*

As a student of necromantic magic, you have obtained a grimoire from which to study spells dealing with the dark arts. Although your study of arcane magic is similar to that of a traditional wizard, you forgo some of their spellcasting prowess in favor of obtaining specialized gifts from your undead subjects.

### Cantrips
At 1st level, you know three cantrips of your choice from the pale master spell list. You learn additional pale master cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Pale Master table.

When you gain a level in this class, you can replace one of the pale master cantrips you know with another cantrip from the pale master spell list.

### Grimoire
At 1st level, you obtain a grimoire, which is the repository of all spells available to you as a pale master. 

> ### A Pale Master's Grimoire
> As this tome contains a significant amount of information about necromancy, as well as a large number of the known necromancy spells in the multiverse, it is quite a rare item indeed. Players may wish to share the details how, where, and from whom they received their grimoire in their character's backstory. Some grimoires have been handed from master to apprentice down through centuries; many pale masters will undertake great risks to obtain another pale master's grimoire in the unfortunate case of the grimoire becoming lost, lest it fall into "the wrong hands."

```
    npc.traits.append("***Grimoire.*** A pale master's grimoire tends to be emblazoned with runes inlaid into a black leather cover, which symbolize the dark magic contained within. Your grimoire is the repository of all spells available to you as a pale master, which you can prepare for use. Your ability to prepare and cast the spells contained within grows, reflecting the research you conduct on your own, as well as intellectual breakthroughs while studying the undead creatures you keep in your cohort. Despite the singular nature of the term, the grimoire can span across multiple physical books. **Replacing the Book.** The grimoire you receive at 1st level is invaluable, entrusted to you when beginning your journey as a pale master. If you lose your grimoire, it will cost you 50 gp per pale master level to replace, and this is before the cost of copying spells into it. Many pale masters will have copies of their grimoire squirreled away in safe locations as backups. **Copying Spells.** When you find an arcane spell of 1st level or higher, you can add it to your spellbook if it is of a level for which you have spell slots and if you can spare the time to decipher and copy it. Copying a spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard or pale master who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation. For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.")
```

### Preparing and Casting Spells
The Pale Master table shows how many spell slots you have to cast your pale master spells of 1st level and higher. To cast one of these spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of pale master spells that are available for you to cast. To do so, choose a number of pale master spells from your grimoire equal to your Intelligence modifier + half your pale master level, rounded down (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you're a 4th-level pale master, you have three 1st-level and three 2nd-level spell slots. With an Intelligence of 14, your list of prepared spells can include four spells of 1st or 2nd level, in any combination, chosen from your grimoire. If you prepare the 1st-level spell [false life](../../Magic/Spells/false-life), you can cast it using a 1st-level or a 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

You can change your list of prepared spells when you finish a long rest. Preparing a new list of pale master spells requires time spent studying your grimoire and memorizing the incantations and gestures you must make to cast the spell: at least 1 minute per spell level for each spell on your list.

### Copying a Spell into the Grimoire
When you find an arcane spell of 1st level or higher, you can add it to your spellbook if it is of a level for which you have spell slots and if you can spare the time to decipher and copy it.

Copying a spell into your spellbook involves reproducing the basic form of the spell, then deciphering the unique system of notation used by the wizard or pale master who wrote it. You must practice the spell until you understand the sounds or gestures required, then transcribe it into your spellbook using your own notation.

For each level of the spell, the process takes 2 hours and costs 50 gp. The cost represents material components you expend as you experiment with the spell to master it, as well as the fine inks you need to record it. Once you have spent this time and money, you can prepare the spell just like your other spells.

### Spellcasting Ability
Intelligence is your spellcasting ability for your pale master spells, since you learn your spells through dedicated study and memorization. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a pale master spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Intelligence modifier

**Spell attack modifier** = your proficiency bonus + your Intelligence modifier

```
    spellcasting = npc.newspellcasting(name, 'INT', name)
    spellcasting.casterclass = allclasses[name]
    spellcasting.slottable = {
        1: [ 2 ],
        2: [ 3 ],
        3: [ 4, 2 ], 
        4: [ 4, 3 ],
        5: [ 4, 3, 2 ],
        6: [ 4, 3, 3 ],
        7: [ 4, 3, 3, 1 ],
        8: [ 4, 3, 3, 2 ],
        9: [ 4, 3, 3, 3, 1 ],
        10: [ 4, 3, 3, 3, 2] ,
        11: [ 4, 3, 3, 3, 2, 1 ],
        12: [ 4, 3, 3, 3, 2, 1 ],
        13: [ 4, 3, 3, 3, 2, 1, 1 ],
        14: [ 4, 3, 3, 3, 2, 1, 1 ],
        15: [ 4, 3, 3, 3, 2, 1, 1, 1 ],
        16: [ 4, 3, 3, 3, 2, 1, 1, 1 ],
        17: [ 4, 3, 3, 3, 2, 1, 1, 1, 1 ],
        18: [ 4, 3, 3, 3, 3, 1, 1, 1, 1 ],
        19: [ 4, 3, 3, 3, 3, 2, 1, 1, 1 ],
        20: [ 4, 3, 3, 3, 3, 2, 2, 1, 1 ]
    }
```

### Ritual Casting
You can cast a pale master spell as a ritual if that spell has the ritual tag and it is from the school of necromancy. You don't need to have the spell prepared. 

### Spellcasting Focus
You can use an arcane focus as a spellcasting focus for your pale master spells. At 3rd level, you obtain your Undead Graft, which becomes your spellcasting focus for your magic, allowing you to cast spells with it and perform the somatic components of spells even when you have weapons or a shield in one or both hands.

### Your Grimoire
Your grimoire contains all of the spells you can prepare for use. Your ability to prepare and cast the spells contained within grows, reflecting the research you conduct on your own, as well as intellectual breakthroughs while studying the undead creatures you keep in your cohort.

Despite the singular nature of the term, the grimoire can span across multiple physical books.

**Replacing the Book**. The grimoire you receive at 1st level is invaluable, entrusted to you when beginning your journey as a pale master. If you lose your grimoire, it will cost you 50 gp per pale master level to replace, and this is before the cost of copying spells into it. Many pale masters will have copies of their grimoire squirreled away in safe locations as backups.

**The Grimoire's Appearance**. A pale master's grimoire tends to be emblazoned with runes inlaid into a black leather cover, which symbolize the dark magic contained within.


## Undead Affinity
*1st-level pale master feature*

Your mere touch can force an undead creature to follow your commands for a short time. Make a melee spell attack against an undead creature with a challenge rating equal to or less than half of your pale master level (rounded down). On a hit, the creature will follow your commands for 1 round per pale master level. When the duration expires, the undead creature returns to its former allegiance, if any. 

If the undead creature has an Intelligence of 6 or more, you make the attack with disadvantage. If it has an Intelligence of 12 or more it is immune to this feature.

You can use this feature a number of times equal to your Intelligence modifier (a minimum of once), but can only control one undead creature at a time. You regain expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Undead Affinity ({npc.INTbonus()}/Recharges on long rest).*** *Melee Spell Attack:* +{npc.proficiencybonus() + npc.INTbonus()} to hit, reach 5ft., one target. Hit: Target creature will follow your commands for {npc.levels(name)} rounds; when the duration expires, the undead creature returns to its former allegiance, if any. If the undead creature has an Intelligence of 6 or more, you make the attack with disadvantage; undead creatures with an Intelligence of 12 or more are immune to this feature.") )
```

## Aspect of the Dead
*1st-level, 6th-level, 11th-level, and 17th-level Pale Master features*

Your form begins to take on the qualities of undeath: an unnerving side effect of spending long periods of time around the dead. This transformation becomes more pronounced as you gain levels in this class.

At 1st level, your composure allows you to shrug off an attack that would normally break your concentration. Once per long rest, when you are concentrating on a spell from the school of necromancy and take damage, you may roll your concentration check with advantage.

```
    npc.traits.append("***Aspect of the Dead (Recharges on long rest).*** While concentrating on a spell from the school of necromancy, if you take damage and need to make a concentration check, you roll with advantage.")
```

At 6th level, your time studying the dead has clarified many mysteries formerly shrouded by the dark. You gain darkvision out to a range of 60 feet. If you already have darkvision, its range is extended by 30 feet.

```
def level6(npc):
    if 'darkvision' in npc.senses: npc.senses['darkvision'] += 30
    else: npc.senses['darkvision'] = 60 
```

At 11th level, your time spent among decay has inured you to the ravages of corpse-borne plagues, granting you resistance to poison and necrotic damage. Additionally, you are immune to disease and can't be poisoned. 

```
def level11(npc):
    npc.damageresistances.append('poison')
    npc.damageresistances.append('necrotic')
    npc.conditionimmunities.append('diseased')
    npc.conditionimmunities.append('poisoned')
```

At 17th level, your form bears a close resemblance to the undead you study, allowing you to age at a slower rate. For every 10 years that pass, your body ages only 1 year, and you are immune to being magically aged.

```
def level17(npc):
    npc.traits.append("***Aspect of the Dead.*** For every 10 years that pass, your body ages only 1 year, and you are immune to being magically aged.")
```

## Macabre Creations
*2nd-level pale master feature*

You gain the ability to enhance mundane items with undead enchantments. The magic items you create with this feature are take the form of undead armors, weapons or wonderous items.

### Macabre Creations Known
When you gain this feature, pick three pale master macabre creations to learn, choosing from the ["Macabre Creations" page](MacabreCreations.md). You learn additional creations of your choice when you reach certain level in this class, as shown in the Creations Known column of the Pale Master table.

Whenever you gain a level in this class, you can replace one of the macabre creations you learned with a new one.

### Crafting a Macabre Creation
Whenever you finish a long rest, you can craft a macabre creation, turning it into a magic item. The magical nature of these creations is specific to certain kinds of objects, as detailed in the creation's description. If the item requires attunement, you can attune yourself to it the instant you create the item, or you can forgo attunement so that someone else can attune to the item. If you decide to attune to the item later, you must do so using the normal process for attunement.

The magical properties of a macabre creation remain indefinitely, but when you die, the magic used in its creation vanishes after a number of days have passed equal to your Intelligence modifier (minimum of 1 day). However, the magic used in its creation will instantly vanish if you give up your knowledge of the macabre creation for another one. 

You can only create one macabre creation per long rest. The maximum number of macabre creations you can have active at a time appears in the Macabre Enchantments column of the Pale Master table. If you try to exceed your maximum number of creations, the oldest one immediately loses its magical properties, and then the newest macabre creation is completed.

```
def level2(npc):
    npc.macabrecreationsknown = 3
    npc.macabrecreations = []

    npc.defer(lambda npc: npc.traits.append(f"***Macabre Creations.*** Whenever you finish a long rest, you can craft a macabre creation, turning it into a magic item. The magical nature of these creations is specific to certain kinds of objects, as detailed in the creation's description. If the item requires attunement, you can attune yourself to it the instant you create the item, or you can forgo attunement so that someone else can attune to the item. If you decide to attune to the item later, you must do so using the normal process for attunement. The magical properties of a macabre creation remain indefinitely, but when you die, the magic used in its creation vanishes after {npc.INTbonus()} days have passed. However, the magic used in its creation will instantly vanish if you give up your knowledge of the macabre creation for another one.  You can only create one macabre creation per long rest. You can have active up to {palemastertable[npc.levels(name)][1]} at a time. If you try to exceed your maximum number of creations, the oldest one immediately loses its magical properties, and then the newest macabre creation is completed.") )

    #choosemacabrecreation(npc)
    #choosemacabrecreation(npc)
    #choosemacabrecreation(npc)
```

## Deathless Axioms
*3rd-level pale master feature*

The study of the dark arts is ancient, stretching back to the earliest discoveries of magic.

You choose a deathless axiom, which forms the foundation of your unending subjugation of the dark arts. The boons of undeath are granted as a result of your obsession in studying one of five elegies: 

* [Decay](PaleMaster/Decay.md)
* [Dread](PaleMaster/Dread.md)
* [Enduring](PaleMaster/Enduring.md)
* [Revenge](PaleMaster/Revenge.md)
* [Twilight](PaleMaster/Twilight.md).

Your choice grants you features at 3rd level and again at 6th and 14th level.

```
def level3(npc):
    # Choose subclass
    (_, subclass) = choose("Choose a Deathless Axiom:", subclasses)
    npc.subclasses[allclasses['Pale Master']] = subclass
    npc.description.append(subclass.description)
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

## Raise Incorporeal Undead
*5th-level pale master feature*

You can create an undead servant from the fading soul of a fallen creature. You choose a humanoid that has been dead no longer than 24 hours and create a [specter](../../Creatures/Undead/Specter.md). Roll initiative for the specter, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to the specter, it defends itself but otherwise takes no actions. The specter is under your control for 10 minutes, after which it disappears. 

Beginning at 12th level, you can raise a [banshee](../../Creatures/Undead/Banshee.md) instead of a specter.

You can use this feature a number of times equal to your Intelligence modifier (a minimum of once), but can only raise one incorporeal undead at a time. You regain any expended uses when you finish a long rest.

```
def level5(npc):
    npc.defer(lambda npc: npc.traits.append("***Raise Incorporeal Undead ({npc.INTbonus()}/Recharges on long rest).*** You choose a humanoid that has been dead no longer than 24 hours and create a {'specter' if npc.levels(name) < 12 else 'banshee'}. Roll initiative for the {'specter' if npc.levels(name) < 12 else 'banshee'}, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to it, it defends itself but otherwise takes no actions. It is under your control for 10 minutes, after which it disappears.") )
```

## Undead Cohort
*10th-level pale master feature*

You are able to create an undead creature specific to your chosen archetype.

## Necromastery
*10th-level pale master feature*

You have gained mastery over certain necromancy spells, allowing you to cast them at will. 

Choose a 1st-level pale master spell and a 2nd-level pale master spell that are in your grimoire and belong to the necromancy school of magic. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal. 

By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.

```
def level10(npc):
    npc.spellcasting[name].atwill = [ 'CHOOSE-1st-level-PaleMaster', 'CHOOSE-2nd-level-PaleMaster' ]
    npc.traits.append("***Necromastery.*** Choose a 1st-level pale master spell and a 2nd-level pale master spell that are in your grimoire and belong to the necromancy school of magic. You can cast those spells at their lowest level without expending a spell slot when you have them prepared. If you want to cast either spell at a higher level, you must expend a spell slot as normal. By spending 8 hours in study, you can exchange one or both of the spells you chose for different spells of the same levels.")
```

## Amaranthine Shroud
*20th-level pale master feature*

When you take a single source of damage that would knock you unconscious or kill you outright, you may use this feature as a reaction to take no damage instead.

Once you use this feature, you can't use it again until you complete a short or long rest.

```
def level20(npc):
    npc.reactions.append("***Amaranthine Shroud (Recharges on short or long rest).*** When you take a single source of damage that would knock you unconscious or kill you outright, you take no damage instead.")
```

---

# Pale Master Spells
Pale master spells are a mix of the arcane, the divine, and the necrotic. However, principally they draw upon arcane forces for their spells, and as such their spells can be learned by wizards. Pale masters are also able to learn wizard spells, but typically choose not to, since doing so would distract from their more... pure... work. Wizards can certainly learn pale master spells, but often find the influence of doing so to be... life-altering... and often choose not to. (Unless, of course, the wizard is already studying necromancy; many of the necromantic-minded find themselves drawn to multiclass as a pale master eventually.)

> ### Game Notes
> Pale masters are capable of copying spells out of a wizard spell book, and likewise for wizards out of a pale master spellbook, for the usual time and cost. Pale masters have a similar relationship to sorcerer and warlock spells as wizards do.
> Note also that, unlike many other class' spells, almost all pale master spells are known at the time of character creation; it is rare among pale masters to keep spells from one another, so barring the GM's decision, any spell on the list is accessible.

## cantrip-Level Spells
* [Balance](../../Magic/Spells/balance.md)
* [Blood Siphon](../../Magic/Spells/blood-siphon.md)
* [Bloodlink](../../Magic/Spells/bloodlink.md)
* [Bolster](../../Magic/Spells/bolster.md)
* [Chill Touch](../../Magic/Spells/chill-touch.md)
* [Corruption](../../Magic/Spells/corruption.md)
* [Dancing Lights](../../Magic/Spells/dancing-lights.md)
* [Eidolic Chains](../../Magic/Spells/eidolic-chains.md)
* [Gloom](../../Magic/Spells/gloom.md)
* [Grim Scythe](../../Magic/Spells/grim-scythe.md)
* [Grimlore's Influence](../../Magic/Spells/grimlores-influence.md)
* [Infestation](../../Magic/Spells/infestation.md)
* [Manipulate Shadow](../../Magic/Spells/manipulate-shadow.md)
* [Minor Illusion](../../Magic/Spells/minor-illusion.md)
* [Night Terror](../../Magic/Spells/night-terror.md)
* [Pacify](../../Magic/Spells/pacify.md)
* [Peaceful Valediction](../../Magic/Spells/peaceful-valediction.md)
* [Poison Spray](../../Magic/Spells/poison-spray.md)
* [Rancorous-Mist Blade](../../Magic/Spells/rancorous-mist-blade.md)
* [Reaver's Touch](../../Magic/Spells/reavers-touch.md)
* [Scourge](../../Magic/Spells/scourge.md)
* [Shadow Embrace](../../Magic/Spells/shadow-embrace.md)
* [Shadow Ink](../../Magic/Spells/shadow-ink.md)
* [Shawl of the Unseen](../../Magic/Spells/shawl-of-the-unseen.md)
* [Shocking Grasp](../../Magic/Spells/shocking-grasp.md)
* [Song of the Dead](../../Magic/Spells/song-of-the-dead.md)
* [Spare the Dying](../../Magic/Spells/spare-the-dying.md)
* [Spare the Living](../../Magic/Spells/spare-the-living.md)
* [Toll the Dead](../../Magic/Spells/toll-the-dead.md)
* [Unholy Flame](../../Magic/Spells/unholy-flame.md)
* [Waning Touch](../../Magic/Spells/waning-touch.md)
 
## 1st-Level Spells
* [Acrid Delight](../../Magic/Spells/acrid-delight.md)
* [Alacritous Interpretation](../../Magic/Spells/alacritous-interpretation.md)
* [Animate Cranium](../../Magic/Spells/animate-cranium.md)
* [Arms of Hadar](../../Magic/Spells/arms-of-hadar.md)
* [Bane](../../Magic/Spells/bane.md)
* [Bone Storm](../../Magic/Spells/bone-storm.md)
* [Cause Fear](../../Magic/Spells/cause-fear.md)
* [Creeping Crawling Claw](../../Magic/Spells/creeping-crawling-claw.md)
* [Cursed with Undeath](../../Magic/Spells/cursed-with-undeath.md)
* [Dark Pact](../../Magic/Spells/dark-pact.md)
* [Dead Man's Tell](../../Magic/Spells/dead-mans-tell.md)
* [Death's Grasp](../../Magic/Spells/deaths-grasp.md)
* [Dread](../../Magic/Spells/dread.md)
* [False Life](../../Magic/Spells/false-life.md)
* [Grimlore's Shadowblight](../../Magic/Spells/grimlores-shadowblight.md)
* [Guillotine](../../Magic/Spells/guillotine.md)
* [Inaudible](../../Magic/Spells/inaudible.md)
* [Inflict Wounds](../../Magic/Spells/inflict-wounds.md)
* [Interpret Bone](../../Magic/Spells/interpret-bone.md)
* [Larloch's Minor Drain](../../Magic/Spells/larlochs-minor-drain.md)
* [Misery](../../Magic/Spells/misery.md)
* [Murmurs of the Restless](../../Magic/Spells/murmurs-of-the-restless.md)
* [Ray of Sickness](../../Magic/Spells/ray-of-sickness.md)
* [Rot](../../Magic/Spells/rot.md)
* [Shed Skin](../../Magic/Spells/shed-skin.md)
* [Unseen Servant](../../Magic/Spells/unseen-servant.md)
* [Witch Bolt](../../Magic/Spells/witch-bolt.md)
 
## 2nd-Level Spells
* [Analyze Blood](../../Magic/Spells/analyze-blood.md)
* [Blindness/Deafness](../../Magic/Spells/blindness-deafness.md)
* [Darkness](../../Magic/Spells/darkness.md)
* [Darkvision](../../Magic/Spells/darkvision.md)
* [Desecration](../../Magic/Spells/desecration.md)
* [Detect Familiar](../../Magic/Spells/detect-familiar.md)
* [Drain Life](../../Magic/Spells/drain-life.md)
* [Elemental Anguish](../../Magic/Spells/elemental-anguish.md)
* [Gentle Repose](../../Magic/Spells/gentle-repose.md)
* [Grimlore's Shadowgrasp](../../Magic/Spells/grimlores-shadowgrasp.md)
* [Lifetap](../../Magic/Spells/lifetap.md)
* [Manacle of Burden](../../Magic/Spells/manacle-of-burden.md)
* [Misty Step](../../Magic/Spells/misty-step.md)
* [Necrotic Visage](../../Magic/Spells/necrotic-visage.md)
* [Ray of Enfeeblement](../../Magic/Spells/ray-of-enfeeblement.md)
* [Shadow Bind](../../Magic/Spells/shadow-bind.md)
* [Shadow Blade](../../Magic/Spells/shadow-blade.md)
* [Silence](../../Magic/Spells/silence.md)
* [Silvanus' Blessing](../../Magic/Spells/silvanus-blessing.md)
* [Unseat Hand](../../Magic/Spells/unseat-hand.md)
 
## 3rd-Level Spells
* [Animate Dead](../../Magic/Spells/animate-dead.md)
* [Bestow Curse](../../Magic/Spells/bestow-curse.md)
* [Counterspell](../../Magic/Spells/counterspell.md)
* [Dispel Magic](../../Magic/Spells/dispel-magic.md)
* [Fear](../../Magic/Spells/fear.md)
* [Feign Death](../../Magic/Spells/feign-death.md)
* [Grimlore's Affliction](../../Magic/Spells/grimlores-affliction.md)
* [Life Transference](../../Magic/Spells/life-transference.md)
* [Lunar Blessing](../../Magic/Spells/lunar-blessing.md)
* [Mummify](../../Magic/Spells/mummify.md)
* [Phantom Steed](../../Magic/Spells/phantom-steed.md)
* [Poisoned Heart](../../Magic/Spells/poisoned-heart.md)
* [Remove Curse](../../Magic/Spells/remove-curse.md)
* [Revivify](../../Magic/Spells/revivify.md)
* [Speak with Dead](../../Magic/Spells/speak-with-dead.md)
* [Stinking Cloud](../../Magic/Spells/stinking-cloud.md)
* [Summon Undead](../../Magic/Spells/summon-undead.md)
* [Tongues](../../Magic/Spells/tongues.md)
* [Vampiric Touch](../../Magic/Spells/vampiric-touch.md)
* [Water Breathing](../../Magic/Spells/water-breathing.md)
 
## 4th-Level Spells
* [Army of the Dead](../../Magic/Spells/army-of-the-dead.md)
* [Blight](../../Magic/Spells/blight.md)
* [Devastate Undead](../../Magic/Spells/devastate-undead.md)
* [Dusk Arrows](../../Magic/Spells/dusk-arrows.md)
* [Embers](../../Magic/Spells/embers.md)
* [Evard's Black Tentacles](../../Magic/Spells/evards-black-tentacles.md)
* [Grimlore's Withering Coils](../../Magic/Spells/grimlores-withering-coils.md)
* [Hallowing Curse](../../Magic/Spells/hallowing-curse.md)
* [Hernan's Hemorrhage](../../Magic/Spells/hernans-hemorrhage.md)
* [Phantasmal Killer](../../Magic/Spells/phantasmal-killer.md)
* [Plague](../../Magic/Spells/plague.md)
* [Shadow of Moil](../../Magic/Spells/shadow-of-moil.md)
* [Vacillate](../../Magic/Spells/vacillate.md)
 
## 5th-Level Spells
* [Cloudkill](../../Magic/Spells/cloudkill.md)
* [Contagion](../../Magic/Spells/contagion.md)
* [Danse Macabre](../../Magic/Spells/danse-macabre.md)
* [Enervation](../../Magic/Spells/enervation.md)
* [Hallow](../../Magic/Spells/hallow.md)
* [Insect Plague](../../Magic/Spells/insect-plague.md)
* [Mislead](../../Magic/Spells/mislead.md)
* [Negative Energy Flood](../../Magic/Spells/negative-energy-flood.md)
* [Raise Dead](../../Magic/Spells/raise-dead.md)
* [Reincarnate](../../Magic/Spells/reincarnate.md)
* [Scrying](../../Magic/Spells/scrying.md)
 
## 6th-Level Spells
* [Circle of Death](../../Magic/Spells/circle-of-death.md)
* [Create Undead](../../Magic/Spells/create-undead.md)
* [Disintegrate](../../Magic/Spells/disintegrate.md)
* [Eyebite](../../Magic/Spells/eyebite.md)
* [Harm](../../Magic/Spells/harm.md)
* [Magic Jar](../../Magic/Spells/magic-jar.md)
* [Soul Cage](../../Magic/Spells/soul-cage.md)
* [True Seeing](../../Magic/Spells/true-seeing.md)
 
## 7th-Level Spells
* [Create Revenant](../../Magic/Spells/create-revenant.md)
* [Etherealness](../../Magic/Spells/etherealness.md)
* [Finger of Death](../../Magic/Spells/finger-of-death.md)
* [Forcecage](../../Magic/Spells/forcecage.md)
* [Resurrection](../../Magic/Spells/resurrection.md)
* [Symbol](../../Magic/Spells/symbol.md)
 
## 8th-Level Spells
* [Abi-Dalzim's Horrid Wilting](../../Magic/Spells/abi-dalzims-horrid-wilting.md)
* [Clone](../../Magic/Spells/clone.md)
* [Feeblemind](../../Magic/Spells/feeblemind.md)
* [Mind Blank](../../Magic/Spells/mind-blank.md)
* [Power Word Stun](../../Magic/Spells/power-word-stun.md)
 
## 9th-Level Spells
* [Astral Projection](../../Magic/Spells/astral-projection.md)
* [Power Word Kill](../../Magic/Spells/power-word-kill.md)
* [True Resurrection](../../Magic/Spells/true-resurrection.md)
