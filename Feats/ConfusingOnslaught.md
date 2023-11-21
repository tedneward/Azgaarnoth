## Confusing Onslaught
*Prerequisites: Chaotic alignment, Gnoll*

The gnolls charge, howling wildly and their chaotic attack confuses their opponents.

The first time you charge in combat, creatures you target during that charge become flat-footed.

```
name = 'Confusing Onslaught'
description = "***Feat: Confusing Onslaught.*** Your chaotic attack confuses your opponents."
def prereq(npc): return npc.race.name == 'Gnoll'
def apply(npc):
    npc.traits.append("***Confusing Onslaught.*** The first time you charge in combat, any creatures you target during that charge you attack at advantage.")
```

