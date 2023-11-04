## Svirfneblin Magic
*Prerequisite: Gnome (deep gnome)*

You have inherited the innate spellcasting ability of your ancestors. This ability allows you to cast [nondetection](../Magic/Spells/nondetection.md) on yourself at will, without needing a material component.

You can also cast each of the following spells once with this ability: [blindness/deafness](../Magic/Spells/blindness-deafness.md), [blur](../Magic/Spells/blur.md), and [disguise self](../Magic/Spells/disguise-self.md). You regain the ability to cast these spells when you finish a long rest. Intelligence is your spellcasting ability for these spells.

```
name = 'Svirfneblin Magic'
description = "***Feat: Svirfneblin Magic.*** You have inherited the innate spellcasting ability of your ancestors."
def prereq(npc): return npc.race.name == 'Gnome' and npc.subrace.name == 'Deep'
def apply(npc):
    spellcasting = innatecaster(npc, 'INT', name)
    spellcasting.atwill.append('nondetection')
    spellcasting.perday[1] = ['blindness-deafness', 'blur', 'disguise self']
```
