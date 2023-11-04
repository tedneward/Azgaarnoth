# Roguish Archetype: Soulknife
Most assassins strike with physical weapons, and many burglars and spies use thieves' tools to infiltrate secure locations, whereas a Soulknife strikes and infiltrates with the mind, cutting through barriers both physical and psychic. These rogues discover psionic power within themselves and channel it to do their roguish work. 

Soulknives find easy employment as members of Rogues' guilds, though they are often mistrusted by rogues who are leery of anyone using strange mind powers to conduct their business, and most governments would be happy to employ a Soulknife as a spy. It is rumored that the [Order of the Copper Dragon](../../Organizations/DraconicOrder/Copper.md) employs a number of Soulknife Rogues as part of their vast intelligence network, as well. Amid the trees of ancient forests on the Material Plane and in the Feywild, some wood elves walk the path of the Soulknife, serving as silent, lethal guardians of their woods. In the endless war among the gith, a githzerai is encouraged to become a Soulknife when stealth is required against the githyanki foe. Rumors persist of a Rogues' Guild of assassins that seek to bring all of the Soulknives in the world under their control (or at least within their influence).

As a Soulknife, your psionic abilities might have haunted you since you were a child, only revealing their potential as you experienced the stress of adventure. Or you might have sought out a reclusive order of psionic adepts and spent years learning how to manifest your power.

```
name = 'Soulknife'
description = "***Roguish Archetype: Soulknife.*** Most assassins strike with physical weapons, and many burglars and spies use thieves' tools to infiltrate secure locations, whereas a Soulknife strikes and infiltrates with the mind, cutting through barriers both physical and psychic. These rogues discover psionic power within themselves and channel it to do their roguish work."
```

## Psionic Talent
*3rd-level Soulknife feature*

You harbor a wellspring of psionic power within yourself, an energy that ebbs and flows as you channel it in various ways. This power is represented by your Psionic Talent die, the starting size of which is a d6.

***Psionic Talent Options.*** You can use your Psionic Talent die in the following ways:

* **Psi-Bolstered Knack**. When your non-psionic training fails you, you can tap into your psionic power to help: if you fail an ability check using a skill or tool with which you have proficiency, you can roll your Psionic Talent die and add the number rolled to the check, potentially turning failure into success.
* **Psychic Whispers**. You can use your psychic abilities to establish telepathic communication between yourself and others--perfect for quiet infiltration. As an action, you give yourself and at least one other creature the ability to speak telepathically with each other. When you do so, roll your Psionic Talent die, and choose creatures you can see, up to a number of creatures equal to the number rolled. For 1 hour, the chosen creatures can speak telepathically with you, and you can speak telepathically with them. To send or receive a message (no action required), you and the other creature must be within 1 mile of each other. A creature can't use this telepathy if it can't speak any languages, and a creature can end the telepathic connection at any time (no action required). You and the creature don't need to speak a common language to understand each other.

***Changing the Die's Size.*** If you roll the highest number on your Psionic Talent die, it decreases by one die size after the roll. This represents you burning through your psionic energy. For example, if the die is a d6 and you roll a 6, it becomes a d4. If it's a d4 and you roll a 4, it becomes unusable until you finish a long rest.

Conversely, if you roll a 1 on your Psionic Talent die, it increases by one die size after the roll, up to its starting size. This represents you conserving psionic energy for later use. For example, if you roll a 1 on a d4, the die then becomes a d6.

Whenever you finish a long rest, your Psionic Talent die resets to its starting size. When you reach certain levels in this class, the starting size of your Psionic Talent die increases: at 5th level (d8), 11th level (d10), and 17th level (d12).

***Psi Replenishment.*** As a bonus action, you can calm your mind for a moment and restore your Psionic Talent die to its starting size. You then can't use Psi Replenishment again until you finish a long rest.

```
def level3(npc):
    npc.psionicdie = 'd0'

    def setpsidice(npc): 
        npc.psionicdie = 'd6' if npc.levels('Rogue') < 5 else 'd8' if npc.levels('Rogue') < 11 else 'd10' if npc.levels('Rogue') < 17 else 'd12'
    npc.defer(lambda npc: setpsidice(npc) )

    npc.defer(lambda npc: npc.traits.append(f"***Psionic Talent (Recharges on long rest).*** Your Psionic Talent die starts as a {npc.psionicdie}. If you roll the highest number on your Psionic Talent die, it decreases by one die size after the roll. Conversely, if you roll a 1 on your Psionic Talent die, it increases by one die size after the roll, up to its starting size. Whenever you finish a long rest, your Psionic Talent die resets to its starting size."))

    npc.traits.append("***Psi-Bolstered Knack.*** When your non-psionic training fails you, you can tap into your psionic power to help: if you fail an ability check using a skill or tool with which you have proficiency, you can roll your Psionic Talent die and add the number rolled to the check, potentially turning failure into success.")

    npc.traits.append("***Psychic Whispers.*** You can use your psychic abilities to establish telepathic communication between yourself and others--perfect for quiet infiltration. As an action, you give yourself and at least one other creature the ability to speak telepathically with each other. When you do so, roll your Psionic Talent die, and choose creatures you can see, up to a number of creatures equal to the number rolled. For 1 hour, the chosen creatures can speak telepathically with you, and you can speak telepathically with them. To send or receive a message (no action required), you and the other creature must be within 1 mile of each other. A creature can't use this telepathy if it can't speak any languages, and a creature can end the telepathic connection at any time (no action required). You and the creature don't need to speak a common language to understand each other.")
```

## Psychic Blades
*3rd-level Soulknife feature*

You can manifest your psionic power as shimmering blades of psychic energy. When you are about to make a melee or ranged weapon attack against a creature, you can manifest a psychic blade from your free hand and make the attack with that blade. This magic blade is a simple melee weapon with the finesse and thrown properties. It has a normal range of 60 feet and no long range, and on a hit, it deals psychic damage equal to 1d6 plus the ability modifier you used for the attack roll. The blade vanishes immediately after it hits or misses its target, and it leaves no mark on its target if it deals damage.

After you attack with the blade, you can make a melee or ranged weapon attack with a second psychic blade as a bonus action on the same turn, provided your other hand is free to create it. The damage die of this bonus attack is 1d4, instead of 1d6.

```
    npc.defer(lambda npc: npc.actions.append(f"***Psychic Blade.*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5ft., one target. Hit: 1d6 + {npc.STRbonus()} psychic damage. The blade vanishes immediately after it hits or misses its target, and it leaves no mark on its target if it deals damage. After you attack with the blade, you can make a melee or ranged weapon attack with a second psychic blade as a bonus action on the same turn, provided your other hand is free to create it."))

    npc.defer(lambda npc: npc.actions.append(f"***Psychic Blade (Thrown).*** Ranged Weapon Attack: +{npc.proficiencybonus() + npc.DEXbonus()} to hit, Range 20/60, one target. Hit: 1d6 + {npc.DEXbonus()} psychic damage. The blade vanishes immediately after it hits or misses its target, and it leaves no mark on its target if it deals damage. After you attack with the blade, you can make a melee or ranged weapon attack with a second psychic blade as a bonus action on the same turn, provided your other hand is free to create it."))

    npc.defer(lambda npc: npc.bonusactions.append(f"***Psychic Blade.*** Melee Weapon Attack: +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5ft., one target. Hit: 1d4 + {npc.STRbonus()} psychic damage"))

    npc.defer(lambda npc: npc.bonusactions.append(f"***Psychic Blade (Thrown).*** Ranged Weapon Attack: +{npc.proficiencybonus() + npc.DEXbonus()} to hit, Range 20/60, one target. Hit: 1d4 + {npc.DEXbonus()} psychic damage"))
```

## Soul Blades
*9th-level Soulknife feature*

Your Psychic Blades are now an expression of your psi-suffused soul, giving you finer control over them in the following ways:

* **Homing Strikes**. If you make an attack roll with your Psychic Blades and miss the target, you can roll your Psionic Talent die and add the number rolled to the attack roll. If this causes the attack to hit, your Psionic Talent die decreases by one die size, regardless of the number rolled.
* **Psychic Teleportation**. If your Psionic Talent die is available, you can hurl your Psychic Blades to magically transport yourself to another location. As a bonus action, you manifest one of your Psychic Blades and throw it at an unoccupied space you can see, up to a number of feet away equal to 5 times the highest number on your Psionic Talent die. You then teleport to that space, the blade vanishes, and your Psionic Talent die decreases by one die size.

```
def level9(npc):
    npc.traits.append("***Homing Strikes.*** If you make an attack roll with your Psychic Blades and miss the target, you can roll your Psionic Talent die and add the number rolled to the attack roll. If this causes the attack to hit, your Psionic Talent die decreases by one die size, regardless of the number rolled.")

    npc.bonusactions.append("***Psychic Teleportation.*** If your Psionic Talent die is available, you can hurl your Psychic Blades to magically transport yourself to another location by manifesting one of your Psychic Blades and throwing it at an unoccupied space you can see, up to a number of feet away equal to 5 times the highest number on your Psionic Talent die. You then teleport to that space, the blade vanishes, and your Psionic Talent die decreases by one die size.")
```

## Psionic Veil
*13th-level Soulknife feature*

You can weave a veil of psychic static to mask yourself. As an action, you can magically become invisible, along with anything you are wearing or carrying, for 10 minutes or until you dismiss this effect (no action required). This invisibility ends if you deal damage to a creature or if you force a creature to make a saving throw.

Once you use this feature, you can't do so again until you finish a long rest, unless you decrease your Psionic Talent die by one die size to use this feature again.

```
def level13(npc):
    npc.actions.append("***Psionic Veil (Recharges on long rest or decreased Psionic Talent die).*** You can magically become invisible, along with anything you are wearing or carrying, for 10 minutes or until you dismiss this effect (no action required). This invisibility ends if you deal damage to a creature or if you force a creature to make a saving throw.")
```

## Rend Mind
*17th-level Soulknife feature*

You can sweep your Psychic Blades directly through a creature's mind. When you use your Psychic Blades to deal Sneak Attack damage to a creature, you can force that target to make a Wisdom saving throw (DC equal to 8 + your proficiency bonus + your Dexterity modifier). Unless the save succeeds, the target is stunned until the end of your next turn.

Once you use this feature, you can't do so again until you finish a long rest, unless you decrease your Psionic Talent die by one die size to use this feature again.

```
def level17(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Rend Mind (Recharges on long rest or decreased Psionic Talent die).*** When you use your Psychic Blades to deal Sneak Attack damage to a creature, you can force that target to make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.DEXbonus()}). Unless the save succeeds, the target is stunned until the end of your next turn."))
```
