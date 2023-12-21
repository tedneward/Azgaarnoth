# Humans
Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human’s memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics.Owing to the prodigious rate at which humans reproduce, they are the dominant species of the Azgaarnothian lands. Owing to the 8,000-plus years of intermixing, humans characteristics are all over the map--different skin tones, different complexions, heights, weights, and so on.

Humans were the servant race of the Eldar and flourished and took over much of the lands after the Fall. It is not clear if humans were created by the Eldar, or were uplifted by them. Either way, humans owe their civilization to the initial one built by the Eldar, inheriting it after the Fall. Human society is broken into several distinct cultures: [Al'Uma](../../Cultures/AlUma.md), [Gozdor](../../Cultures/Gozdor.md), [Anor](../../Cultures/Anor.md), and [Dail](../../Cultures/Dail.md).

```
name = 'Human'
description = "***Race: Human.*** Humans are the most adaptable and ambitious people among the common races. They have widely varying tastes, morals, and customs in the many different lands where they have settled. When they settle, though, they stay: they build cities to last for the ages, and great kingdoms that can persist for long centuries. An individual human might have a relatively short life span, but a human nation or culture preserves traditions with origins far beyond the reach of any single human’s memory. They live fully in the present — making them well suited to the adventuring life — but also plan for the future, striving to leave a lasting legacy. Individually and as a group, humans are adaptable opportunists, and they stay alert to changing political and social dynamics.Owing to the prodigious rate at which humans reproduce, they are the dominant species of the Azgaarnothian lands. Owing to the 8,000-plus years of intermixing, humans characteristics are all over the map--different skin tones, different complexions, heights, weights, and so on."
type = 'humanoid'
```

* **Ability Score Increase.** Two of your ability scores each increase by 1.

* **Age.** Humans reach adulthood in their late teens and live less than a century.

* **Size.** Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium.

* **Speed.** Your base walking speed is 30 feet.

* **Skills.** You gain proficiency in one skill of your choice.

* **Feat.** You gain one [Feat](../../Feats/) of your choice.

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

```
# From https://www.roll4.net/generators/dd-name-generators/dnd-human-name-generator
def generate_name(npc, gender):
    female_firstnames = [
        'Ustice','Ey','Pari','Cora','Ulia','Lla','La','Hali','Zoe','Jeanor','Ypri',
        'Charle','Zie','Ker','Xaris','Ta','Premila'
    ]
    male_firstnames = [
        'Pert','Quincy','Son','Junter','Jonald','Ver','Xan','Eonald','Oinn','Hannon',
        'Isdel','Del','Yer','Ylis','Yaelan','Arker','Wan','Adler','Camen','Caseer',
        'Premilan','Ulan','Xaris','Tayler','Lyn'
    ]
    
    last_names = [
        'We','Ynn','Mpson','Va','Wang','Aross','Barrin','Yncano','Guerre','Krajas',
        'Ser','Guerra','An','Pez','Pruz','Ussen','Corte','Ton','Ubbott','Na','Gers',
        'Quinn','Crosby','Sam','Rince','Ke','Quez','Quinne','Goosethorn',
        'Winterscreamer','Snakewing','Icestriker','Camelcrawl','Fallseeker',
        'Oathbreak','Jaguarscreamer','Crocchaser','Windhold','Tigerwind',
        'Tigerbone','Lionbone','Bearwind','Starlove','Lightforge','Morningbinder',
        'Cranepunch','Wolfguts'
    ]

    return (random(female_firstnames) if gender == 'female' else random(male_firstnames)) + random(last_names) 
```
