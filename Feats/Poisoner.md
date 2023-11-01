## Poisoner
You can prepare and deliver deadly poisons, gaining the following benefits:

* When you make a damage roll, you ignore resistance to poison damage.
* You can coat a weapon in poison as a bonus action, instead of an action.
* You gain proficiency with the poisoner's kit if you don't already have it. With one hour of work using a poisoner's kit and expending 50 gp worth of materials, you can create a number of doses of potent poison equal to your proficiency bonus. Once applied, the poison retains potency for 1 minute or until you hit with the weapon. When a weapon coated in this poison deals damage to a creature, that creature must succeed on a DC 14 Constitution saving throw or take 2d8 poison damage and become poisoned until the end of your next turn. Alternatively, you may choose a different poison to use, using different materials (and costs).

```
name = 'Poisoner'
description = "***Feat: Poisoner.*** You can prepare and deliver deadly poisons."
def prereq(npc): return True
def apply(npc):
    npc.traits.append("***Poisoner.*** When you make a damage roll, you ignore resistance to poison damage.")
    npc.bonusactions.append("***Poison Weapon.*** You coat a weapon in poison.")
    npc.proficiencies.append("Poisoner's kit")
    npc.defer(lambda npc: npc.traits.append(f"***Concoct Poison.*** With one hour of work using a poisoner's kit and expending 50 gp worth of materials, you can create {npc.proficiencybonus()} doses of potent poison. Once applied, the poison retains potency for 1 minute or until you hit with the weapon. When a weapon coated in this poison deals damage to a creature, that creature must succeed on a DC 14 Constitution saving throw or take 2d8 poison damage and become poisoned until the end of your next turn. Alternatively, you may choose a different poison to use, using different materials (and costs).") )
```
