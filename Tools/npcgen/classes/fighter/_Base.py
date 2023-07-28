name = 'Fighter'

def everylevel(npc):
    npc.classes.append(name)
    npc.hits('d10')

def archery(npc):
    npc.features.append("**Fighting Style: Archery.** You gain a +2 bonus to attack rolls you make with ranged weapons.")
def blindfighting(npc):
    npc.senses.append('Blindsight, 10 ft')
    npc.features.append("**Fighting Style: Blindsight.** You have blindsight with a range of 10 feet. Within that range, you can effectively see anything that isn't behind total cover, even if you're blinded or in darkness. Moreover, you can see an invisible creature within that range, unless the creature successfully hides from you.")
def closequarters(npc):
    npc.features.append("**Fighting Style: Close Quarters Shooter.** When making a ranged attack while you are within 5 feet of a hostile creature, you do not have disadvantage on the attack roll. Your ranged attacks ignore half cover and three-quarters cover against targets within 30 feet of you. You have a +1 bonus to attack rolls on ranged attacks.")
def defense(npc):
    npc.features.append("**Fighting Style: Defense.** While you are wearing armor, you gain a +1 bonus to AC.")
def dueling(npc):
    npc.features.append("**Fighting Style: Dueling.** When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")
def greatweaponfighting(npc):
    npc.features.append("**Fighting Style: Great Weapon Fighting.** When you roll a 1 or 2 on a damage die for an attack you make with a melee weapon that you are wielding with two hands, you can reroll the die and must use the new roll, even if the new roll is a 1 or a 2. The weapon must have the two-handed or versatile property for you to gain this benefit.")
def interception(npc):
    npc.features.append("**Fighting Style: Interception.** When a creature you can see hits a target, other than you, within 5 feet of you with an attack, you can use your reaction to reduce the damage the target takes by ldlO + your proficiency bonus (to a minimum of 0 damage). You must be wielding a shield or a simple or martial weapon to use this reaction."),
def mariner(npc):
    npc.speed = npc.speed + "; swimming " + npc.speed + "; climbing " + npc.speed ;
    npc.features.append("**Fighting Style: Mariner.** As long as you not wearing heavy armor or using a shield, you have a swimming speed and a climbing speed equal to your normal speed, and you gain a +1 bonus to armor class."),
def protection(npc):
    npc.reactions.append("**Fighting Style: Protection.** When a creature you can see attacks a target other than you that is within 5 feet of you, you can use your reaction to impose disadvantage on the attack roll. You must be wielding a shield.")
def superiortechnique(npc):
    # TODO: Choose from battlemaster.py maneuvers[] list
    npc.features.append("**Fighting Style: Superior Technique.** You learn one maneuver of your choice from among those available to the [Battle Master](BattleMaster.md) archetype. If a maneuver you use requires your target to make a saving throw to resist the maneuver's effects, the saving throw DC equals 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice). \nYou gain one superiority die, which is a d6 (this die is added to any superiority dice you have from another source). This die is used to fuel your maneuvers. A superiority die is expended when you use it.  You regain your expended superiority dice when you finish a short or long rest.")
def thrownweapon(npc):
    npc.actions.append("**Fighting Style: Thrown Weapon Fighting.** You can draw a weapon that has the 'thrown' property as part of the attack you make with the weapon. In addition, when you hit with a ranged attack using a thrown weapon, you gain a +2 bonus to the damage roll." )
def tunnelfighter(npc):
    npc.bonusactions.append("**Fighting Style: Tunnel Fighter.** You can enter a defensive stance that lasts until the start of your next turn. While in your defensive stance, you can make opportunity attacks without using your reaction, and you can use your reaction to make a melee attack against a creature that moves more than 5 feet while within your reach.")
def twoweapon(npc):
    npc.actions.append("**Fighting Style: Two-Weapon Fighting.** When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.")
def unarmedfighting(npc):
    npc.actions.append("**Fighting Style: Unarmed Fighting.** Your unarmed strikes can deal bludgeoning damage equal to ld6 + your Strength modifier on a hit. If you aren't wielding any weapons or a shield when you make the attack roll, the d6 becomes a d8.\nAt the start of each of your turns, you can deal ld4 bludgeoning damage to one creature grappled by you.")
styles = {
    'Archery': archery,
    'Blind Fighting': blindfighting,
    'Close Quarters Shooter': closequarters,
    'Defense': defense,
    'Dueling': dueling,
    'Great Weapon Fighting': greatweaponfighting, 
    'Interception': interception,
    'Mariner': mariner,
    'Protection': protection,
    'Superior Technique': superiortechnique,
    'Thrown Weapon Fighting': thrownweapon,
    'Tunnel Fighter': tunnelfighter,
    'Two-Weapon Fighting': twoweapon,
    'Unarmed Fighting': unarmedfighting
}

def level1(npc):
    npc.description.append("Fighters share an unparalleled mastery with weapons and armor, and a thorough knowledge of the skills of combat. They are well acquainted with death, both meting it out and staring it defiantly in the face.")

    everylevel(npc)

    npc.savingthrows.append("STR")
    npc.savingthrows.append("CON")

    npc.proficiencies.append("All armor, shields")
    npc.proficiencies.append("Simple weapons")
    npc.proficiencies.append("Martial weapons")

    skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
    npc.skills.append(choose("Choose:", skills))
    npc.skills.append(choose("Choose:", skills))

    npc.bonusactions.append("**Second Wind.** On your turn, you can use a bonus action to regain hit points equal to 1d10 + your fighter level. Once you use this feature, you must finish a short or long rest before you can use it again.")

    # Fighting Style
    style = choose("Choose a Fighting Style:", styles)
    npc.fightingstyle = style[0]
    (style[1])(npc)

def level2(npc):
    everylevel(npc)
    npc.features.append("**Action Surge.** On your turn, you can take one additional action on top of your regular action and a possible bonus action. Once you use this feature, you must finish a short or long rest before you can use it again.")

def level3(npc):
    everylevel(npc)

    # Choose subclass
    subclasses = discover('classes/fighter')
    subclasspair = choose("Choose a Martial Archetype:", subclasses)
    npc.subclasses['Fighter'] = subclasspair[1]
    levelinvoke(npc.subclasses['Fighter'], 3, npc)

def level4(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level5(npc):
    everylevel(npc)

    npc.actions.append("**Multiattack.** You can attack twice whenever you take the Attack action on your turn.")

def level6(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level7(npc):
    everylevel(npc)

    levelinvoke(npc.subclasses['Fighter'], 7, npc)

def level8(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level9(npc):
    everylevel(npc)

    npc.features.append("**Indomitable.** You can reroll a saving throw that you fail. If you do so, you must use the new roll, and you can't use this feature again until you finish a long rest.")

def level10(npc):
    everylevel(npc)

    levelinvoke(npc.subclasses['Fighter'], 10, npc)

def level11(npc):
    everylevel(npc)
    replace("**Multiattack.**", npc.actions, "**Multiattack.** You can attack three times whenever you take the Attack action on your turn.")

def level12(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level13(npc):
    everylevel(npc)

    replace("**Indomitable.**", npc.features, "**Indomitable.** You can reroll a saving throw that you fail. If you do so, you must use the new roll. You can use this feature twice between long rests.")


def level14(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level15(npc):
    everylevel(npc)

    levelinvoke(npc.subclasses['Fighter'], 15, npc)

def level16(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level17(npc):
    everylevel(npc)

    npc.features.append("**Action Surge.** On your turn, you can take one additional action on top of your regular action and a possible bonus action.\nOnce you use this feature twice (not in the same turn), you must finish a short or long rest before you can use it again.")
    replace("**Indomitable.**", npc.features, "**Indomitable.** You can reroll a saving throw that you fail. If you do so, you must use the new roll. You can use this feature three times between long rests.")

def level18(npc):
    everylevel(npc)

    levelinvoke(npc.subclasses['Fighter'], 18, npc)

def level19(npc):
    everylevel(npc)

    # Choose ability score improvement (or Feat)
    abilityscoreimprovement(npc)

def level20(npc):
    everylevel(npc)

    replace("**Multiattack.**", npc.actions, "**Multiattack.** You can attack four times whenever you take the Attack action on your turn.")
