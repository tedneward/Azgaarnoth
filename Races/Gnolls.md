# Gnoll
*(see [Gnolls](../Creatures/Gnolls.md) for more details)*

For gnoll player characters, an important part of the backstory will include the gnoll's relationship to its former pack--were they exiled for having thoughts too different from the rest? Were they the sole survivor of a raid (or reprisal) and left for dead, only to survie but forever in search of a new pack to join? Or are they embittered individualists who seek to prove they need no pack (thanks to some earlier trauma that left them suspicious or distrustful of others)? The longer a gnoll travels with the same group of people, the more loyalty the gnoll will develop to that group, such that (at the DM's discretion) a gnoll may resist enchantments and commands that would cause harm to the members of their adoptive pack (either by gaining advantage on saving throws to resist, by gaining additional chances to resist, or by shortening the time under enchantment, again all at the DM's discretion).

```
name = 'Gnoll'
description = "***Race: Gnoll.*** Gnolls are brutal hunters with a demonic ancestry who are fiercely loyal to their pack."
type = 'humanoid'
```

## Gnoll Traits
Gnolls are brutal hunters with a demonic ancestry who are fiercely loyal to their pack.

* **Ability Score Increase.** Your Strength score increases by 2 and your Dexterity score increases by 1.

```
def level0(npc):
    npc.STR += 2
    npc.DEX += 1
```

* **Age.** Gnolls reach adulthood by the age of 20 and live to around 80.
* **Alignment.** Gnolls are usually chaotic neutral or evil, though there are exceptions.
* **Size.** Most gnolls are between 6 and 7 feet tall. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed.** Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision.** You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Bite.** You are proficient with your bite attack, which is a melee weapon attack that deals 1d6 piercing damage plus your Strength modifier.

```
    npc.defer(lambda npc: npc.actions.append(f"***Bite.*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d6 + {npc.STRbonus()} piercing damage."))
```

* **Rampage.** When you reduce a creature to 0 hit points with a melee attack on your turn, you may, use a bonus action to move up to half your speed and make a bite attack.

```
    npc.bonusactions.append("***Rampage.*** After you reduce a creature to 0 hit points with a melee attack on its turn, the you can move up to half your speed and make a Bite attack.")
```

* **Frightful Appearance.** You are proficient in the Intimidation skill.

```
    npc.skills.append("Intimidation")
```

* **Languages.** You can speak, read, and write Common and Gnoll. You can also understand, but not speak, read or write Abyssal unless learnt through other features.

```
    npc.languages.append("Common")
    npc.languages.append("Gnoll")
    npc.languages.append("Abyssal (can understand but not speak, read, or write)")
```


## Gnoll Names
The brutality of gnolls is reflected even in their names which tend to have many harsh consonants.

Male: Dagnyr, Dhyrn, Doryc, Ghyrryn, Gnasc, Gnoryc, Gnyrn, Hyrn, Lhoryn, Lhyr, Mognyr, Sorgnyn, Thyrn, Toryc, Yrgnyn, Yrych

Female: Dagnyra, Gnara, Gnora, Gnyrl, Hyra, Hyrgna, Lhyra, Lhyrl, Malgna, Myrl, Sargna, Shyrla, Tarnyra, Yrgna

```
def generate_name(npc):
    female_surnames = [
        'Dagnyra', 'Gnara', 'Gnora', 'Gnyrl', 'Hyra', 'Hyrgna', 'Lhyra', 'Lhyrl', 'Malgna', 'Myrl', 'Sargna', 'Shyrla', 'Tarnyra', 'Yrgna'
    ]
    male_surnames = [
        'Dagnyr', 'Dhyrn', 'Doryc', 'Ghyrryn', 'Gnasc', 'Gnoryc', 'Gnyrn', 'Hyrn', 'Lhoryn', 'Lhyr', 'Mognyr', 'Sorgnyn', 'Thyrn', 'Toryc', 'Yrgnyn', 'Yrych'
    ]
    # Family names
    family_names = [
        'Artar', 'Athak', 
        'Bagoslalar', 'Bregan', 
        'Dheubpurwen', 'Dragazakama', 
        'Entragath', 
        'Feldadar', 
        'Heral', 
        'Ilhagos',
        'Jernovalrimi', 'Jernokal', 
        'Krasgosian', 'Kaziganthi', 'Kulris', 
        'Lagrangli', 'Larenthian', 
        'Malauth', 'Mascun', 'Masral', 'Manaron', 
        'Natimorneh',  
        'Orilg', 'Orilgrammar', 
        'Sahramar', 'Shiagan','Sumarr',
        'Tanhos', 'Teskos',  
        'Zhakan', 
    ]

    return (random(female_surnames) if npc.gender == 'Female' else random(male_surnames)) + " " + random(family_names)
```

#### Names
Uz Riverguise
Mok Faildent
Thek Lumphand
Yh Fungihunter
Ozz Dreckclaw
Dozyn Brinefoot
Manor Sootshrapnel
Gnokkex Oozedeath
Thotyh Rivercheek
Exukx Soilhunter
Eh Fizzlewatch
Gnakk Muckmouth
Rokk Brokenboot
Khuazz Fasttooth
Ix Soilboot
Vikxiah Foameyes
Trargen Ashbash
Krerrgark Crackedtoes
Brarguk Snorehallow
Urgyz Burstguard
Kurrg Sandcheek
An Zesttine
Rrykk Clayhands
Drark Zestfoot
Kux Sootscowl
Ikxukk Fizzleclub
Gnakkourk Fungiguise
Aarrguz Soilhead
Tryxurr Snothook
Gekkiar Ashgaze
Grerg Damptalon
Gheirrg Moledance
Gnyc Dirtfists
Brar Rivernail
Rrorr Crackedteeth
Tiruokx Mucuswizzle
Gnakxaz Oozegall
Grourkurrg Staingob
Rrikkun Scumbrass
Gytouzz Loosefrown

#### Female names
Thaas Groundgrappler
Syr Farear
Der Dreckfuse
Snaz Bloodbrass
Yhz Crackmug
Snazna Goldsmile
Tregrarh Claymouth
Ehrras Goreshrapnel
Rheizho Fizzlepinch
Hazrysh Groundpinch
Aahn Grapplecrook
Vu Zestears
Nu Snottoe
Trra Dusthunter
Trohz Scumfrown
Ealmohr Scumfrown
Uigohr Dustfangs
Hahze Clayfrown
Seirtru Fungicheek
Khotzsa Gorescrap
Hruh Frothbash
Tez Scumfinger
Saz Deadtoe
Zyr Crackedfists
Or Dampblast
Trihlar Bloodtine
Tratzoh Rotmaw
Meavgurth Molesnag
Trrathmuth Grapplemask
Usnihn Greasewatch
Ehn Mudtusk
Zah Blightdance
Do Failfinger
Vus Rentwizzle
Khi Brinecheek
Ortesh Sootnail
Kheggeah Snotbeam
Dralgo Gunkgrinder
Snarihr Blightclash
Mruizhor Snorehand

#### Neutral names
Veh Deadhead
Srot Ashmouth
Rror Burstsnag
Oth Sorenails
Xol Fungihead
Krumih Pesthead
Traanvoum Murkcast
Vygrrua Deadeye
Grouznu Scumshrapnel
Souhzyh Mireface
Rurr Farnail
Thrua Sootgrapnel
Gu Ashtine
Grih Saltfangs
Thru Gorescrap
Thryzsin Oozeblast
Rroryc Fizzlecloak
Urlait Zestgaze
Zudo Rotgleam
Gnogvorr Sweatfangs
Therr Stainfingers
Ih Goldclash
Err Greasefinger
Uerr Sootfists
Duet Riverhead
Illoh Fastfangs
Xabbuet Loosepince
Oggat Blightmask
Surniarr Pebbletongue
Rydir Molefoot
Sry Sleazeboot
Ten Googuise
Tryc Fungihands
On Mirefinger
Syl Pebblefinger
Seigrit Snotpincer
Guddai Dustshrapnel
Szilveith Fizzshrapnel
Tueglah Brinehead
Kogut Bloodknuckle
Kryr Burstsnag
Ir Deadhand
Xol Blightfist
Srur Mirethumb
Gro Miretooth
Kobbath Mudmouth
Kualme Fizzlefang
Tuglyr Dreckscowl
Obberr Mucuseyes
Seirlal Frothgrapnel

**Random Height and Weight Table: Gnoll Random Height and Weight**

Base Height | Height Modifier | Base Weight | Weight Modifier
----------- | --------------- | ----------- | ---------------
5'11" | +2d6 | 210 lb. | * (2d4) lb.

```
def generate_height(npc):
    pass

def generate_weight(npc):
    pass
```
