# River Spirit Folk
River Spirit Folk are tied to the flowing waters, embodying the ebb and flow of life. They are adaptable and serene, finding strength in the ever-changing currents.

**Ability Score Increase.** Your Dexterity score increases by 1.

**River Resilience.** You have advantage on saving throws against being restrained, and you have resistance to cold damage.

**Swift Swimmer.** You have a swim speed equal to your walking speed, and you can breathe underwater.

```
name = 'River'
description = "***River Spirit Folk.*** River Spirit Folk are tied to the flowing waters, embodying the ebb and flow of life. They are adaptable and serene, finding strength in the ever-changing currents."
type = 'humanoid'
def level0(npc):
    npc.DEX += 1

    npc.damageresistances.append('cold')
    npc.traits.append("***River Resilience.*** You have advantage on saving throws against being restrained.")

    npc.speed['swimming'] = npc.speed['walking']
    npc.traits.append(traits['amphibious'])

def generate_name(npc):
    return random(['Akiko', 'Emi', 'Hiroshi', 'Kaede', 'Noriko', 'Ryuji', 'Yumi'])
```
