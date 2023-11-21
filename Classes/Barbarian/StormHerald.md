# Primal Path: Path of the Storm Herald
Typical barbarians harbor a fury that dwells within. Their rage grants them superior strength, durability, and speed. Barbarians who follow the Path of the Storm Herald learn instead to transform their rage into a mantle of primal magic that swirls around them. When in a fury, a barbarian of this path taps into nature to create powerful, magical effects.

Storm heralds are typically elite champions who train alongside druids, rangers, and others sworn to protect the natural realm. Other storm heralds hone their craft in elite lodges founded in regions wracked by storms, in the frozen reaches at the world's end, or deep in the hottest deserts. These barbarians can be found in quite a few places, most notably in the [Ravenlands](../../Geography/Ravenlands.md), the [United Hordes](../../Nations/Tragekia.md), or [North Bedia](../../Nations/Bedia.md).

```
name = 'Storm Herald'
description = "***Primal Path: Path of the Storm Herald.*** Typical barbarians harbor a fury that dwells within. Their rage grants them superior strength, durability, and speed. Barbarians who follow the Path of the Storm Herald learn instead to transform their rage into a mantle of primal magic that swirls around them. When in a fury, a barbarian of this path taps into nature to create powerful, magical effects."
```

## Storm Aura
*3rd-level Path of the Storm Herald feature*

You emanate a stormy, magical aura while you rage. The aura extends 10 feet from you in every direction, but not through total cover.

Your aura has an effect that activates when you enter your rage, and you can activate the effect again on each of your turns as a bonus action. Choose desert, sea, or tundra. Your aura's effect depends on that chosen environment, as detailed below. You can change your environment choice whenever you gain a level in this class.

If your aura's effects require a saving throw, the DC equals 8 + your proficiency bonus + your Constitution modifier.

* **Desert**. When this effect is activated, all other creatures in your aura take 2 fire damage each. The damage increases when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level.

* **Sea**. When this effect is activated, you can choose one other creature you can see in your aura. The target must make a Dexterity saving throw. The target takes 1d6 lightning damage on a failed save, or half as much damage on a successful one. The damage increases when you reach certain levels in this class, increasing to 2d6 at 10th level, 3d6 at 15th level, and 4d6 at 20th level.

* **Tundra**. When this effect is activated, each creature of your choice in your aura gains 2 temporary hit points, as icy spirits inure it to suffering. The temporary hit points increase when you reach certain levels in this class, increasing to 3 at 5th level, 4 at 10th level, 5 at 15th level, and 6 at 20th level.

```
def level3(npc):
    npc.stormchoice = choose("Choose a storm aura: ", ['Desert', 'Sea', 'Tundra'])
    if npc.stormchoice == 'Desert':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Storm Aura.*** When you rage, you emanate a stormy, magical aura reminscient of the sandstorms of the desert that extends 10 feet from you in every direction, but not through total cover. All other creatures in your aura take {2 if npc.levels('Barbarian') < 5 else 3 if npc.levels('Barbarian') < 10 else 4 if npc.levels('Barbarian') < 15 else 5 if npc.levels('Barbarian') < 20 else 6} fire damage each.{'' if npc.levels('Barbarian') < 10 else ' Each creature of your choice has resistance to fire while that creature is within your Storm Aura.'}") )
    elif npc.stormchoice == 'Sea':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Storm Aura.*** When you rage, you emanate a stormy, magical aura reminscient of a fierce storm at sea that extends 10 feet from you in every direction, but not through total cover. Choose one other creature you can see in your aura. The target must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}). The target takes {'1d6' if npc.levels('Barbarian') < 10 else '2d6' if npc.levels('Barbarian') < 15 else '3d6' if npc.levels('Barbarian') < 20 else '4d6'} lightning damage on a failed save, or half as much damage on a successful one.{'' if npc.levels('Barbarian') < 10 else ' Each creature of your choice has resistance to lightning while that creature is within your Storm Aura.'}") )
    elif npc.stormchoice == 'Tundra':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Storm Aura.*** When you rage, you emanate a stormy, magical aura reminscient of the icy winds of the tundra that extends 10 feet from you in every direction, but not through total cover. Each creature of your choice in your aura gains {2 if npc.levels('Barbarian') < 5 else 3 if npc.levels('Barbarian') < 10 else 4 if npc.levels('Barbarian') < 15 else 5 if npc.levels('Barbarian') < 20 else 6} temporary hit points.{'' if npc.levels('Barbarian') < 10 else ' Each creature of your choice has resistance to cold while that creature is within your Storm Aura.'}") )
```

## Storm Soul
*6th-level Path of the Storm Herald feature*

At 6th level, the storm grants you benefits even when your aura isn't active. The benefits are based on the environment you chose for your Storm Aura.

* **Desert**. You gain resistance to fire damage, and you don't suffer the effects of extreme heat, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch a flammable object that isn't being worn or carried by anyone else and set it on fire.

* **Sea**. You gain resistance to lightning damage, and you can breathe underwater. You also gain a swimming speed of 30 feet.

* **Tundra**. You gain resistance to cold damage, and you don't suffer the effects of extreme cold, as described in the Dungeon Master's Guide. Moreover, as an action, you can touch water and turn a 5-foot cube of it into ice, which melts after 1 minute. This action fails if a creature is in the cube.

```
def level6(npc):
    if npc.stormchoice == 'Desert':
        npc.damageresistances.append('fire')
        npc.traits.append("***Storm Soul.*** You don't suffer the effects of extreme heat.")
        npc.actions.append("***Storm Touched.*** You touch a flammable object that isn't being worn or carried by anyone else and set it on fire.")
    elif npc.stormchoice == 'Sea':
        npc.damageresistances.append('lightning')
        npc.speed['swimming'] = 30
        npc.traits.append("***Amphibious.*** You can breathe underwater.")
    elif npc.stormchoice == 'Tundra':
        npc.damageresistances.append('cold')
        npc.traits.append("***Storm Soul.*** You don't suffer the effects of extreme cold.")
        npc.actions.append("***Storm Touched.*** You touch water and turn a 5-foot cube of it into ice, which melts after 1 minute. This action fails if a creature is in the cube.")
```

## Shielding Storm
*10th-level Path of the Storm Herald feature*

You learn to use your mastery of the storm to protect others. Each creature of your choice has the damage resistance you gained from the Storm Soul feature while the creature is in your Storm Aura.

## Raging Storm
*14th-level Path of the Storm Herald feature*

The power of the storm you channel grows mightier, lashing out at your foes. The effect is based on the environment you chose for your Storm Aura.

* **Desert**. Immediately after a creature in your aura hits you with an attack, you can use your reaction to force that creature to make a Dexterity saving throw. On a failed save, the creature takes fire damage equal to your Barbarian level.

* **Sea**. When you hit a creature in your aura with an attack, you can use your reaction to force that creature to make a Strength saving throw. On a failed save, the creature is knocked prone, as if struck by a wave.

* **Tundra**. Whenever the effect of your Storm Aura is activated, you can choose one creature you can see in the aura. That creature must succeed on a Strength saving throw, or its speed is reduced to 0 until the start of your next turn, as magical frost covers it.

```
def level14(npc):
    if npc.stormchoice == 'Desert':
        npc.defer(lambda npc: npc.reactions.append(f"***Raging Storm.*** Immediately after a creature in your aura hits you with an attack, you force that creature to make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}). On a failed save, the creature takes {npc.levels('Barbarian')} fire damage.") )
    elif npc.stormchoice == 'Sea':
        npc.defer(lambda npc: npc.reactions.append(f"***Raging Storm.*** When you hit a creature in your aura with an attack, you force that creature to make a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}). On a failed save, the creature is knocked prone, as if struck by a wave.") )
    elif npc.stormchoice == 'Tundra':
        npc.defer(lambda npc: npc.reactions.append(f"***Raging Storm.*** Whenever the effect of your Storm Aura is activated, you can choose one creature you can see in the aura. That creature must make a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}), or its speed is reduced to 0 until the start of your next turn, as magical frost covers it and impairs its movements.") )
```
