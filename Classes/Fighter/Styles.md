# Fighting Styles

## Archery
You gain a +2 bonus to attack rolls you make with ranged weapons.

```
def archery(npc):
    npc.traits.append("***Fighting Style: Archery.*** You gain a +2 bonus to attack rolls you make with ranged weapons.")
```

## Blind Fighting
You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.

```
def blindfighting(npc):
    npc.senses['blindsight'] = 10
```

## Close Quarters Shooter
When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.

```
def closequarters(npc):
    npc.traits.append("***Fighting Style: Close Quarters Shooter.*** When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.")
```

## Defense
While you are wearing armor, you gain a +1 bonus to AC.

```
def defense(npc):
    npc.traits.append("***Fighting Style: Defense.*** While you are wearing armor, you gain a +1 bonus to AC.")
    npc.armorclass['Fighting Style'] = 1
```

## Dueling
When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.

```
def dueling(npc):
    npc.traits.append("***Fighting Style: Dueling.*** When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")
```

## Great Weapon Fighting
When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.

```
def greatweaponfighting(npc):
    npc.traits.append("***Fighting Style: Great Weapon Fighting.*** When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.")
```

## Interception
When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by ldlO + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.

```
def interception(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Fighting Style: Interception.*** When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can reduce the damage the target takes by 1d10 + {npc.proficiencybonus()}. You must be wielding a shield or a simple or martial weapon to use this reaction."))
```

## Mariner
As long as you not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class.

```
def mariner(npc):
    npc.speed['swimming'] = npc.speed['walking']
    npc.speed['climbing'] = npc.speed['walking']
    npc.armorclass['Mariner'] = 1
```

## Protection
When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.

```
def protection(npc):
    npc.reactions.append("***Fighting Style: Protection.*** When a creature you can see attacks a target other than you that is within 5 feet of you, and you are wielding a shield, you can impose disadvantage on the attack roll.")
```

## Superior Technique
You learn one maneuver of your choice from among those available to the [Battle Master](BattleMaster.md) archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).

You gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it.  You regain your expended superiority dice when you finish a short or long rest.

```
def superiortechnique(npc):
    allclasses['Fighter'].choosemaneuver(npc)
```

## Thrown Weapon Fighting
You can draw a weapon that has the thrown property as part of the attack you make with the weapon.

In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.

```
def thrownweapon(npc):
    npc.actions.append("***Fighting Style: Thrown Weapon Fighting.*** You can draw a weapon that has the 'thrown' property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll." )
```

## Tunnel Fighter
As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.

```
def tunnelfighter(npc):
    npc.bonusactions.append("***Fighting Style: Tunnel Fighter.*** You can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.")
```

## Two-Weapon Fighting
When you take the Attack or Multiattack action and attack with a light melee weapon that you're holding in one hand, you can use a bonus action to attack with a different light melee weapon that you're holding in the other hand. You can add your ability modifier to the damage of this other attack. If either weapon has the thrown property, you can throw the weapon, instead of making a melee attack with it.

```
def twoweapon(npc):
    npc.bonusactions.append("***Fighting Style: Two-Weapon Fighting.*** When you take the Attack or Multiattack action and attack with a light melee weapon that you're holding in one hand, you can attack with a different light melee weapon that you're holding in the other hand. You can add your ability modifier to the damage of this other attack. If either weapon has the thrown property, you can throw the weapon, instead of making a melee attack with it.")
```

## Unarmed Fighting
Your unarmed strikes can deal bludgeoning damage equal to ld6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.

At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you.

```
def unarmedfighting(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Fighting Style: Unarmed Fighting.*** Your unarmed strikes can deal 1d6 + {npc.STRbonus()} bludgeoning damage on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8. At the start of each of your turns, you can deal 1d4 bludgeoning damage to one creature grappled by you."))
```

```
styles = {
    'Archery': archery,
    'Blind': blindfighting,
    'Close Quarters Shooter': closequarters,
    'Defense': defense,
    'Dueling': dueling,
    'Great Weapon': greatweaponfighting, 
    'Interception': interception,
    'Mariner': mariner,
    'Protection': protection,
    'Superior Technique': superiortechnique,
    'Thrown Weapon': thrownweapon,
    'Tunnel Fighter': tunnelfighter,
    'Two-Weapon': twoweapon,
    'Unarmed': unarmedfighting
}
def choosestyle(npc):
    (stylename, stylefn) = choose("Choose a Fighting Style: ", styles)
    if getattr(npc, "fightingstyles", None) == None:
        npc.fightingstyles = []
    npc.fightingstyles.append(stylename)
    stylefn(npc)

allclasses['Fighter'].choosestyle = choosestyle
```
