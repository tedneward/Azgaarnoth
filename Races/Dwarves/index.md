# Dwarves
See [*Dwarves*](../../Creatures/Dwarves.md) for more details.

```
name = 'Dwarf'
description = "***Race: Dwarf.*** Dwarves are hardy folk, often usually working in skilled professions. Some have taken up more agrarian roots, choosing to embrace the world of sun and rain, but many dwarves find themselves naturally drawn to lives of practiced skills. Take careful note, though: despite their history, dwarves are just as fond of scroll and pen as they are crossbow and axe. Traditions hold among the dwarven clans, one of those being martial exercise, so most dwarves are trained in some form of weaponry, and likely to fight if antagonized."
type = 'humanoid'
```

* **Ability Score Increase**. Your Constitution score increases by 2.

* **Age**. Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 35. On average, they live about 150 years.

* **Alignment**. Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.

* **Size**. Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.

* **Darkvision**. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Dwarven Resilience**. You have advantage on saving throws against poison, and you have resistance against poison damage.

* **Dwarven Combat Training**. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.

* **Tool Proficiency**. You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.

* **Stonecunning**. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.

* **Languages**. You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.

```
def level0(npc):
    npc.CON += 2
    npc.size = 'Medium'
    npc.speed['walking'] = 25
    npc.senses['darkvision'] = 60
    npc.damageresistances.append('poison')
    npc.traits.append("***Dwarven Resilience.*** You have advantage on saving throws against poison.")
    npc.proficiencies.append("Battleaxe")
    npc.proficiencies.append("Hand axe")
    npc.proficiencies.append("Light hammer")
    npc.proficiencies.append("Warhammer")
    npc.proficiencies.append(choose("Choose a tool proficiency:", ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]))
    npc.traits.append("***Stonecunning.*** Whenever you make an Intelligence (History) check related to the origin of stonework, it is considered proficient in the History skill and add doubles its proficiency bonus to the check.")
```

Dwarves have a number of genetically-differentiated offshoots (subraces):

* [Hill](Hill.md) and [Mountain](Mountain.md) dwarves are the core stock of dwarvish lineage.
* [Ember](Ember.md) dwarves are commonly found in the eastern Daws mountains, near the only active volcanic region in Azgaarnoth, but many have emigrated away to all corners of the continent(s).
* [Stone](Stone.md) dwarves lived (and live still) for entire generations in the Underdark.
* [Tundra](Tundra.md) dwarves are those who have embraced the endless plains of the surface as their home.
* [Dark](Dark.md)
* [Mark of Warding Dragonmark](Warding.md)

```
def generate_name(npc, gender):
    def generate_firstname():
        names = [
            'Alaron', 'Aldrek', 'Ardo',
            'Barazak', 'Balur', 'Bombur', 'Bofur', 'Bnar',
            'Chakrir', 'Carnir', 'Cadmael',
            'Dendirsyr', 'Dorn', 'Dophensus',
            'Erwid', 'Erli', 'Ednir',
            'Farsben', 'Fili', 'Fordreth', 'Fenzig',
            'Gadaric', 'Gimli', 'Graflyn', 'Gunder', 'Goltan', 'Grimn', 'Grisbane',
            'Haldrik', 'Heimoc', 'Helsbid', 'Helwright', 'Hoskuld',
            'Kalhor', 'Karsten', 'Kenth', 'Kili', 'Kulderik', 'Kellan', 'Kardnyr', 'Krael',
            'Kall',
            'Lornir', 'Lorik', 'Laron',
            'Maarik', 'Meli', 'Mostyr',
            'Nomir',
            'Ostrin',
            'Ryonn',
            'Thorin', 'Thordrik', 'Thorstyr', 'Thaladan', 'Tomir',
            'Valamar', 'Valdan',
        ]
        return generate_name(names)

    def generate_lastname():
        # Dwarven lastnames are often two-parters
        prenouns = [
            'strong', 'steady', 'barren',
            'mountain','hill','cliff','range','mine','crag','storm','root',
            'sword', 'spear', 'axe', 'hammer',
            'two', 'three', 'four',
            'shaft', 'haft',
            'wolf', 'bear', 'tiger', 'rat', 'troll', 'dragon',
            'eagle','raven','hawk','hen',
            'brown', 'gray', 'green', 'black', 'red',
            'coal', 'shale', 'iron', 'oak', 'steel', 'gravel',
            'wooden','oaken','ivy',
            'fire','earth','air','water','lightning','thunder','psychic',
        ]
        postnouns = [
            'mountain','hill','cliff','range','mine','crag','storm','root',
            'gates',
            'sword', 'spear', 'axe', 'hammer', 'shield',
            'hand','tongue', 'skull', 'blood', 'fist',
            'talon','claw','beak','hawk',
            'borne', 'heim', 'bane',
            'pants','vest','tunic','shirt',
            'smith','shadow',
        ]
        verbs = [
            'breaker','smiter','hewer','slasher','stealer'
        ]
        if random.randint(0,1) == 0:
            part1 = prenouns[random.randint(0, len(prenouns)-1)].capitalize()
            part2 = postnouns[random.randint(0, len(postnouns)-1)]
            return f"{part1}{part2}"
        else:
            part1 = prenouns[random.randint(0, len(prenouns)-1)].capitalize()
            part2 = verbs[random.randint(0, len(verbs)-1)]
            return f"{part1}{part2}"
    return f"{generate_firstname()} {generate_lastname()}"
```
