name = 'Rogue'

def everylevel(npc):
    npc.classes.append(name)
    npc.hits('d8')

def level1(npc):
    npc.description.append("Rogues rely on skill, stealth, and their foes' vulnerabilities to get the upper hand in any situation. They have a knack for finding the solution to just about any problem, demonstrating a resourcefulness and versatility that is the cornerstone of any successful adventuring party.")

    everylevel(npc)

    npc.savingthrows.append("DEX")
    npc.savingthrows.append("INT")

    npc.proficiencies.append("Light armor")
    npc.proficiencies.append("Simple weapons")
    npc.proficiencies.append("Hand crossbows")
    npc.proficiencies.append("Longswords")
    npc.proficiencies.append("Shortswords")
    npc.proficiencies.append("Rapiers")
    npc.proficiencies.append("Thieves tools")

    skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'Deception', 'History', 
              'Insight', 'Intimidation', 'Investigation', 'Perception', 'Performance', 
              'Persuasion', 'Sleight of Hand', 'Stealth', 'Survival']
    npc.skills.append(choose("Choose:", skills))
    npc.skills.append(choose("Choose:", skills))
    npc.skills.append(choose("Choose:", skills))
    npc.skills.append(choose("Choose:", skills))

    npc.features.append("**Sneak Attack.** Once per turn, you can deal an extra 1d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    npc.features.append("**Thieves' Cant.** During your rogue training you learned thieves' cant, a secret mix of dialect, jargon, and code that allows you to hide messages in seemingly normal conversation. Only another creature that knows thieves' cant understands such messages. It takes four times longer to convey such a message than it does to speak the same idea plainly. In addition, you understand a set of secret signs and symbols used to convey short, simple messages, such as whether an area is dangerous or the territory of a thieves' guild, whether loot is nearby, or whether the people in an area are easy marks or will provide a safe house for thieves on the run.")

def level2(npc):
    everylevel(npc)

    npc.features.append("**Expertise.** Choose two of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.")

    npc.bonusactions.append("**Cunning Action.** You can take a bonus action on each of your turns in combat. This action can be used only to take the Dash, Disengage, or Hide action. You may also your Cunning Action to carefully aim your next attack. As a bonus action, you give yourself advantage on your next attack roll on the current turn. You can use this bonus action only if you haven't moved during this turn, and after you use the bonus action, your speed is 0 until the end of the current turn.")

def level3(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 2d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    # Choose subclass
    subclasses = discover('classes/rogue')
    subclasspair = choose("Choose a Roguish Archetype:", subclasses)
    npc.subclasses[name] = subclasspair[1]
    levelinvoke(npc.subclasses[name], 3, npc)

def level4(npc):
    everylevel(npc)

    abilityscoreimprovement(npc)

def level5(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 3d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    npc.reactions.append("**Uncanny Dodge.** When an attacker that you can see hits you with an attack, you can use your reaction to halve the attack's damage against you.")

def level6(npc):
    everylevel(npc)

    npc.features.append("**Expertise.** Choose two more of your skill proficiencies, or one of your skill proficiencies and your proficiency with thieves' tools. Your proficiency bonus is doubled for any ability check you make that uses either of the chosen proficiencies.")

def level7(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 4d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    npc.actions.append("**Evasion.** When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail.")

def level8(npc):
    everylevel(npc)

    abilityscoreimprovement(npc)

def level9(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 5d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

def level10(npc):
    everylevel(npc)

def level11(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 6d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    npc.features.append("**Reliable Talent.** Whenever you make an ability check that lets you add your proficiency bonus, you can treat a d20 roll of 9 or lower as a 10.")

def level12(npc):
    everylevel(npc)

    abilityscoreimprovement(npc)

def level13(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 7d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

def level14(npc):
    everylevel(npc)

    npc.senses.append("Blindsense 10ft")

def level15(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 8d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    npc.savingthrows.append("WIS")

def level16(npc):
    everylevel(npc)

    abilityscoreimprovement(npc)

def level17(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 9d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

def level18(npc):
    everylevel(npc)

    npc.features.append("**Elusive.** No attack roll has advantage against you while you aren't incapacitated.")

def level19(npc):
    everylevel(npc)

    replace("**Sneak Attack.**", npc.features, "**Sneak Attack.** Once per turn, you can deal an extra 10d6 damage to one creature you hit with an attack if you have advantage on the attack roll. The attack must use a finesse or a ranged weapon. You don't need advantage on the attack roll if another enemy of the target is within 5 feet of it, that enemy isn't incapacitated, and you don't have disadvantage on the attack roll.")

    abilityscoreimprovement(npc)

def level20(npc):
    everylevel(npc)

    npc.features.append("**Stroke of Luck.** If your attack misses a target within range, you can turn the miss into a hit. Alternatively, if you fail an ability check, you can treat the d20 roll as a 20. Once you use this feature, you can't use it again until you finish a short or long rest.")
