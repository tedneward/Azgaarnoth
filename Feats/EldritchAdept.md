## Eldritch Adept
*Prerequisite: Spellcasting or Pact Magic feature*

Studying occult lore, you have unlocked eldritch power within yourself: you learn one Eldritch Invocation option of your choice from the [warlock](/Classes/Warlock.md) class. If the invocation has a prerequisite, you can choose that invocation only if you're a warlock and only if you meet the prerequisite.

Whenever you gain a level, you can replace the invocation with another one from the warlock class.

```
name = 'Eldritch Adept'
description = "***Feat: Eldritch Adept.*** Studying occult lore, you have unlocked eldritch power within yourself."
def prereq(npc):
    if len(npc.spellcasting) > 0: return True
    elif getattr(npc, "pactmagic", None) != None: return True
    else: return False
def apply(npc):
    npc.traits.append("***Eldritch Adept.*** TODO you learn one Eldritch Invocation option of your choice from the [warlock](http://azgaarnoth.tedneward.com/Classes/Warlock) class.")
```
