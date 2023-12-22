# Mark of Handling
The Mark of Handling gives its bearer a primal connection to beasts and the natural world, granting the power to calm and coax. This extends beyond purely natural animals; the mark allows its bearer to guide a hippogriff as easily as a horse.

### Traits
The Mark of Handling only manifests on humans. If your character has the Mark of Handing, these traits replace the human’s Ability Score Increase trait given in the Player’s Handbook.

* **Ability Score Increase**. Your Dexterity and Wisdom scores both increase by 1. In addition, one ability score of your choice increases by 1.
* **Wild Intuition**. When you make a Wisdom (Animal Handling) or Intelligence (Nature) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.
* **Expert Handling**. You can use the Help action to aid an ally animal companion or mount within 30 feet of you, rather than 5 feet of you.
* **Primal Connection**. You can cast [animal friendship](../../Magic/Spells/animal-friendship.md) once with this trait and regain the ability to do so when you finish a short or long rest. Wisdom is your spellcasting ability for this spell.
* **The Bigger They Are**. When you cast a spell that affects only beasts, it also affects monstrosities with an Intelligence score of 3 or lower.

```
name = 'Handling Dragonmarked'
description = "***Dragonmark: Mark of Handling.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. The Mark of Handling gives its bearer a primal connection to beasts and the natural world, granting the power to calm and coax. This extends beyond purely natural animals; the mark allows its bearer to guide a hippogriff as easily as a horse."

def level0(npc):
    npc.DEX += 1
    npc.WIS += 1
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    ability = choose("Choose an ability to improve: ", abilities)
    if ability == 'STR': npc.STR += 1
    elif ability == 'DEX': npc.DEX += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    elif ability == 'CHA': npc.CHA += 1

    npc.traits.append("***Wild Intuition.*** When you make a Wisdom (Animal Handling) or Intelligence (Nature) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    npc.actions.append("***Expert Handling.*** You can use the Help action to aid an ally animal companion or mount within 30 feet of you, rather than 5 feet of you.")

    npc.actions.append(f"***Primal Connection.*** You can cast spelllinkify('animal friendship') once with this trait. Wisdom is your spellcasting ability for this.")

    npc.traits.append("***The Bigger They Are.*** When you cast a spell that affects only beasts, it also affects monstrosities with an Intelligence score of 3 or lower.")

    quirk = random([
        "Your dragonmark is unusually small.",
        "Your dragonmark is remarkably large.",
        "Your dragonmark slowly moves around your body.",
        "Your dragonmark glows dramatically when you use it.",
        "Your dargonmark emits a soft hum when you use it.",
        "Your dragonmark itches when you’re near someone with a dragonmark.",
        "Your dragonmark tingles when you’re near someone with the same mark.",
        "Your dragonmark tickles when you use it.",
        "Your dragonmark is an unusual color but a normal shape."
    ])
    npc.description.append(f"***Dragonmark Quirk.*** {quirk}")
```
