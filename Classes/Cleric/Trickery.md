# Divine Domain: Trickery
Gods of trickery are mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They're patrons of thieves, scoundrels, gamblers, rebels, and liberators. Their clerics are a disruptive force in the world, puncturing pride, mocking tyrants, stealing from the rich, freeing captives, and flouting hollow traditions. They prefer subterfuge, pranks, deception, and theft rather than direct confrontation.

This domain is available to followers of [the Cat Lord](../../Religions/Pantheon/CatLord.md), [Cyric](../../Religions/Pantheon/Cyric.md), [Melil](../../Religions/Pantheon/Milil.md), [the Traveler](../../Religions/Pantheon/Traveler.md), [Tiamat](../../Religions/Pantheon/Tiamat.md), ...

```
name = 'Trickery'
description = "***Divine Domain: Trickery.*** Gods of trickery are mischief-makers and instigators who stand as a constant challenge to the accepted order among both gods and mortals. They're patrons of thieves, scoundrels, gamblers, rebels, and liberators. Their clerics are a disruptive force in the world, puncturing pride, mocking tyrants, stealing from the rich, freeing captives, and flouting hollow traditions. They prefer subterfuge, pranks, deception, and theft rather than direct confrontation."
```

## Domain Spells
*1st-level Trickery domain feature*

You gain domain spells at the cleric levels listed in the Unity Domain Spells table. Once you gain a domain spell, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you have a domain spell that doesn't appear on the cleric spell list, the spell is nonetheless a cleric spell for you.

**Trickery Domain Spells**

Cleric Level |	Spells
------------ | -----
1st |	[charm person](../../Magic/Spells/charm-person.md), [disguise self](../../Magic/Spells/disguise-self.md)
3rd	| [mirror image](../../Magic/Spells/mirror-image.md), [pass without trace](../../Magic/Spells/pass-without-trace.md)
5th	| [blink](../../Magic/Spells/blink.md), [dispel magic](../../Magic/Spells/dispel-magic.md)
7th	| [dimension door](../../Magic/Spells/dimension-door.md), [polymorph](../../Magic/Spells/polymorph.md)
9th	| [dominate person](../../Magic/Spells/dominate-person.md), [modify memory](../../Magic/Spells/modify-memory.md)

```
domainspells = {
    1: ['charm person', 'disguise self'],
    3: ['mirror image', 'pass without trace'],
    5: ['blink', 'dispel magic'],
    7: ['dimension door', 'polymorph'],
    9: ['dominate person', 'modify memory']
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

## Blessing of the Trickster
*1st-level Trickery domain feature*

You can use your action to touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again.

```
    npc.actions.append("***Blessing of the Trickster.*** You touch a willing creature other than yourself to give it advantage on Dexterity (Stealth) checks. This blessing lasts for 1 hour or until you use this feature again.")
```

## Channel Divinity: Invoke Duplicity
*2nd-level Trickery domain feature*

You can use your Channel Divinity to create an illusory duplicate of yourself.

As an action, you create a perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you.

For the duration, you can cast spells as though you were in the illusion's space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target.

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Invoke Duplicity.*** You create {'a' if npc.levels('Cleric') < 17 else 'up to four'} perfect illusion of yourself that lasts for 1 minute, or until you lose your concentration (as if you were concentrating on a spell). The illusion appears in an unoccupied space that you can see within 30 feet of you. As a bonus action on your turn, you can move the illusion up to 30 feet to a space you can see, but it must remain within 120 feet of you. For the duration, you can cast spells as though you were in the illusion's space, but you must use your own senses. Additionally, when both you and your illusion are within 5 feet of a creature that can see the illusion, you have advantage on attack rolls against that creature, given how distracting the illusion is to the target.") )
    npc.defer(lambda npc: npc.bonusactions.append("***Improved Duplicity.*** You can move any number of your illusory duplicates up to 30 feet, to a maximum range of 120 feet.") )
```

## Channel Divinity: Cloak of Shadows
*6th-level Trickery domain feature*

You can use your Channel Divinity to vanish.

As an action, you become invisible until the end of your next turn. You become visible if you attack or cast a spell.

```
def level6(npc):
    npc.actions.append("***Channel Divinity: Cloak of Shadows.*** You become invisible until the end of your next turn. You become visible if you attack or cast a spell.")
```

## Divine Strike
*8th-level Trickery domain feature*

You gain the ability to infuse your weapon strikes with poison – a gift from your deity. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 poison damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns, when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels(baseclass) < 14 else '2d8'} force damage to the target.") )
```

## Improved Duplicity
*17th-level Trickery domain feature*

You can create up to four duplicates of yourself, instead of one, when you use Invoke Duplicity. As a bonus action on your turn, you can move any number of them up to 30 feet, to a maximum range of 120 feet.
