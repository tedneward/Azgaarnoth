## Prodigy
*Prerequisite: Half-elf, half-orc or human*

You have a knack for learning new things. You gain the following benefits:

You gain one skill proficiency of your choice, one tool proficiency of your choice, and fluency in one language of your choice.

Choose one skill in which you have proficiency. You gain expertise with that skill, which means your proficiency bonus is doubled for any ability check you make with it. The skill you choose must be one that isn't already benefiting from a feature, such as Expertise, that doubles your proficiency bonus.

```
name = 'Prodigy'
description = "***Feat: Prodigy.*** You have a knack for learning new things."
def prereq(npc):
    if npc.race.name == 'Half-Elf' or npc.race.name == 'Half-Orc' or npc.race.name == 'Human':
        return True
    else:
        return False
def apply(npc):
    chooseskill(npc)
    choose("Choose a tool proficiency: ", ["Artisan's Tools", "Disguise Kit", "Forgery Kit", "Gaming Set", "Herbalism Kit", "Musical Instrument", "Navigator's Tools", "Poisoner's Kit", "Thieves' Tools"])
    npc.languages.append("CHOOSE")

    npc.addskillorexpertise(choose("Choose a skill:", npc.skills))
```
