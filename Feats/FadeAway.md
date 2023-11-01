## Fade Away
*Prerequisite: Gnome*

Your people are clever, with a knack for illusion magic. You have learned a magical trick for fading away when you suffer harm. You gain the following benefits:

* Increase your Dexterity or Intelligence score by 1, to a maximum of 20.
* Immediately after you take damage, you can use a reaction to magically become invisible until the end of your next turn or until you attack, deal damage, or force someone to make a saving throw. Once you use this ability, you can't do so again until you finish a short or long rest.

```
name = 'Fade Away'
description = "***Feat: Fade Away.*** Your people are clever, with a knack for illusion magic."
def prereq(npc): return npc.race.name == 'Gnome'
def apply(npc):
    ability = choose("Choose: ", ['DEX', 'INT'])
    if ability == 'DEX': npc.DEX += 1
    elif ability == 'INT': npc.INT += 1
    else: error("WTF?!?")

    npc.reactions.append("***Fade Away (Recharges on short or long rest).*** You magically become invisible until the end of your next turn or until you attack, deal damage, or force someone to make a saving throw.")
```
