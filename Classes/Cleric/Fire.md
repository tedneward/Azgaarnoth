# Divine Domain: Fire
*The Dragonborn raises his hand forward to the bloody ghoul, a spark of flame flickering in it. "Return to cinders, feeble undead!" he shouts as a jet of fire spills onto the fiendish creature, with ashes already forming. His elven companion, behind him and dazed, comes to her senses as the Dragonborn raises an amulet and a swirl of flame billows beneath the two of them. Her body fills with renewed vigor, and they stand together, mending each others' wounds.*

Clerics of Fire hold dominion over the powers of destruction but also creation; immolation yet warmth. While fire is a symbol of chaos and unrelenting harm, it also stands as a symbol of purification (such as how incense burned to permeate a scent of cleansing) and healing (like how a wound is seared to prevent infection). The one constant of fire is that whatever it touches is forever changed.

```
name = 'Fire'
description = "***Divine Domain: Fire.*** Clerics of Fire hold dominion over the powers of destruction but also creation; immolation yet warmth. While fire is a symbol of chaos and unrelenting harm, it also stands as a symbol of purification (such as how incense burned to permeate a scent of cleansing) and healing (like how a wound is seared to prevent infection). The one constant of fire is that whatever it touches is forever changed."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Fire Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Fire Domain Spells**

Cleric Level | Spells
------------ | ------
1st	 | [burning hands](../../Magic/Spells/burning-hands.md), [hellish rebuke](../../Magic/Spells/hellish-rebuke.md), [earth tremor](../../Magic/Spells/earth-tremor.md) (pick 2)
3rd	 | [flame blade](../../Magic/Spells/flame-blade.md), [scorching ray](../../Magic/Spells/scorching-ray.md)
5th	 | [fireball](../../Magic/Spells/fireball.md), [melf's minute meteors](../../Magic/Spells/melfs-minute-meteors.md)
7th	 | [wall of fire](../../Magic/Spells/wall-of-fire.md), [fire shield](../../Magic/Spells/fire-shield.md)
9th	 | [conjure elemental](../../Magic/Spells/conjure-elemental.md), [flame strike](../../Magic/Spells/flame-strike.md), [immolation](../../Magic/Spells/immolation.md) (pick 2)

```
domainspells = {
    1: ['burning hands', 'hellish rebuke', 'earth tremor],
    3: ['flame blade', 'scorching ray'],
    5: ['fireball', 'melfs minute meteors'],
    7: ['wall of fire', 'fire shield'],
    9: ['conjure elemental', 'flame strike', 'immolation']
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
*1st-level Fire Domain feature*

When you choose this domain at 1st level, you gain proficiency with heavy armor and martial weapons.

```
    for prof in armor['heavy']|weapons['martial-melee']|weapons['martial-ranged']:
        npc.proficiencies.append(prof)
```

## Wrath of the Inferno
*1st-level Fire Domain feature*

You can blazingly rebuke attackers. When a creature within 5 feet of you hits you with an attack, you can use your reaction to cause the creature to make a Dexterity saving throw using your spell save DC. The creature takes 2d8 fire damage on a failed saving throw, and half as much damage on a successful one. You can use this feature a number of times equal to your Wisdom modifier (a minimum of once).

You regain all expended uses when you finish a long rest, half the amount after a short rest.

```
    npc.reactions.append(f"***Wrath of the Inferno ({'' if npc.WISbonus() == 1 else '' + str(npc.WISbonus()) + '/'}Recharges on long rest, half on short rest).*** When a creature within 5 feet of you hits you with an attack, you cause the creature to make a Dexterity saving throw (DC {spellcasting.spellsavedc()}). The creature takes 2d8 fire damage on a failed saving throw, and half as much damage on a successful one.")
```

## Channel Divinity: Searing Wrath
*2nd-level Fire Domain feature*

You can use your Channel Divinity to wield the power of the blaze with unchecked ferocity. When you roll fire or radiant damage, you can use your Channel Divinity to deal maximum damage instead of rolling.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Searing Wrath.*** When you roll fire or radiant damage, you can use your Channel Divinity to deal maximum damage instead of rolling.")
```

## Blazing Enhancement
*6th-level Fire Domain feature*

Once per long rest, you can imbue a weapon of your choice with flaming power, granting the weapon a damage bonus equal to half your Wisdom modifier (rounded down). This is a magical bonus (meaning it can damage those creatures with immunity to non-magical weapons), but does not aid the die roll to hit. This bonus lasts until your next long rest, after which you may use this feature again.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append("***Blazing Enhancement (Recharges on long rest).*** Once per long rest, you can imbue a weapon of your choice with flaming power, granting the weapon a +{npc.WISbonus() // 2} damage bonus. This is a magical bonus (meaning it can damage those creatures with immunity to non-magical weapons), but does not aid the die roll to hit. This bonus lasts until your next long rest.") )
```

## Divine Strike
*8th-level Fire Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to do an extra 1d8 fire damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to do an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} fire damage to the target.") )
```

## Born of the Furnace
*17th-level Fire Domain feature*

You have developed an immunity to all fire damage, including infernal fire and lava. When you cast a spell that deals fire or radiant damage, add your Wisdom modifier to that damage. You also gain resistance to bludgeoning, piercing and slashing damage from weapon attacks.

```
def level17(npc):
    npc.damageimmunities.append("fire")
    npc.damageresistances.append("bludgeoning")
    npc.damageresistances.append("piercing")
    npc.damageresistances.append("slashing")
    npc.defer(lambda npc: npc.traits.append("When you cast a spell that deals fire or radiant damage, add {npc.WISbonus()} to that damage.") )
```
