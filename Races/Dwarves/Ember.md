# Ember Dwarf
As an ember dwarf, your connection to the elements of fire and earth shines through in your very body. Ember dwarves are often erroneously called half-azer because of their appearance. They have dark, ashen skin, with fiery red or orange hair. When they access the fiery power latent within them, their hair transforms into bright vibrant flames that don't burn them or their equipment. They usually have orange, yellow, or red eyes dotted with ashen flecks of black.

Ember dwarves are born to normal dwarf parents when latent elemental or fiendish bloodlines activate in the child. These dwarves are the descendants of those dwarven clans that grew accustomed to a volcanic home by ancient elemental magic, leaving them changed in subtle--and not-so-subtle--ways.

***Ability Score Increase.*** Your Dexterity score or your Charisma score increases by 1 (your choice).

***Elemental Hybrid.*** You have two creature types: humanoid (dwarf) and elemental (fire). You can be affected by a game effect if it works on either of your creature types.

***Fire Resistance.*** You have resistance to fire damage.

***Heated Body.*** When a creature starts its turn while it is grappling you or you are grappling it, you may choose to deal it fire damage equal to your proficiency bonus. Once you have used this feature, you can't do so again until you finish a short or long rest.

***Hot-Footed.*** Your base walking speed increases to 30 feet.

```
name = 'Ember'
description = "***Subrace: Ember Dwarf.*** Your connection to the elements of fire and earth shines through in your very body. Ember dwarves are often erroneously called half-azer because of their appearance. They have dark, ashen skin, with fiery red or orange hair. When they access the fiery power latent within them, their hair transforms into bright vibrant flames that don't burn them or their equipment. They usually have orange, yellow, or red eyes dotted with ashen flecks of black."

def level0(npc): 
    choice = choose("Choose one: ", ['DEX','WIS'])
    if choice == 'DEX': npc.DEX += 1
    else npc.WIS += 1

    npc.type = 'humanoid/elemental'
    npc.traits.append("***Elemental Hybrid.*** You have two creature types: humanoid (dwarf) and elemental (fire). You can be affected by a game effect if it works on either of your creature types.")

    npc.damageresistances.append('fire')

    npc.defer(lambda npc: npc.actions.append("***Heated Body (Recharges on short or long rest).*** When a creature starts its turn while it is grappling you or you are grappling it, you may choose to deal it {npc.proficiencybonus()} fire damage.") )

    npc.speed['walking'] = 30
```
