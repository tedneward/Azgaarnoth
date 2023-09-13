# Roguish Archetype: Inquisitive
As an archetypal Inquisitive, you excel at rooting out secrets and unraveling mysteries. You rely on your sharp eye for detail, but also on your finely honed ability to read the words and deeds of other creatures to determine their true intent. You excel at defeating creatures that hide among and prey upon ordinary folk, and your mastery of lore and your sharp eye make you well equipped to expose and end hidden evils.

```
name = 'Inquisitive'
description = "***Roguish Archetype: Inquisitive.*** You excel at rooting out secrets and unraveling mysteries. You rely on your sharp eye for detail, but also on your finely honed ability to read the words and deeds of other creatures to determine their true intent. You excel at defeating creatures that hide among and prey upon ordinary folk, and your mastery of lore and your sharp eye make you well equipped to expose and end hidden evils."
```

## Ear for Deceit
*3rd-level Inquisitive feature*

You develop a keen ear for picking out lies. Whenever you make a Wisdom (Insight) check to determine whether a creature is lying, treat a roll of 7 or lower on the d20 as an 8.

```
def level3(npc):
    npc.traits.append("***Ear for Deceit.*** Whenever you make a Wisdom (Insight) check to determine whether a creature is lying, treat a roll of 7 or lower on the d20 as an 8.")
```

## Eye for Detail
*3rd-level Inquisitive feature*

You can use a bonus action to make a Wisdom (Perception) check to spot a hidden creature or object or to make an Intelligence (Investigation) check to uncover or decipher clues.

```
    npc.bonusactions.append("***Eye for Detail.*** You can make a Wisdom (Perception) check to spot a hidden creature or object or to make an Intelligence (Investigation) check to uncover or decipher clues.")
```

## Insightful Fighting
*3rd-level Inquisitive feature*

You gain the ability to decipher an opponent's tactics and develop a counter to them. As a bonus action, you make a Wisdom (Insight) check against a creature you can see that isn't incapacitated, contested by the target's Charisma (Deception) check. If you succeed, you can use your Sneak Attack against that target even if you don't have advantage on the attack roll, but not if you have disadvantage on it.

This benefit lasts for 1 minute or until you successfully use this feature against a different target.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Insightful Fighting.*** You make a Wisdom (Insight) check against a creature you can see that isn't incapacitated, contested by the target's Charisma (Deception) check. If you succeed, you can use your Sneak Attack{' (increased by 3d6)' if npc.levels('Rogue') >= 17 else ''} against that target even if you don't have advantage on the attack roll, but not if you have disadvantage on it. This benefit lasts for 1 minute or until you successfully use this feature against a different target."))
```

## Steady Eye
*9th-level Inquisitive feature*

You gain advantage on any Wisdom (Perception) or Intelligence (Investigation) check if you move no more than half your speed on the same turn.

```
def level9(npc):
    npc.traits.append("***Steady Eye.*** You gain advantage on any Wisdom (Perception) or Intelligence (Investigation) check if you move no more than half your speed on the same turn.")
```

## Unerring Eye
*13th-level Inquisitive feature*

Your senses are almost impossible to foil. As an action, you sense the presence of illusions, shapechangers not in their original form, and other magic designed to deceive the senses within 30 feet of you, provided you aren't blinded or deafened. You sense that an effect is attempting to trick you, but you gain no insight into what is hidden or into its true nature.

You can use this feature a number of times equal to your Wisdom modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.

```
def level13(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Unerring Eye ({npc.WISbonus()}/Recharges on long rest).*** You sense the presence of illusions, shapechangers not in their original form, and other magic designed to deceive the senses within 30 feet of you, provided you aren't blinded or deafened. You sense that an effect is attempting to trick you, but you gain no insight into what is hidden or into its true nature."))
```

## Eye for Weakness
*17th-level Inquisitive feature*

You learn to exploit a creature's weaknesses by carefully studying its tactics and movement. While your Insightful Fighting feature applies to a creature, your Sneak Attack damage against that creature increases by 3d6.

