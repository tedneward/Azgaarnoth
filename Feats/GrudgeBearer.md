## Grudge Bearer
*Prerequisite: Dwarf*

You have a deep hatred for a particular kind of creature. Choose your foes, a type of creature to bear the burden of your wrath: aberrations, beasts, celestials, constructs, dragons, elementals, fey, fiends, giants, monstrosities, oozes, plants, or undead. Alternatively, you can choose two races of humanoid (such as gnolls and orcs). You gain the following benefits:

* Increase your Strength, Constitution, or Wisdom score by 1, to a maximum of 20.
* During the first round of any combat against your chosen foes, your attack rolls against any of them have advantage.
* When any of your chosen foes makes an opportunity attack against you, it makes the attack roll with disadvantage.
* Whenever you make an Intelligence (Arcana, History, Nature, or Religion) check to recall information about your chosen foes, you add double your proficiency bonus to the check, even if you're not normally proficient.

```
name = 'Grudge Bearer'
description = "***Feat: Grudge Bearer.*** You have a deep hatred for a particular kind of creature."
def prereq(npc): return npc.race.name == 'Dwarf'
def apply(npc):
    grudgetype = choose("Choose a type of creature: ", ['aberrations', 'beasts', 'celestials', 'constructs', 'dragons', 'elementals', 'fey', 'fiends', 'giants', 'humanoids', 'monstrosities', 'oozes', 'plants', 'undead'])
    if grudgetype == 'humanoids':
        humanoids = [
            'aasimari','dragonborn','dragonmarked','dwarves','elves','genasi',
            'gnomes','half-elves','half-orcs','halflings','humans','merfolk',
            'tieflings','bugbears','dragonkin','gith','gnolls','goblins','half-dragons',
            'half-ogres','hobgoblins','kenku','kobolds','lizardfolk','minotaurs','orcs',
            'sahuagin','sirens','tabaxi','tortles','tritons','yuan-ti'
        ]
        hum1 = choose("Choose a humanoid: ", humanoids)
        hum2 = choose("Choose another humanoid: ", humanoids)

        grudgetype = f"{hum1} and {hum2}"

    ability = choose("Choose an ability: ", ['STR','CON','WIS'])
    if ability == 'STR': npc.STR += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'WIS': npc.WIS += 1

    npc.traits.append(f"***Grudge Bearer: {grudgetype}.*** During the first round of any combat against {grudgetype}, your attack rolls against any of them have advantage. When a {grudgetype} foe makes an opportunity attack against you, it makes the attack roll with disadvantage.")
```
