# Divine Domain: Twilight
The twilit transition from light into darkness often brings calm and even joy, as the day's labors end and the hours of rest begin. The darkness can also bring terrors, but the gods of twilight guard against the horrors of the night. Clerics who serve these deities bring comfort to those who seek rest and protect them by venturing into the encroaching darkness to ensure that the dark is a comfort, not a terror.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Heironeous](../../Religions/Pantheon/Heironeous.md), [the Traveler](../../Religions/Pantheon/Traveler.md), ...

```
name = 'Twilight'
description = ""
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Unity Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Twilight Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| Faerie Fire, Sleep
3rd	| moonbeam, see invisibility
5th	| Aura of Vitality, Leomund's tiny hut
7th	| aura of life, Greater Invisibility
9th	| Circle of Power, mislead

```
domainspells = {
    1: ['charm person', 'disguise self'],
    3: ['mirror image', 'pass without trace'],
    5: ['blink', 'dispel magic'],
    7: ['dimension door', 'polymorph'],
    9: ['dominate person', 'modify memory']
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

## Bonus Proficiencies
*1st-level Twilight Domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for it in weapons['martial-melee'] | weapons['martial-ranged'] | armor['heavy']:
        npc.proficiencies.append(it)
```

## Eyes of Night
*1st-level Twilight Domain feature*

You can see through the deepest gloom. You have darkvision out to a range of 300 feet. In that radius, you can see in dim light as if it were bright light and in darkness as if it were dim light.

As an action, you can magically share the darkvision of this feature with willing creatures you can see within 10 feet of you, up to a number of creatures equal to your Wisdom modifier (minimum of one creature). The shared darkvision lasts for 1 hour. Once you share it, you can't do so again until you finish a long rest, unless you expend a spell slot of any level to share it again. 

```
    npc.senses['darkvision'] = 300
    npc.defer(lambda npc: npc.actions.append(f"***Eyes of Night (Recharges on long rest or spell slot).*** You magically share the darkvision of this feature with up to {npc.WISbonus()} willing creatures you can see within 10 feet of you. The shared darkvision lasts for 1 hour. Once you share it, you can't do so again until you finish a long rest, unless you expend a spell slot of any level to share it again.") )
```

## Vigilant Blessing
*1st-level Twilight Domain feature*

The night has taught you to be vigilant. As an action, you give one creature you touch (including possibly yourself) advantage on your next initiative roll the creature makes. This benefit ends immediately after the roll or if you use this feature again.

```
    npc.actions.append("***Vigilant Blessing.*** You give one creature you touch (including possibly yourself) advantage on your next initiative roll the creature makes. This benefit ends immediately after the roll or if you use this feature again.")
```

## Channel Divinity: Twilight Sanctuary
*2nd-level Twilight Domain feature*

You can use your Channel Divinity to refresh your allies with soothing twilight.

As an action, you present your holy symbol, and a sphere of twilight emanates from you. The sphere is centered on you, has a 30-foot radius, and is filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature (including you) ends its turn in the sphere, you can grant that creature one of these benefits:

* You grant it temporary hit points equal to 1d6 plus your cleric level.
* You end one effect on it causing it to be charmed or frightened. 

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append("***Channel Divinity: Twilight Sanctuary.*** You present your holy symbol, and you create a 30-foot-radius sphere of twilight, centered on you, filled with dim light. The sphere moves with you, and it lasts for 1 minute or until you are incapacitated or die. Whenever a creature (including you) ends its turn in the sphere, you can grant that creature one of these benefits: You grant it 1d6 + {npc.levels('Cleric')} temporary hit points. You end one effect on it causing it to be charmed or frightened.{'' if npc.levels('Cleric') < 17 else ' You and your allies also have half cover while inside the sphere.'}") )
```

## Steps of Night
*6th-level Twilight Domain feature*

You can draw on the mystical power of night to rise into the air. As a bonus action when you are in dim light or darkness, you can magically give yourself a flying speed equal to your walking speed for 1 minute. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Steps of Night ({npc.proficiencybonus()}/Recharges on long rest).*** When you are in dim light or darkness, you can magically give yourself a flying speed equal to your walking speed for 1 minute.") )
```

## Divine Strike
*8th-level Twilight Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} radiant damage.") )
```

## Twilight Shroud
*17th-level Twilight Domain feature*

The twilight that you summon offers a protective embrace: you and your allies have half cover while in the sphere created by your Twilight Sanctuary. 
