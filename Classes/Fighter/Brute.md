# Martial Archetype: Brute
Brutes are simple warriors who rely on mighty attacks and their own durability to overcome their enemies. Some brutes combine this physical might with tactical cunning. Others just hit things until those things stop hitting back.

```
name = 'Brute'
def level3(npc):
    npc.description.append("***Martial Archetype: Brute.*** Brutes are simple warriors who rely on mighty attacks and their own durability to overcome their enemies. Some brutes combine this physical might with tactical cunning. Others just hit things until those things stop hitting back.")
```

## Brute Force
*3rd-level Brute feature*

You're able to strike with your weapons with especially brutal force. Whenever you hit with a weapon that you're proficient with and deal damage, the weapon's damage increases by an amount based on your level in this class, as shown on the Brute Bonus Damage table.

**Brute Bonus Damage**

Fighter Level | Damage Increase
------------- | ---------------
3rd | 1d4
10th | 1d6
16th | 1d8
20th | 1d10

```
    npc.defer(lambda npc: npc.traits.append(f"***Brute Force.*** Whenever you hit with a weapon that you're proficient with and deal damage, the weapon's damage increases by {'1d4' if npc.levels('Fighter') < 10 else '1d6' if npc.levels('Fighter') < 16 else '1d8' if npc.levels('Fighter') < 20 else '1d10'}."))
```

## Brutish Durability
*7th-level Brute feature*

Your toughness allows you to shrug off assaults that would devastate others. Whenever you make a saving throw, roll 1d6 and add the die to your saving throw total. If applying this bonus to a death saving throw increases the total to 20 or higher, you gain the benefits of rolling a 20 on the d20.

```
def level7(npc):
    npc.traits.append("Whenever you make a saving throw, roll 1d6 and add the die to your saving throw total. If applying this bonus to a death saving throw increases the total to 20 or higher, you gain the benefits of rolling a 20 on the d20.")
```

## Additional Fighting Style
*10th-level Brute feature*

You can choose a second option from the Fighting Style feature.

```
def level10(npc):
    npc.traits.append("***TODO***")
```

## Devastating Critical
*15th-level Brute feature*

When you score a critical hit with a weapon attack, you gain a bonus to that weapon's damage roll equal to your level in this class.

```
def level15(npc):
    npc.traits.append("***TODO***")
```


## Survivor
*18th-level Brute feature*

You attain the pinnacle of resilience in battle. At the start of each of your turns in combat, you regain hit points equal to 5 + your Constitution modifier (minimum of 1 hit point). You don't gain this benefit if you have 0 hit points or if you have more than half of your hit points left.

```
def level18(npc):
    npc.traits.append("***TODO***")
```
