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
name = 'Passage Dragonmark'

def level0(npc):
    npc.DEX += 2
    npc.abilityscoreimprovement()

    npc.speed['walking'] = 40

    npc.traits.append("***Intuitive Motion.*** When you make a Strength (Athletics) check or any ability check to operate or maintain a land vehicle, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    npc.traits.append("***Orien's Grace.*** During your turn, you can spend an amount of movement equal to half your speed to activate this trait. Once you activate Orien's Grace, you don't provoke opportunity attacks for the rest of the turn.")

    npc.bonusactions.append("***Shared Passage (Recharges on long rest).*** You can teleport up to your speed to an unoccupied space that you can see. You can bring one willing creature of your size or smaller who is carrying gear up to its carrying capacity. The creature must be within 5 feet of you.")
```
