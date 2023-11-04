## Terrifying Howl
*Prerequisites: Gnoll*

Your howl is that of the stalking predator, and can terrify your quarry.

You howl, and creatures not allied with you within a 60' radius must make a Wisdom save (DC 8 + your proficiency bonus + your Charisma modifier) or be frightened of you until the end of your next turn.

```
name = 'Terrifying Howl'
description = "***Feat: Terrifying Howl.*** Your howl is that of the stalking predator, and can terrify your quarry."
def prereq(npc): return npc.race.name == 'Gnoll'
def apply(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Terrifying Howl.*** You howl, and creatures not allied with you within a 60' radius must make a Wisdom save (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) or be frightened of you until the end of your next turn.") )
```
