# Arcane Tradition: Conjuration
As a conjurer, you favor spells that produce objects and creatures out of thin air. You can conjure billowing clouds of killing fog or summon creatures from elsewhere to fight on your behalf. As your mastery grows, you learn spells of transportation and can teleport yourself across vast distances, even to other planes of existence, in an instant.

```
name = 'Conjuration'
description = "***Arcane Tradition: Conjuration.*** As a conjurer, you favor spells that produce objects and creatures out of thin air. You can conjure billowing clouds of killing fog or summon creatures from elsewhere to fight on your behalf. As your mastery grows, you learn spells of transportation and can teleport yourself across vast distances, even to other planes of existence, in an instant."
```

## Conjuration Savant
*2nd-level Conjuration feature*

The gold and time you must spend to copy a Conjuration spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Conjuration Savant.*** The gold and time you must spend to copy a Conjuration spell into your spellbook is halved.")
```

## Minor Conjuration
*2nd-level Conjuration feature*

When you select this school, you can use your action to conjure up an inanimate object in your hand or on the ground in an unoccupied space that you can see within 10 feet of you. This object can be no larger than 3 feet on a side and weigh no more than 10 pounds, and its form must be that of a nonmagical object that you have seen. The object is visibly magical, radiating dim light out to 5 feet.

The object disappears after 1 hour, when you use this feature again, or if it takes any damage.

```
    npc.actions.append("***Minor Conjuration.*** You conjure up an inanimate object in your hand or on the ground in an unoccupied space that you can see within 10 feet of you. This object can be no larger than 3 feet on a side and weigh no more than 10 pounds, and its form must be that of a nonmagical object that you have seen. The object is visibly magical, radiating dim light out to 5 feet. The object disappears after 1 hour, when you use this feature again, or if it takes any damage.")
```

## Benign Transportation
*6th-level Conjuration feature*

You can use your action to teleport up to 30 feet to an unoccupied space that you can see. Alternatively, you can choose a space within range that is occupied by a Small or Medium creature. If that creature is willing, you both teleport, swapping places.

Once you use this feature, you can't use it again until you finish a long rest or you cast a conjuration spell of 1st level or higher.

```
def level6(npc):
    npc.actions.append("***Benign Transportation (Recharges on long rest or 1st-level-or-better conjuration spell casting).*** You teleport up to 30 feet to an unoccupied space that you can see. Alternatively, you can choose a space within range that is occupied by a Small or Medium creature. If that creature is willing, you both teleport, swapping places.")
```

## Focused Conjuration
*10th-level Conjuration feature*

While you are concentrating on a conjuration spell, your concentration can't be broken as a result of taking damage.

```
def level10(npc):
    npc.traits.append("***Focused Concentration.*** While you are concentrating on a conjuration spell, your concentration can't be broken as a result of taking damage.")
```

## Durable Summons
*14th-level Conjuration feature*

Any creature that you summon or create with a conjuration spell has 30 temporary hit points.

```
def level14(npc):
    npc.traits.append("***Durable Summons.*** Any creature that you summon or create with a conjuration spell has 30 temporary hit points.")
```
