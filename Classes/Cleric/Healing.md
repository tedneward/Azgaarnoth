# Divine Domain: Healing
Gods of healing & medicine offer guidance to those who wish to rid the world of suffering. They reward compassion and dedication with guidance and intervention and bless their healers with magic to help save lives. Healing temples are often sought out when doctors' surgeries are unavailable. Followers of such deities can be found throughout the world and they come from all walks of life. Many choose to study Medicine in a more direct path and can attention that way, others serve in temples and act as a vessel for the Gods themselves. Some are blessed from a young age with the miraculous healing abilities, hand picked by their deity to do great things in the years to come.

This domain is available to clerics of the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Leriya](../../Religions/Trinitarian.md#leriya), [Diancecht](../../Religions/Pantheon/Diancecht.md), ...

```
name = 'Healing'
description = "***Divine Domain: Healing.*** Gods of healing & medicine offer guidance to those who wish to rid the world of suffering. They reward compassion and dedication with guidance and intervention and bless their healers with magic to help save lives. Healing temples are often sought out when doctors' surgeries are unavailable. Followers of such deities can be found throughout the world and they come from all walks of life. Many choose to study Medicine in a more direct path and can attention that way, others serve in temples and act as a vessel for the Gods themselves. Some are blessed from a young age with the miraculous healing abilities, hand picked by their deity to do great things in the years to come."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Healing Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Healing Domain Spells**

Cleric Level | Spells
------------ | -------
1st | [healing word](../../Magic/Spells/healing-word.md), [sanctuary](../../Magic/Spells/sanctuary.md)
3rd | [prayer of healing](../../Magic/Spells/prayer-of-healing.md), [protection from poison](../../Magic/Spells/protection-from-poison.md)
5th | [beacon of hope](../../Magic/Spells/beacon-of-hope.md), [remove curse](../../Magic/Spells/remove-curse.md)
7th | [death ward](../../Magic/Spells/death-ward.md), [resilient sphere](../../Magic/Spells/otilukes-resilient-sphere.md)
9th | [greater restoration](../../Magic/Spells/greater-restoration.md), [contagion](../../Magic/Spells/contagion.md)

```
domainspells = {
    1: ['healing word', 'sanctuary'],
    3: ['prayer of healing', 'protection from poison'],
    5: ['beacon of hope', 'remove curse'],
    7: ['death ward', 'resilient sphere'],
    9: ['greater restoration', 'contagion']
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


## Gifted Healer
*1st-level Healing Domain feature*

Whenever you use a spell to restore hit points to a creature, the creature regains additional hit points equal to your Wisdom modifier times the level of the spell cast.

If you've selected proficiency in Medicine, you gain Expertise in this field.

In addition, you learn the [spare the dying](../../Magic/Spells/spare-the-dying.md) cantrip, which doesn't count against the number of cleric cantrips you know.

```
    npc.addskillorexpertise('Medicine')
    npc.defer(lambda npc: npc.traits.append(f"***Gifted Healer.*** Whenever you use a spell to restore hit points to a creature, the creature regains {npc.WISbonus()} * the level of the spell cast additional hit points.") )
    spellcasting.cantripsknown.append('spare the dying')
```

## Channel Divinity: Preventative Measures
*2nd-level Healing Domain feature*

You can use your Channel Divinity to protect others from potential threats. Choose an ally within 30 feet of yourself to be granted immunity to poison, diseases and curses for a total of 1 minute.

You can use this one per long rest.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Preventative Measures (Recharges on long rest).*** Choose an ally within 30 feet of yourself to be granted immunity to poison, diseases and curses for a total of 1 minute.")
```

## Divine Diagnosis
*2nd-level Healing Domain feature*

You gain the ability to magically detect and diagnose ailments you encounter. As an action you can present your holy symbol and allow it to guide you towards a hidden source of poison, diseases or illness within 60 feet that isn't protected from divination magic. The sense does not inform you about the nature of the ailment you are tracking.

If you are diagnosing a patient and make physical contact you will be able to detect the exact nature, down to the name and the side effects, of any poison, illness or curse that is ailing them. You have advantage on any check in recalling further information. 

You can use this feature a number of times equal to your Wisdom modifier (minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Divine Diagnosis ({npc.WISbonus()}/Recharges on long rest).*** You can present your holy symbol and allow it to guide you towards a hidden source of poison, diseases or illness within 60 feet that isn't protected from divination magic. The sense does not inform you about the nature of the ailment you are tracking. If you are diagnosing a patient and make physical contact you will be able to detect the exact nature, down to the name and the side effects, of any poison, illness or curse that is ailing them. You have advantage on any check in recalling further information.") )
```

## A Friend in Need...
*6th-level Healing Domain feature*

When you or an ally you can see within 30 feet requires a Constitution save as a reaction you can grant a blessing that gives advantage. If saved successfully that creature will become immune to that threat for 1 hour.

This can only be used once before requiring a short rest.

```
def level6(npc):
    npc.reactions.append("***A Friend in Need (Recharges on short rest).*** When you or an ally you can see within 30 feet requires a Constitution save you grant a blessing that gives advantage. If saved successfully that creature will become immune to that threat for 1 hour.")
```

## Protect the Healer!
*8th-level Healing Domain feature*

As a reaction you can subtract your Wisdom modifier total from an attack roll made against you. 

This can be used twice per long rest.

```
def level8(npc):
    npc.defer(lambda npc: npc.reactions.append("***Protect the Healer (2/Recharges on long rest).*** You subtract {npc.WISbonus()} from an attack roll made against you.") )
```

## Divine Restoration
*17th-level Healing Domain feature*

As your power grows you begin to channel Divine Light in such a way that Material and Somatic components are no longer needed when using the spell Revivy, Raise the Dead or Resurrection.

Once used this feature cannot be accessed again for 1d10 +4 days. 

```
def level17(npc):
    npc.traits.append("***Divine Restoration (Recharges in 1d10+4 days).*** As your power grows you begin to channel Divine Light in such a way that Material and Somatic components are no longer needed when using the spell *revivy*, *raise the dead* or *resurrection*.")
```
