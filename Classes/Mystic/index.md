# Mystic
*A minotaur clad in simple robes walks along a forest path. A gang of goblins emerges from the brush, arrows trained on him, their smiles wide at their good fortune of finding such easy prey for the legion's slave pens. Their smiles turn to shrieks of terror as the traveler grows to huge size and leaps at them, his staff now a deadly cudgel.*

*The militia forms in ranks to prepare for the orcs' charge. The growling brutes howl their battle cries and surge forward. To their surprise, the goblin rabble holds its ground and fights with surprising ferocity. Suddenly, mindless fear clings to the orcs' minds and they, despite facing a far inferior foe, turn and run, never noticing the calm half-orc standing amid the militia and directing its efforts.*

*Baron von Ludwig was always proud of his grand library. Little did he know that each evening, a gnome laden with blank scrolls slipped past his guards each night and dutifully copied his most heavily guarded archives. When the duke's men arrived to arrest him for dealing with demons, he never guessed that the gnome scribe traveling with them had spent more time in his keep than he had over the past year.*

These are all mystics, followers of a strange and mysterious form of power. Mystics shun the world to turn their eyes inward, mastering the full potential of their minds and exploring their psyches before turning to face the world. Mystics are incredibly rare, and most prefer to keep the nature of their abilities secret. Using their inner, psychic strength, they can read minds, fade into invisibility, transform their bodies into living iron, and seize control of the physical world and bend it to their will.

Mysticism has always been a part of the fabric of life in Azgaarnoth, but when the advisors left [Yithi](../People/Yithi.md) and moved north into [Zhi](../../Nations/Zhi.md) to form their Council of Seers there many years later, they found that a new source of power--that of the mind--was open to those willing to put the time and discipline into it. Seeing in this new branch of study an opportunity to leave some of the shackles of arcane and divine behind, the Council put a significant amount of energy into its study, and in time, found a whole new category of power-users. As a result, mystics are far more common among the [Yithi](../../Nations/Yithi.md) and [Zhi](../../Nations/Zhi.md), but many of the secrets of mysticism have had the time required to move all across the world.

Some [mage schools](../../Organizations/MageSchools/index.md) have begun to form around mysticism, but as of yet those schools are extremely small, few, and far apart; those who seek to study the mystic arts are encouraged to journey east, particularly into [Zhi](../../Nations/Zhi.md) to find the master they seek.

```
name = 'Mystic'
description = "***Class: Mystic.*** Mystics shun the world to turn their eyes inward, mastering the full potential of their minds and exploring their psyches before turning to face the world. Mystics are incredibly rare, and most prefer to keep the nature of their abilities secret. Using their inner, psychic strength, they can read minds, fade into invisibility, transform their bodies into living iron, and seize control of the physical world and bend it to their will."
```

## Hermits and Outcasts
Mystics are loners. Most discover the secrets of their power through vague references in tomes of lore or by ingratiating themselves to a master of the power.

In order to master their power, mystics must first master themselves. They spend months and years in quiet contemplation, exploring their minds and leaving nothing uncovered. During this time, they shun society and typically live as hermits at the edge of society. A mystic who studied under a master worked as a virtual slave, toiling away at mundane tasks in return for the occasional lesson or cryptic insight.

When mystics finally master their power, they return to the world to broaden their horizons and practice their craft. Some mystics prefer to remain isolated, but those who become adventurers aren't content to remain on the fringe of the world.

## Eccentric Minds
In order to maintain the strict discipline and intense self-knowledge needed to tap into their power, mystics develop a variety of practices to keep their focus sharp.

These practices are reflected in taboos and quirks, strange little behaviors that govern a mystic's actions. These quirks are oaths or behavioral tics that help keep mystics in the proper frame of mind while maintaining perfect control over their minds and bodies.

While these taboos are harmless, they help cast mystics as outsiders. Few feel accepted by society, and fewer still care to become integrated with it. To mystics, the life of the mind is where they feel most at home.

## Selecting Quirks
To add some texture to your mystic, consider the quirks your character has acquired. These behaviors have no game effect, but your character might become irritated or upset if forced to break them. They're a great roleplaying tool to add character to the game. You can roll on or pick from the table below, or create your own quirks. Aim to create two quirks, to give them more of a chance to come into play. Finally, consider why your character chose these behaviors. What do they say about your character's personality or background? Are they based on a specific incident or a belief?

**Mystic Quirks**

d20|Quirk
---|-----
1|You never cut your hair.
2|You refuse to wear clothes of a specific color.
3|You never say your name.
4|You never wear footwear.
5|You always wear a mask.
6|You dye your hair bright blue or green.
7|You pick a new name each day.
8|You never immerse yourself in water.
9|You sleep on bare earth.
10|You never consume alcohol.
11|You wear a veil to conceal your face.
12|You always wear a specific piece of clothing.
13|You refuse to light fires.
14|You refuse to write things down, instead using pictograms.
15|You never sit on a chair, preferring to stand or sit on the floor.
16|You never answer to any name but your own.
17|You write down the name of each creature you slay, and name ones that are unnamed.
18|You consume only water and raw vegetables.
19|You spend any money you earn within 1 week of gaining it.
20|You often speak to an imaginary companion, and act only with its blessing.

```
def genquirk(npc):
    quirks = [
        "You never cut your hair.",
        "You refuse to wear clothes of a specific color.",
        "You never say your name.",
        "You never wear footwear.",
        "You always wear a mask.",
        "You dye your hair bright blue or green.",
        "You pick a new name each day.",
        "You never immerse yourself in water.",
        "You sleep on bare earth.",
        "You never consume alcohol.",
        "You wear a veil to conceal your face.",
        "You always wear a specific piece of clothing.",
        "You refuse to light fires.",
        "You refuse to write things down, instead using pictograms.",
        "You never sit on a chair, preferring to stand or sit on the floor.",
        "You never answer to any name but your own.",
        "You write down the name of each creature you slay, and name ones that are unnamed.",
        "You consume only water and raw vegetables.",
        "You spend any money you earn within 1 week of gaining it.",
        "You often speak to an imaginary companion, and act only with its blessing."
    ]
    npc.description.append(f"Mystic quirk: {quirks[random.randint[0, len(quirks) - 1]]}")
```

Level|Proficiency Bonus|Features|Talents Known|Disciplines Known|Psi Points|Psi Limit
-----|-----------------|--------|-------------|-----------------|----------|---------
1st|+2|Psionics, Mystic Order|1|1|4|2
2nd|+2|Mystical Recovery, Telepathy|1|1|6|2
3rd|+2|Mystic Order feature|2|2|14|3
4th|+2|Ability Score Improvement, Strength of Mind|2|2|17|3
5th|+3|--|2|3|27|5
6th|+3|Mystic Order feature|2|3|32|5
7th|+3|--|2|4|38|6
8th|+3|Ability Score Improvement, Potent Psionics (1d8)|2|4|44|6
9th|+4|--|2|5|57|7
10th|+4|Consumptive Power|3|5|64|7
11th|+4|Psionic Mastery (1/day)|3|5|64|7
12th|+4|Ability Score Improvement|3|6|64|7
13th|+5|Psionic Mastery (2/day)|3|6|64|7
14th|+5|Mystic Order feature, Potent Psionics (2d8)|3|6|64|7
15th|+5|Psionic Mastery (3/day)|3|7|64|7
16th|+5|Ability Score Improvement|3|7|64|7
17th|+6|Psionic Mastery (4/day)|4|7|64|7
18th|+6|--|4|8|71|7
19th|+6|Ability Score Improvement|4|8|71|7
20th|+6|Psionic Body|4|8|71|7

```
mystictable = {
    # Talents, Disciplines, Psi Points, Psi Limit
    1: [1,1,4,2],
    2: [1,1,6,2],
    3: [2,2,14,3],
    4: [2,2,17,3],
    5: [2,3,27,5],
    6: [2,3,32,5],
    7: [2,4,38,6],
    8: [2,4,44,6],
    9: [2,5,57,7],
    10: [3,5,64,7],
    11: [3,5,64,7],
    12: [3,6,64,7],
    13: [3,6,64,7],
    14: [3,6,64,7],
    15: [3,7,64,7],
    16: [3,7,64,7],
    17: [4,7,64,7],
    18: [4,8,71,7],
    19: [4,8,71,7],
    20: [4,8,71,7]
}
```

As a mystic, you gain the following class features.

## Hit Points
**Hit Dice**: 1d8 per mystic level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per mystic level after 1st

```
def everylevel(npc): npc.hits('d8')
```

## Proficiencies
**Armor**: Light armor 

**Weapons**: Simple weapons 

**Tools**: None

**Saving Throws**: Intelligence, Wisdom

**Skills**: Choose two skills from Arcana, History, Insight, Medicine, Nature, Perception, and Religion

```
def level1(npc):
    npc.savingthrows.append("INT")
    npc.savingthrows.append("WIS")

    for arm in armor['light']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)

    skills = ['Arcana', 'History', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion']
    chooseskill(npc, skills)
    chooseskill(npc, skills)
```

## Equipment
You start with the following equipment, in addition to the equipment granted by your background:
* (a) a spear or (b) a mace
* (a) leather armor or (b) studded leather armor
* (a) a light crossbow and 20 bolts or (b) any simple weapon
* (a) a scholar's pack or (b) an explorer's pack

Alternatively, you can ignore the equipment here and in your background, and buy 5d4 × 10 gp worth of equipment from chapter 5 in the Player's Handbook.

```
    npc.equipment.append("Spear OR mace")
    npc.equipment.append("Leather armor OR Studded leather armor")
    npc.armorclass['Studded leather'] = 12
    npc.equipment.append("Light crossbow and 20 bolts OR any simple weapon")
    npc.equipment.append("Scholar's pack, or explorer's pack")
```

## Psionics
As a student of psionics, you can master and use psionic talents and disciplines. Mystic psionics is a special form of magic use, distinct from spellcasting.

### Psionic Talents
A [psionic talent](#psionic-talents-1) is a minor psionic effect you have mastered. At 1st level, you know one psionic talent of your choice. You learn additional talents of your choice at higher levels. The Talents Known column of the Mystic table shows the total number of talents you know at each level; when that number goes up for you, choose a new talent.

### Psionic Disciplines
A [psionic discipline](Disciplines/index.md) is a rigid set of mental exercises that allows a mystic to manifest psionic power. A mystic masters only a few disciplines at a time.

At 1st level, you know one psionic discipline of your choice. The Disciplines Known column of the Mystic table shows the total number of disciplines you know at each level; when that number goes up for you, choose a new discipline.

In addition, whenever you gain a level in this class, you can replace one discipline you know with a different one of your choice.

### Psi Points
You have an internal reservoir of energy that can be devoted to psionic disciplines you know. This energy is represented by psi points. Each psionic discipline describes effects you can create with it by spending a certain number of psi points. A psionic talent requires no psi points.

The number of psi points you have is based on your mystic level, as shown in the Psi Points column of the Mystic table. The number shown for your level is your psi point maximum. Your psi point total returns to its maximum when you finish a long rest. The number of psi points you have can't go below 0 or over your maximum.

### Psi Limit
Though you have access to a potent amount of psionic energy, it takes training and practice to channel that energy. There is a limit on the number of psi points you can spend to activate a psionic discipline. The limit is based on your mystic level, as shown in the Psi Limit column of the Mystic table. For example, as a 3rd-level mystic, you can spend no more than 3 psi points on a discipline each time you use it, no matter how many psi points you have.

```
    npc.psionictalents = []
    npc.psionicdisciplines = []

    choosetalent(npc)

    choosediscipline(npc)

    def psionicabilitytext(npc):
        results  = f"***Psionic Ability (Int, at level { npc.levels('Mystic') }. Recharges on long rest).*** "
        results += f"{ mystictable[npc.levels('Mystic')][2] } Psi points. "
        results += f"{ mystictable[npc.levels('Mystic')][0] } talents known ({ ', '.join(npc.psionictalents) }). "
        results += f"{ mystictable[npc.levels('Mystic')][1] } disciplines known ({ ', '.join(npc.psionicdisciplines) }). "
        results += f"{ mystictable[npc.levels('Mystic')][3] } Psi/discipline. "
        results += f"Discipline save DC { 8 + npc.proficiencybonus() + npc.INTbonus() }, +{npc.proficiencybonus() + npc.INTbonus()} attack bonus"
        return results

    npc.defer(lambda npc: npc.actions.append(psionicabilitytext(npc)) )
```

### Psychic Focus
You can focus psionic energy on one of your psionic disciplines to draw ongoing benefits from it. As a bonus action, you can choose one of your psionic disciplines and gain its psychic focus benefit, which is detailed in that discipline's description. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit.

You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.

### Psionic Ability
Intelligence is your psionic ability for your psionic disciplines. You use your Intelligence modifier when setting the saving throw DC for a psionic discipline or when making an attack roll with one.

**Discipline save DC** = 8 + your proficiency bonus + your Intelligence modifier

**Discipline attack modifier** = your proficiency bonus + your Intelligence modifier

## Mystic Order
*1st-level Mystic feature*

You choose a Mystic Order: the [Order of the Avatar](Avatar.md), the [Order of the Awakened](Awakened.md), the [Order of the Immortal](Immortal.md), the [Order of the Nomad](Nomad.md), the [Order of the Soul Knife](SoulKnife.md), or the [Order of the Wu Jen](WuJen.md), each of which is detailed at the end of the class description. Each order specializes in a specific approach to psionics.

Your order gives you features when you choose it at 1st level and additional features at 3rd, 6th, and 14th level.

```
    # Choose subclass
    (_, subclass) = choose("Choose a Mystical Order:", subclasses)
    npc.subclasses[allclasses['Mystic']] = subclass
    npc.description.append(subclass.description)
```

## Mystical Recovery
*2nd-level Mystic feature*

You can draw vigor from the psi energy you use to power your psionic disciplines.

Immediately after you spend psi points on a psionic discipline, you can take a bonus action to regain hit points equal to the number of psi points you spent.

```
def level2(npc):
    npc.bonusactions.append("***Mystical Recovery.*** Immediately after you spend psi points on a psionic discipline, you regain hit points equal to the number of psi points you spent.")
```

## Telepathy
*2nd-level Mystic feature*

Your mind awakens to the ability to communicate via telepathy. You can telepathically speak to any creature you can see within 120 feet of you in this manner. You don't need to share a language with the creature for it to understand your telepathic messages, but the creature must be able to understand at least one language or be telepathic itself.

```
    npc.senses['telepathy'] = 120
```

```
def level3(npc):
    choosetalent(npc)
    choosediscipline(npc)
```

## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

## Strength of Mind
*4th-level Mystic feature*

Even the simplest psionic technique requires a deep understanding of how psionic energy can augment mind and body. This understanding allows you to alter your defenses to better deal with threats.

You can replace your proficiency in Wisdom saving throws whenever you finish a short or long rest. To do so, choose Strength, Dexterity, Constitution, or Charisma. You gain proficiency in saves using that ability, instead of Wisdom. This change lasts until you finish your next short or long rest.

```
def level4(npc): 
    abilityscoreimprovement(npc)
    npc.traits.append("***Strength of Mind (Recharges on short or long rest).*** You can replace your proficiency in Wisdom saving throws whenever you finish a short or long rest. To do so, choose Strength, Dexterity, Constitution, or Charisma. You gain proficiency in saves using that ability, instead of Wisdom.")
```

```
def level7(npc):
    choosediscipline(npc)
```

## Potent Psionics
*8th-level Mystic feature*

You gain the ability to infuse your weapon attacks with psychic energy. Once on each of your turns when you hit a creature with a weapon, you can deal an extra 1d8 psychic damage to that target. When you reach 14th level, this extra damage increases to 2d8.

In addition, you add your Intelligence modifier to any damage roll you make for a psionic talent.

```
def level8(npc):
    abilityscoreimprovement(npc)

    npc.defer(lambda npc: npc.traits.append(f"***Potent Psionics: Attacks.*** Once on each of your turns when you hit a creature with a weapon, you can deal an extra {'1d8' if npc.levels('Mystic') < 14 else '2d8'} psychic damage to that target.") )
    npc.defer(lambda npc: npc.traits.append(f"***Potent Psionics.*** You add {npc.INTbonus()} to any damage roll you make for a psionic talent.") )
```

```
def level9(npc):
    choosediscipline(npc)
```

## Consumptive Power
*10th-level Mystic feature*

You gain the ability to sacrifice your physical durability in exchange for psionic power. When activating a psionic discipline, you can pay its psi point cost with your hit points, instead of using any psi points. Your current hit points and hit point maximum are both reduced by the number of hit points you spend. This reduction can't be lessened in any way, and the reduction to your hit point maximum lasts until you finish a long rest.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level10(npc):
    choosetalent(npc)

    npc.traits.append("***Consumptive Power (Recharges on long rest).*** When activating a psionic discipline, you can pay its psi point cost with your hit points, instead of using any psi points. Your current hit points and hit point maximum are both reduced by the number of hit points you spend. This reduction can't be lessened in any way, and the reduction to your hit point maximum lasts until you finish a long rest.")
```

## Psionic Mastery
*11th-level Mystic feature*

Your mastery of psionic energy allows you to push your mind beyond its normal limits. As an action, you gain 9 special psi points that you can spend only on disciplines that require an action or a bonus action to use. You can use all 9 points on one discipline, or you can spread them across multiple disciplines. You can't also spend your normal psi points on these disciplines; you can spend only the special points gained from this feature. When you finish a long rest, you lose any of these special points that you haven't spent.

If more than one of the disciplines you activate with these points require concentration, you can concentrate on all of them. Activating one of them ends any effect you were already concentrating on, and if you begin concentrating on an effect that doesn't use these special points, the disciplines end that you're concentrating on.

At 15th level, the pool of psi points you gain from this feature increases to 11.

You have one use of this feature, and you regain any expended use of it with a long rest. You gain one additional use of this feature at 13th, 15th, and 17th level.

```
def level11(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Psionic Mastery ({'' if npc.levels('Mystic') < 13 else '2/' if npc.levels('Mystic') < 15 else '3/' if npc.levels('Mystic') < 17 else '4/'}Recharges on long rest).*** You gain {9 if npc.levels('Mystic') < 15 else 11} special psi points that you can spend only on disciplines that require an action or a bonus action to use. You can use all {9 if npc.levels('Mystic') < 15 else 11} points on one discipline, or you can spread them across multiple disciplines. You can't also spend your normal psi points on these disciplines; you can spend only the special points gained from this feature. If more than one of the disciplines you activate with these points require concentration, you can concentrate on all of them. Activating one of them ends any effect you were already concentrating on, and if you begin concentrating on an effect that doesn't use these special points, these disciplines end what you were concentrating on. When you finish a long rest, you lose any of these special points that you haven't spent.") )

def level12(npc): 
    abilityscoreimprovement(npc)
    choosediscipline(npc)

def level15(npc): choosediscipline(npc)

def level16(npc): abilityscoreimprovement(npc)

def level17(npc): choosetalent(npc)

def level18(npc): choosediscipline(npc)

def level19(npc): abilityscoreimprovement(npc)
```

## Psionic Body
*20th-level Mystic feature*

At 20th level, your mastery of psionic power causes your mind to transcend the body. Your physical form is infused with psionic energy. You gain the following benefits:

* You gain resistance to bludgeoning, piercing, and slashing damage.
* You no longer age.
* You are immune to disease, poison damage, and the poisoned condition.
* If you die, roll a d20. On a 10 or higher, you discorporate with 0 hit points, instead of dying, and you fall unconscious. You and your gear disappear. You appear at a spot of your choice 1d3 days later on the plane of existence where you died, having gained the benefits of one long rest.

```
def level20(npc):
    npc.damageresistances.append("bludgeoning")
    npc.damageresistances.append("piercing")
    npc.damageresistances.append("slashing")
    npc.damageimmunities.append("poison")
    npc.conditionimmunities.append("diseased")
    npc.conditionimmunities.append("poisoned")
    npc.traits.append("***Psionic Body.*** You no longer age. In addition, if you die, roll a d20. On a 10 or higher, you discorporate with 0 hit points, instead of dying, and you fall unconscious. You and your gear disappear. You appear at a spot of your choice 1d3 days later on the plane of existence where you died, having gained the benefits of one long rest.")
```

# Psionic Talents
Psionic talents are minor abilities that require psionic aptitude but don't drain a mystic's reservoir of psionic power. Talents are similar to disciplines and use the same rules, but with three important exceptions:

* You can never use your psychic focus on a talent.
* Talents don't require you to spend psi points to use them.
* Talents aren't linked to Mystic Orders.

### Beacon
*Psionic Talent*

As a bonus action, you cause bright light to radiate from your body in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. The light lasts for 1 hour, and you can extinguish it earlier as a bonus action.

```
def beacon(npc):
    npc.bonusactions.append(f"***Beacon.*** Bright light radiates from your body in a 20-foot radius and dim light for an additional 20 feet. The light can be colored as you like. The light lasts for 1 hour, and you can extinguish it earlier as a bonus action.")
```

### Blade Meld
*Psionic Talent*

As a bonus action, a one-handed melee weapon you hold becomes one with your hand. For the next minute, you can't let go of the weapon nor can it be forced from your grasp.

```
def blademeld(npc):
    npc.bonusactions.append(f"***Blade Meld.*** A one-handed melee weapon you hold becomes one with your hand. For the next minute, you can't let go of the weapon nor can it be forced from your grasp.")
```

### Blind Spot
*Psionic Talent*

As an action, you erase your image from the mind of one creature you can see within 120 feet of you; the target must succeed on a Wisdom saving throw, or you are invisible to it until the end of your next turn.

```
def blindspot(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Blind Spot.*** You erase your image from the mind of one creature you can see within 120 feet of you; the target must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}), or you are invisible to it until the end of your next turn.") )
```

### Delusion
*Psionic Talent*

As an action, you plant a false belief in the mind of one creature that you can see within 60 feet of you. You can create a sound or an image. Only the target of this talent perceives the sound or image you create.

If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a creature's roar, a musical instrument, or any other sound you pick. It lasts for 1 minute.

If you create an object, it must fit within a 5-foot cube and can't move or be reflective. The image can't create any effect that influences a sense other than sight. The image lasts for 1 minute, and it disappears if the creature touches it.

```
def delusion(npc):
    npc.actions.append(f"***Delusion.*** you plant a false belief in the mind of one creature that you can see within 60 feet of you. You can create a sound or an image. Only the target of this talent perceives the sound or image you create. If you create a sound, its volume can range from a whisper to a scream. It can be your voice, someone else's voice, a creature's roar, a musical instrument, or any other sound you pick. It lasts for 1 minute. If you create an object, it must fit within a 5-foot cube and can't move or be reflective. The image can't create any effect that influences a sense other than sight. The image lasts for 1 minute, and it disappears if the creature touches it.")
```

## Energy Beam
*Psionic Talent*

As an action, you target one creature you can see within 90 feet of you. The target must succeed on a Dexterity saving throw or take 1d8 acid, cold, fire, lightning, or thunder damage (your choice).

The talent's damage increases by 1d8 when you reach 5th level (2d8), 11th level (3d8), and 17th level (4d8).

```
def energybeam(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Energy Beam.*** You target one creature you can see within 90 feet of you. The target must succeed on a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or take {'1d8' if npc.levels('Mystic') < 5 else '2d8' if npc.levels('Mystic') < 11 else '3d8' if npc.levels('Mystic') < 17 else '4d8'} acid, cold, fire, lightning, or thunder damage (your choice).") )
```

## Light Step
*Psionic Talent*

As a bonus action, you alter your density and weight to improve your mobility. For the rest of your turn, your walking speed increases by 10 feet, and the first time you stand up this turn, you do so without expending any of your movement if your speed is greater than 0.

```
def lightstep(npc):
    npc.bonusactions.append(f"***Light Step.*** You alter your density and weight to improve your mobility. For the rest of your turn, your walking speed increases by 10 feet, and the first time you stand up this turn, you do so without expending any of your movement if your speed is greater than 0.")
```

## Mind Meld
*Psionic Talent*

As a bonus action, you can communicate telepathically with one willing creature you can see within 120 feet of you. The target must have an Intelligence of at least 2, otherwise this talent fails and the action is wasted.

This communication can occur until the end of the current turn. You don't need to share a language with the target for it to understand your telepathic utterances, and it understands you even if it lacks a language. You also gain access to one memory of the target's choice, gaining perfect recall of one thing it saw or did.

```
def mindmeld(npc):
    npc.bonusactions.append(f"***Mind Meld.*** You can communicate telepathically with one willing creature you can see within 120 feet of you. The target must have an Intelligence of at least 2, otherwise this talent fails and the action is wasted. This communication can occur until the end of the current turn. You don't need to share a language with the target for it to understand your telepathic utterances, and it understands you even if it lacks a language. You also gain access to one memory of the target's choice, gaining perfect recall of one thing it saw or did.")
```

## Mind Slam
*Psionic Talent*

As an action, you target one creature you can see within 60 feet of you. The target must succeed on a Constitution saving throw or take 1d6 force damage. If it takes any of this damage and is Large or smaller, it is knocked prone.

The talent's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).

```
def mindslam(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Mind Slam.*** You target one creature you can see within 60 feet of you. The target must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or take {'1d6' if npc.levels('Mystic') < 5 else '2d6' if npc.levels('Mystic') < 11 else '3d6' if npc.levels('Mystic') < 17 else '4d6'} force damage. If it takes any of this damage and is Large size or smaller, it is knocked prone.") )
```

## Mind Thrust
*Psionic Talent*

As an action, you target one creature you can see within 120 feet of you. The target must succeed on an Intelligence saving throw or take 1d10 psychic damage.

The talent's damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).

```
def mindthrust(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Mind Thrust.*** You target one creature you can see within 120 feet of you. The target must succeed on an Intelligence saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or take {'1d10' if npc.levels('Mystic') < 5 else '2d10' if npc.levels('Mystic') < 11 else '3d10' if npc.levels('Mystic') < 17 else '4d10'} psychic damage.") )
```

## Mystic Charm
*Psionic Talent*

As an action, you beguile one humanoid you can see within 120 feet of you. The target must succeed on a Charisma saving throw or be charmed by you until the end of your next turn.

```
def mysticcharm(npc):
    npc.actions.append(f"***Mystic Charm.*** You beguile one humanoid you can see within 120 feet of you. The target must succeed on a Charisma saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or be charmed by you until the end of your next turn.")
```

## Mystic Hand
*Psionic Talent*

You can use your action to manipulate or move one object within 30 feet of you. The object can't weigh more than 10 pounds, and you can't affect an object being worn or carried by another creature. If the object is loose, you can move it up to 30 feet in any direction.

This talent allows you to open an unlocked door, pour out a beer stein, and so on.

The object falls to the ground at the end of your turn if you leave it suspended in midair.

```
def mystichand(npc):
    npc.actions.append(f"***Mystic Hand.*** You manipulate or move one object within 30 feet of you. The object can't weigh more than 10 pounds, and you can't affect an object being worn or carried by another creature. If the object is loose, you can move it up to 30 feet in any direction. This talent allows you to open an unlocked door, pour out a beer stein, and so on. The object falls to the ground at the end of your turn if you leave it suspended in midair.")
```

## Psychic Hammer
*Psionic Talent*

As an action, you try to grasp one creature you can see within 120 feet of you, with a hand crafted from telekinetic energy. The target must succeed on a Strength saving throw or take 1d6 force damage. If it takes any of this damage and is Large or smaller, you can move it up to 10 feet in a straight line in a direction of your choice. You can't lift the target off the ground unless it is already airborne or underwater.

The talent's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).

```
def psychichammer(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Psychic Hammer.*** You try to grasp one creature you can see within 120 feet of you, with a hand crafted from telekinetic energy. The target must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or take {'1d6' if npc.levels('Mystic') < 5 else '2d6' if npc.levels('Mystic') < 11 else '3d6' if npc.levels('Mystic') < 17 else '4d6'} force damage. If it takes any of this damage and is Large or smaller, you can move it up to 10 feet in a straight line in a direction of your choice. You can't lift the target off the ground unless it is already airborne or underwater.") )
```

```
talents = {
    'Beacon' : beacon,
    'Blade Meld' : blademeld,
    'Blind Spot' : blindspot,
    'Delusion' : delusion,
    'Energy Beam' : energybeam,
    'Light Step' : lightstep,
    'Mind Meld' : mindmeld,
    'Mind Slam' : mindslam,
    'Mind Thrust' : mindthrust,
    'Mystic Charm' : mysticcharm,
    'Mystic Hand' : mystichand,
    'Psychic Hammer': psychichammer
}
def choosetalent(npc):
    choices = {}
    for poss in talents:
        if poss not in npc.psionictalents:
            choices[poss] = talents[poss]
    (talentname, talentfn) = choose("Choose a Psionic Talent: ", choices)
    npc.psionictalents.append(talentname)
    talentfn(npc)
```

# Psionic Disciplines
Psionic disciplines are the heart of a mystic's craft. They are the mental exercises and psionic formulae used to forge will into tangible, magical effects.

Psionic disciplines were each discovered by different orders and tend to reflect their creators' specialties. However, a mystic can learn any discipline regardless of its associated order.

## Using a Discipline
Each psionic discipline has several ways you can use it, all contained in its description. The discipline specifies the type of action and number of psi points it requires. It also details whether you must concentrate on its effects, how many targets it affects, what saving throws it requires, and so on.

The following sections go into more detail on using a discipline. Psionic disciplines are magical and function similarly to spells.

### Psychic Focus
The Psychic Focus section of a discipline describes the benefit you gain when you choose that discipline for your psychic focus.

### Effect Options and Psi Points
A discipline provides different options for how to use it with your psi points. Each effect option has a name, and the psi point cost of that option appears in parentheses after its name. You must spend that number of psi points to use that option, while abiding by your psi limit. If you don't have enough psi points left, or the cost is above your psi limit, you can't use the option.

Some options show a range of psi points, rather than a specific cost. To use that option, you must spend a number of points within that point range, still abiding by your psi limit. Some options let you spend additional psi points to increase a discipline's potency. Again, you must abide by your psi limit, and you must spend all the points when you first use the discipline; you can't decide to spend additional points once you see the discipline in action.

Each option notes specific information about its effect, including any action required to use it and its range.

### Components
Disciplines don't require the components that many spells require. Using a discipline requires no spoken words, gestures, or materials. The power of psionics comes from the mind.

### Duration
An effect option in a discipline specifies how long its effect lasts.

***Instantaneous.*** If no duration is specified, the effect of the option is instantaneous.

***Concentration.*** Some options require concentration to maintain their effects. This requirement is noted with "conc." after the option's psi point cost. The "conc." notation is followed by the maximum duration of the concentration. For example, if an option says "conc., 1 min.," you can concentrate on its effect for up to 1 minute. Concentrating on a discipline follows the same rules as concentrating on a spell. This rule means you can't concentrate on a spell and a discipline at the same time, nor can you concentrate on two disciplines at the same time.

### Targets and Areas of Effect
Psionic disciplines use the same rules as spells for determining targets and areas of effect.

**Saving Throws** and **Attack Rolls**. If a discipline requires a saving throw, it specifies the type of save and the results of a successful or failed saving throw. The DC is determined by your psionic ability.

Some disciplines require you to make an attack roll to determine whether the discipline's effect hits its target. The attack roll uses your psionic ability.

### Combining Psionic Effects
The effects of different psionic disciplines add together while the durations of the disciplines overlap. Likewise, different options from a psionic discipline combine if they are active at the same time. However, a specific option from a psionic discipline doesn't combine with itself if the option is used multiple times. Instead, the most potent effect--usually dependent on how many psi points were used to create the effect--applies while the durations of the effects overlap.

Psionics and spells are separate effects, and therefore their benefits and drawbacks overlap. A psionic effect that reproduces a spell is an exception to this rule.

```
disciplines = {
}

def choosediscipline(npc, disciplinelist = None):
    if disciplinelist == None:
        disciplinelist = disciplines

    choices = {}
    for poss in disciplinelist:
        if poss not in npc.psionicdisciplines:
            choices[poss] = disciplinelist[poss]
    (discname, discfn) = choose("Choose a Psionic Discipline: ", choices)
    npc.psionicdisciplines.append(discname)
    discstruct = discfn(npc)
```
