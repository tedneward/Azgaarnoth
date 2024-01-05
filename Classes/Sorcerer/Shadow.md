# Sorcerous Origin: Shadow
Your innate magic comes from the Shadowfell. You might trace your lineage to an entity from that place, or perhaps you were exposed to its fell energy and transformed in some fundamental manner.

```
name = 'Shadow'
description = "***Sorcerous Origin: Shadow.*** Your innate magic comes from the Shadowfell. You might trace your lineage to an entity from that place, or perhaps you were exposed to its fell energy and transformed in some fundamental manner."
```

The power of shadow magic casts a strange pall over your physical presence. The spark of life that sustains you is muffled, as if it struggles to remain viable against the dark energy that imbues your soul. At your option, you can pick from or roll on the following table to create a unique quirk for your character.

**Shadow Sorcerer Quirks**
d6|Quirk
--|-----
1|You are always icy cold to the touch.
2|When you are asleep, you don't appear to breathe (though you must still breathe to survive).
3|You don't seem to bleed, even when badly injured.
4|Your heart beats once per minute (though you still need it to survive). This event sometimes surprises you.
5|You have trouble remembering that living creatures and corpses should be treated differently.
6|You blinked. Once. Last week.

```
quirks = [
    "You are always icy cold to the touch.",
    "When you are asleep, you don't appear to breathe (though you must still breathe to survive).",
    "You don't seem to bleed, even when badly injured.",
    "Your heart beats once per minute (though you still need it to survive). This event sometimes surprises you.",
    "You have trouble remembering that living creatures and corpses should be treated differently.",
    "You blinked. Once. Last week."
]
def level1(npc):
    npc.description.append(f"***Shadow Sorcerer Quirk.*** ${random(quirks)}")
```

## Eyes of the Dark
*1st-level Shadow feature*

You have darkvision with a range of 60 feet. You can cast darkness by spending 1 sorcery point. You can see through any darkness spell you cast using this ability.

```
    npc.senses['darkvision'] = 60
    npc.actions.append(f"***Eyes of the Dark.*** You can cast {spelllinkify('darkness')} by spending 1 sorcery point. You can see through any darkness spell you cast using this ability.")
```

## Strength of the Grave
*1st-level Shadow feature*

Your existence in a twilight state between life and death makes you difficult to defeat. Whenever damage reduces you to 0 hit points, you can make a Constitution saving throw (DC 5 + the damage taken). On a success, you instead drop to 1 hit point. You cannot use this feature if you are reduced to 0 hit points by radiant damage or by a critical hit.

```
    npc.traits.append("***Strength of the Grave.*** Whenever damage reduces you to 0 hit points, you can make a Constitution saving throw (DC 5 + the damage taken). On a success, you instead drop to 1 hit point. You cannot use this feature if you are reduced to 0 hit points by radiant damage or by a critical hit.")
```

## Hound of Ill Omen
*6th-level Shadow feature*

You gain the ability to call forth a howling creature of darkness to harass your foes. As a bonus action, you can spend 3 sorcery points to summon a [hound of ill omen](../../Creatures/Wolves.md#hound-of-ill-omen) to target one creature you can see. The hound appears in an unoccupied space of your choice within 30 feet of the target. Roll initiative for the hound. On its turn, it can move only toward its target by the most direct route, and it can use its action only to attack its target. The hound makes opportunity attacks, but only against its target. Additionally, the target has disadvantage on all saving throws against your spells while the hound is within 5 feet of it. The hound disappears if it is reduced to 0 hit points, if its target is reduced to 0 hit points, or after 5 minutes.

```
def level6(npc):
    npc.bonusactions.append("***Hound of Ill Omen.*** You spend 3 sorcery points to summon a [hound of ill omen](http://azgaarnoth.tedneward.com/creatures/Wolves.md#hound-of-ill-omen) to target one creature you can see. The hound appears in an unoccupied space of your choice within 30 feet of the target. Roll initiative for the hound. On its turn, it can move only toward its target by the most direct route, and it can use its action only to attack its target. The hound makes opportunity attacks, but only against its target. Additionally, the target has disadvantage on all saving throws against your spells while the hound is within 5 feet of it. The hound disappears if it is reduced to 0 hit points, if its target is reduced to 0 hit points, or after 5 minutes.")
```

## Shadow Walk
*14th-level Shadow feature*

You gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action, you can teleport up to 120 feet to an unoccupied space you can see that is also in dim light or darkness.

```
def level14(npc):
    npc.bonusactions.append("***Shadow Walk.*** When you are in dim light or darkness, you teleport up to 120 feet to an unoccupied space you can see that is also in dim light or darkness.")
```

## Shadow Form
*18th-level Shadow feature*

You can spend 3 sorcery points to transform yourself into a shadow form as a bonus action. In this form, you have resistance to all damage except force damage, and you can move through other creatures and objects as if they were difficult terrain. You take 5 force damage if you end your turn inside an object. You remain in this form for 1 minute.

```
def level18(npc):
    npc.bonusactions.append("***Shadow Form.*** You spend 3 sorcery points to transform yourself into a shadow form as a bonus action. In this form, you have resistance to all damage except force damage, and you can move through other creatures and objects as if they were difficult terrain. You take 5 (1d8) force damage if you end your turn inside an object. You remain in this form for 1 minute.")
```
