# Divine Domain: Protection
The protection domain is the purview of deities who charge their followers to shield the weak from the strong. The gods’ faithful dwell in villages and towns on the borderlands, where they help bolster defenses and seek out evils to defeat. These gods believe that a strong shield and a suit of armor is the best defense against evil, second only to a stout mace on hand to respond to any attacks in kind.

This is a domain available to followers of the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric), the [Kaevarian Church](../../Religions/KaevarianChurch.md), [Trinitarians who worship Sor](../../Religions/Trinitarian.md#sor), [Bahamut](../../Religions/Pantheon/Bahamut.md), [Ehlonna](../../Religions/Pantheon/Ehlonna.md), [Lathander](../../Religions/Pantheon/Lathander.md), [Lugh](../../Religions/Pantheon/Lugh.md), ...

```
name = 'Protection'
description = "***Divine Domain: Protection.*** The protection domain is the purview of deities who charge their followers to shield the weak from the strong. The gods’ faithful dwell in villages and towns on the borderlands, where they help bolster defenses and seek out evils to defeat. These gods believe that a strong shield and a suit of armor is the best defense against evil, second only to a stout mace on hand to respond to any attacks in kind."
```

## Domain Spells
Starting at 1st level, you gain domain spells at the cleric levels listed in the Protection Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Protection Domain Spells**

Cleric Level |	Spells
------------ | -----
1st	| [compelled duel](../../Magic/Spells/compelled-duel.md), [protection from evil and good](../../Magic/Spells/protection-from-evil-and-good.md)
3rd	| [aid](../../Magic/Spells/aid.md), [protection from poison](../../Magic/Spells/protection-from-poison.md)
5th	| [protection from energy](../../Magic/Spells/protection-from-energy.md), [slow](../../Magic/Spells/slow.md)
7th	| [guardian of faith](../../Magic/Spells/guardian-of-faith.md), [Otiluke's resilient sphere](../../Magic/Spells/otilukes-resilient-sphere.md)
9th	| [antilife shell](../../Magic/Spells/antilife-shell.md), [wall of force](../../Magic/Spells/wall-of-force.md)

```
domainspells = {
    1: ['compelled duel', 'protection from evil and good'],
    3: ['aid', 'protection from poison'],
    5: ['protection from energy', 'slow'],
    7: ['guardian of faith', 'otilukes resilient sphere'],
    9: ['antilife shell', 'wall of force']
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
*1st-level Protection domain feature*

You gain proficiency with heavy armor.

```
    for prof in armor['heavy']:
        npc.proficiencies.append(prof)
```

## Shield of the Faithful
*1st-level Protection domain feature*

You gain the ability to hinder attacks intended for others. When a creature attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. To do so, you must be able to see both the attacker and the target. You interpose an arm, a shield, or some other part of yourself to try to throw the attack off target.

```
    npc.reactions.append("***Shield of the Faithful.*** When a creature attacks a target other than you that is within 5 feet of you, you impose disadvantage on the attack roll. To do so, you must be able to see both the attacker and the target. You interpose an arm, a shield, or some other part of yourself to try to throw the attack off target.")
```

## Channel Divinity: Radiant Defense
*2nd-level Protection domain feature*

You can use your Channel Divinity to cloak your allies in radiant armor.

As an action, you channel blessed energy into an ally that you can see within 30 feet of you. The first time that ally is hit by an attack within the next minute, the attacker takes radiant damage equal to 2d10 + your cleric level.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Radiant Defense.*** You channel blessed energy into an ally that you can see within 30 feet of you. The first time that ally is hit by an attack within the next minute, the attacker takes radiant damage equal to 2d10 + {npc.levels('Cleric')}.") )
```

## Blessed Healer
*6th-level Protection domain feature*

The healing spells you cast on others can heal you as well. When you cast a spell with a spell slot and it restores hit points to any creature other than you this turn, you regain hit points equal to 2 + the spell's level.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Blessed Healer.*** When you cast a spell with a spell slot and it restores hit points to any creature other than you this turn, you regain 2 + {npc.levels('Cleric')} hit points.") )
```

## Divine Strike
*8th-level Protection domain feature*

You gain the ability to infuse your weapon strikes with divine energy. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 radiant damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} radiant damage to the target."))
```

## Indomitable Defense
*17th-level Protection domain feature*

You gain resistance to two damage types of your choice, choosing from bludgeoning, necrotic, piercing, radiant, and slashing. Whenever you finish a short or long rest, you can change the damage types you chose.

As an action, you can temporarily give up this resistance and transfer it to one creature you touch. The creature keeps the resistance until the end of your next short or long rest or until you transfer it back to yourself as a bonus action.

```
def level17(npc):
    npc.traits.append("***Indomitable Defense.*** Whenever you finish a short or long rest, you gain resistance to two damage types of your choice, choosing from bludgeoning, necrotic, piercing, radiant, and slashing.")
    npc.actions.append("***Indomitable Defense.*** You can temporarily give up your Indomitable Defense resistance and transfer it to one creature you touch. The creature keeps the resistance until the end of your next short or long rest or until you transfer it back to yourself as a bonus action.")
```
