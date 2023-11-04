## Wild Talent
You awaken to your psionic potential, which enhances your mind or body. Increase one ability score of your choice by 1, to a maximum of 20, to represent this enhancement.

You also harbor a wellspring of psionic power within yourself, an energy that ebbs and flows as you channel it in various ways. This power is represented by your Psionic Talent die, the starting size of which is a d6.

You can use your Psionic Talent die in the following ways:

* **Psi-Boosted Ability**. When you make an ability check with the ability increased by this feat, you can roll your Psionic Talent die and add the number rolled to the check. You can choose to do so before or after rolling the d20, but before you know whether the check succeeded or failed.
* **Psi-Guided Strike**. Once on each of your turns when you hit with an attack roll that uses the ability increased by this feat, you can roll your Psionic Talent die after you make the damage roll and then replace one of the damage dice with the number rolled on the Psionic Talent die.

***Changing the Die's Size.*** If you roll the highest number on your Psionic Talent die, it decreases by one die size after the roll. This represents you burning through your psionic energy. For example, if the die is a d6 and you roll a 6, it becomes a d4. If it's a d4 and you roll a 4, it becomes unusable until you finish a long rest.

Conversely, if you roll a 1 on your Psionic Talent die, it increases by one die size after the roll, up to its starting size. This represents you conserving psionic energy for later use. For example, if you roll a 1 on a d4, the die then becomes a d6.

Whenever you finish a long rest, your Psionic Talent die resets to its starting size. When you reach certain levels, the starting size of your Psionic Talent die increases: at 5th level (d8), 11th level (d10), and 17th level (d12).

If you have a Psionic Talent die from another source, such as a class feature, you don't get more than one die; use only the one with the largest starting size.

***Psi Replenishment.*** As a bonus action, you can calm your mind for a moment and restore your Psionic Talent die to its starting size. You then can't use Psi Replenishment again until you finish a long rest.

```
name = 'Wild Talent'
description = "***Feat: Wild Talent.*** You awaken to your psionic potential, which enhances your mind or body."
def prereq(npc): return True
def apply(npc):
    ability = chooseability(npc)

    if getattr(npc, 'psionicdie', None) == None:
        npc.psionicdie = 'd0'

    npc.traits.append(f"***Psi-Boosted Ability.*** When you make a {ability} ability check, you can roll your Psionic Talent die and add the number rolled to the check. You can choose to do so before or after rolling the d20, but before you know whether the check succeeded or failed.")
    npc.traits.append(f"***Psi-Guided Strike.*** Once on each of your turns when you hit with an attack roll that uses {ability}, you can roll your Psionic Talent die after you make the damage roll and then replace one of the damage dice with the number rolled on the Psionic Talent die.")

    def supplementpsi(npc):
        dielevels = ['d4','d6','d8','d10','d12','d20']
        if npc.psionicdie == 'd0':
            npc.psionicdie = 'd6' if npc.levels() < 5 else 'd8' if npc.levels() < 11 else 'd10' if npc.levels() < 17 else 'd12'

            npc.defer(lambda npc: npc.traits.append(f"***Psionic Talent (Recharges on long rest).*** You also harbor a wellspring of psionic power within yourself, an energy that ebbs and flows as you channel it in various ways. This power is represented by your Psionic Talent die, the starting size of which is a {npc.psionicdie}. If you roll the highest number on your Psionic Talent die, it decreases by one die size after the roll, and if the die size is d4 when it decreases, your Psionic Talent becomes unusuable until after a long rest. Conversely, if you roll a 1 on your Psionic Talent die, it increases by one die size after the roll, up to its starting size."))
        else:
            current = npc.psionicdie
            wildtalent = 'd6' if npc.levels() < 5 else 'd8' if npc.levels() < 11 else 'd10' if npc.levels() < 17 else 'd12'
            if current == wildtalent:
                npc.psionicdie = dielevels[dielevels.index(current) + 1]
            else:
                if dielevels.index(current) > dielevels.index(wildtalent):
                    npc.psionicdie = dielevels[dielevels.index(current)]
                else:
                    npc.psionicdie = dielevels[dielevels.index(wildtalent)]

            if npc.levels('Fighter') > 0 and npc.subclasses[allclasses['Fighter']].name == 'Psi Warrior':
                # This is a Psi Warrior
                replace("***Psionic Energy Dice", npc.traits, f"(Recharges on long rest).*** You harbor a wellspring of psionic energy within yourself. This energy is represented by {npc.proficiencybonus() * 2} Psionic Energy dice, which are each a {npc.psionicdie}, and they fuel various psionic powers you have, which are detailed below. You can't use a power if it requires you to use a die when your dice are all expended.")
            elif npc.levels('Rogue') > 0 and npc.subclasses[allclasses['Rogue']].name == 'Soulknife':
                replace("***Psionic Talent", npc.traits, f" (Recharges on long rest).*** You also harbor a wellspring of psionic power within yourself, an energy that ebbs and flows as you channel it in various ways. This power is represented by your Psionic Talent die, the starting size of which is a {npc.psionicdie}. If you roll the highest number on your Psionic Talent die, it decreases by one die size after the roll, and if the die size is d4 when it decreases, your Psionic Talent becomes unusuable until after a long rest. Conversely, if you roll a 1 on your Psionic Talent die, it increases by one die size after the roll, up to its starting size.")
            else:
                error("WTF! What other Psionic Subclasses are there?!?")
                npc.traits.append("***TODO:*** Figure out Psionic Wild Talent interaction!")
    npc.defer(lambda npc: supplementpsi(npc))

    npc.defer(lambda npc: npc.bonusactions.append(f"***Psi Replenishment (Recharges on long rest).*** You can calm your mind for a moment and restore your Psionic Talent die to its starting size (a {npc.psionicdie}).") )
```
