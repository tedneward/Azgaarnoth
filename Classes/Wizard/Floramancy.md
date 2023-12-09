# Arcane Tradition: Floramancy
Floramancy wizards are sometimes confused with or mistaken for druids. They tend their gardens, protect their woods, or study in cabins buried deep in the lush jungles of the world, living in harmony with the plants, animals, and nature that they revere. Their abodes are often decorated with the preserved green-things of the world, delicately displayed for visitors to truly see the beauty of nature. Floramancy wizards dedicate themselves to magic that evokes the strength, beauty, and fortitude of the natural world.

Floramancers are frequently found in the [Animalists](../../Organizations/MageSchools/Animalists.md) school, when they're found indoors at all.

```
name = 'Floramancy'
description = "***Arcane Tradition: Floramancy.*** Floramancy wizards are sometimes confused with or mistaken for druids. They tend their gardens, protect their woods, or study in cabins buried deep in the lush jungles of the world, living in harmony with the plants, animals, and nature that they revere. Their abodes are often decorated with the preserved green-things of the world, delicately displayed for visitors to truly see the beauty of nature. Floramancy wizards dedicate themselves to magic that evokes the strength, beauty, and fortitude of the natural world."
```

## Nature Savant
*2nd-level Floramancy feature*

You gain proficiency in the Nature skill.

Additionally, you have advantage on Intelligence (Nature) checks to identify plants such as trees, flowers, and herbs.

```
def level2(npc):
    npc.skills.append('Nature')
    npc.traits.append("***Nature Savant.*** You have advantage on Intelligence (Nature) checks to identify plants such as trees, flowers, and herbs.")
```

## Nature Magic
*2nd-level Floramancy feature*

You have a knowledge of nature and magic that is unparalleled. The following nature-based magic spells are added to the Wizard spell list for you: [barkskin](../../Magic/Spells/barkskin.md), [commune with nature](../../Magic/Spells/commune-with-nature.md), [detect poison and disease](../../Magic/Spells/detect-poison-and-disease.md), [druidcraft](../../Magic/Spells/druidcraft.md), [grasping vine](../../Magic/Spells/grasping-vine.md), [locate animals or plants](../../Magic/Spells/locate-animals-or-plants.md), [plant growth](../../Magic/Spells/plant-growth.md), [protection from poison](../../Magic/Spells/protection-from-poison.md), [speak with plants](../../Magic/Spells/speak-with-plants.md), [spike growth](../../Magic/Spells/spike-growth.md), [thorn whip](../../Magic/Spells/thorn-whip.md), [transport via plants](../../Magic/Spells/transport-via-plants.md), [tree stride](../../Magic/Spells/tree-stride.md), and [wall of thorns](../../Magic/Spells/wall-of-thorns.md).

## Plant Camouflage
*6th-level Floramancy feature*

You can magically adapt your body to appear more plant-like. As an action, your body becomes covered in leaves, vines, petals, or twigs. This transformation lasts for 10 minutes. While transformed in this way, you have advantage on Dexterity (Stealth) checks made to hide in any natural terrain brimming with plantlife. You can use this ability a number of times per day equal to your Intelligence modifier (minimum of once).

You regain all expended uses of this ability when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Plant Camouflage ({npc.INTbonus()}/Recharges on long rest).*** your body becomes covered in leaves, vines, petals, or twigs. This transformation lasts for 10 minutes. While transformed in this way, you have advantage on Dexterity (Stealth) checks made to hide in any natural terrain brimming with plantlife.{'' if npc.levels('Wizard') < 10 else 'You can choose to add thorns to your transformation. If you do, whenever you are targeted by a melee attack, the attacker takes 2d6 piercing damage from the thorns covering your body. The damage counts as magical for the purposes of overcoming resistance and immunity to non-magical attacks and damage.' if npc.levels('Wizard') < 14 else 'You can choose to add thorns to your transformation. If you do, whenever you are targeted by a melee attack, the attacker takes 4d6 piercing damage from the thorns covering your body. The damage counts as magical for the purposes of overcoming resistance and immunity to non-magical attacks and damage.'}") )
```

## Thorns
*10th-level Floramancy feature*

Whenever you use your Plant Camouflage ability, you can choose to add thorns to your transformation. If you do, whenever you are targeted by a melee attack, the attacker takes 2d6 piercing damage from the thorns covering your body. The damage counts as magical for the purposes of overcoming resistance and immunity to non-magical attacks and damage. At 14th level, the thorn damage increases to 4d6.

## Photosynthesis
*14th-level Floramancy feature*

Whenever you use your Plant Camouflage ability, you are renewed while you are in sunlight. If you spend a total of 10 minutes or more in direct sunlight while transformed, you do not require food or drink for that day. If you are reduced to zero hit points whilst you are transformed in this way, you automatically stabilize if you are in direct sunlight.

Additionally, for a single transformation, you regain 1d4 hit points for each minute spent in direct sunlight. 

If this ability hasn't been used, and you are reduced to zero hit points while transformed in sunlight, it automatically activates. 

After you have used the regeneration part of this ability, you cannot use it again until after you have completed a long rest.

```
def level14(npc):
    npc.traits.append("***Photosynthesis.*** Whenever you use your Plant Camouflage ability, you are renewed while you are in sunlight. If you spend a total of 10 minutes or more in direct sunlight while transformed, you do not require food or drink for that day. If you are reduced to zero hit points whilst you are transformed in this way, you automatically stabilize if you are in direct sunlight.Additionally, for a single transformation, you regain 1d4 hit points for each minute spent in direct sunlight. If this ability hasn't been used, and you are reduced to zero hit points while transformed in sunlight, it automatically activates. After you have used the regeneration part of this ability, you cannot use it again until after you have completed a long rest.")
```

---

# Floramancy Spells

## Cantrips
* [preserve plant](../../Magic/Spells/preserve-plant.md)
* [whimsybloom](../../Magic/Spells/whimsybloom.md)

## 3rd-level
* [conjure plants](../../Magic/Spells/conjure-plants.md)

## 5th-level
* [sunglow](../../Magic/Spells/sunglow.md)

