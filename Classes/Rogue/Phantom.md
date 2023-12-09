# Roguish Archetype: Phantom
Many rogues walk a fine line between life and death, risking their own lives and taking the lives of others. While adventuring on that line, some rogues discover a mystical connection to death itself. These rogues take knowledge from the dead and become immersed in negative energy, eventually becoming like ghosts. Rogues' guilds value them as highly effective information gatherers and spies.

Many shadar-kai of the Shadowfell are masters of these macabre techniques, and some are willing to teach this path. In places where many necromancers practice their craft, a Phantom can become a wizard's confidant and right hand. In temples of gods of death, the Phantom works as an agent to track down those who try to cheat death and to recover knowledge that might otherwise be lost to the grave. Phantoms are found all over Azgaarnoth, but they tend to end up in the company of the [Night's Blessing](../../Organizations/MageSchools/NightsBlessing.md) or [Twilight Star](../../Organizations/MageSchools/TwilightStar.md) magi over time. Some end up working for some of the [Great Houses](../../Organizations/Houses/index.md), and some find a home in a [Rogues' Guild](../../Organizations/RoguesGuilds/index.md).

```
name = 'Phantom'
description = "***Roguish Archetype: Phantom.*** Many rogues walk a fine line between life and death, risking their own lives and taking the lives of others. While adventuring on that line, some rogues discover a mystical connection to death itself. These rogues take knowledge from the dead and become immersed in negative energy, eventually becoming like ghosts. Rogues' guilds value them as highly effective information gatherers and spies."
```

## Whispers of the Dead
*3rd-level Phantom feature*

Echoes of those who have died begin to cling to you. Whenever you finish a short or long rest, you can gain one skill or tool proficiency of your choice, as a ghostly presence shares its knowledge with you. This proficiency lasts until you use this feature again.

```
def level3(npc):
    npc.traits.append("***Whispers of the Dead.*** Whenever you finish a short or long rest, you can gain one skill or tool proficiency of your choice, as a ghostly presence shares its knowledge with you. This proficiency lasts until you use this feature again.")
```

## Wails from the Grave
*3rd-level Phantom feature*

As you nudge someone closer to the grave, you can cause deathly wails to be heard near them. Immediately after you deal your Sneak Attack damage to a creature on your turn, you can target a second creature that you can see within 30 feet of the first creature. Roll half the number of Sneak Attack dice for your level (round up), and the second creature takes psychic damage equal to the roll's total, as wails of the dead sound around them for a moment.

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Wails from the Grave {npc.proficiencybonus()}/Recharges on long rest.*** Immediately after you deal your Sneak Attack damage to a creature on your turn, you can target a second creature that you can see within 30 feet of the first creature. Roll {(npc.levels('Rogue') + 3) // 4}d6, and {'the second creature takes' if npc.levels('Rogue') < 17 else 'both the first and second creatures take'} psychic damage equal to the roll's total, as wails of the dead sound around them for a moment."))
```

## Tokens of the Departed
*9th-level Phantom feature*

When a life ends in your presence, you're able to snatch a token from the departing soul, a sliver of its life essence that takes physical form: as a reaction when a creature you can see dies within 30 feet of you, you open your free hand and a Tiny trinket appears there, a soul trinket. The DM chooses the trinket's form or has you roll on the Trinkets table in the Player's Handbook to determine it.

While the soul trinket is on your person, you have advantage on death saving throws and Constitution saving throws, as your vitality is enhanced by the life essence within the object.

You can have a maximum number of soul trinkets equal to your proficiency bonus, and you can't create one while at your maximum.

As an action, you can destroy one of your soul trinkets, no matter where it's located. When you do so, you can ask the spirit associated with the trinket one question. The spirit appears to you and answers in a language it knew in life. It's under no obligation to be truthful, and it answers as concisely as possible, eager to be free.

```
def level9(npc):
    npc.reactions.append("***Tokens of the Departed.*** When a creature you can see dies within 30 feet of you, you open your free hand and a Tiny trinket appears there, a soul trinket. The DM chooses the trinket's form or has you roll on the Trinkets table in the Player's Handbook to determine it.")
    npc.defer(lambda npc: npc.traits.append("***Tokens of the Departed.*** While the soul trinket is on your person, you have advantage on death saving throws and Constitution saving throws, as your vitality is enhanced by the life essence within the object. You can have a maximum number of {npc.proficiencybonus()} soul trinkets, and you can't create one while at your maximum."))
    npc.actions.append("***Tokens of the Departed.*** You can destroy one of your soul trinkets, no matter where it's located. When you do so, you can ask the spirit associated with the trinket one question. The spirit appears to you and answers in a language it knew in life. It's under no obligation to be truthful, and it answers as concisely as possible, eager to be free.")
```

## Ghost Walk
*13th-level Phantom feature*

You can now phase partially into the realm of the dead, becoming like a ghost. As a bonus action, you assume a spectral form. While in this form, you have a flying speed of 10 feet, you can hover, and attack rolls have disadvantage against you. You can also move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object.

You stay in this form for 10 minutes or until you end it as a bonus action. To use this feature again, you must finish a long rest or destroy one of your soul trinkets as part of the bonus action you use to activate Ghost Walk.

```
def level13(npc):
    npc.bonusactions.append("***Ghost Walk (Recharges on long rest).*** You assume a spectral form. While in this form, you have a flying speed of 10 feet, you can hover, and attack rolls have disadvantage against you. You can also move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object. You stay in this form for 10 minutes or until you end it as a bonus action. To use this feature again, you must finish a long rest or destroy one of your soul trinkets as part of the bonus action you use to activate Ghost Walk.")
```


## Death Knell
*17th-level Phantom feature*

When you use your Wails from the Grave feature, you can now deal the psychic damage to both the first and the second creature.
