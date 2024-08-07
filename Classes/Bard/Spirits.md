# Bardic College: College of Spirits
Stories of the past are powerful; they hold lessons of history, philosophy, and magic. Bards of the College of Spirits seek the stories of those from beyond the material plane. They reach out to hear their stories, but the bards have no control over what story they find.

```
name = 'College of Spirits'
description = "***Bardic College: College of Spirits.*** Stories of the past are powerful; they hold lessons of history, philosophy, and magic. Bards of the College of Spirits seek the stories of those from beyond the material plane. They reach out to hear their stories, but the bards have no control over what story they find."
```

## Guiding Whispers
*3rd-level College of Spirits feature*

You can reach out to spirits to guide you and others. You learn the [guidance](../../Magic/Spells/guidance.md) cantrip, which doesn't count against the number of bard cantrips you know. For you, it has a range of 60 feet when you cast it.

```
def level3(npc):
    npc.traits.append("***Guiding Whispers.*** The [guidance](../../Magic/Spells/guidance.md) cantrip doesn't count against the number of bard cantrips you know, and a range of 60 feet when you cast it.")
    npc.spellcasting['Bard'].cantripsknown.append('guidance')
```

## Spiritual Focus
*3rd- and 6th-level College of Spirits feature*

Your practice of contacting spirits can employ special tools. You can use the following objects as a spellcasting focus for your bard spells: a candle, a crystal ball, a talking board, a tarokka deck, or a skull.

At 6th level, when you cast a bard spell that deals damage or restores hit points through the Spiritual Focus, roll a d6, and you gain a bonus to one roll of the spell equal to the number rolled.

```
    npc.defer(lambda npc: npc.traits.append(f"***Spiritual Focus.*** You can use the following objects as a spellcasting focus for your bard spells: a candle, a crystal ball, a talking board, a tarokka deck, or a skull.{' When you cast a bard spell that deals damage or restores hit points through this Spiritual Focus, roll a d6 and add that to the result.' if npc.levels('Bard') >= 6 else ''}") )
```

## Tales from Beyond
*3rd-level College of Spirits feature*

You reach out to spirits who tell their tales through you. While you are holding your Spiritual Focus, you can use a bonus action to expend one use of your Bardic Inspiration and roll on the Spirits' Tales table using your Bardic Inspiration die to determine the tale told. You retain the tale in mind until you bestow the tale's effect or you finish a short or long rest.

You can use an action to choose one creature you can see within 30 feet of you (this can be you) to be the target of the tale's effect. Once you do so, you can't bestow the tale's effect again until you roll it again.

You can retain only one of these tales in mind at a time, and rolling on the Spirits' Tales table immediately ends the effect of the previous tale.

If the tale requires a saving throw, the DC equals your spell save DC.

**Spirits' Tales**

Bardic Insp. Die|Tale
----------------|----
1|**Beast.** You recite the tale of a clever animal. For 1 minute, the target has advantage on Wisdom (Perception) checks and advantage on attack rolls against a creature if another enemy is within 5 feet of it, and that enemy isn't incapacitated.
2|**Warrior.** You recount the story of a renowned duelist. Make a melee spell attack against the target as an attacking spectral warrior briefly appears in an unoccupied space within 5 feet of the target before vanishing. On a hit, the target takes force damage equal to two rolls of your Bardic Inspiration die + your Charisma modifier.
3|**Friends.** You recite the tale of friends who found each other in the afterlife. The target and another creature of its choice it can see within 5 feet of it regains hit points equal to a roll of your Bardic Inspiration die + your Charisma modifier.
4|**Runaway.** You tell the tale of an adventurer that could escape any confinement. The target can immediately use its reaction to teleport up to 30 feet to an unoccupied space it can see. When the target teleports, it can choose a number of creatures it can see within 30 feet of it up to your Charisma modifier (minimum of 1) to immediately use the same reaction.
5|**Avenger.** You recount the tale of an avenging knight. For 1 minute, whenever a creature the target can see within 30 feet of it is damaged by a creature, the target can use its reaction to deal force damage equal to a roll of your Bardic Inspiration die to the attacker.
6|**Hero.** You speak the tale of an epic hero. Choose a creature you can see within 30 feet of you. The target gains temporary hit points equal to a roll of your Bardic Inspiration die + your bard level. While it has these temporary hit points, the target's walking speed increases by 10 feet.
7|**Fey.** You recount the tale of a mischievous fey. The target must succeed on a Wisdom saving throw or become charmed by you until the end of its next turn. The charmed target must use its action to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no other creature.
8|**Dark Spirit.** You speak a dreadful tale of a slayer in the dark. The target becomes invisible until the end of its next turn or until it hits a creature with an attack. If it hits a creature with an attack during this invisibility, that creature takes necrotic damage equal to a roll of your Bardic Inspiration die and is frightened of the target until the end of its next turn.
9|**Giant.** You speak of the deeds of a mighty giant. Each creature of the target's choice it can see within 30 feet of it must make a Strength saving throw, taking force damage equal to two rolls of your Bardic Inspiration die on a failed save and is knocked prone. A creature that succeeds on its saving throw takes half as much damage and isn't knocked prone.
10|**Dragon.** You breathe a poem of a wrathful dragon. The target magically spews fire from their mouth in a 30-foot cone. Each creature in that area must make a Dexterity saving throw, taking fire damage equal to three rolls of your Bardic Inspiration die on a failed save, or half as much damage on a successful one.
11|**Celestial.** You speak of the exalted deeds of a celestial. The target regains hit points equal to two rolls of your Bardic Inspiration die + your bard level, and you end one disease or a condition from the following list affecting the target: blinded, deafened, paralyzed, petrified, or poisoned.
12|**Unknown.** You utter an incomprehensible fable from a being beyond the stars. Choose a creature you can see within 30 feet of you. The target must succeed on an Intelligence saving throw or take psychic damage equal to three rolls of your Bardic Inspiration die, and the target is unable to speak any language for 1 minute.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Tales from the Beyond.*** You expend one use of your Bardic Inspiration and roll on against the list below using {'either a d6 or ' if npc.levels('Bard') >= 14 else ''}one of your Bardic Inspiration dice (a d{npc.bardicinspirationdie}) to determine the tale told. You retain the tale in mind until you bestow the tale's effect or you finish a short or long rest. You can retain only one of these tales in mind at a time, and rolling on the Spirits' Tales table immediately ends the effect of the previous tale. **1: Beast.** You recite the tale of a clever animal. For 1 minute, the target has advantage on Wisdom (Perception) checks and advantage on attack rolls against a creature if another enemy is within 5 feet of it, and that enemy isn't incapacitated; **2: Warrior.** You recount the story of a renowned duelist. Make a melee spell attack against the target as an attacking spectral warrior briefly appears in an unoccupied space within 5 feet of the target before vanishing. On a hit, the target takes 2d{npc.bardicinspirationdie} + {npc.CHAbonus()} force damage; **3: Friends.** You recite the tale of friends who found each other in the afterlife. The target and another creature of its choice it can see within 5 feet of it regains 2d{npc.bardicinspirationdie} + {npc.CHAbonus()} hit points; **4: Runaway.** You tell the tale of an adventurer that could escape any confinement. The target can immediately use its reaction to teleport up to 30 feet to an unoccupied space it can see. When the target teleports, it can choose {npc.CHAbonus()} creatures it can see within 30 feet of it to immediately use the same reaction; **5: Avenger.** You recount the tale of an avenging knight. For 1 minute, whenever a creature the target can see within 30 feet of it is damaged by a creature, the target can use its reaction to deal 1d{npc.bardicinspirationdie} force damageto the attacker; **6: Hero.** You speak the tale of an epic hero. Choose a creature you can see within 30 feet of you. The target gains 1d{npc.bardicinspirationdie} + {npc.levels('Bard')} temporary hit points. While it has these temporary hit points, the target's walking speed increases by 10 feet;**7: Fey.** You recount the tale of a mischievous fey. The target must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or become charmed by you until the end of its next turn. The charmed target must use its action to make a melee attack against a creature other than itself that you mentally choose. The target can act normally on its turn if you choose no other creature; **8: Dark Spirit.** You speak a dreadful tale of a slayer in the dark. The target becomes invisible until the end of its next turn or until it hits a creature with an attack. If it hits a creature with an attack during this invisibility, that creature takes 1d{npc.bardicinspirationdie} necrotic damage equal and is frightened of the target until the end of its next turn; **9: Giant.** You speak of the deeds of a mighty giant. Each creature of the target's choice it can see within 30 feet of it must make a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}), taking 2d{npc.bardicinspirationdie} force damage on a failed save and is knocked prone. A creature that succeeds on its saving throw takes half as much damage and isn't knocked prone; **10: Dragon.** You breathe a poem of a wrathful dragon. The target magically spews fire from their mouth in a 30-foot cone. Each creature in that area must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}), taking 3d{npc.bardicinspirationdie} fire damage on a failed save, or half as much damage on a successful one; **11: Celestial.** You speak of the exalted deeds of a celestial. The target regains 2d{npc.bardicinspirationdie} + {npc.levels('Bard')} hit points, and you end one disease or a condition from the following list affecting the target: blinded, deafened, paralyzed, petrified, or poisoned; **12: Unknown.** You utter an incomprehensible fable from a being beyond the stars. Choose a creature you can see within 30 feet of you. The target must succeed on an Intelligence saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or take 3d{npc.bardicinspirationdie} psychic damage, and the target is unable to speak any language for 1 minute.") )
    npc.actions.append("***Tell the Tale.*** You choose one creature you can see within 30 feet of you (this can be you) to be the target of the Tales from the Beyond tale's effect. Once you do so, you can't bestow the tale's effect again until you roll it again.")
```

## Spirit Session
*6th-level College of Spirits feature*

You can channel spirits to gain insights into magic. You can conduct an hour-long ritual channeling spirits (which can be done during a short or long rest) using your Spiritual Focus. You can conduct the ritual with a number of creatures equal to your proficiency bonus (including yourself). At the end of the ritual, you temporarily learn one spell of your choice from any class.

The spell you choose must be of a level equal to the number of creatures that conducted the ritual or less, the spell must of a level you can cast, and it must be in the school of divination or necromancy. The chosen spell counts as a bard spell for you but doesn't count against the number of bard spells you know.

Once you perform the ritual, you can't do so again until you start a long rest, and you know the chosen spell until you start a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Spirit Session (Recharges on long rest).*** You can conduct an hour-long ritual channeling spirits (which can be done during a short or long rest) using your Spiritual Focus. You can conduct the ritual with {npc.proficiencybonus()} creatures (including yourself). At the end of the ritual, you temporarily learn one spell of your choice from any class.The spell you choose must be level {npc.proficiencybonus()} or less, the spell must of a level you can cast, and it must be in the school of divination or necromancy. The chosen spell counts as a bard spell for you but doesn't count against the number of bard spells you know. You know the chosen spell until you start a long rest.") )
```

## Mystical Connection
*14th-level College of Spirits feature*

Your connection to spirits has become semipermanent. Whenever you use your Tales from Beyond feature, you can roll a d6 and use it instead of expending a Bardic Inspiration die. You still use your Bardic Inspiration die for the tale's effect, without expending it.

---

# Custom Bard Spells

* 3rd: [song of mercy]()
* 4th: [song of light and shadow]()
