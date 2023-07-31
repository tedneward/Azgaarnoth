name = "Divine Agent"

def level3(npc):
    npc.description.append("**Roguish Archetype: Divine Agent.** In secrecy and shadows, divine agents work to further the agendas of the gods. Although divine agents dedicate their service to a deity in a similar way to clerics, they are generally above many of the normal rules and conventions of the church. Usually, they answer only to their deity and use divine magic and blessings to augment their roguish skills.")

    npc.cantripsknown.append(spelllinkify('guidance'))
    npc.cantripsknown.append(spelllinkify('(placeholder)'))
    npc.cantripsknown.append(spelllinkify('(placeholder)'))

    npc.spellcastingattribute = "WIS"
    npc.maxspellsknown = 3
    npc.spellslots = { 1:2 }

    domains = discover('classes/cleric')
    domainpair = choose("Choose a Divine Domain:", domains)
    npc.domain = domainpair[1]
    levelinvoke(npc.domain, 1, npc)


def level4(npc):
    npc.maxspellsknown = 4
    npc.spellslots = { 1:3 }

def level7(npc):
    npc.maxspellsknown = 5
    npc.spellslots = { 1:4, 2:2 }

def level8(npc):
    npc.maxspellsknown = 6

def level9(npc):
    npc.features.append(commonfeatures('lucky'))

def level10(npc):
    npc.cantripsknown.append(spelllinkify('(placeholder)'))
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
