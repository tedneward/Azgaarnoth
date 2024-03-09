# Bardic College: College of Swords
Bards of the College of Swords are called blades, and they entertain through daring feats of weapon prowess. Blades perform stunts such as sword swallowing, knife throwing and juggling, and mock combats. Though they use their weapons to entertain, they are also highly trained and skilled warriors in their own right. Their talent with weapons inspires many blades to lead double lives. One blade might use a circus troupe as cover for nefarious deeds such as assassination, robbery, and blackmail. Other blades strike at the wicked, bringing justice to bear against the cruel and powerful. Most troupes are happy to accept a blade's talent for the excitement it adds to a performance, but few entertainers fully trust them.

Blades who abandon lives as entertainers have often run into trouble that makes maintaining their secret activities impossible. A blade caught stealing or engaging in vigilante justice is too great a liability for most troupes. With their weapon skills and magic, these blades either take up work as enforcers for Rogues' guilds or strike out on their own as adventurers.

Being one of the least-restrictive among the Bardic Colleges, the Colleges of Swords are found in universities all over Azgaarnoth; additionally, Sword bards are often taking on promising individuals, teaching them the rudiments, and then passing them on with a referral or endorsement to a nearby Sword College. These bards are often found out in the sketchiest places of the world, and many have found employment as an agent of the [Copper Order](../../Organizations/MilitantOrders/DraconicOrder/Copper.md). Many also join [mercenary companies](../../Organizations/MercCompanies/index.md) as soldiers, support staff, or advisers, and still more sign on with [merchant guilds](../../Organizations/MerchantGuilds/index.md) as guards, entertainment, or just to travel.

```
name = 'College of Swords'
description = "***Bardic College: College of Swords.*** Bards of the College of Swords are called blades, and they entertain through daring feats of weapon prowess. Blades perform stunts such as sword swallowing, knife throwing and juggling, and mock combats. Though they use their weapons to entertain, they are also highly trained and skilled warriors in their own right. Their talent with weapons inspires many blades to lead double lives. One blade might use a circus troupe as cover for nefarious deeds such as assassination, robbery, and blackmail. Other blades strike at the wicked, bringing justice to bear against the cruel and powerful. Most troupes are happy to accept a blade's talent for the excitement it adds to a performance, but few entertainers fully trust them."
```

## Bonus Proficiencies
*3rd-level College of Swords feature*

You gain proficiency with medium armor and scimitars.

If you're proficient with a simple or martial melee weapon, you can use it as a spellcasting focus for your bard spells.

```
def dueling(npc):
    npc.traits.append("***Fighting Style: Dueling.*** When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.")

def twoweapon(npc):
    npc.bonusactions.append("***Fighting Style: Two-Weapon Fighting.*** When you take the Attack or Multiattack action and attack with a light melee weapon that you're holding in one hand, you can attack with a different light melee weapon that you're holding in the other hand. You can add your ability modifier to the damage of this other attack. If either weapon has the thrown property, you can throw the weapon, instead of making a melee attack with it.")

def level3(npc):
    for prf in armor['medium']:
        npc.proficiencies.append(prf)
    npc.proficiencies.append("Scimitar")
```

## Fighting Style
*3rd-level College of Swords feature*

You adopt a style of fighting as your specialty. Choose one of the following options. You can't take a Fighting Style option more than once, even if something in the game lets you choose again.

* **Dueling**. When you are wielding a melee weapon in one hand and no other weapons, you gain a +2 bonus to damage rolls with that weapon.
* **Two-Weapon Fighting**. When you engage in two-weapon fighting, you can add your ability modifier to the damage of the second attack.

```
    choice = choose("Choose a fighting style: ", ['Dueling', 'Two-Weapon Fighting'])
    if choice == 'Dueling': dueling(npc)
    elif choice == 'Two-Weapon Fighting': twoweapon(npc)
```

## Blade Flourish
*3rd-level College of Swords feature*

You learn to conduct impressive displays of martial prowess and speed. As an action, you can make one melee weapon attack, and your walking speed increases by 10 feet until the end of the current turn. Whenever you use this action, you can also use one of the following Blade Flourish options as part of it.

* **Defensive Flourish**. You spin your weapon in circles, creating a hypnotic display. You can expend one of your uses of Bardic Inspiration, rolling a Bardic Inspiration die and adding the number rolled to your AC until the start of your next turn.
* **Slashing Flourish**. If the attack hits its target, you can expend one of your uses of Bardic Inspiration to cause the weapon to damage each creature of your choice, other than the target, that you can see within 5 feet of you. The damage equals the number you roll on the Bardic Inspiration die.
* **Mobile Flourish**. If the attack hits its target, you can expend one of your uses of Bardic Inspiration to push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on the Bardic Inspiration die. You can then immediately use your reaction to move up to your speed to an unoccupied space within 5 feet of the target.

```
    npc.defer(lambda npc: npc.actions.append("***Blade Flourish.*** You make {'one melee weapon attack' if npc.levels('Bard') < 6 else 'two melee weapon attacks'}, and you use one of the following options as part of it: **Defensive Flourish**. You spin your weapon in circles, creating a hypnotic display; {'you can expend one of your uses of Bardic Inspiration' if npc.levels('Bard') < 14 else 'you can roll a d6'} and adding the number rolled to your AC until the start of your next turn; **Slashing Flourish**. If the attack hits its target, {'you can expend one of your uses of Bardic Inspiration' if npc.levels('Bard') < 14 else 'you can roll a d6'} to cause the weapon to damage each creature of your choice, other than the target, that you can see within 5 feet of you. The damage equals the number you roll on the Bardic Inspiration die; **Mobile Flourish**. If the attack hits its target, {'you can expend one of your uses of Bardic Inspiration' if npc.levels('Bard') < 14 else 'you can roll a d6'} to push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on the Bardic Inspiration die. You can then immediately use your reaction to move up to your speed to an unoccupied space within 5 feet of the target.") )
```

## Cunning Flourish
*6th-level College of Swords feature*

You can attack twice, instead of once, whenever you use the Blade Flourish action on your turn. You can, nevertheless, still use only one Blade Flourish option when you take that action.

## Master's Flourish
*14th-level College of Swords feature*

Whenever you use a Blade Flourish option, you can roll a d6 and use it instead of expending a Bardic Inspiration die.

---

# Custom Bard Spells
The College of Swords developed many custom spells over the years.

* 2nd: [body spin](../../Magic/Spells/body-spin.md)
* 4th: [winterfloor](../../Magic/Spells/winterfloor.md)
