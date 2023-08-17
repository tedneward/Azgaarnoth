# Creatures of Azgaarnoth
These creatures are found in various places across the map. Over time, all these will be "tuned" to the map specifically, but many of them are direct "lifts" from the official D&D content so that I have convenient links that are under my control for various purposes.

## Creature Modifier Templates
- Dire
- Half-Dragon
- Unead
    - [Ghost](./Templates/Ghostly.md)
    - Mummy
    - [Skeleton](./Templates/Skeletal.md)
    - Withered
    - [Zombie](./Templates/Zombie.md)

## A
- [Aarakocra](Aarakocra.md)
- [Abishai](Abishai.md)
- [Aboleth](Aboleth.md)
- [Abomination](Abomination.md)
- [Achaierai](Achaierai.md)
- [Allip](Allip.md)
- [Angel](Angel.md)
- [Animated Object](AnimatedObjects.md)
- [Ankheg](Ankheg.md)
- [Ape](Ape.md)
- [Awakened](Awakened.md)
- [Axe Beak](AxeBeak.md)
- [Azer](Azer.md)

## B
- [Baboon](Ape.md#baboon)
- [Badger](Badger.md)
- [Banshee](Banshee.md)
- [Barghest](Barghest.md)
- [Basilisk](Basilisk.md)
- [Bat](Bat.md)
- [Bear](Bear.md)
- [Beetle](Beetle.md)
- [Behir](Behir.md)
- [Blink Dog](Dog.md#blink-dog)
- [Boar](Boar.md)
- [Boneclaw](Boneclaw.md)
- [Bonedrinker](Bonedrinker.md)
- [Brother of Undeath](BrotherOfUndeath.md)
- [Bulette](Bulette.md)
- [Bullywug](Bullywug.md)

## C
- [Cat](Cat.md)
- [Chimera](Chimera.md)
- [Corpse Flower](CorpseFlower.md)
- [Crab](Crab.md)
- [Crocodile](Crocodile.md)

## D
- [Death Dog](Dog.md#death-dog)
- [Deer](Deer.md)
- [Dog](Dog.md)

## E
- [Elemental](Elemental.md)
- [Elephant](Elephant.md)
- [Empyrean](Empyrean.md)
- [Ettercap](Ettercap.md)

## F
- [Frog](Frog.md)

## G
- [Gargoyle](Gargoyle.md)
- [Ghast](Ghast.md)
- [Ghost](Ghost.md)
- [Ghoul](Ghoul.md)
- [Giant Ape](Ape.md#giant-ape)
- [Gibbering Mouther](GibberingMouther.md)
- [Goat](Goat.md)
- [Golem](Golem.md)
- [Gray Render](GrayRender.md)

## H
- [Hag](Hag.md)
- [Hell Hound](Dog.md#hell-hound)
- [Helmed Horror](HelmedHorror.md)
- [Hydra](Hydra.md)

## I
- [Invisible Stalker](Elemental.md#invisible-stalker)

## J

## K

## L
- [Lion](Cat.md#lion)
- [Lizard](Lizard.md)

## M
- [Magen](Magen.md)
- [Magmin](Elemental.md#magmin)
- [Mephit](Mephit.md)

## N
- [Nightstriker Serpent](NightstrikerSerpent.md)

## O
- [Ooze](Ooze.md)
- [Owlbear](Owlbear.md)

## P
- [Panther](Cat.md#panther)

## Q

## R
- [Raptor](Raptor.md)
- [Rat](Rat.md)

## S
- [Saber-Toothed Tiger](Cat.md#saber-toothed-tiger)
- [Sahuagin](Sahuagin.md)
- [Scorpion](Scorpion.md)
- [Sea Horse](SeaHorse.md)
- [Shadow](Shadow.md)
- [Shambling Mound](ShamblingMound.md)
- [Shark](Shark.md)
- [Skull Lord](SkullLord.md)
- [Snake](Snake.md)
- [Specter](Specter.md)
- [Spider](Spider.md)
- [Sunken Sailor](SunkenSailor.md)

## T
- [Tiger](Cat.md#tiger)
- [Troll](Troll.md)

## U

## V

## W
- [Water Weird](Elemental.md#water-weird)
- [Weasel](Weasel.md)
- [Whale](Whale.md)
- [Wight](Wight.md)
- [Will O' Wisp](WillOWisp.md)
- [Withered Hound](Dog.md#withered-hound)
- [Wolf](Wolf.md)
- [Worg](Wolf.md#worg)
- [Wraith](Wraith.md)

## X

## Y

## Z

---

# Creature Template

## Name
General description

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

---

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
