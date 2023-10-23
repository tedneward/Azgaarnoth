## Dragon Fear
*Prerequisite: Dragonborn, Half-Dragon*

When angered, you radiate menace. You gain the following benefits:

* Increase your Strength, Constitution, or Charisma score by 1, to a maximum of 20.
* Instead of exhaling destructive energy, you can expend a use of your Breath Weapon trait to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw (DC 8 + your proficiency bonus + your Charisma modifier). A target automatically succeeds on the save if it can't hear or see you. On a failed save, a target becomes frightened for 1 minute. If the frightened target takes any damage, it can repeat the saving throw, ending the effect on itself on a success.

```
name = 'Dragon Fear'
description = "***Feat: Dragon Fear.*** When angered, you radiate menace."
def prereq(npc):
    if npc.race.name == 'Dragonborn':
        return True
    elif npc.race.name == 'Half-Dragon':
        return True
    else:
        return False
def apply(npc):
    chooseability(npc, ['STR', 'CON', 'CHA'])

    npc.defer(lambda npc: npc.actions.append("***Roar.*** You can expend a use of your Breath Weapon trait to roar, forcing each creature of your choice within 30 feet of you to make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}). A target automatically succeeds on the save if it can't hear or see you. On a failed save, a target becomes frightened for 1 minute. If the frightened target takes any damage, it can repeat the saving throw, ending the effect on itself on a success.") )
```
