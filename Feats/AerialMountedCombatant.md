## Aerial Mounted Combatant
You have learned how to ride a flying mount during both air-to-air and air-to-ground combat. This means you are a dangerous foe to face while mounted. While you are mounted and aren't incapacitated, you gain the following benefits:

* You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount. You also have advantage on any ground-bound creature while you are in flight.
* You can force an attack targeted at your mount to target you instead.
* If your mount is subjected to an effect that allows it to make Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.

This feat may be a prerequisite for other aerial combat feats.

```
name = 'Aerial Mounted Combatant'
description = "***Feat: Aerial Mounted Combatant.*** You have learned how to ride a flying mount during both air-to-air and air-to-ground combat. This means you are a dangerous foe to face while mounted."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Aerial Mounted Combatant.*** You have advantage on melee attack rolls against any unmounted creature that is smaller than your mount. You also have advantage on any ground-bound creature while you are in flight. You can force an attack targeted at your mount to target you instead. If your mount is subjected to an effect that allows it to make Dexterity saving throw to take only half damage, it instead takes no damage if it succeeds on the saving throw, and only half damage if it fails.")
```
