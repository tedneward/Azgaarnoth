# Bright Elf
One of your parents was a [Bright Elf](../Elves/Bright.md).

* **Ability Score Increase.** One ability score of your choice other than Dexterity increases by 1.

* **Ancient Magic.** Choose one of the following cantrips: [light](../../Magic/Spells/light.md), [dancing lights](../../Magic/Spells/dancing-lights.md), or [thaumaturgy](../../Magic/Spells/thaumaturgy.md). You know that cantrip, and Charisma is your spellcasting ability for it.

* **Brightfolk.** You have resistance to radiant damage, and you have advantage on saving throws to resist being blinded by effects that deal radiant damage or create light.

```
name = 'Bright'
description = "***Elvish Heritage: Bright Elf.*** One of your parents was a Bright Elf."
def level0(npc):
    asi = choose("Choose an ability score increase:", ['STR', 'CON', 'INT', 'WIS', 'CHA'])

    if asi == 'STR': npc.STR += 1
    elif asi == 'CON': npc.CON += 1
    elif asi == 'INT': npc.INT += 1
    elif asi == 'WIS': npc.WIS += 1
    elif asi == 'CHA': npc.CHA += 1

    spellcasting = innatecaster(npc, 'CHA', "Half-Bright Elf")
    spellcasting.cantripsknown.append(choose("Choose a cantrip:", ['light', 'dancing lights', 'thaumaturgy']))

    npc.traits.append("***Brightfolk.*** You have advantage on saving throws to resist being blinded by effects that deal radiant damage or create light.")
    npc.damageresistances.append('radiant')
```