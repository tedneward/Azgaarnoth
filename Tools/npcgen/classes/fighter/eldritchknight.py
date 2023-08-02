name = "Eldritch Knight"

def level3(npc):
    npc.description.append("**Fighter Martial Archetype: Eldritch Knight.** The archetypal Eldritch Knight combines the martial mastery common to all fighters with a careful study of magic. Eldritch Knights use magical techniques similar to those practiced by wizards. They focus their study on two of the eight schools of magic: abjuration and evocation. Abjuration spells grant an Eldritch Knight additional protection in battle, and evocation spells deal damage to many foes at once, extending the fighter's reach in combat. These knights learn a comparatively small number of spells, committing them to memory instead of keeping them in a spellbook.")

    npc.features.append("**Weapon Bond.** You can conduct a ritual that creates a magical bond between yourself and one weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. The weapon must be within your reach throughout the ritual, at the conclusion of which you touch the weapon and forge the bond. Once you have bonded a weapon to yourself, you can't be disarmed of that weapon unless you are incapacitated. If it is on the same plane of existence, you can summon that weapon as a bonus action on your turn, causing it to teleport instantly to your hand. You can have up to two bonded weapons, but can summon only one at a time with your bonus action. If you attempt to bond with a third weapon, you must break the bond with one of the other two.")

    npc.cantripsknown.append("(placeholder)")
    npc.cantripsknown.append("(placeholder)")

    npc.spellcastingattribute = "INT"
    npc.maxspellsknown = 3
    npc.spellslots = { 1:2 }

def level4(npc):
    npc.maxspellsknown = 4
    npc.spellslots = { 1:3 }

def level7(npc):
    npc.actions.append("**War Magic.** When you use your action to cast a cantrip, you can make one weapon attack as a bonus action.")
    npc.maxspellsknown = 5
    npc.spellslots = { 1:4, 2:2 }

def level8(npc):
    npc.maxspellsknown = 6

def level10(npc):
    npc.cantripsknown.append("(placeholder)")
    npc.maxspellsknown = 7
    npc.spellslots = { 1:4, 2:3 }

def level11(npc):
    npc.maxspellsknown = 8

def level13(npc):
    npc.maxspellsknown = 9
    npc.spellslots = { 1:4, 2:3, 3:2 }

def level14(npc):
    npc.maxspellsknown = 10

def level16(npc):
    npc.maxspellsknown = 11
    npc.spellslots = { 1:4, 2:3, 3:3 }

def level19(npc):
    npc.maxspellsknown = 12
    npc.spellslots = { 1:4, 2:3, 3:3, 4:1 }

def level20(npc):
    npc.maxspellsknown = 13
