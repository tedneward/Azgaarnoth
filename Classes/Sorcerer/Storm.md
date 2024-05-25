# Sorcerous Origin: Storm
Storm sorcerers channel the power of the thunderstorm: The gale-force winds, the crashing of thunder, the pelting rain. This connection to the storm echoes radiates out of them, giving them some control over wind and weather in their immediate area. Their magic embraces the air and storm, and their connection allows them to communicate with the creatures born of the power of the storm.

Your innate magic comes from the power of elemental air. Perhaps you were born during a howling gale so powerful that folk still tell stories of it. Your lineage might include the influence of potent air creatures such as vaati or djinni. Whatever the case, the magic of the storm permeates your soul. Storm sorcerers are invaluable members of a ship's crew. Their abilities also prove useful in repelling attacks by sahuagin, pirates, and other waterborne threats.

```
name = 'Storm'
description = "***Sorcerous Origin: Storm.*** Storm sorcerers channel the power of the thunderstorm: The gale-force winds, the crashing of thunder, the pelting rain. This connection to the storm echoes radiates out of them, giving them some control over wind and weather in their immediate area. Their magic embraces the air and storm, and their connection allows them to communicate with the creatures born of the power of the storm."
```

## Stormborn
The arcane magic you command is infused with elemental air. You can speak, read, and write Primordial. In addition, you gain the following spells at the listed sorcerer level. These spells do not count against the number of sorcerer spells you know.

**Storm Sorcerer Bonus Spells**
Sorcerer Level | Spells
-------------- | ------
1st | fog cloud, thunderwave
3rd | gust of wind, levitate
5th | call lightning, sleet storm
7th | conjure minor elementals (smoke mephits, steam mephits, ice mephits, or dust mephits only),  ice storm
9th | conjure elemental (air elementals only)

```
bonusspells = {
    1: ['fog cloud', 'thunderwave'],
    3: ['gust of wind', 'levitate'],
    5: ['call lightning', 'sleet storm'],
    7: ['conjure minor elementals', 'ice storm'],
    9: ['conjure elemental']
}
```

## Tempestuous Magic
*1st-level Storm feature*

At 1st level, you are attuned to elemental air magic. Whenever you cast a spell other than a cantrip during your turn, whirling gusts of elemental air surround you. You can use a bonus action to fly 10 feet without provoking opportunity attacks.

```
def level1(npc):
    npc.bonusactions.append("***Tempestuous Magic.*** Whenever you cast a spell other than a cantrip during your turn, you can fly 10 feet without provoking opportunity attacks.")
```

## Heart of the Storm
*6th-level Storm feature*

At 6th level, you gain resistance to lightning and thunder damage. Whenever you cast a spell other than a cantrip that deals lightning or thunder damage, a stormy aura surrounds you. In addition to the spell's effects, creatures of your choice within 10 feet of you take lightning or thunder damage (choose each time this ability activates) equal to half your sorcerer level.

```
def level6(npc):
    npc.damageresistances.append('lightning')
    npc.damageresistances.append('thunder')
    npc.defer(lambda npc: npc.bonusactions.append(f"***Tempestuous Magic.*** Whenever you cast a spell other than a cantrip that deals lightning or thunder damage, creatures of your choice within 10 feet of you take {npc.levels('Sorcerer') // 2} lightning or thunder (your choice) damage.") )
```

## Storm Guide
*6th-level Storm feature*

You gain the ability to subtly control the weather around you. If it is raining, you can use an action to cause the rain to stop falling in a 20-foot radius centered on you. You can end this effect as a bonus action.

If it is windy, you can use a bonus action each round to choose the direction that the wind blows in a 100-foot radius around you. The wind blows in that direction until the end of your next turn. You have no ability to alter the speed of the wind.

```
    npc.actions.append("***Storm Guide.*** If it is raining, you can use an action to cause the rain to stop falling in a 20-foot radius centered on you. You can end this effect as a bonus action.")
    npc.bonusactions.append("***Storm Guide.*** If it is windy, you can choose the direction that the wind blows in a 100-foot radius around you. The wind blows in that direction until the end of your next turn. You have no ability to alter the speed of the wind.")
```

## Storm's Fury
*14th-level Storm feature*

The storm energy you channel through your magic seethes within your soul. When you are hit by a melee attack, you can use your reaction to deal lightning damage to the attacker equal to your sorcerer level. The attacker must also make a Strength saving throw, with a DC equal to 8 + your Charisma bonus + your proficiency bonus. On a failed save, the attacker is pushed in a straight line 20 feet away from you.

```
def level14(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Storm's Fury.*** When you are hit by a melee attack, you can deal {npc.levels('Sorcerer')} lightning damage to the attacker. The attacker must also make a Strength saving throw (DC {8 + npc.CHAbonus() + npc.proficiencybonus()}). On a failed save, the attacker is pushed in a straight line 20 feet away from you.") )
```

## Wind Soul
*18th-level Storm feature*

You gain a flying speed of 60 feet and immunity to lightning and thunder damage. As an action, you can reduce your flying speed to 30 feet for one hour and choose a number of creatures within 30 feet of you equal to 3 + your Charisma modifier. The chosen creatures gain a flying speed of 30 feet for 1 hour.

```
def level18(npc):
    npc.speed['flying'] = 60
    npc.damageimmunities.append('lightning')
    npc.damageimmunities.append('thunder')
    npc.defer(lambda npc: npc.actions.append(f"***Wind Soul.*** You reduce your flying speed to 30 feet for one hour, then choose {3 + npc.CHAbonus()} creatures within 30 feet of you, all of which gain a flying speed of 30 feet for 1 hour.") )
```
