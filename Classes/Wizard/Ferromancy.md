# Arcane Tradition: Ferromancy
Ferromancers are specialists in metal and magnetism; learning to create or manipulate metal objects, enhance or destroy them, or use magnetic forces to attract, repel or statically charge nearby metal. Ferromancers favor metal weapons and armor, their unique specialty enhanced, not hindered, by bulky raiment and arms.

```
name = 'Ferromancy'
description = "***Arcane Tradition: Ferromancy.*** Ferromancers are specialists in metal and magnetism; learning to create or manipulate metal objects, enhance or destroy them, or use magnetic forces to attract, repel or statically charge nearby metal. Ferromancers favor metal weapons and armor, their unique specialty enhanced, not hindered, by bulky raiment and arms."
```

## Bonus Proficiencies
*2nd-level Ferromancy feature*

You are proficient with all metal weapons and metal armor. You also learn the [heat metal](../../Magic/Spells/heat-metal.md) spell, adding it to your spellbook, but you cannot cast it until you have access to 2nd level spell slots.

```
def level2(npc):
    wpns = weapons['simple-melee'] | weapons['martial-melee'] | weapons['martial-ranged']
    for w in ['Club', 'Greatclub', 'Javelin', 'Quarterstaff', 'Whip', 'Blowgun', 'Longbow', 'Net']:
        del wpns[w]
    for w in wpns:
        npc.proficiencies.append(w)

    npc.spellcasting['Wizard'].spellbook.append('heat metal')
```

## Magnetic Ward
*2nd-level Ferromancy feature*

As a reaction you can generate a magnetic ward around yourself that interferes with incoming weapon attacks, deflecting and reducing their velocity. For 1 minute, you reduce all damage that you take from weapon attacks by an amount equal to your Intelligence modifier (minimum of 1). You do not regain hit points if the damage is reduced to below zero. You regain the use of this ability after completing a long rest. At 10th level, you regain the use of this ability after finishing a short or long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Magnetic Ward (Recharges on{' short or' if npc.levels('Wizard') >= 10 else ''} long rest).*** For 1 minute, you reduce all damage that you take from weapon attacks by {npc.INTbonus()}. You do not regain hit points if the damage is reduced to below zero.") )
```

## Static
*6th-level Ferromancy feature*

Whenever a creature fails a saving throw against one of your spells, they are surrounded by a residual static charge for a number of turns equal to your Intelligence modifier (minimum of 1). If the creature ends its turn within 5 feet of one or more creatures affected by this static charge, each creature takes 1d6 lightning damage.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append("***Static.*** Whenever a creature fails a saving throw against one of your spells, they are surrounded by a residual static charge for {npc.INTbonus()} turns. If the creature surrounded by the static charge ends its turn within 5 feet of one or more creatures also affected by this static charge, each creature takes 1d6 lightning damage.") )
```

## Breach Armor
*10th-level Ferromancy feature*

Your weapon and spell attacks against creatures constructed of metal, or creatures wearing armor that is primarily made of metal, are made with advantage as you are able to subtly manipulate their defenses to open weaknesses.

```
def level10(npc):
    npc.traits.append("***Breach Armor.*** Your weapon and spell attacks against creatures constructed of metal, or creatures wearing armor that is primarily made of metal, are made with advantage.")
```

## Magnetic Field
*14th-level Ferromancy feature*

As an action, you can evoke an electrically charged magnetic field in a 20-foot-radius around yourself that moves with you. The field lasts for 1 minute. When a creature enters the magnetic field for the first time on a turn or starts its turn there, if it is wearing metal armor, wielding metal weapons, or carrying more than 30lbs of metal, the creature takes 1d6 lightning damage and treats the area as difficult terrain. If the creature is also affected by your Static ability, the damage increases to 2d6 lightning damage.

You can use this ability once per long rest.

```
def level14(npc):
    npc.actions.append("***Magnetic Field.*** You evoke an electrically charged magnetic field in a 20-foot-radius around yourself that moves with you. The field lasts for 1 minute. When a creature enters the magnetic field for the first time on a turn or starts its turn there, if it is wearing metal armor, wielding metal weapons, or carrying more than 30lbs of metal, the creature takes 1d6 lightning damage and treats the area as difficult terrain. If the creature is also affected by your Static ability, the damage increases to 2d6 lightning damage.")
```

---

# Ferromancy Spells

## Cantrips
* [flechette](../../Magic/Spells/flechette.md)

## 2nd-level
* [chaotic polarity aura](../../Magic/Spells/chaotic-polarity-aura.md)

## 3rd-level
* [flechette spray](../../Magic/Spells/flechette-spray.md)
* [rusting grasp](../../Magic/Spells/rusting-grasp.md)

## 4th-level
* [rusting burst](../../Magic/Spells/rusting-burst.md)

## 5th-level
* [flechette storm](../../Magic/Spells/flechette-storm.md)

## 6th-level
* [rust field](../../Magic/Spells/rust-field.md)

