## Dragon Hide
*Prerequisite: Dragonborn, Half-Dragon*

You manifest scales and claws reminiscent of your draconic ancestors. You gain the following benefits:

* Increase your Strength, Constitution, or Charisma score by 1, up to a maximum of 20.
* Your scales harden. While you aren't wearing armor, you can calculate your AC as 13 + your Dexterity modifier. You can use a shield and still gain this benefit.
* You can grow retractable claws from the tips of your fingers. Extending or retracting the claws requires no action. The claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the normal bludgeoning damage for an unarmed strike.

```
name = 'Dragon Hide'
description = "***Feat: Dragon Hide.*** You manifest scales and claws reminiscient of your draconic ancestors."
def prereq(npc):
    if npc.race.name == 'Dragonborn':
        return True
    elif npc.race.name == 'Half-Dragon':
        return True
    else:
        return False
def apply(npc):
    chooseability(npc, ['STR', 'CON', 'CHA'])

    npc.traits.append("***Scales.*** Your scales harden. While you aren't wearing armor, you have a natural armor class of 13. You can use a shield and still gain this benefit.")
    npc.armorclass['Natural armor'] = 13

    npc.traits.append("***Retractable Claws.*** You can grow retractable claws from the tips of your fingers. Extending or retracting the claws requires no action.")
    npc.defer(lambda npc: npc.actions.append("***Claws.*** *Melee Weapon Attack:* +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d4 + {npc.STRbonus()} slashing damage.") )
```

