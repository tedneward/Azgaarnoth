# Divine Domain: Shadow
The gods of Shadow, though sometimes evil, are not always.  They are the patrons for those who feel out of place; from an orphan or an aspiring artist to a thief well versed in lying, used to being double-crossed. The gods of shadow teach that sometimes it is not always best for your presence to be known, or for your true identity to be known, sometimes it is best to sneak past your rival than punch them in the face. 

Clerics of these deities seek to silently affect from the darkness, convince others to liberate mines overrun by orcs or sneak past the guards of a museum to retrieve an artefact; these clerics tend to sit back and watch while they can, allowing others to make their choices, but if they go astray they are not afraid to quickly dart into action to rectify the mistakes. Clerics from these domains seek not to gain praise for themselves but seek to change the world from within the veil of shadow.

This domain is available to the [Almalzish tradition](../../Religions/AlUma.md#almalzish-cleric),[Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Malar](../../Religions/Pantheon/Malar.md), [Tiamat](../../Religions/Pantheon/Tiamat.md), ...

```
name = 'Shadow'
description = "***Divine Domain: Shadow.*** The gods of Shadow, though sometimes evil, are not always.  They are the patrons for those who feel out of place; from an orphan or an aspiring artist to a thief well versed in lying, used to being double-crossed. The gods of shadow teach that sometimes it is not always best for your presence to be known, or for your true identity to be known, sometimes it is best to sneak past your rival than punch them in the face."
```

## Domain Spells
You gain domain spells at the cleric levels listed in the Shadow Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Domain Spells**

Cleric Level | Spells
------------ | ------
1st	| [disguise self](../../Magic/Spells/disguise-self.md), [longstrider](../../Magic/Spells/longstrider.md)
3rd	| [pass without trace](../../Magic/Spells/pass-without-trace.md), [invisibility](../../Magic/Spells/invisibility.md)
5th	| [nondetection](../../Magic/Spells/nondetection.md), [phantom steed](../../Magic/Spells/phantom-steed.md)
7th	| [greater invisibility](../../Magic/Spells/greater-invisibility.md), [freedom of movement](../../Magic/Spells/freedom-of-movement.md)
9th	| [seeming](../../Magic/Spells/seeming.md), [modify memory](../../Magic/Spells/modify-memory.md)

```
domainspells = {
    1: ['disguise self', 'longstrider'],
    3: ['pass without trace', 'invisibility'],
    5: ['nondetection', 'phantom steed'],
    7: ['greater invisibility', 'freedom of movement'],
    9: ['seeming', 'modify memory']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(spellcasting.casterclass) >= 1: results += domainspells[1]
        if npc.levels(spellcasting.casterclass) >= 3: results += domainspells[3]
        if npc.levels(spellcasting.casterclass) >= 5: results += domainspells[5]
        if npc.levels(spellcasting.casterclass) >= 7: results += domainspells[7]
        if npc.levels(spellcasting.casterclass) >= 9: results += domainspells[9]
        spellcasting.spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```


## Bonus Proficiency
*1st-level Shadow domain feature*

Chose two skills from: Stealth, Deception, Persuasion, Sleight of hand and Insight. These two skills now have proficiency, if you already had proficiency in it you can double your proficiency bonus with these checks.

```
    skilllist = ['Stealth', 'Deception', 'Persuasion', 'Sleight of Hand', 'Insight']
    skill = chooseskill(skilllist)
    npc.addskillorexpertise(skill)
    skilllist.remove(skill)
    skill = chooseskill(skilllist)
    npc.addskillorexpertise(skill)
```

## Stealthy Movement
*1st-level Shadow domain feature*

Your speed increases by 10 and travelling at a fast pace does not impose disadvantage on your stealth checks.

```
    npc.speed['walking'] += 10
    npc.traits.append("***Stealthy Movement.*** Traveling at a fast pace does not impose disadvantage on your Stealth checks.")
```

## Channel Divinity: Alter Perception
*2nd-level Shadow domain feature*

You can use your Channel Divinity to change the perception of others.

You can use this as a reaction to alter any dice roll within 60 feet of you by 1d4+ 1/4 your cleric level rounded up. You choose whether to add this or subtract this.

```
def level2(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Alter Perception.*** You can use this to alter any dice roll within 60 feet of you by 1d4 + {(npc.levels('Cleric') // 4)+1}. You choose whether to add this or subtract this.") )
```

## Heart of Shadows
*6th-level Shadow domain feature*

When someone makes a spell attack roll or melee attack roll aimed at yourself or someone within 5 ft of you, you can use your reaction to impose disadvantage on that roll. You can do this a number of times equal to your Wisdom modifier before you need a short rest to recharge.

```
def level6(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Heart of Shadows ({npc.WISbonus()}/Recharges on short rest).*** When someone makes a spell attack roll or melee attack roll aimed at yourself or someone within 5 ft of you, you impose disadvantage on that roll."))
```

## Divine Strike
*8th-level Shadow domain feature*

You gain the ability to strike harder with your weapon due to your elusive nature. Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 force damage to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.actions.append("***Divine Strike (1/turn).*** When you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} force damage to the target.")
```

## Elusive Spirit
*17th-level Shadow domain feature*

You become truly elusive. From this point, all saving throws are made with advantage.

```
def level17(npc):
    npc.traits.append("***Elusive Spirit.*** All saving throws are made with advantage.")
```
