# Mystic Order: Order of the Nomad
Mystics of the Order of the Nomad keep their minds in a strange, rarified state. They seek to accumulate as much knowledge as possible, as they quest to unravel the mysteries of the multiverse and seek the underlying structure of all things. At the same time, they perceive a bizarre, living web of knowledge they call the noosphere.

Nomads, as their name indicates, delight in travel, exploration, and discovery. They desire to accumulate as much knowledge as possible, and the pursuit of secrets and hidden lore can become an obsession for them.

```
name = 'Order of the Nomad'
description = "***Mystic Order: Order of the Nomad.*** Mystics of the Order of the Nomad keep their minds in a strange, rarified state. They seek to accumulate as much knowledge as possible, as they quest to unravel the mysteries of the multiverse and seek the underlying structure of all things. At the same time, they perceive a bizarre, living web of knowledge they call the noosphere."
```

## Bonus Disciplines
*1st-level Order of the Nomad feature*

You learn two additional psionic disciplines of your choice. They must be chosen from among the Nomad disciplines.

```
def level1(npc):
    allclasses['Mystic'].choosediscipline(npc, nomaddisciplines)
    allclasses['Mystic'].choosediscipline(npc, nomaddisciplines)
```

## Breadth of Knowledge
*1st-level Order of the Nomad feature*

You gain the ability to extend your knowledge. When you finish a long rest, you gain two proficiencies of your choice: two tools, two skills, or one of each. You can replace one or both of these selections with languages. This benefit lasts until you finish a long rest.

```
    npc.traits.append("***Breadth of Knowledge.*** When you finish a long rest, you gain two proficiencies of your choice: two tools, two skills, or one of each. You can replace one or both of these selections with languages. This benefit lasts until you finish a long rest.")
```

## Memory of One Thousand Steps
*3rd-level Order of the Nomad feature*

You gain the ability to use psionics to recall your steps. As a reaction when you are hit by an attack, you can teleport to an unoccupied space that you occupied since the start of your last turn, and the attack misses you. Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level3(npc):
    npc.reactions.append("***Memory of One Thousand Steps (Recharges on short or long rest).*** When you are hit by an attack, you can teleport to an unoccupied space that you occupied since the start of your last turn, and the attack misses you.")
```

## Superior Teleportation
*6th-level Order of the Nomad feature*

You gain a superior talent for teleportation. When you use a psionic discipline to teleport any distance, you can increase that distance by up to 10 feet.

```
def level6(npc):
    npc.traits.append("***Superior Teleportation.*** When you use a psionic discipline to teleport any distance, you can increase that distance by up to 10 feet.")
```

## Effortless Journey
*14th-level Order of the Nomad feature*

Your mind can mystically move your body. Once on each of your turns, you can forfeit up to 30 feet of your movement to teleport the distance you forfeited. You must teleport to an unoccupied space you can see.

```
def level14(npc):
    npc.actions.append("***Effortless Journey.*** Once on each of your turns, you can forfeit up to 30 feet of your movement to teleport the distance you forfeited. You must teleport to an unoccupied space you can see.")
```

## Nomad Psionic Disciplines
* [nomadic arrow](Disciplines/nomadic-arrow.md)
* [nomadic chameleon](Disciplines/nomadic-chameleon.md)
* [nomadic mind](Disciplines/nomadic-mind.md)
* [nomadic step](Disciplines/nomadic-step.md)
* [third eye](Disciplines/third-eye.md)

```
def nomadicarrow(npc):
    npc.bonusactions.append("***Psychic Focus: Nomadic Arrow.*** While you are focused on this discipline, any attack roll you make for a ranged weapon attack ignores disadvantage. If disadvantage would normally apply to the roll, that roll also can’t benefit from advantage.")

    npc.bonusactions.append("***Speed Dart (1–7 psi).*** You imbue one ranged weapon you hold with psionic power. The next attack you make with it that hits before the end of the current turn deals an extra 1d10 psychic damage per psi point spent.")

    npc.reactions.append("***Seeking Missile (2 psi).*** When you miss with a ranged weapon attack, you can repeat the attack roll against the same target.")

    npc.bonusactions.append("***Faithful Archer (5 psi; concentration, 1 min.).*** You imbue a ranged weapon with a limited sentience. Until your concentration ends, you can make an extra attack with the weapon at the start of each of your turns (no action required). If it is a thrown weapon, it returns to your grasp each time you make any attack with it.")

def nomadicchameleon(npc):
    npc.bonusactions.append("***Psychic Focus: Nomadic Chameleon.*** While focused on this discipline, you have advantage on Dexterity (Stealth) checks.")

    npc.actions.append("***Chameleon (2 psi).*** You can attempt to hide even if you fail to meet the requirements needed to do so. At the end of the current turn, you remain hidden only if you then meet the normal requirements for hiding.")

    npc.bonusactions.append("***Step from Sight (3 psi; concentration, 1 min.).*** You cloak yourself from sight. You can target one additional creature for every additional psi point you spend on this ability. The added targets must be visible to you and within 60 feet of you. Each target turns invisible and remains so until your concentration ends or until immediately after it targets, damages, or otherwise affects any creature with an attack, a spell, or another ability.")

    npc.bonusactions.append("***Enduring Invisibility (7 psi; concentration, 1 min.).*** You turn invisible and remain so until your concentration ends.")

def nomadicmind(npc):
    npc.bonusactions.append("***Psychic Focus: Nomadic Mind.*** Whenever you focus on this discipline, you choose one skill or tool and have proficiency with it until your focus ends. Alternatively, you gain the ability to read and write one language of your choice until your focus ends.")

    npc.traits.append("***Wandering Mind (2–6 psi; concentration, 10 min.).*** You enter a deep contemplation. If you concentrate for this option’s full duration, you then gain proficiency with up to three of the following skills (one skill for every 2 psi points spent): Animal Handling, Arcana, History, Medicine, Nature, Performance, Religion, and Survival. The benefit lasts for 1 hour, no concentration required.")

    npc.traits.append("***Find Creature (2 psi; concentration, 1 hr.).*** You cast your mind about for information about a specific creature. If you concentrate for this option’s full duration, you then gain a general understanding of the creature’s current location. You learn the region, city, town, village, or district where it is, pinpointing an area between 1 and 3 miles on a side (DM’s choice). If the creature is on another plane of existence, you instead learn which plane.")

    npc.traits.append("***Item Lore (3 psi; concentration, 1 hr.).*** You carefully study an item. If you concentrate for this option’s full duration while remaining within 5 feet of the item, you then gain the benefits of an identify spell cast on that item.")

    npc.actions.append("***Psychic Speech (5 psi).*** You attune your mind to the psychic imprint of all language. For 1 hour, you gain the ability to understand any language you hear or attempt to read. In addition, when you speak, all creatures that can understand a language understand what you say, regardless of what language you use.")

    npc.actions.append("***Wandering Eye (6 psi; concentration, 1 hr.).*** You create a psychic sensor within 60 feet of you. The sensor lasts until your concentration ends. The sensor is invisible and hovers in the air. You mentally receive visual information from it, which has normal vision and darkvision with a range of 60 feet. The sensor can look in all directions. As an action, you can move the sensor up to 30 feet in any direction. There is no limit to how far away from you the eye can move, but it can’t enter another plane of existence. A solid barrier blocks the eye’s movement, but the eye can pass through an opening as small as 1 inch in diameter.")

    npc.actions.append("***Phasing Eye (7 psi; concentration, 1 hr.).*** As Wandering Eye above, except the eye can move through solid objects but can’t end its movement in one. If it does so, the effect immediately ends.")

def nomadicstep(npc):
    npc.bonusactions.append("***Psychic Focus: Nomadic Step.*** After you teleport on your turn while focused on this discipline, your walking speed increases by 10 feet until the end of the turn, as you are propelled by the magic of your teleportation. You can receive this increase only once per turn.")

    npc.bonusactions.append("***Step of a Dozen Paces (1–7 psi).*** If you haven’t moved yet on your turn, you teleport up to 20 feet per psi point spent to an unoccupied space you can see, and your speed is reduced to 0 until the end of the turn.")

    npc.actions.append("***Nomadic Anchor (1 psi).*** You create an invisible, intangible teleportation anchor in a 5-foot cube you can see within 120 feet of you. For the next 8 hours, whenever you use this psionic discipline to teleport, you can instead teleport to the anchor, even if you can’t see it, but it must be within range of the teleportation ability.")

    npc.reactions.append("***Defensive Step (2 psi).*** When you are hit by an attack, you gain a +4 bonus to AC against that attack, possibly turning it into a miss. You then teleport up to 10 feet to an unoccupied space you can see.")

    npc.bonusactions.append("***There and Back Again (2 psi).*** You teleport up to 20 feet to an unoccupied space you can see and then move up to half your speed. At the end of your turn, you can teleport back to the spot you occupied before teleporting, unless it is now occupied or on a different plane of existence.")

    npc.bonusactions.append("***Transposition (3 psi).*** If you haven’t moved yet on your turn, choose an ally you can see within 60 feet of you. You and that creature teleport, swapping places, and your speed is reduced to 0 until the end of the turn. This ability fails and is wasted if either of you can’t fit in the destination space.")

    npc.actions.append("***Baleful Transposition (5 psi).*** Choose one creature you can see within 120 feet of you. That creature must make a Wisdom saving throw. On a failed save, you and that creature teleport, swapping places. This ability fails and is wasted if either of you can’t fit in the destination space.")

    npc.actions.append("***Phantom Caravan (6 psi).*** You and up to six willing creatures of your choice that you can see within 60 feet of you teleport up to 1 mile to a spot you can see. If there isn’t an open space for all the targets to occupy at the arrival point, this ability fails and is wasted.")

    npc.actions.append("***Nomad’s Gate (7 psi; concentration, 1 hr.).*** You create a 5-foot cube of dim, gray light within 5 feet of you. You create an identical cube at any point of your choice within 1 mile that you have viewed within the past 24 hours. Until your concentration ends, anyone entering one of the cubes immediately teleports to the other one, appearing in an unoccupied space next to it. The teleportation fails if there is no space for the creature to appear in.")

def thirdeye(npc): 
    npc.bonusactions.append("***Psychic Focus.*** While focused on this discipline, you have darkvision with a range of 60 feet. If you already have darkvision with that range or greater, increase its range by 10 feet.")

    npc.bonusactions.append("***Tremorsense (2 psi; concentration, 1 min.).*** You gain tremorsense with a radius of 30 feet, which lasts until your concentration ends.")

    npc.bonusactions.append("***Unwavering Eye (2 psi).*** You gain advantage on Wisdom checks for 1 minute.")

    npc.bonusactions.append("***Piercing Sight (3 psi; concentration, 1 min.).*** You gain the ability to see through objects that are up to 1 foot thick within 30 feet of you. This sight lasts until your concentration ends")

    npc.bonusactions.append("***Truesight (5 psi; concentration, 1 min.).*** You gain truesight with a radius of 30 feet, which lasts until your concentration ends.")


nomaddisciplines = {
    'Nomadic Arrow': nomadicarrow,
    'Nomadic Chameleon': nomadicchameleon,
    'Nomadic Mind': nomadicmind,
    'Nomadic Step': nomadicstep,
    'Third Eye': thirdeye
}
for ad in nomaddisciplines:
    allclasses['Mystic'].disciplines[ad] = nomaddisciplines[ad]
```
