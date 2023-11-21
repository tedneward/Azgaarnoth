# Martial Archetype: Dragon Slayer
Despite the beneficial intent of the [Draconic Order](../../Organizations/MilitantOrders/DraconicOrder/), many groups and individuals do not trust dragons, regardless of the nature of their scales. As a result, many communities spend a great deal of time--quietly--training individuals who are capable of slaying something draconic in nature. These are collectively known as "Dragon Slayers". The [Dread Emperor](../../People/DreadEmperor.md) has been openly training Dragon Slayers, and offers a warm welcome to any who would take up the cause and occupation. The Hordes have also given warm welcome to Slayers, though often to attack other creatures that are far from draconic.

Regardless of their intended target, a Dragon Slayer is a stoic warrior who stands fast in the face of daunting foes and revels in the challenging combat they bring with them. They are often reckless, charging into a fray that others would run from, and then coming out on top time and time again, relying on deadly slaying strikes to bring down even the toughest of monsters.

```
name = 'Dragon Slayer'
description = "***Martial Archetype: Dragon Slayer.*** A Dragon Slayer is a stoic warrior who stands fast in the face of daunting foes and revels in the challenging combat they bring with them. They are often reckless, charging into a fray that others would run from, and then coming out on top time and time again, relying on deadly slaying strikes to bring down even the toughest of monsters."
```

## Slayer Skill
*3rd-level Dragon Slayer feature*

You gain proficiency in either Nature or Survival. Additionally, you have advantage on ability checks using that skill, if whatever you are identifying or tracking is draconic in nature.

```
def level3(npc):
    skill = choose("Choose one: ", ['Nature', 'Survival'])
    npc.proficiencies.append(skill)
    npc.traits.append(f"***Slayer Skill.*** You have advantage on checks using {skill}, if whatever you are identifying or tracking is draconic in nature.")
```

## Slaying Strike
*3rd-level Dragon Slayer feature*
 
You can make the most of an advantageous position. If you take the Attack action on your turn and have advantage on one of the attacks, you can forgo the advantage for that roll to make your strike exceptionally deadly. If the attack hits, it deals an extra 1d8 damage of the weapon's damage type, and the creature must succeed on a Strength saving throw or be knocked prone. This damage increases to 2d8 at 10th level. The DC for the Strength saving throw is equal to the total damage dealt. You can use this ability only once per round.

```
    npc.defer(lamba npc: npc.actions.append("***Slaying Strike (1/round).*** If you take the Attack action on your turn and have advantage on one of the attacks, you can forgo the advantage for that roll to make your strike exceptionally deadly. If the attack hits, it deals an extra {'1d8' if npc.levels('Fighter') < 10 else '2d8'} damage of the weapon's damage type, and the creature must succeed on a Strength saving throw (DC equals the total damage dealt) or be knocked prone.") )
```

## Supernatural Resilience
*7th-level Dragon Slayer feature*
 
You have enough experience dealing with dragons and other monsters to be able to withstand their most powerful attacks. When another creature forces you to make a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll, but before any of the roll's effects occur.

If you use this feature and then reroll the save using your Indomitable class feature, the bonus you rolled also applies to the second roll.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level7(npc):
    npc.traits.append("***Supernatural Resilience (Recharges on short or long rest).*** When another creature forces you to make a saving throw, you can use this feature to add a d10 to your roll. You can do so after seeing the initial roll, but before any of the roll's effects occur. If you use this feature and then reroll the save using your Indomitable class feature, the bonus you rolled also applies to the second roll.")
```

## Slayer's Counter
*10th-level Dragon Slayer feature*
 
When a creature larger than you hits or misses you with a melee weapon attack, you can use your reaction to immediately make a melee weapon attack against that creature.

```
def level10(npc):
    npc.reactions.append("***Slayer's Counter.*** When a creature larger than you hits or misses you with a melee weapon attack, you make a melee weapon attack against that creature.")
```

## Slayer's Defense
*15th-level Dragon Slayer feature*
 
If an enemy creature hits you with a weapon attack, you can add +4 to your AC for all subsequent attacks that the creature makes against you until the end of the current turn. You can use this ability once per round.

```
def level15(npc):
    npc.traits.append("***Slayer's Defense (1/round).*** If an enemy creature hits you with a weapon attack, you can add +4 to your AC for all subsequent attacks that the creature makes against you until the end of the current turn.")
```

## Deadly Strike
*18th-level Dragon Slayer feature*
 
You have learned how to maximize the effectiveness of your Slaying Strike. If you hit a creature with a Slaying Strike, you can choose to automatically deal maximum damage rather than rolling damage. If you do so, the creature falls prone without a saving throw.

Once you use this ability, you can't do so again until you finish a short or long rest.

```
def level18(npc):
    npc.traits.append("***Deadly Strike (Recharges on short or long rest).*** If you hit a creature with a Slaying Strike, you can choose to automatically deal maximum damage rather than rolling damage. If you do so, the creature falls prone without a saving throw.")
```
