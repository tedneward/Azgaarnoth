# Divine Domain: Defier
Clerics of this domain are not true clerics, though they have similar abilities. They are disillusioned or heretical and have disavowed the worship of any deities they once believed in. Most consider the divine mysteries of the gods (who they often refer to only as "powers") to be elaborate scams. Many come to believe that the creatures called "gods" are not changeless, ineffable beings, but merely entities that have achieved a greater level of power--and are still as fallible as mortals. Such "clerics" often work tirelessly to discredit the gods, interfering with their clergy and attempting to liberate their congregations from what they consider false faith.

To maintain spellcasting abilities that equal those of religious clerics, some defiers enter into some kind of arrangement with a powerful being, like the otherworldly pact of a warlock. There are no delusions of divinity or worship involved in these arrangements; the defiers know what they are getting into, and are willing to pay the price.

Other defiers instead align themselves with the supreme force they call "the Great Unknown." This entity transcends the alleged gods (whom they consider to be powerful beings rather than divine creators worthy of worship). After all, some force must've created the planes of reality and given mortals their innate sense of good and evil. Such a force could not merely be one of the petty powers, however, wrangling with rivals and driven by greedy narcissism to seek worship. Rather, the force behind all creation must be unequalled and beyond such temporal concerns. Defiers aligned with the Great Unknown call themselves the Athar, and they are a very influential faction in some parts of the Outer Planes.

```
name = 'Defier'
description = "***Divine Domain: Defier.*** Clerics of this domain are not true clerics, though they have similar abilities. They are disillusioned or heretical and have disavowed the worship of any deities they once believed in. Most consider the divine mysteries of the gods to be elaborate scams. Many come to believe that the creatures called \"gods\" are not changeless, ineffable beings, but merely entities that have achieved a greater level of power--and are still as fallible as mortals. Defier clerics often work tirelessly to discredit the gods, interfering with their clergy and attempting to liberate their congregations from what they consider false faith."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Defier Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Defier Domain Spells**

Cleric Level | Spells
------------ | ------
1st|[detect evil and good](../../Magic/Spells/detect-evil-and-good.md), [nerveskitter](../../Magic/Spells/nerveskitter.md)
3rd|[calm emotions](../../Magic/Spells/calm-emotions.md), [silence](../../Magic/Spells/silence.md)
5th|[clarity of mind](../../Magic/Spells/clarity-of-mind.md), [counterspell](../../Magic/Spells/counterspell.md)
7th|[aura of purity](../../Magic/Spells/aura-of-purity.md), [Mordenkainen's private sanctum](../../Magic/Spells/mordenkainens-private-sanctum.md) 
9th|[banishing smite](../../Magic/Spells/banishing-smite.md), [lesser chainfire](../../Magic/Spells/lesser-chainfire.md)

```
domainspells = {
    1: ['detect evil and good', 'nerveskitter'],
    3: ['calm emotions', 'silence'],
    5: ['clarity of mind', 'counterspell'],
    7: ['aura of purity', 'mordenkainens private sanctum'],
    9: ['banishing smite', 'lesser chainfire']
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

## Bonus Proficiency
*1st-level Defier Domain feature*

You gain proficiency with heavy armor and with all martial weapons.

```
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
    for arm in armor['heavy']:
        npc.proficiencies.append(arm)
```

## Unbinding Strike
*1st-level Defier Domain feature*

When you hit a target with an attack roll, you can expend a spell slot to attempt to free that target from the influences of planar powers--whether they want that freedom or not. The target you hit takes extra psychic damage equal to twice the level of the spell slot you expended for this feature, and any divination, enchantment, or illusion spell that is on the target ends if it is of a level equal to or lower than that spell slot.

In addition, if the damaged creature is concentrating on a spell, the DC of the saving throw it makes to maintain its concentration is equal to your cleric spell save DC or half the damage inflicted, whichever is higher.

```
    npc.traits.append("***Unbinding Strike.*** When you hit a target with an attack roll, you can expend a spell slot to attempt to free that target from the influences of planar powers--whether they want that freedom or not. The target you hit takes extra psychic damage equal to twice the level of the spell slot you expended for this feature, and any divination, enchantment, or illusion spell that is on the target ends if it is of a level equal to or lower than that spell slot. In addition, if the damaged creature is concentrating on a spell, the DC of the saving throw it makes to maintain its concentration is equal to your cleric spell save DC or half the damage inflicted, whichever is higher.")
```

## Channel Divinity: Skeptic's Rebuke
*2nd-level Defier Domain feature*

You can use your Channel Divinity to repel those you see as representative of the so-called gods. As an action, you present your holy symbol and one aberration, celestial, fiend, or humanoid spellcaster of your choice with 30 feet of you must make a Wisdom saving throw, provided it can see or hear you. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.

A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.

After you reach 5th level, when a creature fails its saving throw against your Skeptic's Rebuke feature, the creature is banished for 1 minute (as the banishment spell, no concentration required) if it isn't on its plane of origin and its challenge rating is 1/2 or lower. As you reach higher levels in your cleric class, the challenge rating can be higher, as follows: CR 1 at 8th level, CR 2 at 11th level, CR 3 at 14th level, and CR 4 at 17th level.

```
def level2(npc):
    def skepticsrebuke(npc):
        if npc.levels('Cleric') < 5:
            npc.actions.append("***Channel Divinity: Skeptic's Rebuke.*** You present your holy symbol and one aberration, celestial, fiend, or humanoid spellcaster of your choice with 30 feet of you must make a Wisdom saving throw, provided it can see or hear you. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage. A turned creature must spend its turns trying to move as far away from you as it can, and it can't willingly move to a space within 30 feet of you. It also can't take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there's nowhere to move, the creature can use the Dodge action.")
        else:
            npc.actions.append("***Channel Divinity: Skeptic's Rebuke.*** You present your holy symbol and one aberration, celestial, fiend, or humanoid spellcaster of your choice with 30 feet of you must make a Wisdom saving throw, provided it can see or hear you. If the creature fails its saving throw, the creature is banished for 1 minute (as the {spelllinkify('banishment')} spell, no concentration required) if it isn't on its plane of origin and its challenge rating is {'1/2' if npc.levels('Cleric') < 8 else '1' if npc.levels('Cleric') < 11 else '2' if npc.levels('Cleric') < 14 else '3' if npc.levels('Cleric') < 17 else '4'} or lower.")

    npc.defer(lambda npc: skepticsrebuke(npc) )
```

## Defiant Mind
*6th-level Defier Domain feature*

Your defiant nature grants you resistance to psychic damage. In addition, when you hit an aberration, celestial, or fiend with an attack, or any creature that has regained hit points since the end of your last turn, you deal additional psychic damage to it equal to your cleric level.

```
def level6(npc):
    npc.traits.append("***Defiant Mind.*** Your defiant nature grants you resistance to psychic damage. In addition, when you hit an aberration, celestial, or fiend with an attack, or any creature that has regained hit points since the end of your last turn, you deal additional psychic damage to it equal to your cleric level.")
```
 
## Disillusioned Strike
*8th-level Defier Domain feature*

You gain the ability to infuse your weapon strikes with psychic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 psychic damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Disillusioned Strike.*** You gain the ability to infuse your weapon strikes with psychic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} psychic damage to the target.") )
```

## Unshackled Will
*17th-level Defier Domain feature*

You gain resistance to necrotic damage and radiant damage, and you have advantage on all saving throws against divination, enchantment, and illusion spells.

```
def level17(npc):
    npc.damageresistances.append('necrotic')
    npc.damageresistances.append('radiant')
    npc.traits.append("***Unshackled Will.*** You have advantage on all saving throws against divination, enchantment, and illusion spells.")
```
