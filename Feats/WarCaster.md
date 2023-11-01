## War Caster
*Prerequisite: The ability to cast at at least one spell*

You have practiced casting spells in the midst of combat, learning techniques that grant you the following benefits:

* You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.
* You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.
* When a hostile creature's movement provokes an opportunity attack from you, you can use your reaction to cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature.

```
name = 'War Caster'
description = "***Feat: War Caster.*** You have practiced casting spells in the midst of combat, learning useful techniques."
def prereq(npc): 
    return len(npc.spellcasting) > 0
def apply(npc):
    npc.traits.append("***War Caster: Concentration.*** You have advantage on Constitution saving throws that you make to maintain your concentration on a spell when you take damage.")
    npc.traits.append("***War Caster: Somaticism.*** You can perform the somatic components of spells even when you have weapons or a shield in one or both hands.")
    npc.reactions.append("***War Caster: Opportunity Cast.*** When a hostile creature's movement provokes an opportunity attack from you, you can cast a spell at the creature, rather than making an opportunity attack. The spell must have a casting time of 1 action and must target only that creature. This does not count against your ability to cast a spell during your turn.")
```
