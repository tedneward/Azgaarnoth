## Telekinetic
*Prerequisite*: Psionic Talent feature or Wild Talent feat

You learn to move things with your mind. You gain the following benefits:

* Increase your Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.
* You learn the [mage hand](https://www.dndbeyond.com/spells/mage-hand) cantrip. You can cast it without verbal or somatic components, and you can make the spectral hand invisible. If you already know this spell, its range increases by 30 feet when you cast it. Its spellcasting ability is the ability increased by this feat.
* As a bonus action, you can try to telekinetically shove one creature you can see within 30 feet of you. When you do so, roll your Psionic Talent die, and the target must succeed on a Strength saving throw (DC 8 + your proficiency bonus + the ability modifier of the score increased by this feat) or be moved toward you or away from you a number of feet equal to 5 times the number you rolled. A creature can willingly fail this save.

```
name = 'Telekinetic'
description = "***Feat: Telekinetic.*** You learn to move things with your mind."
def prereq(npc): return getattr(npc, 'psionicdie', None) != None
def apply(npc):
    ability = chooseability(npc, ['INT','WIS','CHA'])
    npc.actions.append(f"***Telekinesis.*** You can cast {spelllinkify('mage hand')} without verbal or somatic components, and you can make the spectral hand invisible. If you already know this spell, its range increases by 30 feet when you cast it. Your spellcasting ability for this spell is {ability}.")
    npc.defer(lambda npc: npc.bonusactions.append(f"***Telekinetic Shove.*** You can try to telekinetically shove one creature you can see within 30 feet of you. When you do so, roll your Psionic Talent die, and the target must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(ability)}) or be moved toward you or away from you a number of feet equal to 5 times the number you rolled. A creature can willingly fail this save.") )
```

