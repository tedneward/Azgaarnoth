# Druid
Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will.

Druids follow the path of [Druidism](../../Religions/Druidism.md) and carve their own path. Frequently that path comes into conflict with one or more of the established religions or nations or other organizations, but the druids press on, knowing that they labor on behalf of the entire world. The gods and the Eldar might await in the afterlife, but druids worry about this one.

*You must have a Wisdom score of 13 or higher in order to multiclass in or out of this class.*

```
name = 'Druid'
description = "***Class: Druid.*** Whether calling on the elemental forces of nature or emulating the creatures of the animal world, druids are an embodiment of nature's resilience, cunning, and fury. They claim no mastery over nature, but see themselves as extensions of nature's indomitable will."
```

## Class features
As a druid, you gain the following class features.

Level|Proficiency Bonus|Cantrips Known|1st|2nd|3rd|4th|5th|6th|7th|8th|9th|Features
-----|-----------------|--------------|---|---|---|---|---|---|---|---|---|--------
1st  |+2|2|2|-|-|-|-|-|-|-|-|[Druidic](#druidic), [Spellcasting](#spellcasting)
2nd  |+2|2|3|-|-|-|-|-|-|-|-|[Wild Shape](#wild-shape), [Druid Circle](#druid-circle)
3rd  |+2|2|4|2|-|-|-|-|-|-|-|
4th  |+2|3|4|3|-|-|-|-|-|-|-|[Wild Shape](#wild-shape) improvement, [Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
5th  |+3|3|4|3|2|-|-|-|-|-|-|
6th  |+3|3|4|3|3|-|-|-|-|-|-|Druid Circle feature
7th  |+3|3|4|3|3|1|-|-|-|-|-|
8th  |+3|3|4|3|3|2|-|-|-|-|-|[Wild Shape](#wild-shape) improvement, [Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
9th  |+4|3|4|3|3|3|1|-|-|-|-|
10th |+4|4|4|3|3|3|2|-|-|-|-|Druid Circle feature
11th |+4|4|4|3|3|3|2|1|-|-|-|
12th |+4|4|4|3|3|3|2|1|-|-|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
13th |+5|4|4|3|3|3|2|1|1|-|-|
14th |+5|4|4|3|3|3|2|1|1|-|-|Druid Circle feature
15th |+5|4|4|3|3|3|2|1|1|1|-|
16th |+5|4|4|3|3|3|2|1|1|1|-|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
17th |+6|4|4|3|3|3|2|1|1|1|1|
18th |+6|4|4|3|3|3|3|1|1|1|1|[Timeless Body](#timeless-body), [Beast Shapes](#beast-shapes)
19th |+6|4|4|3|3|3|3|2|1|1|1|[Ability Score Improvement](#ability-score-improvement) or [Feat](../Feats.md)
20th |+6|4|4|3|3|3|3|2|2|1|1|[Archdruid](#archdruid)

### Hit Points
**Hit Dice**: 1d8 per druid level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per druid level after 1st

```
def everylevel(npc): npc.hits('d8')
```

### Proficiencies
**Armor**: Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)

**Weapons**: Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears

**Tools**: Herbalism kit

**Saving Throws**: Intelligence, Wisdom

**Skills**: Choose two from Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, and Survival

```
def level1(npc):
    for arm in armor['light']:
        npc.proficiencies.append(arm)
    npc.proficiencies.append('Hide armor')
    npc.proficiencies.append('Shield')

    npc.proficiencies.append('Club')
    npc.proficiencies.append('Dagger')
    npc.proficiencies.append('Dart')
    npc.proficiencies.append('Javelin')
    npc.proficiencies.append('Mace')
    npc.proficiencies.append('Quarterstaff')
    npc.proficiencies.append('Scimitar')
    npc.proficiencies.append('Sickle')
    npc.proficiencies.append('Sling')
    npc.proficiencies.append('Spear')

    npc.savingthrows.append('WIS')
    npc.savingthrows.append('INT')

    druidskills = ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival']
    chooseskill(npc, druidskills)
    chooseskill(npc, druidskills)
```

### Equipment
You start with the following equipment, in addition to the equipment granted by your background:

* (a) a wooden shield or (b) any simple weapon
* (a) a scimitar or (b) any simple melee weapon
* Leather armor, an explorer's pack, and a druidic focus

```
    npc.equipment.append("Shield (wood) OR any simple weapon")
    npc.equipment.append("Scimitar OR any simple melee weapon")
    npc.armorclass['Leather armor'] = 11
    npc.equipment.append("Explorer's pack")
    npc.equipment.append("Druidic focus")
```

### Druidic
You know Druidic, the secret language of druids. You can speak the language and use it to leave hidden messages. You and others who know this language automatically spot such a message. Others spot the message's presence with a successful DC 15 Wisdom (Perception) check but can't decipher it without magic.

```
    npc.languages.append("Druidic")
```

## Spellcasting
*1st-level druid feature*

Drawing on the divine essence of nature itself, you can cast spells to shape that essence to your will.

### Cantrips
You know two cantrips of your choice from the druid spell list. You learn additional druid cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Druid table.

### Preparing and Casting Spells
The Druid table shows how many spell slots you have to cast your spells of 1st level and higher. To cast one of these druid spells, you must expend a slot of the spell's level or higher. You regain all expended spell slots when you finish a long rest.

You prepare the list of druid spells that are available for you to cast, choosing from the druid spell list. (Note that at the DM's discretion, the list of druid spells available for preparation may not be the entire list of druid spells in the world.) When you do so, choose a number of druid spells equal to your Wisdom modifier + your Druid level (minimum of one spell). The spells must be of a level for which you have spell slots.

For example, if you are a 3rd-level druid, you have four 1st-level and two 2nd-level spell slots. With a Wisdom of 16, your list of prepared spells can include six spells of 1st or 2nd level, in any combination. If you prepare the 1st-level spell Cure Wounds, you can cast it using a 1st-level or 2nd-level slot. Casting the spell doesn't remove it from your list of prepared spells.

### Spellcasting Ability
Wisdom is your spellcasting ability for your druid spells, since your magic draws upon your devotion and attunement to nature. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a druid spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Wisdom modifier

**Spell attack modifier** = your proficiency bonus + your Wisdom modifier

### Ritual Casting
You can cast a druid spell as a ritual if that spell has the ritual tag and you have the spell prepared.

### Spellcasting Focus
You can use a druidic focus as a spellcasting focus for your druid spells.

```
    sc = fullcaster(npc, 'WIS', name)

    def spellcasting(npc): 
        npc.spellcasting[name].maxcantripsknown = 3 if npc.levels(name) < 4 else 4 if npc.levels(name) < 10 else 5
        npc.spellcasting[name].spellsprepared = npc.levels(name) + npc.WISbonus()

    npc.defer(lambda npc: spellcasting(npc))
```

## Wild Shape
*2nd-level druid feature*

You can use your action to magically assume the shape of a beast that you have seen before. You can use this feature twice. You regain expended uses when you finish a short or long rest.

Your druid level determines the beasts you can transform into, as shown in the Beast Shapes table. At 2nd level, for example, you can transform into any beast that has a challenge rating of 1/4 or lower that doesn't have a flying or swimming speed.

**Beast Shapes**

Level | Max. CR | Limitations | Example
----- | ------- | ----------- | --------
2nd   | 1/4     | No flying or swimming speed | Wolf
4th   | 1/2     | No flying speed | Crocodile
8th   |  1      | - | Giant eagle

You can stay in a beast shape for a number of hours equal to half your druid level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.

While you are transformed, the following rules apply:

* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you and the bonus in its stat block is higher than yours, use the creature's bonus instead of yours. If the creature has any legendary or lair actions, you can't use them.

* When you transform, you assume the beast's hit points and Hit Dice. When you revert to your normal form, you return to the number of hit points you had before you transformed. However, if you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form, For example, if you take 10 damage in animal form and have only 1 hit point left, you revert and take 9 damage. As long as the excess damage doesn't reduce your normal form to 0 hit points, you aren't knocked unconscious.

* You can't cast spells, and your ability to speak or take any action that requires hands is limited to the capabilities of your beast form. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as Call Lightning, that you've already cast.

* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so. However, you can't use any of your special senses, such as darkvision, unless your new form also has that sense.

* You choose whether your equipment falls to the ground in your space, merges into your new form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the new form to wear a piece of equipment, based on the creature's shape and size. Your equipment doesn't change size or shape to match the new form, and any equipment that the new form can't wear must either fall to the ground or merge with it. Equipment that merges with the form has no effect until you leave the form.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Wild Shape{' (2/Recharges on short or long rest)' if npc.levels('Druid') < 20 else ''}.*** You can magically assume the shape of a beast that you have seen before. You can transform into any beast that has a challenge rating of {'1/4' if npc.levels('Druid') < 4 else '1/2' if npc.levels('Druid') < 8 else '1'} or lower{'that has no flying or swimming speed' if npc.levels('Druid') < 4 else 'that has no flying speed' if npc.levels('Druid') < 8 else ''}. You can stay in a beast shape for {npc.levels('Druid') // 2} hours. You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.") )
```

## Wild Companion
*2nd-level druid feature*

You gain the ability to summon a spirit that assumes an animal form: as an action, you can expend a use of your Wild Shape feature to cast the [find familiar](../../Magic/Spells/find-familiar.md) spell, without material components.

When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after a number of hours equal to half your druid level.

```
    npc.defer(lambda npc: npc.actions.append(f"***Wild Companion.*** You can expend a use of your Wild Shape to cast {spelllinkify('find familiar')}, without material components. When you cast the spell in this way, the familiar is a fey instead of a beast, and the familiar disappears after {(npc.levels('Druid') + 1) // 2} hours.") )
```

## Druid Circle
At 2nd level, you choose to identify with a circle of druids:

* [Circle of Dragons](Dragons.md)
* [Circle of Dreams](Dreams.md)
* [Circle of Frost](Frost.md)
* [Circle of the Land](Land.md)
* [Circle of the Molt](Molt.md)
* [Circle of the Moon](Moon.md)
* [Circle of the Shepherd](Shepherd.md)
* [Circle of the Sepulchre](Sepulchre.md)
* [Circle of the Solstice](Solstice.md)
* [Circle of Sonority](Sonority.md)
* [Circle of Spores](Spores.md)
* [Circle of Stars](Stars.md)
* [Circle of Twilight](Twilight.md)
* [Circle of Wildfire](Wildfire.md)
* [Circle of Winter](Winter.md)

Your choice grants you features at 2nd level and again at 6th, 10th, and 14th level.

```
    (_, subclass) = choose("Choose a subclass: ", subclasses)
    npc.subclasses[allclasses['Druid']] = subclass
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

## Cantrip Versatility
*4th-level druid feature*

Whenever you reach a level in this class that grants the Ability Score Improvement feature, you can replace one cantrip you learned from this class's Spellcasting feature with another cantrip from the druid spell list. 

## Timeless Body
*18th-level druid feature*

The primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.

```
def level18(npc):
    npc.traits.append("***Timeless Body.*** The primal magic that you wield causes you to age more slowly. For every 10 years that pass, your body ages only 1 year.")
```

## Beast Shapes
*18th-level druid feature*

You can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components.

```
    npc.traits.append("***Beast Shapes.*** You can cast many of your druid spells in any shape you assume using Wild Shape. You can perform the somatic and verbal components of a druid spell while in a beast shape, but you aren't able to provide material components.")
```

## Archdruid
*20th-level druid feature*

You can use your Wild Shape an unlimited number of times.

---

# "Core" Druid Spells
The following spells listed are known (but not necessarily accessible, depending on the circle chosen) to all druids throughout Azgaarnoth; this is not the complete list of all druid spells, however. Certain circles may have additional spells that are only known to them, and thus are not accessible to other circles. Druids can learn new spells by visiting foreign circles, studying with other druids, communing with nature for significant periods of time, and so on.

> ### GM Notes
> These are all the spells found in the *Player's Handbook*, with no additions. In game terms, these spells are always accessible for use by a druid.

## Cantrips
* [druidcraft](../../Magic/Spells/druidcraft.md)
* [guidance](../../Magic/Spells/guidance.md)
* [mending](../../Magic/Spells/mending.md)
* [poison spray](../../Magic/Spells/poison-spray.md)
* [produce flame](../../Magic/Spells/produce-flame.md)
* [resistance](../../Magic/Spells/resistance.md)
* [shillelagh](../../Magic/Spells/shillelagh.md)
* [thorn whip](../../Magic/Spells/thorn-whip.md)

## 1st Level
* [animal friendship](../../Magic/Spells/animal-friendship.md)
* [charm person](../../Magic/Spells/charm-person.md)
* [create or destroy water](../../Magic/Spells/create-or-destroy-water.md)
* [cure wounds](../../Magic/Spells/cure-wounds.md)
* [detect magic](../../Magic/Spells/detect-magic.md)
* [detect poison and disease](../../Magic/Spells/detect-poison-and-disease.md)
* [entangle](../../Magic/Spells/entangle.md)
* [faerie fire](../../Magic/Spells/faerie-fire.md)
* [fog cloud](../../Magic/Spells/fog-cloud.md)
* [goodberry](../../Magic/Spells/goodberry.md)
* [healing word](../../Magic/Spells/healing-word.md)
* [jump](../../Magic/Spells/jump.md)
* [longstrider](../../Magic/Spells/longstrider.md)
* [purify food and drink](../../Magic/Spells/purify-food-and-drink.md)
* [speak with animals](../../Magic/Spells/speak-with-animals.md)
* [thunderwave](../../Magic/Spells/thunderwave.md)

## 2nd Level
* [animal messenger](../../Magic/Spells/animal-messenger.md)
* [barkskin](../../Magic/Spells/barkskin.md)
* [beast sense](../../Magic/Spells/beast-sense.md)
* [darkvision](../../Magic/Spells/darkvision.md)
* [enhance ability](../../Magic/Spells/enhance-ability.md)
* [find traps](../../Magic/Spells/find-traps.md)
* [flame blade](../../Magic/Spells/flame-blade.md)
* [flaming sphere](../../Magic/Spells/flaming-sphere.md)
* [gust of wind](../../Magic/Spells/gust-of-wind.md)
* [heat metal](../../Magic/Spells/heat-metal.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [lesser restoration](../../Magic/Spells/lesser-restoration.md)
* [locate animals or plants](../../Magic/Spells/locate-animals-or-plants.md)
* [locate object](../../Magic/Spells/locate-object.md)
* [moonbeam](../../Magic/Spells/moonbeam.md)
* [pass without trace](../../Magic/Spells/pass-without-trace.md)
* [protection from poison](../../Magic/Spells/protection-from-poison.md)
* [spike growth](../../Magic/Spells/spike-growth.md)

## 3rd Level
* [call lightning](../../Magic/Spells/call-lightning.md)
* [conjure animals](../../Magic/Spells/conjure-animals.md)
* [daylight](../../Magic/Spells/daylight.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [feign death](../../Magic/Spells/feign-death.md)
* [meld into stone](../../Magic/Spells/meld-into-stone.md)
* [plant growth](../../Magic/Spells/plant-growth.md)
* [protection from energy](../../Magic/Spells/protection-from-energy.md)
* [sleet storm](../../Magic/Spells/sleet-storm.md)
* [speak with plants](../../Magic/Spells/speak-with-plants.md)
* [water breathing](../../Magic/Spells/water-breathing.md) (ritual)
* [water walk](../../Magic/Spells/water-walk.md) (ritual)
* [wind wall](../../Magic/Spells/wind-wall.md)

## 4th Level
* [blight](../../Magic/Spells/blight.md)
* [confusion](../../Magic/Spells/confusion.md)
* [conjure minor elementals](../../Magic/Spells/conjure-minor-elementals.md)
* [conjure woodland beings](../../Magic/Spells/conjure-woodland-beings.md)
* [control water](../../Magic/Spells/control-water.md)
* [dominate beast](../../Magic/Spells/dominate-beast.md)
* [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
* [giant insect](../../Magic/Spells/giant-insect.md)
* [grasping vine](../../Magic/Spells/grasping-vine.md)
* [hallucinatory terrain](../../Magic/Spells/hallucinatory-terrain.md)
* [ice storm](../../Magic/Spells/ice-storm.md)
* [locate creature](../../Magic/Spells/locate-creature.md)
* [polymorph](../../Magic/Spells/polymorph.md)
* [stone shape](../../Magic/Spells/stone-shape.md)
* [stoneskin](../../Magic/Spells/stoneskin.md)
* [wall of fire](../../Magic/Spells/wall-of-fire.md)

## 5th Level
* [antilife shell](../../Magic/Spells/antilife-shell.md)
* [awaken](../../Magic/Spells/awaken.md)
* [commune with nature](../../Magic/Spells/commune-with-nature.md)
* [conjure elemental](../../Magic/Spells/conjure-elemental.md)
* [contagion](../../Magic/Spells/contagion.md)
* [geas](../../Magic/Spells/geas.md)
* [greater restoration](../../Magic/Spells/greater-restoration.md)
* [insect plague](../../Magic/Spells/insect-plague.md)
* [mass cure wounds](../../Magic/Spells/mass-cure-wounds.md)
* [planar binding](../../Magic/Spells/planar-binding.md)
* [reincarnate](../../Magic/Spells/reincarnate.md)
* [scrying](../../Magic/Spells/scrying.md)
* [tree stride](../../Magic/Spells/tree-stride.md)
* [wall of stone](../../Magic/Spells/wall-of-stone.md)

## 6th Level
* [conjure fey](../../Magic/Spells/conjure-fey.md)
* [find the path](../../Magic/Spells/find-the-path.md)
* [heal](../../Magic/Spells/heal.md)
* [heroes' feast](../../Magic/Spells/heroes-feast.md)
* [move earth](../../Magic/Spells/move-earth.md)
* [sunbeam](../../Magic/Spells/sunbeam.md)
* [transport via plants](../../Magic/Spells/transport-via-plants.md)
* [wall of thorns](../../Magic/Spells/wall-of-thorns.md)
* [wind walk](../../Magic/Spells/wind-walk.md)

## 7th Level
* [fire storm](../../Magic/Spells/fire-storm.md)
* [mirage arcane](../../Magic/Spells/mirage-arcane.md)
* [plane shift](../../Magic/Spells/plane-shift.md)
* [regenerate](../../Magic/Spells/regenerate.md)
* [reverse gravity](../../Magic/Spells/reverse-gravity.md)

## 8th Level
* [animal shapes](../../Magic/Spells/animal-shapes.md)
* [antipathy/sympathy](../../Magic/Spells/antipathy-sympathy.md)
* [control weather](../../Magic/Spells/control-weather.md)
* [earthquake](../../Magic/Spells/earthquake.md)
* [feeblemind](../../Magic/Spells/feeblemind.md)
* [sunburst](../../Magic/Spells/sunburst.md)
* [tsunami](../../Magic/Spells/tsunami.md)

## 9th Level
* [foresight](../../Magic/Spells/foresight.md)
* [shapechange](../../Magic/Spells/shapechange.md)
* [storm of vengeance](../../Magic/Spells/storm-of-vengeance.md)
* [true resurrection](../../Magic/Spells/true-resurrection.md)
