# Bardic College: College of Whispers
Most folk are happy to welcome a bard into their midst. Bards of the College of Whispers use this to their advantage. They appear to be like any other bard, sharing news, singing songs, and telling tales to the audiences they gather. In truth, the College of Whispers teaches its students that they are wolves among sheep. These bards use their knowledge and magic to uncover secrets and turn them against others through extortion and threats.

Many other bards hate the College of Whispers, viewing it as a parasite that uses the bards' reputation to acquire wealth and power. For this reason, these bards rarely reveal their true nature unless they must. They typically claim to follow some other college, or keep their true nature secret in order to better infiltrate and exploit royal courts and other settings of power.

Rumors suggest that the College of Whispers is run by the [Copper Order](../../Organizations/MilitantOrders/DraconicOrder/Copper.md), although it is also said that they are operated by the [Dread Emperor](../../People/DreadEmperor.md), or any of the other nations of Azgaarnoth. It is entirely possible (and likely) that, like the [College of Valor](Valor.md), there are multiple colleges of Whispers within Azgaarnoth.

```
name = 'College of Whispers'
description = "***Bardic College.*** Bards of the College of Whispers appear to be like any other bard, sharing news, singing songs, and telling tales to the audiences they gather. In truth, the College of Whispers teaches its students that they are wolves among sheep. These bards use their knowledge and magic to uncover secrets and turn them against others through extortion and threats."
```

## Psychic Blades
*3rd-level College of Whispers feature*

You gain the ability to make your weapon attacks magically toxic to a creature's mind.

When you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an additional 2d6 psychic damage to that target. You can do so only once per round on your turn.

The psychic damage increases when you reach certain levels in this class, increasing to 3d6 at 5th level, 5d6 at 10th level, and 8d6 at 15th level.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append("***Psychic Blades.*** When you hit a creature with a weapon attack, you can expend one use of your Bardic Inspiration to deal an additional {'2d6' if npc.levels('Bard') < 5 else '3d6' if npc.levels('Bard') < 10 else '5d6' if npc.levels('Bard') < 15 else '8d6'} psychic damage to that target. You can do so only once per round on your turn.") )
```

## Words of Terror
*3rd-level College of Whispers feature*

You learn to infuse innocent-seeming words with an insidious magic that can inspire terror.

If you speak to a humanoid alone for at least 1 minute, you can attempt to seed paranoia and fear into its mind. At the end of the conversation, the target must succeed on a Wisdom saving throw against your spell save DC or be frightened of you or another creature of your choice. The target is frightened in this way for 1 hour, until it is attacked or damaged, or until it witnesses its allies being attacked or damaged.

If the target succeeds on its saving throw, the target has no hint that you tried to frighten it.

Once you use this feature, you can't use it again until you finish a short rest or long rest.

```
    npc.defer(lambda npc: npc.actions.append("***Words of Terror (Recharges on short or long rest).*** If you speak to a humanoid alone for at least 1 minute, you can attempt to seed paranoia and fear into its mind. At the end of the conversation, the target must succeed on a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or be frightened of you or another creature of your choice. The target is frightened in this way for 1 hour, until it is attacked or damaged, or until it witnesses its allies being attacked or damaged. If the target succeeds on its saving throw, the target has no hint that you tried to frighten it.") )
```

## Mantle of Whispers
*6th-level College of Whispers feature*

You gain the ability to adopt a humanoid's persona. When a humanoid dies within 30 feet of you, you can magically capture its shadow using your reaction. You retain this shadow until you use it or you finish a long rest.

You can use the shadow as an action. When you do so, it vanishes, magically transforming into a disguise that appears on you. You now look like the dead person, but healthy and alive. This disguise lasts for 1 hour or until you end it as a bonus action.

While you're in the disguise, you gain access to all information that the humanoid would freely share with a casual acquaintance. Such information includes general details on its background and personal life, but doesn't include secrets. The information is enough that you can pass yourself off as the person by drawing on its memories.

Another creature can see through this disguise by succeeding on a Wisdom (Insight) check contested by your Charisma (Deception) check. You gain a +5 bonus to your check.

Once you capture a shadow with this feature, you can't capture another one with it until you finish a short or long rest.

```
def level6(npc):
    npc.reactions.append("***Mantle of Whispers: Capture Shadow (Recharges on a long rest).*** When a humanoid dies within 30 feet of you, you magically capture its shadow.")
    npc.actions.append("***Mantle of Whispers: Utilize Shadow.*** You transform the captured shadow into a disguise that appears on you. You now look like the dead person, but healthy and alive. This disguise lasts for 1 hour or until you end it as a bonus action. While you're in the disguise, you gain access to all information that the humanoid would freely share with a casual acquaintance. Such information includes general details on its background and personal life, but doesn't include secrets. The information is enough that you can pass yourself off as the person by drawing on its memories.Another creature can see through this disguise by succeeding on a Wisdom (Insight) check contested by your Charisma (Deception) check. You gain a +5 bonus to your check.")
```

## Shadow Lore
*14th-level College of Whispers feature*

You gain the ability to weave dark magic into your words and tap into a creature's deepest fears.

As an action, you magically whisper a phrase that only one creature of your choice within 30 feet of you can hear. The target must make a Wisdom saving throw against your spell save DC. It automatically succeeds if it doesn't share a language with you or if it can't hear you. On a successful saving throw, your whisper sounds like unintelligible mumbling and has no effect.

If the target fails its saving throw, it is charmed by you for the next 8 hours or until you or your allies attack or damage it. It interprets the whispers as a description of its most mortifying secret.

While you gain no knowledge of this secret, the target is convinced you know it. While charmed in this way, the creature obeys your commands for fear that you will reveal its secret. It won't risk its life for you or fight for you, unless it was already inclined to do so. It grants you favors and gifts it would offer to a close friend.

When the effect ends, the creature has no understanding of why it held you in such fear.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level14(npc):
    npc.actions.append("***Shadow Lore (Recharges on long rest).*** You magically whisper a phrase that only one creature of your choice within 30 feet of you can hear. The target must make a Wisdom saving throw against your spell save DC. It automatically succeeds if it doesn't share a language with you or if it can't hear you. On a successful saving throw, your whisper sounds like unintelligible mumbling and has no effect. If the target fails its saving throw, it is charmed by you for the next 8 hours or until you or your allies attack or damage it. It interprets the whispers as a description of its most mortifying secret. While you gain no knowledge of this secret, the target is convinced you know it. While charmed in this way, the creature obeys your commands for fear that you will reveal its secret. It won't risk its life for you or fight for you, unless it was already inclined to do so. It grants you favors and gifts it would offer to a close friend. When the effect ends, the creature has no understanding of why it held you in such fear.")
```

---

# Custom Bard Spells

* 1st: [sheltered voices]()
* 2nd: [arcane transference](), [disperse reserves]()
* 4th: [zone of sonic amplification]()
