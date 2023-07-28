"""
# Tritons
Tritons guard the ocean depths, building small settlements beside deep trenches, portals to the elemental planes, and other dangerous spots far from the eyes of land-bound folk. Long-established guardians of the deep ocean floor, the noble tritons have gradually become increasingly active in the world above.

* **Ability Score Increase**. Your Strength, Constitution, and Charisma scores each increase by 1.

* **Age**. Tritons reach maturity around age 15 and can live up to 200 years.

* **Alignment**. Tritons tend toward lawful good. As guardians of the darkest reaches of the sea, their culture pushes them toward order and benevolence.

* **Size**. Tritons are slightly shorter than humans, averaging about 5 feet tall. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet, and you have a swimming speed of 30 feet.

* **Amphibious**. You can breathe air and water.

* **Control Air and Water**. A child of the sea, you can call on the magic of elemental air and water. You can cast [fog cloud](/Magic/Spells/fog-cloud.md) with this trait. Starting at 3rd level, you can cast [gust of wind](/Magic/Spells/gust-of-wind.md) with it, and starting at 5th level, you can also cast [wall of water](/Magic/Spells/wall-of-water.md) with it. Once you cast a spell with this trait, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.

* **Emissary of the Sea**. Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.

* **Guardians of the Depths**. Adapted to even the most extreme ocean depths, you have resistance to cold damage, and you ignore any of the drawbacks caused by a deep, underwater environment.

* **Languages**. You can speak, read, and write Common and Aquan.
"""
name = "Triton"
def apply_race(npc):
    npc.description.append("Tritons guard the ocean depths, building small settlements beside deep trenches, portals to the elemental planes, and other dangerous spots far from the eyes of land-bound folk. Long-established guardians of the deep ocean floor, the noble tritons have gradually become increasingly active in the world above.")

    npc.STR += 1
    npc.CON += 1
    npc.CHA += 1

    npc.size = 'Medium'

    npc.speed = '30ft; swimming 30ft'

    npc.features.append(commonfeatures['amphibious'])

    npc.actions.append("**Control Air and Water**. You can cast [fog cloud](/Magic/Spells/fog-cloud.md) with this trait. Once you cast a spell with this trait, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.")

    npc.features.append("**Emissary of the Sea**. Aquatic beasts have an extraordinary affinity with your people. You can communicate simple ideas with beasts that can breathe water. They can understand the meaning of your words, though you have no special ability to understand them in return.")

    npc.resistances.append("cold")
    npc.features.append("**Guardians of the Depths**. Adapted to even the most extreme ocean depths, you have resistance to cold damage, and you ignore any of the drawbacks caused by a deep, underwater environment.")
    
    npc.languages.append("Common")
    npc.languages.append("Aquan")

subraces = []

def level3(npc):
    replace("**Control Air and Water**.", npc.actions, "**Control Air and Water**. You can cast [fog cloud](/Magic/Spells/fog-cloud.md) or [gust of wind](/Magic/Spells/gust-of-wind.md) with this trait. Once you cast a spell with this trait, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.")

def level5(npc):
    replace("**Control Air and Water**.", npc.actions, "**Control Air and Water**. You can cast [fog cloud](/Magic/Spells/fog-cloud.md), [gust of wind](/Magic/Spells/gust-of-wind.md) or [wall of water](/Magic/Spells/wall-of-water.md) with this trait. Once you cast a spell with this trait, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.")
