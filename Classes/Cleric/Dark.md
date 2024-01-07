# Divine Domain: Dark
The most primal fear of all mortal races is fear of the dark.  Priests of the Dark Domain revel in this fear, worship it and learn to shape and control it. For some clerics, that control is to remove the fear, and show that in the dark, all there is to fear is the fear itself. But other clerics of the Dark Domain, their motives are not so pure. They can reach into your mind and take the face of your loved ones.  They coalesce shadows around themselves making them harder to see and hit.  Darkness can remove them from sight even in a completely lit room.  The strongest among them can control weaker minds with nightmarish powers that force their enemies greatest fears to the surface. Darkness is the edge of fear, and as such has much in common with deities that also embody death, madness, and the void. 

This domain is available to [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [the Keeper](../../Religions/Pantheon/Keeper.md), ...

```
name = 'Dark'
description = "***Divine Domain: Dark.*** The most primal fear of all mortal races is fear of the dark.  Priests of the Dark Domain revel in this fear, worship it and learn to shape and control it. For some clerics, that control is to remove the fear, and show that in the dark, all there is to fear is the fear itself. But other clerics of the Dark Domain, their motives are not so pure. They can reach into your mind and take the face of your loved ones.  They coalesce shadows around themselves making them harder to see and hit.  Darkness can remove them from sight even in a completely lit room.  The strongest among them can control weaker minds with nightmarish powers that force their enemies greatest fears to the surface. Darkness is the edge of fear, and as such has much in common with deities that also embody death, madness, and the void."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Dark Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Dark Domain Spells**

Cleric Level | Spell
------------ | ----
1st	| [disguise self](../../Magic/Spells/disguise-self.md), [sleep](../../Magic/Spells/sleep.md)
3rd	| [blur](../../Magic/Spells/blur.md), [detect thoughts](../../Magic/Spells/detect-thoughts.md)
5th	| [fear](../../Magic/Spells/fear.md), [bestow curse](../../Magic/Spells/bestow-curse.md)
7th	| [greater invisibility](../../Magic/Spells/greater-invisibility.md), [phantasmal killer](../../Magic/Spells/phantasmal-killer.md)
9th	| [telepathic bond](../../Magic/Spells/rarys-telepathic-bond.md), [dream](../../Magic/Spells/dream.md)

```
domainspells = {
    1: ['disguise self', 'sleep'],
    3: ['blur', 'detect thoughts'],
    5: ['fear', 'bestow curse'],
    7: ['greater invisibility', 'phatasmal killer'],
    9: ['telepathic bond', 'dream']
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


## Eyes of Black
*1st-level Dark domain feature*

Your eyes are a dark void from which no light escapes.  You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.

```
    npc.senses['darkvision'] = 120
    npc.traits.append("***Eyes of Black.*** You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.")
```

## Don't Fear the Dark
*1st-level Dark domain feature*

You can use your action to touch a willing creature, including yourself, to give it advantage on Wisdom saving throws against being frightened. This blessing lasts for 1 hour.  You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Don't Fear the Dark ({npc.WISbonus()}/Recharges on a long rest).*** You touch a willing creature, including yourself, and give it {'advantage on Wisdom saving throws' if npc.levels('Cleric') < 6 else 'immunity'} against being frightened{'and can see normally in darkness, both magical and nonmagical, to a distance of 60 feet' if npc.levels('Cleric') < 6 else ''}. This blessing lasts for {'1 hour' if npc.levels('Cleric') < 6 else '24 hours or until you take a long rest'}.") )
```

## Channel Divinity: Coalesce Fear
*2nd-level Dark domain feature*

You can use your Channel Divinity to create an area of Magical Darkness which spreads from a point you choose within 60 feet to fill a 15-foot-radius sphere for 5 minutes, or until you lose your concentration (as if you were concentrating on a spell). The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it.  

If any of this spell's area overlaps with an area of light created by a spell of your highest casting level or lower, the spell that created the light is dispelled or negated.

Each creature of your choice within the darkness must make a Wisdom saving throw or be stunned until the end of their next turn. Creatures immune to being frightened have advantage on the saving throw.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Coalesce Fear.*** You create an area of Magical Darkness which spreads from a point you choose within 60 feet to fill a 15-foot-radius sphere for 5 minutes, or until you lose your concentration (as if you were concentrating on a spell). The darkness spreads around corners. A creature with darkvision can't see through this darkness, and nonmagical light can't illuminate it. If any of this spell's area overlaps with an area of light created by a spell of your highest casting level or lower, the spell that created the light is dispelled or negated. Each creature of your choice within the darkness must make a Wisdom saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}) or be stunned until the end of their next turn. Creatures immune to being frightened have advantage on the saving throw.") )
```

## Fear Itself
*6th-level Dark domain feature*

Creatures under the effect of your Don't Fear the Dark feature are immune to being frightened and can see normally in darkness, both magical and nonmagical, to a distance of 60 feet. These benefits now last for 24 hours or until you take a long rest.

## Prevailing Darkness
*8th-level Dark domain feature*

Magical light has difficulty piercing your darkness.  When an effect would dispel darkness created by your spells or Channel Divinity options make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a successful check, the darkness remains.

```
def level8(npc):
    npc.traits.append("***Prevailing Darkness.*** When an effect would dispel darkness created by your spells or Channel Divinity options, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a successful check, the darkness remains.")
```

## Kakoneirophobia
*17th-level Dark domain feature*

Your mastery of the dark is perfected.  You no longer have to concentrate on your darkness spells or Channel Divinity options and whenever you create a sphere of darkness the casting distance, size of the sphere, and duration all double.

Additionally, you reach into the minds of your enemies and give form to the most base mortal fear.  As an action each creature of your choice in a sphere of darkness you've created must make a Wisdom saving throw, taking 8d8 psychic damage on a failed save, or half as much damage on a successful one. Creatures immune to being frightened have advantage on the saving throw.

```
def level17(npc):
    npc.traits.append("***Kakoneirophobia.*** You no longer have to concentrate on your darkness spells or Channel Divinity options and whenever you create a sphere of darkness, you double the casting distance, size of the sphere, and duration.")
    npc.defer(lambda npc: npc.actions.append(f"***Kakoneirophobia.*** You reach into the minds of your enemies and give form to the most base mortal fear. Each creature of your choice in a sphere of darkness you've created must make a Wisdom saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}), taking 8d8 psychic damage on a failed save, or half as much damage on a successful one. Creatures immune to being frightened have advantage on the saving throw.") )
```
