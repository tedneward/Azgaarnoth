# Humans
Owing to the prodigious rate at which humans reproduce, they are the dominant species of the Azgaarnothian lands. Owing to the 8,000-plus years of intermixing, humans characteristics are all over the map--different skin tones, different complexions, heights, weights, and so on. Humans were the servant race of the Eldar and flourished and took over much of the lands after the Fall. It is not clear if humans were created by the Eldar, or were uplifted by them. Either way, humans owe their civilization to the initial one built by the Eldar, inheriting it after the Fall.

Human society is broken into several distinct cultures: [Al'Uma](../Cultures/AlUma.md), [Gozdor](../Cultures/Gozdor.md), [Anor](../Cultures/Anor.md), and [Dail](../Cultures/Dail.md).

```
name = 'Human'
description = "***Race: Human.*** Humans were the servant race of the Eldar and flourished and took over much of the lands after the Fall. It is not clear if humans were created by the Eldar, or were uplifted by them. Either way, humans owe their civilization to the initial one built by the Eldar, inheriting it after the Fall."
type = 'humanoid'
```

* **Ability Score Increase.** Two of your ability scores each increase by 1.

* **Age.** Humans reach adulthood in their late teens and live less than a century.

* **Size.** Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Skills.** You gain proficiency in one skill of your choice.

* **Feat.** You gain one [Feat](../Classes/Feats.md) of your choice.

* **Languages.** You can speak, read, and write Common and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with words borrowed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on.

```
def level0(npc):
    npc.size = 'Medium'
    npc.speed['walking'] = 30

    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    for _ in range(0, 2):
        ability = choose("Choose an ability to improve: ", abilities)
        if ability == 'STR': npc.STR += 1
        elif ability == 'DEX': npc.DEX += 1
        elif ability == 'CON': npc.CON += 1
        elif ability == 'INT': npc.INT += 1
        elif ability == 'WIS': npc.WIS += 1
        elif ability == 'CHA': npc.CHA += 1

    chooseskill(npc)

    choosefeat(npc)

    npc.languages.append("Common")
    npc.languages.append("CHOOSE")
```

Humans may be [dragonmarked](Dragonmarked.md) with the [Mark of Handling](Handling.md), the [Mark of Making](Making.md), the [Mark of Passage](Passage.md), or the [Mark of Sentinel](Sentinel.md). Or not, as they choose.

## Sample human names (from https://www.roll4.net/generators/dd-name-generators/dnd-human-name-generator)
Ustice We
Pert Ynn
Pari Mpson
Ey Va
Quincy Wang
Cora Aross
Junter Barrin
Ulia Yncano
Jonald Guerre
Ver Krajas
Lla Ser
Xan Guerra
Son An
La Pez
Hali Pruz
Zoe Ussen
Oinn Ls
Jeanor Ccorte
Eonald Ton
Ypri Ubbott
Larkez Na
Jaelan Gers
Vel Quinn
Hannon Ice
Is Crosby
Del Sam
Yer Rrince
Ylis Ke
Ver Quez
Von Things
Yaelan As
Arker Quinne
Wan Quez
Zie Mccars
Charle No
Pen Ton
Van Dman
Tt Boyd
Xer Pson
Kly Villo
Icky Goosethorn
Zan Winterscreamer
St Snakewing
Ker Icestriker
Camen Camelcrawl
Macey Fallseeker
Ulan Jaguarscreamer
Ley Oathbeak
Xer Crocodilechaser
Caseer Windwind
Xaris Tigerhold
Tayler Lionbone
An Bearlove
Ta Starwind
Adler Lightforge
Madel Morningbinder
Zie Geckodestroyer
Premilan Cranepunch
Lyn Havocbash
Ugh Wolfgutz