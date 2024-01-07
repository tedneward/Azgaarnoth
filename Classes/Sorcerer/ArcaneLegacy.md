# Sorcerous Origin: Arcane Legacy
You have inherited an aptitude for magic which you later learned to control. This usually means you are part of a long line of powerful mages, but it's also possible that your inborn talent is the first in your family. In either case, your powers manifest through the following features.

```
name = 'Arcane Legacy'
description = "***Sorcerous Origin: Arcane Legacy.*** You have inherited an aptitude for magic which you later learned to control. This usually means you are part of a long line of powerful mages, but it's also possible that your inborn talent is the first in your family."
```

## Arcane Awareness
*1st-level Arcane Legacy feature*

The arcane power which suffuses your being makes you sensitive to the magic in your environment. You can cast [detect magic](../../Magic/Spells/detect-magic.md) at will without expending a spell slot. You also learn the [identify](../../Magic/Spells/identify.md) spell, and it becomes a sorcerer spell for you. Neither of these spells count against your number of spells known.

```
def level1(npc):
    npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('detect magic')
    npc.spellcasting['Sorcerer'].spellsalwaysprepared.append('identify')
```

## Legacy Magic
*1st-level Arcane Legacy feature*

Most sorcerers' magic is simplistic and raw, but yours carries the echoes of great practitioners of the past. Even though you haven't studied enough to master ritual casting, you nevertheless have a knack for some of those spells.

You learn extra spells at certain levels, as shown in the Legacy Spells chart below. These spells count as sorcerer spells for you, and do not count against your total number of spells known. Additionally, whenever you cast a spell you know that has the ritual tag, you can choose to expend 1 sorcery point instead of a spell slot.

**Legacy Spells**
Sorcerer Level|Spell
--------------|-----
1st|[find familiar](../../Magic/Spells/find-familiar.md)
3rd|[silence](../../Magic/Spells/silence.md)
5th|[Leomund's tiny hut](../../Magic/Spells/leomunds-tiny-hut.md)
7th|[detect curses](../../Magic/Spells/detect-curses.md)
9th|[Rary's telepathic bond](../../Magic/Spells/rarys-telepathic-bond.md)

> **GM's Note:** Alternatively, allow the player to choose a non-sorcerer spell of their choice from the wizard's spell list, so long as all the spells chosen follow a player-defined theme.

```
    def legacyspells(npc):
        level = npc.levels('Sorcerer')
        spellcasting = npc.spellcasting['Sorcerer']
        spellcasting.spellsalwaysprepared.append('find familiar')
        if level >= 3: spellcasting.spellsalwaysprepared.append('silence')
        if level >= 5: spellcasting.spellsalwaysprepared.append('leomunds tiny hut')
        if level >= 7: spellcasting.spellsalwaysprepared.append('detect curses')
        if level >= 9: spellcasting.spellsalwaysprepared.append('rarys telepathic bond')
    npc.defer(lambda npc: legacyspells(npc))
```

## Magical Knack
*6th-level Arcane Legacy feature*

Whenever you make an Intelligence (Arcana) check, you can add your Charisma modifier to the roll. If you make the check intentionally (such as to examine something), you can expend 1 sorcery point to give yourself advantage on the roll.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Magical Knack.*** Whenever you make an Intelligence (Arcana) check, you can add {npc.CHAbonus()} to the roll. If you make the check intentionally (such as to examine something), you can expend 1 sorcery point to give yourself advantage on the roll.") )
```

## Forceful Concentration
*14th-level Arcane Legacy feature*

You learn how to funnel extra power into your spells to allow you to maintain more than one spell at a time. If you are concentrating on exactly one spell, you can cast a concentration spell without ending the first spell. The combined spell level of the two spells cannot exceed the highest spell level for which you have spell slots. Any Constitution saving throws to maintain concentration are made for each spell individually.

At the start of each of your turns while you are concentrating on two spells, you must use a bonus action and expend sorcery points to maintain concentration. The sorcery point cost is equal to the spell level of the highest-level spell you're concentrating on. If you are unable to pay this cost (or if you choose not to), you instead choose one spell to end.

```
def level14(npc):
    def highestlevelspellslot(npc):
        slots = npc.spellcasting['Sorcerer'].slottable[npc.levels('Sorcerer')]
        return len(slots)
    npc.defer(lambda npc: npc.actions.append(f"***Forceful Concentration.*** While you are concentrating on exactly one spell, you cast a concentration spell without ending the first spell. The combined spell level of the two spells cannot exceed {highestlevelspellslot(npc)}. Any Constitution saving throws to maintain concentration are made for each spell individually.") )

    npc.bonusactions.append("***Maintain Forceful Concentration.*** You expend sorcery points equal to the spell level of the highest-level spell you're concentrating on. If you are unable to pay this cost (or if you choose not to), you instead choose one spell to end.")
```

## Mana Drain
*18th-level Arcane Legacy feature*

You can pull the magic out of other creatures and absorb it for yourself. As an action, you can spend any number of sorcery points and target a creature you can see, forcing them to make a Charisma saving throw against your spell save DC. On a failed save, the target loses unused spell slots with a combined spell level equal to the number of sorcery points spent, or half that amount on a successful save. Higher-level spell slots are lost first. You regain expended spell slots of the same number and levels as what the target lost. This cannot cause you to stockpile spell slots beyond your normal allotment.

```
def level18(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Mana Drain.*** You spend any number of sorcery points and target a creature you can see, forcing them to make a Charisma saving throw (DC {npc.spellcasting['Sorcerer'].spellsavedc()}). On a failed save, the target loses unused spell slots with a combined spell level equal to the number of sorcery points spent, or half that amount on a successful save. Higher-level spell slots are lost first. You regain expended spell slots of the same number and levels as what the target lost. This cannot cause you to stockpile spell slots beyond your normal allotment.") )
```
