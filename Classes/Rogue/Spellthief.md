# Roguish Archetype: Spellthief
These rogues focus their skills and training on recognizing magical spells and stealing them from the caster. They then refocus that magical energy to power their own spells.

```
name = 'Spellthief'
description = "***Roguish Archetype: Spellthief.*** These rogues focus their skills and training on recognizing magical spells and stealing them from the caster. They then refocus that magical energy to power their own spells."
```

## Spellcasting
*3rd-level Spellthief feature*

You gain the ability to cast spells… as long as you can steal the magical energy from another caster.

### Spell List
You can choose one spell list from any of the following: Bard, Cleric, Druid, Sorcerer, Warlock, or Wizard. Once you have chosen a spell list, all the spells you cast will come from that spell list.

```
def level3(npc):
    listchoices = {
        'Bard' : 'CHA',
        'Cleric' : 'WIS',
        'Druid' : 'WIS',
        'Sorcerer' : 'CHA',
        'Wizard' : 'INT'
    }
    castingchoice = choose("Choose a spell list: ", list(listchoices.keys()))
    spellcasting = halfcaster(npc, listchoices[castingchoice], name)
    spellcasting.casterclass = allclasses['Rogue']
    npc.spellthievery = castingchoice
```

### Cantrips
You learn two cantrips from your spell list. You learn additional cantrips at 4th level and 10th level. You do not have to steal magical power to cast your cantrips.

```
    def assigncantrips(npc): spellcasting.maxcantripsknown = (2 if npc.levels('Rogue') < 4 else 3 if npc.levels('Rogue') else 4)
    npc.defer(lambda npc: assigncantrips(npc))
```

### Spells Known and Maximum Level
You learn three 1st level spells from your spell list. The Spells Known column from the Spell Thief Spellcasting Table shows when you learn more spells. The Maximum Level column from the Spell Thief Spellcasting Table shows the maximum level of any spell you can know. Whenever you gain a level in this class, you can replace one spell with another spell from your spell list.

### Spellcasting Ability
Your spellcasting ability depends on the spell list that you choose.

* Cleric or Druid – Wisdom
* Bard, Sorcerer, or Warlock – Charisma
* Wizard - Intelligence

**Spell save DC** = 8 + your proficiency bonus + your Spellcasting Ability modifier

**Spell attack modifier** = your proficiency bonus + your Spellcasting Ability modifier

**Spellthief Spellcasting Table**
Rogue Level |  Spells Known  | Maximum Level
----------- | -------------- | -------------
3rd         | 3              | 1
4th         | 4              | 1
5th         | 4              | 1
6th         | 5              | 2
7th         | 5              | 2
8th         | 6              | 2
9th         | 6              | 2
10th        | 7              | 3
11th        | 8              | 3
12th        | 8              | 3
13th        | 9              | 3
14th        | 10             | 4
15th        | 10             | 4
16th        | 11             | 4
17th        | 11             | 4
18th        | 12             | 5
19th        | 12             | 5
20th        | 13             | 5


```
    spellcastingtable = {
        3: [3, 1],
        4: [4, 1],
        5: [4, 1],
        6: [5, 2],
        7: [5, 2],
        8: [6, 2],
        9: [6, 2],
        10: [7, 3],
        11: [8, 3],
        12: [8, 3],
        13: [9, 3],
        14: [10, 4],
        15: [10, 4],
        16: [11, 4],
        17: [11, 4],
        18: [12, 5],
        19: [12, 5],
        20: [13, 5],
    }
    def assignmaxspells(npc): npc.maxspellsknown = spellcastingtable[npc.levels('Rogue')][0]
    npc.defer(lambda npc: assignmaxspells(npc) )
```

### Stealing Spells
In order to cast a spell you know, you must steal the magical energy from a spellcaster who is actively casting a spell of their own. You can steal a number of spell levels equal to your rogue level per long rest. For example, if you are a 3rd level Spell Thief, you can steal up to 3 levels of spells per long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Spellthievery.*** You can learn and know {npc.spellthievery} spells up to level {spellcastingtable[npc.levels('Rogue')][1]}, and you can steal {npc.levels('Rogue')} total spell levels per long rest."))
```

In order to steal the magical energy from a spellcaster, you must use your reaction. You must also be able to see the spellcaster and they must be within 30 feet of you.

Once you have stolen the magical energy from another spellcaster, you immediately channel that energy into a spell of your own. You can cast any spell you know, and you will cast it at the level corresponding to the level of the spell you just stole. For example, if you steal a 3rd level Fireball that a wizard is trying to cast, you can channel that energy into a spell that you know such as Magic Missile which will be cast at 3rd level.

If you attempt to steal a spell that is higher level than what you are able to steal, the attempt will fail, and you cannot steal spells again until you finish a long rest. For example, if you are a 5th level Spell Thief, you can steal 5 levels of spells per long rest. If you have already stolen 2 levels of spells and attempt to steal a 4th level Fireball, the attempt will fail and you will no longer be able to steal spells until you complete a long rest.

```
    npc.reactions.append("***Steal Spell.*** In order to cast a spell you know, you must steal the magical energy from a spellcaster who is actively casting a spell of their own. In order to steal the magical energy from a spellcaster, you must be able to see the spellcaster and they must be within 30 feet of you. Once you have stolen the magical energy from another spellcaster, you immediately channel that energy into a spell of your own. You can cast any spell you know, and you will cast it at the level corresponding to the level of the spell you just stole. If that spell has a casting time of 1 action or longer, you must cast it on your next action, or the energy dissipates harmlessly. If you attempt to steal a spell that is higher level than what you are able to steal, or if stealing the spell would exceed your maximum spell levels per long rest, the attempt will automatically fail and you cannot steal spells again until you finish a long rest.")
```

## Spell Drain
*9th-level Spellthief feature*

You gain the ability to steal spell slots from a spellcaster even if they are not casting.

As an action, you can steal a number of spell slots from a spellcaster equal to the maximum level spell you can cast and use those spell levels to cast a spell of your own. When you attempt to do this, the spellcaster must make a wisdom saving thrown. On a success, they block your attempt to steal their magical energy. On a failure, you steal their energy and can cast a spell with their spell slots. You must be within 30 feet of the spellcaster, and these stolen spell slots count against the total number you can steal per long rest.

```
def level9(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spell Drain.*** You can steal a number of spell slots from a spellcaster equal to the maximum level spell you can cast and use those spell levels to cast a spell of your own. When you attempt to do this, the spellcaster must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(npc.spellcasting[name].ability)}). On a success, they block your attempt to steal their magical energy. On a failure, you steal their energy and can cast a spell with their spell slots. You must be within 30 feet of the spellcaster{', and these stolen spell slots count against the total number you can steal per long rest' if npc.levels('Rogue') < 17 else ', and these stolen spell slots do not count against your total number you can steal per long rest'}. {'If you are hidden from a spellcaster, you can use your Spell Drain ability without the target getting the chance to make a saving throw.' if npc.levels('Rogue') > 13 else ''}"))
```

## Hidden Spell Drain
*14th-level Spellthief feature*

If you are hidden from a spellcaster, you can use your Spell Drain ability without the target getting the chance to make a saving throw.

## Infinite Spell Drain
*17th-level Spellthief feature*

You can use your Spell Drain (or Hidden Spell Drain) ability without it counting against the total number of spell slots that you can steal per long rest.
