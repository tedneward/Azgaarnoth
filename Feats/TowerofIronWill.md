## Tower of Iron Will
*Prerequisite*: Psionic Talent feature or [Wild Talent feat](#wild-talent)

Your mind's defenses are formidable. After you or another creature you can see within 30 feet of you fails a saving throw, you can use your reaction to roll your Psionic Talent die and add the number rolled to the saving throw, potentially causing it to succeed.

```
name = 'Tower of Iron Will'
description = "***Feat: Tower of Iron Will.*** Your mind's defenses are formidable."
def prereq(npc): return getattr(npc, 'psionicdie', None) != None
def apply(npc):
    npc.reactions.append("***Tower of Iron Will.*** After you or another creature you can see within 30 feet of you fails a saving throw, you can roll your Psionic Talent die and add the number rolled to the saving throw, potentially causing it to succeed.")
```
