# Green Dragonborn
Green dragonborn....

### Breath Weapon
You can use your action to exhale destructive poison. It deals damage in a 15' cone. When you use your breath weapon, all creatures in the area must make a CON saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 poison damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to poison.

### Chromatic Warding
*5th-level Green Dragonborn feature*

As an action, you can channel your draconic energy to protect yourself. For 1 minute, you become immune to poison damage. Once you use this trait, you can’t do so again until you finish a long rest.

```
name = 'Green'
description = "***Green Dragonborn.***"
def level0(npc):
    npc.damageresistances.append("poison")
    npc.defer(lambda npc: npc.actions.append(f"***Breath Weapon ({npc.proficiencybonus()}/Reharges on a long rest).*** You exhale destructive poison in a 15' cone. All creatures in the area must make a CON saving throw, DC {8 + npc.CONbonus() + npc.proficiencybonus()}. A creature takes {'1d10' if npc.levels() < 6 else '2d10' if npc.levels() < 11 else '3d10' if npc.levels() < 16 else '4d10'} poison damage on a failed save, or half on a successful one."))
def level5(npc):
    npc.actions.append("***Chromatic Warding (Recharges on long rest).*** For 1 minute, you become immune to poison damage.")
```
