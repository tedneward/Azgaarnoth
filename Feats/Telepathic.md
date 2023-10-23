## Telepathic
*Prerequisite*: Psionic Talent feature or Wild Talent feat

You awaken the ability to mentally connect with others. You gain the following benefits:

* Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.
* You can speak telepathically to any creature you can see within 30 feet of you. Your telepathic utterances are in a language you know, and the creature understands you only if it knows that language. Your communication doesn't give the creature the ability to respond to you telepathically.
* If your Psionic Talent die is available, you can cast the [detect thoughts]() spell, requiring no components. When you start casting the spell, your Psionic Talent die decreases by one die size. Your spellcasting ability for the spell is the ability increased by this feat.

```
name = 'Telepathic'
description = "***Feat: Telepathic.*** You awaken the ability to mentally connect with others."
def prereq(npc): return getattr(npc, 'psionicdie', None) != None
def apply(npc):
    ability = chooseability(npc, ['INT','WIS','CHA'])
    npc.languages.append("telepathy 30 ft")
    npc.actions.append(f"***Telepathic.*** If your Psionic Talent die is available, you can cast the {spelllinkify('detect thoughts')} spell, requiring no components. When you start casting the spell, your Psionic Talent die decreases by one die size. Your spellcasting ability for this spell is {ability}.")
```
