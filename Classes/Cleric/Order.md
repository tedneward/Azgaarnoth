# Divine Domain: Order
The ideal of order is obedience to the law above all else, rather than to a specific individual or the passing influence of emotion or popular rule. Clerics of Order believe that well-crafted laws establish legitimate hierarchies, and those selected by law to lead must be obeyed. Those who obey must do so to the best of their ability, and if those who lead fail to protect the law, they must be replaced. More importantly, law establishes hierarchies. Those selected by the law to lead must be obeyed. Those who obey must do so to the best of their ability. In this manner, law creates an intricate web of obligations that allows society to forge order and security in a chaotic multiverse.

This is a domain granted by the [Alalihatian clerical tradition](../../Religions/AlUma.md#alalihatian-prophecy), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), [Bahamut](../../Religions/Pantheon/Bahamut.md), [Lythtzu](../../Religions/Pantheon/Lythtzu.md), [Maglubiyet](../../Religions/Pantheon/Maglubiyet.md), ...

```
name = 'Order'
description = "***Divine Domain: Order.*** The ideal of order is obedience to the law above all else, rather than to a specific individual or the passing influence of emotion or popular rule. Clerics of Order believe that well-crafted laws establish legitimate hierarchies, and those selected by law to lead must be obeyed. Those who obey must do so to the best of their ability, and if those who lead fail to protect the law, they must be replaced. More importantly, law establishes hierarchies. Those selected by the law to lead must be obeyed. Those who obey must do so to the best of their ability. In this manner, law creates an intricate web of obligations that allows society to forge order and security in a chaotic multiverse."
```

## Domain Spells
*1st-level Order Domain feature* 

You gain domain spells at the cleric levels listed in the Order Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Order Domain Spells**

Cleric Level | Spells
------------ | ------
1st | [command](../../Magic/Spells/command.md), [heroism](../../Magic/Spells/heroism.md)
3rd | [hold person](../../Magic/Spells/hold-person.md), [zone of truth](../../Magic/Spells/zone-of-truth.md)
5th | [mass healing word](../../Magic/Spells/mass-healing-word.md), [slow](../../Magic/Spells/slow.md)
7th | [compulsion](../../Magic/Spells/compulsion.md), [locate creature](../../Magic/Spells/locate-creature.md)
9th | [commune](../../Magic/Spells/commune.md), [dominate person](../../Magic/Spells/dominate-person.md)

```
domainspells = {
    1: ['command', 'heroism'],
    3: ['hold person', 'zone of truth'],
    5: ['mass healing word', 'slow'],
    7: ['compulsion', 'locate creature'],
    9: ['commune', 'dominate person']
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
*1st-level Order Domain feature*

You gain proficiency with heavy armor. You also gain proficiency in the Intimidation or Persuasion skill (your choice). 

```
    for prof in armor['heavy']:
        npc.proficiencies.append(prof)
    npc.proficiencies.append(choose("Choose one: ",['Intimidation', 'Persuasion']))
```

## Voice of Authority
*1st-level Order Domain feature*

You can invoke the power of law to embolden an ally to attack. If you cast a spell with a spell slot of 1st level or higher and target an ally with the spell, that ally can use their reaction immediately after the spell to make one weapon attack against a creature of your choice that you can see. 

If the spell targets more than one ally, you choose the ally who can make the attack. 

```
    npc.traits.append("***Voice of Authority.*** You can invoke the power of law to embolden an ally to attack. If you cast a spell with a spell slot of 1st level or higher and target an ally with the spell, that ally can use their reaction immediately after the spell to make one weapon attack against a creature of your choice that you can see. If the spell targets more than one ally, you choose the ally who can make the attack.")
```

## Channel Divinity: Order's Demand
*2nd-level Order Domain feature*

You can use your Channel Divinity to exert an intimidating presence over others.

As an action, you present your holy symbol, and each creature of your choice that can see or hear you within 30 feet of you must succeed on a Wisdom saving throw or be charmed by you until the end of your next turn or until the charmed creature takes any damage. You can also cause any of the charmed creatures to drop what they are holding when they fail the saving throw.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Order's Demand.*** You present your holy symbol, and each creature of your choice that can see or hear you within 30 feet of you must succeed on a Wisdom saving throw or be charmed by you until the end of your next turn or until the charmed creature takes any damage. You can also cause any of the charmed creatures to drop what they are holding when they fail the saving throw.") )
```

## Embodiment of the Law
*6th-level Order Domain feature*

You have become remarkably adept at channeling magical energy to compel others.

If you cast a spell of the enchantment school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Embodiment of the Law ({npc.WISbonus()}/Recharges on long rest).*** If you cast a spell of the enchantment school using a spell slot of 1st level or higher, you can change the spell's casting time to 1 bonus action for this casting, provided the spell's casting time is normally 1 action.") )
```

## Divine Strike
*8th-level Order Domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 psychic damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} force damage to the target.") )
```

## Order's Wrath
*17th-level Order Domain feature*

Enemies you designate for destruction wilt under the combined efforts of you and your allies. If you deal your Divine Strike damage to a creature on your turn, you can curse that creature until the start of your next turn. The next time one of your allies hits the cursed creature with an attack, the target also takes 2d8 psychic damage, and the curse ends. You can curse a creature in this way only once per turn. 

```
def level17(npc):
    npc.traits.append("***Order's Wrath (1/turn).*** If you deal your Divine Strike damage to a creature on your turn, you can curse that creature until the start of your next turn. The next time one of your allies hits the cursed creature with an attack, the target also takes 2d8 psychic damage, and the curse ends. You can curse a creature in this way only once per turn.")
```
