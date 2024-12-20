# Arcane Tradition: Pyromancy
The pyromancer is the elemental master of fire. While many mages can conjure fire for blasts of devastating energy, the pyromancer understands the primal nature of fire, heat, and the deeper secrets of the multiverse--that elemental flame is one of the fundamental building blocks of all creation. And while it's most basic nature can be turned to destruction, the subtle nuances of its uses go far beyond that. Pyromancers embrace all aspects of heat, fire, and flame knowing that all creatures are connected to the elements, and flames can cleanse as well as consume.

```
name = 'Pyromancy'
description = "***Arcane Tradition: Pyromancy.*** The pyromancer is the elemental master of fire. While many mages can conjure fire for blasts of devastating energy, the pyromancer understands the primal nature of fire, heat, and the deeper secrets of the multiverse--that elemental flame is one of the fundamental building blocks of all creation. And while it's most basic nature can be turned to destruction, the subtle nuances of its uses go far beyond that. Pyromancers embrace all aspects of heat, fire, and flame knowing that all creatures are connected to the elements, and flames can cleanse as well as consume."
```

## Fire Savant
*2nd-level Pyromancy feature*

The gold and time you must spend to copy a fire-based spell into your spellbook is halved. A fire-based spell is defined by having fire, flame, or heat in its name.

```
def level2(npc):
    npc.traits.append("***Fire Savant.*** The gold and time you must spend to copy a fire-based spell into your spellbook is halved. A fire-based spell is defined by having 'fire', 'flame', or 'heat' in its name.")
```

## Fireshaper
*2nd-level Pyromancy feature*

As a bonus action, you are able to exert influence on any non-magical flame that you can see within 60 feet and that is no larger than a 5-foot cube. You affect it in one of the following ways:
* You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location.
* You instantaneously extinguish the flames. 
* You can double or halve the area of bright light and dim light cast by the flame, change its color, or both. These changes last for 1 hour.
* You cause simple shapes--such as the vague form of a creature, an inanimate object, or a location--to appear and animate within the flames, as you like. These shapes last for 1 hour.

This ability replicates the effects of the [control flames](../../Magic/Spells/control-flames.md) cantrip, but is not considered a spell.

```
    npc.bonusactions.append("***Fireshaper.*** you are able to exert influence on any non-magical flame that you can see within 60 feet and that is no larger than a 5-foot cube. You affect it in one of the following ways: You instantaneously expand the flame 5 feet in one direction, provided that wood or other fuel is present in the new location; You instantaneously extinguish the flames; You can double or halve the area of bright light and dim light cast by the flame, change its color, or both. These changes last for 1 hour; You cause simple shapes--such as the vague form of a creature, an inanimate object, or a location--to appear and animate within the flames, as you like.")
```

## Heart of Fire
*6th-level Pyromancy feature*

You take no damage from natural or mundane sources of flame or heat and you gain immunity to environmental, heat-based exhaustion. You also have advantage on saving throws against fire-based spells and effects.

```
def level6(npc):
    npc.traits.append("***Heart of Fire.*** You take no damage from natural or mundane sources of flame or heat and you gain immunity to environmental, heat-based exhaustion. You also have advantage on saving throws against fire-based spells and effects.")
```

## Heat Channeling
*10th-level Pyromancy feature*

As a bonus action, you can siphon fire and heat from natural or magical sources to fuel your abilities. By drawing the residual heat from your environment, dropping the temperature noticeably for a moment, and extinguishing any natural fl ames within 10 feet of you, the power of your fire-based spells is magnified, allowing you to add your wizard level to the damage of all your fire or heat-based spells. If the spell affects multiple targets, select one target to take the additional damage. You regain the use of this ability after a short or long rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Heat Channeling.*** You siphon fire and heat from natural or magical sources to fuel your abilities. By drawing the residual heat from your environment, dropping the temperature noticeably for a moment, and extinguishing any natural flames within 10 feet of you, the power of your fire-based spells is magnified, allowing you to add {npc.levels('Wizard')} to the damage of all your fire or heat-based spells. If the spell affects multiple targets, select one target to take the additional damage.") )
```

## Piercing Flames
*14th-level Pyromancy feature*

Fire and flames you generate are so hot they pierce most protections. Your spells and abilities ignore resistance to fire damage, and creatures immune to fire damage take fire damage equal to your Intelligence modifier (minimum of 1) instead.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Piercing Flames.*** Fire and flames you generate are so hot they pierce most protections. Your spells and abilities ignore resistance to fire damage, and creatures immune to fire damage take {npc.INTbonus()} fire damage instead.") )
```

---

# Pyromancy Spells

## 1st-level
* [pure flame](../../Magic/Spells/pure-flame.md)

## 4th-level
* [fire trap](../../Magic/Spells/fire-trap.md)

## 5th-level
* [curse of combustion](../../Magic/Spells/curse-of-combustion.md)

## 6th-level
* [greater fire trap](../../Magic/Spells/greater-fire-trap.md)

## 9th-level
* [pyroclastic cataclysm](../../Magic/Spells/pyroclastic-cataclysm.md)

