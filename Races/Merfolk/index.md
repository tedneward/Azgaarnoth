# [Merfolk](../Creatures/Merfolk.md)
Merfolk are an amphibious race, born and at home in the water but comfortable on dry land. Humanoid in form, they have skin of ivory, silver, russet, blue, or deep purple. Long fins extend from the backs of their forearms and calves, and their fingers and toes are webbed. The hairlike growths on their heads are either thick and bristly like the needles of a sea urchin, or long and wavy, resembling fine seaweed. In either case, these growths typically range in color from red to warm brown to black. Male merfolk have similar growths extending down from their cheekbones.

Merfolk are associated with knowledge, logic, and strategy, though the traditional merfolk creeds express this connection in different ways.

* **Ability Score Increase.** Your Charisma score increases by 1.
* **Age.** Merfolk mature at the same rate humans do and reach adulthood around the age of 20. They live considerably longer than humans, though, often reaching well over 100 years.
* **Alignment.** Most merfolk are neutral, though this varies with creeds.
* **Size.** Merfolk are about the same size and build as humans. Your size is Medium.
* **Speed.** Your base walking speed is 30 feet. You also have a swimming speed of 30 feet.
* **Amphibious.** You can breathe air and water.
* **Languages.** You can speak, read, and write Common, Merfolk, Aquan, and one additional language of your choice.

```
name = 'Merfolk'
type = 'humanoid'
def level0(npc):
    npc.description.append("***Race: Merfolk.*** Merfolk are an amphibious race, born and at home in the water but comfortable on dry land. Humanoid in form, they have skin of ivory, silver, russet, blue, or deep purple. Long fins extend from the backs of their forearms and calves, and their fingers and toes are webbed. The hairlike growths on their heads are either thick and bristly like the needles of a sea urchin, or long and wavy, resembling fine seaweed. In either case, these growths typically range in color from red to warm brown to black. Male merfolk have similar growths extending down from their cheekbones.")

    npc.CHA += 1

    npc.size = 'Medium'

    npc.speed['walking'] = 30
    npc.speed['swimming'] = 30

    npc.traits.append(traits['amphibious'])

    npc.languages.append("Common")
    npc.languages.append("Merfolk")
    npc.languages.append("Aquan")
    npc.languages.append("CHOOSE")
```

## Creeds
The merfolk race is divided into three creeds, founded on the principles of [Emeria](Merfolk/Emeria.md) (wind), [Ula](Merfolk/Ula.md) (water), and [Cosi](Merfolk/Cosi.md) (the trickster). A merfolk isn’t born into a creed but chooses it upon reaching adulthood, and it is rare for a merfolk not to choose a creed. Merfolk of the wind and water creeds aren’t hostile to each other, but members of each creed regard the other creed with a vague disdain. Members of both those creeds regard the Cosi creed with suspicion and some degree of fear, and Cosi-creed adherents tend to keep their affiliation secret. Choose one of these creeds for your character.

Some scholars believe that the Merfolk creeds are actually an ancient deviation from the Three-in-One religion of the [Trinitarians](../Religions/Trinitarian.md), split long ago and developed in isolation from one another. Whether this is true is not known, to either Merfolk or the Trinitarians.


