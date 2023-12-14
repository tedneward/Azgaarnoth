# Arcane Tradition: Geomancy
Geomancy wizards are the kind of wizard who appreciate the sturdiness and stability of earth magic. The world of stone, dirt, and rock is firm, hardy and strong. A wizard who learns to harness the magic of the earth can become a hardy practitioner of magic; one who can withstand even the toughest of foes.

```
name = 'Geomancy'
description = "***Arcane Tradition: Geomancy.*** Geomancy wizards are the kind of wizard who appreciate the sturdiness and stability of earth magic. The world of stone, dirt, and rock is firm, hardy and strong. A wizard who learns to harness the magic of the earth can become a hardy practitioner of magic; one who can withstand even the toughest of foes."
```

## Geomancer's Knowledge
*2nd-level Geomancy feature*

Your affinity for utilizing stone and the earth has become second nature for you. You have advantage on Dexterity (Stealth) checks made to hide in rocky terrain, and advantage on Constitution saving throws to maintain your concentration while in rocky terrain.

Additionally, the following spells are added to the wizard spell list for you: [bones of the earth](../../Magic/Spells/bones-of-the-earth.md), [earthquake](../../Magic/Spells/earthquake.md), [magic stone](../../Magic/Spells/magic-stone.md), and [meld into stone](../../Magic/Spells/meld-into-stone.md).

```
def level2(npc):
    npc.traits.append("***Geomancer's Knowledge.*** You have advantage on Dexterity (Stealth) checks made to hide in rocky terrain, and advantage on Constitution saving throws to maintain your concentration while in rocky terrain.")

    npc.spellcasting['Wizard'].spellbook.append('bones of the earth')
    npc.spellcasting['Wizard'].spellbook.append('magic stone')
    npc.spellcasting['Wizard'].spellbook.append('meld into stone')
```

## Stone Form
*6th-level Geomancy feature*

As an action, you can transform yourself temporarily into stone form, your skin hardening and taking on a number of characteristics of an earth elemental. You can use this feature twice and you regain expended uses after finishing a long rest.

Whilst in stone form, you gain a +2 bonus to AC, you are immune to the poisoned condition and have immunity to poison damage, and you have resistance to bludgeoning, piercing, and slashing from nonmagical weapons. Additionally, your movement speed is reduced by 10 feet and you have disadvantage on Dexterity saving throws.

You maintain your stone form for 1 hour unless you end it early using a bonus action. If you fall unconscious, drop to zero hit points, or die, you automatically revert to your normal form.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append("***Stone Form ({ str(2 + npc.INTbonus()) if npc.levels('Wizard') < 14 else '2'}/Recharges on long rest).*** You transform yourself temporarily into stone form, your skin hardening and taking on a number of characteristics of an earth elemental. Whilst in stone form, you gain a +2 bonus to AC, you are immune to the poisoned condition and have immunity to poison damage, and you have resistance to bludgeoning, piercing, and slashing from nonmagical weapons. Additionally, your movement speed is reduced by 10 feet and you have disadvantage on Dexterity saving throws. You maintain your stone form for 1 hour unless you end it early using a bonus action. If you fall unconscious, drop to zero hit points, or die, you automatically revert to your normal form.{'If you revert back to your normal form from your stone form as a result of the duration time of 1 hour has expired, or by using your bonus action to do so, you gain ' + str(npc.levels('Wizard') + npc.CONbonus()) + ' temporary hit points' if npc.levels('Wizard') >= 10 else ''}") )
```

## Protection of the Earth
*10th-level Geomancy feature*

If you revert back to your normal form from your stone form as a result of the duration time of 1 hour has expired, or by using your bonus action to do so, you gain temporary hit points equal to your wizard level + your Constitution modifier.

## Master Geomancer
*14th-level Geomancy feature*

You can use your Stone Form ability an additional number of times equal to your Intelligence modifier (minimum of 1). You can expend 2 uses of your stone form ability to instead transform into the form of an [earth elemental](../../Creatures/Extraplanar/Elementals.md#earth-elemental). Whilst in earth elemental form, you can speak any languages you know.

While you are transformed, the following rules apply:

* Your game statistics are replaced by the statistics of the earth elemental, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the earth elemental. If the earth elemental has the same proficiency as you and the bonus in its stat block is higher than yours, use the earth elemental's bonus instead of yours.
* You can't cast spells while transformed. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as [rain of stones](../../Magic/Spells/rain-of-stones.md), that you've already cast.
* You retain the benefit of any features from your class, race, or other source and can use them if the earth elemental form is physically capable of doing so. However, you can't use any special senses that you might have (such as darkvision) unless the earth elemental also has that sense.
* You choose whether your equipment falls to the ground in your space, merges into your earth elemental form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the earth elemental to wear a piece of equipment based on the earth elemental's shape and size. Your equipment doesn't change size or shape to match the earth elemental form, and any equipment that the earth elemental form can't wear must either fall to the ground or merge with it. Equipment that merges with the earth elemental form has no effect until you revert back to your normal form.

```
def level14(npc):
    npc.actions.append(f"***Master Geomancer.*** You can expend 2 uses of your Stone Form ability to instead transform into the form of an [earth elemental](http://azgaarnoth.tedneward/creatures/extraplanar/Elementals/#earth-elemental). Whilst in earth elemental form, you can speak any languages you know. While you are transformed, your game statistics are replaced by the statistics of the earth elemental, but you retain your alignment, personality, and Intelligence, Wisdom, and Charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the earth elemental. If the earth elemental has the same proficiency as you and the bonus in its stat block is higher than yours, use the earth elemental's bonus instead of yours. You can't cast spells while transformed. Transforming doesn't break your concentration on a spell you've already cast, however, or prevent you from taking actions that are part of a spell, such as {spelllinkify('rain of stones')}, that you've already cast. You retain the benefit of any features from your class, race, or other source and can use them if the earth elemental form is physically capable of doing so. However, you can't use any special senses that you might have (such as darkvision) unless the earth elemental also has that sense. You choose whether your equipment falls to the ground in your space, merges into your earth elemental form, or is worn by it. Worn equipment functions as normal, but the DM decides whether it is practical for the earth elemental to wear a piece of equipment based on the earth elemental's shape and size. Your equipment doesn't change size or shape to match the earth elemental form, and any equipment that the earth elemental form can't wear must either fall to the ground or merge with it. Equipment that merges with the earth elemental form has no effect until you revert back to your normal form.")
```

---

# Geomancy Spells

## 1st-level
* [earthen grace](../../Magic/Spells/earthen-grace.md)
* [sandblast](../../Magic/Spells/sandblast.md)

## 2nd-level
* [fist of stone](../../Magic/Spells/fist-of-stone.md)

## 3rd-level
* [rain of stones](../../Magic/Spells/rain-of-stones.md)

