# Monastic Tradition: Way of Shadow
Monks of the Way of Shadow follow a tradition that values stealth and subterfuge. These monks might be called ninjas or shadowdancers, and they serve as spies and assassins. Sometimes the members of a ninja monastery are family members, forming a clan sworn to secrecy about their arts and missions. Other monasteries are more like thieves' guilds, hiring out their services to nobles, rich merchants, or anyone else who can pay their fees. Regardless of their methods, the heads of these monasteries expect the unquestioning obedience of their students.

These monks are often deeply involved in, if not the head of, several Rogues' Guilds. Monasteries dedicated to the Way of Shadow are deeply-hidden secrets, but rumors abound around location of several of them deep in the [Dradehalian Empire](../../Nations/Dradehalia.md); whether they work for that nation or simply found a remote location there centuries prior is not known. There is, however, at least one monastery in [Yithi](../../Nations/Yithi.md) that is known to the tribes, and they are frequently asked to take on missions for the Prince in exchange for court support and continued secrecy. It is also rumored that the [Order of the Copper Dragon](../../Organizations/DraconicOrder/Copper.md) maintain one monastery dedicated to the Order somewhere, as well.

```
name = 'Way of Shadow'
description = "***Monastic Tradition: Way of Shadow.*** Monks of the Way of Shadow follow a tradition that values stealth and subterfuge. These monks might be called ninjas or shadowdancers, and they serve as spies and assassins. Sometimes the members of a ninja monastery are family members, forming a clan sworn to secrecy about their arts and missions. Other monasteries are more like thieves' guilds, hiring out their services to nobles, rich merchants, or anyone else who can pay their fees. Regardless of their methods, the heads of these monasteries expect the unquestioning obedience of their students."
```

## Shadow Arts
*3rd-level Way of Shadow feature*

You can use your ki to duplicate the effects of certain spells. As an action, you can spend 2 ki points to cast Darkness, Darkvision, Pass without Trace, or Silence, without providing material components. Additionally, you gain the Minor Illusion cantrip if you don't already know it.

```
def level3(npc):
    npc.actions.append(f"***Ki: Shadow Arts.*** You can spend 2 ki points to cast one of {spelllinkify('darkness')}, {spelllinkify('darkvision')}, {spelllinkify('pass without trace')}, or {spelllinkify('silence')}, without providing material components.")
    spellcasting = innatecaster(npc, 'WIS', name)
    spellcasting.cantripsknown.append('minor illusion')
```

## Shadow Step
*6th-level Way of Shadow feature*

You gain the ability to step from one shadow into another. When you are in dim light or darkness, as a bonus action you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn.

```
def level6(npc):
    npc.bonusactions.append("***Shadow Step.*** When you are in dim light or darkness, you can teleport up to 60 feet to an unoccupied space you can see that is also in dim light or darkness. You then have advantage on the first melee attack you make before the end of the turn.")
```

## Cloak of Shadows
*11th-level Way of Shadow feature*

You have learned to become one with the shadows. When you are in an area of dim light or darkness, you can use your action to become invisible. You remain invisible until you make an attack, cast a spell, or are in an area of bright light.

```
def level11(npc):
    npc.actions.append("***Cloak of Shadows.*** When you are in an area of dim light or darkness, you can become invisible. You remain invisible until you make an attack, cast a spell, or are in an area of bright light.")
```

## Opportunist
*17th-level Way of Shadow feature*

You can exploit a creature's momentary distraction when it is hit by an attack. Whenever a creature within 5 feet of you is hit by an attack made by a creature other than you, you can use your reaction to make a melee attack against that creature.

```
def level17(npc):
    npc.reactions.append("***Opportunist.*** Whenever a creature within 5 feet of you is hit by an attack made by a creature other than you, you can make a melee attack against that creature.")
```
