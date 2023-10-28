## Metamagic Adept
*Prerequisite: Spellcasting or Pact Magic feature*

You've learned how to exert your will on your spells to alter how they function. You gain the following benefits:

* You learn two Metamagic options of your choice from the [sorcerer](Sorcerer.md) class. You can use only one Metamagic option on a spell when you cast it, unless the option says otherwise. Whenever you gain a level, you can replace one of your Metamagic options with another one from the sorcerer class.
* You gain 2 sorcery points to spend on Metamagic (these points are added to any sorcery points you have from another source but can be used only on Metamagic). You regain all spent sorcery points when you finish a long rest.

```
name = 'Metamagic Adept'
description = "***Feat: Metamagic Adept.*** You've learned how to exert your will on your spells to alter how they function."
def prereq(npc): return len(npc.spellcasting) > 0
def apply(npc):
    #TODO: Add the Metamagic options once I flesh out Sorcerer
    
    npc.traits.append("***Metamagic Adept (Recharges on long rest).*** You learn two Metamagic options of your choice from the sorcerer class. You can use only one Metamagic option on a spell when you cast it, unless the option says otherwise. Whenever you gain a level, you can replace one of your Metamagic options with another one from the sorcerer class. You gain 2 sorcery points to spend on Metamagic (these points are added to any sorcery points you have from another source but can be used only on Metamagic). You regain all spent sorcery points when you finish a long rest.")
```
