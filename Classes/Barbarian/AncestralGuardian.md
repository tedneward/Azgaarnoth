# Primal Path: Path of the Ancestral Guardian
Some barbarians hail from cultures that revere their ancestors. These tribes teach that the warriors of the past linger in the world as mighty spirits, who can guide and protect the living. When a barbarian who follows this path rages, the barbarian contacts the spirit world and calls on these guardian spirits for aid.

Barbarians who draw on their ancestral guardians can better fight to protect their tribes and their allies. In order to cement ties to their ancestral guardians, barbarians who follow this path cover themselves in elaborate tattoos that celebrate their ancestors' deeds. These tattoos tell sagas of victories against terrible monsters and other fearsome rivals.

These barbarians are most commonly found among the [United Hordes](../../Nations/Tragekia.md) or [Yithi](../../Nations/Yithi.md).

```
name = 'Ancestral Guardian'
description = "***Primal Path: Path of the Ancestral Guardian.*** Some barbarians hail from cultures that revere their ancestors. These tribes teach that the warriors of the past linger in the world as mighty spirits, who can guide and protect the living. When a barbarian who follows this path rages, the barbarian contacts the spirit world and calls on these guardian spirits for aid."
```

## Ancestral Protectors
*3rd-level Path of the Ancestral Guardian feature*

Spectral warriors appear when you enter your rage. While you're raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks. Until the start of your next turn, that target has disadvantage on any attack roll that isn't against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage of the target's attacks.

```
def level3(npc):
    npc.traits.append("***Ancestral Protectors.*** While you're raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks. Until the start of your next turn, that target has disadvantage on any attack roll that isn't against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage of the target's attacks.")
```

## Spirit Shield
*6th-level Path of the Ancestral Guardian feature*

The guardian spirits that aid you can provide supernatural protection to those you defend. If you are raging and a creature you can see within 30 feet of you takes damage, you can use your reaction to reduce that damage by 2d6.

When you reach certain levels in this class, you can reduce the damage by more: by 3d6 at 10th level and by 4d6 at 14th level.

```
def level6(npc):
    npc.defer(lambda npc: npc.reactions.append("***Spirit Shield.*** If you are raging and a creature you can see within 30 feet of you takes damage, you reduce that damage by {'2d6' if npc.levels('Barbarian') < 10 else '3d6' if npc.levels('Barbarian') < 14 else '4d6'}.{'' if npc.levels('Barbarian') < 14 else ' The attacker takes that same amount of damage as force damage.'}") )
```

## Consult the Spirits
*10th-level Path of the Ancestral Guardian feature*

You gain the ability to consult with your ancestral spirits. When you do so, you cast the [augury](../../Magic/Spells/augury.md) or [clairvoyance](../../Magic/Spells/clairvoyance.md) spell, without using a spell slot or material components. Rather than creating a spherical sensor, this use of Clairvoyance invisibly summons one of your ancestral spirits to the chosen location. Wisdom is your spellcasting ability for these spells.

After you cast either spell in this way, you can't use this feature again until you finish a short or long rest.

```
def level10(npc):
    npc.traits.append("***Consult the Spirits (Recharges on short or long rest).*** You consult with your ancestral spirits, which give you the ability to cast the {spelllinkify('augury')} or {spelllinkify('clairvoyance')} spell, without using a spell slot or material components. Rather than creating a spherical sensor, this use of *clairvoyance* invisibly summons one of your ancestral spirits to the chosen location. Wisdom is your spellcasting ability for these spells.")
```

## Vengeful Ancestors
*14th-level Path of the Ancestral Guardian feature*

Your ancestral spirits grow powerful enough to retaliate. When you use your Spirit Shield to reduce the damage of an attack, the attacker takes an amount of force damage that your Spirit Shield prevents.
