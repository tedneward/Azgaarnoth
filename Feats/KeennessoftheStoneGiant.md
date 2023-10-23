## Keenness of the Stone Giant
*Prerequisite: 4th Level, [Strike of the Giants (Stone Giant) Feat](#strike-of-the-giants)*

You've manifested the physical talents emblematic of stone giants, granting you the following benefits:

* **Ability Score Increase.** Increase your Strength, Constitution, or Wisdom score by 1, to a maximum of 20.
* **Stone Throw.** As a bonus action, you can touch a rock that can fit in the palm of your hand and imbue it with magic. While the rock is imbued with magic and you are wielding it, the rock is a magic ranged weapon with which you're proficient, and it has the thrown property with a normal range of 60 feet and a long range of 180 feet. On a hit, the rock deals 1d10 bludgeoning damage, and if the target is a creature, it must succeed on a Strength saving throw (DC equals 8 + your proficiency bonus + the modifier of the ability increased by this feat) or be knocked prone. The magic remains in the rock until you hit with it or finish a long rest. You can imbue a number of rocks equal to your proficiency bonus with this bonus action, and you regain all expended uses when you finish a long rest.
* **Cavernous Sight.** You gain darkvision out to a range of 60 feet. If you already have darkvision from another source, its range increases by 60 feet.

```
name = 'Keenness of the Stone Giant'
description = "***Feat: Keenness of the Stone Giant.*** You've manifested the physical talents emblematic of stone giants."
def prereq(npc):
    return (npc.levels() >= 4) and ('Strike of the Giants' in npc.feats)
def apply(npc):
    ability = chooseability(npc, ['STR', 'CON', 'WIS'])

    if 'darkvision' in npc.senses:
        npc.senses['darkvision'] += 60
    else:
        npc.senses['darkvision'] = 60

    npc.defer(lambda npc: npc.bonusactions.append(f"***Stone Throw ({npc.proficiencybonus()} rocks/Recharges on long rest).*** You touch a rock that can fit in the palm of your hand and imbue it with magic. While the rock is imbued with magic and you are wielding it, the rock is a magic ranged weapon with which you're proficient. *Ranged Weapon Attack:* {npc.proficiencybonus() + npc.DEXbonus()} to hit, range 60/180, one target. Hit: 1d10 bludgeoning dmage. If the target is a creature, it must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.abilitybonus(ability)}) or be knocked prone. The magic remains in the rock until you hit with it or finish a long rest.") )
```

