## Drow High Magic
*Prerequisite: Elf (drow)*

You learn more of the magic typical of dark elves. You learn the [detect magic](http://azgaarnoth.tedneward.com/magic/spells/detect-magic/) spell and can cast it at will, without expending a spell slot. You also learn [levitate](http://azgaarnoth.tedneward.com/magic/spells/levitate/) and [dispel magic](http://azgaarnoth.tedneward.com/magic/spells/dispel-magic/), each of which you can cast once without expending a spell slot. You regain the ability to cast the spell in this way when you finish a long rest. Charisma is your spellcasting ability for these spells.

```
name = 'Drow High Magic'
description = "***Feat: Drow High Magic.*** You learn more of the magic typical of dark elves."
def prereq(npc):
    if npc.race.name == 'Elf' and npc.subrace.name == 'Dark':
        return True
    else:
        return False
def apply(npc):
    npc.spellcasting['Dark Elf'].perday['atwill'] = ['detect magic']
    if 1 in npc.spellcasting['Dark Elf'].perday:
        npc.spellcasting['Dark Elf'].perday[1].append('levitate')
        npc.spellcasting['Dark Elf'].perday[1].append('dispel magic')
    else:
        npc.spellcasting['Dark Elf'].perday[1] = ['levitate', 'dispel magic']
```
