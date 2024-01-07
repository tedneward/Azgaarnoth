# Arcane Tradition: Arcanist
Arcanists are those wizards who, rather than pursue an arcane tradition specific to an area of magic or pursuit of study, choose instead to dedicate their time and energy to the [mage school](../../Organizations/MageSchools/index.md) in which they are a member. (Arcanists are always members of a mage school; should they lose their membership for some reason, they must immediately join a new school, or lose some of their particular traits, at the DM's discretion.)

The [White Winds](../../Organizations/MageSchools/WhiteWinds.md) were the first to use arcanists, and remain by far the most common source of arcanists in Azgaarnoth.

```
name = 'Arcanist'
description = "***Arcane Tradition: Arcanist.*** Arcanists are those wizards who, rather than pursue an arcane tradition specific to an area of magic or pursuit of study, choose instead to dedicate their time and energy to the mage school in which they are a member. In addition to the usual membership benefits within the school, arcanists have found ways to harness the collective arcane power of the organization."
```

## Arcanist's Privileges
*2nd-level Arcanist feature*

Your willingness to contribute to the whole at large (that is, the mage school to which you belong) grants you prestige and insight when interacting with other spellcasters, granting you the following benefits:

* Whenever you gain a wizard level, in addition to the normal spells you learn, you can choose one extra wizard spell of a level you can cast (preferably of the school's unique spell list, if any) and copy it into your spellbook for half the usual price in gold.
* You gain a bonus on all your Charisma checks to interact with other spellcasters, equal to half your Intelligence modifier (minimum 1).

In exchange for these benefits, you must pay dues (typically 10 gp per month) to the guild, and if you have spent at least 1 day of downtime in the past month, you must spend 1 additional downtime day to maintain your guild duties. If you miss payments, you must make up back dues (in both gold and in downtime, if applicable) to remain in your guild's good graces. If you are behind on payments, you do not enjoy any of the benefits of this feature. 

When you reach 14th level in your wizard class, you no longer need to pay these dues in gold or downtime, and can always use this feature's benefits, whether or not you have paid for them.

```
def level2(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Arcanist's Privileges.*** You gain a +{(npc.INTbonus + 1) // 2} bonus on all your Charisma checks to interact with other spellcasters.") )
```

## Arcanist's Grimoire
*2nd-level Arcanist feature*

Your spellbook not only contains your spells, but special notes, mental exercises, and anecdotes from your school's history to help you use magic more effectively in particular situations. During your turn, immediately after you use your action to cast a spell of 1st level or higher, if that spell is particular to your school, you can use a bonus action to reroll either a number of the damage dice up to your Intelligence modifier (minimum of 1), or a target creature's saving throw, or your own. You must use the new rolls.

You can use this feature a number of times equal to your Intelligence modifier (minimum of once), regaining all expended uses when you finish a long rest.

In addition, a copy of your spellbook is always available at any tower of your mage school.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Arcanist's Grimoire ({npc.INTbonus}/Recharges on long rest).*** Immediately after you use your action to cast a spell of 1st level or higher, if that spell is particular to your school, you reroll either up to {npc.INTbonus()} of the damage dice, or a target creature's saving throw, or your own. You must use the new rolls.") )
```

## Guild Proficiencies
*2nd-level Arcanist feature*

You gain expertise with the Arcana skill, which means your proficiency bonus is doubled for any ability check you make with it.

```
    npc.expertises.append("Arcana")
```

## Signature Training
*6th-level Arcanist feature*

You can employ an impressive spellcasting technique that is either distinctive to your guild, or your own method for distinguishing yourself within it. When you use your action to cast a spell of 3rd-level or higher that you prepared from your spellbook, you can use your bonus action to cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw against your spell save DC. On a failed save, the creature is charmed or frightened by you (your choice) until the end of your next turn. You can use this feature once, regaining the ability to do so the next time you make an ability check for initiative.

```
def level6(npc):
    npc.bonusactions.append("***Signature Training (Recharges on Initiative die roll).*** When you use your action to cast a spell of 3rd-level or higher that you prepared from your spellbook, you cause each creature in a 10-foot cube originating from you to make a Wisdom saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}). On a failed save, the creature is charmed or frightened by you (your choice) until the end of your next turn.")
```

## Spellpool
*10th-level Arcanist feature*

When you prepare your spells each day, you can make use of a spellpool, a magical reservoir of spells that can be drawn upon by members of your wizardly guild or magical academy. 

The first time you look to take advantage of this feature, you must first perform a 1-minute ritual with a spellcasting focus, adding a spiraling pattern of sigils to that spellcasting focus using 25 gp worth of copper wire. If you lose this spellcasting focus, you must repeat this ritual with a new focus.

This specially prepared arcane focus allows you to access the spellpool. You can perform this ritual on as many spellcasting foci as you wish, but once a focus is prepared by a particular wizard, any wizard can attune and use it to access the spellpool. (For this reason, loss of such an augmented spell focus is a very deep concern for any mage school, and discovery of a school's spellpool foci in the hands of a non-member will spark extraordinary efforts to retrieve it, legally or otherwise.)

When accessing the spellpool, you attempt to prepare a spell that is not in your spellbook. Each time you try to prepare a spell in this way, you must check first to see if the desired spell is available, using your action to roll an Intelligence (Arcana) check against a DC equal to 10 + twice the spell's level. You must be holding your specially prepared spellcasting focus when you do so. To check for a spell, you must already have a spell of the same level or higher in your spellbook. You can check to see if any spell (from any class spell list) is available, as long as you know it exists, but if a spell you check for is not on the wizard spell list, the DC of the Intelligence (Arcana) check increases by 5. If you are not currently on the same plane of existence as any of the locations where your institution is based, you make the check with disadvantage.

Once you have successfully checked that a spell is available, until the next time you finish a long rest you can prepare it just as if it were in your spellbook. If the spell is not available, you must finish a long rest before you can attempt to prepare that particular spell using this feature again. There is no limit to the number of spells you can search for in this manner, but each spell you search for requires you to use an action to make a separate Intelligence (Arcana) check. The maximum number of spells you can prepare with this feature at one time is equal to half your Intelligence modifier (rounded up, minimum of 1).

For each spell you prepare with this feature, you must choose one spell of the same level or higher from your spellbook and loan it to the spellpool. A spell you loan in this way is lost from your spellbook until the next time you finish a long rest, at which time it reappears in your spellbook, exactly as it was before. You cannot loan a spell you currently have prepared.

When you cast a spell you prepared via the spellpool, it is cast normally, with all the necessary components and other requirements.

All spells prepared using the spellpool return to the spellpool the next time you finish a long rest. Having successfully prepared a spell with this feature before does not allow you to prepare it with this feature again, nor does it alter your chances of finding that same spell available the next time you search for it.

```
def level10(npc):
    npc.traits.append("***Spellpool.***")
```

## Master of Wizardry
*14th-level Arcanist feature*

Having spent so much time interacting with other mages, you can quickly analyze their casting and seek to counter it. When a spell cast by another creature you can see allows you to make a saving throw to take only half damage, if you succeed on the saving throw, you can expend a wizard spell slot of 1st-level or higher as a reaction to instead take no damage at all.

In addition, when you this feature, you can instead choose to reflect the spell back on the caster. When you do so, as part of the same reaction, you cause the spell to target its caster instead of you, and the caster makes its own saving throw against the same DC. If the spell you are trying to reflect is 6th-level or higher this ability fails. After you use this feature to reflect a spell you cannot use it again until you finish a long rest.

```
def level14(npc):
    npc.reactions.append("***Master of Wizardry (Reflect recharges on long rest).*** When a spell cast by another creature you can see allows you to make a saving throw to take only half damage, if you succeed on the saving throw, you can expend a wizard spell slot of 1st-level or higher to instead take no damage at all. In addition, when you this feature, you can instead choose to reflect the spell back on the caster. When you do so, as part of the same reaction, you cause the spell to target its caster instead of you, and the caster makes its own saving throw against the same DC. If the spell you are trying to reflect is 6th-level or higher this ability fails.")
```
