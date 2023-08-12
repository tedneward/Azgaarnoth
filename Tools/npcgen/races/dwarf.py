"""
* **Ability Score Increase**. Your Constitution score increases by 2.

* **Age**. Dwarves mature at the same rate as humans, but they're considered young until they reach the age of 50. On average, they live about 350 years.

* **Alignment**. Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves to share in the benefits of a just order.

* **Size**. Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 25 feet. Your speed is not reduced by wearing heavy armor.

* **Darkvision**. Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Dwarven Resilience**. You have advantage on saving throws against poison, and you have resistance against poison damage.

* **Dwarven Combat Training**. You have proficiency with the battleaxe, handaxe, light hammer, and warhammer.

* **Tool Proficiency**. You gain proficiency with the artisan's tools of your choice: smith's tools, brewer's supplies, or mason's tools.

* **Stonecunning**. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.

* **Languages**. You can speak, read, and write Common and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dwarf might speak.
"""
name = 'Dwarf'
def apply_race(npc):
    npc.size = 'Medium'
    npc.speed = '25 ft'

    # Ability Score Increase
    npc.CON += 2

    npc.features.append(commonfeatures['darkvision'])
    npc.senses.append("darkvision")
    
    npc.resistances.append('poison')
    npc.features.append("**Dwarven Resilience**. You have advantage on saving throws against poison.")

    npc.proficiencies.append("Battleaxe")
    npc.proficiencies.append("Handaxe")
    npc.proficiencies.append("Light hammer")
    npc.proficiencies.append("Warhammer")

    npc.features.append("**Stonecunning**. Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.")

    npc.languages.append("Common")
    npc.languages.append("Dwarvish")

    npc.description.append("**Race: Dwarf.** Dwarves ...")

# -------------
# Subraces
#

def hill(npc):
    """
### Hill dwarf and Mountain dwarf
These are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the mountains as part of their guild/clan, and mountain dwarves are often found in hills for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them.

#### Hill dwarf
* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Dwarven Toughness**. Your hit point maximum increases by 1, and it increases by 1 every time you gain a level.
    """
    npc.WIS += 1
    npc.hitpoints += 1

    npc.description.append("These are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the hills as part of their guild/clan, but it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them and mountain dwarves.")

def mountain(npc):
    """
### Hill dwarf and Mountain dwarf
These are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--hill dwarves often work in the mountains as part of their guild/clan, and mountain dwarves are often found in hills for similar reasons. In fact, it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them.

#### Mountain dwarf
* **Ability Score Increase**. Your Strength score increases by 2.

* **Dwarven Armor Training**. You have proficiency with light and medium armor.
    """
    npc.STR += 2
    npc.proficiencies.append("Light armor")
    npc.proficiencies.append("Medium armor")

    npc.description.append("These are essentially small genetic differences within the dwarven bloodline, but at this point in Azgaarnoth's history they are essentially meaningless as cultural differentiators--mountain dwarves are often found in mountains as part of their guild/clan, but it's more common to see them in cities than in hills or mountains. Most non-dwarves can't even tell the difference between them and hill dwarves.")

def dark(npc):
    """
### Dark dwarves (*duergar*) ("Underdark dwarf")
Rumors persist of clans of dwarves that never participated as part of the Exodus (or were left behind either accidentally or deliberately, depending on the rumor), and were forced into hard living and driven deeper into the depths to survive. The *duergar*'s legends claim that those clans were captured by the *illithid* (mind flayers) at the same time elves were captured (who later became the [Gith](Gith.md)). While most dwarves consider the "dark dwarves" to be myth, most scholars agree that the *duergar* are real, whatever their history. Rumors of *duergar* generally also tie into the rumors of tunnels that connect the western and eastern reaches of the Daw mountain range underneath the Ravensound, as such tunnels would provide adequate depth to hide them from the Hordes that precipitated the Exodus.

Most of the *duergar* encountered tend to be bitter and resentful, angry at the dwarves for their collective racial pain, with little to no remorse for the dwarves' own tragedies or history. *Duergar* are often paranoid and shun outsiders, though many that have come into contact with surface-dwellers have slowly adjusted their feelings and expectations accordingly. *Duergar* society is clan-based, much like the dwarves' was prior to the Exodus, and the bonds of clan often supersede all other concerns and obligations, even unto death.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Superior Darkvision**. You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

* **Duergar Resilience**. You have advantage on saving throws against illusions and against being charmed or paralyzed.

* **Duergar Magic**. When you reach 3rd level, you can cast the [enlarge/reduce](/Magic/Spells/enlarge-reduce.md) spell on yourself once with this trait, using only the spell's enlarge option. When you reach 5th level, you can cast the [invisibility](/Magic/Spells/invisibility.md) spell on yourself once with this trait. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest. Intelligence is your spellcasting ability for these spells.

* **Sunlight Sensitivity**. You have disadvantage on Attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.
    """
    npc.description.append("**Underdark Dwarf.** Rumors persist of clans of dwarves that never participated as part of the Exodus (or were left behind either accidentally or deliberately, depending on the rumor), and were forced into hard living and driven deeper into the depths to survive. The *duergar*'s legends claim that those clans were captured by the *illithid* (mind flayers) at the same time elves were captured (who later became the [Gith](Gith.md)). While most dwarves consider the \"dark dwarves\" to be myth, most scholars agree that the *duergar* are real, whatever their history. Rumors of *duergar* generally also tie into the rumors of tunnels that connect the western and eastern reaches of the Daw mountain range underneath the Ravensound, as such tunnels would provide adequate depth to hide them from the Hordes that precipitated the Exodus.\nMost of the *duergar* encountered tend to be bitter and resentful, angry at the dwarves for their collective racial pain, with little to no remorse for the dwarves' own tragedies or history. *Duergar* are often paranoid and shun outsiders, though many that have come into contact with surface-dwellers have slowly adjusted their feelings and expectations accordingly. *Duergar* society is clan-based, much like the dwarves' was prior to the Exodus, and the bonds of clan often supersede all other concerns and obligations, even unto death.")

    npc.STR += 1

    replace("**Darkvision.**", npc.features, commonfeatures['superiordarkvision'])

    npc.features.append("**Duergar Resilience**. You have advantage on saving throws against illusions and against being charmed or paralyzed.")

    npc.features.append(commonfeatures['sunlight-sensitivity'])

    npc.languages.append("Undercommon")

def derro(npc):
    """
Still other rumors tell of clans of non-Exodus dwarves that were then captured by [mind flayers](/Creatures/MindFlayer.md) and enslaved until they could either escape or were freed by the [Gith](Gith.md); according to the *duergar*, they were clans that refused to join the *duergar* in their initial battles for freedom, fearing the mind flayers' power, and suffered worse for it when the *duergar* were able to win free. Eventually the *derro* slipped away, but hideously changed for the experience.
    """
    npc.description.append("**Legacy of the mind flayers.** Rumors tell of clans of non-Exodus dwarves that were then captured by [mind flayers](/Creatures/MindFlayer.md) and enslaved until they could either escape or were freed by the [Gith](/Races/Gith.md); according to the *duergar*, these were clans that refused to join the *duergar* in their initial battles for freedom, fearing the mind flayers' power, and suffered worse for it when the *duergar* were able to win free. Eventually the *derro* slipped away, but hideously changed for the experience. Many went insane, while others incorporated the insanity into their culture.")

    npc.size = 'Small'
    npc.speed = '30 ft'

    npc.DEX += 2
    npc.WIS += 2

    replace("**Darkvision.**", npc.features, commonfeatures['superiordarkvision'])

    npc.languages.append("Undercommon")

    npc.features.append(commonfeatures['sunlight-sensitivity'])

    npc.features.append("**Eldritch Resilience.** You have advantage on Constitution saving throws against spells.")

    npc.features.append("**Psychic Barrier.** You have resistance to psychic damage, and you have advantage on ability checks and saving throws made against effects that inflict insanity, such as spells like *contact other plane* and *symbol*, and effects that cause short-term, long-term, or indefinite madness.")

    npc.features.append("**Studied Insight.** If you study a creature for at least 1 minute, you have advantage on any initiative checks in combat against that creature for the next hour.")
    npc.skills.append("Insight")

subracemap = {
    'Hill' : hill,
    'Mountain': mountain,
    'Dark': dark,
    'Derro': derro
}
subraces = list(subracemap.keys())

def apply_subrace(which, npc): 
    npc.subrace = which
    subracemap[which](npc)

def level2(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level3(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1
    elif npc.subrace == 'Dark':
        npc.features.append("**Duergar Magic.** You can cast the [enlarge/reduce](/Magic/Spells/enlarge-reduce.md) spell (only the spell's enlarge option) on yourself once with this trait, using INT as your spellcasting ability. You don't need material components, and you can't cast it while you're in direct sunlight, although sunlight has no effect on it once cast. You regain the ability to cast this spell with this trait when you finish a long rest.")

def level4(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level5(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1
    elif npc.subrace == 'Dark':
        replace("**Duergar Magic.**", npc.features, "**Duergar Magic**. You can cast [enlarge/reduce](/Magic/Spells/enlarge-reduce.md) (only the spell's enlarge option) or [invisibility](/Magic/Spells/invisibility.md) on yourself once with this trait, using INT as your spellcasting ability. You don't need material components for either spell, and you can't cast them while you're in direct sunlight, although sunlight has no effect on them once cast. You regain the ability to cast these spells with this trait when you finish a long rest.")

def level6(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level7(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level8(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level9(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level10(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level11(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level12(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level13(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level14(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level15(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level16(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level17(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level18(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level19(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1

def level20(npc): 
    if npc.subrace == 'Hill': npc.hitpoints += 1
