# Mark of Passage
The Mark of Passage governs motion, allowing its bearer to move with uncanny speed and precision. Running, leaping, climbing--the Mark of Passage enhances every form of movement. The bearer of the mark can even slip through space, leaping from point to point in the blink of an eye.

### Traits
The Mark of Passage only manifests on humans. If your character has the Mark of Passage, these traits replace the human's Ability Score Increase trait given in the Player's Handbook.

**Ability Score Increase**. Your Dexterity score increases by 2, and one other ability score of your choice increases by 1.

**Courier's Speed**. Your base walking speed increases to 40 ft.

**Intuitive Motion**. When you make a Strength (Athletics) check or any ability check to operate or maintain a land vehicle, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

**Orien's Grace**. During your turn, you can spend an amount of movement equal to half your speed to activate this trait. Once you activate Orien's Grace, you don't provoke opportunity attacks for the rest of the turn.

**Shared Passage**. You can use your bonus action to teleport up to your speed to an unoccupied space that you can see. You can bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you. Once you use this trait, you can't use it again until you finish a long rest.

```
name = 'Passage Dragonmarked'
description = "***Dragonmark: Mark of Passage.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. The Mark of Passage governs motion, allowing its bearer to move with uncanny speed and precision. Running, leaping, climbing--the Mark of Passage enhances every form of movement. The bearer of the mark can even slip through space, leaping from point to point in the blink of an eye."

def level0(npc):
    npc.DEX += 2
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    ability = choose("Choose an ability to improve: ", abilities)
    if ability == 'STR': npc.STR += 1
    elif ability == 'DEX': npc.DEX += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    elif ability == 'CHA': npc.CHA += 1

    npc.speed['walking'] = 40

    npc.traits.append("***Intuitive Motion.*** When you make a Strength (Athletics) check or any ability check to operate or maintain a land vehicle, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    npc.traits.append("***Orien's Grace.*** During your turn, you can spend an amount of movement equal to half your speed to activate this trait. Once you activate Orien's Grace, you don't provoke opportunity attacks for the rest of the turn.")

    npc.bonusactions.append("***Shared Passage (Recharges on long rest).*** You can teleport up to your speed to an unoccupied space that you can see. You can bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you.")

    quirk = random([
        "Your dragonmark is unusually small.",
        "Your dragonmark is remarkably large.",
        "Your dragonmark slowly moves around your body.",
        "Your dragonmark glows dramatically when you use it.",
        "Your dargonmark emits a soft hum when you use it.",
        "Your dragonmark itches when you’re near someone with a dragonmark.",
        "Your dragonmark tingles when you’re near someone with the same mark.",
        "Your dragonmark tickles when you use it.",
        "Your dragonmark is an unusual color but a normal shape."
    ])
    npc.description.append(f"***Dragonmark Quirk.*** {quirk}")
```
