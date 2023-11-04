# Brass Dragonborn
Brass dragonborn....

### Breath Weapon
You can use your action to exhale destructive fire. It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to fire.

### Metallic Breath Weapon. 
*5th-level Brass Dragonborn feature*

You gain a second breath weapon. When you take the Attack action on your turn, you can replace one of your attacks with an exhalation in a 15-foot cone. The save DC for this breath is 8 + your Constitution modifier + your proficiency bonus. Whenever you use this trait, choose one:

* Enervating Breath. Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn.
* Repulsion Breath. Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone.
  
Once you use your Metallic Breath Weapon, you can’t do so again until you finish a long rest.

```
name = 'Brass'
description = "***Brass Dragonborn.***"
def level0(npc):
    npc.damageresistances.append("fire")
    npc.defer(lambda npc: npc.actions.append(f"***Breath Weapon ({npc.proficiencybonus()}/Reharges on a long rest).*** You exhale destructive fire in a line 5' x 30'. All creatures in the area must make a DEX saving throw, DC {8 + npc.CONbonus() + npc.proficiencybonus()}. A creature takes {'1d10' if npc.levels() < 6 else '2d10' if npc.levels() < 11 else '3d10' if npc.levels() < 16 else '4d10'} fire damage on a failed save, or half on a successful one."))
def level5(npc):
    npc.defer(lambda npc: npc.actions.append("***Metallic Breath Weapon (Recharges on long rest).*** You exhale a 15-foot cone of either Enervating Breath (Each creature in the cone must succeed on a Constitution saving throw or become incapacitated until the start of your next turn) or Repulsion Breath (Each creature in the cone must succeed on a Strength saving throw or be pushed 20 feet away from you and be knocked prone); save DC is {8 + npc.CONbonus() + npc.proficiencybonus()}.") )
```
