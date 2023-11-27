# Divine Domain: Forge
The gods of the forge are patrons of artisans who work with metal, from a humble blacksmith who keeps a village in horseshoes and plow blades to the mighty elf artisan whose diamond-tipped arrows of mithral have felled demon lords. The gods of the forge teach that, with patience and hard work, even the most intractable metal can be transformed from a lump of ore to a beautifully wrought object. Clerics of these deities search for objects lost to the forces of darkness, liberate mines overrun by orcs, and uncover rare and wondrous materials necessary to create potent magic items. Followers of these gods take great pride in their work, and they are willing to craft and use heavy armor and powerful weapons to protect them.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), [Gond](../../Religions/Pantheon/Gond.md), [Onatar](../../Religions/Pantheon/Onatar.md), ...

```
name = 'Forge'
description = "***Divine Domain: Forge.*** The gods of the forge are patrons of artisans who work with metal, from a humble blacksmith who keeps a village in horseshoes and plow blades to the mighty elf artisan whose diamond-tipped arrows of mithral have felled demon lords. The gods of the forge teach that, with patience and hard work, even the most intractable metal can be transformed from a lump of ore to a beautifully wrought object. Clerics of these deities search for objects lost to the forces of darkness, liberate mines overrun by orcs, and uncover rare and wondrous materials necessary to create potent magic items. Followers of these gods take great pride in their work, and they are willing to craft and use heavy armor and powerful weapons to protect them."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Forge Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Forge Domain Spells**

Cleric Level | Spells
------------ | ------
1st | [identify](../../Magic/Spells/identify.md), [searing smite](../../Magic/Spells/searing-smite.md)
3rd	| [heat metal](../../Magic/Spells/heat-metal.md), [magic weapon](../../Magic/Spells/magic-weapon.md)
5th	| [elemental weapon](../../Magic/Spells/elemental-weapon.md), [protection from energy](../../Magic/Spells/protection-from-energy.md)
7th	| [fabricate](../../Magic/Spells/fabricate.md), [wall of fire](../../Magic/Spells/wall-of-fire.md)
9th	| [animate objects](../../Magic/Spells/animate-objects.md), [creation](../../Magic/Spells/creation.md)

```
domainspells = {
    1: ['identify', 'searing smite'],
    3: ['heat metal', 'magic weapon'],
    5: ['elemental weapon', 'protection from energy'],
    7: ['fabricate', 'wall of fire'],
    9: ['animate objects', 'creation']
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
*1st-level Forge domain feature*

You gain proficiency with heavy armor and smith's tools.

```
    for prof in armor['heavy']:
        npc.proficiencies.append(prof)
    npc.proficiencies.append("Smith's tools")
```

## Blessing of the Forge
*1st-level Forge domain feature*

You gain the ability to imbue magic into a weapon or armor. At the end of a long rest, you can touch one nonmagical object that is a suit of armor or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes a magic item, granting a +1 bonus to AC if it's armor or a +1 bonus to attack and damage rolls if it's a weapon.

Once you use this feature, you can't use it again until you finish a long rest.

```
    npc.traits.append("***Blessing of the Forge (Recharges on long rest).*** You gain the ability to imbue magic into a weapon or armor. At the end of a long rest, you can touch one nonmagical object that is a suit of armor or a simple or martial weapon. Until the end of your next long rest or until you die, the object becomes a magic item, granting a +1 bonus to AC if it's armor or a +1 bonus to attack and damage rolls if it's a weapon.")
```

## Channel Divinity: Artisan's Blessing
*2nd-level Forge domain feature*

You can use your Channel Divinity to create simple items.

You conduct an hour-long ritual that crafts a nonmagical item that must include some metal: a simple or martial weapon, a suit of armor, ten pieces of ammunition, a set of tools, or another metal object. The creation is completed at the end of the hour, coalescing in an unoccupied space of your choice on a surface within 5 feet of you.

The thing you create can be something that is worth no more than 100 gp. As part of this ritual, you must lay out metal, which can include coins, with a value equal to the creation. The metal irretrievably coalesces and transforms into the creation at the ritual's end, magically forming even nonmetal parts of the creation.

The ritual can create a duplicate of a nonmagical item that contains metal, such as a key, if you possess the original during the ritual.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Artisan's Blessing.*** You conduct an hour-long ritual that crafts a nonmagical item that must include some metal: a simple or martial weapon, a suit of armor, ten pieces of ammunition, a set of tools, or another metal object. The creation is completed at the end of the hour, coalescing in an unoccupied space of your choice on a surface within 5 feet of you.The thing you create can be something that is worth no more than 100 gp. As part of this ritual, you must lay out metal, which can include coins, with a value equal to the creation. The metal irretrievably coalesces and transforms into the creation at the ritual's end, magically forming even nonmetal parts of the creation. The ritual can create a duplicate of a nonmagical item that contains metal, such as a key, if you possess the original during the ritual.")
```

## Soul of the Forge
*6th-level Forge domain feature*

Your mastery of the forge grants you special abilities:

* You gain resistance to fire damage.
* While wearing heavy armor, you gain a +1 bonus to AC.

```
def level6(npc):
    npc.damageresistances.append('fire')
    npc.armorclass['Soul of the Forge'] = 1
```

## Divine Strike
*8th-level Forge domain feature*

You gain the ability to infuse your weapon strikes with the fiery power of the forge. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 fire damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.traits.append("***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} fire damage to the target.")
```

## Saint of Forge and Fire
*17th-level Forge domain feature*

Your blessed affinity with fire and metal becomes more powerful:

* You gain immunity to fire damage.
* While wearing heavy armor, you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.

```
def level17(npc):
    npc.damageimmunities.append('fire')
    npc.traits.append("***Saint of Forge and Fire.*** While wearing heavy armor, you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks.")
```
