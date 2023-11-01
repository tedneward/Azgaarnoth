## Strike of the Giants
You have absorbed primeval magic that gives you an echo of the might of giants. 

Choose one of the kinds of giants listed below. As a bonus action, you can call on the power of your giant magic to imbue your attacks with additional power. The next time you hit a target with a melee or thrown weapon attack within the next minute, the attack has an additional effect depending on the origin of your giant magic:

* **Hill Giant**. The target takes an extra 1d6 damage of the weapon's type. If the target is a creature, it must succeed on a Strength saving throw or be knocked prone.
* **Stone Giant**. The target takes an extra 1d6 force damage. If the target is a creature, it must succeed on a Strength saving throw or be pushed 10 feet away from you in a straight line.
* **Frost Giant**. The target takes an extra 1d6 cold damage. If the target is a creature, it must succeed on a Constitution saving throw, or its speed is reduced to 0 until the start of your next turn.
* **Fire Giant**. The target takes an extra 1d8 fire damage.
* **Cloud Giant**. The target takes an extra 1d4 thunder damage. If the target is a creature, it must succeed on a Wisdom saving throw, or you become invisible to it until the start of your next turn.
* **Storm Giant**. The target takes an extra 1d6 lightning damage. If the target is a creature, it must succeed on a Constitution saving throw, or it has disadvantage on attack rolls until the start of your next turn.

The saving throw DC for these effects equals 8 + your proficiency bonus + your Strength or Constitution modifier.

You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
name = 'Strike of the Giants'
description = "***Feat: Strike of the Giants.*** You have absorbed primeval magic that gives you an echo of the might of giants."
def prereq(npc): return True
def apply(npc):
    giant = choose("Choose a type: ", ['Hill','Stone','Frost','Fire','Cloud','Storm'])

    def applystrike(npc):
        text = "You can call on the power of your giant magic to imbue your attacks with additional power. The next time you hit a target with a melee or thrown weapon attack within the next minute, "
        bonus = npc.STRbonus() if npc.STRbonus() >= npc.CONbonus() else npc.CONbonus()
        dc = 8 + npc.proficiencybonus() + bonus
        if giant == 'Hill':
            npc.bonusactions.append(f"***Hill Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d6 damage of the weapon's type. If the target is a creature, it must succeed on a Strength saving throw (DC {dc}) or be knocked prone.")
        elif giant == 'Stone':
            npc.bonusactions.append(f"***Stone Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d6 force damage. If the target is a creature, it must succeed on a Strength saving throw (DC {dc}) or be pushed 10 feet away from you in a straight line.")
        elif giant == 'Frost':
            npc.bonusactions.append(f"***Frost Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d6 cold damage. If the target is a creature, it must succeed on a Constitution saving throw (DC {dc}), or its speed is reduced to 0 until the start of your next turn.")
        elif giant == 'Fire':
            npc.bonusactions.append(f"***Fire Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d8 fire damage.")
        elif giant == 'Cloud':
            npc.bonusactions.append(f"***Cloud Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d4 thunder damage. If the target is a creature, it must succeed on a Wisdom saving throw (DC {dc}), or you become invisible to it until the start of your next turn.")
        elif giant == 'Storm':
            npc.bonusactions.append(f"***Storm Giant Strike ({npc.proficiencybonus()}/Recharges on long rest).*** {text} the target takes an extra 1d6 lightning damage. If the target is a creature, it must succeed on a Constitution saving throw (DC {dc}), or it has disadvantage on attack rolls until the start of your next turn.")
        else:
            error(f"WTF! {giant} -- Not a recognized giant type!")
    npc.defer(lambda npc: applystrike(npc))
```
