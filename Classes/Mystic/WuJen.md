# Mystic Order: Order of the Wu Jen
The Order of the Wu Jen features some of the most devoted mystics. These mystics seek to lock themselves away from the world, denying the limits of the physical world and replacing it with a reality that they create for themselves. Known as wu jens, these mystics cast their minds into the world, seize control of its fundamental principles, and rebuild it.

In practical terms, wu jens excel at controlling the forces of the natural world. They can hurl objects with their minds, control the four elements, and alter reality to fit their desires.

```
name = 'Order of the Wu Jen'
description = "***Mystic Order: Order of the Wu Jen.*** The Order of the Wu Jen features some of the most devoted mystics. These mystics seek to lock themselves away from the world, denying the limits of the physical world and replacing it with a reality that they create for themselves. Known as wu jens, these mystics cast their minds into the world, seize control of its fundamental principles, and rebuild it."
```

## Bonus Disciplines
*1st-level Order of the Wu Jen feature*

You learn two additional psionic disciplines of your choice. They must be chosen from among the Wu Jen disciplines.

```
def level1(npc):
    allclasses['Mystic'].choosediscipline(npc, wujendisciplines)
    allclasses['Mystic'].choosediscipline(npc, wujendisciplines)
```

## Hermit's Study
*1st-level Order of the Wu Jen feature*

You gain proficiency with two of the following skills of your choice: Animal Handling, Arcana, History, Insight, Medicine, Nature, Perception, Religion, or Survival.

```
    chooseskill(npc, ['Animal Handling', 'Arcana', 'History', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'])
    chooseskill(npc, ['Animal Handling', 'Arcana', 'History', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'])
```

## Elemental Attunement
*3rd-level Order of the Wu Jen feature*

When a creature's resistance reduces the damage dealt by a psionic discipline of yours, you can spend 1 psi point to cause that use of the discipline to ignore the creature's resistance. You can't spend this point if doing so would increase the discipline's cost above your psi limit.

```
def level3(npc):
    npc.traits.append("***Elemental Attunement.*** When a creature's resistance reduces the damage dealt by a psionic discipline of yours, you can spend 1 psi point to cause that use of the discipline to ignore the creature's resistance. You can't spend this point if doing so would increase the discipline's cost above your psi limit.")
```

## Arcane Dabbler
*6th-level Order of the Wu Jen feature*

You learn three wizard spells of your choice and always have them prepared. The spells must be of 1st through 3rd level.

As a bonus action, you can spend psi points to create spell slots that you can use to cast these spells, as well as other spells you are capable of casting. The psi-point cost of each spell slot is detailed on the table below.

Spell Slot Level|Psi Cost
----------------|--------
1st | 2
2nd | 3
3rd | 5
4th | 6
5th | 7

The spell slot remains until you use it or finish a long rest. You must observe your psi limit when spending psi points to create a spell slot.

Whenever you gain a level in this class, you can replace one of the chosen wizard spells with a different wizard spell of 1st through 3rd level.

```
def level6(npc):
    spellcasting = npc.newspellcasting('Mystic', 'INT', named='Wu Jen Spellcasting')
    spellcasting.casterclass = allclasses['Mystic']
    spellcasting.maxspellsknown = 3
    npc.bonusactions.append("***Arcane Dabbler.*** You can spend psi points to create spell slots (**2 psi:** 1st-level slot, **3:** 2nd, **5:** 3rd, **6:** 4th, **7:** 5th) that you can use to cast these spells, as well as other spells you are capable of casting. The spell slot remains until you use it or finish a long rest. You must observe your psi limit when spending psi points to create a spell slot.")
```

## Elemental Mastery
*14th-level Order of the Wu Jen feature*

If you have resistance to a type of damage, you can spend 2 psi points as a reaction when you take damage of that type to ignore that damage; you gain immunity to that damage type until the end of your next turn.

```
def level14(npc):
    npc.reactions.append("***Elemental Mastery.*** If you have resistance to a type of damage, you can spend 2 psi points when you take damage of that type to ignore that damage; you gain immunity to that damage type until the end of your next turn.")
```

## WuJen Psionic Disciplines
* [Mastery of Air](../../Magic/Disciplines/mastery-of-air.md)
* [Mastery of Fire](../../Magic/Disciplines/mastery-of-fire.md)
* [Mastery of Force](../../Magic/Disciplines/mastery-of-force.md)
* [Mastery of Ice](../../Magic/Disciplines/mastery-of-ice.md)
* [Mastery of Light and Darkness](../../Magic/Disciplines/mastery-of-light-and-darkness.md)
* [Mastery of Water](../../Magic/Disciplines/mastery-of-water.md)
* [Mastery of Weather](../../Magic/Disciplines/mastery-of-weather.md)
* [Mastery of Wood and Earth](../../Magic/Disciplines/mastery-of-wood-and-earth.md)

```
def masteryofair(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Air.*** While focused on this discipline, you take no falling damage, and you ignore difficult terrain when walking. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Wind Step (1–7 psi).*** As part of your move on your turn, you can fly up to 20 feet for each psi point spent. If you end this flight in the air, you fall unless something else holds you aloft.")

    npc.actions.append("***Wind Stream (1–7 psi).*** You create a line of focused air that is 30 feet long and 5 feet wide. Each creature in that area must make a Strength saving throw, taking 1d8 bludgeoning damage per psi point spent and being knocked prone on a failed save, or half as much damage on a successful one.")

    npc.bonusactions.append("***Cloak of Air (3 psi; concentration, 10 min.).*** You seize control of the air around you to create a protective veil. Until your concentration ends, attack rolls against you have disadvantage, and when a creature you can see misses you with a melee attack, you can use your reaction to force the creature to repeat the attack roll against itself.")

    npc.bonusactions.append("***Wind Form (5 psi; concentration, 10 min.).*** You gain a flying speed of 60 feet, which lasts until your concentration ends.")

    npc.actions.append("***Misty Form (6 psi; concentration, 1 min.).*** Your body becomes like a misty cloud until your concentration ends. In this form, you gain resistance to bludgeoning, piercing, and slashing damage, and you can’t take actions other than the Dash action. You can pass through openings that are no more than 1 inch wide without squeezing.")

    npc.actions.append("***Animate Air (7 psi; concentration, 1 hr.).*** You cause an air elemental to appear in an unoccupied space you can see within 120 feet of you. The elemental lasts until your concentration ends, and it obeys your verbal commands. In combat, roll for its initiative, and choose its behavior during its turns. When this effect ends, the elemental disappears.")

def masteryoffire(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of fire.*** While focused on this discipline, you gain resistance to fire damage, and you gain a +2 bonus to rolls for fire damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Combustion (1–7 psi; concentration, 1 min.).*** Choose one creature or object you can see within 120 feet of you. The target must make a Constitution save. On a failed save, the target takes 1d10 fire damage per psi point spent, and it catches on fire, taking 1d6 fire damage at the end of each of its turns until your concentration ends or until it or a creature adjacent to it extinguishes the flames with an action. On a successful save, the target takes half as much damage and doesn’t catch on fire.")

    npc.actions.append("***Rolling Flame (3 psi; concentration, 1 min.).*** You create fire in a 20-foot-by-20-foot cube within 5 feet of you. The fire lasts until your concentration ends. Any creature in that area when you use this ability and any creature that ends its turn there takes 5 fire damage.")

    npc.actions.append("***Detonation (5 psi).*** You create a fiery explosion at a point you can see within 120 feet of you. Each creature in a 20-foot-radius sphere centered on that point must make a Constitution saving throw, taking 7d6 fire damage and being knocked prone on a failed save, or half as much damage on a successful one.")

    npc.bonusactions.append("***Fire Form (5 psi; concentration, 1 min.).*** You become wreathed in flames until your concentration ends. Any creature that end its turn within 5 feet of you takes 3d6 fire damage.")

    npc.actions.append("***Animate Fire (7 psi; concentration, 1 hr.).*** You cause a fire elemental to appear in an unoccupied space you can see within 120 feet of you. The elemental lasts until your concentration ends, and it obeys your verbal commands. In combat, roll for its initiative, and choose its behavior during its turns. When this effect ends, the elemental disappears.")

def masteryofforce(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Force.*** While focused on this discipline, you have advantage on Strength checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Push (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must make a Strength saving throw. On a failed save, it takes 1d8 force damage per psi point spent and is pushed up to 5 feet per point spent in a straight line away from you. On a successful save, it takes half as much damage.")

    npc.actions.append("***Move (2–7 psi).*** Choose one object you can see within 60 feet of you that isn’t being worn or carried by another creature and that isn’t secured in place. It can’t be larger than 20 feet on a side, and its maximum weight depends on the psi points spent on this ability (**2**: 25 lbs; **3**: 50lbs; **5**: 250lbs; **6**: 500lbs; **7**: 1000lbs). You move the object up to 60 feet, and you must keep the object within sight during this movement. If the object ends this movement in the air, it falls. If the object would fall on a creature, the creature must succeed on a DC 10 Dexterity saving throw. On failure, the creature takes damage as given by the weight/psi spent: **2**: 2d6; **3**: 4d6; **5**: 6d6; **6**: 7d6; **7**: 8d6.")

    npc.actions.append("***Inertial Armor (2 psi).*** You sheathe yourself in an intangible field of magical force. For 8 hours, your base AC is 14 + your Dexterity modifier, and you gain resistance to force damage. This effect ends if you are wearing or don armor.")

    npc.actions.append("***Telekinetic Barrier (3 psi; concentration, 10 min.).*** You create a transparent wall of telekinetic energy, at least one portion of which must be within 60 feet of you. The wall is 40 feet long, 10 feet high, and 1 inch thick. The wall lasts until your concentration ends. Each 10-foot section of the wall has an AC of 10 and 10 hit points.")

    npc.actions.append("***Grasp (3 psi; concentration, 1 min.).*** You attempt to grasp a creature in telekinetic energy and hold it captive. Choose one creature you can see within 60 feet of you. The target must succeed on a Strength saving throw or be grappled by you until your concentration ends or until the target leaves your reach, which is 60 feet for this grapple. The grappled target can escape by succeeding on a Strength (Athletics) or Dexterity (Acrobatics) check contested by your psionic ability plus your proficiency bonus. When a target attempts to escape in this way, you can spend psi points to boost your check, abiding by your psi limit. You gain a +1 bonus per psi point spent. While a target is grappled in this manner, you create one of the following effects as an action: **Crush (1–7 psi)**. The target takes 1d6 bludgeoning damage per psi point spent; **Move (1–7 psi)**. You move the target up to 5 feet per psi point spent. You can move it in the air and hold it there. It falls if the grapple ends.")

def masteryofice(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Ice.*** While focused on this discipline, you have resistance to cold damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Ice Spike (1–7 psi).*** You hurl a mote of ice at one creature you can see within 120 feet of you. The target must make a Dexterity saving throw. On a failed save, the target takes 1d8 cold damage per psi point spent and has its speed halved until the start of your next turn. On a successful save, the target takes half as much damage.")

    npc.actions.append("***Ice Sheet (2 psi).*** Choose a point on the ground you can see within 60 feet of you. The ground in a 20-foot radius centered on that point becomes covered in ice for 10 minutes. It is difficult terrain, and any creature that moves more than 10 feet on it must succeed on a Dexterity saving throw or fall prone. If the surface is sloped, a creature that falls prone in the area immediately slides to the bottom of the slope.")

    npc.bonusactions.append("***Frozen Sanctuary (3 psi).*** You sheathe yourself with icy resilience. You gain 20 temporary hit points.")

    npc.actions.append("***Frozen Rain (5 psi; concentration, 1 min.).*** Choose a point you can see within 120 feet of you. The air in a 20-foot-radius sphere centered on that point becomes deathly cold and saturated with moisture. Each creature in that area must make a Constitution saving throw. On a failed save, a target takes 6d6 cold damage, and its speed is reduced to 0 until your concentration ends. On a successful save, a target takes half as much damage. A target that has its speed reduced can end the effect early if it succeeds on a Strength (Athletics) check with a DC equal to this effect’s save DC. You can increase this effect’s damage by 1d6 per each additional psi point spent on it.")

    npc.actions.append("***Ice Barrier (6 psi; concentration, 10 min.).*** You create a wall of ice, at least one portion of which must be within 60 feet of you. The wall is 60 feet long, 15 feet high, and 1 foot thick. The wall lasts until your concentration ends. Each 10-foot section of the wall has AC 12 and 30 hit points. A creature that damages the wall with a melee attack takes cold damage equal to the damage the creature dealt to the wall.")

def masteryoflightanddarkness(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Light and Darkness.*** While focused on this discipline, natural and magical darkness within 30 feet of you has no effect on your vision. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Darkness (1–7 psi).*** You create an area of magical darkness, which foils darkvision. Choose a spot you can see within 60 feet of you. Magical darkness radiates from that point in a sphere with a 10-foot radius per psi point spent on this ability. The light produced by spells of 2nd level or less is suppressed in this area.")

    npc.actions.append("***Light (2 psi; concentration, 1 min.).*** An object you touch radiates light in a 20-foot radius and dim light for an additional 20 feet. The light lasts until your concentration ends. Alternatively, a creature you touch radiates light in the same manner if it fails a Dexterity saving throw. While lit in this manner, it can’t hide, and attack rolls against it gain advantage.")

    npc.actions.append("***Shadow Beasts (3 psi; concentration, 1 min.).*** You cause two shadows to appear in unoccupied spaces you can see within 60 feet of you. The shadows last until your concentration ends, and they obey your verbal commands. In combat, roll for their initiative, and choose their behavior during their turns. When this effect ends, the shadows disappear. See the Monster Manual for their stat block.")

    npc.actions.append("***Radiant Beam (5 psi; concentration, 1 min.).*** You project a beam of light at one creature you can see within 60 feet of you. The target must make a Dexterity saving throw. On a failed save, it takes 6d6 radiant damage and is blinded until your concentration ends. On a successful save, it takes half as much damage. A blinded target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a success. You can increase this effect’s damage by 1d6 per each additional psi point spent on it.")

def masteryofwater(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Water.*** While focused on this discipline, you have a swimming speed equal to your walking speed, and you can breathe underwater. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Desiccate (1–7 psi).*** Choose one creature you can see within 60 feet of you. The target must make a Constitution saving throw, taking 1d10 necrotic damage per psi point spent on this ability, or half as much damage on a successful one.")

    npc.actions.append("***Watery Grasp (2 psi).*** You unleash a wave that surges forth and then retreats to you like the rising tide. You create a wave in a 20-foot-by-20-foot square. At least some portion of the square’s border must be within 5 feet of you. Any creature in that square must make a Strength saving throw. On a failed save, a target takes 2d6 bludgeoning damage, is knocked prone, and is pulled up to 10 feet closer to you. On a successful save, a target takes half as much damage. You can increase this ability’s damage by 1d6 per additional psi point spent on it.")

    npc.actions.append("***Water Whip (3 psi).*** You unleash a jet of water in a line that is 60 feet long and 5 feet wide. Each creature in the line must make a Strength saving throw, taking 3d6 bludgeoning damage on a failed save, or half as much damage on a successful one. In addition, you can move each target that fails its saving throw to any unoccupied space touching the line. You can increase this ability’s damage by 1d6 per additional psi point spent on it.")

    npc.actions.append("***Water Breathing (5 psi).*** You grant yourself and up to ten willing creatures you can see within 60 feet of you the ability to breathe underwater for the next 24 hours.")

    npc.actions.append("***Water Sphere (6 psi; concentration, 1 min.).*** You cause a sphere of water to form around a creature. Choose one creature you can see within 60 feet of you. The target must make a Dexterity saving throw. On a failed save, it becomes trapped in the sphere of water until your concentration ends. While the target is trapped, its speed is halved, it suffers disadvantage on attack rolls, and it can’t see anything more than 10 feet away from it. However, attack rolls against it also suffer disadvantage. The target can repeat the saving throw at the end of each of its turns, ending the effect on itself on a successful one.")

    npc.actions.append("***Animate Water (7 psi; concentration, 1 hr.).*** You cause a water elemental to appear in an unoccupied space you can see within 120 feet of you. The elemental lasts until your concentration ends, and it obeys your verbal commands. In combat, roll for its initiative, and choose its behavior during its turns. When this effect ends, the elemental disappears. See the Monster Manual for its stat block.")

def masteryofweather(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Water.*** While focused on this discipline, you have resistance to lightning and thunder damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Cloud Steps (1–7 psi; concentration, 10 min.).*** You conjure forth clouds to create a solid, translucent staircase that lasts until your concentration ends. The stairs form a spiral that fills a 10-foot-by-10-foot area and reaches upward 20 feet per psi point spent.")

    npc.actions.append("***Hungry Lightning (1–7 psi).*** You lash out at one creature you can see within 60 feet of you with tendrils of lightning. The target must make a Dexterity saving throw, with disadvantage if it’s wearing heavy armor. The target takes 1d8 lightning damage per psi point spent on a failed save, or half as much damage on a successful one.")

    npc.actions.append("***Wall of Clouds (2 psi; concentration, 10 min.).*** You create a wall of clouds, at least one portion of which must be within 60 feet of you. The wall is 60 feet long, 15 feet high, and 1 foot thick. The wall lasts until your concentration ends. Creatures can pass through it without hindrance, but the wall blocks vision.")

    npc.actions.append("***Whirlwind (2 psi).*** Choose a point you can see within 60 feet of you. Winds howl in a 20-foot-radius sphere centered on that point. Each creature in the sphere must succeed on a Strength saving throw or take 1d6 bludgeoning damage and be moved to an unoccupied space of your choice in the sphere. Any loose object in the sphere is moved to an unoccupied space of your choice within it if the object weighs no more than 100 pounds.")

    npc.actions.append("***Lightning Leap (5 psi).*** You let loose a line of lightning that is 60 feet long and 5 feet wide. Each creature in the line must make a Dexterity saving throw, taking 6d6 lightning damage on a failed save, or half as much damage on a successful one. You can then teleport to an unoccupied space touched by the line. You can increase this ability’s damage by 1d6 per additional psi point spent on it.")

    npc.actions.append("***Wall of Thunder (6 psi; concentration, 10 min.).*** You create a wall of thunder, at least one portion of which must be within 60 feet of you. The wall is 60 feet long, 15 feet high, and 1 foot thick. The wall lasts until your concentration ends. Every foot moved through the wall costs 1 extra foot of movement. When a creature moves into the wall’s space for the first time on a turn or starts its turn there, that creature must succeed on a Strength saving throw, or it takes 6d6 thunder damage, is pushed in a straight line up to 30 feet away from the wall, and is knocked prone.")

    npc.actions.append("***Thunder Clap (7 psi).*** Choose a point you can see within 60 feet of you. Thunder energy erupts in a 20-foot-radius sphere centered on that point. Each creature in that area must make Constitution saving throw. On a failed save, a target takes 8d6 thunder damage, and it is stunned until the end of your next turn. On a successful save, a target takes half as much damage.")

def masteryofwoodandearth(npc):
    npc.bonusactions.append("***Psychic Focus: Mastery of Water.*** While focused on this discipline, you have a +1 bonus to AC. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Animate Weapon (1–7 psi).*** Your mind seizes control of a one-handed melee weapon you’re holding. The weapon flies toward one creature you can see within 30 feet of you and makes a one-handed melee weapon attack against it, using your discipline attack modifier for the attack and damage rolls. On a hit, the weapon deals its normal damage, plus an extra 1d10 force damage per psi point spent on this ability. The weapon returns to your grasp after it attacks.")

    npc.actions.append("***Warp Weapon (2 psi).*** Choose one nonmagical weapon held by one creature you can see within 60 feet of you. That creature must succeed on a Strength saving throw, or the chosen weapon can’t be used to attack until the end of your next turn.")

    npc.actions.append("***Warp Armor (3 psi).*** Choose a nonmagical suit of armor worn by one creature you can see within 60 feet of you. That creature must succeed on a Constitution saving throw, or the creature’s AC becomes 10 + its Dexterity modifier until the end of your next turn.")

    npc.actions.append("***Wall of Wood (3 psi; concentration, 1 hr.).*** You create a wall of wood at least one portion of which must be within 60 feet of you. The wall is 60 feet long, 15 feet high, and 1 foot thick. The wall lasts until your concentration ends. Each 5-foot wide section of the wall has AC 12 and 100 hit points. Breaking one section creates a 5-foot by 5-foot hole in it, but the wall otherwise remains intact.")

    npc.bonusactions.append("***Armored Form (6 psi; concentration, 1 min.).*** You gain resistance to bludgeoning, piercing, and slashing damage, which lasts until your concentration ends.")

    npc.actions.append("***Animate Earth (7 psi; concentration, 1 hr.).*** You cause an earth elemental to appear in an unoccupied space you can see within 120 feet of you. The elemental lasts until your concentration ends, and it obeys your verbal commands. In combat, roll for its initiative, and choose its behavior during its turns. When this effect ends, the elemental disappears.")

wujendisciplines = {
    'Mastery of Air': masteryofair,
    'Mastery of Fire': masteryoffire,
    'Mastery of Force': masteryofforce,
    'Mastery of Ice': masteryofice,
    'Mastery of Light and Darkness': masteryoflightanddarkness,
    'Mastery of Water': masteryofwater,
    'Mastery of Weather': masteryofweather,
    'Mastery of Wood and Earth': masteryofwoodandearth
}
for ad in wujendisciplines:
    allclasses['Mystic'].disciplines[ad] = wujendisciplines[ad]
```