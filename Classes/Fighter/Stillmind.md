# Martial Archetype: Stillmind Warrior
The stillmind exercises a variety of secret techniques in order to cut themselves from the source of magic and life that underlies the universe. The effects of this training scar their soul, giving them an unnerving aura recognisable from a distance. The advantages of these techniques, however, are undeniable: Stillmind Warriors are able to resist the effects of hostile magic to an enviable degree, making them ideal assassins and bodyguards.

```
name = 'Stillmind'
description = "***Martial Archetype: Stillmind Warrior.*** The stillmind exercises a variety of secret techniques in order to cut themselves from the source of magic and life that underlies the universe. The effects of this training scar their soul, giving them an unnerving aura recognisable from a distance. The advantages of these techniques, however, are undeniable: Stillmind Warriors are able to resist the effects of hostile magic to an enviable degree, making them ideal assassins and bodyguards."
```

## Tranquil Soul
*3rd-level Stillmind feature*

Your training distances you from the weave of magic. This has the following effects:

* You can no longer be detected by magical spells of any kind, and you are invisible to all magical sensors
* Creatures wanting to target you with any spell (including beneficial magic) must first succeed on a spellcasting ability check with a DC of 10+ half your character level rounded up. On a failed check, the spell has no effect and is wasted.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Tranquil Soul.*** You can no longer be detected by magical spells of any kind, and you are invisible to all magical sensors; Creatures wanting to target you with any spell (including beneficial magic) must first succeed on a spellcasting ability check (DC {10 + (npc.levels() // 2) + 1}). On a failed check, the spell has no effect and is wasted.") )
```

## Stillness Aura
*7th-level Stillmind feature*

You can project a strange aura that confounds magical abilities. As a bonus action, you can activate the aura, which is invisible and extends outwards to 30 feet from your location. Any creature which attempts to cast a spell whilst inside the aura must succeed on a spellcasting ability check with a DC of 10+ half your character level rounded up. On a failed check, the spell has no effect and is wasted.

```
def level7(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Stillness Aura.*** You activate an aura that confounds magical abilities, which is invisible and extends outwards to 30 feet from your location. Any creature which attempts to cast a spell whilst inside the aura must succeed on a spellcasting ability check (DC {10 + (npc.levels() // 2) + 1}). On a failed check, the spell has no effect and is wasted.") )
```

## Reflection
*10th-level Stillmind feature*

You gain the ability to rebound harmful magics. If you suceed on a saving throw against a harmful spell and the spell is 7th level or lower, you can choose to reflect it upon the caster. In this case, the spell has no effect on you and instead targets the caster, using the slot level, spell save DC, attack bonus, and spellcasting ability of the caster. You must finish a short rest before using this ability again.

```
def level10(npc):
    npc.traits.append("***Reflection (Recharges on short rest).*** If you suceed on a saving throw against a harmful spell and the spell is 7th level or lower, you can choose to reflect it upon the caster. In this case, the spell has no effect on you and instead targets the caster, using the slot level, spell save DC, attack bonus, and spellcasting ability of the caster.")
```

## Magic Resistance
*15th-level Stillmind feature*

At 15th level, you gain advantage on saving throws against any effect created by magic (as opposed to psionics or other source).

```
def level15(npc):
    npc.traits.append("***Magic Resistance.*** You have advantage on saving throws against any effect created by magic.")
```

## Limited Spell immunity
*18th-level Stillmind feature*

You cannot be affected by spells of 6th level or lower unless you wish to be. (This means all spells of 6th level or lower, even if cast with a higher level spell slot, such as a 7th level *fireball*).

```
def level18(npc):
    npc.traits.append("***Limited Spell Immunity.*** You cannot be affected by spells of 6th level or lower unless you wish to be. (This means all spells of 6th level or lower, even if cast with a higher level spell slot, such as a 7th level *fireball*).")
```
