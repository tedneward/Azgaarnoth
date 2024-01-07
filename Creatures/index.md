# Master List of the Creatures of Azgaarnoth

[Creatures A-Z](./index-az.md) | [Demons](Demons/index.md) | [Devils](Devils/index.md) | [Dragons](Dragons/index.md) | [Giants](Giants/index.md)

## Categories
[Aberrations](./index-aberration.md) | [Beasts](./index-beast.md) | [Constructs](./index-construct.md) | [Celestials](./index-celestial.md) | [Dragons](./index-dragon.md) | [Elementals](./index-elemental.md) | [Fey](./index-fey.md) | [Fiend](./index-fiend.md) | [Giant](./index-giant.md) | [Humanoids](./index-humanoid.md) | [Monstrosities](./index-monstrosity.md) | [Oozes](./index-ooze.md) | [Plants](./index-plant.md) | [Undead](./index-undead.md)

## Players!
For PCs to know more about a creature, they must make a skill check of the type specified in the below table:

Monster Type | Skill Check
------------ | ----------------
Beasts | Wisdom (Survival)
Celestials, Elementals, Fiends, Undead | Intelligence (Religion)
Fey, Oozes, Plants | Intelligence (Nature)
Aberrations, Constructs, Dragons, Giants, Monstrosities | Intelligence (Arcana)
Humanoids | Intelligence (History)

... and the resulting roll reveals the following:

DC + CR | Knowledge
------- | ---------------------
CR + 5  | attacks, Hit Dice, speed, Armor Class
CR + 10 | abilities, bonus attacks, reactions, class (if any)
CR + 15 | traits, damage resistances, class levels (if any)
CR + 20 | damage immunities, damage vulnerabilities, condition immunities
CR + 25 | complete lore (you get the link to the creature page)

Alternatively, a player making a skill check can ask one specific, targeted (as in, can be answered definitively "yes/no" or with a numeric value or one/two-word answer) question for each "5" of the die roll, such as:

* "What is (the creature)'s strongest attack?"
* "Can (the creature) make ranged attacks?"
* "Can (the creature) be hit by ordinary non-silvered weapons?"

If you are a player, please don't consult the reference page during the game! Browse all you want in between sessions, but let's keep it a little mysterious during the game, yeah?

---

## Creature Templates
- Bestial: [Alpha](Templates/Alpha.md), [Young](Templates/Young.md)
- Martial: [Berserker](Templates/Berserker.md), [Knight](Templates/Knight.md), [Soldier](Templates/Soldier.md), [Elite Warrior](Templates/Elite.md), [Sergeant](Templates/Sargeants.md), [Veteran](Templates/Veteran.md)
- [Dire](Templates/Dire.md)
- [Draconic](Dragons/DragonTemplates.md): [Dracolich](Dragons/DragonTemplates.md#dracolich), [Ghost](Dragons/DragonTemplates.md#ghost), [Shadow](Dragons/DragonTemplates.md#shadow), [Skeletal](Dragons/DragonTemplates.md#skeletal), [Zombie](Dragons/DragonTemplates.md#zombie)
- [Half-Dragon](Templates/HalfDragon.md)
- Undeath: [Skeleton](Templates/Skeletal.md), [Zombie](Templates/Zombie.md), [Withered](Templates/Withered.md), [Demizen](Templates/Demizen.md), [Ghoul](Templates/Ghoulish.md), [Ghost](Templates/Ghostly.md), [Mummy](Templates/Mummified.md), [Lich](Templates/Lich.md), [Vampiric](Templates/Vampiric.md)

---

## Markdown Template

## Name
General description

### Environment
Arctic, Astral, Coastal, Desert, Forest, Grassland, Hill, Mountain, Ruins, Swamp, Underdark, Underwater, Urban, Summoned/Conjured

### Token
![](-Token.png)

>### (Subtype if any) (Name)
>*Size Type, alignment*
>___
>- **Armor Class** AC (breakdown)
>- **Hit Points** HP (Hit Dice)
>- **Speed** 30 ft.
>___
>|**STR**|**DEX**|**CON**|**INT**|**WIS**|**CHA**|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|10 (0)|10 (0)|10 (0)|10 (+0)|10 (+0)|10 (0)|
>
>___
>- **Proficiency Bonus** 
>- **Saving Throws** 
>- **Damage Vulnerabilities** 
>- **Damage Resistances** 
>- **Damage Immunities** 
>- **Condition Immunities** 
>- **Skills** 
>- **Senses** 
>- **Languages** 
>- **Challenge** 
>___
>***Feature.***   
>
>#### Actions
>#### Bonus Actions
>#### Reactions
>#### Legendary Actions
>
### A Creature's Lair
Pre-text
#### Lair Actions
#### Regional Effects

---

# Encounter goals

---

# Roll20 template
Maybe?

```
// For use with https://github.com/jfrondeau/roll20/blob/master/statblock-import-5e.js
// Linked from https://app.roll20.net/forum/post/1612177/script-statblock-import-for-5e-character-sheet#

Creature Name
Medium humanoid (sahuagin), lawful evil //NAME AND SIZE TYPE ALIGNMENT GO ON 2 LINES
Armor Class 10 (natural armor) //EACH ITEM (AC, HP, Speed) SHOULD BE SEPARATED BY A LINE BREAK
Hit Points 22 (4d8 + 4)
Speed 30ft., swim 40 ft.
STR 13 (+1) //SPACING DOESN'T SEEM TO MATTER THAT MUCH, BUT EACH STAT SHOULD BE ON ITS OWN LINE//
DEX 11 (+0)
CON 12 (+1)
INT 12 (+1)
WIS 13 (+1)
CHA 9 (- 1)
Skills Perception +5
Senses darkvision 120ft., passive Perception 15 
Languages Common, Elven
Challenge 1/2 (100 XP)
Blood Frenzy. The creature has advantage on melee attack rolls against any creature that doesn't have all its hit points. //EACH ITEM IN ITS OWN LINE, AND THIS WILL GO INTO TRAITS. TRAIT NAME, PERIOD. FOLLOWED BY DESCRIPTION.
Limited Amphibiousness. The creature can breathe air and water, but it needs to be submerged at least once every 4 hours to avoid suffocating.
Shark Telepathy. The creature can magically command any shark within 120 feet of it, using a limited telepathy.
ACTIONS // THIS PART MARKS WHERE THE NPC ACTIONS START. 
Multiattack. The creature makes two melee attacks: one with its bite and one with its claws or spear. //SCRIPT CORRECTLY PLACES MULTIATTACK, INTO THE MA LINE. 
Bite. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage.
Claws. Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage.
Spear. Melee or Ranged Weapon Attack:+3 to hit, reach 5 ft. or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage, or 5 (1d8 + 1) piercing damage if used with two hands to make a melee attack. //ONLY THING TO NOTE IS THAT MY COPY PASTELIKED TO TURN 1's into L's AND SCRIPT DOES NOT TURN ON MULTIATTACK FOR ATTACKS THAT HAVE THEM, SO YOU'LL DO THAT MANUALLY
```
