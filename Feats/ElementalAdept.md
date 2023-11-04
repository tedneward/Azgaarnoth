## Elemental Adept
*Prerequisite: The ability to cast at least one spell*

When you gain this feat, choose one of the following damage types: acid, cold, fire, lightning, or thunder. Spells you cast ignore resistance to damage of the chosen type. In addition, when you roll damage for a spell you cast that deals damage of that type, you can treat any 1 on a damage die as a 2. You can select this feat multiple times. Each time you do so, you must choose a different damage type.

```
name = 'Elemental Adept'
description = "***Feat: Elemental Adept.*** You have affinity for spells of elemental power."
def prereq(npc): return len(npc.spellcasting) > 0
def apply(npc):
    element = choose("Choose one: ", ['acid', 'cold', 'fire', 'lightning', 'thunder'])
    npc.traits.append(f"***Elemental Adept.*** Spells you cast ignore resistance to {element}. In addition, when you roll damage for a spell you cast that deals {element} damage, you can treat any 1 on a damage die as a 2.")
```
