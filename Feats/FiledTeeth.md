## Filed Teeth
*Prerequisites: Gnoll, bite attack*

Your teeth are filed to razor-sharp points.

Your bite deals +1 point of damage.

```
name = 'Filed Teeth'
description = "***Feat: Filed Teeth.*** Your teeth are filed to razor-sharp points."
def prereq(npc): return npc.race.name == 'Gnoll'
def apply(npc):
    npc.actions.append("**TODO** Add +1 to Bite attack damage")
```

