# Sea Spirit Folk
Sea Spirit Folk call the endless seas their home, navigating the depths with grace and command. They are often wanderers and explorers of the boundless oceans.

**Ability Score Increase.** Your Charisma score increases by 1.

**Sea Resilience.** You have advantage on saving throws against being charmed, and you have resistance to lightning damage.

**Aquatic Adaptation.** You can breathe underwater, and you have a swimming speed equal to your walking speed. Additionally, you can communicate simple ideas with aquatic creatures, such as fish and dolphins, when speaking in Aquan.

```
name = 'Sea'
description = "***Sea Spirit Folk.*** Sea Spirit Folk call the endless seas their home, navigating the depths with grace and command. They are often wanderers and explorers of the boundless oceans."
type = 'humanoid'
def level0(npc):
    npc.CHA += 1

    npc.damageresistances.append('lightning')
    npc.traits.append("***Sea Resilience.*** You have advantage on saving throws against being charmed.")

    npc.traits.append(traits['amphibious'])
    npc.speed['swimming'] = npc.speed['walking']
    npc.languages.append("Aquan")
```
