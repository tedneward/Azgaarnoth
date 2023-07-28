name = "Duelist"

def level3(npc):
    npc.description.append("**Martial Archetype: Duelist.** The duelist lives for the thrill of combat, but most of all, they thrive in seeking out and challenging the most skilled foe on any battlefield. Once a duelist engages with their latest nemesis, everything else fades into oblivion, forgotten in the moment. The dance of the duel offers them the best way to learn new tricks, hone combat skills, and—most importantly—solidify their reputation as the superior swordsman.")

    npc.reactions.append("**Duelist's Defense.** You add your Intelligence bonus to your AC against a single attack.")

def level7(npc):
    npc.features.append("**Duelist's Challenge.** You may issue a challenge against a single target within 30 feet that you can see. That target must make a Charisma save (DC = 8 + your proficiency bonus + your Charisma modifier) or be forced to engage you in combat. You gain advantage on melee attacks against that target, but all other foes (except your challenge target) gain advantage on attacks against you. If your target does not engage you (by making their save) or exits combat, you may drop your challenge without using an action. You may not change your challenge. You regain this ability after finishing a short rest.")

def level10(npc):
    npc.reactions.append("**Riposte.** When you use your Duelist’s Defense ability and an opponent misses, you may make an immediate attack against your attacker as part of your reaction.")

def level15(npc):
    npc.features.append("**Opportune Strike.** You have advantage on opportunity attack rolls and gain a bonus to damage on opportunity attacks equal to your Intelligence modifier.")

def level18(npc):
    npc.features.append("**Perfect Strikes.** You score critical hits on 19 and 20. In addition, whenever you deal a critical hit, add +1d6 to the base damage. This extra damage is doubled on the critical hit.")
