# Otherworldly Patron: The Undying Light
Your patron is not a specific entity, but the energy that radiates from the Positive Plane. Your pact allows you to experience the barest touch of the raw stuff of life that powers the multiverse. Anything more, and you would be instantly incinerated by its energy. Contact with the Positive Plane causes subtle changes to your behavior and beliefs. You are driven to bring light to dark places, to annihilate undead creatures, and to protect all living things. At the same time, you crave the light and find total darkness a suffocating experience akin to drowning. Sometimes, however, contact with the Positive Plane creates a terrible imbalance in a mortal's mental state, and over time, their drive is to bring everything into the light--the bright, searing, cleansing, annihiliating light that leaves nothing behind except... light.

As an optional way to add more flavor to your character, you can pick from or roll on the following table of flaws associated with warlocks of the Undying Light.

**Undying Light Flaws**

d6| Flaw
--| ----
1 | You are afraid of the dark, and must always have a light source at hand.
2 | You have a nervous compulsion to keep a bright light in even the barest shadow.
3 | You have a compulsion to enter and illuminate dark areas.
4 | You have an overwhelming hatred of undead creatures.
5 | You fidget and are irritable when you can't see the sun.
6 | In a dark area, you always carry a lit torch or lantern. Putting it down is an unbearable thought.
7 | You find yourself prone to create as much light as possible, setting whole buildings ablaze if necessary.
8 | You constantly seek to bring living beings into the light, by force and violence if necessary.

```
name = 'Undying Light'
description = "***Otherworldly Patron: The Undying Light.*** Your patron is not a specific entity, but the energy that radiates from the Positive Plane. Your pact allows you to experience the barest touch of the raw stuff of life that powers the multiverse. Anything more, and you would be instantly incinerated by its energy. Contact with the Positive Plane causes subtle changes to your behavior and beliefs. You are driven to bring light to dark places, to annihilate undead creatures, and to protect all living things. At the same time, you crave the light and find total darkness a suffocating experience akin to drowning."
```

## Expanded Spell List
The Undying Light lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.

**Undying Light Expanded Spells** 
Spell Level|Spells
-----------|------
1st | [burning hands](../../Magic/Spells/burning-hands.md)
2nd | [flaming sphere](../../Magic/Spells/flaming-sphere.md)
3rd | [daylight](../../Magic/Spells/daylight.md)
4th | [fire shield](../../Magic/Spells/fire-shield.md)
5th | [flame strike](../../Magic/Spells/flame-strike.md)

```
def level1(npc):
    flaws = [
        'You are afraid of the dark, and must always have a light source at hand.',
        'You have a nervous compulsion to keep a bright light in even the barest shadow.',
        'You have a compulsion to enter and illuminate dark areas.',
        'You have an overwhelming hatred of undead creatures.',
        "You fidget and are irritable when you can't see the sun.",
        'In a dark area, you always carry a lit torch or lantern. Putting it down is an unbearable thought.'
    ]
    npc.defer(lambda npc: npc.description.append(f"***Flaw: Undying Light.*** {randomlist[flaws]}"))

    def expandedspells(npc):
        if npc.pactmagic.slotlevel >= 1:
            npc.pactmagic.spellsknown.append('dissonant whispers')
            npc.pactmagic.spellsknown.append('tashas hideous laughter')
        if npc.pactmagic.slotlevel >= 2:
            npc.pactmagic.spellsknown.append('detect thoughts')
            npc.pactmagic.spellsknown.append('phantasmal force')
        if npc.pactmagic.slotlevel >= 3:
            npc.pactmagic.spellsknown.append('clairvoyance')
            npc.pactmagic.spellsknown.append('sending')
        if npc.pactmagic.slotlevel >= 4:
            npc.pactmagic.spellsknown.append('dominate beast')
            npc.pactmagic.spellsknown.append('evards black tentacles')
        if npc.pactmagic.slotlevel >= 5:
            npc.pactmagic.spellsknown.append('dominate person')
            npc.pactmagic.spellsknown.append('telekinesis')
    npc.defer(lambda npc: expandedspells(npc) )
```

## Radiant Soul
*1st-level Undying Light patron feature*

Your link to the Positive Plane allows you to serve as a conduit for radiant energy. You have resistance to radiant damage, and when you cast a spell that deals radiant damage or fire damage, you add your Charisma modifier to that damage. Additionally, you know the [sacred flame](../../Magic/Spells/sacred-flame.md) and [light](../../Magic/Spells/light.md) cantrips and can cast them at will. They don't count against your number of cantrips known.

```
    npc.damageresistances.append('radiant')
    npc.defer(lambda npc: npc.traits.append("***Radiant Soul.*** When you cast a spell that deals radiant or fire damage, you add {npc.CHAbonus()} to that damage.") )
    npc.pactmagic.cantripsknown.append('sacred flame')
    npc.pactmagic.cantripsknown.append('light')
```

## Searing Vengeance
*6th-level Undying Light patron feature*

The radiant energy you channel allows you to overcome grievous injuries. When you would make a death saving throw, you can instead spring back to your feet with a burst of radiant energy. You immediately stand up (if you so choose), and you regain hit points equal to half your hit point maximum. All hostile creatures within 30 feet of you take 10 + your Charisma modifier radiant damage and are blinded until the end of your turn.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Searing Vengeance (Recharges on long rest).*** When you would make a death saving throw, you can instead spring back to your feet with a burst of radiant energy. You immediately stand up (if you so choose), and regain {npc.hitpoints // 2} hit points. All hostile creatures within 30 feet of you take {10 + npc.CHAbonus()} radiant damage and are blinded until the end of your turn.") )
```

## Radiant Resilience
*10th-level Undying Light patron feature*

You gain temporary hit points whenever you finish a long or short rest. These temporary hit points equal your warlock level + your Charisma modifier. Additionally, choose up to five creatures you can see at the end of your rest. Those creatures gain temporary hit points equal to half your warlock level + your Charisma modifier.

```
def level10(npc):
    npc.defer(lambda npc: npc.traits.append("***Radiant Resilience.*** You gain {npc.levels('Warlock') + npc.CHAbonus()} temporary hit points whenever you finish a long or short rest. Additionally, choose up to five creatures you can see at the end of your rest; those creatures gain {(npc.levels('Warlock') // 2) + npc.CHAbonus()} temporary hit points."))
```

## Blazing Light
*14th-level Undying Light patron feature*

You gain the ability to channel the Undying Light itself, to either heal or harm. 

As a bonus action, you can touch a creature and heal it. With each touch, a creature regains from 1d6 to 5d6 (your choice) hit points.

As a bonus action, you can make an Melee Spell attack, and upon a successful touch, deliver 1d6 to 5d6 (your choice) radiant damage, in addition to your normal Unarmed Strike damage.

You have a total pool of 15d6 you can expend. Subtract the dice you use with each touch from that total. You regain all expended dice from your pool when you finish a long rest.

```
def level14(npc):
    npc.traits.append("***Blazing Light (Recharges on long rest).*** You have a total pool of 15d6 you can expend. Subtract the dice you use with each touch from that total.")
    npc.defer(lambda npc: npc.bonusactions.append("***Blazing Light.*** *Melee Spell Attack:* +{npc.proficiencybonus() + npc.WISbonus()} to hit, range 5ft., one creature. Hit: 1d6 to 5d6 (your choice) radiant damage.") )
    npc.bonusactions.append("***Blazing Light.*** You touch a creature, and it regains from 1d6 to 5d6 (your choice) hit points.")
```
