# Protector Aasimar
Protector aasimar are charged by the powers of good to guard the weak, to strike at evil wherever it arises, and to stand vigilant against the darkness. From a young age, a protector aasimar receives advice and directives that urge to stand against evil.

* **Ability Score Increase**. Your Wisdom score increases by 1.

* **Radiant Soul**. Starting at 3rd level, you can use your action to unleash the divine energy within yourself, causing your eyes to glimmer and two luminous, incorporeal wings to sprout from your back.
  
  Your transformation lasts for 1 minute or until you end it as a bonus action. During it, you have a flying speed of 30 feet, and once on each of your turns, you can deal extra radiant damage to one target when you deal damage to it with an attack or a spell. The extra radiant damage equals your level.
  
  Once you use this trait, you can't use it again until you finish a long rest.

```
name = 'Protector'

def level0(npc): 
    npc.WIS += 1

def level3(npc): 
    npc.actions.append("***Radiant Soul (Recharges after long rest).*** The aasimar can unleash the divine energy within itself, causing its eyes to glimmer and two luminous, incorporeal wings to sprout from its back. This transformation lasts for 1 minute or until the aasimar ends it as a bonus action. During it, the aasimar has a flying speed of 30 feet, and once on each of its turns, you can deal extra radiant damage (equal to its level) to one target when it deals damage to it with an attack or a spell.")
```
