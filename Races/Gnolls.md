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
    npc.defer(lambda npc: npc.actions.append("***Bite.*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d6 + {npc.STRbonus()} piercing damage."))
```

* **Rampage.** When you reduce a creature to 0 hit points with a melee attack on your turn, you may, use a bonus action to move up to half your speed and make a bite attack.

```
    npc.bonusactions.append("***Rampage.*** After you reduce a creature to 0 hit points with a melee attack on its turn, the you can move up to half its speed and make a Bite attack.")
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
def generate_name(npc, gender):
    female_surnames = ['Dagnyra', 'Gnara', 'Gnora', 'Gnyrl', 'Hyra', 'Hyrgna', 'Lhyra', 'Lhyrl', 'Malgna', 'Myrl', 'Sargna', 'Shyrla', 'Tarnyra', 'Yrgna']
    male_surnames = ['Dagnyr', 'Dhyrn', 'Doryc', 'Ghyrryn', 'Gnasc', 'Gnoryc', 'Gnyrn', 'Hyrn', 'Lhoryn', 'Lhyr', 'Mognyr', 'Sorgnyn', 'Thyrn', 'Toryc', 'Yrgnyn', 'Yrych']
    # Family names
    family_names = ['Artar', 'Athak', 'Bagoslalar', 'Bregan', 'Dheubpurwen', 'Dragazakama', 'Entragath', 'Feldadar', 
        'Heral', 'Jernovalrimi', 'Jernokal', 'Malauth', 'Krasgosian', 'Natimorneh', 'Kaziganthi', 'Lagrangli', 
        'Larenthian', 'Mascun', 'Orilg', 'Sahramar', 'Shiagan', 'Orilgrammar', 'Masral', 'Kulris', 'Manaron', 
        'Sumarr', 'Teskos',  'Zhakan', 'Tanhos', 'Ilhagos']

    if gender == 'female': return random(female_surnames) + " " + random(family_names)
    else: return random(male_surnames) + " " + random(family_names)
```

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
