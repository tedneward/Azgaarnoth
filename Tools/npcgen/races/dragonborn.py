"""
# Dragonborn
While the origins of the [elves](Firstborn.md) are thought to be wrapped up in the [Eldar](Eldar.md), and the [dwarves](Firstborn.md)/[gnomes](Firstborn.md)/[halflings](Firstborn.md) in the Exodus, the history of the dragonborn (and their distant kin, tieflings and aasimar) is quite clear: dragonborn are a Created race, given life from dragons' eggs, and from there to flourish on their own. It is thought that even today, dragons periodically place a "firstborn dragonborn" (that is, Created from the egg) as an adoption with a family or other group to refresh the genetics of the race, though if true, it is not discussed among dragonborn. (Whether this is due to ignorance of their parentage or a deeper desire to preserve a secret is not known outside of the firstborn.)

Platinum dragonborn (from The Book of Dragons) are found within Azgaarnoth, though extremely rare. Any platinum dragonborn are inevitably deeply linked to the [Draconic Order](/Organizations/DraconicOrder/DraconicOrder.md).
 
Dragonborn, though not nearly as numerous as humans, are found throughout Azgaarnoth, in almost any climate or environment.

* **Ability Score increase**. Your Strength score increases by 2, and your Charisma score increases by 1.

* **Age**. Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80.

* **Alignment**. Dragonborn tend towards extremes, making a conscious choice for one side or the other between Good and Evil (represented by Bahamut and Tiamat, respectively). More side with Bahamut than Tiamat (whose non-dragon followers are mostly kobolds), but villainous dragonborn can be quite terrible indeed. Some rare few choose to devote themselves to lesser dragon deities, such as Chronepsis (Neutral), and fewer still choose to worship Io, the Ninefold Dragon, who is all alignments at once.

* **Size**. Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Languages**. You can read, speak, and write Common and Draconic.
"""
name = "Dragonborn"

def apply_race(npc):
    npc.size = 'Medium'
    npc.speed = '30 ft'

    # Ability Score Increase
    npc.STR += 2
    npc.CHA += 1

    npc.languages.append('Common')
    npc.languages.append('Draconic')

    npc.description.append("**Dragonborn.** While the origins of the [elves](Firstborn.md) are thought to be wrapped up in the [Eldar](Eldar.md), and the [dwarves](Firstborn.md)/[gnomes](Firstborn.md)/[halflings](Firstborn.md) in the Exodus, the history of the dragonborn (and their distant kin, tieflings and aasimar) is quite clear: dragonborn are a Created race, given life from dragons' eggs, and from there to flourish on their own. It is thought that even today, dragons periodically place a \"firstborn dragonborn\" (that is, Created from the egg) as an adoption with a family or other group to refresh the genetics of the race, though if true, it is not discussed among dragonborn. (Whether this is due to ignorance of their parentage or a deeper desire to preserve a secret is not known outside of the firstborn. Dragonborn, though not nearly as numerous as humans, are found throughout Azgaarnoth, in almost any climate or environment.")

# -------------
# Subraces
#

# Subraces are the draconic ancestry entries
subraces = [
    'Black',
    'Blue',
    'Brown',
    'Gray',
    'Green',
    'Red',
    'White',
    'Bronze',
    'Brass',
    'Copper',
    'Gold',
    'Silver',
    'Steel'
]
colormap = {
    'Black' : ('acid', "5' by 30' line", "DEX"),
    'Blue' : ('lightning', "5' by 30' line", "DEX"),
    'Brown' : ('force (sand)', "15' cone", "DEX"),
    'Gray' : ('poison', "5' by 30' line", "CON"),
    'Green' : ('poison', "15' cone", "DEX"),
    'Red' : ('fire', "15' cone", "DEX"),
    'White' : ('cold', "15' cone", "CON"),
    'Bronze' : ('lightning', "5' by 30' line", "DEX"),
    'Brass' : ('fire', "5' by 30' line", "DEX"),
    'Copper' : ('acid', "5' by 30' line", "DEX"),
    'Gold' : ('fire', "15' cone", "DEX"),
    'Silver' : ('cold', "15' cone`", "CON"),
    'Steel' : ('lightning', "5' by 30' line", "DEX")
}
def apply_subrace(which, npc):
    npc.features.append("**Draconic Ancestry (" + which + ").** You are distantly related to " + which + " dragons.")
    npc.actions.append("**Breath Weapon.** You can use your action to exhale " + colormap[which][0] + " in a " + colormap[which][1] + ". When you use your breath weapon, all creatures in the area must make a " + colormap[which][2] + " saving throw against DC 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.")
    npc.resistances.append(colormap[which][0])

def level6(npc):
    # Breath Weapon advances to 3d6
    replace("**Breath Weapon.**", npc.actions, "**Breath Weapon.** You can use your action to exhale " + 
            colormap[npc.subrace][0] + " in a " + colormap[npc.subrace][1] + 
            ". When you use your breath weapon, all creatures in the area must make a " + 
            colormap[npc.subrace][2] + " saving throw against DC 8 + your Constitution modifier + your proficiency bonus. " + 
            "A creature takes 3d6 damage on a failed save, and half as much damage on a successful one. " + 
            "You may use your breath weapon a number of times equal to your Constitution modifier. " + 
            "You regain expended uses on a long rest.")

def level11(npc):
    # Breath Weapon advances to 4d6
    replace("**Breath Weapon.**", npc.actions, "**Breath Weapon.** You can use your action to exhale " + 
            colormap[npc.subrace][0] + " in a " + colormap[npc.subrace][1] + 
            ". When you use your breath weapon, all creatures in the area must make a " + 
            colormap[npc.subrace][2] + " saving throw against DC 8 + your Constitution modifier + your proficiency bonus. " + 
            "A creature takes 4d6 damage on a failed save, and half as much damage on a successful one. " + 
            "You may use your breath weapon a number of times equal to your Constitution modifier. " + 
            "You regain expended uses on a long rest.")

def level16(npc):
    # Breath Weapon advances to 5d6
    replace("**Breath Weapon.**", npc.actions, "**Breath Weapon.** You can use your action to exhale " + 
            colormap[npc.subrace][0] + " in a " + colormap[npc.subrace][1] + 
            ". When you use your breath weapon, all creatures in the area must make a " + 
            colormap[npc.subrace][2] + " saving throw against DC 8 + your Constitution modifier + your proficiency bonus. " + 
            "A creature takes 5d6 damage on a failed save, and half as much damage on a successful one. " + 
            "You may use your breath weapon a number of times equal to your Constitution modifier. " + 
            "You regain expended uses on a long rest.")
