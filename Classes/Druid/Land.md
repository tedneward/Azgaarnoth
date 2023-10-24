# Druidic Circle: Circle of the Land
The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. The circle's wisest members preside as the chief priests of communities that venerate nature as the primal force in the world, and serve as advisors to the numerous provincial and city leaders, particularly among the [Hordes](/Races/Hordes.md). As a member of this circle, your magic is influenced by the land where you were initiated into the circle's mysterious rites.

```
name = 'Circle of the Land'
description = "***Druidic Circle: Circle of the Land.*** The Circle of the Land is made up of mystics and sages who safeguard ancient knowledge and rites through a vast oral tradition. These druids meet within sacred circles of trees or standing stones to whisper primal secrets in Druidic. As a member of this circle, your magic is influenced by the land where you were initiated into the circle's ways."
```

## Bonus Cantrip
*2nd-level Circle of the Land feature*

You learn one additional druid cantrip of your choice.

```
def level2(npc):
    def boostcantrips(npc): npc.spellcasting['Druid'].maxcantripsknown += 1
    npc.defer(lambda npc: boostcantrips(npc) )
```

## Natural Recovery
*2nd-level Circle of the Land feature*

You can regain some of your magical energy by sitting in meditation and communing with nature. During a short rest, you choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than half your druid level (rounded up), and none of the slots can be 6th level or higher. You can't use this feature again until you finish a long rest.

For example, when you are a 4th-level druid, you can recover up to two levels worth of spell slots. You can recover either a 2nd-level slot or two 1st-level slots.

```
    npc.defer(lambda npc: npc.traits.append(f"***Natural Recovery (Recharges on long rest).*** During a short rest, you can recover up to {(npc.levels('Druid') + 1) // 2} total spell slots of less than 6th level.") )
```

## Circle Spells
Your mystical connection to the land infuses you with the ability to cast certain spells. At 3rd, 5th, 7th, and 9th level you gain access to circle spells connected to the land where you became a druid. Choose that land – arctic, coast, desert, forest, grassland, mountain, swamp, or Underdark – and consult the associated list of spells.

Once you gain access to a circle spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.

```
    choices = {
        'Arctic' : arcticcirclespells, 
        'Coast' : coastcirclespells, 
        'Desert' : desertcirclespells, 
        'Forest' : forestcirclespells, 
        'Grassland' : grasslandcirclespells, 
        'Mountain' : mountaincirclespells, 
        'Swamp' : swampcirclespells, 
        'Underdark' : underdarkcirclespells
    }
    (_, circlespells) = choose("Choose your Land: ", choices)

    def circlespellsforlevel(npc):
        results = []
        if npc.levels(baseclass.name) >= 3: results += circlespells[3]
        if npc.levels(baseclass.name) >= 5: results += circlespells[5]
        if npc.levels(baseclass.name) >= 7: results += circlespells[7]
        if npc.levels(baseclass.name) >= 9: results += circlespells[9]
        npc.spellcasting[baseclass.name].spellsalwaysprepared += results

    npc.defer(lambda npc: circlespellsforlevel(npc))
```

**Arctic**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Hold Person, Ice Beam
5th	|Sleet Storm, Slow
7th	|Freedom of Movement, Ice Storm
9th	|Commune with Nature, Cone of Cold

Artic regions will be found only in southernmost [Dradehalia](../../Nations/Dradehalia.md) or [Chidia](../../Geography/Chidia.md).

```
arcticcirclespells = {
    3: ['hold person', "ice beam"],
    5: ['slow', 'sleet storm'],
    7: ['freedom of movement', 'ice storm'],
    9: ['commune with nature', 'cone of cold']
}
```

**Coast**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Mirror Image, [misty step](https://www.dndbeyond.com/spells/misty-step)
5th	|Water Breathing, Water Walk
7th	|Control Water, Freedom of Movement
9th	|Conjure Elemental, Scrying

Many coastal Druids of the Land are found within the [*al'meara*](../../Cultures/AlUma.md). Many [Sea Reavers](../../Organizations/MercCompanies/SeaReavers.md) also have druids of this Circle on their decks.

```
coastcirclespells = {
    3: ['mirror image', 'misty step'],
    5: ['water breathing', 'water walk'],
    7: ['freedom of movement', 'control water'],
    9: ['conjure elemental', 'scrying']
}
```

**Desert**

Druid Level|	Circle Spells
---------- | --------------
3rd | Blur, Silence
5th | Create Food and Water, Protection from Energy
7th | Blight, Hallucinatory Terrain
9th | Insect Plague, Wall of Stone

While Azgaarnoth lacks the traditional sweeping-dunes-of-sand deserts, the parched tundras of southernmost Dradehalia are the same low-moisture deserts, and druids of these lands feel kinship to those of sand.

```
desertcirclespells = {
    3: ['blur', 'silence'],
    5: ['create food and water', 'protection from energy'],
    7: ['blight', 'hallucinatory terrain'],
    9: ['insect plague', 'wall of stone']
}
```

**Forest**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Barkskin, Spider Climb
5th	|Call Lightning, Plant Growth
7th	|Divination, Freedom of Movement
9th	|Commune with Nature, Tree Stride

```
forestcirclespells = {
    3: ['barkskin', 'spider climb'],
    5: ['call lightning', 'plant growth'],
    7: ['divination', 'freedom of movement'],
    9: ['commune with nature', 'tree stride']
}
```

**Grassland**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Invisibility, Pass Without Trace
5th	|Daylight, Haste
7th	|Divination, Freedom of Movement
9th	|Dream, Insect Plague

Grassland areas include the [Ravenlands](../../Geography/Ravenlands.md), most of [Al'Uma](../../Geography/AlUma.md), and [Yithia](../../Geography/Yithia.md). Parts of [Dradehalia](../../Geography/Dradehalia.md) are also grassland, though colder than the regions further north.

```
grasslandcirclespells = {
    3: ['invisibility', 'pass without trace'],
    5: ['daylight', 'haste'],
    7: ['divination', 'freedom of movement'],
    9: ['dream', 'insect plague']
}
```

**Mountain**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Spider Climb, Spike Growth
5th	|Lightning Bolt, Meld into Stone
7th	|Stone Shape, Stoneskin
9th	|Passwall, Wall of Stone

The Daws mountains represent most of the mountainous regions in Azgaarnoth.

```
mountaincirclespells = {
    3: ['spider climb', 'spike growth'],
    5: ['lightning bolt', 'meld into stone'],
    7: ['stone shape', 'stoneskin'],
    9: ['passwall', 'wall of stone']
}
```

**Swamp**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Darkness, Melf's Acid Arrow
5th	|Water Walk, Stinking Cloud
7th	|Freedom of Movement, Locate Creature
9th	|Insect Plague, Scrying

Swamps abound in [Yithia](../../Geography/Yithia.md), and in southeatern [Liria](../../Nations/Liria.md).

```
swampcirclespells = {
    3: ['darkness', "melf's acid arrow"],
    5: ['water walk', 'stinking cloud'],
    7: ['freedom of movement', 'locate creature'],
    9: ['insect plague', 'scrying']
}
```

**Underdark**

Druid Level|	Circle Spells
---------- | --------------
3rd	|Spider Climb, Web
5th	|Gaseous Form, Stinking Cloud
7th	|Greater Invisibility, Stone Shape
9th	|Cloudkill, Insect Plague

```
underdarkcirclespells = {
    3: ['spider climb', 'web'],
    5: ['gaseous form', 'stinking cloud'],
    7: ['greater invisibility', 'stone shape'],
    9: ['cloudkill', 'insect plague']
}
```



## Land's Stride
*6th-level Circle of the Land feature*

Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard.

In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.

```
def level6(npc):
    npc.traits.append("***Land's Stride.*** Moving through nonmagical difficult terrain costs you no extra movement. You can also pass through nonmagical plants without being slowed by them and without taking damage from them if they have thorns, spines, or a similar hazard. In addition, you have advantage on saving throws against plants that are magically created or manipulated to impede movement, such as those created by the Entangle spell.")
```

## Nature's Ward
*10th-level Circle of the Land feature*

You can't be charmed or frightened by elementals or fey, and you are immune to poison and disease.

```
def level10(npc):
    npc.damageimmunities.append('poison')
    npc.conditionimmunities.append('poisoned')
    npc.conditionimmunities.append('diseased')
```

## Nature's Sanctuary
*14th-level Circle of the Land feature*

Creatures of the natural world sense your connection to nature and become hesitant to attack you. When a beast or plant creature attacks you, that creature must make a Wisdom saving throw against your druid spell save DC. On a failed save, the creature must choose a different target, or the attack automatically misses. On a successful save, the creature is immune to this effect for 24 hours.

The creature is aware of this effect before it makes its attack against you.
