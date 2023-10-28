## Polearm Master
You gain the following benefits:

* When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you can use a bonus action to make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and it deals bludgeoning damage.
* While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon.

```
name = 'Polearm Master'
description = "***Feat: Polearm Master.*** You have mastered the fine art of using a polearm as a weapon."
def prereq(npc): return True
def apply(npc):
    npc.bonusactions.append("***Polearm Mastery.*** When you take the Attack action and attack with only a glaive, halberd, quarterstaff, or spear, you make a melee attack with the opposite end of the weapon. This attack uses the same ability modifier as the primary attack. The weapon's damage die for this attack is a d4, and it deals bludgeoning damage.")
    npc.traits.append("***Polearm Mastery.*** While you are wielding a glaive, halberd, pike, quarterstaff, or spear, other creatures provoke an opportunity attack from you when they enter the reach you have with that weapon.")
```
