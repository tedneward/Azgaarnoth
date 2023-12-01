# Divine Domain: Zeal
The Zeal domain is not so much a concept owned by a deity, but the fervor with which a worshiper evangelizes their divine being's message or portfolio; as a result any cleric can be a zealot, but to do so is to take the messages of the deity as your core identity.

This domain is available to clerics of the [Alalihatian tradition](../../Religions/AlUma.md#alalihatian-cleric), the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), ...

```
name = 'Zeal'
description = "***Divine Domain: Zeal.*** The Zeal domain is not so much a concept owned by a deity, but the fervor with which a worshiper evangelizes their divine being's message or portfolio; as a result any cleric can be a zealot, but to do so is to take the messages of the deity as your core identity."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Unity Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Zeal Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [searing smite](../../Magic/Spells/searing-smite.md), [thunderous smite](../../Magic/Spells/thunderous-smite.md)
3rd	| [magic weapon](../../Magic/Spells/magic-weapon.md), [zeal](../../Magic/Spells/zeal.md)
5th	| [haste](../../Magic/Spells/haste.md), [fireball](../../Magic/Spells/fireball.md)
7th	| [fire shield](../../Magic/Spells/fire-shield.md) (warm shield only), [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
9th	| [destructive wave](../../Magic/Spells/destructive-wave.md), [flame strike](../../Magic/Spells/flame-strike.md)

```
domainspells = {
    1: ['searing smite', 'thunderous smite'],
    3: ['magic weapon', 'zeal'],
    5: ['haste', 'fireball'],
    7: ['fire shield', 'freedom of movement'],
    9: ['destructive wave', 'flame strike']
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
*1st-level Zeal domain feature*

You gain proficiency with martial weapons and heavy armor.

```
    for prof in weapons['martial-melee'] | weapons['martial-ranged'] | armor['heavy']:
        npc.proficiencies.append(prof)
```

## Priest of Zeal
*1st-level Zeal domain feature*

Your god delivers bolts of inspiration to you while you are engaged in battle. When you use the Attack action, you can make one weapon attack as a bonus action.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Priest of Zeal ({npc.WISbonus()}/Recharges on long rest).*** When you use the Attack action, you can make one weapon attack as a bonus action.") )
```

## Channel Divinity: Consuming Fervor
*2nd-level Zeal domain feature*

You can use your Channel Divinity to channel your zeal into unchecked ferocity.

When you roll fire or thunder damage, you can use your Channel Divinity to deal maximum damage instead of rolling.

```
def level2(npc):
    npc.traits.append("***Channel Divinity: Consuming Fervor.*** When you roll fire or thunder damage, you can use your Channel Divinity to deal maximum damage instead of rolling.")
```

## Resounding Strike
*6th-level Zeal domain feature*

When you deal thunder damage to a Large or smaller creature, you can also push it up to 10 feet away from you.

```
def level6(npc):
    npc.traits.append("***Resounding Strike.*** When you deal thunder damage to a Large or smaller creature, you can also push it up to 10 feet away from you.")
```

## Divine Strike
*8th-level Zeal domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} damage of the same type dealt by the weapon to the target.") )
```

## Blaze of Glory
*17th-level Zeal domain feature*

You can delay death for an instant to perform a final heroic act.

When you are reduced to 0 hit points by an attacker you can see, even if you would be killed outright, you can use your reaction to move up to your speed toward the attacker and make one melee weapon attack against it, as long as the movement brings it within your reach. You make this attack with advantage. If the attack hits, the creature takes an extra 5d10 fire damage and an extra 5d10 damage of the weapon's type. You then fall unconscious and begin making death saving throws as normal, or you die if the damage you took would have killed you outright.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level17(npc):
    npc.reactions.append("***Blaze of Glory (Recharges on long rest).*** When you are reduced to 0 hit points by an attacker you can see, even if you would be killed outright, you move up to your speed toward the attacker and make one melee weapon attack against it, as long as the movement brings it within your reach. You make this attack with advantage. If the attack hits, the creature takes an extra 5d10 fire damage and an extra 5d10 damage of the weapon's type. You then fall unconscious and begin making death saving throws as normal, or you die if the damage you took would have killed you outright.")
```