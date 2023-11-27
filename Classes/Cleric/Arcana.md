# Divine Domain: Arcana
Magic is an energy that suffuses the multiverse and that fuels both destruction and creation. Gods of the Arcana domain know the secrets and potential of magic intimately. For some of these gods, magical knowledge is a great responsibility that comes with a special understanding of the nature of reality. Other gods of Arcana see magic as pure power, to be used as its wielder sees fit.

The gods of this domain are often associated with knowledge, as learning and arcane power tend to go hand-in-hand.

This is a domain granted by [the Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Sor](../../Religions/Trinitarian.md#sor), [Azuth](../../Religions/Pantheon/Azuth.md), [Brigantia](../../Religions/Pantheon/Brigantia.md), and [Wee Jas](WeeJas.md).

```
name = 'Arcana'
description = "***Divine Domain: Arcana.*** Magic is an energy that suffuses the multiverse and that fuels both destruction and creation. Gods of the Arcana domain know the secrets and potential of magic intimately. For some of these gods, magical knowledge is a great responsibility that comes with a special understanding of the nature of reality. Other gods of Arcana see magic as pure power, to be used as its wielder sees fit."
```

## Domain Spells
*1st-level Arcana Domain feature* 

Starting at 1st level, you gain domain spells at the cleric levels listed in the Arcana Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Arcana Domain Spells**

Cleric Level |	Spells
------------ | -----
1st | [detect magic](../../Magic/Spells/detect-magic.md), [magic missile](../../Magic/Spells/magic-missile.md)
3rd	| [magic weapon](../../Magic/Spells/magic-weapon.md), [Nystul's magic aura](../../Magic/Spells/nystuls-magic-aura.md)
5th	| [dispel magic](../../Magic/Spells/dispel-magic.md), [magic circle](../../Magic/Spells/magic-circle.md)
7th	| [arcane eye](../../Magic/Spells/arcane-eye.md), [Leomund's Secret chest](../../Magic/Spells/leomunds-secret-chest.md)
9th	| [planar binding](../../Magic/Spells/planar-binding.md), [teleportation circle](../../Magic/Spells/teleportation-circle.md)

```
domainspells = {
    1: ['detect magic', 'magic missile'],
    3: ['magic weapon', 'nystuls magic aura'],
    5: ['dispel magic', 'magic circle'],
    7: ['arcane eye', 'leomunds secret chest'],
    9: ['planar binding', 'teleportation circle']
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

## Arcane Initiate
*1st-level Arcana Domain feature* 

You gain proficiency in the Arcana skill, and you gain two cantrips of your choice from the [wizard "core" spell list](../Wizard/index.md#core-wizard-spells). For you, these cantrips count as cleric cantrips.

```
    npc.proficiencies.append("Arcana")
    spellcasting.cantripsknown.append("CHOOSE-Wizard")
    spellcasting.cantripsknown.append("CHOOSE-Wizard")
```

## Channel Divinity: Arcane Abjuration
*2nd-level Arcana Domain feature* 

You can use your Channel Divinity to abjure otherworldly creatures.

As an action, you present your holy symbol, and one celestial, elemental, fey, or fiend of your choice that is within 30 feet of you must make a Wisdom saving throw, provided that the creature can see or hear you. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. It also can't take reactions. For its action, it can only use the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

After you reach 5th level, when a creature fails its saving throw against your Arcane Abjuration feature, the creature is banished for 1 minute (as in the Banishment spell, no concentration required) if it isn't on its plane of origin and its challenge rating is at or below a certain threshold, as shown on the Arcane Banishment table.

**Arcane Banishment**
Cleric Level |	Banishes Creatures of CR...
------------ | --------------------------
5th | 1/2 or lower
8th	| 1 or lower
11th | 2 or lower
14th | 3 or lower
17th | 4 or lower

```
def level2(npc):
    def turntext(npc): 
        cl = npc.levels(spellcasting.casterclass)
        if cl <= 5:
            return f"If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly end its move in a space within 30 feet of you. It also can't take reactions. For its action, it can only use the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action."
        else:
            return f"When a creature fails its saving throw against your Arcane Abjuration feature, the creature is banished for 1 minute (as in the {spelllinkify('banishment')} spell, no concentration required) if it isn't on its plane of origin and its challenge rating is {'1/2' if cl < 8 else '1' if cl < 11 else '2' if cl < 14 else '3' if cl < 17 else '4'} or below."

    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Arcane Abjuration.*** You present your holy symbol, and one celestial, elemental, fey, or fiend of your choice that is within 30 feet of you must make a Wisdom saving throw, provided that the creature can see or hear you. {turntext(npc)}") )
```

## Spell Breaker
*6th-level Arcana Domain feature* 

When you restore hit points to an ally with a spell of 1st level or higher, you can also end one spell of your choice on that creature. The level of the spell you end must be equal to or lower than the level of the spell slot you use to cast the healing spell.

```
def level6(npc):
    npc.traits.append("***Spell Breaker.*** When you restore hit points to an ally with a spell of 1st level or higher, you can also end one spell of your choice on that creature. The level of the spell you end must be equal to or lower than the level of the spell slot you use to cast the healing spell.")
```

## Potent Spellcasting
*8th-level Arcana Domain feature* 

You add your Wisdom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.traits.append("***Potent Spellcasting.*** You add your Wisdom modifier to the damage you deal with any cleric cantrip.")
```

## Arcane Mastery
*17th-level Arcana Domain feature* 

You choose four spells from the wizard spell list, one from each of the following levels: 6th, 7th, 8th, and 9th. You add them to your list of domain spells. Like your other domain spells, they are always prepared and count as cleric spells for you.

```
def level17(npc):
    spellcasting.spellsalwaysprepared.append("CHOOSE-Wizard-6th")
    spellcasting.spellsalwaysprepared.append("CHOOSE-Wizard-7th")
    spellcasting.spellsalwaysprepared.append("CHOOSE-Wizard-8th")
    spellcasting.spellsalwaysprepared.append("CHOOSE-Wizard-9th")
```
