# Bardic College: College of Lore
Bards of the College of Lore know something about most things, collecting bits of knowledge from sources as diverse as scholarly tomes and peasant tales. Whether singing folk ballads in taverns or elaborate compositions in royal courts, these bards use their gifts to hold audiences spellbound. When the applause dies down, the audience members might find themselves questioning everything they held to be true, from their faith in the priesthood of the local temple to their loyalty to the king.

The loyalty of these bards lies in the pursuit of beauty and truth, not in fealty to a monarch or following the tenets of a deity. A noble who keeps such a bard as a herald or advisor knows that the bard would rather be honest than politic.

The college's members gather in libraries and sometimes in actual colleges, complete with classrooms and dormitories, to share their lore with one another. They also meet at festivals or affairs of state, where they can expose corruption, unravel lies, and poke fun at self-important figures of authority. Many of these bards were trained at the Lore College one operated out of the Great Library of the [Brass Dragon](../../Organizations/MilitantOrders/DraconicOrder/Brass.md). These bards are often scholars and are paid by the Academy to discover new facts about Azgaarnoth. Numerous other universities also host a Lore College.

```
name = 'College of Lore'
description = "***Bardic College: College of Lore.*** Bards of the College of Lore know something about most things, collecting bits of knowledge from sources as diverse as scholarly tomes and peasant tales. Whether singing folk ballads in taverns or elaborate compositions in royal courts, these bards use their gifts to hold audiences spellbound. When the applause dies down, the audience members might find themselves questioning everything they held to be true, from their faith in the priesthood of the local temple to their loyalty to the king."
```

## Bonus Proficiencies
*3rd-level College of Lore feature*

You gain proficiency with three skills of your choice.

```
def level3(npc):
    chooseskill(npc)
    chooseskill(npc)
    chooseskill(npc)
```

## Cutting Words
*3rd-level College of Lore feature*

You learn how to use your wit to distract, confuse, and otherwise sap the confidence and competence of others. When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed.

```
    npc.reactions.append("***Cutting Words.*** When a creature that you can see within 60 feet of you makes an attack roll, an ability check, or a damage roll, you can use your reaction to expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and subtracting the number rolled from the creature's roll. You can choose to use this feature after the creature makes its roll, but before the DM determines whether the attack roll or ability check succeeds or fails, or before the creature deals its damage. The creature is immune if it can't hear you or if it's immune to being charmed.")
```

## Additional Magical Secrets
*6th-level College of Lore feature*

You learn two spells of your choice from any class. A spell you choose must be of a level you can cast, as shown on the Bard table, or a cantrip. The chosen spells count as bard spells for you but don't count against the number of bard spells you know.

```
def level6(npc):
    npc.spellcasting['Bard'].spellsknown.append("CHOOSE-any class")
    npc.spellcasting['Bard'].spellsknown.append("CHOOSE-any class")
```

## Peerless Skill
*14th-level College of Lore feature*

When you make an ability check, you can expend one use of Bardic Inspiration. Roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail.

```
def level14(npc):
    npc.traits.append("***Peerless Skill.*** When you make an ability check, expend one use of Bardic Inspiration; roll a Bardic Inspiration die and add the number rolled to your ability check. You can choose to do so after you roll the die for the ability check, but before the DM tells you whether you succeed or fail.")
```

---

# Custom Bard Spells

* 3rd: [appraiser's light]()
