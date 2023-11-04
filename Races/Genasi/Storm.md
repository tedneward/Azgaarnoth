# Storm Genasi
As a storm genasi, you have manifested both air and fire, connecting you with the intense dual-element of lightning, the sky's fire. You are passionate and boisterous, moving swiftly from friendly eagerness to raging anger or bitter sorrow and back to calm optimism or certain determination more quickly than others might think possible. Unlike an air genasi, your emotional storms can last for days on end.

Storm genasi have skin of deep blue or sometimes shades of bluish purple or grey. Their hair, which is usually a dark color but can sometimes be stark white, is always standing up because of the static charge that suffuses their body at all times. Storm genasi have loud, resonating voices that boom like thunder when they are upset or excited.

***Ability Score Increase.*** Your Charisma score increases by 1.

***Tempest Resistance.*** You have resistance to lightning damage and thunder damage.

***Beckon the Storm.*** You know the shocking grasp cantrip. Once you reach 3rd leveL you can cast the spell [Radic's sudden spark](../../Magic/Spells/radics-sudden-spark.md) once, and it recharges after a long rest. Once you reach 5th leveL you can also cast [gust of wind](../../Magic/Spells/gust-of-wind.md) once, and it recharges after a long rest. Constitution is your spellcasting ability for these spells.

```
name = 'Storm'
description = "***Subrace: Storm Genasi.*** Storm genasi have skin of deep blue or sometimes shades of bluish purple or grey. Their hair, which is usually a dark color but can sometimes be stark white, is always standing up because of the static charge that suffuses their body at all times. Storm genasi have loud, resonating voices that boom like thunder when they are upset or excited."

def level0(npc):
    npc.CHA += 1

    npc.damageresistances.append("lightning")
    npc.damageresistances.append("thunder")

    spellcasting = innatecaster(npc, 'CON', 'Storm Genasi')
    spellcasting.cantripsknown.append('shocking grasp')

def level3(npc):
    npc.spellcasting['Ice Genasi'].perday[1] = ["ice sculpture"]

def level5(npc):
    npc.spellcasting['Ice Genasi'].perday[1].append("sleet storm")
```
