name = "Burglar"

def level3(npc):
    npc.description.append("**Roguish Archetype: Burglar.** Most burglars are much more than robbers in the night. They have their sights on much more than the baubles and trinkets that they would get out of a neighbor's safe, or even than the treasures they would find in a noble's vault. Burglars aspire for hoards of legendary proportion: ancient tombs containing kingly treasure, the lost riches of a dwarven city, or even a dragon's hoard. The challenge is every bit as rewarding as the loot, and many a burglar has gotten caught only because they chose one challenge too far, not because they needed the money, but because they wanted to astound with their skill.")

    if "darkvision" in npc.senses:
        # Find the Darkvision trait and extend it
        for feat in npc.features:
            if feat[0:len("**Darkvision.**")] == "**Darkvision.**":
                replace("**Darkvision.**", npc.features, feat.replace('60', '90'))
            if feat[0:len("**Superior Darkvision.**")] == "**Superior Darkvision.**":
                replace("**Superior Darkvision.**", npc.features, feat.replace('120', '150'))
    else:
        npc.senses.append("darkvision")
        npc.features.append(commonfeatures['darkvision30'])

    npc.actions.append("**Detect Treasure.** You can use an action to detect the location of Medium or smaller objects that are worth 100 gp or more, out to a range of 30 feet, for the next 10 minutes. This ability can penetrate most barriers, but is blocked by 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt. When you use this ability, you cannot do so again until you finish a long rest.")

def level9(npc):
    npc.features.append("**Deep Pockets.** During a long rest, you can enchant one container on your person, usually a pocket or backpack that becomes the equivalent of a bag of holding for you. You can enchant a different container over the course of a long rest. If you do so, the previous container loses its magic. If the container is filled above its capacity, if there are still items in the container when you enchant a different one, or if the container is targeted by a spell such as dispel magic or antimagic field, all of its contents spill out around you, landing in an empty adjacent space.")

def level13(npc):
    npc.features.append("**Trap Sense: Investigation.** If you succeed on an Investigation ability check to determine how a trap works by 5 or more, you and your allies can safely bypass the trap without triggering or disarming it.")
    npc.featurs.append("**Trap Sense: Evasion.** You have advantage on saving throws against traps and their effects.")
    npc.features.append("**Trap Sense: Dodge.** Traps make attack rolls against you with disadvantage.")

def level17(npc):
    replace("**Deep Pockets.**", npc.features, "**Deep Pockets.** During a long rest, you can enchant one container on your person, usually a pocket or backpack that becomes the equivalent of a bag of holding for you. You can enchant a different container over the course of a long rest. You can have two containers enchanted simutaneously; if you enchant a third, the first container loses its magic. If the container is filled above its capacity, if there are still items in the container when you enchant a different one, or if the container is targeted by a spell such as dispel magic or antimagic field, all of its contents spill out around you, landing in an empty adjacent space.")

    npc.features.append("**Disappear.** You have gained the ability to make yourself disappear from sight. You can cast " + spelllinkify('greater invisibility') + " once without expending a spell slot. Once you cast the spell in this way, you cannot do so again until you finish a long rest.")
