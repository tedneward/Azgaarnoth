# Divine Domain: Vengeance
There will always be those who have been wronged, robbed, or wounded. So much is lost to greed, treachery, and murder. In a corrupt world, sworn alliances crumble and trust shatters. Some can indulge in the complacency of forgiveness and compassion. For others, this is mere cowardice, a refusal to stand against the tyranny of injustice. When confronted with pain and devastation, the weak settle for acceptance. The strong choose vengeance.

This domain is available to followers of [the Cat Lord](../../Religions/Pantheon/CatLord.md), [the Keeper](../../Religions/Pantheon/Keeper.md), ...

```
name = 'Vengeance'
description = "***Divine Domain: Vengeance.*** There will always be those who have been wronged, robbed, or wounded. So much is lost to greed, treachery, and murder. In a corrupt world, sworn alliances crumble and trust shatters. Some can indulge in the complacency of forgiveness and compassion. For others, this is mere cowardice, a refusal to stand against the tyranny of injustice. When confronted with pain and devastation, the weak settle for acceptance. The strong choose vengeance."
```

## Domain Spells
**Vengeance Domain Spells**

Cleric Level | Spells
------------ | -----
1st | [compelled duel](../../Magic/Spells/compelled-duel.md), [hellish rebuke](../../Magic/Spells/hellish-rebuke.md)
3rd | [see invisibility](../../Magic/Spells/see-invisibility.md), [zone of truth](../../Magic/Spells/zone-of-truth.md)
5th | [bestow curse](../../Magic/Spells/bestow-curse.md), [counterspell](../../Magic/Spells/counterspell.md)
7th | [phantasmal killer](../../Magic/Spells/phantasmal-killer.md), [staggering smite](../../Magic/Spells/staggering-smite.md)
9th | [hold monster](../../Magic/Spells/hold-monster.md), [immolation](../../Magic/Spells/immolation.md)

```
domainspells = {
    1: ['compelled duel', 'hellish rebuke'],
    3: ['see invisibility', 'zone of truth'],
    5: ['bestow curse', 'counterspell'],
    7: ['phantasmal killer', 'staggering smite'],
    9: ['hold monster', 'immolation']
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
*1st-level Vengeance domain feature*

You gain proficiency with martial weapons and the Intimidation skill.

```
    npc.proficiencies.append('Intimidation')
    for prof in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(prof)
```

## Divine Retribution
*1st-level Vengeance domain feature*

You can psychically rebuke attackers. When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to force the creature to make an Intelligence saving throw. The creature takes 2d8 psychic damage on a failed save, and half as much damage on a successful one.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Divine Retribution ({npc.WISbonus()}).*** When a creature within 5 feet of you that you can see hits you with an attack, you can use your reaction to force the creature to make an Intelligence saving throw. The creature takes 2d8 psychic damage on a failed save, and half as much damage on a successful one.") )
```

## Channel Divinity: Marked for Vengeance
*2nd-level Vengeance domain feature*

You learn how to mark a creature as the target of your vengeance. With a bonus action, you place a magical mark on a creature within 30 feet of you that you can see. While marked, the creature takes an additional 1d8 psychic damage from your attacks, spells and Divine Retribution feature. The mark lasts until you dismiss it (requiring no action) or until the creature dies. Only one creature can be marked at a time― if you recast it, the current mark disappears.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
def level2(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Channel Divinity: Marked for Vengeance ({npc.WISbonus()}/Recharges on long rest).*** You place a magical mark on a creature within 30 feet of you that you can see. While marked, the creature takes an additional 1d8 psychic damage from your attacks, spells and Divine Retribution feature. The mark lasts until you dismiss it (requiring no action) or until the creature dies. Only one creature can be marked at a time― if you recast it, the current mark disappears.") )
```

## Nowhere to Hide
*6th-level Vengeance domain feature*

You learn how to locate the target of your vengeance. After spending 10 minutes in prayer, you learn the location of a creature that is marked with your Marked for Vengeance ability. When the targets location is revealed, you are aware of the general direction and distance to the marked target. When you are within 120 feet of the target, you know its exact location.

```
def level6(npc):
    npc.traits.append("***Nowhere to Hide.*** After spending 10 minutes in prayer, you learn the location of a creature that is marked with your Marked for Vengeance ability. When the targets location is revealed, you are aware of the general direction and distance to the marked target. When you are within 120 feet of the target, you know its exact location.")
```

## Swift Retribution
*8th-level Vengeance domain feature*

When you or an ally that you can see within 30 feet of you, is hit by an attack from a creature you have marked with your Marked for Vengeance ability, you can strike them down with the wrath of your deity. When the creature hits you or your ally, you can use your reaction to deal 1d8 psychic damage to the target. At 14th level, this damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Swift Retribution.*** When you or an ally that you can see within 30 feet of you, is hit by an attack from a creature you have marked with your Marked for Vengeance ability, you can strike them down with the wrath of your deity. When the creature hits you or your ally, you can use your reaction to deal {'1d8' if npc.levels('Cleric') < 14 else '2d8'} psychic damage to the target.") )
```

## Vengeful Divinity
*17th-level Vengeance domain feature*

You are a true bane to your marks. Once per long rest, while a creature is marked, you can become an Angel of Vengeance. While transformed, you gain spectral wings (any armor or clothing you're wearing is unaffected), which grant you a flying speed of 60 feet. While you have your wings deployed and are not in the air, you can use your wings as a shield if you aren't wielding one already. You can add half of your Wisdom modifier to your AC (rounded down, with a minimum of +1).

Additionally, while in this form, if a creature you've marked deals damage to you, you can force them to have disadvantage on their next saving throw against a spell you cast that deals damage as a bonus action.

This form lasts for 1 hour, and during this time you can freely deploy or hide your wings, requiring no action.

```
def level17(npc):
    npc.defer(lambda npc: npc.traits.append("***Vengeful Divinity (Recharges on long rest).*** While a creature is marked, you can become an Angel of Vengeance. While transformed, you gain spectral wings (any armor or clothing you're wearing is unaffected), which grant you a flying speed of 60 feet. While you have your wings deployed and are not in the air, you can use your wings as a shield if you aren't wielding one already. You can add {npc.WISbonus() // 2} to your AC. Additionally, while in this form, if a creature you've marked deals damage to you, you can force them to have disadvantage on their next saving throw against a spell you cast that deals damage as a bonus action. This form lasts for 1 hour, and during this time you can freely deploy or hide your wings, requiring no action.") )
```
