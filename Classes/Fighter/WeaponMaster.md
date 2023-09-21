# Martial Archetype: Weapon Master
The Weapon Master devotes their training to a single weapon to the exclusion of all others. This signature weapon becomes an extension of their mind, body, and spirit, a true part of their soul.

Once the Weapon Master enters combat, their absolute dedication to their signature weapon becomes apparent to enemies and allies alike. Weapon Master and weapon cease to be distinct, separate entities. They bond, becoming a single--and unstoppable--instrument of death.

```
name = 'Weapon Master'
description = "***Martial Archetype: Weapon Master.*** The Weapon Master devotes their training to a single weapon to the exclusion of all others. This signature weapon becomes an extension of their mind, body, and spirit, a true part of their soul. Once the Weapon Master enters combat, their absolute dedication to their signature weapon becomes apparent to enemies and allies alike. Weapon Master and weapon cease to be distinct, separate entities. They bond, becoming a single--and unstoppable--instrument of death."
```


## Signature Weapon
*3rd-level Weapon Master feature*

You forego the use of all other weapons, choosing one weapon as your signature martial focus. Add half your proficiency bonus to all attack rolls with your signature weapon.

Should you wield another weapon of any type, you do so with disadvantage.

In addition, any time an attack or effect would cause you to drop your weapon, you may choose to keep hold of it so long as you remain conscious.

```
def level3(npc):
    npc.masteryweapon = choose("Choose the weapon: ", list(weapons.keys()))
    npc.traits.append(f"***Signature Weapon: {npc.masteryweapon}.*** Add half your proficiency bonus to all attack rolls with this weapon. Should you wield another weapon of any type, you do so with disadvantage. In addition, any time an attack or effect would cause you to drop your weapon, you may choose to keep hold of it so long as you remain conscious.")
```

## Practiced Defense
*7th-level Weapon Master feature*

While wielding your signature weapon, you gain a +1 bonus to AC. 

```
def level7(npc):
    npc.armorclass['Practiced Defense'] = 1
```

## Perfect Strike
*10th-level Weapon Master feature*

You gain your signature weapon bonus to damage as well as attack rolls. You deal critical hits on a roll of 19 and 20.

```
def level10(npc):
    npc.traits.append("***Perfect Strike.*** You gain your signature weapon bonus to damage as well as attack rolls. You deal critical hits on a roll of 19 and 20.")
```

## Awakened Soul
*15th-level Weapon Master feature*

You have forged a deep spiritual bond with your weapon, investing a portion of your own spiritual energy into the weapon. The chosen weapon awakens, becoming a magical +2 weapon.

```
def level15(npc):
    npc.traits.append("***Awakened Soul.*** You have forged a deep spiritual bond with your weapon, investing a portion of your own spiritual energy into the weapon. The chosen weapon awakens, becoming a magical +2 weapon.")
```

## Weapon Mastery
*18th-level Weapon Master feature*

Your signature weapon deals critical hits on 18, 19 and 20 and an additional +2d6 damage on critical hits. 

```
def level18(npc):
    npc.traits.append("***Weapon Mastery.*** Your signature weapon deals critical hits on 18, 19 and 20 and an additional +2d6 damage on critical hits.")
```
