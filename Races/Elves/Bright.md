# Bright Elf
The bright elves are one of the oldest subraces of elves. Due to their long years of close association with the Eldar they have an innate connection to the celestial light and song of creation. They are more lawful than other elven societies, and they value obedience as well as conformity. Many bright elves believe themselves to be the purest and most original form of elf, and see other elven subraces as little better than non-elves, but others among their ranks  are more accepting, often chiding their haughtier peers and worrying that such thinking is what led to the Fall.

As a bright elf, your body and soul are infused with light. A bright elf's skin is bronze, silvery, pearly, or pale white, and their hair is golden blond, platinum blond, or silvery white. Their eyes are usually golden or silvery gray, with streaks of white radiating from their pupils like a starburst.

```
name = 'Bright'
description = "***Subrace: Bright Elf.*** As a bright elf, your body and soul are infused with light. A bright elf's skin is bronze, silvery, pearly, or pale white, and their hair is golden blond, platinum blond, or silvery white. Their eyes are usually golden or silvery gray, with streaks of white radiating from their pupils like a starburst."
```

* **Ability Score Increase.** One ability score of your choice other than Dexterity increases by 1.

* **Ancient Magic.** Choose one of the following cantrips: [light](../../Magic/Spells/light.md), [dancing lights](../../Magic/Spells/dancing-lights.md), or [thaumaturgy](../../Magic/Spells/thaumaturgy.md). You know that cantrip, and Charisma is your spellcasting ability for it.

* **Brightfolk.** You have resistance to radiant damage, and you have advantage on saving throws to resist being blinded by effects that deal radiant damage or create light.

* **Celestial Nature.** You have two creature types: humanoid and celestial You can be affected by a game effect if it works on either of your creature types.

```
name = 'Bright'
def level0(npc):
    npc.type += "/celestial"

    asi = choose("Choose an ability score increase:", ['STR', 'CON', 'INT', 'WIS', 'CHA'])
    match asi:
        case 'STR': npc.STR += 1
        case 'CON': npc.CON += 1
        case 'INT': npc.INT += 1
        case 'WIS': npc.WIS += 1
        case 'CHA': npc.CHA += 1

    spellcasting = innatecaster(npc, 'CHA', "Bright Elf")
    spellcasting.cantripsknown.append(choose("Choose a cantrip:", ['light', 'dancing lights', 'thaumaturgy']))

    npc.traits.append("***Brightfolk.*** You have advantage on saving throws to resist being blinded by effects that deal radiant damage or create light.")
    npc.damageresistances.append('radiant')
```