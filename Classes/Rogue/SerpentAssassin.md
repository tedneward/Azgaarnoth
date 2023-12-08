# Roguish Archetype: Serpent Assassin
The Serpent Assassin embodies the deadly art of assassination and poison mastery. These rogues excel at infiltrating their targets’ domains, striking swiftly and silently, and utilizing poisons to devastating effect. 

Originally, the Serpent Assassins came with the Hordes and were exclusively of the [yuan-ti](../../Races/YuanTi.md). But as the Hordes spread across Azgaarnoth, so did the snake people, and so did the secrets of their order. Though never numerous, a Serpent Assassin can now be found in most major cities, though usually not more than one, since one of the credos of the profession is that "no serpent shares a lair". 

Although most rogues' guilds would love to have a Serpent Assassin as a member, most of the Snakes (a common colloquial term among the rogues for a Serpent Assassin) prefer to remain independent, taking jobs from guilds as they choose--or choose not. In a few, rare, cases, the Serpent Assassin moves in to take over the guild, but if they do, usually they find it tiresome to run, and move back to being an independent.

Despite the stereotype of the uncaring, evil, sociopathic killer, some Serpent Assassins actually use their skills toward good ends, looking to eliminate evil in the most subtle means possible. By far the majority, however, strike at those that bring them money--or power.

```
name = 'Serpent Assassin'
description = "***Roguish Archetype: Serpent Assassin.*** The Serpent Assassin embodies the deadly art of assassination and poison mastery. These rogues excel at infiltrating their targets’ domains, striking swiftly and silently, and utilizing poisons to devastating effect."
```

## Poisoner’s Expertise
*3rd-level Serpent Assassin feature*

Your proficiency with poisons deepens. You gain proficiency with the poisoner’s kit if you don’t already have it. Additionally, you can create and apply potent poisons more quickly and effectively. When you use the poisoner’s kit to apply poison to a weapon, it takes you half the normal time, and the DC to resist the poison’s effects is increased by your proficiency bonus.

```
def level3(npc):
    if "Poisoner's kit" not in npc.proficiencies:
        npc.proficiencies.append("Poisoner's kit")
    npc.traits.append("***Poisoner's Expertise.*** When you use the poisoner’s kit to apply poison to a weapon, it takes you half the normal time, and the DC to resist the poison’s effects is increased by your proficiency bonus.")
```

## Serpent Strike
*3rd-level Serpent Assassin feature*

You learn the art of striking with deadly precision. When you hit a creature with a weapon attack that deals sneak attack damage, you can choose to forego rolling damage dice and instead automatically deal maximum damage. Additionally, if the target is poisoned, it has disadvantage on the saving throw to resist being grappled or restrained by your abilities.

```
    npc.traits.append("***Serpent Strike.*** When you hit a creature with a weapon attack that deals sneak attack damage, you can choose to forego rolling damage dice and instead automatically deal maximum damage. Additionally, if the target is poisoned, it has disadvantage on the saving throw to resist being grappled or restrained by your abilities.")
```

## Serpent’s Guile
*9th-level Serpent Assassin feature*

Your mastery of deception and manipulation reaches new heights. You gain advantage on all Charisma (Deception) and Charisma (Persuasion) ability checks made to deceive or manipulate others. Additionally, when you use your Cunning Action to Hide, you can choose to make a Charisma (Deception) check contested by a creature’s Wisdom (Perception) check. If you succeed, the creature’s passive Perception is considered 10 for the purpose of detecting you until the start of your next turn.

```
def level9(npc):
    npc.traits.append("***Serpent's Guile.*** You gain advantage on all Charisma (Deception) and Charisma (Persuasion) ability checks made to deceive or manipulate others. Additionally, when you use your Cunning Action to Hide, you can choose to make a Charisma (Deception) check contested by a creature’s Wisdom (Perception) check. If you succeed, the creature’s passive Perception is considered 10 for the purpose of detecting you until the start of your next turn.")
```

## Cloak of Shadows
*13th-level Serpent Assassin feature*

You gain the ability to blend seamlessly with shadows. When you are in an area of dim light or darkness, you can use a bonus action to magically become invisible until the start of your next turn or until you attack or cast a spell. Once you use this feature, you can’t use it again until you finish a short or long rest.

```
def level13(npc):
    npc.bonusactions.append("***Cloak of Shadows (Recharges on short or long rest).*** When you are in an area of dim light or darkness, you can use a bonus action to magically become invisible until the start of your next turn or until you attack or cast a spell.")    
```

## Serpent’s Embrace
*17th-level Serpent Assassin feature*

You unlock the true power of the serpent within you. When you hit a creature with a sneak attack, you can choose to expend a use of your Venomous Strike feature to force the target to make a Constitution saving throw against your Ninjutsu DC. On a failed save, the target takes poison damage equal to your Sneak Attack damage at the start of its turns for a number of rounds equal to your Dexterity modifier. On a successful save, the target takes half damage and the effect ends. Additionally, while you are hidden, your Sneak Attack damage increases by an additional 1d6.

```
def level17(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Serpent's Embrace.*** When you hit a creature with a sneak attack, you can choose to expend a use of your Serpent Strike to force the target to make a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.DEXbonus()}). On a failed save, the target takes {(npc.levels(name) + 1) // 2}d6 poison damage at the start of its turns for {npc.DEXbonus()} rounds. On a successful save, the target takes half damage and the effect ends. Additionally, while you are hidden, your Sneak Attack damage increases by an additional 1d6.") )
```
