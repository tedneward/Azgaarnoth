# Cosi (Trickster) Creed
No merfolk will openly admit to following the creed of the trickster, but those who do view Cosi as an ally who can grant them control over the chaotic forces of the world.

* **Ability Score Increase.** Your Charisma score increases by an additional 1 (for a total of 2), and your Intelligence score increases by 1.
* **Creed of the Trickster.** You have proficiency in the Sleight of Hand and Stealth skills.
* **Cantrip.** You know one cantrip of your choice from the Bard spell list. Charisma is your spellcasting ability for it.

```
name = 'Cosi'
description = "***Cosi Merfolk.*** No merfolk will openly admit to following the creed of the trickster, but those who do view Cosi as an ally who can grant them control over the chaotic forces of the world."
def level0(npc):
    npc.CHA += 1
    npc.INT += 1

    npc.skills.append("Sleight of Hand")
    npc.skills.append("Stealth")

    spellcasting = innatecaster(npc, 'CHA', "Cosi Merfolk")
    spellcasting.cantripsknown.append("CHOOSE-Bard")
```