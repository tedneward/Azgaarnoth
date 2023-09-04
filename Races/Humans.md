# Humans
Owing to the prodigious rate at which humans reproduce, they are the dominant species of the Azgaarnothian lands. Owing to the 8,000-plus years of intermixing, humans characteristics are all over the map--different skin tones, different complexions, heights, weights, and so on. Humans were the servant race of the Eldar and flourished and took over much of the lands after the Fall. It is not clear if humans were created by the Eldar, or were uplifted by them. Either way, humans owe their civilization to the initial one built by the Eldar, inheriting it after the Fall."

Humans may be [dragonmarked](Dragonmarked.md) with the Mark of Handling, the Mark of Making, the Mark of Passage, or the Mark of Sentinel; see that entry for details.

Human society is broken into several distinct cultures: [Al'Uma](../Cultures/AlUma.md), [Gozdor](../Cultures/Gozdor.md), [Anor](../Cultures/Anor.md), and [Dail](../Cultures/Dail.md).

* **Ability Score Increase.** Two of your ability scores each increase by 1.

* **Age.** Humans reach adulthood in their late teens and live less than a century.

* **Size.** Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Skills.** You gain proficiency in one skill of your choice.

* **Feat.** You gain one [Feat](../Classes/Feats.md) of your choice.

* **Languages.** You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.

```
name = 'Human'
type = 'humanoid'
def level0(npc):
    npc.description.append("Owing to the prodigious rate at which humans reproduce, they are the dominant species of the Azgaarnothian lands. Owing to the 8,000-plus years of intermixing, humans characteristics are all over the map--different skin tones, different complexions, heights, weights, and so on. Humans were the servant race of the Eldar and flourished and took over much of the lands after the Fall. It is not clear if humans were created by the Eldar, or were uplifted by them. Either way, humans owe their civilization to the initial one built by the Eldar, inheriting it after the Fall.")

    abilityscoreimprovement(npc)
    abilityscoreimprovement(npc)

    npc.size = 'Medium'
    skillchoice(npc)

    featchoice(npc)

    npc.languages.append("Common")
    npc.languages.append("(choice)")
```
