# Arcane Tradition: Battle Magi
Battlemages are the frontline warriors in magical warfare. Unlike evokers and war mages, battlemages do not provide long range tactical support or magical assault, instead they lead from the front, steel on steel with the foe, wielding their mageblades in tandem with casting magic, devastating their enemies. Whilst in the fray, battlemages rely on their protective enchantments to guard and protect them. In melee, battlemages are a power to be reckoned with; often unexpected and underestimated, though rarely twice.

Lore holds that the battle magi are a splinter tradition of the ancient [Bladesinger](./Bladesinging.md), with a more practical focus, though both battle magi and Bladesingers dispute this. Battle magi are most commonly found among the [Fiery Fist](../../Organizations/MageSchools/FieryFist.md) and [Crimson Sunrise](../../Organizations/MageSchools/CrimsonSunrise.md) schools and are often hired by mercenary companies. However, many "wilder" practitioners are also found in the world, either teaching individual apprentices, or sometimes even founding a [dueling college](../../Organizations/DuelingColleges/index.md) to pass on the skills. Some battle magi instructors teach at the Academy of the [Order of the Bronze Dragon](../../Organizations/MilitantOrders//DraconicOrder/Bronze.md), and [Dradehalian military units](../../Nations/Dradehalia.md) have been seen in the field with what appear to be homegrown battle magi. It is also rumored that the Zhi Military Institute has a wing devoted to battle magi trainees.

```
name = 'Battle Magi'
description = "***Arcane Tradition: Battle Magi.*** Battlemages are the frontline warriors in magical warfare. Unlike evokers and war mages, battlemages do not provide long range tactical support or magical assault, instead they lead from the front, steel on steel with the foe, wielding their mageblades in tandem with casting magic, devastating their enemies. Whilst in the fray, battlemages rely on their protective enchantments to guard and protect them. In melee, battlemages are a power to be reckoned with; often unexpected and underestimated, though rarely twice."
```

## Bonus Proficiencies
*2nd-level Battle Magi feature*

You gain proficiency with martial weapons.

```
def level2(npc):
    for wpn in weapons['martial-melee'] | weapons['martial-ranged']:
        npc.proficiencies.append(wpn)
```

## Imbue Mageblade
*2nd-level Battle Magi feature*

You are able to imbue any melee weapon with a powerful enchantment, creating a magical link between it and you. This ritual requires 1 hour of uninterrupted contact with the weapon, in which you may undertake no other activity. Once imbued, attacks with this weapon use your Intelligence modifier for attack and damage rolls. You can use your bonus action to summon the imbued weapon, regardless of its location, to your hand, provided it is not being worn or carried by another creature. The imbued weapon can be used as an arcane focus, and attacks made with it count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. You can remove the link from one weapon and place it on another by performing the ritual again. Despite its name, this ability works with any melee weapon.

```
    npc.traits.append("***Imbue Mageblade.*** This ritual requires 1 hour of uninterrupted contact with any melee weapon, in which you may undertake no other activity. Once imbued, attacks with this weapon use your Intelligence modifier for attack and damage rolls. The imbued weapon can be used as an arcane focus, and attacks made with it count as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. You can remove the link from one weapon and place it on another by performing the ritual again.")
    npc.bonusactions.append("***Summon Mageblade.*** You summon the imbued weapon, regardless of its location, to your hand, provided it is not being worn or carried by another creature.")
```

## Kinetic Shield
*2nd-level Battle Magi feature*

When you are struck by a weapon attack, you can use your reaction to generate a kinetic shield that reduces the damage from the strike by an amount equal to your proficiency bonus. The shield remains active until the beginning of your next turn, reducing damage from all weapon strikes until it dissipates. You can use this feature a number of times equal to your Intelligence modifier (a minimum of once). You regain expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Kinetic Shield ({npc.INTbonus()}/Recharges on long rest).*** You generate a kinetic shield that reduces the damage from the strike by {npc.proficiencybonus()}. The shield remains active until the beginning of your next turn, reducing damage from all weapon strikes until it dissipates.") )
```

## Spell and Blade
*6th-level Battle Magi feature*

When you use your action to cast a cantrip, as a bonus action, you can make one melee attack with a weapon you are holding.

```
def level6(npc):
    npc.bonusactions.append("***Spell and Blade.*** When you use your action to cast a cantrip, you make one melee attack with a weapon you are holding.")
```

## Kinetic Augmentation
*10th-level Battle Magi feature*

On your next turn after activating Kinetic Shield, you can use your bonus action to take the Dash action. This movement does not provoke opportunity attacks.

```
def level10(npc):
    npc.bonusactions.append("***Kinetic Augmentation.*** On your next turn after activating Kinetic Shield, you take the Dash action. This movement does not provoke opportunity attacks.")
```

## Kinetic Assault
*14th-level Battle Magi feature*

On your next turn after using Kinetic Shield, you can take one additional action on your turn to make an attack or cast a spell. This ability allows you to break the restrictions on casting two spells (that both require an action to cast), on the same turn. This ability cannot be used in conjunction with Action Surge or any other ability that allows the casting of multiple spells on a single turn. You regain the use of this ability after completing a long rest.

```
def level14(npc):
    npc.bonusactions.append("***Kinetic Assault (Recharges on long rest).*** On your next turn after using Kinetic Shield, you can take one additional action on your turn to make an attack or cast a spell. This ability allows you to break the restrictions on casting two spells (that both require an action to cast), on the same turn. This ability cannot be used in conjunction with Action Surge or any other ability that allows the casting of multiple spells on a single turn.")
```

---

# Battle Mage Unique Spells

## 1st-level
* [warding blade](../../Magic/Spells/warding-blade.md)

## 2nd-level
* [aggressive surge](../../Magic/Spells/aggressive-surge.md)

## 3rd-level
* [hungering blade](../../Magic/Spells/hungering-blade.md)

## 4th-level
* [arcane resilience](../../Magic/Spells/arcane-resilience.md)

## 5th-level
* [blessing of the elements](../../Magic/Spells/blessing-of-the-elements.md)

