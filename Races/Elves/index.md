# [Elves](../Creatures/Elves.md)
Elves may be [dragonmarked](Dragonmarked.md) with the Mark of Shadow; see that entry for details.

```
name = 'Elf'
description = "***Race: Elf.*** Elves are almost as diverse as humans in their occupations, entertainments, and while most elves have a strong familial tie between them, numerous elves have wandered away from home to make their mark within the world, then to return and take up familial responsibilities. Elves revere their familial ancestors, and will often have a shrine to a favored ancestor, but elves do not see their familial ancestors as gods, and many elves are quite comfortable serving in a religious order even as they put offerings to their revered ancestors out on important holidays."
type = 'humanoid'
```

* **Ability Score Increase**. Your Dexterity score increases by 2.

* **Age**. Although elves reach physical maturity at about the same age as humans, the elven understanding of adulthood goes beyond physical growth to encompass worldly experience. An elf typically claims adulthood and an adult name around the age of 25 and most can live to be 150 years old.

* **Alignment**. Elves love freedom, variety, and self-expression, so they lean strongly towards the gentler aspects of chaos. They value and protect others' freedom as well as their own, and are good more often than not.

* **Size**. Elves range from under 5 to over 6 feet tall and have slender builds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Darkvision**. Accustomed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Fey Ancestry**. You have advantage on saving throws against being charmed, and magic can't put you to sleep.

* **Trance**. Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is "trance". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.

* **Keen Senses**. You have proficiency in the Perception skill.

* **Languages**. You can speak, read, and write Common and Elven.

```
def level0(npc):
    npc.DEX += 2

    npc.size = 'Medium'
    npc.speed['walking'] = 30

    npc.senses['darkvision'] = 60

    npc.traits.append(traits['fey-ancestry'])

    npc.conditionimmunities.append("sleep")

    npc.traits.append("***Trance.*** Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is 'trance'. While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.")

    npc.skills.append("Perception")

    npc.languages.append("Common")
    npc.languages.append("Elven")
```

Elves have a number of genetically-differentiated offshoots (subraces):

* [Bright Elves](Elves/Bright.md)
* [High Elves](Elves/High.md)
* [Wood Elves](Elves/Wood.md)
* [Fey Elves](Elves/Fey.md)
* [Winged Elves](Elves/Winged.md)
* [Wild Elves](Elves/Wild.md)
* [Sea Elves](Elves/Sea.md)
* [Shadow Elves](Elves/Shadow.md)
* [Dark Elves](Elves/Dark.md)

```
def generate_name(npc):
    def generate_malefirstname():
        return generatemarkovname([
            'Adorellan','Ailluin','Airdan','Akkar','Aumanas',
            'Conall',
            'Ehlark','Eldaerenth','Elidyr',
            'Ganamede',
            'Halueve','Horith',
            'Illianaro','Ivaran','Iymbryl',
            'Jaonos',
            'Kellam','Kharis',
            'Lathlaeril',
            'Navarre','Nym',
            'Olaurae','Ornthalas',
            'Rilitar','Riluaneth','Ruven',
            'Sythaeryn',
            'Toross',
            'Usunaar',
        ])
    def generate_femalefirstname():
        return generatemarkovname([
            'Aila','Arthia','Allisa','Aerilaya','Ashera','Aravae',
            'Bemere',
            'Clanire','Cithrel',
            'Elincia','Elmyra','Edraele',
            'Fayeth','Faraine',
            'Hamalitia','Hycis',
            'Immianthe',
            'Kilyn',
            'Leilatha',
            'Madris','Melarue',
            'Nueleth','Nyana','Naexi',
            'Phaerille','Phyrra','Pyria',
            'Sana','Shaerra','Syllia','Sorisana',
            'Thaciona','Thasinia','Tanelia',
            'Vaeri',
            'Yalanue',
            'Zentha',
        ])

    def generate_lastname():
        return generatemarkovname([
            'Adsys','Aetumal','Aehana','Aegwyn',
            'Bryxalim','Brynelis','Brygolor',
            'Cargwyn','Crawenys','Carna,
            'Dalee','Damyar',
            'Elkian','Enris',
            'Faedove','Farralei','Faquinal',
            'Genthyra',
            'Hervalur',
            'Ianhana','Ianxalim','Iliqen','Ilihorn',
            'Keagella','Krisceran','Kelthana',
            'Liaqirelle','Luroris','Luwynn','Luzorwyn,
            'Magwenys','Miafir','Miaharice','Morleth',
            'Norbalar',
            'Olahana','Olawraek','Omasatra','Oloro',
            'Papeiros',
            'Ralofir','Ravagolor','Rogwyn','Ralogeiros',
            'Sarjor','Shapeiros','Sylmaer',
            'Thefiel','Tramaer',
            'Ulasatra','Ulawynn','Urikalyn',
            'Venmenor','Valsys','Virmaer','Vathyra','Venmyar',
            'Wranrora','Wynlen','Wysaroris','Wynceran','Waesxisys',
            'Yeszeiros','Yinthana','Yesfir','Yindithas','Yllakalyn',
            'Zinynore','Zinlen','Zylrie',
        ])

    return f"{generate_malefirstname() if npc.gender == 'Male' else generate_femalefirstname()} {generate_lastname()}"
```

#### Male
Alwin Herwenys
Ellisar Herthana
Raibyn Naewenys
Rhistel Elacan
Elephon Quijor
Saevel Wranrie
Zaos Elasys
Almar Elkalyn
Kivessin Kelkrana
Grathgor Mormaris
Kellam Rolee
Alinar Fennelis
Aithlin Wranmaris
Halueth Leobanise
Erendriel Bryhorn
Intevar Yesbalar
Elashor Elrona
Ayred Reytoris
Grathgor Faedi
Drannor Yelthana
Jandar Elafina
Rhothomir Beigolor
Laiex Yllajeon
Merellien Genydark
Garrik Aeharice
Iliphar Xilceran
Ardreth Glynzana
Cohnal Yinwenys
Gorred Oriyarus
Elas Bihice
Gorluin Miadove
Kelvhan Carnan
Elkhazel Ravazorwyn
Elorshin Leokrana
Navarre Liacyne
Katar Aracyne
Klaern Daehana
Abarat Balzeiros
Abarat Aerona
Adamar Aegwyn

#### Female Names
Gaelira Xilynore
Micaiah Sarneiros
Faylen Kelsalor
Vestele Heithana
Lyndis Yllaran
Syvis Farmys
Sumina Qilynn
Shalaevar Keaphyra
Nakiasha Rowynn
Tephysea Yeswenys
Artin Vabella
Ynaselle Lufir
Sakaala Qingella
Lenna Eilren
Darshee Virxina
Liluth Pamoira
Chaenath Waesnala
Keenor Miaro
Shanaera Araxina
Ratha Daekrana
Leena Perric
Imra Wysaydark
Lensa Faexina
Meira Qinqen
Lusserina Ilinorin
Ahrendue Elaro
Rophalin Zinyra
Alanis Venyra
Lithoniel Grecyne
Nuovis Magdan

#### Neutral
Taleasin Lorajor
Haemir Aethana
Gorre Waesvaris
Ailuin Chaeneiros
Jhaartael Xyrralei
Luthais Balstina
Elre Triszana
Folluin Enwynn
Darunia Thefiel
Jhaeros Yesrora
Ellisar Kelstina
Paeris Royarus
Ithronel Qinberos
Tamnaeth Nerineiros
Cohnal Gilhana
Cyran Kelsatra
Ilphas Lumaris
Artin Olohorn
Sinaht Ronan
Halaema Xilwraek
Sinaht Sarlamin
Erendriel Heinorin
Imizael Fenmaer
Kharis Xilphine
Vaeril Ianyarus
Alosrin Arapeiros
Naevys Loranala
Ciradyl Heican
Iliphar Olobella
Neremyn Wynxalim
Goren Presrel
Isilynor Umetumal
Vulwin Omamys
Ailre Yellen
Zeno Vazeiros
Wynather Torthyra
Aimer Zinvyre
Elas Gilwenys
Myriil Farberos
Cornaith Yessandoral
Syvis Bryrel
Ciradyl Thegwyn
Mnementh Bilana
Elanil Wynren
Dain Waesvalur
Kailu Eldan
Tamnaeth Erynore
Alais Sargella
Saida Elro
Tannyll Venric