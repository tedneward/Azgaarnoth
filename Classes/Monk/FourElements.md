# Monastic Tradition: Way of the Four Elements
You follow a monastic tradition that teaches you to harness the elements. When you focus your ki, you can align yourself with the forces of creation and bend the four elements to your will, using them as an extension of your body. Some members of this tradition dedicate themselves to a single element, but others weave the elements together.

Many monks of this tradition tattoo their bodies with representations of their ki powers, commonly imagined as coiling dragons, but also as phoenixes, fish, plants, mountains, and cresting waves.

```
name = 'Way of the Four Elements'
description = "***Monastic Tradition: Way of the Four Elements.*** You follow a monastic tradition that teaches you to harness the elements. When you focus your ki, you can align yourself with the forces of creation and bend the four elements to your will, using them as an extension of your body. Some members of this tradition dedicate themselves to a single element, but others weave the elements together."
```

## Disciple of the Elements
*3rd level Way of the Four Elements feature*

You learn magical disciplines that harness the power of the four elements. A discipline requires you to spend ki points each time you use it.

You know the Elemental Attunement discipline and one other elemental discipline of your choice. You learn one additional elemental discipline of your choice at 6th, 11th, and 17th level.

Whenever you learn a new elemental discipline, you can also replace one elemental discipline that you already know with a different discipline.

***Casting Elemental Spells.*** Some elemental disciplines allow you to cast spells. See chapter 10 for the general rules of spellcasting. To cast one of these spells, you use its casting time and other rules, but you don't need to provide material components for it.

Once you reach 5th level in this class, you can spend additional ki points to increase the level of an elemental discipline spell that you cast, provided that the spell has an enhanced effect at a higher level, as Burning Hands does. The spell's level increases by 1 for each additional ki point you spend. For example, if you are a 5th-level monk and use Sweeping Cinder Strike to cast Burning Hands, you can spend 3 ki points to cast it as a 2nd-level spell (the discipline's base cost of 2 ki points plus 1).

```
def level5(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Ki: Fueling Elemental Disciplines.*** You can spend up to the (total) maximum of {3 if npc.levels('Monk') < 8 else 4 if npc.levels('Monk') < 12 else 5 if npc.levels('Monk') < 16 else 6} ki points to increase the level of an elemental discipline spell that you cast, provided that the spell has an enhanced effect at a higher level. The spell's level increases by 1 for each additional ki point you spend.") )
```

The maximum number of ki points you can spend to cast a spell in this way (including its base ki point cost and any additional ki points you spend to increase its level) is determined by your monk level, as shown in the Spells and Ki Points table.

**Spells and Ki Points**

Monk Levels|Maximum Ki Points for a Spell
-----------|-----------------------------
5th-8th    |3
9th-12th	 |4
13th-16th	 |5
17th-20th	 |6

## Elemental Disciplines

**Breath of Winter** (*Prerequisite: 17th Level*) You can spend 6 ki points to cast [Cone of Cold](http://azgaarnoth.tedneward.com/magic/spells/cone-of-cold).

```
def breathofwinter(npc):
    npc.actions.append(f"***Ki: Breath of Winter.*** You can spend 6 ki points to cast {spelllinkify('cone of cold')}.")
```

**Clench of the North Wind.** (*Prerequisite: 6th Level*) You can spend 3 ki points to cast [Hold Person](http://azgaarnoth.tedneward.com/magic/spells/hold-person).

```
def clenchofthenorthwind(npc):
    npc.actions.append(f"***Ki: Clench of the North Wind.*** You can spend 3 ki points to cast {spelllinkify('hold person')}.")
```

**Elemental Attunement.** You can use your action to briefly control elemental forces within 30 feet of you, causing one of the following effects of your choice:

* Create a harmless, instantaneous sensory effect related to air, earth, fire, or water such as a shower of sparks, a puff of wind, a spray of light mist, or a gentle rumbling of stone.
* Instantaneously light or snuff out a candle, a torch, or a small campfire.
* Chill or warm up to 1 pound of nonliving material for up to 1 hour.
* Cause earth, fire, water, or mist that can fit within a 1-foot cube to shape itself into a crude form you designate for 1 minute.

```
def elementalattunement(npc):
    npc.actions.append(f"***Ki: Elemental Attunement.*** You can briefly control elemental forces within 30 feet of you, causing one of the following effects of your choice: Create a harmless, instantaneous sensory effect related to air, earth, fire, or water such as a shower of sparks, a puff of wind, a spray of light mist, or a gentle rumbling of stone; Instantaneously light or snuff out a candle, a torch, or a small campfire; Chill or warm up to 1 pound of nonliving material for up to 1 hour; Cause earth, fire, water, or mist that can fit within a 1-foot cube to shape itself into a crude form you designate for 1 minute.")
```

**Eternal Mountain Defense.** (*Prerequisite: 17th Level*) You can spend 5 ki points to cast [Stoneskin](http://azgaarnoth.tedneward.com/magic/spells/stoneskin), targeting yourself.

```
def eternalmountaindefense(npc):
    npc.actions.append(f"***Ki: Eternal Mountain Defense.*** You can spend 5 ki points to cast {spelllinkify('stoneskin')}, targeting yourself.")
```

**Fangs of the Fire Snake.** When you use the Attack action on your turn, you can spend 1 ki point to cause tendrils of flame to stretch out from your fists and feet. Your reach with your unarmed strikes increases by 10 feet for that action, as well as the rest of the turn. A hit with such an attack deals fire damage instead of bludgeoning damage, and if you spend 1 ki point when the attack hits, it also deals an extra 1d10 fire damage.

```
def fangsofthefiresnake(npc):
    npc.actions.append("***Ki: Fangs of the Fire Snake.*** When you use the Attack action on your turn, you can spend 1 ki point to cause tendrils of flame to stretch out from your fists and feet. Your reach with your unarmed strikes increases by 10 feet for that action, as well as the rest of the turn. A hit with such an attack deals fire damage instead of bludgeoning damage, and if you spend 1 ki point when the attack hits, it also deals an extra 1d10 fire damage.")
```

**Fist of Four Thunders.** You can spend 2 ki points to cast [Thunderwave](http://azgaarnoth.tedneward.com/magic/spells/thunderwave).

```
def fistoffourthunders(npc):
    npc.actions.append(f"***Ki: Fist of Four Thunders.*** You can spend 2 ki points to cast {spelllinkify('thunderwave')}.")
```

**Fist of Unbroken Air.** You can create a blast of compressed air that strikes like a mighty fist. As an action, you can spend 2 ki points and choose a creature within 30 feet of you. That creature must make a Strength saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can push the creature up to 20 feet away from you and knock it prone. On a successful save, the creature takes half as much damage, and you don't push it or knock it prone.

```
def fistofunbrokenair(npc):
    npc.actions.append("***Ki: Fist of Unbroken Air.*** You can spend 2 ki points and choose a creature within 30 feet of you. That creature must make a Strength saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can push the creature up to 20 feet away from you and knock it prone. On a successful save, the creature takes half as much damage, and you don't push it or knock it prone.")
```

**Flames of the Phoenix.** (*Prerequisite: 11th Level*) You can spend 4 ki points to cast [Fireball](http://azgaarnoth.tedneward.com/magic/spells/fireball).

```
def flamesofthephoenix(npc):
    npc.actions.append(f"***Ki: Flames of the Phoenix.*** You can spend 4 ki points to cast {spelllinkify('fireball')}.")
```

**Gong of the Summit.** (*Prerequisite: 6th Level*) You can spend 3 ki points to cast [Shatter](http://azgaarnoth.tedneward.com/magic/spells/shatter).

```
def gongofthesummit(npc):
    npc.actions.append(f"***Ki: Gong of the Summit.*** You can spend 3 ki points to cast {spelllinkify('shatter')}.")
```

**Mist Stance.** (*Prerequisite: 11th Level*) You can spend 4 ki points to cast [Gaseous Form](http://azgaarnoth.tedneward.com/magic/spells/gaseous-form), targeting yourself.

```
def miststance(npc):
    npc.actions.append(f"***Ki: Mist Stance.*** You can spend 4 ki points to cast {spelllinkify('gaseous form')}, targeting yourself.")
```

**Ride the Wind.** (*Prerequisite: 11th Level*) You can spend 4 ki points to cast [Fly](http://azgaarnoth.tedneward.com/magic/spells/fly), targeting yourself.

```
def ridethewind(npc):
    npc.actions.append(f"***Ki: Ride the Wind.*** You can spend 4 ki points to cast {spelllinkify('fly')}, targeting yourself.")
```

**River of Hungry Flame.** (*Prerequisite: 17th Level*) You can spend 5 ki points to cast [Wall of Fire](http://azgaarnoth.tedneward.com/magic/spells/wall-of-fire).

```
def riverofhungryflame(npc):
    npc.actions.append(f"***Ki: River of Hungry Flame.*** You can spend 5 ki points to cast {spelllinkify('wall of fire')}.")
```

**Rush of the Gale Spirits.** You can spend 2 ki points to cast [Gust of Wind](http://azgaarnoth.tedneward.com/magic/spells/gust-of-wind).

```
def rushofthegalespirits(npc):
    npc.actions.append(f"***Ki: Rush of the Gale Spirits.*** You can spend 2 ki points to cast {spelllinkify('gust of wind')}.")
```

**Shape the Flowing River.** As an action, you can spend 1 ki point to choose an area of ice or water no larger than 30 feet on a side within 120 feet of you. You can change water to ice within the area and vice versa, and you can reshape ice in the area in any manner you choose. You can raise or lower the ice's elevation, create or fill in a trench, erect or flatten a wall, or form a pillar. The extent of any such changes can't exceed half the area's largest dimension. For example, if you affect a 30-foot square, you can create a pillar up to 15 feet high, raise or lower the square's elevation by up to 15 feet, dig a trench up to 15 feet deep, and so on. You can't shape the ice to trap or injure a creature in the area.

```
def shapetheflowingriver(npc):
    npc.actions.append("***Ki: Shape the Flowing River.*** you can spend 1 ki point to choose an area of ice or water no larger than 30 feet on a side within 120 feet of you. You can change water to ice within the area and vice versa, and you can reshape ice in the area in any manner you choose. You can raise or lower the ice's elevation, create or fill in a trench, erect or flatten a wall, or form a pillar. The extent of any such changes can't exceed half the area's largest dimension. For example, if you affect a 30-foot square, you can create a pillar up to 15 feet high, raise or lower the square's elevation by up to 15 feet, dig a trench up to 15 feet deep, and so on. You can't shape the ice to trap or injure a creature in the area.")
```

**Sweeping Cinder Strike.** You can spend 2 ki points to cast [Burning Hands](http://azgaarnoth.tedneward.com/magic/spells/burning-hands).

```
def sweepingcinderstrike(npc):
    npc.actions.append(f"***Ki: Sweeping Cinder Strike.*** You can spend 2 ki points to cast {spelllinkify('burning hands')}.")
```

**Water Whip.** You can spend 2 ki points as an action to create a whip of water that shoves and pulls a creature to unbalance it. A creature that you can see that is within 30 feet of you must make a Dexterity saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can either knock it prone or pull it up to 25 feet closer to you. On a successful save, the creature takes half as much damage, and you don't pull it or knock it prone.

```
def waterwhip(npc):
    npc.actions.append("***Ki: Water Whip.*** You can spend 2 ki points as an action to create a whip of water that shoves and pulls a creature to unbalance it. A creature that you can see that is within 30 feet of you must make a Dexterity saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can either knock it prone or pull it up to 25 feet closer to you. On a successful save, the creature takes half as much damage, and you don't pull it or knock it prone.")
```

**Wave of Rolling Earth.** (*Prerequisite: 17th Level*) You can spend 6 ki points to cast [Wall of Stone](http://azgaarnoth.tedneward.com/magic/spells/wall-of-stone).

```
def waveofrollingearth(npc):
    npc.actions.append(f"***Ki: Wave of Rolling Earth.*** You can spend 6 ki points to cast {spelllinkify('wall of stone')}.")
```

```
def level3(npc):
    npc.elementaldisciplines = ['Elemental Attunement']
    elementalattunement(npc)
    choosediscipline(npc)

def level6(npc):
    choosediscipline(npc)

def level11(npc):
    choosediscipline(npc)

def level17(npc):
    choosediscipline(npc)

disciplines = {
    'Breath of Winter': [17, breathofwinter],
    'Clench of the North Wind': [6, clenchofthenorthwind],
    'Elemental Attunement': [0, elementalattunement],
    'Eternal Mountain Defense': [17, eternalmountaindefense],
    'Fangs of the Fire Snake': [0, fangsofthefiresnake],
    'Fist of Unbroken Air': [0, fistofunbrokenair],
    'Flames of the Phoenix': [11, flamesofthephoenix],
    'Gong of the Summit': [6, gongofthesummit],
    'Mist Stance': [11, miststance],
    'Ride the Wind': [11, ridethewind],
    'River of Hungry Flame': [17, riverofhungryflame],
    'Rush of the Gale Spirits': [0, rushofthegalespirits],
    'Shape the Flowing River': [0, shapetheflowingriver],
    'Sweeping Cinder Strike': [0, sweepingcinderstrike],
    'Water Whip': [0, waterwhip]
}
def choosediscipline(npc):
    availdisciplines = {}
    for (dname, dlist) in disciplines.items():
        if dname not in npc.elementaldisciplines:
            if npc.levels('Monk') >= dlist[0]:
                availdisciplines[dname] = dlist[1]
    (chosenname, chosenfn) = choose("Choose an elemental discipline: ", availdisciplines)
    npc.elementaldisciplines.append(chosenname)
    chosenfn(npc)
```
