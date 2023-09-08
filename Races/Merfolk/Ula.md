# Ula (Water) Creed
Ula-creed merfolk emphasize intellectual pursuits, stressing hard evidence and reason over passion. They are analytical scholars, chroniclers, explorers, and navigators who pride themselves on being blunt and straightforward.

* **Ability Score Increase.** Your Intelligence score increases by 2.
* **Water Creed Navigation.** You have proficiency with navigator’s tools and in the Survival skill.
* **Cantrip.** You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.

```
name = 'Ula'
def level0(npc):
    npc.INT += 2
    npc.proficiencies.append("Navigator's tools")
    npc.skills.append("Survival")

    npc.cantripsknown.append("CHOOSE-Wizard")
```
