# Fallen Aasimar
An aasimar who was touched by dark powers as a youth or who turns to evil in early adulthood can become one of the fallen -- a group of aasimar whose inner light has been replaced by shadow.

* **Ability Score Increase**. Your Strength score increases by 1.

* **Necrotic Shroud**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn.

  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target when you deal damage to it with an attack or a spell. The extra necrotic damage equals your level.

  Once you use this trait, you can't use it again until you finish a long rest.

```
name = 'Fallen'

def level0(npc): 
    npc.description.append("***Fallen Aasimar.*** ...")

    npc.STR += 1

def level3(npc): 
    npc.actions.append("***Necrotic Shroud (Recharges after long rest).*** You can unleash the divine energy within yourself, causing your eyes to turn into pools of darkness and two skeletal, ghostly, flightless wings to sprout from your back. The instant you transform, other creatures within 10 feet of you that can see you must each succeed on a Charisma saving throw (DC 8 + your proficiency bonus + your Charisma modifier) or become frightened of you until the end of your next turn. Your transformation lasts for 1 minute or until you end it as a bonus action. During it, once on each of your turns, you can deal extra necrotic damage to one target (equal to your level) when you deal damage to it with an attack or a spell.")
```
