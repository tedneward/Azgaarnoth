# Martial Archetype: Banneret
A banneret is a knight who inspires greatness in others by committing brave deeds in battle. The mere presence of one in a hamlet is enough to cause some orcs and bandits to seek easier prey. A lone banneret is a skilled warrior, but a banneret leading a band of allies can transform even the most poorly equipped militia into a ferocious war band.

A banneret prefers to lead through deeds, not words. As a banneret spearheads an attack, their actions can awaken reserves of courage and conviction in allies that they never suspected they had.

```
name = 'Banneret'
description = "***Martial Archetype: Banneret.*** A banneret is a knight who inspires greatness in others by committing brave deeds in battle. The mere presence of one in a hamlet is enough to cause some orcs and bandits to seek easier prey. A lone banneret is a skilled warrior, but a banneret leading a band of allies can transform even the most poorly equipped militia into a ferocious war band."
```

## Rallying Cry
*3rd-level Banneret feature*

You learn how to inspire your allies to fight on past their injuries. When you use your Second Wind feature, you can choose up to three creatures within 60 feet of you that are allied with you. Each one regains hit points equal to your fighter level, provided that the creature can see or hear you.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append("***Rallying Cry.*** When you use your Second Wind feature, you can choose up to three creatures within 60 feet of you that are allied with you. Each one regains {npc.levels('Fighter')} hit points, provided that the creature can see or hear you.") )
```

## Royal Envoy
*7th-level Banneret feature*

Knights of high standing are expected to conduct themselves with grace. You gain proficiency in the Persuasion skill. If you are already proficient in it, you gain proficiency in one of the following skills of your choice: Animal Handling, Insight, Intimidation, or Performance.

Your proficiency bonus is doubled for any ability check you make that uses Persuasion. You receive this benefit regardless of the skill proficiency you gain from this feature.

```
def level7(npc):
    if 'Persuasion' in npc.proficiencies: 
        npc.proficiencies.append(choose("Choose a proficiency: ", ['Animal Handling', 'Insight', 'Intimidation', 'Performance']))
    else:
        npc.proficiencies.append("Persuasion")
    npc.traits.append("***Royal Envoy.*** Your proficiency bonus is doubled for any ability check you make that uses Persuasion.")
```

## Inspiring Surge
*10th-level Banneret feature*

When you use your Action Surge feature, you can choose one creature within 60 feet of you that is allied with you. That creature can make one melee or ranged weapon attack with its reaction, provided that it can see or hear you.

Starting at 18th level, you can choose two allies within 60 feet of you, rather than one.

```
def level10(npc):
    npc.defer(lambda npc: npc.traits.append(f"When you use your Action Surge feature, you can choose {'one creature' if npc.level('Fighter') < 18 else 'two creatures'} within 60 feet of you that is allied with you. That creature(s) can make one melee or ranged weapon attack with its reaction, provided that it can see or hear you.") )
```

## Bulwark
*15th-level Banneret feature*

You can extend the benefit of your Indomitable feature to an ally. When you decide to use Indomitable to reroll an Intelligence, a Wisdom, or a Charisma saving throw and you aren't incapacitated, you can choose one ally within 60 feet of you that also failed its saving throw against the same effect. If that creature can see or hear you, it can reroll its saving throw and must use the new roll.

```
def level15(npc):
    npc.traits.append("***Bulwark.*** When you decide to use Indomitable to reroll an Intelligence, a Wisdom, or a Charisma saving throw and you aren't incapacitated, you can choose one ally within 60 feet of you that also failed its saving throw against the same effect. If that creature can see or hear you, it can reroll its saving throw and must use the new roll.")
```
