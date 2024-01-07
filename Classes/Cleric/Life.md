# Divine Domain: Life
The Life domain focuses on the vibrant positive energy – one of the fundamental forces of the universe – that sustains all life. The gods of life promote vitality and health through healing the sick and wounded, caring for those in need, and driving away the forces of death and undeath

This is a domain granted by the [Alalihatian tradition](../../Religions/AlUma.md#alalihatian-cleric), the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Zabalasan tradition](../../Religions/AlUma.md#zabalasan-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Arawn](../../Religions/Pantheon/Arawn.md), [Daghda](../../Religions/Pantheon/Daghda.md), [Diancecht](../../Religions/Pantheon/Diancecht.md), [Lugh](../../Religions/Pantheon/Lugh.md), [Pelor](../../Religions/Pantheon/Pelor.md), ...

```
name = 'Life'
description = "***Divine Domain: Life.*** The Life domain focuses on the vibrant positive energy -- one of the fundamental forces of the universe -- that sustains all life. The gods of life promote vitality and health through healing the sick and wounded, caring for those in need, and driving away the forces of death and undeath."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Life Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Life Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [bless](../../Magic/Spells/bless.md), [cure wounds](../../Magic/Spells/cure-wounds.md)
3rd	| [lesser restoration](../../Magic/Spells/lesser-restoration.md), [spiritual weapon](../../Magic/Spells/spiritual-weapon.md)
5th	| [beacon of hope](../../Magic/Spells/beacon-of-hope.md), [revivify](../../Magic/Spells/revivify.md)
7th	| [death ward](../../Magic/Spells/death-ward.md), [guardian of faith](../../Magic/Spells/guardian-of-faith.md)
9th	| [mass cure wounds](../../Magic/Spells/mass-cure-wounds.md), [raise dead](../../Magic/Spells/raise-dead.md)

```
domainspells = {
    1: ['bless', 'cure wounds'],
    3: ['lesser restoration', 'spiritual weapon'],
    5: ['beacon of hope', 'revivify'],
    7: ['death ward', 'guardian of faith'],
    9: ['mass cure wounds', 'raise dead']
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
*1st-level Life Domain feature*

When you choose this domain at 1st level, you gain proficiency with heavy armor.

```
    for arm in armor['heavy']:
        npc.proficiencies.append(arm)
```

## Disciple of Life
*1st-level Life Domain feature*

Also starting at 1st level, your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level.

```
    npc.traits.append("***Disciple of Life.*** Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell's level.")
```

## Channel Divinity: Preserve Life
*2nd-level Life Domain feature*

You can use your Channel Divinity to heal the badly injured.

As an action, you present your holy symbol and evoke healing energy that can restore a number of hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Preserve Life.*** You present your holy symbol and evoke healing energy that can restore {5 * npc.levels('Cleric')} hit points equal to five times your cleric level. Choose any creatures within 30 feet of you, and divide those hit points among them. This feature can restore a creature to no more than half of its hit point maximum. You can't use this feature on an undead or a construct.") )
```

## Blessed Healer
*6th-level Life Domain feature*

The healing spells you cast on others heal you as well. When you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level.

```
def level6(npc):
    npc.traits.append("***Blessed Healer.*** hen you cast a spell of 1st level or higher that restores hit points to a creature other than you, you regain hit points equal to 2 + the spell's level.")
```

## Divine Strike
*8th-level Life Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {1 if npc.levels('Cleric') < 14 else 2}d8 radiant damage to the target.") )
```

## Supreme Healing
*17th-level Life Domain feature*

When you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die. For example, instead of restoring 2d6 hit points to a creature, you restore 12.

```
def level17(npc):
    npc.traits.append("***Supreme Healing.*** When you would normally roll one or more dice to restore hit points with a spell, you instead use the highest number possible for each die.")
```