# Ash Genasi
As an ash genasi, you have manifested both earth and fire, connecting you with the deathly dual-element of ash, the dead flames. Your mood gravitates toward dourness, and you tend to take on a more pessimistic perspective than others.

Ash genasi have gray skin tones that range from nearly charcoal black to a pale, almost bone-white color, which is almost constantly flaky and ashy. Their hair is usually a dark red or orange, and baldness is common among them. Some rare ash genasi have smoldering flames which never grow very long or very intense instead of hair. Many ash genasi also smell of smoke and burnt hair at all times.

***Ability Score Increase.*** Your Wisdom score increases by 1.

***Ashen Resistance.*** You have resistance to fire damage and necrotic damage.

***Awaken the Ashes.*** You know the [control flames](../../Magic/Spells/control-flames.md) cantrip, but you can only use it to extinguish flames and create simple shapes. You can also cast the [fog cloud](../../Magic/Spells/fog-cloud.md) spell once with this trait, and you regain the ability to cast it this way when you finish a long rest. Constitution is your spellcasting ability for these spells.

```
name = 'Ash'
description = "***Ash Genasi.*** Ash genasi have gray skin tones that range from nearly charcoal black to a pale, almost bone-white color, which is almost constantly flaky and ashy. Their hair is usually a dark red or orange, and baldness is common among them. Some rare ash genasi have smoldering flames which never grow very long or very intense instead of hair."

def level0(npc):
    npc.damageresistances.append('fire')
    npc.damageresistances.append('necrotic')

    spellcasting = innatecaster(npc, 'CON', 'Ash Genasi')
    spellcasting.cantripsknown.append('control flames')
    spellcasting.cantripsknown.perday[1] = ['fog cloud']
```
