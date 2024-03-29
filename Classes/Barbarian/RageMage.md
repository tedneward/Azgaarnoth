# Primal Path: Path of the Rage Mage
Barbarians are often thought of as warriors, but the key element to a barbarian is rage; some use it to fuel their sword swings, where others tap into it to channel lightning. The rage mage makes for an interesting case, since her approach to magic is based on the primal passion of magic more than the studious quasi-scientific approach. A rage mage raises fascinating questions on the true nature of magic and magic use. But don't ask the rage mage to answer those questions herself - she's not interested in the "why", only the results.

A rage mage taps into the primal essence of magic, using her own natural anger and frenzy to channel the arcane power in flashy, flamboyant ways. Like any barbarian, a rage mage is often the product of a less civilized society. A rage mage is not necessarily stupid, however, and should be feared for it.

Rage magi are found among the Ravenstribes, the United Hordes, the Ulmhorde, and a few of the tribes of Yithi that still cling to "the old ways". Rage magi are wildly uncomfortable around mage school magi, and vice versa, but frequently get along well with shamans, sorcerers, and warlocks.

```
name = 'Rage Mage'
description = "***Primal Path: Path of the Rage Mage.*** A rage mage taps into the primal essence of magic, using her own natural anger and frenzy to channel the arcane power in flashy, flamboyant ways. Like any barbarian, a rage mage is often the product of a less civilized society. A rage mage is not necessarily stupid, however, and should be feared for it."
```

## Font of Fury
*3rd-level Path of the Rage Mage feature*

You can cast spells while raging. However, casting spells in this way is reckless and you lose some of your ability to defend yourself.

When you cast a spell while raging, attack rolls against you are rolled with advantage until the beginning of your next turn.

In addition, your rage ends early if you are knocked unconscious, if your turn ends and you haven't attacked a hostile creature, cast a spell, or taken damage since the end of your previous turn. Otherwise your rage works normally.

**Fury Points**. The Spells and Fury Points table shows how many fury points you have to cast your spells of 1st level and higher. To cast one of these spells, you must be in rage and you must expend a number of fury points depending on the spell's level, as shown in the Fury Point Cost table. You regain all expended fury points when you finish a long rest.

You use the spells' casting time and other rules as normal, except you're still unable to concentrate on any spell while raging.

The maximum spell level is determined by your barbarian level, as shown in the Spells and Fury Points table.

**Spells Known**. You know three 1st level sorcerer spells of your choice, two of which you must choose from the evocation and transmutation spells on the sorcerer spell list.

The Spells Known column of the Spells and Fury Points table shows when you learn more sorcerer spells of 1st level or higher. Each of these spells must be an evocation or transmutation spell of your choice, and must be of a level you can cast with Fury Points. For instance, when you reach 7th level in this class, you can learn one new spell of 1st or 2nd level.

The spells you learn at 8th, 14th, and 20th level can come from any school of magic. 

Whenever you gain a level in this class, you can replace one of the sorcerer spells you know with another spell of your choice from the sorcerer spell list. The new spell must be of a level you can cast with Fury Points, and it must be an evocation or transmutation spell, unless you're replacing the spell you gained at 3rd, 8th, 14th, or 20th level.

**Spellcasting Ability**. Charisma is your spellcasting ability for your sorcerer spells. You use your Charisma whenever a spell refers to your spellcasting ability.

**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier.

**Spell attack modifier** = your proficiency bonus + your Charisma modifier.

## Spells and Fury Points
Class Level|Cantrips Known|Spells Known|Fury Points|Max Spell Level
-----------|--------------|------------|-----------|---------------
3rd|2|3|4|1st
4th|2|4|6|1st
7th|2|5|14|2nd
8th|2|6|14|2nd
10th|3|7|17|2nd
11th|3|8|17|2nd
13th|3|9|27|3rd
14th|3|10|27|3rd
16th|3|11|32|3rd
19th|3|12|38|4th
20th|3|13|38|4th

## Fury Point Cost
Spell Level|Fury Point Cost
-----------|---------------
1st|2
2nd|3
3rd|5
4th|6

```
class RageMageSpellcasting(Spellcasting):
    def __init__(self, npc):
        Spellcasting.__init__(self, npc, 'CHA', "Rage Mage Spellcasting")
        self.casterclass = allclasses['Barbarian']
        del self.maxcantripsknown
        del self.maxspellsknown

    def maxcantripsknown(self):
        npc = self.npc
        return 2 if npc.levels('Barbarian') < 10 else 3

    def maxspellsknown(self):
        npc = self.npc
        return 3 if npc.levels('Barbarian') < 4 else 4 if npc.levels('Barbarian') < 7 else 5 if npc.levels('Barbarian') < 8 else 6 if npc.levels('Barbarian') < 10 else 7 if npc.levels('Barbarian') < 11 else 8 if npc.levels('Barbarian') < 13 else 9 if npc.levels('Barbarian') < 14 else 10 if npc.levels('Barbarian') < 16 else 11 if npc.levels('Barbarian') < 19 else 12 if npc.levels('Barbarian') < 20 else 13

    def furypoints(self):
        npc = self.npc
        return 4 if npc.levels('Barbarian') < 4 else 6 if npc.levels('Barbarian') < 7 else 14 if npc.levels('Barbarian') < 10 else 17 if npc.levels('Barbarian') < 13 else 27 if npc.levels('Barbarian') < 16 else 32 if npc.levels('Barbarian') < 19 else 38

    def emitMD(self):
        text = f">***Rage Mage Spellcasting (Cha, at level {self.casterlevel()}. Recharges on long rest).*** "
        text += f"Spell save DC: {self.spellsavedc()}, Spell attack bonus: +{self.spellattack()} "
        text += f"{self.furypoints()} Fury Points. "
        text += f"{self.maxcantripsknown()} cantrips known. "
        text += f"{self.maxspellsknown()} spells known.\n"
        text += f">\n>Cantrips known:\n"
        text +=  ">\n>Spells known:\n"
        text += f">* *1st-level (2 fury points):*\n"
        if self.npc.levels('Barbarian') >= 7: text += f">* *2nd-level (3 fury points):*\n"
        if self.npc.levels('Barbarian') >= 13: text += f">* *3rd-level (5 fury points):*\n"
        if self.npc.levels('Barbarian') >= 19: text += f">* *4th-level (6 fury points):*\n"
        text +=  ">\n"
        return text

def level3(npc):
    npc.traits.append("***Font of Fury.*** When you cast a spell while raging, attack rolls against you are rolled with advantage until the beginning of your next turn. In addition, your rage ends early if you are knocked unconscious, if your turn ends and you haven't attacked a hostile creature, cast a spell, or taken damage since the end of your previous turn. Otherwise your rage works normally.")
    npc.spellcasting['Rage Mage Spellcasting'] = RageMageSpellcasting(npc)
```

## Rage Weapon Focus
*3rd-level Path of the Rage Mage feature*

You learn a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond.

Once you have bonded a weapon to yourself, you can use the weapon as a spellcasting focus for your spells you cast using Font of Fury, and if the weapon wasn't magical before, the weapon counts as magical for the purpose of bypassing damage resistance or immunity against nonmagical weapon damage.

## Uncanny Adept
*6th-level Path of the Rage Mage feature*

You can add half your proficiency bonus (round up) to any Intelligence, Wisdom, or Charisma check you make that doesn't already use your proficiency bonus.

In addition, when you cast a spell that deals acid, cold, fire, lightning, or thunder damage while raging, you gain resistance to that damage for 1d4 rounds.

## Iron Will
*10th-level Path of the Rage Mage feature*

Your will is like iron, your determination unwavering. As a result you can't be charmed or frightened while you are conscious.

## Spell Fury
*14th-level Path of the Rage Mage feature*

You have grown capable of maintaining concentration on spells you cast with Font of Fury. However, concentrating on spells in this way takes more effort than usual. You lose concentration on a spell if you cast another spell, even if the spell being cast does not require concentration.

In addition, you can add your rage damage bonus to one damage roll of any spell you cast using Font of Fury.
