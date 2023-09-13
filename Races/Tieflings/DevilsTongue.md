### Devil's Tongue Bloodline
Aside from their raw physical and arcane power, many types of devils possess the means to warp and affect the attention of others. Tieflings may inherit some of these traits from a manipulative devilish ancestor.

* **Ability Score Increase** Your Intelligence score increases by 1.

* **Devil's Tongue**. You know the Vicious Mockery cantrip. Once you reach 3rd level, you can cast the Charm Person spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Enthrall spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Devil\'s Tongue'
description = "***Tiefling Bloodline: Devil's Tongue.*** Aside from their raw physical and arcane power, many types of devils possess the means to warp and affect the attention of others. Tieflings may inherit some of these traits from a manipulative devilish ancestor."
def level0(npc):
    npc.INT += 1

    npc.cantripsknown.append("vicious mockery")

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Devil's Tongue (Recharges on long rest).*** You can cast " + spelllinkify('charm person') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Devil's Tongue", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('charm person')} as a 2nd-level spell or {spelllinkify('enthrall')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
