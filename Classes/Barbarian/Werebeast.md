# Primal Path: Path of the Werebeast
The curse of lycanthropy can be a boon to those who embrace the power it provides. Barbarians that are used to the altered mental state of their rage often have less difficulty with controlling the curse and its corrupting influences on their behavior, but no one can easily tame their inner were-beast once it is unleashed.

Some were-beast barbarians are actual lycanthropes, bitten by another lycanthrope or corrupted by dark magic, like a cursed fur belt. Other were-beasts are the heir to a unique generational curse that transforms them, passed down from the hapless ancestor who earned the wrath of a hag, fiend, or god.

```
name = 'Werebeast'
description = "***Primal Path: Path of the Werebeast.*** The curse of lycanthropy can be a boon to those who embrace the power it provides. Barbarians that are used to the altered mental state of their rage often have less difficulty with controlling the curse and its corrupting influences on their behavior, but no one can easily tame their inner were-beast once it is unleashed."
```

## Bestial Bond
*3rd-level Path of the Werebeast feature*

Your lycanthropic connection with the form of a beast grants you the special abilities of that beast. You gain darkvision out to a range of 60 feet, or if you already have darkvision, its range increases by 30 feet, up to a maximum range of 150 feet.

In addition, you choose one of the following options for your bond: ape, bear, boar, cobra, crocodile, kraken, owl, rat, shark, spider, tiger, turtle, or wolf. You gain a trait based on your choice.

Ape, Bear, Boar, Eagle, Owl, Shark, or Wolf: Hunter Senses
Cobra, Crocodile, Kraken, Rat, Spider, Tiger, or Turtle: Lurker Instincts

***Hunter Senses.*** You gain proficiency in your choice of Perception or Survival. Also, you can memorize a creature's scent by sniffing it for 1 minute, and you have advantage on ability checks made to track, perceive, or recognize any creature whose scent you've memorized.

***Lurker Instincts.*** You gain proficiency in your choice of Sleight of Hand or Stealth. Also, you never have to slow your travel pace to move stealthily, and you can always watch for danger while traveling, even when you are performing an activity.

```
def level3(npc):
    if 'darkvision' in npc.senses: npc.senses['darkvision'] += 30
    else: npc.senses['darkvision'] = 60

    npc.werebeast = choose("Choose a Bestial Bond: ", ['Ape', 'Bear', 'Boar', 'Eagle', 'Owl', 'Shark', 'Wolf', 'Cobra', 'Crocodile', 'Kraken', 'Rat', 'Spider', 'Tiger', 'Turtle'])

    if npc.werebeast in ['Ape', 'Bear', 'Boar', 'Eagle', 'Owl', 'Shark', 'Wolf']:
        npc.skills.append(choose("Choose one: ", ['Perception', 'Survival']))
        npc.traits.append("***Hunter Senses.*** You can memorize a creature's scent by sniffing it for 1 minute, and you have advantage on ability checks made to track, perceive, or recognize any creature whose scent you've memorized.")
    else:
        npc.skills.append(choose("Choose one: ", ['Sleight of Hand', 'Stealth']))
        npc.traits.append("***Lurker Instincts.*** You never have to slow your travel pace to move stealthily, and you can always watch for danger while traveling, even when you are performing an activity.")
```

## Were-Beast Form
*3rd-level Path of the Werebeast feature*

You gain the ability to take the form of a powerful humanoid monster with bestial features.

As a bonus action, or as part of the bonus action you use to enter your rage, you can transform into a were-beast form. In this form, your bite is a natural weapon which deals 1d8 + Strength modifier piercing damage, and you count as a beast in addition to your normal type or types. While you are not wearing heavy armor in this form, you also gain a +1 bonus to AC and to the damage rolls of your weapon attacks that use Strength. (Your bite does not transfer the curse of lycanthropy unless you are in fact cursed with that affliction.)

While you're transformed using this feature, you also gain special traits determined by your choice for your Bestial Bond feature. The following list describes the benefits for each choice. If the description mentions a saving throw, the DC for that saving throw is 8 + your Strength modifier + your proficiency bonus.

***Ape.*** You have a climbing speed equal to your walking speed, and your jumping distance is doubled.  You have advantage on Strength checks, and when you enter your rage, you gain temporary hit points equal to your barbarian level + your Strength modifier (minimum of one temporary hit point) that disappear when your rage ends.

```
    if npc.werebeast == 'Ape':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereape form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and to the damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a climbing speed equal to your walking speed, and your jumping distance is doubled.  You have advantage on Strength checks, and when you enter your rage, you gain {npc.STRbonus() + npc.levels('Barbarian')} temporary hit points that disappear when your rage ends.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Bear.*** You have advantage on Strength checks, your carrying capacity is doubled, and your form's bonus to AC is also doubled. When you enter your rage, you gain temporary hit points equal to your barbarian level + your Strength modifier (minimum of one temporary hit point) that disappear when your rage ends.

```
    elif npc.werebeast == 'Bear':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a werebear form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{2 if npc.levels('Barbarian') < 14 else 4} bonus to AC and +1 to the damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have advantage on Strength checks, and your carrying capacity is doubled. When you enter your rage, you gain {npc.STRbonus() + npc.levels('Barbarian')} temporary hit points that disappear when your rage ends.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Boar.*** Once per hour, if you take damage that would reduce you to 0 hit points, you stay at 1 hit point instead. Once per turn while you are raging, if you move at least 15 feet straight toward a creature and hit it with your next melee weapon attack on that turn, the target takes extra damage equal to 1d6 + half your barbarian leveL and it must succeed on a Strength saving throw or be knocked prone. If the target is larger than you, it has advantage on the saving throw.

```
    elif npc.werebeast == 'Boar':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereboar form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} Once per hour, if you take damage that would reduce you to 0 hit points, you stay at 1 hit point instead. Once per turn while you are raging, if you move at least 15 feet straight toward a creature and hit it with your next melee weapon attack on that turn, the target takes 1d6 + {npc.levels('Barbarian') // 2} extra damage, and it must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}) or be knocked prone. If the target is larger than you, it has advantage on the saving throw.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Cobra.*** Your bite attack has a reach of 10 feet and has the finesse property. You also have a swimming speed equal to your walking speed, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. While you are raging, the first creature you hit on each of your turns with a melee weapon attack takes extra poison damage equal to 1d6 + half your barbarian level.

```
    elif npc.werebeast == 'Cobra':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a werecobra form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a swimming speed equal to your walking speed, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. While you are raging, the first creature you hit on each of your turns with a melee weapon attack takes 1d6 + {npc.levels('Barbarian') // 2} extra poison damage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 10ft., one target, finesse. Hit: 1d8 + {npc.STRbonus() + 1} piercing + 1d6 poison damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Crocodile.*** You have a swimming speed equal to your walking speed, you can hold your breath for 10 minutes, and your bite attack improves. Its weapon die increases to 1d10, and on a hit, you can use your bonus action to cause the target to become grappled by your bite. Until this grapple ends, you can't bite another target. While you're raging and you have a creature grappled in this way, it takes piercing damage equal to 1d4 + half your barbarian level at the start of each of your turns.

```
    elif npc.werebeast == 'Crocodile':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a weregator form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a swimming speed equal to your walking speed, and you can hold your breath for 10 minutes.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d10 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
        npc.defer(lambda npc: npc.bonusactions.append(f"***Biting Grapple (Were-Beast Form only). If you hit with your Bite attack, you cause the target to become grappled. Until this grapple ends, you can't Bite another target. While you're raging and you have a creature grappled in this way, it takes 1d4 + {npc.levels('Barbarian') // 2} piercing damage at the start of each of your turns."))

```

***Eagle.*** You have a flying speed equal to your walking speed, you have advantage on any Perception checks, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. Additionally, you can cast [sacred flame](../../Magic/Spells/sacred-flame.md) at will while in this form.

```
    elif npc.werebeast == 'Eagle':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereeagle form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a flying speed equal to your walking speed, you have advantage on any Wisdom (Perception) checks, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. Additionally yu can cast {spelllinkify('sacred flame')} at will while in this form.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Kraken.*** You have a swimming speed equal to your walking speed, you can breathe underwater, and you have blindsight that extends 5 feet, or 30 feet while you are in water. You have advantage on any Dexterity checks or saving throws while in this form, you can use a bonus action on your each of your turns to Hide or Disengage, and the first attack made against you after the end of each of your turns has disadvantage.

```
    elif npc.werebeast == 'Kraken':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a werekraken form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a swimming speed equal to your walking speed, you can breathe underwater, and you have blindsight that extends 5 feet, or 30 feet while you are in water. You have advantage on any Dexterity checks or saving throws while in this form, you can use a bonus action on each of your turns to Hide or Disengage, and the first attack made against you after the end of each of your turns has disadvantage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Owl.*** You have a flying speed equal to your walking speed, you have advantage on any Perception checks, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. Additionally, you can cast [ray of frost](../../Magic/Spells/ray-of-frost.md) at will while in this form.

```
    elif npc.werebeast == 'Owl':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereowl form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a flying speed equal to your walking speed, you have advantage on any Wisdom (Perception) checks, and your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength. Additionally, you can cast {spelllinkify('ray of frost')} at will while in this form.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Rat.*** You have a climbing speed equal to your walking speed, your bite attack has the finesse property, your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength, and you can use a bonus action on your each of your turns to Hide or Disengage. While you're raging, your speed also increases by 10 feet, and the first attack made against you after the end of each of your turns has disadvantage.

```
    elif npc.werebeast == 'Rat':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wererat form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} Once per hour, if you take damage that would reduce you to 0 hit points, you stay at 1 hit point instead. You have a climbing speed equal to your walking speed, your bite attack has the finesse property, your barbarian features grant bonus damage to your attacks that use Dexterity as well as those using Strength, and you can use a bonus action on your each of your turns to Hide or Disengage. While you're raging, your speed also increases by 10 feet, and the first attack made against you after the end of each of your turns has disadvantage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Shark.*** You have a swimming speed equal to your walking speed, you can breathe underwater, and you have blindsight that extends 5 feet, or 30 feet while you are in water. While you're raging, the first time on each of your turns that you hit with a melee weapon attack against a creature that has blood and doesn't have all its hit points, the attack deals bonus damage equal to 1d6 + half your barbarian level.

```
    elif npc.werebeast == 'Shark':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereshark form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a swimming speed equal to your walking speed, you can breathe underwater, and you have blindsight that extends 5 feet, or 30 feet while you are in water. While you're raging, the first time on each of your turns that you hit with a melee weapon attack against a creature that has blood and doesn't have all its hit points, the attack deals 1d6 + {npc.levels('Barbarian') // 2} bonus damage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Spider.*** Your climbing speed is equal to your walking speed, and you can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check. You can use a bonus action on your each of your turns to Hide or Disengage. While you are raging, the first creature you hit on each of your turns with a melee weapon attack takes extra poison damage equal to 1d6 + half your barbarian level.

```
    elif npc.werebeast == 'Spider':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a werespider form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} Your climbing speed is equal to your walking speed, and you can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check. You can use a bonus action on your each of your turns to Hide or Disengage. While you are raging, the first creature you hit on each of your turns with a melee weapon attack takes 1d6 + {npc.levels('Barbarian') // 2} extra poison damage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing and 1d6 poison damage damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

***Tiger.*** Your walking speed increases by 10 feet, your jumping distance is tripled, and once per turn, when you move at least 15 feet straight toward a creature and hit it with your next melee weapon attack on that turn, it must succeed on a Strength saving throw or be knocked prone, with advantage if it is larger than you. If you're raging and it falls prone, you can immediately use your bonus action to make a bite attack against it, dealing extra damage equal to half your barbarian level on a hit.

```
    elif npc.werebeast == 'Tiger':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a were-beast form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} Your walking speed increases by 10 feet, your jumping distance is tripled, and once per turn, when you move at least 15 feet straight toward a creature and hit it with your next melee weapon attack on that turn, it must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}) or be knocked prone, with advantage if it is larger than you. If you're raging and it falls prone, you can immediately use your bonus action to make a bite attack against it, dealing {npc.levels('Barbarian') // 2} extra damage on a hit.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Turtle.*** You have a swimming speed equal to your walking speed, you can hold your breath for 1 hour, and your form's bonus to AC is tripled. In addition, while in this form, you can use [poison spray](../../Magic/Spells/poison-spray.md) at will.

```
    elif npc.werebeast == 'Turtle':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a wereturtle form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{3 if npc.levels('Barbarian') < 14 else 6} bonus to AC and a +1 bonus to damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} You have a swimming speed equal to your walking speed, and you can hold your breath for 1 hour. In addition, while in this form, you can use {spelllinkify('poison spray')}at will.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {npc.STRbonus() + 1} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )

```

***Wolf.*** Your walking speed increases by 10 feet, and your form's bonus to damage rolls is doubled While you are raging, the first time on each of your turns that you hit with a melee weapon attack against a creature that has at least one of your allies within 5 feet of it and the ally isn't incapacitated, the target takes bonus damage equal to 1d4 + half your barbarian level.

```
    elif npc.werebeast == 'Wolf':
        npc.defer(lambda npc: npc.bonusactions.append(f"***Were-Beast Transformation (Recharges on long rest or another usage of Rage).*** You transform into a werewolf form, and you count as a beast in addition to your normal type or types. (You can also do this as part of the bonus action used to Rage.) The transformation lasts {'2 hours' if npc.levels('Barbarian') < 6 else '4 hours' if npc.levels('Barbarian') < 10 else '6 hours' if npc.levels('Barbarian') < 14 else '8 hours' if npc.levels('Barbarian') < 20 else 'indefinitely'} or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. While you are not wearing heavy armor in this form, you gain a +{1 if npc.levels('Barbarian') < 14 else 2} bonus to AC and +2 to damage rolls of your weapon attacks that use Strength.{'' if npc.levels('Barbarian') < 14 else ' You have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons.'} Your walking speed increases by 10 feet, and your form's bonus to damage rolls is doubled. While you are raging, the first time on each of your turns that you hit with a melee weapon attack against a creature that has at least one of your allies within 5 feet of it and the ally isn't incapacitated, the target takes 1d4 + {npc.levels('Barbarian') // 2} bonus damage.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}") )
        npc.defer(lambda npc: npc.actions.append(f"***Bite (Were-Beast Form Only).*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to Hit, reach 5ft., one target. Hit: 1d8 + {(npc.STRbonus() + 1) * 2} piercing damage. Your bite does not transfer the curse of lycanthropy unless you are cursed with that affliction.") )
```

The transformation lasts for 2 hours or until you are reduced to 0 hit points. You can use your action to end the transformation early, but only after at least 1 hour. The duration increases to 4 hours at 6th level, 6 hours at 10th level, 8 hours at 14th level, and unending at 20th level, although the minimum duration of 1 hour remains unchanged.

Once you use this feature, you can't use it again until you finish a long rest, unless you expend one usage of your rage to use this feature again.

## Feral Shape
*6th-level Path of the Werebeast feature*

You gain the ability to complete your bestial transformation. You can use an action on your turn to transform into a full beast based on your choice of were-beast. This transformation follows all the same rules as the druid's Wild Shape class feature, except for what is stated differently in this feature.

You can transform into only one creature and no others, which is based on your choice for your Bestial Bond feature, as shown in the table below:

Bond | Beast Form
---- | ------------
Ape | [Ape](../../Creatures/Simians.md#ape)
Bear | [Brown Bear](../../Creatures/Bears.md#brown-bear)
Boar | [Giant Boar](../../Creatures/Boars.md#giant-boar)
Cobra | [Giant Poisonous Snake](../../Creatures/Snakes.md#giant-poisonous-snake) 
Crocodile | [Crocodile](../../Creatures/Crocodiles.md#crocodile)
Eagle | [Giant Eagle](../../Creatures/Raptors.md#giant-eagle)
Kraken | [Giant Octopus](../../Creatures/Octopi.md#giant-octopus)
Owl | [Giant Owl](../../Creatures/Raptors.md#giant-owl)
Rat | [Giant Badger](../../Creatures/Badgers.md#giant-badger) 
Shark | [Hunter Shark](../../Creatures/Sharks.md#hunter-shark)
Spider | [Giant Spider](../../Creatures/Spiders.md#giant-spider)
Tiger | [Tiger](../../Creatures/Cats.md#tiger) 
Turtle | [Giant Snapping Turtle](../../Creatures/Turtles.md#giant-snapping-turtle)
Wolf | [Wolf](../../Creatures/Wolves.md#wolf)

While transformed, your statistics for your hit points, AC, and ability scores remain unchanged, and you keep any special senses your normal form possesses. Instead of the beast's normal size, you choose to be either Large or Medium when you transform. If you make a Dexterity (Stealth) check, you use the beast's Dexterity score for the check instead of your own. You also benefit from the special traits for your bond's Were-Beast Form, but not the bonus to AC or damage rolls.

The transformation lasts for up to 1 hour, until you are reduced to 0 hit points, or until you choose to end it as an action. When the transformation ends, you resume whatever form you were in when it began.

Once you transform, you can't do so again until you finish a long rest. The number of uses per long rest increases to two at 10th leveL and the uses become unlimited at 20th level

In addition, your natural weapons in your Were-Beast Form and your Feral Shape form count as magical for the purposes of overcoming resistance or immunity.

```
def level6(npc):
    creatures = {
        'Ape': '[Ape](../../Creatures/Simians.md#ape)',
        'Bear': '[Brown Bear](../../Creatures/Bears.md#brown-bear)',
        'Boar': '[Giant Boar](../../Creatures/Boars.md#giant-boar)',
        'Cobra': '[Giant Poisonous Snake](../../Creatures/Snakes.md#giant-poisonous-snake)',
        'Crocodile': '[Crocodile](../../Creatures/Crocodiles.md#crocodile)',
        'Eagle': '[Giant Eagle](../../Creatures/Raptors.md#giant-eagle)',
        'Kraken': '[Giant Octopus](../../Creatures/Octopi.md#giant-octopus)',
        'Owl': '[Giant Owl](../../Creatures/Raptors.md#giant-owl)',
        'Rat': '[Giant Badger](../../Creatures/Badgers.md#giant-badger)', 
        'Shark': '[Hunter Shark](../../Creatures/Sharks.md#hunter-shark)',
        'Spider': '[Giant Spider](../../Creatures/Spiders.md#giant-spider)',
        'Tiger': '[Tiger](../../Creatures/Cats.md#tiger)',
        'Turtle': '[Giant Snapping Turtle](../../Creatures/Turtles.md#giant-snapping-turtle)',
        'Wolf': '[Wolf](../../Creatures/Wolves.md#wolf)'
    }
        
    npc.actions.append(f"***Feral Shape{' (Recharges on long rest)' if npc.levels('Barbarian') < 10 else ' (2/Recharges on long rest)' if npc.levels('Barbarian') < 20 else ''}.*** You transform into a {creatures[npc.werebeast]}. While transformed, your statistics for your hit points, AC, and ability scores remain unchanged, and you keep any special senses your normal form possesses. Your natural weapons in Feral Shape form count as magical for the purposes of overcoming resistance or immunity. You also benefit from the special traits for your bond's Were-Beast Form, but not the bonus to AC or damage rolls. Instead of the beast's normal size, you choose to be either Large or Medium when you transform. If you make a Dexterity (Stealth) check, you use the beast's Dexterity score for the check instead of your own. You also benefit from the special traits for your bond's Were-Beast Form, but not the bonus to AC or damage rolls.{'' if npc.levels('Barbarian') < 10 else ' In addition, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.'}")
```

## Lunar Resolve
*10th-level Path of the Werebeast feature*

While you are in your Were-Beast Form or your Feral Shape transformation, you have advantage on saving throws against being charmed, frightened, or having your emotions changed by magic, and you are immune to any effect that can only target beasts unless you choose to be affected.

In addition, when you use your Were-Beast Form or Feral Shape feature, you can regain hit points equal to twice your barbarian level. Once you do so, you can't do so again until you finish a long rest.

```
def level10(npc):
    npc.traits.append(f"***Lunar Resolve (Recharges on long rest).*** When you use your Were-Beast Form or Feral Shape feature, you can regain {npc.levels('Barbarian') * 2} hit points.")
```

## Second Skin
*14th-level Path of the Werebeast feature*

You start to feel more at home in your werebeast form than your true form. You might feel that this lycanthropic form, rather than the form you were born in, is what you were always meant to be.

While you are in your Were-Beast Form, the AC granted by your Unarmored Defense feature increases by 1, and you have resistance to bludgeoning, piercing, and slashing damage from nonmagical attacks that are not using silvered weapons. While you are raging, any bludgeoning, piercing, or slashing damage that you take from such attacks is reduced by an amount equal to half your proficiency bonus and can't reduce your hit points below half of your hit point maximum.

Also, regardless of your form, you have advantage on saving throws against curses, diseases, and effects that would reveal your true form against your will.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Second Skin.*** While you are raging, any bludgeoning, piercing, or slashing damage that you take from such attacks is reduced by {npc.proficiencybonus() // 2} and can't reduce your hit points below half of your hit point maximum. You have advantage on saving throws against curses, diseases, and effects that would reveal your true form against your will.") )
```
