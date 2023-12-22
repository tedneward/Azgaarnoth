# Sirens
Sirens are mercurial creatures who can turn in an instant from lonely to repulsed, from desirous to hateful, from welcoming to irritated, from loving to murderous--and then back again. They are humanoid creatures with birdlike features, with long, slender arms that extend into powerful wings that easily carry their light frames into the air. Their fingers bear sharp claws but are nimble enough to wield weapons and perform fine manipulation. Crests of feathery plumage start between their eyes and cover the backs of their heads.

Sirens are at home along the shallower waters of the Deepwaters. They settle on rocky coasts and remote islands, and even on floating piles of kelp. 

They are fascinated with ships, and enjoy toying with them. One siren might call out to a passing crew for company, only to capriciously draw the ship into an entangling mass of kelp. Another might lure a vessel onto jagged rocks so as to study the wreckage and learn more about the strange contraption. But as time has passed and the number of ships on the waters has increased over the years, a growing number of sirens have decided to satisfy their curiosity by taking positions on ship crews--including, in at least one case, the position of captain.

```
name = 'Siren'
description = "***Race: Siren.*** Sirens are mercurial creatures who can turn in an instant from lonely to repulsed, from desirous to hateful, from welcoming to irritated, from loving to murderous--and then back again. They are humanoid creatures with birdlike features, with long, slender arms that extend into powerful wings that easily carry their light frames into the air. Their fingers bear sharp claws but are nimble enough to wield weapons and perform fine manipulation. Crests of feathery plumage start between their eyes and cover the backs of their heads."
type = 'humanoid'
```

## Features

* **Ability Score Increase.** Your Charisma score increases by 2.
* **Alignment.** Most sirens lean toward chaotic alignment, cherishing the freedom and independence that comes from joining a pirate crew.
* **Size.** Sirens stand about 5 to 6 feet tall, but their bodies are slender and their bones partially hollow to facilitate their flight. Your size is Medium.
* **Speed.** Your base walking speed is 25 feet.
* **Flight.** You have a flying speed of 30 feet. You can’t use your flying speed while you wear medium or heavy armor.
* **Siren’s Song.** You know the [friends](../Magic/Spells/friends.md) cantrip and can cast it without material components.
* **Languages.** You can speak, read, and write Common, Siren, and Aquan.

```
def level0(npc):
    npc.description.append("***Race: Siren.*** Sirens are humanoid creatures with birdlike features. Their long, slender arms extend into powerful wings that easily carry their light frames into the air. Their fingers bear sharp claws but are nimble enough to wield weapons and perform fine manipulation. Crests of feathery plumage start between their eyes and cover the backs of their heads.")

    npc.CHA += 2
    npc.size = 'Medium'
    npc.speed['walking'] = 25
    npc.speed['flying'] = 30

    spellcasting = innatecaster(npc, 'CHA', name)
    spellcasting.cantripsknown.append('friends')

    npc.languages.append('Common')
    npc.languages.append('Siren')
    npc.languages.append('Aquan')
```
