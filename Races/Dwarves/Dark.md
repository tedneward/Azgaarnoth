# Dark Dwarf 
([*duergar*](../../Creatures/Duergar.md))

Histories tell of clans of dwarves that never participated as part of the Exodus (or were left behind either accidentally or deliberately, depending on the rumor), and were forced into hard living and driven deeper into the depths to survive. The *duergar*'s legends claim that those clans were captured by the *illithid* (mind flayers) at the same time elves were captured (who later became the [Gith](../Gith.md)).

Most dwarves consider the "dark dwarves" to be myth, but the *duergar* are real, whatever their history. Rumors of *duergar* generally also tie into the rumors of tunnels that connect the western and eastern reaches of the Daw mountain range underneath the Ravensound, as such tunnels would provide adequate depth to hide them from the Hordes that precipitated the Exodus.

Most of the *duergar* encountered tend to be bitter and resentful, angry at the dwarves for their collective racial pain, with little to no remorse for the dwarves' own tragedies or history. *Duergar* are often paranoid and shun outsiders, though many that have come into contact with surface-dwellers have slowly adjusted their feelings and expectations accordingly. *Duergar* society is clan-based, much like the dwarves' was prior to the Exodus, and the bonds of clan often supersede all other concerns and obligations, even unto death.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Superior Darkvision**. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Duergar Resilience**. You have advantage on saving throws against illusions and against being charmed or paralyzed.

* **Duergar Magic**. When you reach 3rd level, you can cast the [enlarge/reduce](../../Magic/Spells/enlarge-reduce.md) spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the [invisibility](../../Magic/Spells/invisibility.md) spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.

* **Sunlight Sensitivity**. You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.

```
name = 'Duergar'
description = "***Dark Dwarf (duergar).***"
def level0(npc): 
    npc.STR += 1
    npc.senses['darkvision'] = '120 ft'
    npc.proficiencies.append("Light armor")
    npc.proficiencies.append("Medium armor")

    npc.traits.append("***Duergar Resilience.*** You have advantage on saving throws against illusions and against being charmed or paralyzed.")

    npc.traits.append("***Sunlight Sensitivity.*** You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight. Additionally, you cannot cast your Duergar Spellcasting while in direct sunlight.")

def level3(npc):
    spellcasting = innatecaster(npc, 'INT', name)
    spellcasting.perday[1] = []
    spellcasting.perday[1].append("enlarge/reduce")
    npc.spellcasting[name] = spellcasting

def level5(npc):
    npc.spellcasting[name].perday[1].append("invisibility")
```
