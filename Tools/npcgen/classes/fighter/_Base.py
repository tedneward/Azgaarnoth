# Fighter
name = 'Fighter'

def everylevel(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level1(npc):
    npc.classes.append(name)
    npc.description.append("Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.")
    npc.hitdice["d10"] += 1

    npc.savingthrows.append("STR")
    npc.savingthrows.append("CON")

    npc.proficiencies.append("All armor, shields")
    npc.proficiencies.append("Simple weapons")
    npc.proficiencies.append("Martial weapons")

    skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    npc.skills.append(choose("Choose:", skills))
    npc.skills.append(choose("Choose:", skills))

    npc.bonusactions.append("**Second Wind.** On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level.\nOnce you use this feature, you must finish a short or long rest before you can use it again.")

    #Fighting Style
    styles = {
        'Archery': "You gain a +2 bonus to attack rolls you make with ranged weapons.",
        'Blind Fighting': "You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.",
        'Close Quarters Shooter': "When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.",
        'Defense': "While you are wearing armor, you gain a +1 bonus to AC.",
        'Dueling': "When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.",
        'Great Weapon Fighting': "When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.",
        'Interception': "When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by ldlO + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction.",
        'Mariner': "As long as you not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class.",
        'Protection': "When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.",
        'Superior Technique': "You learn one maneuver of your choice from among those available to the [Battle Master](BattleMaster.md) archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice). \nYou gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it.  You regain your expended superiority dice when you finish a short or long rest.",
        'Thrown Weapon Fighting': "You can draw a weapon that has the thrown property as part of the attack you make with the weapon.\nIn addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll.",
        'Tunnel Fighter': "As a bonus action, you can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.",
        'Two-Weapon Fighting': "When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.",
        'Unarmed Fighting': "Your unarmed strikes can deal bludgeoning damage equal to ld6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.\nAt the start of each of your turns, you can deal ld4 bludgeoning damage to one creature grappled by you."
    }
    stylekey = choose("Choose a Fighting Style:", list(styles.keys()))
    style = styles[stylekey]
    npc.features.append("**" + stylekey + ".** " + style)

def level2(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    npc.features.append("**Action Surge.** On your turn, you can take one additional action on top of your regular action and a possible bonus action.\nOnce you use this feature, you must finish a short or long rest before you can use it again.")

def level3(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose subclass
    subclasses = subclassload('classes/fighter')
    subclasskey = choose("Choose a Martial Archetype:", list(subclasses.keys()))
    subclass = subclasses[subclasskey]
    levelinvoke(subclass, 3, npc)

def level4(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level5(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    npc.actions.append("**Multiattack.** You can attack twice whenever you take the Attack action on your turn.")

def level6(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level7(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level8(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level9(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level10(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level11(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    replace("**Multiattack.**", npc.actions, "**Multiattack.** You can attack three times whenever you take the Attack action on your turn.")

def level12(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level13(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level14(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level15(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level16(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level17(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    npc.features.append("**Action Surge.** On your turn, you can take one additional action on top of your regular action and a possible bonus action.\nOnce you use this feature twice (not in the same turn), you must finish a short or long rest before you can use it again.")

def level18(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1

def level19(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    # Choose ability score improvement (or Feat)

def level20(npc):
    npc.classes.append(name)
    npc.hitdice["d10"] += 1
    replace("**Multiattack.**", npc.actions, "**Multiattack.** You can attack four times whenever you take the Attack action on your turn.")
