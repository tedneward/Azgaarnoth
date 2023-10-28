## Shield Training
You've trained in the effective use of shields. You gain the following benefits:

* Increase your Strength, Dexterity, or Constitution score by 1, to a maximum of 20.
* You gain proficiency with shields.
* In combat, you can don or doff a shield as the free object interaction on your turn.
* If you have the Spellcasting or Pact Magic feature, you can use a shield as a spellcasting focus.

```
name = 'Shield Training'
description = "***Feat: Shield Training.*** You've trained in the effective use of shields."
def prereq(npc): return True
def apply(npc):
    chooseability(npc, ['STR', 'DEX', 'CON'])
    for arm in armor['shields']:
        npc.proficiencies.append(arm)
    if (len(npc.spellcasting) > 0) or getattr(npc, 'pactmagic', None) != None:
        npc.traits.append("***Arcane Shield.*** You can use a shield as a spellcasting focus.")
```
