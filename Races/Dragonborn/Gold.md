# Gold Dragonborn
Gold dragonborn....

### Breath Weapon
You can use your action to exhale destructive fire. It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to fire.

```
name = 'Gold'
description = "***Gold Dragonborn.***"
def level0(npc):
    npc.damageresistances.append("fire")
    npc.defer(lambda npc: npc.actions.append(f"***Breath Weapon ({npc.CONbonus()}/Reharges on a long rest).*** You exhale destructive fire in a line 5' x 30'. All creatures in the area must make a DEX saving throw, DC {8 + npc.CONbonus() + npc.proficiencybonus()}. A creature takes {'2d6' if npc.levels() < 6 else '3d6' if npc.levels() < 11 else '4d6' if npc.levels() < 16 else '5d6'} fire damage on a failed save, or half on a successful one."))
```
