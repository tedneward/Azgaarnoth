# Dwarves
See [*Dwarves*](../Creatures/Dwarves.md) for more details.

```
name = 'Dwarf'
type = 'humanoid'
subraces = {}
```

* **Ability Score Increase**. Your Constitution score increases by 2.

* **Age**. Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.

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
    npc.size = Medium
    npc.speed['walking'] = 25
    npc.senses['darkvision'] = "60ft"
    npc.resistances.append('poison')
    npc.features.append("***Dwarven Resilience.*** The dwarf has advantage on saving throws against poison.")
    npc.proficiencies.append("Battleaxe")
    npc.proficiencies.append("Hand Axe")
    npc.proficiencies.append("Light Hammer")
    npc.proficiencies.append("Warhammer")
    npc.proficiencies.append(choose("Choose a tool proficiency:", ["Smith's Tools", "Brewer's Supplies", "Mason's Tools"]))
    npc.features.append("***Stonecunning.*** Whenever the dwarf makes an Intelligence (History) check related to the origin of stonework, it is considered proficient in the History skill and add doubles its proficiency bonus to the check.")
```

Dwarves have a number of genetically-differentiated offshoots (subraces):

* [Hill](#hill-dwarf)
* [Mountain](#mountain-dwarf)
* [Dark](#dark-dwarf)

---

## Hill Dwarf
The hill and mountain dwarves are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the hills as part of their guild/clan, and mountain dwarves are often found in mountains for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Dwarven Toughness**. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.

```
def hill():
    print('Hello from hill()')
    def level0(npc):
        npc.WIS += 1

    def dwarventoughness(npc):
        npc.hitpoints += 1

    return {
        'name' : 'Hill',
        'level0' : level0,
        'level1' : dwarventoughness,
        'level2' : dwarventoughness,
        'level3' : dwarventoughness,
        'level4' : dwarventoughness,
        'level5' : dwarventoughness,
        'level6' : dwarventoughness,
        'level7' : dwarventoughness,
        'level8' : dwarventoughness,
        'level9' : dwarventoughness,
        'level10' : dwarventoughness,
        'level11' : dwarventoughness,
        'level12' : dwarventoughness,
        'level13' : dwarventoughness,
        'level14' : dwarventoughness,
        'level15' : dwarventoughness,
        'level16' : dwarventoughness,
        'level17' : dwarventoughness,
        'level18' : dwarventoughness,
        'level19' : dwarventoughness,
        'level20' : dwarventoughness
    }

subraces['hill'] = hill()
```

---

## Mountain Dwarf
The hill and mountain dwarves are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the hills as part of their guild/clan, and mountain dwarves are often found in mountains for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them.

* **Ability Score Increase**. Your Strength score increases by 2.

* **Dwarven Armor Training**. You have proficiency with light and medium armor.

```
def mountain():
    def level0(npc): 
        npc.STR += 2
        npc.proficiencies.append("Light armor")
        npc.proficiencies.append("Medium armor")

    return {
        'name': 'Mountain',
        'level0': level0
    }

subraces['mountain'] = mountain()
```

---

## Dark Dwarf 
([*duergar*](../../Creatures/Duergar.md))

Histories tell of clans of dwarves that never participated as part of the Exodus (or were left behind either accidentally or deliberately, depending on the rumor), and were forced into hard living and driven deeper into the depths to survive. The *duergar*'s legends claim that those clans were captured by the *illithid* (mind flayers) at the same time elves were captured (who later became the [Gith](../Gith.md)).

Most dwarves consider the "dark dwarves" to be myth, but the *duergar* are real, whatever their history. Rumors of *duergar* generally also tie into the rumors of tunnels that connect the western and eastern reaches of the Daw mountain range underneath the Ravensound, as such tunnels would provide adequate depth to hide them from the Hordes that precipitated the Exodus.

Most of the *duergar* encountered tend to be bitter and resentful, angry at the dwarves for their collective racial pain, with little to no remorse for the dwarves' own tragedies or history. *Duergar* are often paranoid and shun outsiders, though many that have come into contact with surface-dwellers have slowly adjusted their feelings and expectations accordingly. *Duergar* society is clan-based, much like the dwarves' was prior to the Exodus, and the bonds of clan often supersede all other concerns and obligations, even unto death.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Superior Darkvision**. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Duergar Resilience**. You have advantage on saving throws against illusions and against being charmed or paralyzed.

* **Duergar Magic**. When you reach 3rd level, you can cast the [enlarge/reduce](../../Magic/Spells/enlarge-reduce.md) spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the [invisibility](../../Magic/Spells/invisibility.md) spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.

* **Sunlight Sensitivity**. You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.

```
def duergar():
    def level0(npc): 
        npc.STR += 1
        npc.senses['darkvision'] = '120 ft'
        npc.proficiencies.append("Light armor")
        npc.proficiencies.append("Medium armor")

    return {
        'name': 'Duergar',
        'level0': level0
    }

subraces['duergar'] = duergar()
```
