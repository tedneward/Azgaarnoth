## Medium Armor Master
*Prerequisite: Proficiency with medium armor*

You have practiced moving in medium armor to gain the following benefits:

* Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checks.
* When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher.

```
name = 'Medium Armor Master'
description = "***Feat: Medium Armor Master.*** You have trained to master the use of medium armor."
def prereq(npc):
    for arm in armor['medium']:
        if arm in npc.proficiencies:
            return True
    return False

def apply(npc):
    npc.traits.append("***Medium Armor Master.*** Wearing medium armor doesn't impose disadvantage on your Dexterity (Stealth) checks. When you wear medium armor, you can add 3, rather than 2, to your AC if you have a Dexterity of 16 or higher.")
```

