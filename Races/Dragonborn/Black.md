# Black Dragonborn
Descendant of black dragons, black dragonborn are often moody and reclusive, regardless of alignment.

### Breath Weapon
You can use your action to exhale destructive acid. It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to acid.

```
name = 'Black'
def level0(npc):
    npc.actions.append("***Breath Weapon (Reharges on a long rest).*** It deals damage in an line 5' x 30'. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increase to 3d6 at 6th level, 4d6 at 11th, and 5d6 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier.")
    npc.resistances.append("acid")
```
