# Martial Archetype: Ghost Warrior
The Ghost Warrior draws upon the collective wisdom, knowledge, and experience of a choir of ghosts or other ancestral spirits. This choir remains bonded to them, invisible and silent until summoned, offering guidance until the warrior fulfills their destiny or perishes in battle. Such a choir includes ancestral spirits, as well as spirits of former protectors of their clan and legendary warriors slain in combat--and perhaps even an enemy or rival slain by their hand. When the Ghost Warrior needs insight or advice, they listen to these spirits and--if wise--heed their counsel. In those moments where the ghost warrior needs an edge against enemies, they allow one of the spirits to possess their body. When the time comes and the ghost warrior falls, then they become part of another warrior's choir, continuing the cycle of life and death.

The Ghost Warrior is most commonly found among the tribes of Yithi, Zhi, and (increasingly) among the United Hordes.

```
name = 'Ghost Warrior'
description = "***Martial Archetype: Ghost Warrior.*** The Ghost Warrior draws upon the collective wisdom, knowledge, and experience of a choir of ghosts or other ancestral spirits. This choir remains bonded to them, invisible and silent until summoned, offering guidance until the warrior fulfills their destiny or perishes in battle. Such a choir includes ancestral spirits, as well as spirits of former protectors of their clan and legendary warriors slain in combat--and perhaps even an enemy or rival slain by their hand. When the Ghost Warrior needs insight or advice, they listen to these spirits and--if wise--heed their counsel. In those moments where the ghost warrior needs an edge against enemies, they allow one of the spirits to possess their body. When the time comes and the ghost warrior falls, then they become part of another warrior's choir, continuing the cycle of life and death."
```

## Ghostly Choir
*3rd-level Ghost Warrior feature*

You have a collection of spirits known as a choir. These spirits, bound to you until your death, follow and watch over you. In times of danger or stress, you call upon one of these spirits to aid you. Each spirit offers a different benefit, but each demands a sacrifice in exchange for their help.

***Ghosts.*** You gain the services of four ghosts of your choice, which are described below under "Spirits." Each spirit provides a different benefit; some aid your attacks or defenses, while others help you with ability checks or saving throws. You can only benefit from one spirit per attack or action.

Under normal conditions (except as noted below), only you can see your choir or hear their voices. These spirits can, however, be detected by means of detect magic, and can be seen with a  gem of true seeing. The ghosts are not treated as undead or any type of creature--they cannot be attacked, harmed, exorcised, or banished.

Once you've gained a particular spirit's benefit, you cannot call upon that same spirit again until after you've completed a short or long rest.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Ghostly Choir.*** You gain the services of several ghostly spirits. You can only benefit from one spirit per attack or action. Under normal conditions (except as noted), only you can see your choir or hear their voices. These spirits can, however, be detected by means of {spelllinkify('detect magic')}, and can be seen with a *gem of true seeing*. The ghosts are not treated as undead or any type of creature--they cannot be attacked, harmed, exorcised, or banished. Once you've gained a particular spirit's benefit, you cannot call upon that same spirit again until after you've completed a short or long rest. Currently you have a choir consisting of the spirits of " + ",".join(npc.ghosts)))
    npc.ghosts = []
    chooseghost(npc)
    chooseghost(npc)
    chooseghost(npc)
    chooseghost(npc)
```

***Saving Throw.*** Some benefits provided by your ghostly choir call for your target to make a saving throw to avoid or resist the feature's effects. Calculate the saving throw DC as follows:

**Spirit save DC** = 8 + your proficiency bonus + your Wisdom modifier

## The Spirit Path
*3rd-level Ghost Warrior feature*

As long as you have at least one spirit you have not invoked, you gain proficiency in two skills chosen from History, Medicine, Religion, and Survival. If you have called upon all your spirits, you lose this feature until you complete a short or long rest.

```
    skill1 = chooseskill(npc, ['History','Medicine','Religion','Survival'])
    skill2 = chooseskill(npc, ['History','Medicine','Religion','Survival'])
    npc.traits.append("***Spirit Path (Recharges on short or long rest).*** As long as you have at least one spirit you have not invoked, you have proficiency in " + skill1 + " and " + skill2 + ". If you have called upon all your spirits, you lose this feature.")
```

## Ghostly Counsel
*7th-level Ghost Warrior feature*

As a free action you can call upon any one of your spirits to double your proficiency bonus in one skill of your choice, in place of the usual bonus that spirit provides.

```
def level7(npc):
    npc.traits.append("***Ghostly Counsel.*** As a free action you can call upon any one of your spirits to double your proficiency bonus in one skill of your choice, in place of the usual bonus that spirit provides.")
```

## Greater Spirit Choir
*10th-level Ghost Warrior feature*

Add three additional spirits to your choir. At 18th level, you gain an additional three spirits.

```
def level10(npc):
    chooseghost(npc)
    chooseghost(npc)
    chooseghost(npc)

def level18(npc):
    chooseghost(npc)
    chooseghost(npc)
    chooseghost(npc)
```

## Resurgence
*15th-level Ghost Warrior feature*

At 15th level, you regain access to two spirits of your choice if you have no spirits remaining to call upon when you roll initiative.

```
def level15(npc):
    npc.traits.append("***Resurgence.*** You regain access to two spirits of your choice if you have no spirits remaining to call upon when you roll initiative.")
```

# Spirits
When you add a spirit to your choir, select from those described below. Once you select a spirit, you cannot change it. 

When you gain a new fighter level, you can change one of your spirits for another.

***Berserker.*** His rage clouds your mind, blocking your foe's honeyed words. You do not summon this spirit, but rather he appears unbidden. If you fail a saving throw against an effect that imposes the charmed condition, each round thereafter at the beginning of your turn you may reroll the saving throw with advantage. If you succeed, the charm effect ends. If you fail, however, you suffer 1 hit point per level of damage. This feature continues until you break free of the charm or drop to 0 hit points--you cannot voluntarily end this feature.

```
def berserker(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Spirit: Berserker.*** His rage clouds your mind, blocking your foe's honeyed words. You do not summon this spirit, but rather he appears unbidden. If you fail a saving throw against an effect that imposes the charmed condition, each round thereafter at the beginning of your turn you may reroll the saving throw with advantage. If you succeed, the charm effect ends. If you fail, however, you suffer {npc.levels()} hit points of damage. This feature continues until you break free of the charm or drop to 0 hit points--you cannot voluntarily end this feature."))
```

***Butcher.*** She bleeds your enemies of their vitality, granting it to you. You can invoke this spirit as a bonus action. Choose a number of enemies equal to your proficiency bonus that you can see within 30 feet. Each target must make a Constitution saving throw or suffer 2 points of necrotic damage. You regain half of this amount as temporary hit points.

```
def butcher(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Butcher.*** Choose {npc.proficiencybonus()} enemies that you can see within 30 feet. Each target must make a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}) or suffer 2 points of necrotic damage. You regain half of this amount as temporary hit points."))
```

***Coward.*** He teaches you the value of fear and caution. If you take the disengage action to move away from an enemy, your speed increases by half for that round only. Unlike the other spirits, you do not lose the coward feature after using him. Instead, choose one of your other ghostly choir. You instead lose that spirit's feature until you complete a short or long rest.

```
def coward(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Coward.*** If you take the Disengage action to move away from an enemy, your speed increases by half for that round only. Unlike the other spirits, you do not lose the coward feature after using him. Instead, choose one of your other ghostly choir. You instead lose that spirit's feature until you complete a short or long rest."))
```

***Crone.*** She peers a few moments ahead into your future and predicts what might happen. When an effect requires you to make a saving throw, as a reaction you can draw on this spirit and have advantage on that saving throw. If you cannot take a reaction, you cannot call upon the crone.

```
def crone(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Spirit: Crone.*** When an effect requires you to make a saving throw, you can draw on this spirit and have advantage on that saving throw. If you cannot take a reaction, you cannot call upon the crone."))
```

***Fallen Hero.*** He bolsters your reserves and helps you overcome hopeless odds. When an attack would drop you to 0 hit points, as a reaction you can summon this spirit. You remain at 1 hit point, standing and conscious. If you take further damage that drops you to 0 hit points, you fall unconscious.

```
def fallenhero(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Spirit: Fallen Hero.*** He bolsters your reserves and helps you overcome hopeless odds. When an attack would drop you to 0 hit points, you can summon this spirit. You remain at 1 hit point, standing and conscious. If you take further damage that drops you to 0 hit points, you fall unconscious."))
```

***Healer.*** Her gentle touch alleviates pain and staunches wounds. When you invoke the healer as an action, you may expend a number of your available recovery hit dice equal to 1 plus 1 additional die per five levels, as part of that action. Alternatively, you can ask the spirit to infuse one of your allies within 30 feet that you can see with the benefits of one of your recovery dice.

```
def healer(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Healer.*** You may expend {1 + (npc.levels('Fighter') // 5)} of your available recovery hit dice. Alternatively, you can ask the spirit to infuse one of your allies within 30 feet that you can see with the benefits of one of your recovery dice."))
```

***Hunter.*** This spirit guides your step, allowing you to move stealthily. Invoke this spirit as a bonus action to gain advantage on your next Dexterity (Stealth) check.

```
def hunter(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Hunter.*** Gain advantage on your next Dexterity (Stealth) check."))
```

***Mentor.*** He goads, cajoles, and pushes you beyond your limits. Invoke this spirit as a bonus action to gain advantage on your next Strength, Constitution, Intelligence, or Wisdom ability check.

```
def mentor(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Mentor.*** Gain advantage on your next Strength, Constitution, Intelligence, or Wisdom ability check."))
```

***Monster.*** The ghost of a ferocious monster now grudgingly aids your cause. When you invoke the monster as an action, choose a number of enemy creatures within 30 feet that you can see, to a maximum of your proficiency bonus. Each creature must make a Wisdom saving throw or become frightened for a number of rounds equal to your Wisdom modifier (minimum of 1).

```
def monster(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Monster.*** Choose a number of enemy creatures within 30 feet that you can see, to a maximum of {npc.proficiencybonus()}. Each creature must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}) or become frightened for {npc.WISbonus()} rounds."))
```

***Old Hand.*** He tells you what you need to hear after you've suffered a setback. When you call upon this spirit as a bonus action, you can ignore one condition you are suffering, or up to two levels of exhaustion, for a number of rounds equal to your Wisdom modifier (minimum of 1).

```
def oldhand(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Old Hand.*** When you call upon this spirit, you can ignore one condition you are suffering, or up to two levels of exhaustion, for {npc.WISbonus()} rounds."))
```

***Protector.*** If an enemy creature attacks you with advantage because you are surprised, you can draw on this spirit as a reaction to negate that advantage. You are no longer surprised, and the attacker rolls his attack normally.

```
def protector(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Spirit: Protector.*** If an enemy creature attacks you with advantage because you are surprised, you can draw on this spirit as a reaction to negate that advantage. You are no longer surprised, and the attacker rolls his attack normally."))
```

***Rival.*** She infuses your attack with a ferocious burst of power. You invoke this spirit as a bonus action following a successful attack, thereby granting you one additional weapon damage die. The number of bonus damage dice increases to two when you reach 7th level, and then increases to three dice when you reach 14th level.

```
def rival(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Rival.*** You invoke this spirit following a successful attack, thereby granting you {'one' if npc.levels('Fighter') < 7 else 'two' if npc.levels('Fighter') < 14 else 'three'} additional weapon damage {'die' if npc.levels('Fighter') < 7 else 'dice'}."))
```

***Shield-Mate.*** As an action, you summon the shield-mate. They protect your back and guards against threats. A ghostly, flickering image of a shield-bearing warrior appears adjacent to you for a number of rounds equal to your Wisdom modifier (minimum of 1). As long as the ghost remains, treat your armor class as if you wielded a shield.

```
def shieldmate(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Shield-Mate.*** A ghostly, flickering image of a shield-bearing warrior appears adjacent to you for {npc.WISbonus()} rounds. As long as the ghost remains, treat your armor class as if you wielded a shield."))
```

***Skald.*** She teaches you a rousing war cry to rally your comrades. As an action, each ally within 30 feet who can hear you can either automatically succeed at a death saving throw or remove one of the following conditions: charmed, frightened, poisoned, or one level of exhaustion. You gain no benefit from this feature.

```
def skald(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Skald.*** Each ally within 30 feet who can hear you can either automatically succeed at a death saving throw or remove one of the following conditions: charmed, frightened, poisoned, or one level of exhaustion. You gain no benefit from this feature."))
```

***Stag.*** A magnificent, fleet-of-foot stag appears and grants you a burst of speed. When you draw on this spirit, you can take Dash as a bonus action.

```
def stag(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Stag.*** When you draw on this spirit, you can take Dash as a bonus action."))
```

***Steed.*** A spectral horse appears at your side, plainly visible. You can summon your spectral steed as an action. Treat the mount as a riding horse. The mount remains for up to one hour per level, or until you dismiss it as a bonus action, whichever comes first. The mount only has 1 hit point.

```
def steed(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Steed.*** A spectral horse appears at your side, plainly visible. Treat the mount as a riding horse, and it remains for up to {npc.levels('Fighter')} hours, or until you dismiss it as a bonus action, whichever comes first. The mount only has 1 hit point."))
```

***Storyteller.*** Her song or poem inspires you when you need it most. If you summon this spirit as a bonus action, you gain +1d4 temporary hit points. These hit points last for one minute.

```
def storyteller(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Storyteller.*** Her song or poem inspires you; you gain 1d4 temporary hit points for one minute."))
```

***Unbound Slave.*** He grants desperate strength to help you gain freedom. If you are immobilized or restrained, call on this spirit as a bonus action to gain advantage on an ability or skill check to break free of that effect. This spirit cannot aid you against petrification effects.

```
def unboundslave(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Spirit: Unbound Slave.*** Calling on this spirit while you are immobilized or restrained grants advantage on an ability or skill check to break free of that effect. This spirit cannot aid you against petrification effects."))
```

***Vigilant.*** She stands watch you while you rest. You can invoke this spirit as an action. The spirit remains on watch for up to 8 hours, guarding an area as described in the alarm spell. If the vigilant sounds the alarm, only you hear it. 

```
def vigilant(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Spirit: Vigilant.*** She stands watch you while you rest. The spirit remains on watch for up to 8 hours, guarding an area as described in the {spelllinkify('alarm')} spell. If the vigilant sounds the alarm, only you hear it."))
```

```
ghosts = {
    'Berserker': berserker,
    'Butcher': butcher,
    'Coward': coward,
    'Crone': crone,
    'Fallen Hero': fallenhero,
    'Healer': healer,
    'Hunter': hunter,
    'Mentor': mentor,
    'Monster': monster,
    'Old Hand': oldhand,
    'Protector': protector,
    'Rival': rival,
    'Shield-Mate': shieldmate,
    'Skald': skald,
    'Stag': stag,
    'Steed': steed,
    'Storyteller': storyteller,
    'Unbound Slave': unboundslave,
    'Vigilant': vigilant
}
def chooseghost(npc):
    availableghosts = ghosts.copy()

    for (agname, agfn) in ghosts.items():
        if agname in npc.ghosts:
            availableghosts.pop(agname)
    
    ghost = choose("Pick a spirit: ", availableghosts)
    npc.ghosts.append(ghost[0])
    ghost[1](npc)
```
