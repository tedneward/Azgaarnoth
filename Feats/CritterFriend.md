## Critter Friend
*Prerequisite: Gnome (forest)*

Your friendship with animals mystically deepens. You gain the following benefits:

* You gain proficiency in the Animal Handling skill. If you're already proficient in it, your proficiency bonus is doubled for any check you make with it.
* You learn the [speak with animals](../Magic/Spells/speak-with-animals.md) spell and can cast it at will, without expending a spell slot. You also learn the [animal friendship](../Magic/Spells/animal-friendship.md) spell, and you can cast it once with this feat, without expending a spell slot. You regain the ability to cast it in this way when you finish a long rest. Wisdom is your spellcasting ability for these spells.

```
name = 'Critter Friend'
description = "***Feat: Critter Friend.*** Your friendship with animals mystically deepens."
def prereq(npc): 
    if npc.race.name == 'Gnome' and npc.subrace.name == 'Forest':
        return True
    else:
        return False
def apply(npc):
    npc.addskillorexpertise("Animal Handling")
    
    spellcasting = innatecaster(npc, 'WIS', name)
    spellcasting.atwill = ['speak with animals']
    spellcasting.perday[1] = ['animal friendship']
```

