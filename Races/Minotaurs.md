# [Minotaurs](../Creatures/Minotaur.md)
Minotaurs found in [Yithi](../Nations/Yithi.md) and (less often) [Zhi](../Nations/Zhi.md) are quite strikingly different from their Horde-homed brethren: frequently solitary, thoughtful, and quite committed to rule of law and order. Among the [United Hordes](../Nations/Tragekia.md) they often take leadership roles among the tribes and Houses, exhibiting more physical attributes and less intellectual ones than their northern cousins. Among the [Ulmhorde](../Nations/Ulm.md), minotaurs are frequently solitary champions of cunning physical combat, looking for tests to their skill and strength among their opponents. Many minotaurs of both Tragekian and Ulm descent find life among a mercenary company to be ideal, allowing them ample opportunities to test their prowess and build personal wealth, and many more take to the seas for the same reasons.

```
name = 'Minotaur'
description = "***Race: Minotaur.*** "
type = 'humanoid'
```

## Traits
* **Ability Score Increase**. Your Strength score increases by 2, and your Constitution score increases by 1.

* **Age**. Minotaurs enter adulthood at around the age of 17 and can live up to 150 years.

* **Size**. Minotaurs typically stand well over 6 feet tall and weigh an average of 300 pounds. Your size is Large.

* **Hit Points.** You start with 6d10 + (6 * CON bonus) hit points. Thse are "base" hit points, and do not count as Hit Dice for use during short rest periods, for example. These also do not count as character "levels"; thus, a Minotaur Fighter 1 has 1 Hit Dice and is 1 level, even though they have 6d10 + 1d10 + (7x CON bonuses) total hit points. *(GM's note: For this reason, minotaur PCs should usually be a few levels behind their peers, as a means of keeping balance.)*

* **Speed**. Your base walking speed is 30 feet.

* **Horns**. You are never unarmed. You are proficient with your horns, which are a melee weapon that deals 1d6 + your Strength modifier piercing damage. Your horns grant you advantage on all checks made to shove a creature, but not to avoid being shoved yourself.

* **Goring Rush**. When you use the Dash action during your turn, you can make a melee attack with your horns as a bonus action.

* **Hammering Horns**. When you use the Attack action during your turn to make a melee attack, you can attempt to shove a creature with your horns as a bonus action. You cannot use this shove attempt to knock a creature prone.

* **Menacing.** You	have proficiency in the Intimidation skill. 

* **Languages**. You can speak, read, and write Common.

* **Alignment**. Minotaurs believe in a strict code of honor, and thus tend toward law. They are loyal to the death and make implacable enemies, even as their brutal culture and disdain for weakness push them toward evil.

* **Hybrid Nature**. You have two creature types: humanoid and monstrosity. You can be affected by a game effect if it works on either of your creature types.

```
def level0(npc):
    npc.size = 'Medium'

    npc.hitpoints += dieroll('6d10') + (6 * npc.CONbonus())

    npc.speed['walking'] = 30

    npc.STR += 2
    npc.CON += 1

    npc.skills.append("Intimidation")

    npc.languages.append("Common")

    npc.defer(lambda npc: npc.actions.append(f"***Horns.*** Melee Weapon Attack: {npc.proficiencybonus() + npc.STRbonus()} to it, reach 5ft., one creature. Hit: 1d6 + {npc.STRbonus()} piercing damage. Your horns grant you advantage on all checks made to shove a creature, but not to avoid being shoved yourself."))

    npc.bonusactions.append("***Goring Rush.*** When you use the Dash action during your turn, you can make a melee attack with your horns as a bonus action.")

    npc.bonusactions.append("***Hammering Horns.*** When you use the Attack action during your turn to make a melee attack, you can attempt to shove a creature with your horns as a bonus action. You cannot use this shove attempt to knock a creature prone.")

def generate_name(npc, gender):
    # Female names always end in a vowel
    female_surnames = ['Ayasha', 'Calina', 'Fliara', 'Helati', 'Keeli', 'Kyri', 'Mogara', 'Sekra', 'Tariki', 'Telia']
    # Male names never end in a vowel
    male_surnames = ['Beliminorgath', 'Cinmac', 'Dastrun', 'Edder', 'Galdar', 'Ganthirogan', 'Hecariveran', 'Kyris', 'Tosher', 'Zurgas']
    # Family names
    family_names = ['Artar', 'Athak', 'Bagoslalar', 'Bregan', 'Dheubpurwen', 'Dragazakama', 'Entragath', 'Feldadar', 
        'Heral', 'Jernovalrimi', 'Jernokal', 'Malauth', 'Krasgosian', 'Natimorneh', 'Kaziganthi', 'Lagrangli', 
        'Larenthian', 'Mascun', 'Orilg', 'Sahramar', 'Shiagan', 'Orilgrammar', 'Masral', 'Kulris', 'Manaron', 
        'Sumarr', 'Teskos',  'Zhakan', 'Tanhos', 'Ilhagos']

    if gender == 'female': return random(female_surnames) + " " + random(family_names)
    else: return random(male_surnames) + " " + random(family_names)
```

## Sample minotaur names (from https://www.roll4.net/generators/dd-name-generators/minotaur-name-generator)
Kallia Sulgho
Lysagu Tim
Vabghu Aganth
Vigu Abunga
Kag Brath
Tha Igitel
Aritos Ymios
Ales Dagh
Vlorga Niasoc
Regug Aredem
Tog Panexi
Agho Maeshg
Gnor Anthu
Xoth Narfut
Helion Dig
Zena Ambili
Eronog Zurgu
Farkgo Naros
Cukgin Anoth
Sos Xughe
Cordud Drasikod
Hyginugh Euthes
Pregug Ephos
Wapdud Hylus
Kebub Apigorga
Gog Theldrok
Mab Lagugh
Wingloug Dides
Fog Vron
Pho Omagaa
Dakgu Arfu
Sog Vamyntin
Urmistra Lysopyto
Istomatu Agh
Krug Vergu
Gnarfari Istatok
Saraugug Sughe
The Arek
The Ampia
Frikug Nagno
Snorlena Stollus
Pankrito Amynth
Igmug Irtgu
Zlapduda Zombilon
Ulkagog Igorguka
Bareknar Barotios
Bereneuk Eia
Snug Plaogu
Agh Stios
Arod Daghe
Numhug Hedhanth
Irenia Arodulga
Kallia Ambilon
Naragha Dracle
Ste Dristo
Plamgu Xunas
Solog Ephonica
Torgan Xeneios
Vitgu Chugotur
Athanoti Drastone
Maltorin Ha
Krothagh Ditha
Nergu Eidos
Corim Leios
Rugbu Dios
Herais Zon
Glappho Hiline
Nurghugl Anthu
Hagbu Urgorkga
Ja Fagh
Sugbu Kakgarfu
Xugh Fagh
Vrok Enos
Agape Niastorl
Eudiod Urbaghun
Anassa Papos
Ronkath Zugh
Eutha Oristras
Bargu Niasto
Etkallis Vag