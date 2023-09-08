# Emeria (Wind) Creed
Merfolk who followed Emeria’s creed seek wisdom and truth in the Wind Realm, exploring the mystical forces--rather than natural causes--behind historical events. They are evasive and intentionally enigmatic in their interactions with others, and are often described as manipulative and deceptive.

* **Ability Score Increase.** Your Wisdom score increases by 2.
* **Wind Creed Manipulation.** You have proficiency in the Deception and Persuasion skills.
* **Cantrip.** You know one cantrip of your choice from the Druid spell list. Wisdom is your spellcasting ability for it.

```
name = 'Emeria'
def level0(npc):
    npc.WIS += 2

    npc.skills.append("Deception")
    npc.skills.append("Persuasion")

    npc.cantripsknown.append("CHOOSE-Druid")
```
