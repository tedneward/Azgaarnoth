# Dragonkin
Thought to be a distant branch off of the same genetic line that created [dragonborn](Dragonborn.md), dragonkin are the larger, more muscular but more violent cousins to dragonborn. Most dragonkin originated out of the lands of the Hordes, though now dragonkin can be found all over Azgaarnoth, albeit rarely.

Dragonkin seem to hate dragonborn, and many will attack a dragonborn on sight. Even dragonborn are not sure why, though many theories have been put forth regarding potential shared ancestry (which most dragonborn reject wholeheartedly).

```
name = 'Dragonkin'
description = "***Race: Dragonkin.*** Thought to be a distant branch off of the same genetic line that created dragonborn, dragonkin are the larger, more muscular but more violent cousins to dragonborn. Most dragonkin originated out of the lands of the Hordes, though now dragonkin can be found all over Azgaarnoth, albeit rarely."
type = 'humanoid'
```

* **Ability Score increase**. Your Strength score increases by 2, and your Charisma score increases by 1.

```
def level0(npc):
    npc.STR += 2
    npc.CHA += 1
```

* **Age**. Dragonkin grow quickly as children, walking and running within days of their birth. They mature fully by the time they reach about 14 years old. They can live to be as old as 80 or 90, but that is assuming they haven't died in battle by then.

* **Alignment**. Dragonkin society is a violent one where the strongest rule and the weakest die. As a result, dragonkin are often evil with a chaotic bent, but anomalies exist.

* **Size**. Dragonkin are usually around 8 feet tall and weigh between 300 and 350 pounds. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed**. Your base walking speed is 25 feet.

```
    npc.speed['walking'] = 25
```

* **Claws**. Your claws are natural weapons, which you can use to make unarmed strikes. If you hit with them, you deal slashing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

```
    npc.defer(lambda npc: npc.actions.append(f"***Claws.*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d4 + {npc.STRbonus()} piercing damage."))
```

* **Darkvision**. You have a dragon's keen senses, especially in the dark. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray. 

```
    npc.senses['darkvision'] = 60
```

* **Flight**. You have a flying speed of 40 feet. To use this speed, you can't be wearing medium or heavy armor.

```
    npc.speed['flying'] = 40
    npc.traits.append("***Flight.*** You can't be wearing medium or heavy armor while flying.")
```

* **Natural Armor**. You have tough, scaly skin. When you aren't wearing armor, your AC is 13 + your Dexterity modifier. You can use your natural armor to determine your AC if the armor you wear would leave you with a lower AC. A shield's benefits apply as normal while you use your natural armor.

```
    npc.armorclass['natural armor'] = 13
```

* **Powerful Build**. You count as one size larger when determining your carrying capacity and the weight you can push, drag, or lift.

```
    npc.traits.append(traits['powerful-build'])
```

* **Languages**. You can read, speak, and write Common and Draconic.

```
    npc.languages.append("Common")
    npc.languages.append("Draconic")
```
