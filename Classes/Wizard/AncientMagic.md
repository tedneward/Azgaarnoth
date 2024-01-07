# Arcane Tradition: Ancient Magic
You have stumbled upon some source of ancient magic (often--but not always--Eldar magic), whether it be spellcasting notes, an old magical item, magic runes, or something else which you are only starting to unravel the secrets of. The only thing that you know for certain is that this source of magic will enhance your spellcasting in some way.

Practitioners of this tradition are almost never part of a [Mage School](../../Organizations/MageSchools/index.md) and will often refuse to share their hard-won secrets with others.

```
name = 'Ancient Magic'
description = "***Arcane Tradition: Ancient Magic.*** You have stumbled upon some source of ancient magic (often--but not always--Eldar magic), whether it be spellcasting notes, an old magical item, magic runes, or something else which you are only starting to unravel the secrets of. The only thing that you know for certain is that this source of magic will enhance your spellcasting in some way."
```

## Arcane Protection
*2nd-level Ancient Magic feature*

You have learned how to invoke an old protection magic to help protect someone. As a bonus action, you may touch a creature, giving it a bonus to all saving throws equal to half your proficiency bonus rounded down for 8 hours. Once you use this feature, you can not use it again until after you finish a long rest.

```
def level2(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Arcane Protection (Recharges on long rest).*** You touch a creature, giving it a +{npc.proficiencybonus() // 2} bonus to all saving throws for 8 hours.") )
```

## Studied
*2nd-level Ancient Magic feature*

Starting at 2nd level, you have begun to study up on ancient uses of arcane magic. You have advantage on any Intelligence (Arcana) or Intelligence (History) checks related to magic.

```
    npc.traits.append("***Studied.*** You have advantage on any Intelligence (Arcana) or Intelligence (History) checks related to magic.")
```

## Enhanced Spellcasting
*6th-level Ancient Magic feature*

You have begun to incorporate ancient magic into your spellcasting. When you cast a cantrip or spell that deals damage and roll a 1 on a damage roll, you may reroll the die. You must then use the new roll.

```
def level6(npc):
    npc.traits.append("***Enhanced Spellcasting.*** When you cast a cantrip or spell that deals damage and roll a 1 on a damage roll, you may reroll the die. You must then use the new roll.")
```

## Aura of Magic
*10th-level Ancient Magic feature*

Your study of ancient magic has irreversibly altered you. You now emit a 10 foot magical aura. This aura dispels all illusions that come into contact with the aura, and you can sense whenever a creature enters or exits your aura, but not where they are in your aura.

```
def level10(npc):
    npc.traits.append("***Aura of Magic.*** You now emit a 10 foot magical aura. This aura dispels all illusions that come into contact with the aura, and you can sense whenever a creature enters or exits your aura, but not where they are in your aura.")
```

## Ancient Glyph
*14th-level Ancient Magic feature*

You have mastered a piece of the art of ancient magic, and are able to place a "glyph" on a creature's very soul. As an action, you may place this "glyph" on a creature you can see within 60 feet of you. For 1 minute, they have disadvantage on saving throws caused by spells you cast, they take 1d10 psychic damage at the start of their turn, and you have advantage on any saving throws due to the target's actions, bonus actions, reactions, or other activities. Once you use this feature, you can not use it again until you finish a long rest.

```
def level14(npc):
    npc.actions.append("***Ancient Glyph (Recharges on long rest).*** You place an ancient glyph of magic on a creature you can see within 60 feet of you. For 1 minute, they have disadvantage on saving throws caused by spells you cast, they take 1d10 psychic damage at the start of their turn, and you have advantage on any saving throws due to the target's actions, bonus actions, reactions, or other activities.")
```
