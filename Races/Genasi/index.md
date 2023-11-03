# Genasi
Thought to trace their ancestry to the genies of the Elemental Planes, each genasi can tap into the power of one of the elements. [Air](Air.md), [earth](Earth.md), [fire](Fire.md), and [water](Water.md) -- these are the four pillars of the Material Plane and the four types of genasi. Some genasi are direct descendants of a genie, while others were born to non-genasi parents who lived near a place suffused by a genie’s magic.

Many genasi are dual-nature genasi, combining two of the elemental natures; [Ash](Ash.md) (earth/fire), [Ice](Ice.md) (air/water), [Slime](Slime.md) (earth/water), and [Storm](Storm.) (air/fire). The genetic legacy of these genasi is more complicated, owing to their mixed genasi parentage. It is believed that offspring of pairings of "opposite" genasi (air and earth, or fire and water) are impossible.

A typical genasi has a life span of 120 years.

Within Azgaarnoth, genasi are often viewed with a certain amount of suspicion or glee, depending on the locals' relationship to the nearest source of elemental power (and how it's treated the locals recently). Fire genasi born after the eruption of Mt Belzulb (and there were many!) were often cast out of their villages, but are often prized as family members among artisans and Merchant Guilds. Earth genasi born to Ulmhorde tribes are often cast out, but welcomed within Yithi and Zhi. Air genasi are loved among the Al'Uma, but viewed with suspicion elsewhere. And so on.

> GM Notes: Between the fact that genasi are rare (less than 5% of the population) and because the general populace is not clear on whether the Eldar had a hand in the creation of the genasi, most Azgaarians--regardless of national culture or lineage--have not fully formed their opinions of these kin of the genie. As a result, genasi often grow up wary, never knowing what their reception will be like; similarly, genasi are one of the few races on Azgaarnoth that will elicit stares from city-dwelllers and townsfolk alike.

**Ability Score Increase.** When determining your character’s ability scores, increase one score by 2 and increase a different score by 1, or increase three different scores by 1. You can't raise any of your scores above 20.

**Creature Type.** You are a Humanoid.

**Size.** You are Medium or Small. You choose the size when you select this race.

**Speed.** Your walking speed is 30 feet.

**Darkvision.** You can see in dim light within 60 feet of you as if it were bright light and in darkness as if it were dim light. You discern colors in that darkness only as shades of gray.

```
name = 'Genasi'
description = "***Race: Genasi.*** Thought to trace their ancestry to the genies of the Elemental Planes, each genasi can tap into the power of one of the elements."
type = 'humanoid'
def level0(npc):
    npc.size = choose("Choose your size: ", ['Small', 'Medium'])
    npc.speed['walking'] = 30

    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    for _ in range(0, 3):
        ability = choose("Choose an ability to improve: ", abilities)
        if ability == 'STR': npc.STR += 1
        elif ability == 'DEX': npc.DEX += 1
        elif ability == 'CON': npc.CON += 1
        elif ability == 'INT': npc.INT += 1
        elif ability == 'WIS': npc.WIS += 1
        elif ability == 'CHA': npc.CHA += 1

    npc.senses['darkvision'] = 60
```
