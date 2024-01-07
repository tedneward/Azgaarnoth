# Divine Domain: Light
The gods of light have many followers, as so many mortals look up into the sky and see the sun, full of power and majesty. These deities often cast their light into the darkest shadows, bringing their light against the evil of the dark.

This domain is available to those who follow the [Alalihatian tradition](../../Religions/AlUma.md#alalihatian-cleric), the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), and those who revere [Ehlonna](../../Religions/Pantheon/Ehlonna.md), [Lathander](../../Religions/Pantheon/Lathander.md), [Larethian](../../Religions/Pantheon/Larethian.md), [Pelor](../../Religions/Pantheon/Pelor.md), ...

```
name = 'Light'
description = "***Divine Domain: Light.*** The gods of light have many followers, as so many mortals look up into the sky and see the sun, full of power and majesty. These deities often cast their light into the darkest shadows, bringing their light against the evil of the dark."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Light Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Light Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [burning hands](../../Magic/Spells/burning-hands.md), [faerie fire](../../Magic/Spells/faerie-fire.md)
3rd	| [flaming sphere](../../Magic/Spells/flaming-sphere.md), [scorching ray](../../Magic/Spells/scorching-ray.md)
5th	| [daylight](../../Magic/Spells/daylight.md), [fireball](../../Magic/Spells/fireball.md)
7th	| [guardian of faith](../../Magic/Spells/guardian-of-faith.md), [wall of fire](../../Magic/Spells/wall-of-fire.md)
9th	| [flame strike](../../Magic/Spells/flame-strike.md), [scrying](../../Magic/Spells/scrying.md)

```
domainspells = {
    1: ['burning hands', 'faerie fire'],
    3: ['flaming sphere', 'scorching ray'],
    5: ['daylight', 'fireball'],
    7: ['guardian of faith', 'wall of fire'],
    9: ['flame strike', 'scrying']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(spellcasting.casterclass) >= 1: results += domainspells[1]
        if npc.levels(spellcasting.casterclass) >= 3: results += domainspells[3]
        if npc.levels(spellcasting.casterclass) >= 5: results += domainspells[5]
        if npc.levels(spellcasting.casterclass) >= 7: results += domainspells[7]
        if npc.levels(spellcasting.casterclass) >= 9: results += domainspells[9]
        spellcasting.spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```

## Bonus Cantrip
*1st-level Light domain feature*

You gain the [light](../../Magic/Spells/light.md) cantrip if you don't already know it.

```
    spellcasting.cantripsknown.append('light')
```

## Warding Flare
*1st-level Light domain feature*

You can interpose divine light between yourself and an attacking enemy. When you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses. An attacker that can't be blinded is immune to this feature.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Warding Flare ({npc.WISbonus()}/Recharges on long rest).*** When {'you' if npc.levels('Cleric') < 6 else 'a creature that you can see'} are attacked by a creature within 30 feet of you that you can see, you cause light to flare before the attacker before it hits or misses, imposing disadvantage on the attack roll. An attacker that can't be blinded is immune to this feature.") )
```

## Channel Divinity: Radiance of the Dawn
*2nd-level Light domain feature*

You can use your Channel Divinity to harness sunlight, banishing darkness and dealing radiant damage to your foes.

As an action, you present your holy symbol, and any magical darkness within 30 feet of you is dispelled. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature takes radiant damage equal to 2d10 + your cleric level on a failed saving throw, and half as much damage on a successful one. A creature that has total cover from you is not affected.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Radiance of the Dawn.*** you present your holy symbol, and any magical darkness within 30 feet of you is dispelled. Additionally, each hostile creature within 30 feet of you must make a Constitution saving throw. A creature takes 2d8 + {npc.levels('Cleric')} radiant damage on a failed saving throw, and half as much damage on a successful one. A creature that has total cover from you is not affected.")
```

## Improved Flare
*6th-level Light domain feature*

You can also use your Warding Flare feature when a creature that you can see within 30 feet of you attacks a creature other than you.

## Potent Spellcasting
*8th-level Light domain feature*

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.traits.append("***Potent Spellcasting.*** You add your Wisdom modifier to the damage you deal with any cleric cantrip.")
```

## Corona of Light
*17th-level Light domain feature*

You can use your action to activate an aura of sunlight that lasts for 1 minute or until you dismiss it using another action. You emit bright light in a 60-foot radius and dim light 30 feet beyond that. Your enemies in the bright light have disadvantage on saving throws against any spell that deals fire or radiant damage.

```
def level17(npc):
    npc.actions.append("***Corona of Light.*** You activate an aura of sunlight that lasts for 1 minute or until you dismiss it using another action. You emit bright light in a 60-foot radius and dim light 30 feet beyond that. Your enemies in the bright light have disadvantage on saving throws against any spell that deals fire or radiant damage.")
```
