# Mountain Spirit Folk
Mountain Spirit Folk are born in the towering heights, where they are shaped by the rugged terrain and elemental forces. They are known for their unwavering determination and endurance.

**Ability Score Increase.** Your Strength score increases by 1.

**Mountain Resilience.** You have advantage on saving throws against fear, and you have resistance to thunder damage.

**Mountain Climber.** You have a climbing speed equal to your walking speed, and you can make a running long jump or a running high jump after moving only 5 feet on foot.

```
name = 'Mountain'
description = "***Mountain Spirit Folk.*** Mountain Spirit Folk are born in the towering heights, where they are shaped by the rugged terrain and elemental forces. They are known for their unwavering determination and endurance."
type = 'humanoid'
def level0(npc):
    npc.STR += 1
    
    npc.damageresistances.append('thunder')
    npc.traits.append("***Mountain Resilience.*** You have advantage on saving throws against fear.")
    
    npc.speed['climbing'] = npc.speed['walking']
    npc.traits.append("***Mountain Climber.*** You can make a running long jump or a running high jump after moving only 5 feet on foot.")
```
