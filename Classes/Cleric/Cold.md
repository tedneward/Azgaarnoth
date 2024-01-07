# Divine Domain: Cold
The more benevolent gods of cold value patience and hard, enduring work ethic. Their followers are varied from the humble farmer stocking up the larder to make it through the winter; to the rugged deckmate bundling up sails while sheets of snow and frigid water threaten to freeze him solid. These followers have the fortitude to accomplish the toughest of tasks in the worst conditions and keep pushing forward. They push their bodies to the limit seeking to find their breaking point. They are rewarded when they find it, with newfound strength, and a new appreciation for the harshness of the cold. Along with this enduring work ethic however, is their tendency to like to take things slowly. Often these followers are told they slow their friends and acquaintances down whether in decision making or in moments when quick action is of highest import. The old story of the Tortle and the Tabaxi rings true for the Cleric of the Cold Domain in that they will most often take the slower, safer route knowing they will reach their goal in due time.

However, some gods of cold seek to bring the world to a complete stop--to enmesh everything in cold, unfeeling, immobile ice. What the benevolent gods of cold see as strength to persevere, the malevolent gods of cold see as a relentless drive to bury the world in ice.

```
name = 'Cold'
description = "***Divine Domain: Cold.*** The more benevolent gods of cold value patience and hard, enduring work ethic. Their followers are varied from the humble farmer stocking up the larder to make it through the winter; to the rugged deckmate bundling up sails while sheets of snow and frigid water threaten to freeze him solid. These followers have the fortitude to accomplish the toughest of tasks in the worst conditions and keep pushing forward. They push their bodies to the limit seeking to find their breaking point. They are rewarded when they find it, with newfound strength, and a new appreciation for the harshness of the cold. Along with this enduring work ethic however, is their tendency to like to take things slowly. Often these followers are told they slow their friends and acquaintances down whether in decision making or in moments when quick action is of highest import. The old story of the Tortle and the Tabaxi rings true for the Cleric of the Cold Domain in that they will most often take the slower, safer route knowing they will reach their goal in due time."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Cold Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Cold Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [armor of agathys](../../Magic/Spells/armor-of-agathys.md), [ice knife](../../Magic/Spells/ice-knife.md)
3rd	| [frost backlash](../../Magic/Spells/frost-backlash.md), [snilloc's snowball swarm](../../Magic/Spells/snillocs-snowball-storm.md)
5th	| [sleet storm](../../Magic/Spells/sleet-storm.md), [frost armor](../../Magic/Spells/frost-armor.md)
7th	| [ice storm](../../Magic/Spells/ice-storm.md), [orb of cold](../../Magic/Spells/orb-of-cold.md)
9th	| [cone of cold](../../Magic/Spells/cone-of-cold.md), [consume flame](../../Magic/Spells/consume-flame.md)

```
domainspells = {
    1: ['armor of agathys', 'ice knife'],
    3: ['frost backlash', 'snillocs snowball swarm'],
    5: ['sleet storm', 'frost armor'],
    7: ['ice storm', 'orb of cold'],
    9: ['cone of cold', 'consume flame']
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
*1st level Cold domain feature*

When you choose this domain at 1st level, you gain the [frostbite](../../Magic/Spells/frostbite.md) cantrip. It does not count against the number of cantrips you can know.

```
    spellcasting.cantripsknown.append('frostbite')
```

## Winter Ward
*1st level Cold domain feature*

You can move across difficult terrain created by ice or snow without spending extra movement, and you are no longer negatively impacted by the effects of cold climates.

Additionally, you may use an action to extend an aura of cold around you, freezing the ground. While the aura is active, you become resistant to cold damage, the ground within 10ft of you becomes difficult terrain for up to 4 creatures of your choice and your cold spells deal an extra 1d6 damage to creatures within this aura. The aura lasts for one minute.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.traits.append("***Winter Ward.*** You can move across difficult terrain created by ice or snow without spending extra movement, and you are no longer negatively impacted by the effects of cold climates.")

    npc.defer(lambda npc: npc.actions.append(f"***Winter Ward ({npc.WISbonus()}/Recharges on long rest).*** You extend an aura of cold around you, freezing the ground. While the aura is active, you become resistant to cold damage, the ground within {'10' if npc.levels('Cleric') < 17 else '30'}ft of you becomes difficult terrain for {'up to 4' if npc.levels('Cleric') < 17 else 'any number of'} creatures of your choice{', who also have disadvantage on Dexterity checks and saving throws if they are not resistant or immune to cold damage' if npc.levels('Cleric') < 17 else ''}, and your cold spells deal an extra {'1d6' if npc.levels('Cleric') < 17 else '2d6'} damage to creatures within this aura. The aura lasts for one minute.") )
```

## Channel Divinity: Frost Burn
*2nd-level Cold domain feature*

You can use your Channel Divinity to summon unthinkable cold and unleash it upon your enemies.

When you roll cold damage, you can use your Channel Divinity to deal maximum damage, instead of rolling.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Frost Burn.*** When you roll cold damage, you use one use of Channel Divinity to deal maximum damage, instead of rolling.")
```

## Chilled Blast
*6th-level Cold domain feature*

When you deal cold damage you may also reduce the targets speed by 10ft until the start of your next turn. 

```
def level6(npc):
    npc.traits.append("***Chilled Blast.*** When you deal cold damage you also reduce the target's speed by 10ft until the start of your next turn.")
```

## Divine Strike
*8th-level Cold domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 cold damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} cold damage to the target.") )
```

## Improved Winter Ward
*17th-level Cold domain feature*

You can withstand cold that would kill others and have improved your ability to radiate it. You are immune to cold damage. 

The range of your Winter Ward increases to 30 feet, affects any number of creatures of your choice within it, and your spells that deal cold damage to targets within it deal an extra 2d6 cold damage.

Additionally, creatures affected by your Winter Ward have disadvantage on Dexterity checks and saving throws if they are not resistant or immune to cold damage. 

```
def level17(npc):
    npc.damageimmunities.append("cold")
```