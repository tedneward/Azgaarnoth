# Mystic Order: Order of the Soul Knife
The Order of the Soul Knife sacrifices the breadth of knowledge other mystics gain to focus on a specific psionic technique. These mystics learn to manifest a deadly weapon of pure psychic energy that they can use to cleave through foes.

Soul knives vary widely in their approach to this path. Some follow it out of a desire to achieve martial perfection. Others are ruthless assassins who seek to become the perfect killer.

```
name = 'Order of the Soul Knife'
description = "***Mystic Order: Order of the Soul Knife.*** The Order of the Soul Knife sacrifices the breadth of knowledge other mystics gain to focus on a specific psionic technique. These mystics learn to manifest a deadly weapon of pure psychic energy that they can use to cleave through foes."
```

## Martial Training
*1st-level Order of the Soul Knife feature*

You gain proficiency with medium armor and martial weapons.

```
def level1(npc):
    for arm in armor['medium']:
        npc.proficiencies.append(arm)
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
```

## Soul Knife
*1st-level Order of the Soul Knife feature*

You gain the ability to manifest a blade of psychic energy. As a bonus action, you create scintillating knives of energy that project from both of your fists. You can't hold anything in your hands while manifesting these blades. You can dismiss them as a bonus action.

For you, a soul knife is a martial melee weapon with the light and finesse properties. It deals 1d8 psychic damage on a hit.

As a bonus action, you can prepare to use the blades to parry; you gain a +2 bonus to AC until the start of your next turn or until you are incapacitated.

```
    npc.bonusactions.append("***Soul Knife.*** You create scintillating knives of energy that project from both of your fists. You can't hold anything in your hands while manifesting these blades. You can dismiss them as a bonus action.")
    npc.defer(lambda npc: npc.actions.append(f"***Soul Knife.*** *Melee Weapon Attack:* +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft, one target. Hit: 1d8 psychic damage. This is a martial melee weapon with the light and finesse properties.") )
    npc.bonusactions.append("***Soul Knife Parry.*** You gain a +2 bonus to AC until the start of your next turn or until you are incapacitated.")
```

## Hone the Blade
*3rd-level Order of the Soul Knife feature*

As a bonus action, you can spend psi points to augment your soul knife's attack rolls and damage. You gain a bonus to attack and damage rolls with your soul knives depending on the number of psi points spent, as shown on the table below. This bonus lasts for 10 minutes.

Psi Points|Attack and Damage Bonus
----------|-------------------
2|+1
5|+2
7|+4

```
def level3(npc):
    npc.bonusactions.append("***Hone the Blade.*** You augment your Soul Knife attack rolls and damage using psi points (2 psi points = +1 attack and damage bonus; 5 psi = +2, 7 psi = +4). This bonus lasts for 10 minutes.")
```

## Consumptive Knife
*6th-level Order of the Soul Knife feature*

Whenever you slay an enemy creature with a soul knife attack, you immediately regain 2 psi points.

```
def level6(npc):
    npc.traits.append("***Consumptive Knife.*** Whenever you slay an enemy creature with a soul knife attack, you immediately regain 2 psi points.")
```

## Phantom Knife
*14th-level Order of the Soul Knife feature*

You can make an attack that phases through most defenses. As an action, you can make one attack with your soul knife. Treat the target's AC as 10 against this attack, regardless of the target's actual AC.

```
def level14(npc):
    npc.actions.append("***Phantom Knife.*** You can make one attack with your soul knife that phases through most defenses. Treat the target's AC as 10 against this attack, regardless of the target's actual AC.")
```
