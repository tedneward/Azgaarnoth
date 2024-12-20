# Divine Domain: Desire
Gods and Goddesses of the Desire Domain take many forms, but all wield power over the feeling of raw desire, whether it be desire for money, food, fame, love, drugs, or even darker delights.

This domain is available to [Trinitarians who worship Leriya](../../Religions/Trinitarian.md#leriya), [Lythtzu](../../Religions/Pantheon/Lythtzu.md), [Melil](../../Religions/Pantheon/Milil.md), ...

```
name = 'Desire'
description = "***Divine Domain: Desire.*** Gods and Goddesses of the Desire Domain take many forms, but all wield power over the feeling of raw desire, whether it be desire for money, food, fame, love, drugs, or even darker delights."
```

**DESIRE DOMAIN SPELLS**

Cleric Level|Spells
------------|------
1st|[charm person](../../Magic/Spells/charm-person.md), [command](../../Magic/Spells/command.md)
3rd|[enthrall](../../Magic/Spells/enthrall.md), [locate object](../../Magic/Spells/locate-object.md)
5th|[excite emotions](../../Magic/Spells/excite-emotions.md), [vampiric touch](../../Magic/Spells/vampiric-touch.md)
7th|[charm monster](../../Magic/Spells/charm-monster.md), [compulsion](../../Magic/Spells/compulsion.md)
9th|[dominate person](../../Magic/Spells/dominate-person.md), [geas](../../Magic/Spells/geas.md)

```
domainspells = {
    1: ['charm person', 'command'],
    3: ['enthrall', 'locate object'],
    5: ['excite emotions', 'vampiric touch'],
    7: ['charm monster', 'compulsion'],
    9: ['dominate person', 'geas']
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

## Honeyed Words
*1st-level Desire Domain feature*

When you choose this domain at 1st level you learn the [friends](../../Magic/Spells/friends.md) and [vicious mockery](../../Magic/Spells/vicious-mockery.md) cantrips, which don't count against the number of cleric cantrips you know.

You also gain proficiency in one of the following skills of your choice: Deception, Performance, or Persuasion.

```
    spellcasting.cantripsknown.append('friends')
    spellcasting.cantripsknown.append('vicious mockery')

    prof = choose("Choose one: ", ['Deception', 'Performance', 'Persuasion'])
    npc.proficiencies.append(prof)
```

## Disarming Appeal
*1st-level Desire Domain feature*

You gain the ability to hamper your enemies with blessed charm. When a creature within 15 feet of you that you can see targets you with an attack but before the attack roll you can use your reaction to attempt to beguile it.

The attacker must make a Wisdom saving throw. On a failed saving throw, the triggering attack misses, and the attacker cannot attack you until the end of your next turn. An attacker that can't be charmed is immune to this feature.

You can use this feature a number of times equal to your Wisdom modifier (a minimum of once). You regain all expended uses when you finish a long rest.

```
    def disarmingappeal(npc):
        if npc.levels('Cleric') >= 17:
            npc.reactions.append(f"***Disarming Appeal.*** When a creature within 15 feet of you that you can see targets you with an attack but before the attack roll you can use your reaction to attempt to beguile it. The attacker must make a Wisdom saving throw. On a failed saving throw, the triggering attack misses, and the attacker cannot attack you until the end of your next turn. An attacker that can't be charmed is immune to this feature.  When you use this against a humanoid that can hear you and shares a language with you, you can make your choice of a Charisma (Persuasion) or Charisma (Deception) check contested by a Wisdom (Insight) check. If you win the contest, the target has disadvantage on their saving throw against the triggering class feature.")
        elif npc.levels('Cleric') >= 8:
            npc.reactions.append(f"***Disarming Appeal ({npc.WISbonus()}/Recharges on long rest).*** When a creature within 15 feet of you that you can see targets you with an attack but before the attack roll you can use your reaction to attempt to beguile it. The attacker must make a Wisdom saving throw. On a failed saving throw, the triggering attack misses, and the attacker cannot attack you until the end of your next turn. An attacker that can't be charmed is immune to this feature.  When you use this against a humanoid that can hear you and shares a language with you, you can make your choice of a Charisma (Persuasion) or Charisma (Deception) check contested by a Wisdom (Insight) check. If you win the contest, the target has disadvantage on their saving throw against the triggering class feature.")
        else:
            npc.reactions.append(f"***Disarming Appeal ({npc.WISbonus()}/Recharges on long rest).*** When a creature within 15 feet of you that you can see targets you with an attack but before the attack roll you can use your reaction to attempt to beguile it. The attacker must make a Wisdom saving throw. On a failed saving throw, the triggering attack misses, and the attacker cannot attack you until the end of your next turn. An attacker that can't be charmed is immune to this feature.")

    npc.defer(lambda npc: disarmingappeal(npc) )
```

## Channel Divinity: Charm of the Gods
*2nd-level Desire Domain feature*

You can use your channel divinity to briefly change what another creature deeply wants. As an action, you choose one creature that you can see within 30 feet of you. That creature must make a Wisdom saving throw.

On a failed saving throw, the target is charmed by you until the start of your next turn. While it is charmed in this way, you can dictate how the target takes its turns. For example, you can designate a location that the creature must try to move toward, or you can designate another creature that the target must take hostile action toward. The target will not take obviously lethal action such as walking off a cliff, jumping into lava, or engaging a pit fiend in single combat. If it is forced to attack its allies, the attack has disadvantage.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Charm of the Gods.*** You choose one creature that you can see within 30 feet of you. That creature must make a Wisdom saving throw. On a failed saving throw, the target is charmed by you until the start of your next turn. While it is charmed in this way, you can dictate how the target takes its turns. For example, you can designate a location that the creature must try to move toward, or you can designate another creature that the target must take hostile action toward. The target will not take obviously lethal action such as walking off a cliff, jumping into lava, or engaging a pit fiend in single combat. If it is forced to attack its allies, the attack has disadvantage.{' When you use this against a humanoid that can hear you and shares a language with you, you can make your choice of a Charisma (Persuasion) or Charisma (Deception) check contested by a Wisdom (Insight) check. If you win the contest, the target has disadvantage on their saving throw against the triggering class feature.' if npc.levels('Cleric') >= 8 else ''}") )
```

## One Man's Trash
*6th-level Desire Domain feature*

Your deity grants you the uncanny ability to sense that which people value and desire. You know when an object worth 200gp or more is within 60 feet of you, and you know how many. This does not inform you of the location or full value of the object or objects.

```
def level6(npc):
    npc.traits.append("***One Man's Trash.*** You know when an object worth 200gp or more is within 60 feet of you, and you know how many. This does not inform you of the location or full value of the object or objects.")
```

## An Offer You Can't Refuse
*6th-level Desire Domain feature*

You gain the ability to strengthen your divine magic by using nothing more than your words to weaken your enemies' resolve.

When you use your [Disarming Appeal](#disarming-appeal) or [Charm of the Gods](#charm-of-the-gods) class features against a humanoid that can hear you and shares a language with you, you can make your choice of a Charisma (Persuasion) or Charisma (Deception) check contested by the target's Wisdom (Insight) check. If you win the contest, the target has disadvantage on their saving throw against the triggering class feature.

## Potent Spellcasting
*8th-level Desire Domain feature*

You add your Widsom modifier to the damage you deal with any cleric cantrip.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Potent Spellcasting.*** You add {npc.WISbonus()} to the damage you deal with any cleric cantrip.") )
```

## Untouchable
*17th-level Desire Domain feature*

You can use your [Disarming Appeal](#disarming-appeal) class feature an unlimited number of times without having to rest, though it still requires you to use your reaction.

