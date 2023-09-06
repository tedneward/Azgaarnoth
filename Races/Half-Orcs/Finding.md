# Mark of Finding
The Mark of Finding sharpens the senses of those who carry it, guiding the hunter to their prey. It first appeared in the [United Hordes](../Nations/Tragekia.md), where Hordes scouts used it to find their prey. The mark helped unite humans and orcs in the [United Hordes](../Nations/Tragekia.md) and brought [House Thar'ashk](../../Organizations/Houses/Tharashk.md) to lead the Five Hordes for a time.

```
name = 'Finding Dragonmarked'
```

### Traits
The Mark of Finding only manifests on half-orcs. If your character has the Mark of Finding, these traits replace the Ability Score Increase, Menacing, Relentless Endurance, and Savage Attacks given in the Player's Handbook. Despite their orcish blood, heirs of the Mark of Finding often resemble their human parents in appearance and temperament. When you create your character, decide if the signs of your orcish ancestry are obvious or subtle.

```
def level0(npc):
```

* **Ability Score Increase**. Your Strength and Wisdom scores both increase by 1. In addition, one ability score of your choice increases by 1.

```
    npc.STR += 1
    npc.abilityscoreimprovement()
```

* **Hunter's Intuition**. Your mark sharpens your senses and helps you find your prey. When you make a Wisdom (Perception) or Wisdom (Survival) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

```
    npc.traits.append("***Hunter's Intuition.*** Your mark sharpens your senses and helps you find your prey. When you make a Wisdom (Perception) or Wisdom (Survival) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")
```

* **Imprint Prey**. As a bonus action, choose one creature you can see within 30 feet of you. The target is imprinted in your mind until it dies or you use this trait again. Alternatively, you can imprint a creature as your quarry whenever you succeed on a Wisdom (Survival) check to track it.
    When you are tracking your quarry, double the result of your Intuition die. When your quarry is within 60 feet of you, you have a general sense of its location. Your attacks against it ignore half cover. If you can't see the target when you attack it, your inability to see it doesn't impose disadvantage on the attack roll. Likewise, your quarry doesn't doesn't gain advantage on attack rolls against you due to being hidden or invisible. Once you use this trait, you cannot use it again until you finish a short or long rest.

```
    npc.bonusactions.append("***Imprint Prey (Recharges on short or long rest).*** Choose one creature you can see within 30 feet of you. The target is imprinted in your mind until it dies or you use this trait again. Alternatively, you can imprint a creature as your quarry whenever you succeed on a Wisdom (Survival) check to track it. When you are tracking your quarry, double the result of your Intuition die. When your quarry is within 60 feet of you, you have a general sense of its location. Your attacks against it ignore half cover. If you can't see the target when you attack it, your inability to see it doesn't impose disadvantage on the attack roll. Likewise, your quarry doesn't doesn't gain advantage on attack rolls against you due to being hidden or invisible.")
```

* **Nature's Voice**. When you reach 3rd level you gain the ability to cast [locate animals or plants](../Magic/Spells/locate-animals-or-plants.md), but only as a ritual.

```
def level3(npc):
    npc.traits.append(f"***Nature's Voice.*** You can cast {spelllinkify('locate animals or plants')} as a ritual.")
```
