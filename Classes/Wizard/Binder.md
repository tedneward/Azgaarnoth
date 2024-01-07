# Arcane Tradition: School of Binding
When a wizard states they're a conjurer, it usually means they summon creatures from the planes and use them as servants. A binder takes this tradition a step further: they make a deal with one of these beings and become their partner. Some wizards will bind an individual creature, over and over. Others will rotate through a slew of creatures, adapting abilities as needed.

The Binder tradition is unique to the [School of the Collared Fiend](../../Organizations/MageSchools/CollaredFiend.md), and anyone of this tradition has some kind of history with that school at some point in their life.

```
name = 'Binder'
description = "***Arcane Tradition: School of Binding.*** When a wizard states they're a conjurer, it usually means they summon creatures from the planes and use them as servants. A binder takes this tradition a step further: they make a deal with one of these beings and become their partner. Some wizards will bind an individual creature, over and over. Others will rotate through a slew of creatures, adapting abilities as needed."
```

## Planar Contact
*2nd-level Binding feature*

You learn your choice of two of the following languages: Abyssal, Infernal, Celestial, or Sylvan. Additionally, you become proficient with a set of tattoo needles.

```
def level2(npc):
    npc.languages.append(choose("Choose a language: ", ['Abyssal', 'Infernal', 'Celestial', 'Sylvan']))
    npc.languages.append(choose("Choose a language: ", ['Abyssal', 'Infernal', 'Celestial', 'Sylvan']))
```

## Align Contact
*2nd-level Binding feature*

Whenever you complete a long rest, you can reach out to creatures of the planes. You choose to contact a devil, demon, angel, or guardinal and you make a deal with it. The creature becomes a spirit and wraps itself around your body, exhibiting itself as a tattoo that appears on your skin.

While you have a creature bound in this fashion, the creature is available to you to ask questions. Because it is bound to you, it must provide you an answer to the best of its ability, granting you advantage on Intelligence checks related to the creature and its home plane, as well as any other information it reasonably possesses.

```
    npc.traits.append("***Align Contact.*** Whenever you complete a long rest, you can reach out to creatures of the planes. You choose to contact a devil, demon, angel, or guardinal and you make a deal with it. The creature becomes a spirit and wraps itself around your body, exhibiting itself as a tattoo that appears on your skin.While you have a creature bound in this fashion, the creature is available to you to ask questions. Because it is bound to you, it must provide you an answer to the best of its ability, granting you advantage on Intelligence checks related to the creature and its home plane, as well as any other information it reasonably possesses.")
```

## Be My Guide
*6th-level Binding feature*

As a bonus action, your bound spirit can be released to aid you in combat. The tattoo begins to glow on your skin. This ability lasts a number of rounds equal to half your wizard level (minimum of 1). You gain one of the following benefits based on the creature that was bound to you:

* **Demon**. Your physical form becomes more demonic, growing spikes and claws. If you deal damage to a creature with a spell on your turn, you can use your bonus action to try and claw them. This is a melee weapon attack you are proficient with, that uses your Intelligence modifier instead of Strength, and deals 2d6 slashing damage. This attack can be used as part of the bonus action to invoke this ability.
* **Devil**. Your eyes blacken, your body reeks of brimstone, and you grow thick horns. When you cast a spell that has a duration on a creature, while that creature is affected by your spell, they are harassed by a flock of imps that come seemingly out of nowhere. All attacks against that target are made with advantage. If the spell targets multiple creatures, you must choose one of those creatures as the target creature to be affected by this ability. You can change this choice at the start of each of your turns.
* **Angel**. You grow glowing wings made of light. You gain a fly speed that is twice your movement speed, and you shed bright light in a 20-foot radius and dim light for an additional 20 feet.
* **Guardinal**. Your skin gains shaggy fur, your hair has the texture of feathers, and your physical form becomes more bestial. You are resistant to lightning damage, and magic can't put you to sleep. Additionally, whenever you reduce a creature to zero hit points, you gain temporary hit points equal to your wizard level that last until this ability ends.

Once you use this ability, you cannot use it again until after you have completed a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Be My Guide (Recharges on long rest).*** Your bound spirit is released to aid you in combat for {(npc.levels('Wizard') + 1) // 2}. You gain one of the following benefits based on the creature that was bound to you: **Demon**. Your physical form becomes more demonic, growing spikes and claws. If you deal damage to a creature with a spell on your turn, you can use your bonus action to try and claw them. This is a melee weapon attack you are proficient with, that uses your Intelligence modifier instead of Strength, and deals 2d6 slashing damage. This attack can be used as part of the bonus action to invoke this ability. **Devil**. Your eyes blacken, your body reeks of brimstone, and you grow thick horns. When you cast a spell that has a duration on a creature, while that creature is affected by your spell, they are harassed by a flock of imps that come seemingly out of nowhere. All attacks against that target are made with advantage. If the spell targets multiple creatures, you must choose one of those creatures as the target creature to be affected by this ability. You can change this choice at the start of each of your turns. **Angel**. You grow glowing wings made of light. You gain a fly speed that is twice your movement speed, and you shed bright light in a 20-foot radius and dim light for an additional 20 feet. **Guardinal**. Your skin gains shaggy fur, your hair has the texture of feathers, and your physical form becomes more bestial. You are resistant to lightning damage, and magic can't put you to sleep. Additionally, whenever you reduce a creature to zero hit points, you gain temporary hit points equal to your wizard level that last until this ability ends.") )
```

## Guard My Back
*10th-level Binding feature*

As an action, your bound spirit can be released to protect you. The tattoo begins to glow on your skin and a ghostly copy of the bound creature appears in an unoccupied space adjacent to you. This ability lasts a number of rounds equal to half your wizard level (minimum 1). You have half cover while the facsimile of the creature is adjacent to you. You gain one of the following benefits based on which creature was bound to you:

* **Demon**. You gain a +1 bonus to AC, and creatures that attack you take magical slashing damage equal to half your wizard level.
* **Devil**. You have resistance against damage from spells.
* **Angel**. You have advantage on saving throws against spells.
* **Guardinal**. Beasts will not attack you unless you attack them first, and you can cast speak with animals at will. At the start of each of your turns, if you are at less than half of your hit points total, you regain 5 hit points.

Once you use this ability, you cannot use it again until after you have finished a long rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Guard My Back (Recharges on long rest).*** The tattoo begins to glow on your skin and a ghostly copy of the bound creature appears in an unoccupied space adjacent to you, to protect you. This ability lasts {npc.levels('Wizard') // 2} a number of rounds equal to half your wizard level (minimum 1). You have half cover while the facsimile of the creature is adjacent to you. You gain one of the following benefits based on which creature was bound to you: **Demon**. You gain a +1 bonus to AC, and creatures that attack you take magical slashing damage equal to half your wizard level. **Devil**. You have resistance against damage from spells. **Angel**. You have advantage on saving throws against spells. **Guardinal**. Beasts will not attack you unless you attack them first, and you can cast {spelllinkify('speak with animals')} at will. At the start of each of your turns, if you are at less than half of your hit points total, you regain 5 hit points.") )
```

## By My Side!
*14th-level Binding feature*

As an action, you can summon your bound creature to physical form. The tattoos disappear from your body and the bound creature appears in an unoccupied space of your choice within 30 feet. Without your tattoos, you are unable to invoke either of your Be My Guide or Guard My Back abilities.

The creature acts on its own initiative, makes its own decisions, but considers you an ally. This ability lasts for 10 minutes, or until the creature hits zero hit points, or until you use your action to end the effect. When the creature disappears, your binding tattoo does not reappear, requiring you to use your tattoo needles and complete a long rest, to create a new binding tattoo.

The creature you summon is based on the creature that was bound to you:

* Demon - [Barlgura](../../Creatures/Demons/Barlgura.md)
* Devil - [Barbed Devil](../../Creatures/Devils/Barbed.md)
* Angel - [Couatl](../../Creatures/Extraplanar/Couatl.md)
* Guardinal - [Musteval](../../Creatures/Extraplanar/Guardinals.md#musteval)

```
def level14(npc):
    npc.actions.append("***By My Side.*** you can summon your bound creature to physical form. The tattoos disappear from your body and the bound creature appears in an unoccupied space of your choice within 30 feet. Without your tattoos, you are unable to invoke either of your Be My Guide or Guard My Back abilities. The creature acts on its own initiative, makes its own decisions, but considers you an ally. This ability lasts for 10 minutes, or until the creature hits zero hit points, or until you use your action to end the effect. When the creature disappears, your binding tattoo does not reappear, requiring you to use your tattoo needles and complete a long rest, to create a new binding tattoo. The creature you summon is based on the creature that was bound to you: **Demon**: [Barlgura](../../Creatures/Demons/Barlgura.md) **Devil**: [Barbed Devil](../../Creatures/Devils/Barbed.md) **Angel**: [Couatl](../../Creatures/Extraplanar/Couatl.md) **Guardinal**: [Musteval](../../Creatures/Extraplanar/Guardinals.md#musteval)")
```

---

# Binder Unique Spell List

## 2nd
* [disconnect bond](../../Magic/Spells/disconnect-bond.md)
* [overpower bond](../../Magic/Spells/overpower-bond.md)

## 3rd
* [ethereal quiver](../../Magic/Spells/ethereal-quiver.md)

## 5th
* [Tenser's recall](../../Magic/Spells/tensers-recall.md)
