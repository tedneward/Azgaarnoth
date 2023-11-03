# Ice Genasi
As an ice genasi, you have manifested both air and water, connecting you with the enduring dual-element of ice, water that has been robbed of its heat. You are nearly emotionless, except when pushed to anger or grief, which you feel very rarely and only in the worst of situations.

Ice genasi have pale skin made out of a fragile, flexible crystaL usually a cloudy white or bluish-white, but sometimes a vibrant blue-black color instead They are a bit larger than humans on average and cold to the touch, often developing condensation water upon their skin just by existing. Many ice genasi have blue, black, or white hair, usually of a very soft and fine texture, but others have rigid crystals sprouting from their head instead of hair, with no hair anywhere upon their body. 

Ice genasi have blue eyes, but they vary in shades from nearly white to deep indigo.

***Ability Score Increase.*** Your Strength score increases by 1.

***Always Cool.*** You're naturally adapted to hot climates, as described in the Dungeon Master's Guide.

***Icy Resilience.*** You have resistance to cold damage, and your speed can't be reduced by effects that deal cold damage except through conditions that reduce your speed to 0, such as being restrained or grappled.

***Invocation of Ice.*** You can cast [armor of Agathys](../../Magic/Spells/armor-of-agathys.md) with this trait. Starting at 3rd leveL you can cast the new [ice sculpture](../../Magic/Spells/ice-sculpture.md) spell with it, and starting at 5th leveL you can also cast [sleet storm](../../Magic/Spells/sleet-storm.md) with it. Once you cast a spell with this trait, you can't cast that spell with it again until you finish a long rest. Constitution is your spellcasting ability for these spells.

```
name = 'Ice'
description = "***Subrace: Ice Genasi.*** Ice genasi have pale skin made out of a fragile, flexible crystaL usually a cloudy white or bluish-white, but sometimes a vibrant blue-black color instead They are a bit larger than humans on average and cold to the touch, often developing condensation water upon their skin just by existing. Many ice genasi have blue, black, or white hair, usually of a very soft and fine texture, but others have rigid crystals sprouting from their head instead of hair, with no hair anywhere upon their body."

def level0(npc):
    npc.STR += 1

    npc.traits.append("***Always Cool.*** You're naturally adapted to hot climates, as described in the Dungeon Master's Guide.")

    npc.damageresistances.append("cold")
    npc.traits.append("***Icy Resilience.*** Your speed can't be reduced by effects that deal cold damage except through conditions that reduce your speed to 0, such as being restrained or grappled.")

    spellcasting = innatecaster(npc, 'CON', 'Ice Genasi')
    spellcasting.perday[1] = ['armor of agathys']

def level3(npc):
    npc.spellcasting['Ice Genasi'].perday[1].append("ice sculpture")

def level5(npc):
    npc.spellcasting['Ice Genasi'].perday[1].append("sleet storm")
```
