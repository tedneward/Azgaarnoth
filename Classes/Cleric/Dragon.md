# Divine Domain: Dragon
Within certain parts of Azgaarnoth, reverence for the dragons (both metallic and chromatic) has slipped into outright deification, and for whatever reason, their prayers are being answered.

This domain is available to followers of [Bahamut](../../Religions/Pantheon/Bahamut.md) and [Tiamat](../../Religions/Pantheon/Tiamat.md).

```
name = 'Dragon'
description = "***Divine Domain: Dragon.*** Within certain parts of Azgaarnoth, reverence for the dragons (both metallic and chromatic) has slipped into outright deification, and for whatever reason, their prayers are being answered."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Dragon Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Dragon Domain Spells**

Cleric Level|Spells
------------|------
1st|[absorb elements](../../Magic/Spells/absorb-elements.md), [identify](../../Magic/Spells/identify.md)
3rd|[locate object](../../Magic/Spells/locate-object.md), [dragon's breath](../../Magic/Spells/dragons-breath.md)
5th|[elemental weapon](../../Magic/Spells/elemental-weapon.md), [fear](../../Magic/Spells/fear.md)
7th|[elemental bane](../../Magic/Spells/elemental-bane.md), [leomund's secret chest](../../Magic/Spells/leomunds-secret-chest.md)
9th|[scrying](../../Magic/Spells/scrying.md), [skill empowerment](../../Magic/Spells/skill-empowerment.md)

```
domainspells = {
    1: ['absorb elements', 'identify'],
    3: ['locate object', "dragon's breath"],
    5: ['elemental weapon', 'fear'],
    7: ['elemental bane', "leomund's secret chest"],
    9: ['scrying', 'skill empowerment']
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

## Draconic Knowledge
*1st-level Dragon domain feature*

You learn Draconic if you don't know it already. If you already know Draconic, you learn a different language of your choice. You also gain proficiency in your choice of one the the following: Arcana, History, or Nature. Your proficiency bonus is doubled for any skill checks you make using that skill.

Additionally, if you spend at least one minute studying a gem or object, you can determine the item's exact value.

```
    if 'Draconic' in npc.languages:
        npc.languages.append("CHOOSE")
    else:
        npc.languages.append("Draconic")

    npc.expertises.append(choose("Choose an expertise: ", ['Arcana', 'History', 'Nature']))

    npc.traits.append("***Draconic Knowledge.*** If you spend at least one minute studying a gem or object, you can determine the item's exact value.")
```

## Channel Divinity: Frightful Presence
*2nd-level Dragon domain feature*

You can use your Channel Divinity to magically make yourself appear more draconic and menacing in nature.

As an action, choose a number of creatures up to your Wisdom modifier (minimum 1) that are within 30 feet of you. These creatures must succeed on a Wisdom saving throw or be frightened of you for one minute. A creature that fails its saving throw can attempt it again at the end of each of its turns, ending the effect on itself on a success.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append("***Channel Divinity: Frightful Presence.*** Choose up to {npc.WISbonus()} creatures that are within 30 feet of you. These creatures must succeed on a Wisdom saving throw or be frightened of you for one minute. A creature that fails its saving throw can attempt it again at the end of each of its turns, ending the effect on itself on a success.") )
```

## Draconic Resistance
*6th-level Dragon domain feature*

You gain resistance to a damage type of your choice: acid, cold, fire, lightning, or poison. This choice cannot be changed.

Additionally, if a creature within 20 feet of you takes acid, cold, fire, or lightning damage from an effect that you can see, you can use your reaction to grant resistance to the creature against that instance of the damage.

```
def level6(npc):
    npc.draconicresistance = choose("Choose a draconic resistance: ", ['acid', 'cold', 'fire', 'lightning', 'poison'])
    npc.damageresistances.append(npc.draconicresistance)
    npc.reactions.append(f"***Draconic Resistance.*** Additionally, if a creature within 20 feet of you takes acid, cold, fire, or lightning damage from an effect that you can see, you can use your reaction to grant resistance to the creature against that instance of the damage.")
```

## Dragon's Strike
*8th-level Dragon domain feature*

You gain the ability to infuse your weapon strikes with draconic energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra ld8 damage to the target. When you reach 14th level, the extra damage increases to 2d8. The damage is of the same type that you chose for your Draconic Resistance class feature.

```
def level8(npc):
    npc.defer(lambda npc: npc.actions.append("***Dragon's Strike (1/turn).*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} damage to the target.") )
```

## Draconic Immunity
*17th-level Dragon domain feature*

You become immune to the damage type that you chose for your Draconic Resistance class feature.

Additionally, you become immune to being charmed, and magic can't put you to sleep.

```
def level17(npc):
    npc.conditionimmunities.append('charmed')
    npc.conditionimmunities.append('sleep')
```