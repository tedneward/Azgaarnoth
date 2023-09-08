# Martial Archetype: Duelist
The duelist lives for the thrill of combat, but most of all, they thrive in seeking out and challenging the most skilled foe on any battlefield. Once a duelist engages with their latest nemesis, everything else fades into oblivion, forgotten in the moment. The dance of the duel offers them the best way to learn new tricks, hone combat skills, and--most importantly--solidify their reputation as the superior swordsman.

Dueling grew out of the Dueling Colleges that have flourished across Azgaarnoth, and although the classic duelist is the rapier-and-dagger two-handed swashbuckler, many duelers are finding value in dueling using other weapons, including warhammers (particularly among dwarven duelists) or even weapons like the quarterstaff.

```
name = 'Duelist'
description = "***Martial Archetype: Duelist.*** The duelist lives for the thrill of combat, but most of all, they thrive in seeking out and challenging the most skilled foe on any battlefield. Once a duelist engages with their latest nemesis, everything else fades into oblivion, forgotten in the moment. The dance of the duel offers them the best way to learn new tricks, hone combat skills, and—most importantly--solidify their reputation as the superior swordsman."
```

## Duelist's Defense
*3rd-level Duelist feature*

As a reaction, you add your Intelligence bonus to your AC against a single attack.

```
def level3(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Duelist's Defense.*** You add +{npc.INTbonus()} to your AC against a single attack."))
```

## Duelist's Challenge
*7th-level Duelist feature*

At 7th level, you may issue a challenge against a single target within 30 feet that you can see. That target must make a Charisma save (DC = 8 + your proficiency bonus + your Charisma modifier) or be forced to engage you in combat. You gain advantage on melee attacks against that target, but all other foes (except your challenge target) gain advantage on attacks against you. If your target does not engage you (by making their save) or exits combat, you may drop your challenge without using an action. You may not change your challenge. You regain this ability after finishing a short rest.

```
def level7(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Duelist's Challenge (Recharges on short rest).*** You may issue a challenge against a single target within 30 feet that you can see. That target must make a Charisma save (DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}) or be forced to engage you in combat. You gain advantage on melee attacks against that target, but all other foes (except your challenge target) gain advantage on attacks against you. If your target does not engage you (by making their save) or exits combat, you may drop your challenge without using an action. You may not change your challenge."))
```

## Riposte
*10th-level Duelist feature*

When you use your Duelist's Defense ability and an opponent misses, you may make an immediate attack against your attacker as part of your reaction.

```
def level10(npc):
    npc.reactions.append("***Riposte.*** When you use your Duelist’s Defense ability and an opponent misses, you may make an immediate attack against your attacker as part of your reaction.")
```

## Opportune Strike
*15th-level Duelist feature*

You learn how to identify and exploit flaws in your enemies' defenses. You gain advantage on opportunity attack rolls and gain a bonus to damage on opportunity attacks equal to your Intelligence modifier.

```
def level15(npc):
    npc.traits.append("***Opportune Strike.*** You have advantage on opportunity attack rolls and gain a bonus to damage on opportunity attacks equal to your Intelligence modifier.")
```

## Perfect Strikes
*18th-level Duelist feature*

You have become a master swordsman. You score critical hits on 19 and 20. In addition, whenever you deal a critical hit, add +1d6 to the base damage. This extra damage is doubled on the critical hit. 

```
def level18(npc):
    npc.traits.append("***Perfect Strikes.*** You score critical hits on 19 and 20. In addition, whenever you deal a critical hit, add +1d6 to the base damage. This extra damage is doubled on the critical hit.")
```
