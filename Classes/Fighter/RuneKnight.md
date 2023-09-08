# Martial Archetype: Rune Knight
You discovered how to enhance your martial prowess using the supernatural power of [runes](../../Magic/Runes.md). You likely learned your methods first or second hand from one of the few who know how to scribe such runes, or found an ancient rune carved into a hill or cave. In time, you learned how to carve and apply runes to your equipment and how to invoke their magic, ultimately becoming a Rune Knight.

> Rune Knights either have in the past or will in the future run into or work with the [School of the Eldar](../../Organizations/MageSchools/SchoolOfTheEldar.md) at some point in their career. In fact, it's highly likely that even if the Rune Knight hasn't directly met up with a member of that school, the school has had the Rune Knight under observation and simply chosen not to approach.

```
name = 'Rune Knight'
description = "You discovered how to enhance your martial prowess using the supernatural power of runes. You likely learned your methods first or second hand from one of the few who know how to scribe such runes, or found an ancient rune carved into a hill or cave. In time, you learned how to carve and apply runes to your equipment and how to invoke their magic, ultimately becoming a Rune Knight."
```


## Bonus Proficiencies
*3rd-level Rune Knight feature*

You gain proficiency with smith's tools, and you learn to speak, read, and write Giant.

```
def level3(npc):
    npc.proficiencies.append("Smith's tools")
    npc.languages.append("Giant")
```

## Rune Carver
*3rd-level Rune Knight feature*

You can use magic runes to enhance your gear. You can inscribe up to two runes of your choice, from among the [list below](#runes), and each time you gain a level in this class, you can replace one rune you know with a different one from this feature. When you reach certain levels in this class, you learn additional runes, as shown in the Runes Known table.

**Runes Inscribed**

Fighter Level|Number of Runes
-------------|---------------
3rd | 2
7th | 3
10th| 4
15th| 5

Whenever you finish a long rest, you can touch a number of objects equal to the number of runes you know, and you inscribe a different rune onto each of the objects. To be eligible, an object must be a weapon, a suit of armor, a shield, a piece of jewelry, or something else you can wear or hold in a hand. Your rune remains on an object until you finish a long rest, and an object can bear only one of your runes at a time. You can only have up to the number of runes given in the table inscribed at a time; any additional runes beyond that number will fade away, leaving no trace of their passing.

If a rune requires a saving throw, your Rune Magic save DC equals 8 + your proficiency bonus + your Constitution modifier.

```
    npc.defer(lambda npc: npc.traits.append("***Rune Carver (Recharges on long rest).*** You can touch a number of objects equal to {'twice ' if npc.levels('Fighter') >= 15}the number of runes you know, and you inscribe a different rune onto each of the objects. To be eligible, an object must be a weapon, a suit of armor, a shield, a piece of jewelry, or something else you can wear or hold in a hand. Your rune remains on an object until you finish a long rest, and an object can bear only one of your runes at a time. You can only have up to the number of runes given in the table inscribed at a time; any additional runes beyond that number will fade away, leaving no trace of their passing. If a rune requires a saving throw, your Rune Magic save DC equals {8 + npc.proficiencybonus() + CONbonus()}."))
```

### Runes
**Skye (Cloud).** This rune channels deception and trickery and misdirection. While wearing or carrying an object inscribed with this rune, you have advantage on Dexterity (Sleight of Hand) checks and Charisma (Deception) checks.

In addition, when you or a creature you can see within 30 feet of you is hit by an attack roll, you can use your reaction to invoke the rune and choose a different creature within 30 feet of you, other than the attacker. The chosen creature becomes the target of the attack, using the same roll. This magic can transfer the attack's effects regardless of the attack's range. Once you invoke this rune, you can't do so again until you finish a short or long rest.

**Ild (Fire).** This rune's magic channels the masterful craftsmanship of great smiths. While wearing or carrying an object inscribed with this rune, your proficiency bonus is doubled for any ability check you make that uses your proficiency with a tool.

In addition, when you hit a creature with an attack using a weapon, you can invoke the rune to summon fiery shackles: the target takes an extra 2d6 fire damage, and it must succeed on a Strength saving throw or be restrained for 1 minute. While restrained by the shackles, the target takes 2d6 fire damage at the start of each of its turns. The target can repeat the saving throw at the end of each of its turns, banishing the shackles on a success. Once you invoke this rune, you can't do so again until you finish a short or long rest.

**Isa (Frost).** This rune's magic evokes the might of those who survive in the wintry wilderness. While wearing or carrying an object inscribed with this rune, you have advantage on Wisdom (Animal Handling) checks and Charisma (Intimidation) checks.

In addition, you can invoke the rune as a bonus action to increase your sturdiness. For 10 minutes, you gain a +2 bonus to all ability checks and saving throws that use Strength or Constitution. Once you invoke this rune, you can't do so again until you finish a short or long rest.

**Haug (Resilience).** *(Prerequisite: 7th Level or higher Rune Knight)* This rune's magic bestows resilience and fortitude. While wearing or carrying an object that bears this rune, you have advantage on saving throws against being poisoned, and you have resistance against poison damage.

In addition, you can invoke the rune as a bonus action, gaining resistance to bludgeoning, piercing, and slashing damage for 1 minute. Once you invoke this rune, you can't do so again until you finish a short or long rest.

**Stein (Stone).** This rune's magic channels the judiciousness and wisdom. While wearing or carrying an object inscribed with this rune, you have advantage on Wisdom (Insight) checks, and you have darkvision out to a range of 120 feet. 

In addition, when a creature you can see ends its turn within 30 feet of you, you can use your reaction to invoke the rune and force the creature to make a Wisdom saving throw. Unless the save succeeds, the creature is charmed by you for 1 minute. While charmed in this way, the creature has a speed of 0 and is incapacitated, descending into a dreamy stupor. The creature repeats the saving throw at the end of each of its turns, ending the effect on a success. Once you invoke this rune, you can't do so again until you finish a short or long rest.

**Uvar (Storm).** *(Prerequisite: 7th Level or higher Rune Knight)* Using this rune, you can glimpse the future like a seer. While wearing or carrying an object inscribed with this rune, you have advantage on Intelligence (Arcana) checks, and you can't be surprised as long as you aren't incapacitated.

In addition, you can invoke the rune as a bonus action to enter a prophetic state for 1 minute or until you're incapacitated. Until the state ends, when you or another creature you can see within 60 feet of you makes an attack roll, a saving throw, or an ability check, you can use your reaction to cause the roll to have advantage or disadvantage. Once you invoke this rune, you can't do so again until you finish a short or long rest. 


## Rune's Might
*3rd-level Rune Knight feature*

You have learned how to imbue yourself with the power of runes. As a bonus action, you magically gain the following benefits, which last for 1 minute:

* If you are smaller than Large, you become Large, along with anything you are wearing. If you lack the room to become Large, your size doesn't change.
* You have advantage on Strength checks and Strength saving throws.
* Once on each of your turns, one of your attacks with a weapon or an unarmed strike can deal an extra ld6 damage to a target on a hit.

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses of it when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append("***Rune's Might ({npc.proficiencybonus()}/Recharges on {'short or ' if npc.levels('Fighter') >= 15}long rest).*** You have learned how to imbue yourself with the power of runes. As a bonus action, you magically gain the following benefits, which last for 1 minute: {'* You become Large, along with anything you are wearing.\n' if (npc.size == 'Tiny' or npc.size == 'Small' or npc.size == 'Medium') else ''}* You have advantage on Strength checks and Strength saving throws.\n* Once on each of your turns, one of your attacks with a weapon or an unarmed strike can deal an extra {'1d6' if npc.levels('Fighter') < 7 else '1d8' if npc.levels('Fighter') < 18 else '1d10'} damage to a target on a hit.") )
```

## Runic Shield
*7th-level Rune Knight feature*

You learn to invoke your rune magic to protect your allies. When another creature you can see within 60 feet of you is hit by an attack roll, you can use your reaction to force the attacker to reroll the d20 and use the new roll. 

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
def level7(npc):
    npc.defer(lambda npc: npc.reactions.append("***Runic Shield ({npc.proficiencybonus()}/Recharges on long rest).*** When another creature you can see within 60 feet of you is hit by an attack roll, you can use your reaction to force the attacker to reroll the d20 and use the new roll."))
```

## Great Stature
*10th-level Rune Knight feature*

The magic of your runes permanently alters you. When you gain this feature, roll 3d4. You grow a number of inches in height equal to the roll. Morepver, the extra damage you deal with your Rune's Might feature increases to 1d8.

```
def level10(npc):
    npc.traits.append("***Great Stature.*** You are 3d4 inches taller than you were at level 1.")
```

## Master of Runes
*15th-level Rune Knight feature*

You can invoke each rune you know from your Rune Carver feature twice, rather than once, and you regain all expended uses when you finish a short or long rest.

## Runic Juggernaut
*18th-level Rune Knight feature*

You learn how to amplify your rune-powered transformation. As a result, the extra damage you deal with the Rune's Might feature increases to 1d10. Moreover, when you use that feature, your size can increase to Huge, and while you are that size, your reach increases by 5 feet.

```
def level18(npc):
    npc.traits.append("***Runic Juggernaut.*** When you use your Runic Might, your size can increase to Huge, and while you are that size, your reach increases by 5 feet.")
```