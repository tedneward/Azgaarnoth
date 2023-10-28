## Outsized Might
You have absorbed primeval magic that allows you, despite your relatively small stature, to embody the might of titanic creatures. This grants you the following benefits:

* **Little but Mighty.** You gain proficiency in either the Athletics or Acrobatics skill.
* **Powerful Build.** You count as one size larger when determining your carrying capacity and the amount you can push, drag, or lift.
* **Stalwart.** You have advantage on saving throws against being moved or knocked prone.

```
name = 'Outsized Might'
description = "***Feat: Outsized Might.*** You have absorbed primeval magic that allows you, despite your relatively small stature, to embody the might of titanic creatures."
def prereq(npc): return npc.size == 'Small'
def apply(npc):
    skill = choose("Choose a skill: ", ['Athletics', 'Acrobatics'])
    npc.proficiencies.append(skill)

    npc.traits.append("***Powerful Build.*** You count as one size larger when determining your carrying capacity and the amount you can push, drag, or lift.")

    npc.traits.append("***Stalwart.*** You have advantage on saving throws against being moved or knocked prone.")
```
