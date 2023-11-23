# Divine Domain: Chaos
Chaos is the opposite of order, and so gods of chaos are opposed to stasis, preservation, and structure in almost all things. Deities of chaos are often unpredictable, but they usually favor change and transformation whenever possible, altering the status quo using both the forces of destruction and renewal. Some gods of chaos (such as The Traveler or Maglubiyet) are mischief-makers that delight in any deception that causes upheaval. Many of them (such as the Cat Lord) are masters of change itself, whether that change is manmade, natural and un-controllable, or sudden and magical. There are deities that see change and chaos as aspects of luck, while a few (Cyric) represent the inevitable chaotic destruction of entropy and disaster.

This domain is available to the followers of [the Cat Lord](../../Religions/Pantheon/CatLord.md), [Cyric](../../Religions/Pantheon/Cyric.md), [Malar](../../Religions/Pantheon/Malar.md), [the Traveler](../../Religions/Pantheon/Traveler.md), ...

Clerics of the Chaos Domain often aspire to be just as unpredictable as their deity. They work to abolish every status quo and upset every unquestioned norm.

```
name = 'Chaos'
description = "***Divine Domain: Chaos.*** Clerics of the Chaos Domain often aspire to be just as unpredictable as their deity. They work to abolish every status quo and upset every unquestioned norm."
```

**Chaos Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [bane](../../Magic/Spells/bane.md), [chaos bolt](../../Magic/Spells/chaos-bolt.md)
3rd	| [alter self](../../Magic/Spells/alter-self.md), [shatter](../../Magic/Spells/shatter.md)
5th	| [bestow curse](../../Magic/Spells/bestow-curse.md), [blink](../../Magic/Spells/blink.md)
7th	| [jinx](../../Magic/Spells/jinx.md), [polymorph](../../Magic/Spells/polymorph.md)
9th	| [animate objects](../../Magic/Spells/animate-objects.md), [reincarnate](../../Magic/Spells/reincarnate.md)

```
domainspells = {
    1: ['bane', 'chaos bolt'],
    3: ['alter self', 'shatter'],
    5: ['bestow curse', 'blink'],
    7: ['jinx', 'polymorph'],
    9: ['animate objects', 'reincarnate']
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
*1st-level Chaos Domain feature*

You gain proficiency with martial weapons.

```
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
```

## Chaotic Fate
*1st-level Chaos Domain feature*

Your link to chaos allows to you alter fate in minor ways. After a creature that you can see within 60 feet of you rolls a d20 for an attack roll or ability check or rolls a die for a table in a class feature or spell, you can use your reaction to alter fate, forcing the creature to reroll the die and use the new result.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Chaotic Fate ({npc.WISbonus()}/Recharges on long rest).*** After a creature that you can see within 60 feet of you rolls a d20 for an attack roll or ability check or rolls a die for a table in a class feature or spell, you can alter fate, forcing the creature to reroll the die and use the new result."))
```

## Channel Divinity: Wild Blessing
*2nd-level Chaos Domain feature*

You can use your Channel Divinity to invoke a small miracle of chaotic divinity, bestowed by your deity to spark change and disrupt order.

As an action, you present your holy symbol and cause a random effect. You roll on the Wild Blessing Table to determine the effect each time you use this feature.

**Wild Blessing Table**

d10	| Channel Divinity Effect
--- | -----------------------
1 | You teleport up to 60 feet to an unoccupied space that you can see. Each creature of your choice within 15 feet of either your starting position or your new position must make a Constitution saving throw, taking thunder damage equal to 2d6 + your cleric level on a failed save, or half as much damage on a successful one. Nonmagical objects of your choice in the area that aren't being worn or carried also take full damage.
2 | Each creature of your choice within 30 feet of you is surrounded by a barrier that grants it a +2 bonus to AC until the end of your next turn and advantage on the next saving throw it makes during that time.
3 | A wave of flames bursts outward in a 15-foot radius sphere centered on a point that you can see within 60 feet of you. Each creature in the area must make a Dexterity saving throw, taking fire damage equal to 2d10 + your cleric level on a failed save, or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried.
4 | Negative energy swirls as dark mist around you, lightly obscuring the area within 30 feet of you until the end of your next turn. Each creature of your choice within the area must succeed on a Constitution saving throw or be poisoned until the end of your next turn. If you target at least one creature with this effect, you and each creature of your choice in the area also gain temporary hit points equal to your cleric level.
5 | A wave of positive energy fills the area within 30 feet of you with bright light until the end of your next turn. Up to four creatures of your choice within the area each regain a number of hit points equal to your cleric level. If a creature has more than 0 hit points when it receives this healing, it also gains temporary hit points equal to half your cleric level.
6 | A bolt of lightning surges toward one creature or object that you can see within 60 feet of you. You may also choose up to two other creatures or objects within 15 feet of the first target. Each target must make a Dexterity saving throw. On a failed saving throw, a target takes lightning damage equal to 2d6 + your cleric level, and until the end of its next turn, it can't take reactions and it has disadvantage on attack rolls. On a successful saving throw, a target takes half as much damage and suffers no other effects.
7 | Each creature of your choice within 30 feet of you must succeed on a Wisdom saving throw or else it must use its reaction to make a melee weapon attack against one creature of your choice within its reach, dealing extra damage equal to your cleric level on a hit.
8 | Up to three creatures that you can see within 30 feet of you must make a Charisma saving throw. On a failed saving throw, a creature is transformed into a Small object chosen by the DM (such as a chair or a potted plant) until the end of its next turn. While transformed, it is stunned and it can't speak. If it takes damage, the transformation ends immediately.
9 | One willing creature that you can see within 60 feet of you regains hit points equal to 1d6 + two times your cleric level. Also, you can teleport the target up to 30 feet to an unoccupied space that you can see within 60 feet of you, and until the end of its next turn, it has advantage on saving throws and enemies have disadvantage on attacks against it.
10 | One creature that you can see within 60 feet of you must make a Constitution saving throw. On a failed saving throw, it takes cold damage equal to 3d6 + two times your cleric level and its speed is reduced to 0 feet until the end of its next turn. On a successful saving throw, it takes half as much damage and its speed isn't reduced.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Wild Blessing.*** You present your holy symbol and {'roll a d10' if npc.levels(spellcasting.casterclass) < 6 else 'roll two d10s and choose one of the two effects rolled; if both d10s are the same, choose any effect' if npc.levels(spellcasting.casterclass) < 17 else 'choose an effect from the following:'}: **1:** You teleport up to 60 feet to an unoccupied space that you can see. Each creature of your choice within 15 feet of either your starting position or your new position must make a Constitution saving throw, taking thunder damage equal to 2d6 + {npc.levels(spellcasting.casterclass)} on a failed save, or half as much damage on a successful one. Nonmagical objects of your choice in the area that aren't being worn or carried also take full damage. **2:** Each creature of your choice within 30 feet of you is surrounded by a barrier that grants it a +2 bonus to AC until the end of your next turn and advantage on the next saving throw it makes during that time. **3:** A wave of flames bursts outward in a 15-foot radius sphere centered on a point that you can see within 60 feet of you. Each creature in the area must make a Dexterity saving throw, taking 2d10 + {npc.levels(spellcasting.casterclass)} fire damage on a failed save, or half as much damage on a successful one. The fire ignites any flammable objects in the area that aren't being worn or carried. **4:** Negative energy swirls as dark mist around you, lightly obscuring the area within 30 feet of you until the end of your next turn. Each creature of your choice within the area must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}) or be poisoned until the end of your next turn. If you target at least one creature with this effect, you and each creature of your choice in the area also gain {npc.levels(spellcasting.casterclass)} temporary hit points. **5:** A wave of positive energy fills the area within 30 feet of you with bright light until the end of your next turn. Up to four creatures of your choice within the area each regain {npc.levels(spellcasting.casterclass)} hit points. If a creature has more than 0 hit points when it receives this healing, it also gains {npc.levels(spellcasting.casterclass) // 2} temporary hit points. **6:** A bolt of lightning surges toward one creature or object that you can see within 60 feet of you. You may also choose up to two other creatures or objects within 15 feet of the first target. Each target must make a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}). On a failed saving throw, a target takes lightning damage equal to 2d6 + {npc.levels(spellcasting.casterclass)}, and until the end of its next turn, it can't take reactions and it has disadvantage on attack rolls. On a successful saving throw, a target takes half as much damage and suffers no other effects. **7:** Each creature of your choice within 30 feet of you must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}) or else it must use its reaction to make a melee weapon attack against one creature of your choice within its reach, dealing {npc.levels(spellcasting.casterclass)} extra damage. **8:** Up to three creatures that you can see within 30 feet of you must make a Charisma saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}). On a failed saving throw, a creature is transformed into a Small object chosen by the DM (such as a chair or a potted plant) until the end of its next turn. While transformed, it is stunned and it can't speak. If it takes damage, the transformation ends immediately. **9:** One willing creature that you can see within 60 feet of you regains 1d6 + {2 * npc.levels(spellcasting.casterclass)} hit points. Also, you can teleport the target up to 30 feet to an unoccupied space that you can see within 60 feet of you, and until the end of its next turn, it has advantage on saving throws and enemies have disadvantage on attacks against it. **10:** One creature that you can see within 60 feet of you must make a Constitution saving throw. On a failed saving throw, it takes 3d6 + {2 * npc.levels(spellcasting.casterclass)} cold damage and its speed is reduced to 0 feet until the end of its next turn. On a successful saving throw, it takes half as much damage and its speed isn't reduced."))
```

## Inspired Chaos
*6th-level Chaos Domain feature*

Your deity grants you a measure of control over the chaos you receive from it. When you would roll a d10 for your Wild Blessing feature, you roll two d10s instead and choose which result to use. If both dice roll the same result, you choose the effect from the table.

## Divine Strike
*8th-level Chaos Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage to the target. When you reach 14th level, the extra damage increases to 2d8.

The type of this extra damage is based on the result of the d8. Starting at 14th level, you choose which d8 to use to determine the damage type. If both d8s roll the same result, you instead choose a type from the table.

d8 | Damage Type
-- | -----------
1 | Acid	
2 | Cold	
3 | Fire	
4 | Lightning	
5 | Necrotic
6 | Poison
7 | Radiant
8 | Thunder

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(spellcasting.casterclass) < 14 else '2d8'} damage to the target. The type of damage depends on the number rolled{'' if npc.levels(spellcasting.casterclass) < 14 else '; choose which d8 to use to determine the damage type. If both d8s roll the same result, you instead choose a type'}: **1** acid **2** cold **3** fire **4** lightning **5** necrotic **6** poison **7** radiant **8** thunder.") )
```

## Chaos Control
*17th-level Chaos Domain feature*

You gain the ability to alter fate and control chaos directly. Whenever you use your Wild Blessing feature, you can choose the effect from the table instead of rolling.

In addition, when you use your Channel Divinity feature, you can cause one spell of 3rd-level or lower that is affecting you or a willing creature that you can see within 30 feet of you to stop affecting that creature and instead start affecting a different willing creature of your choice that you can see within 30 feet.

Once you transform a spell in this way, you can't do so again until you finish a long rest.

```
def level17(npc):
    npc.traits.append("***Chaos Control (Recharges on long rest).*** When you use a Channel Divinity feature, you can cause one spell of 3rd-level or lower that is affecting you or a willing creature that you can see within 30 feet of you to stop affecting that creature and instead start affecting a different willing creature of your choice that you can see within 30 feet.")
```
