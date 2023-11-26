# Divine Domain: Luck
The gods of luck and fortune have many followers, as so many mortals seek good luck and easy fortune. These deities rarely take sides, weighing weal and woe (mostly) fairly for all. Some are benevolent, especially favoring those who leave tokens of chance at their shrines. Clerics of luck often make decisions based on a coin flip or dice roll leaving tough choices to their deity, and preaching that life is always unpredictable.

This domain is available to [Trinitarians who worship Leriya](../../Religions/Trinitarian.md#leriya), [Silvanus](../../Religions/Pantheon/Silvanus.md), ...

```
name = 'Luck'
description = "***Divine Domain: Luck.*** The gods of luck and fortune have many followers, as so many mortals seek good luck and easy fortune. These deities rarely take sides, weighing weal and woe (mostly) fairly for all. Some are benevolent, especially favoring those who leave tokens of chance at their shrines. Clerics of luck often make decisions based on a coin flip or dice roll leaving tough choices to their deity, and preaching that life is always unpredictable."
```

## Domain Spells
Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**LUCK DOMAIN SPELLS**

Cleric Level|Spells
------------|------
1st | [bane](../../Magic/Spells/bane.md), [bless](../../Magic/Spells/bless.md)
3rd | [augury](../../Magic/Spells/augury.md), [mirror image](../../Magic/Spells/mirror-image.md)
5th | [bestow curse](../../Magic/Spells/bestow-curse.md), [haste](../../Magic/Spells/haste.md)
7th | [jinx](../../Magic/Spells/jinx.md), [twist fate](../../Magic/Spells/twist-fate.md)
9th | [blessing of luck](../../Magic/Spells/blessing-of-luck.md), [circle of power](../../Magic/Spells/circle-of-power.md)

```
domainspells = {
    1: ['bane', 'bless'],
    3: ['augury', 'mirror image'],
    5: ['bestow curse', 'haste'],
    7: ['jinx', 'twist fate'],
    9: ['blessing of luck', 'circle of power']
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

## Prophect of Chance
*1st-level Luck Domain feature*

You gain proficiency with two gaming set of your choice, and you have advantage on ability checks made to play gaming sets that involve chance.

You also learn the *guidance* cantrip, which doesn't count against the number of cleric cantrips you know.

```
    gamingset = choose("Choose a gaming set: ", tools['gaming'])
    npc.proficiencies.append(gamingset[0])
    gamingset = choose("Choose a gaming set: ", tools['gaming'])
    npc.proficiencies.append(gamingset[0])
    spellcasting.cantripsknown.append('guidance')
```

## Fortune's Blessing
*1st-level Luck Domain feature*

Whenever a creature that you can see within 60 feet of you rolls a 1 or 20 on the d20 for an attack rolL ability check, or saving throw, you can use your reaction to invoke your god's power. You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

Each time you use this feature, you choose one of the following effects:

* **Blessing.** Either you or the creature (your choice) has advantage on one attack rolL ability check, or saving throw of its choice that it makes before the end of its next turn. It chooses to use the blessing before it makes a rolL not after. Once used, the blessing vanishes. 
* **Fortune.** Either you or the creature regains hit points equal to 2 + half your cleric level (your choice).
* **Fumble.** The creature must succeed on a Dexterity saving throw against your cleric spell save DC, or else it is knocked prone, drops what it is holding, and is unable to take reactions until the start of its next turn.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Fortune's Blessing ({npc.WISbonus()}/Recharges on long rest).*** Whenever a creature that you can see within 60 feet of you rolls a 1 or 20 on the d20 for an attack rolL ability check, or saving throw, you invoke your god's power, which provides one of the following effects: **Blessing.** Either you or the creature (your choice) has advantage on one attack rolL ability check, or saving throw of its choice that it makes before the end of its next turn. It chooses to use the blessing before it makes a rolL not after. Once used, the blessing vanishes. **Fortune.** Either you or the creature regains hit points equal to {2 + (npc.classes('Cleric') // 2)} (your choice). **Fumble.** The creature must succeed on a Dexterity saving throw against your cleric spell save DC, or else it is knocked prone, drops what it is holding, and is unable to take reactions until the start of its next turn..") )
```

## Channel Divinity: Blind Luck
*2nd-level Luck Domain feature*

You can use your Channel Divinity to pray for a blessing of miraculous luck.

As a bonus action, you present your holy symbol and pray. Until the end of your next turn, when you make an attack, you can briefly close your eyes and choose to use the blessing. You have advantage on the attack roll and ignore disadvantage for being unable to see the target. If you hit with the attack, the blessing is used up, and if the attack deals any damage, you increase the damage dealt to one target by 2d6 + your cleric level.

```
def level2(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Channel Divinity: Blink Luck.*** You present your holy symbol and pray. Until the end of your next turn, when you make an attack, you can briefly close your eyes and choose to use the blessing. You have advantage on the attack roll and ignore disadvantage for being unable to see the target. If you hit with the attack, the blessing is used up, and if the attack deals any damage, you increase the damage dealt to one target by 2d6 + {npc.levels('Cleric')}.") )
```

## Sense Misfortune
*6th-level Luck Domain feature*

You learn how to recognize the sensation of approaching bad fortune. You have advantage on saving throws against traps and on initiative rolls, and you can't be surprised. In addition, when you are critically hit by an attack, you reduce the damage you take from the attack by an amount equal to your cleric level.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Sense Misfortune.*** You have advantage on saving throws against traps and on initiative rolls, and you can't be surprised. In addition, when you are critically hit by an attack, you reduce the damage you take from the attack by {npc.levels('Cleric')}.") )
```

## Divine Strike
*8th-level Luck Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} damage of the same type dealt by the weapon to the target.") )
```

## In the Zone
*17th-level Luck Domain feature*

You are able to control your lucky streaks with perfect precision. At the start of any of your turns, you can choose to enter into a lucky trance. Until the start of your next turn, you have advantage and ignore disadvantage on all attacks, ability checks, and saving throws, and creatures have disadvantage on saving throws against cleric spells you cast.

Once you use this feature, you cannot use it again until you finish a short or long rest.

```
def level17(npc):
    npc.traits.append("***In the Zone (Recharges on short or long rest.)*** At the start of any of your turns, you can choose to enter into a lucky trance. Until the start of your next turn, you have advantage and ignore disadvantage on all attacks, ability checks, and saving throws, and creatures have disadvantage on saving throws against cleric spells you cast.")
```
