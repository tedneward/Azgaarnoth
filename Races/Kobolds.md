# [Kobolds](../Creatures/Kobolds.md)

```
name = 'Kobold'
description = "***Race: Kobold.*** "
type = 'humanoid'
def level0(npc):
```

* **Ability Score Increase.** When determining your character’s ability scores, increase one score by 2 and increase a different score by 1, or increase three different scores by 1. You can't raise any of your scores above 20.

```
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    for _ in range(0, 3):
        ability = choose("Choose an ability to improve: ", abilities)
        if ability == 'STR': npc.STR += 1
        elif ability == 'DEX': npc.DEX += 1
        elif ability == 'CON': npc.CON += 1
        elif ability == 'INT': npc.INT += 1
        elif ability == 'WIS': npc.WIS += 1
        elif ability == 'CHA': npc.CHA += 1
```

* **Creature Type.** You are a Humanoid.

* **Size.** You are Small.

```
    npc.size = 'Small'
```

* **Speed.** Your walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision.** You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Draconic Cry.** As a bonus action, you let out a cry at your enemies within 10 feet of you. Until the start of your next turn, you and your allies have advantage on attack rolls against any of those enemies who could hear you. You can use this trait a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Draconic Cry ({npc.proficiencybonus()}/Recharges on long rest).*** You let out a cry at your enemies within 10 feet of you. Until the start of your next turn, you and your allies have advantage on attack rolls against any of those enemies who could hear you."))
```

* **Kobold Legacy.** Kobolds’ connection to dragons can manifest in unpredictable ways in an individual kobold. Choose one of the following legacy options for your kobold:

    * *Craftiness.* You have proficiency in one of the following skills of your choice: Arcana, Investigation, Medicine, Sleight of Hand, or Survival.
    * *Defiance.* You have advantage on saving throws to avoid or end the frightened condition on yourself.
    * *Draconic Sorcery.* You know one cantrip of your choice from the sorcerer spell list. Intelligence, Wisdom, or Charisma is your spellcasting ability for that cantrip (choose when you select this race).
    * *Ferocity.* You can make unarmed strikes with your tail. When you hit with it, the strike deals 1d6 + your Strength modifier bludgeoning damage, instead of the bludgeoning damage normal for an unarmed strike.

```
    npc.koboldlegacy = choose("Choose a legacy: ", ['Craftiness', 'Defiance', 'Sorcery', 'Ferocity'])
    if npc.koboldlegacy == 'Craftiness':
        chooseskill(npc, ['Arcana', 'Investigation', 'Medicine', 'Sleight of Hand', 'Survival'])
    elif npc.koboldlegacy == 'Defiance':
        npc.traits.append("***Kobold Legacy: Defiance.*** You have advantage on saving throws to avoid or end the frightened condition on yourself.")
    elif npc.koboldlegacy == 'Sorcery':
        ability = choose("Choose your socery ability: ", ['INT', 'WIS', 'CHA'])
        spellcasting = innatecaster(npc, ability, name)
        spellcasting.cantripsknown.append("CHOOSE-Sorcerer")
    elif npc.koboldlegacy == 'Ferocity':
        npc.defer(lambda npc: npc.actions.append(f"***Tail.*** Melee Weapon Attack: {npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d6 + {npc.STRbonus()} bludgeoning damage."))
    else:
        print("WTF?!? Kobolds dont have a legacy called '" + npc.koboldlegacy + "'")
```

#### Male names
Qrek Boulderflare
Gand Hillthorn
Vrig Mudbringer
Vink Redeye
Shrizad Covenfeet
Vruzrisz Windarm
Kakes Netherpelt
Children Claweyes
Xalbrarg Foolspine
Strudrig Stormdust
Knink Cragbrow
Grag Bloodcrag
Qug Hazebane
Chosk Hillcut
Etkeing Rivercleaver
Qhogvais Platebane
Snagdeeg Dustash
Dritkeg Brickhammer
Xirkex Morningfeather
Zrugrerc Leadguard
Snag Brewbuckle
Drauc Largeguard
Skerg Bouldergrip
Krais Moltentongue
Khaurus Netherbender
Gegisk Dimripper
Crogger Brewfist
Igmeg Hardsurge
Kutzusz Heavybender
Qhaugmeik Goredust
Guk Embercutter
Qhand Rapidfoot
Breg Nightsplinter
Gik Hardhammer
Grukkurc Rumblewound
Ghromqend Lonebreaker
Trunszaag Dustfeet
Snaimdarg Sharpeye
Garenk Stonewound
Strudix Grayhunter
Qhaag Stoutmaul
Shosz Pebblefall
Qrik Pebblehammer
Xirc Windsurge
Gubbunk Redgaze
Knilgias Craggazer
Cleenzuk Plateflare
Skiarrek Pinechewer
Vruddink Grumbleback
Chrumging Rivereyes

#### Neutral names
Shoz Riverdelver
Shreh Mudbrand
Scel Platebone
Thriz Brickpunch
Kiki Rockcrest
Vrazse Mukborn
Strimkan Brickeye
Vraanzi Nightmaw
Streigrur Forerage
Utzusz Windcoat
Snir Hillhammer
Shisz Fistbelt
Dox Windcrest
Shraan Ironmaster
Chagrasz Brickgrog
Odong Stouthorn
Shrumzre Steelbane
Dabian Bitterchest
Dagnux Grayhide
Shugvi Tuskbelly
Clas Wildbane
Vrez Starblade
Shrein Farbane
Clah Moltenchest
Zreenge Hardstrike
Belgis Lonerunner
Churchus Stonecut
Khuzszan Browngut
Szugmu Grassash
Cluldrai Forebelt
Shrun Platechin
Ghresz Flatcleaver
Kham Broadarm
Clax Gorewatcher
Gede Skullbelly
Egmen Grayclaw
Shrialdam Mudhead
Shengeng Fogseeker
Szurresz Embermark
Kulkian Grassthorn
Knor Redbrow
Szen Cragfist
Snang Flatbrow
Shal Grumbleeye
Vuzzen Coldbluff
Einzosz Hardarm
Keggir Orbstalker
Ugmesz Greybrace
Birkeim Nightcrusher
Igrel Pebblebough

#### Female names
Shnahs Brickchewer
Vrehn Clawdigger
Shoy Wildbone
Zhuhl Bonebrow
Tolvol Leadmaul
Clikgi Grumblejaw
Zrakkay Tuskeye
Shteemsa Rumblefinger
Bheggehn Rockfinger
Ghrumcha Sharpblower
Sheng Mountainmark
Shtin Steelfeet
Bhing Keenbringer
Toh Heavyfeather
Childjih Kragwound
Gumchez Greyripper
Vrelza Keeneye
Ghobi Orbcrusher
Szakshang Keenchew
Bhramga Emberflaw
Ghris Netherbelly
Zhoy Coalbuster
Zeh Sharpbrow
Slin Nightcoat
Shtansha Sharpback
Ghabbi Grumblecrusher
Dhimdje Hardflare
Agra Wildborn
Keibbe Clawstalker
Slirrahn Fareyes
Szeh Rockgrip
Klehl Mudeye
Theeh Shatterwound
Dhel Barbhide
Scekse Leadeyes
Dhuddih Greydelver
Igril Dimscar
Bobno Brickborn
Eeglei Barbedstride
Vrebbe Barbedscar
Thiz Goretongue
Snel Hardjaw
Til Brownstalker
Khnez Dimmail
Bhrubbe Emberwound
Szubbi Barbgrog
Adeng Ashspine
Ghaindo Steelsnarl
Zrandahl Raindrifter
Scairreng Bronzeseeker
