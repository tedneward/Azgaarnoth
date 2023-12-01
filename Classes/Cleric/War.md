# Divine Domain: War
War has many manifestations. It can make heroes of ordinary people. It can be desperate and horrific, with acts of cruelty and cowardice eclipsing instances of excellence and courage. In either case, the gods of war watch over warriors and reward them for their great deeds. The clerics of such gods excel in battle, inspiring others to fight the good fight or offering acts of violence as prayers. Gods of war include champions of honor and chivalry (such as Torm, Heironeous, and Kiri-Jolith) as well as gods of destruction and pillage (such as Erythnul, the Fury, Gruumsh, and Ares) and gods of conquest and domination (such as Bane, Hextor, and Maglubiyet). Other war gods (such as Tempus, Nike, and Nuada) take a more neutral stance, promoting war in all its manifestations and supporting warriors in any circumstance.

This is a domain granted by the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Zabalasan tradition](../../Religions/AlUma.md#zabalasan-cleric),the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), [Bahamut](../../Religions/Pantheon/Bahamut.md), [Heironeous](../../Religions/Pantheon/Heironeous.md), [Gruumsh](../../Religions/Pantheon/Gruumsh.md), [Hextor](../../Religions/Pantheon/Hextor.md), [Lythtzu](../../Religions/Pantheon/Lythtzu.md), [Maglubiyet](../../Religions/Pantheon/Maglubiyet.md), ...

```
name = 'War'
description = "***Divine Domain: War.*** War has many manifestations. It can make heroes of ordinary people. It can be desperate and horrific, with acts of cruelty and cowardice eclipsing instances of excellence and courage. In either case, the gods of war watch over warriors and reward them for their great deeds. The clerics of such gods excel in battle, inspiring others to fight the good fight or offering acts of violence as prayers. Gods of war include champions of honor and chivalry (Heironeous) as well as gods of destruction and pillage (Gruumsh) and gods of conquest and domination (Hextor, and Maglubiyet). Other war gods take a more neutral stance, promoting war in all its manifestations and supporting warriors in any circumstance."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Unity Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**War Domain Spells**

Cleric Level |	Spells
------------ | -----
1st | [divine favor](../../Magic/Spells/divine-favor.md), [shield of faith](../../Magic/Spells/shield-of-faith.md)
3rd | [magic weapon](../../Magic/Spells/magic-weapon.md), [spiritual weapon](../../Magic/Spells/spiritual-weapon.md)
5th | [crusader's mantle](../../Magic/Spells/crusaders-mantle.md), [spirit guardians](../../Magic/Spells/spirit-guardians.md)
7th | [freedom of movement](../../Magic/Spells/freedom-of-movement.md), [stoneskin](../../Magic/Spells/stoneskin.md)
9th | [flame strike](../../Magic/Spells/flame-strike.md), [hold monster](../../Magic/Spells/hold-monster.md)

```
domainspells = {
    1: ['bane', 'hellish rebuke'],
    3: ['cloud of daggers', 'heat metal'],
    5: ['bestow curse', 'fear'],
    7: ['phatasmal killer', 'staggering smite'],
    9: ['synaptic static', 'geas']
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
*1st-level War domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for prof in weapons['martial-melee'] | weapons['martial-ranged'] | armor['heavy']:
        npc.proficiencies.append(prof)
```

## War Priest
*1st-level War domain feature*

Your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***War Priest ({npc.WISbonus()}/Recharges on long rest).*** When you use the Attack action, you can make one weapon attack as a bonus action.") )
```

## Channel Divinity: Guided Strike
*2nd-level War domain feature*

You can use your Channel Divinity to strike with supernatural accuracy. When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Guided Strike.*** When you make an attack roll, you can use your Channel Divinity to gain a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
```

## Channel Divinity: War God's Blessing
*6th-level War domain feature*

When a creature within 30 feet of you makes an attack roll, you can use your reaction to grant that creature a +10 bonus to the roll, using your Channel Divinity. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.

```
def level6(npc):
    npc.reactions.append("***Channel Divinity: War God's Blessing.*** When a creature within 30 feet of you makes an attack roll, you grant that creature a +10 bonus to the roll. You make this choice after you see the roll, but before the DM says whether the attack hits or misses.")
```

## Divine Strike
*8th-level War domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} damage of the same type dealt by the weapon to the target.") )
```

## Avatar of Battle
*17th-level War domain feature*

You gain resistance to bludgeoning, piercing, and slashing damage from nonmagical weapons.

```
def level17(npc):
    npc.damageresistances.append('bludgeoning, piercing, and slashing damage from nonmagical weapons')
```