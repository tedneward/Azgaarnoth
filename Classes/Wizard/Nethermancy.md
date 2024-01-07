# Arcane Tradition: Nethermancy
You focus your studies on shadow magic, also known as nethermancy, a method for extricating the magical substance of primordial shadow from various environments, then blending it with arcane forces to augment magical effects. By such means, the spells of a shadow mage can excite or dull the senses, punch holes through reality to allow swift passage, and spin creatures from the raw substance of night. 

Common folk are often quick to distrust a nethermancer, but shadow magic's apologists defend their art by pointing out that with spells, just like any other tool, the evil is in their misapplication, not in the magic itself.

```
name = 'Nethermancy'
description = "***Arcane Tradition: Nethermancy.*** You focus your studies on shadow magic, a method for extricating the magical substance of primordial shadow from various environments, then blending it with arcane forces to augment magical effects. By such means, the spells of a shadow mage can excite or dull the senses, punch holes through reality to allow swift passage, and spin creatures from the raw substance of night."
```

## Umbral Insights
*2nd-level Nethermancy feature*

When you choose this arcane tradition, you understand the darkness as few mortal beings can. You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.

Additionally, the gold and time you must spend to copy a spell into your spellbook is halved if the copied spell does one or more of the following things:

* Creates magical darkness
* Deals necrotic damage
* Teleports you
* Conjures or summons creatures

```
def level2(npc):
    npc.traits.append("***Umbral Insights.*** You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.")
    npc.traits.append("***Shadow Scholarship.*** The gold and time you must spend to copy a spell into your spellbook is halved if the copied spell creates magical darkness, deals necrotic damage, teleports you, or conjures or summons creatures")
```

## Casting Shadows
*2nd-level Nethermancy feature*

Nearby shadows assist you in concealing your spellcasting and scaring your enemies.

While you are in dim light or darkness, you have advantage on Charisma (Intimidation) checks, and spells of 5th level or lower that you cast using a wizard spell slot do not require verbal components.

```
    npc.traits.append("***Casting Shadows.*** While you are in dim light or darkness, you have advantage on Charisma (Intimidation) checks, and spells of 5th level or lower that you cast using a wizard spell slot do not require verbal components.")
```

## Step into darkness
*6th-level Nethermancy feature*

You add the [darkness](http://azgaarnoth.tedneward.com/magic/spells/darkness) and [misty step](http://azgaarnoth.tedneward.com/magic/spells/misty-step) spells to your spellbook. While you are in dim light or darkness, if you cast [misty step](http://azgaarnoth.tedneward.com/magic/spells/misty-step) to teleport into an area of dim light or darkness, you can take the Hide action as part of the same bonus action, and you immediately regain the spell slot you used to cast the spell. Once you use this feature three times, you must finish a short or long rest before you can use it again.

```
def level6(npc):
    npc.spellcasting['Wizard'].spellbook.append('darkness')
    npc.spellcasting['Wizard'].spellbook.append('misty step')
    npc.actions.append("***Step Into Darkness (3/Recharges on short or long rest).*** While you are in dim light or darkness, if you cast [misty step](http://azgaarnoth.tedneward.com/magic/spells/misty-step) to teleport into an area of dim light or darkness, you can take the Hide action as part of the same bonus action, and you immediately regain the spell slot you used to cast the spell.")
```

## Unraveling Shadows
*10th-level Nethermancy feature*

You can sense, and sometimes direct, a silent and malevolent awareness in the magical currents of shadow magic: a presence that seeks out weakness. When you cast a spell that inflicts necrotic or psychic damage during your turn, you can choose one target of that spell. If the target is vulnerable to any damage types, it also becomes vulnerable to necrotic and psychic damage until the end of the turn. If the target has no vulnerabilities, you add your Intelligence modifier (minimum of 1) to the damage the spell deals to that creature.

```
def level10(npc):
    npc.defer(lambda npc: npc.traits.append("***Unraveling Shadows.*** When you cast a spell that inflicts necrotic or psychic damage during your turn, you can choose one target of that spell. If the target is vulnerable to any damage types, it also becomes vulnerable to necrotic and psychic damage until the end of the turn. If the target has no vulnerabilities, you add {npc.INTbonus()} to the damage the spell deals to that creature.") )
```

## Conjured Gloom
*14th-level Nethermancy feature*

You can invest shadow magic into creatures you conjure. When you use a conjuration spell to summon or create one or more creatures, you can choose to grant each of those creatures 15 temporary hit points, and advantage on Dexterity (Stealth) checks for the spell's duration. A creature with sight that gains these benefits also gains darkvision out to a range of 60 feet. If such a creature already has darkvision, its range increases by 60 feet. Creatures you augment in this way also have sunlight sensitivity, giving them disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight whilst in direct sunlight.

Additionally, when you cast a conjuration spell that summons or creates one or more creatures, you can choose for the space in which each creature first appears to become heavily obscured by magical darkness until the end of your next turn.

```
def level14(npc):
    npc.traits.append("***Conjured Gloom.*** When you use a conjuration spell to summon or create one or more creatures, you can choose to grant each of those creatures 15 temporary hit points, and advantage on Dexterity (Stealth) checks for the spell's duration. A creature with sight that gains these benefits also gains darkvision out to a range of 60 feet. If such a creature already has darkvision, its range increases by 60 feet. Creatures you augment in this way also have Sunlight Sensitivity, giving them disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight whilst in direct sunlight. Additionally, you can choose for the space in which each creature first appears to become heavily obscured by magical darkness until the end of your next turn.")
```

---

# Nethermantic Spells

## Cantrips
* [shifting shadow](../../Magic/Spells/shifting-shadow.md)

## 4th-level
* [blade of flickering shadows](../../Magic/Spells/blade-of-flickering-shadows.md)

## 5th-level
* [shadow magic](../../Magic/Spells/shadow-magic.md)

## 6th-level
* [inevitable winter](../../Magic/Spells/inevitable-winter.md)

