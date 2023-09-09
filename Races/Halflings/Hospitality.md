# Mark of Hospitality
They may not always have gold, but a halfling with the Mark of Hospitality is sure to be rich in friends. The magic of the mark allows the bearer to keep a place clean, and to heat, chill, and season food. But it also helps the bearer connect with others, setting troubled minds at ease--a powerful tool, though it can cause anger if abused.

```
name = 'Hospitality Dragonmarked'
description = "***Dragonmark: Mark of Healing.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. They may not always have gold, but a halfling with the Mark of Hospitality is sure to be rich in friends. The magic of the mark allows the bearer to keep a place clean, and to heat, chill, and season food. But it also helps the bearer connect with others, setting troubled minds at ease--a powerful tool, though it can cause anger if abused."
```

### Traits
The Mark of Hospitality manifests exclusively on halflings. If your character has the Mark of Hospitality, this is your halfling subrace.

**Ability Score Increase.** Your Charisma score increases by 1.

```
def level0(npc):
    npc.CHA += 1
```

**Innkeeper's Charms.** You know the cantrips [friends](../Magic/Spells/friends.md) and [prestidigitation](../Magic/Spells/prestidigitation.md). Charisma is your spellcasting ability for them.

```
    npc.cantripsknown.append('friends')
    npc.cantripsknown.append('prestidigitation')
```

**Ever Hospitable.** When you make a Charisma (Persuasion) check or an ability check involving brewer's supplies or cook's utensils, you can roll one Intuition die (a d4) and add the number rolled to the ability check.

```
    npc.traits.append("***Ever Hospitable.*** When you make a Charisma (Persuasion) check or an ability check involving brewer's supplies or cook's utensils, you can roll one Intuition die (a d4) and add the number rolled to the ability check.")
```
