# Accursed Velobarn

When you were born into life you were cursed. Perhaps it came from a god or, a powerful caster, or perhaps an ancient ancestor passed it on to their bloodline. Either way, somewhere along the way your curse became a power that now resides within you, allowing you to curse those you wish. You may relish in the curse, or reject with every fiber of your being.

***Cursed blood.*** Broken magic lives in your veins, you gain proficiency in the Arcana skill.

***Great curse.*** You learn [hex](../../Magic/Spells/hex.md) and can cast once per day without a spell slot.You score critical hits against hexed creatures on a 19-20 and, on a critical hit you heal 1d6 health. At 3rd level, you can cast hex a number of times per day equal to your proficiency bonus. Constitution is your spellcasting ability for hex.

```
name = 'Accursed'
description = "***Accursed Velobarn.*** When you were born into life you were cursed. Perhaps it came from a god or, a powerful caster, or perhaps an ancient ancestor passed it on to their bloodline. Either way, somewhere along the way your curse became a power that now resides within you, allowing you to curse those you wish. You may relish in the curse, or reject with every fiber of your being."
def hexperday(npc):
    if npc.level < 3: return 1
    else: return npc.proficiencybonus()

def level0(npc):
    npc.skills.append("Arcana")

    npc.defer(lambda npc: npc.spellcasting['Accursed Velobarn'].perday[hexperday(npc)] = [ 'hex' ])
```
