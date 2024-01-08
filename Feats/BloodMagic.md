## Blood Magic
*Prerequisite: Spellcasting or Pact Magic*

You have delved into the forbidden secrets of blood magic, learning to fuel the magic of your spell casting using blood itself.

> Player's Note: Blood magic is a dark secret, and shunned by polite society. Open practitioners of blood magic are openly disliked or hated (at best), jailed, or immediately hunted and killed. Choosing to take this feat is to put yourself under a dark cloud with a murderous secret. Good luck!

You gain the following benefits:

* Choose one class that grants you spell slots, and choose a number of spells on that class's spell list equal to 1 + half your proficiency bonus. When you cast any of these spells as a spell of that class, you may choose to cast them as Blood spells. As your proficiency bonus increases, you can choose more spells. You also choose one of the following cantrips to learn as the chosen class when you gain this feat: [blood boil](../Magic/Spells/blood-boil.md), [hemokinesis](../Magic/Spells/hemokinesis.md), or [gore spike](../Magic/Spells/gore-spike.md). Whenever you reach a level that grants the Ability Score Improvement feature, you can change one of these choices.

* When a creature with blood fails a saving throw against a Blood spell that you cast or takes damage from one, it suffers disadvantage on all ability checks made with one ability score of your choice until the end of your next turn. Alternatively, you can reduce its speed by 10 feet for the same duration instead.

* You can use the Blood Magic feature (below). Your limit for the number of times you can gain blood points is equal to half your proficiency bonus. If you have levels in the sanguinist class, you increase your Blood Magic Uses by half your proficiency bonus instead.

***Blood Magic.*** When a creature with blood fails a saving throw against a *blood*-tagged spell that you cast, or takes damage from one, you can choose to gain 1 blood point by extracting energy from the target's blood. You can also gain 1 blood point whenever a creature with blood is reduced to O hit points within 60 feet of you. You can only have up to half your proficiency bonus (minimum 1) blood points at any time. When you finish a short or long rest, you lose any unexpended blood points.

When you cast a spell of 5th-level or lower, you may expend blood points instead of spell slots, but you must expend at least a number of blood points equal to the level of the spell When you do so, the spell doesn't require a spell slot and counts as a Blood spell in addition to its other schools.

However, the spell can't restore a dead creature to life. Also, unless it is a necromancy spelL it can't cause any creature to regain hit points; instead of restoring hit points, it grants temporary hit points equal to half as many hit points as it would have restored.

```
name = 'Blood Magic'
description = "***Feat: Blood Magic.*** You have delved into the forbidden secrets of blood magic, learning to fuel the magic of your spell casting using blood itself."
def prereq(npc): return len(npc.spellcasting.keys()) > 0
def apply(npc):
    spellcastingclasses = []
    for classname in npc.spellcasting:
        spellcastingclasses.append(classname)
    if len(spellcastingclasses) == 1:
        npc.bloodspellcasting = npc.spellcasting[spellcastingclasses[0]]
    else:
        npc.bloodspellcasting = npc.spellcasting[choose("Choose a spellcasting class: ", spellcastingclasses)]

    cantrip = choose("Choose one:", ['blood boil', 'hemokinesis', 'gore spike'])
    npc.bloodspellcasting.cantripsknown.append(cantrip)

    npc.defer(lambda npc: npc.traits.append(f"***Blood Casting.*** (Choose {1 + npc.proficiencybonus()} spells from your spell list.) When you cast any of these spells, you may choose to cast them as *blood*-tagged spells.") )

    npc.defer(lambda npc: npc.traits.append(f"***Blood Magic (Recharges uses on long rest).*** When a creature with blood fails a saving throw against a *blood*-tagged spell that you cast, or takes damage from one, you can choose to gain 1 blood point by extracting energy from the target's blood. You can also gain 1 blood point whenever a creature with blood is reduced to O hit points within 60 feet of you. You can only have up to {(npc.proficiencybonus() // 2) + 1} blood points at any time. When you finish a short or long rest, you lose any unexpended blood points. When you cast a spell of 5th-level or lower, you may expend blood points instead of spell slots, but you must expend at least a number of blood points equal to the level of the spell When you do so, the spell doesn't require a spell slot and counts as a Blood spell in addition to its other schools. However, the spell can't restore a dead creature to life. Also, unless it is a necromancy spelL it can't cause any creature to regain hit points; instead of restoring hit points, it grants temporary hit points equal to half as many hit points as it would have restored.") )

    npc.traits.append("***Blood Power.*** When a creature with blood fails a saving throw against a Blood spell that you cast or takes damage from one, it suffers disadvantage on all ability checks made with one ability score of your choice until the end of your next turn. Alternatively, you can reduce its speed by 10 feet for the same duration instead.")
```
