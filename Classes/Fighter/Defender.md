# Martial Archetype: (Dwarven) Defender
Dwarves are well-known for their stubborn, head-on approach on things. Give them a suit of armor, a shield, and centuries of war history, and you have a typical dwarven defender. Ironclad, both literally and metaphorically, these juggernauts embody a valuable lesson of why dwarves are not meant to be trifled with. Those who are foolish enough to taunt these guardians' physical appearance tend to regret what they just did, often while being stomped to death to the half-pints they've been wooing a minute before.

Over the millennia, dwarves have learned to teach these martial skills to others (most notably humans). However, most defenders are dwarven still to this day, and any who take up this archetype likely have strong dwarven influence in their lives.

```
name = 'Defender'
description = "***Martial Archetype: Defender.*** Dwarves are well-known for their stubborn, head-on approach on things. Give them a suit of armor, a shield, and centuries of war history, and you have a typical dwarven defender. Ironclad, both literally and metaphorically, these juggernauts embody a valuable lesson of why dwarves are not meant to be trifled with. Those who are foolish enough to taunt these guardians' physical appearance tend to regret what they just did, often while being stomped to death to the half-pints they've been wooing a minute before."
```

## Stands Like A Rock, Hits Like A Rock
*3rd-level Defender feature*

When you choose this subclass, your training as a Defender grants you a special stance that allows you to hold your ground firmly. You gain the following benefits:

As long as you are wearing a heavy armor, wielding a shield, and not incapacitated, the area within 5 feet of you is considered the difficult terrain for creatures hostile to you.

You can wield a shield as a melee weapon you are proficient in. On a hit, the shield deals 1d6 bludgeoning damage.

When you hit a creature with a shield on your turn, you can use a bonus action to goad the target, compelling it to attack you. The target must make a Wisdom saving throw. The DC equals 8 + your proficiency bonus + your Strength modifier. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.

```
def level3(npc):
    npc.traits.append("***Stands Like A Rock.*** As long as you are wearing a heavy armor, wielding a shield, and not incapacitated, the area within 5 feet of you is considered the difficult terrain for creatures hostile to you.")
    npc.actions.append("***Hits Like A Rock.*** You can wield a shield as a melee weapon you are proficient in. On a hit, the shield deals 1d6 bludgeoning damage.")
    npc.defer(lambda npc: npc.bonusactions.append("***Goad.*** When you hit a creature with a shield on your turn, you goad the target, compelling it to attack you. The target must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}). On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.") )
```

## Compact Yet Colossal
*7th-level Defender feature*

You are surprisingly resilient against outer force to move you out of your space. As long as you are not incapacitated, you are considered one size larger for the purpose of avoiding or resisting being shoved or grappled, and creatures smaller than you have disadvantage on Strength (Athletics) checks when attempting to shove or grapple you.

```
def level7(npc):
    npc.traits.append("***Compact Yet Colossal.*** As long as you are not incapacitated, you are considered one size larger for the purpose of avoiding or resisting being shoved or grappled, and creatures smaller than you have disadvantage on Strength (Athletics) checks when attempting to shove or grapple you.")
```

## Additional Fighting Style
*10th-level Defender feature*

You gain the [Defense](Styles.md#defense) or [Protection](Styles.md#protection) option the [Fighting Style](Styles.md) class feature, if you do not have it already. If you already have both Fighting Style options, you can choose a third option from the Fighting Style class feature.

```
def level10(npc):
    if 'Defense' and 'Protection' in npc.fightingstyles:
        allclasses['Fighter'].choosestyle(npc)
    elif 'Defense' in npc.fightingstyles:
        allclasses['Fighter'].choosestyle(npc)
    elif 'Protection' in npc.fightingstyles:
        allclasses['Fighter'].choosestyle(npc)
    else:
        allclasses['Fighter'].choosestyle(npc)
```

## Warding Shield
*15th-level Defender feature*

You can wield your shield to protect yourself from an attack that would normally unable to avoid. When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. You must wield a shield to gain this benefit.

```
def level15(npc):
    npc.traits.append("***Warding Shield.*** When you are subjected to an effect that allows you to make a Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw, and only half damage if you fail. You must wield a shield to gain this benefit.")
```

## Stands Like A Mountain, Hits Like A Mountain
*18th-level Defender feature*

Your presence is improved to the point that simply standing there imposes threat against your enemies. You gain the following benefits.

When a hostile creature first enters the area within 5 feet of you or starts its turn there, it must make a Wisdom saving throw. The DC equals 8 + your proficiency bonus + your Strength modifier. On a failed save, it has disadvantage on all attack rolls against targets other than you until the end of your next turn. You must be wearing heavy armor, wielding a shield, and not incapacitated to gain this benefit.

Once on each of your turn when you hit a creature with a shield, you can deal an additional 1d6 damage with the attack.

When you hit a creature with a shield on your turn, you can use a bonus action to cause a concussive smite against the target. The target must make a Constitution saving throw. The DC equals 8 + your proficiency bonus + your Strength modifier. On a failed save, the creature becomes stunned until the end of your next turn.

```
def level18(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Stands Like A Mountain.*** When a hostile creature first enters the area within 5 feet of you or starts its turn there, it must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}). On a failed save, it has disadvantage on all attack rolls against targets other than you until the end of your next turn. You must be wearing heavy armor, wielding a shield, and not incapacitated to gain this benefit.") )

    npc.traits.append("***Hits Like A Mountain.*** Once on each of your turn when you hit a creature with a shield, you can deal an additional 1d6 damage with the attack.")

    npc.defer(lambda npc: npc.bonusactions.append(f"***Shield Bash.*** When you hit a creature with a shield on your turn, you cause a concussive smite against the target. The target must make a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}). On a failed save, the creature becomes stunned until the end of your next turn.") )
```