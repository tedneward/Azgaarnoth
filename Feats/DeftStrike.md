## Deft Strike
*Prerequisite: proficiency in Perception or Investigation*

Given enough time, you can find weak points in an opponent's armor and exploit them. You can use an action to search for weak points in another creature's armor, natural or not. Make an Investigation check contested by the creature's Armor Class. If you succeed, your next attack ignores all armor bonuses that the creature has, and its effective AC against your attack becomes 10 + the creature's Dexterity modifier.

You can only gain this benefit if you are wielding a weapon that deals piercing or slashing damage. If you are using a ranged weapon, the creature must be within 30 feet of you for you to gain this benefit.

```
name = 'Deft Strike'
description = "***Feat: Deft Strike.*** Given enough time, you can find weak points in an opponent's armor and exploit them."
def prereq(npc):
    if 'Perception' in npc.proficiencies:
        return True
    elif 'Investigation' in npc.proficiencies:
        return True
    else:
        return False
def apply(npc):
    npc.actions.append("***Deft Strike.*** Make an Investigation check contested by the creature's Armor Class. If you succeed, your next attack ignores all armor bonuses that the creature has, and its effective AC against your attack becomes 10 + the creature's Dexterity modifier. You can only gain this benefit if you are wielding a weapon that deals piercing or slashing damage. If you are using a ranged weapon, the creature must be within 30 feet of you for you to gain this benefit.")
```
