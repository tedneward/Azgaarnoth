# Arcane Tradition: School of Bladesinging
The original bladesingers were elves who bravely stood against the Hordes. They were elf wizards who mastered a school of sword fighting grounded in a tradition of arcane magic. In combat, a bladesinger uses a series of intricate, elegant maneuvers that fend off harm and allow the bladesinger to channel magic into devastating attacks and a cunning defense. As the wars spread and the humans took up much of the burden of the combat, the elves were persuaded to teach Bladesinging to them, and over time to yet more others.

Styles of Bladesinging are broadly categorized based on the type of weapon employed, and each is associated with a category of animal. Within that style are specializations named after specific animal types, based on the types of spells employed, the techniques of the master, and the particular weapon used.

Styles that employ a sword belong to the Cat family, including the longsword-wielding Lion style, and the scimitar-wielding Red Tiger style. Styles that focus on the use of hafted weapons belong to the Bird family, including the handaxe-throwing Eagle style or warpick-wielding Raven style. Styles that use whips, chains, or flails are included in the Snake style family, such as the whip-wielding Viper style. Other styles have been invented and perfected for other weapons.

When a Bladesingers apprentices to a master, they typically get a tattoo of their chosen style's animal. Some bladesingers learn multiple styles and bear many tattoos, wearing a warning on their skin of their deadly skills. Some even work their style tattoo into a [magic tattoo](../../Magic/Tattoos/index.md), making them even more dangerous and deadly.

Bladesingers are rare, typically loners, preferring the open road and opportunities to put their skills to the test, either in pursuit of improvement or to prove their skills to the world. Every Bladesinger, however, feels a deep-seated need to pass on their skills and knowledge to a new generation, and many take multiple students before passing on; they often take on students while taking residence at (or, sometimes, founding) a [dueling college](../../Organizations/DuelingColleges.md). Some Bladesingers have also taken up residence with [kensai](../../Classes/Monk/Kensai.md) monasteries. Some few teach at the Academy of the [Bronze Order](../../Organizations/MilitantOrders/DraconicOrder/Bronze.md) or other militant orders, and periodically a [mercenary company](../../Organizations/MercCompanies/index.md) can convince a Bladesinger to take employment (usually for a specific mission or towards a particular goal).

```
name = 'Bladesinging'
description = "***Arcane Tradition: School of Bladesinging.*** The original bladesingers were elves who bravely stood against the Hordes. They were elf wizards who mastered a school of sword fighting grounded in a tradition of arcane magic. In combat, a bladesinger uses a series of intricate, elegant maneuvers that fend off harm and allow the bladesinger to channel magic into devastating attacks and a cunning defense. As the wars spread and the humans took up much of the burden of the combat, the elves were persuaded to teach Bladesinging to them, and over time to yet more others."
```

## Training in War and Song
*2nd-level Bladesinging feature*

You gain proficiency with light armor, and you gain proficiency with one type of one-handed melee weapon of your choice.

You also gain proficiency in the Performance skill if you don't already have it.

```
def level2(npc):
    for arm in armor['light']:
        npc.proficiencies.append(arm)
    npc.skills.append('Performance')
    bladesingerweapons = []
    for wpnname in weapons['simple-melee']:
        if wpnname in npc.proficiencies:
            pass
        elif 'two-handed' not in weapons['simple-melee'][wpnname][2]:
            bladesingerweapons.append(wpnname)
    for wpnname in weapons['martial-melee']:
        if wpnname in npc.proficiencies:
            pass
        if 'two-handed' not in weapons['martial-melee'][wpnname][2]:
            bladesingerweapons.append(wpnname)
    npc.proficiencies.append(choose("Choose a weapon: ", bladesingerweapons) )
```

## Bladesong
*2nd-level Bladesinging feature*

You can invoke a secret magic called the Bladesong, provided that you aren't wearing medium or heavy armor or using a shield. It graces you with supernatural speed, agility, and focus.

You can use a bonus action to start the Bladesong, which lasts for 1 minute. It ends early if you are incapacitated, if you don medium or heavy armor or a shield, or if you use two hands to make an attack with a weapon. You can also dismiss the Bladesong at any time you choose (no action required).

While your Bladesong is active, you gain the following benefits:

* You gain a bonus to your AC equal to your Intelligence modifier (minimum of +1).

* Your walking speed increases by 10 feet.

* You have advantage on Dexterity (Acrobatics) checks.

* You gain a bonus to any Constitution saving throw you make to maintain your concentration on a spell. The bonus equals your Intelligence modifier (minimum of +1).

You can use this feature twice. You regain all expended uses of it when you finish a short or long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Bladesong (2/Recharges on short or long rest).*** You start the Bladesong, which lasts for 1 minute, and ends early if you are incapacitated, if you don medium or heavy armor or a shield, or if you use two hands to make an attack with a weapon, or if you choose to (no action required). While your Bladesong is active, you gain the following benefits: You gain a +{npc.INTbonus()} bonus to your AC; Your walking speed increases by 10 feet; You have advantage on Dexterity (Acrobatics) checks; You gain a +{npc.INTbonus()} bonus to any Constitution saving throw you make to maintain your concentration on a spell{'; You add ' + str(npc.INTbonus()) + ' to the damage of your melee weapon attacks.' if npc.levels('Wizard') >= 14 else '.'}") )
```

## Extra Attack
*6th-level Bladesinging feature*

You can attack twice, instead of once, whenever you take the Attack action on your turn.

```
def level6(npc):
    npc.actions.append("***Multiattack.*** You can attack twice, instead of once, whenever you take the Attack action on your turn.")
```

## Song of Defense
*10th-level Bladesinging feature*

You can direct your magic to absorb damage while your Bladesong is active. When you take damage, you can use your reaction to expend one spell slot and reduce that damage to you by an amount equal to five times the spell slot's level.

```
def level10(npc):
    npc.reactions.append("***Song of Defense.*** When you take damage while your Bladesong is active, you expend one spell slot and reduce that damage to you by an amount equal to five times the spell slot's level.")
```

## Song of Victory
*14th-level Bladesinging feature*

You add your Intelligence modifier (minimum of +1) to the damage of your melee weapon attacks while your Bladesong is active.

---

# Bladesinging Spells
Over the years, bladesingers have developed a certain number of spells that they will only teach to their apprentices.

* [blade of elemental chaos](), [blazing blade arc](), [darkness blade arc](), [freezing blade arc](), [howling blade arc](), [luminous blade arc](), [magic blade arc](), [shocking blade arc]()
* [battlesheath of flames](), [battlesheath of frost](), [battlesheath of lightning]()
* 6th: [antimagic strike]()
