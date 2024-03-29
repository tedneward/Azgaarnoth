# Bardic College: College of Glamour
The College of Glamour is the home of bards who mastered their craft in the vibrant realm of the Feywild or under the tutelage of someone who dwelled there. Tutored by satyrs, eladrin, and other fey, these bards learn to use their magic to delight and captivate others.

The bards of this college are regarded with a mixture of awe and fear. Their performances are the stuff of legend. These bards are so eloquent that a speech or song that one of them performs can cause captors to release the bard unharmed and can lull a furious dragon into complacency. The same magic that allows them to quell beasts can also bend minds. Villainous bards of this college can leech off a community for weeks, abusing their magic to turn their hosts into thralls. Heroic bards of this college instead use this power to gladden the downtrodden and undermine oppressors.

This college is quite popular among the [Mercenary Companies](../../Organizations/MercCompanies/MercCompanies.md) as they incite the troops to greater and greater ideals, or tell the oral histories of the companies around the campfire during the march. Many universities that host this College are found in cities which has a mercenary company wintering nearby. Rumors abound, however, of Colleges funded by more shadowy organizations that seek to use these bards in more nefarious ways; the [Order of the Copper Dragon](../../Organizations/MilitantOrders/DraconicOrder/Copper.md) has been rumored to use Glamour to ferret out secrets in non-violent ways.

```
name = 'College of Glamour'
description = "***Bardic College: College of Glamour.*** The College of Glamour is the home of bards who mastered their craft in the vibrant realm of the Feywild or under the tutelage of someone who dwelled there. Tutored by satyrs, eladrin, and other fey, these bards learn to use their magic to delight and captivate others."
```

## Mantle of Inspiration
*3rd-level College of Glamour feaure*

You gain the ability to weave a song of fey magic that imbues your allies with vigor and speed.

As a bonus action, you can expend one use of your Bardic Inspiration to grant yourself a wondrous appearance. When you do so, choose a number of creatures you can see and who can see you within 60 feet of you, up to a number equal to your Charisma modifier (minimum of one). Each of them gains 5 temporary hit points. When a creature gains these temporary hit points, it can immediately use its reaction to move up to its speed, without provoking opportunity attacks.

The number of temporary hit points increases when you reach certain levels in this class, increasing to 8 at 5th level, 11 at 10th level, and 14 at 15th level.

```
def level3(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Mantle of Inspiration.*** You expend one use of your Bardic Inspiration to grant yourself a wondrous appearance. Choose a number of creatures you can see and who can see you within 60 feet of you, up to {npc.CHAbonus()}. Each of them gains {5 if npc.levels('Bard') < 5 else 8 if npc.levels('Bard') < 10 else 11 if npc.levels('Bard') < 15 else 14} temporary hit points. When a creature gains these temporary hit points, it can immediately use its reaction to move up to its speed, without provoking opportunity attacks.") )
```

## Enthralling Performance
*3rd-level College of Glamour feaure*

You can charge your performance with seductive, fey magic.

If you perform for at least 1 minute, you can attempt to inspire wonder in your audience by singing, reciting a poem, or dancing. At the end of the performance, choose a number of humanoids within 60 feet of you who watched and listened to all of it, up to a number equal to your Charisma modifier (minimum of one). Each target must succeed on a Wisdom saving throw against your spell save DC or be charmed by you. While charmed in this way, the target idolizes you, it speaks glowingly of you to anyone who speaks to it, and it hinders anyone who opposes you, avoiding violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies.

If a target succeeds on its saving throw, the target has no hint that you tried to charm it.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Enthralling Performance (Recharges on short or long rest).*** If you perform for at least 1 minute, you can attempt to inspire wonder in your audience by singing, reciting a poem, or dancing. At the end of the performance, choose up to {npc.CHAbonus()} humanoids within 60 feet of you who watched and listened to all of it. Each target must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or be charmed by you. While charmed in this way, the target idolizes you, it speaks glowingly of you to anyone who speaks to it, and it hinders anyone who opposes you, avoiding violence unless it was already inclined to fight on your behalf. This effect ends on a target after 1 hour, if it takes any damage, if you attack it, or if it witnesses you attacking or damaging any of its allies. If a target succeeds on its saving throw, the target has no hint that you tried to charm it.") )
```

## Mantle of Majesty
*6th-level College of Glamour feaure*

You gain the ability to cloak yourself in a fey magic that makes others want to serve you. As a bonus action, you cast Command, without expending a spell slot, and you take on an appearance of unearthly beauty for 1 minute or until your concentration ends (as if you were concentrating on a spell). During this time, you can cast Command as a bonus action on each of your turns, without expending a spell slot.

Any creature charmed by you automatically fails its saving throw against the Command you cast with this feature.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level6(npc):
    npc.bonusactions.append(f"***Mantle of Majesty (Recharges on long rest).*** You cast {spelllinkify('command')} without expending a spell slot, taking on an appearance of unearthly beauty for 1 minute or until your concentration ends. During this time, you can cast {spelllinkify('command')} as a bonus action on each of your turns without expending a spell slot. Any creature charmed by you automatically fails its saving throw against the *command* you cast with this feature.")
```

## Unbreakable Majesty
*14th-level College of Glamour feaure*

Your appearance permanently gains an otherworldly aspect that makes you look more lovely and fierce.

In addition, as a bonus action, you can assume a magically majestic presence for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw against your spell save DC. On a failed save, it can't attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn.

Once you assume this majestic presence, you can't do so again until you finish a short or long rest.

```
def level14(npc):
    npc.description.append("***Unbreakable Majesty.*** Your appearance permanently gains an otherworldly aspect that makes you look more lovely and fierce.")
    npc.defer(lambda npc: npc.bonusactions.append("***Unbreakable Majesty.*** You assume a magically majestic presence for 1 minute or until you are incapacitated. For the duration, whenever any creature tries to attack you for the first time on a turn, the attacker must make a Charisma saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}). On a failed save, it can't attack you on this turn, and it must choose a new target for its attack or the attack is wasted. On a successful save, it can attack you on this turn, but it has disadvantage on any saving throw it makes against your spells on your next turn.") )
```

---

# Custom Bard Spells
The College of Glamour has developed many custom spells solely for its own use.

* 1st: [glow mark](), [luminous trail](), [persistent sparkle]()
* 4th: [thunder stomp]()
* 8th: [cacophony of thunder]()
* 9th: [calm the skies](), [winterland]()
