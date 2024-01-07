# Divine Domain: Fertility
Gods of fertility are known in every culture and are associated with life, birth, abundance, and prosperity. They are known for their passionate hearts and physical beauty. These deities can be fickle and cruel, but they are more often playful and passionate. Their priestesses are known for their vitality, productivity, and proclivity. They are often accompanied by a menagerie animals and a harem of sexual partners.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Leriya](../../Religions/Trinitarian.md#leriya), [Brigantia](../../Religions/Pantheon/Brigantia.md), [Lathander](../../Religions/Pantheon/Lathander.md), ...

```
name = 'Fertility'
description = "***Divine Domain: Fertility.*** Gods of fertility are known in every culture and are associated with life, birth, abundance, and prosperity. They are known for their passionate hearts and physical beauty. These deities can be fickle and cruel, but they are more often playful and passionate. Their priestesses are known for their vitality, productivity, and proclivity. They are often accompanied by a menagerie animals and a harem of sexual partners."
```

**Fertility Domain Spells**

Cleric Level|Spells
------------|------
1st|[ceremony](../../Magic/Spells/ceremony.md), [charm person](../../Magic/Spells/charm-person.md)
3rd|[calm emotions](../../Magic/Spells/calm-emotions.md), [warding bond](../../Magic/Spells/warding-bond.md)
5th|[aura of vitality](../../Magic/Spells/aura-of-vitality.md), [beacon of hope](../../Magic/Spells/beacon-of-hope.md)
7th|[aura of life](../../Magic/Spells/aura-of-life.md), [aura of purity](../../Magic/Spells/aura-of-purity.md)
9th|[dominate person](../../Magic/Spells/dominate-person.md), [greater restoration](../../Magic/Spells/greater-restoration.md)

Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

```
domainspells = {
    1: ['ceremony', 'charm person'],
    3: ['calm emotions', 'warding bond'],
    5: ['aura of vitality', 'beacon of hope'],
    7: ['aura of life', 'aura of purity'],
    9: ['dominate person', 'greater restoration']
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

## Blessing of Allure
*1st-level Fertility domain feature*

You learn two languages of your choice. You also become proficient in your choice of two of the following skills: Deception, Insight, Performance, or Persuasion.

Your proficiency bonus is doubled for any ability check you make that uses either of those skills.

```
    npc.languages.append("CHOOSE")
    npc.languages.append("CHOOSE")
    npc.expertises.append(choose("Choose a skill: ", ['Deception', 'Insight', 'Performance', 'Persuasion']))
```

## Channel Divinity: Captivate Crowd
*2nd-level Fertility domain feature*

You can use your Channel Divinity to sway other people's opinions of you.

You weave a captivating string of words inspiring love and comraderie between you and the members of a crowd. As an action, choose a number of humanoids within 60 feet of you, up to a number equal to your Wisdom modifier (minimum of one). Each target must succeed on a Wisdom saving throw against your spell save DC or be charmed by you. While charmed in this way, the target adores you and those you designate, and it hinders anyone who opposes you, although it avoids violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies.

If a target succeeds on its saving throw, the target has no hint that you tried to charm it.

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Captivate Crowd.*** Choose a number of humanoids within 60 feet of you, up to a number equal to your Wisdom modifier (minimum of one). Each target must succeed on a Wisdom saving throw against your spell save DC or be charmed by you. While charmed in this way, the target adores you and those you designate, and it hinders anyone who opposes you, although it avoids violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies. If a target succeeds on its saving throw, the target has no hint that you tried to charm it.")
```

## Embodiment of Affection
*6th-level Fertility domain feature*

If you cast a spell of the abjuration school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Embodiment of Affection ({npc.WISbonus()}/Recharges on long rest).*** If you cast a spell of the abjuration school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action.") )
```

## Divine Strike
*8th-level Fertility domain feature*

Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} thunder damage to the target.") )
```

## Love's Embrace
*17th-level Fertility domain feature*

As a bonus action, you can designate an ally to encapsulate with the loving embrace of your aura for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack the embraced creature for the first time on a turn, the attacker must make a Charisma saving throw against your spell save DC. On a failed save, it can't attack that creature on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack the creature on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level17(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Love's Embrace (Recharges on short or long rest).*** You can designate an ally to encapsulate with the loving embrace of your aura for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack the embraced creature for the first time on a turn, the attacker must make a Charisma saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}). On a failed save, it can't attack that creature on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack the creature on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn.") )
```
