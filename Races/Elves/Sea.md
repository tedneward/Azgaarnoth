# Sea Elves (*maerach*)
The *maerach* are those elves that chose the oceans and seas as their home, and with Eldar assistance, came to own them as any other elf does their woods. The *maerach* discovered, however, that like the lands they had left, the seas were also home to numerous creatures that sought mastery and domination. *Maerach* have found themselves in conflict with these creatures of the [Undersea](../../Geography/Undersea.md) ever since. Fortunately, the *maerach* retain their ability to breathe air, and have often aided surface mortals against the creatures of the Undersea in exchange for knowledge, tactics, and sometimes even mercenary help. Individual *maerach* are sometimes dispatched to the surface to learn of events there, carry messages, and create friendships, and a few port cities are even called "home" to some *maerach* who find the surface interesting. *Maerach* look strikingly similar to elves, aside from a small set of gills set just below their ears, which long hair (worn loosely) can usually hide.

*Maerach* are a strongly matrilineal society, with family names associated with the birth mother of the elf involved. Families are more "pod"-like in nature, and family bonds are often more fluid than is found in other elvish societies--it is not uncommon to see a *maerach* family pod that consists of multiple adults raising multiple children. Adults in the "pod" are generally loyal to their family, though family disputes often do see a pod member kicked out of the pod (often temporarily, but sometimes permanently), which can lead to *maerach* journeying "abovewater" for a while.

While some *maerach* have settled "abovewater" for long periods of time, most *maerach* consider the sea their homes, and will generally not want to settle anywhere more than a day's walk or ride away from the ocean. (For whatever reason, *maerach* do not consider interior lakes or rivers to be "proper sea"; discussions on the subject usually end quickly as the *maerach* changes the subject.) As a result, any concentration of *maerach* is inevitably in a port city or town, and *maerach* are often engaged "abovewater" in maritime activities--sailors, shipbuilders, or even fishers.

Whether *maerach* have cities in the Undersea is a hotly-debated topic among the non-*maerach*, and one that *maerach* refuse to discuss, even at point of torture.

*Maerach* generally have very good relationships with [tortles](../Tortles.md) and [tritons](../Tritons.md), but are highly prejudiced against [lizardfolk](../Lizardfolk.md), at least at first. Like all elves, *maerach* tend to judge individuals based on their actions as they observe them, but it is not uncommon to see *maerach* loosen weapons at first sight of lizardfolk, or be surprised in combat by devious tortles or tritons.

* **Ability Score Increase**. Your Constitution score increases by 1.

* **Sea Elf Training**. You have proficiency with the spear, trident, light crossbow, and net.

* **Child of the Sea**. You have a swimming speed of 30 feet, and you can breathe air and water.

* **Friend of the Sea**. Using gestures and sounds, you can communicate simple ideas with any beast that has an innate swimming speed.

* **Languages**. You can speak, read, and write Aquan.

```
name = 'Sea'
def level0(npc):
    npc.description.append("***Subrace: Sea Elf.*** *Maerach* look strikingly similar to elves, aside from a small set of gills set just below their ears, which long hair (worn loosely) can usually hide.")

    npc.CON += 1

    npc.proficiencies.append("Spear")
    npc.proficiencies.append("Trident")
    npc.proficiencies.append("Light crossbow")
    npc.proficiencies.append("Net")

    npc.traits.append(traits['sea-emissary'])
    npc.traits.append(traits['amphibious'])
    npc.speed['swimming'] = 30

    npc.languages.append('Aquan')
```
