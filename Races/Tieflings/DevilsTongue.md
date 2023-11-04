### Devil's Tongue Bloodline
Aside from their raw physical and arcane power, many types of devils possess the means to warp and affect the attention of others. Tieflings may inherit some of these traits from a manipulative devilish ancestor.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Devil's Tongue**. You know the Vicious Mockery cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Enthrall spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Devil\'s Tongue'
description = "***Tiefling Bloodline: Devil's Tongue.*** Aside from their raw physical and arcane power, many types of devils possess the means to warp and affect the attention of others. Tieflings may inherit some of these traits from a manipulative devilish ancestor."
def level0(npc):
    npc.INT += 1

    spellcasting = innatecaster(npc, 'CHA', "Devil's Tongue Tiefling")
    spellcasting.cantripsknown.append("vicious mockery")

def level3(npc):
    npc.spellcasting["Devil's Tongue Tiefling"].perday[1] = [ 'charm person' ]

def level5(npc):
    npc.spellcasting["Devil's Tongue Tiefling"].perday[1].append('enthrall')
```
