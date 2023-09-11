# Gnomes

Gnomes may be [dragonmarked](Dragonmarked.md) with the Mark of Scribing; see that entry for details.

```
name = 'Gnome'
type = 'humanoid'
description = "***Race: Gnome.***"
```

**Ability Score Increase.** Your Intelligence score increases by 2.

**Age.** Gnomes mature at the same rate humans do, and most are expected to settle down into an adult life by around age 40. They can live 350 to almost 500 years.

**Size.** Gnomes are between 3 and 4 feet tall and average about 40 pounds. Your size is Small.

**Speed.** Your base walking speed is 25 feet.

**Darkvision.** Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.

**Gnome Cunning.** You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.

**Languages.** You can speak, read, and write Common and Gnomish. The Gnomish language, which uses the Dwarvish script, is renowned for its technical treatises and its catalogs of knowledge about the natural world.

```
def level0(npc):
    npc.INT += 2

    npc.size = 'Small'

    npc.speed['walking'] = 25

    npc.senses['darkvision'] = 60

    npc.traits.append("***Gnome Cunning.*** You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic.")

    npc.languages.append("Common")
    npc.languages.append("Gnomish")

def generate_name(npc, gender):
  """
Male Names: Alston, Alvyn, Boddynock, Brocc, Burgell, Dimble, Eldon, Erky, Fonkin, Frug, Gerbo, Gimble, Glim, Jebeddo, Kellen, Namfoodle, Orryn, Roondar, Seebo, Sindri, Warryn, Wrenn, Zook

Female Names: Bimpnottin, Breena, Caramip, Carlin, Donella, Duvamil, Ella, Ellyjobell, Ellywick, Lilli, Loopmottin, Lorilla, Mardnab, Nissa, Nyx, Oda, Orla, Roywyn, Shamil, Tana, Waywocket, Zanna

Clan Names: Beren, Daergel, Folkor, Garrick, Nackle, Murnig, Ningel, Raulnor, Scheppen, Timbers, Turen
  """
```

There are a few known gnomish subraces, and gnomes can also be [Dragonmarked](../Dragonmarked/index.md) with the [Mark of Scribing](Scribing.md):

* [Dark](Dark.md)
* [Deep](Deep.md)
* [Forest](Forest.md)
* [Rock](Rock.md)
* [Mark of Scribing](Scribing.md)


