## Feat: Aberrant [Dragonmark](..//Races/Dragonmarked.md)
*Prerequisite: No existing dragonmark.*

```
name = 'Aberrant Dragonmark'
description = "***Feat: Aberrant Dragonmark.*** Aberrant dragonmarks are marks that are unpredictable and dangerous to both the bearer and the people around them. Someone with such a mark can kill with a touch or control minds with a glance. Aberrant marks always have flaws. These may not actively hurt a character, but they are always a burden in some way--a burden that could drive a weak-willed person to madness."

def prereq(npc):
    if npc.race.name.find("Dragonmarked") > -1: return False
    else: return True
```

The twelve original dragonmarks, passed down from the Eldar through countless generations, have prven to be reliable and predictable, and their powers are constructive. They create; they heal; they protect.

But there is another kind of dragonmark: marks that are unpredictable and dangerous to both the bearer and the people around them. Someone with such a mark can kill with a touch or control minds with a glance. Aberrant marks often appear when people from different dragonmarked families produce a child, and for this reason such unions are absolutely forbidden by the Twelve. But aberrant dragonmarks can appear on members of any race, at any age, regardless of bloodline. No two aberrant dragonmarks are exactly alike; even if they grant the same power, they may appear and manifest in different ways. If two aberrant marks might grant fire bolt, one mark may be formed from scar tissue while another is traced on the skin in lines of cold fire.

You have manifested such an aberrant dragonmark. Determine its appearance and the flaw associated with it.

While aberrant dragonmarks can be disturbing, on the surface an aberrant mark seems no more dangerous or threatening than the powers of a sorcerer. So, what makes them significant? Aberrant marks always have flaws. These may not actively hurt a character, but they are always a burden in some way---a burden that could drive a weak-willed person to madness. If you develop an aberrant mark, you can choose a flaw from this list, or you and the DM can develop a unique flaw of your own.

**Aberrant Mark Flaw**
1d8 | Aberrant Mark Flaw
--- | ------------------
1 | Your mark is a source of constant pain.
2 | Your mark whispers to you, though you may not understand what it says.
3 | In times of stress, your mark may trigger a cantrip effect involuntarily.
4 | The skin around your mark has an unusual appearance: burned, scaly, withered, etc.
5 | Mundane animals become uneasy around you.
6 | You have dramatic mood swings any time you use your mark.
7 | Your appearance changes in some minor way every time you use your mark.
8 | You have horrific nightmares after you use your mark.

You gain the following benefits.

* Increase your Constitution score by 1, to a maximum of 20.
* You learn a cantrip from the sorcerer spell list. In addition, choose a 1st-level spell from the sorcerer spell list. You learn that spell and can cast it at its lowest level. Once you cast it, you must finish a long rest before you can cast it again. Constitution is your spellcasting ability for these spells.
* You can increase the power of your aberrant spells at the risk of your own vitality. When you cast a spell with your aberrant mark, you can use one of your Hit Die to increase the spell's level by 1. Immediately after you cast the spell, roll the Hit Die. You take damage equal to the number rolled.

```
def apply(npc):
    npc.CON += 1

    spellcasting = innatecaster(npc, 'CON', name)
    spellcasting.cantripsknown.append("CHOOSE-Sorcerer")
    spellcasting.perday[1] = [ "CHOOSE-Sorcerer-1st" ]

    npc.traits.append("***Aberrant Mark Metamagic.*** When you cast a spell with your aberrant mark, you can use one of your Hit Die to increase the spell's level by 1. Immediately after you cast the spell, roll the Hit Die. You take damage equal to the number rolled.")

    flaws = [
        "Your mark is a source of constant pain.",
        "Your mark whispers to you, though you may not understand what it says.",
        "In times of stress, your mark may trigger a cantrip effect involuntarily.",
        "The skin around your mark has an unusual appearance: burned, scaly, withered, etc.",
        "Mundane animals become uneasy around you.",
        "You have dramatic mood swings any time you use your mark.",
        "Your appearance changes in some minor way every time you use your mark.",
        "You have horrific nightmares after you use your mark."
    ]
    npc.traits.append(f"***Aberrant Dragonmark Flaw.*** {random(flaws)}")
```