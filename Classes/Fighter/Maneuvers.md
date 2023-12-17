# Fighter Martial techniques: Maneuvers
Maneuvers are available to [Battle Master](BattleMaster.md)s and to characters who have the Superior Technique [fighting style](Styles.md) or the Martial Adept [feat](../Feats.md).

***Saving Throws.*** Some of your maneuvers require your target to make a saving throw to resist the maneuver's effects. The saving throw DC is calculated as follows:

**Maneuver save DC** = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice)

***Superiority Dice.*** The study of maneuvers will grant one or more superiority dice; a superiority die is expended when you use it. You regain all of your expended superiority dice when you finish a short or long rest.

### Ambush
When you make a Dexterity (Stealth) check or an initiative roll, you can expend one superiority die and add the die to the roll, provided you aren't incapacitated.

```
def ambush(npc):
    npc.traits.append("***Maneuver: Ambush.*** When you make a Dexterity (Stealth) check or an initiative roll, you can expend one superiority die and add the die to the roll, provided you aren't incapacitated.")
```

### Bait and Switch
When you're within 5 feet of a creature on your turn, you can expend one superiority die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is willing and isn't incapacitated. This movement doesn't provoke opportunity attacks.

Roll the superiority die. Until the start of your next turn, you or the other creature (your choice) gains a bonus to AC equal to the number rolled. 

```
def baitandswitch(npc):
    npc.traits.append("***Maneuver: Bait and Switch.*** When you're within 5 feet of a creature on your turn, you can expend one superiority die and switch places with that creature, provided you spend at least 5 feet of movement and the creature is willing and isn't incapacitated. This movement doesn't provoke opportunity attacks. Roll the superiority die. Until the start of your next turn, you or the other creature (your choice) gains a bonus to AC equal to the number rolled.")
```

### Brace
When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the superiority die to the weapon's damage roll. 

```
def brace(npc):
    npc.traits.append("***Maneuver: Brace.*** When a creature you can see moves into the reach you have with the melee weapon you're wielding, you can use your reaction to expend one superiority die and make one attack against the creature, using that weapon. If the attack hits, add the superiority die to the weapon's damage roll.")
```

### Commander's Strike
When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.

```
def commanderstrike(npc):
    npc.bonusactions.append("***Maneuver: Commander's Strike.*** When you take the Attack action on your turn, you can forgo one of your attacks and use a bonus action to direct one of your companions to strike. When you do so, choose a friendly creature who can see or hear you and expend one superiority die. That creature can immediately use its reaction to make one weapon attack, adding the superiority die to the attack's damage roll.")
```

### Commanding Presence
When you make a Charisma (Intimidation), a Charisma (Performance), or a Charisma (Persuasion) check, you can expend one superiority die and add the superiority die to the ability check.

```
def commandingpresence(npc):
    npc.traits.append("***Maneuver: Commanding Presence.*** When you make a Charisma (Intimidation), a Charisma (Performance), or a Charisma (Persuasion) check, you can expend one superiority die and add the superiority die to the ability check.")
```

### Disarming Attack 
When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it's holding. You add the superiority die to the attack's damage roll, and the target must make a Strength saving throw. On a failed save, it drops the object you choose. The object lands at its feet.

```
def disarmingattack(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Maneuver: Disarming Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to attempt to disarm the target, forcing it to drop one item of your choice that it's holding. You add the superiority die to the attack's damage roll, and the target must make a Strength saving throw (DC {8 + npc.proficiencybonus() + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}). On a failed save, it drops the object you choose. The object lands at its feet.") )
```

### Distracting Strike
When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack's damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn.

```
def distractingstrike(npc):
    npc.traits.append("***Maneuver: Distracting Strike.*** When you hit a creature with a weapon attack, you can expend one superiority die to distract the creature, giving your allies an opening. You add the superiority die to the attack's damage roll. The next attack roll against the target by an attacker other than you has advantage if the attack is made before the start of your next turn.")
```

### Evasive Footwork
When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving.

```
def evasivefootwork(npc):
    npc.traits.append("***Maneuver: Evasive Footwork.*** When you move, you can expend one superiority die, rolling the die and adding the number rolled to your AC until you stop moving.")
```

### Feinting Attack
You can expend one superiority die and use a bonus action on your turn to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature this turn. If that attack hits, add the superiority die to the attack's damage roll.

```
def feintingattack(npc):
    npc.bonusactions.append("***Maneuver: Feinting Attack.*** You can expend one superiority die to feint, choosing one creature within 5 feet of you as your target. You have advantage on your next attack roll against that creature this turn. If that attack hits, add the superiority die to the attack's damage roll.")
```

### Goading Attack
When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.

```
def goadingattack(npc):
    npc.traits.append("***Maneuver: Goading Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to attempt to goad the target into attacking you. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, the target has disadvantage on all attack rolls against targets other than you until the end of your next turn.")
```

### Grappling Strike
Immediately after you hit a creature with a melee attack on your turn, you can expend one superiority die and then try to grapple the target as a bonus action. Add the superiority die to your Strength (Athletics) check.

```
def grapplingstrike(npc):
    npc.bonusactions.append("***Maneuver: Grappling Strike.*** Immediately after you hit a creature with a melee attack on your turn, you can expend one superiority die and then try to grapple the target as a bonus action. Add the superiority die to your Strength (Athletics) check.")
```

### Lunging Attack
When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack's damage roll.

```
def lungingattack(npc):
    npc.traits.append("***Maneuver: Lunging Attack.*** When you make a melee weapon attack on your turn, you can expend one superiority die to increase your reach for that attack by 5 feet. If you hit, you add the superiority die to the attack's damage roll.")
```

### Maneuvering Attack
When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack's damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack.

```
def maneuveringattack(npc):
    npc.traits.append("***Maneuver: Maneuvering Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to maneuver one of your comrades into a more advantageous position. You add the superiority die to the attack's damage roll, and you choose a friendly creature who can see or hear you. That creature can use its reaction to move up to half its speed without provoking opportunity attacks from the target of your attack.")
```

### Menacing Attack
When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw. On a failed save, it is frightened of you until the end of your next turn.

```
def menacingattack(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Maneuver: Menacing Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to attempt to frighten the target. You add the superiority die to the attack's damage roll, and the target must make a Wisdom saving throw (DC {8 + npc.proficiencybonus() + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}). On a failed save, it is frightened of you until the end of your next turn.") )
```

### Parry
When another creature damages you with a melee attack, you can use your reaction and expend one superiority die to reduce the damage by the number you roll on your superiority die + your Dexterity modifier.

```
def parry(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Maneuver: Parry.*** When another creature damages you with a melee attack, you can expend one superiority die to reduce the damage by the number you roll on your superiority die + {npc.DEXbonus()}.") )
```

### Precision Attack
When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied.

```
def precisionattack(npc):
    npc.traits.append("***Maneuver: Precision Attack.*** When you make a weapon attack roll against a creature, you can expend one superiority die to add it to the roll. You can use this maneuver before or after making the attack roll, but before any effects of the attack are applied.")
```

### Pushing Attack
When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you push the target up to 15 feet away from you.

```
def pushingattack(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Maneuver: Pushing Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to attempt to drive the target back. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw (DC {8 + npc.proficiencybonus() + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}). On a failed save, you push the target up to 15 feet away from you.") )
```

### Quick Toss
As a bonus action, you can expend one superiority die and make a ranged attack with a weapon that has the thrown property. You can draw the weapon as part of making this attack. If you hit, add the superiority die to the weapon's damage roll. 

```
def quicktoss(npc):
    npc.bonusactions.append("***Maneuver: Quick Toss.*** You can expend one superiority die and make a ranged attack with a weapon that has the thrown property. You can draw the weapon as part of making this attack. If you hit, add the superiority die to the weapon's damage roll.")
```

### Rally
On your turn, you can use a bonus action and expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the superiority die roll + your Charisma modifier.

```
def rally(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Maneuver: Rally.*** On your turn, you can expend one superiority die to bolster the resolve of one of your companions. When you do so, choose a friendly creature who can see or hear you. That creature gains temporary hit points equal to the superiority die roll + {npc.CHAbonus()}.") )
```

### Restraining Strike
Immediately after you hit a creature with a melee weapon attack on your turn, you can expend one superiority die and use a bonus action to grapple the target (see chapter 9 in the Player's Handbook for rules on grappling). Add the superiority die to your Strength (Athletics) check. The target is also restrained while grappled in this way.

```
def restrainingstrike(npc):
    npc.bonusactions.append("***Maneuver: Restraining Strike.*** Immediately after you hit a creature with a melee weapon attack on your turn, you expend one superiority die and grapple the target. Add the superiority die to your Strength (Athletics) check. The target is also restrained while grappled in this way.")
```

### Riposte
When a creature misses you with a melee attack, you can use your reaction and expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack's damage roll.

```
def riposte(npc):
    npc.reactions.append("***Maneuver: Riposte.*** When a creature misses you with a melee attack, you expend one superiority die to make a melee weapon attack against the creature. If you hit, you add the superiority die to the attack's damage roll.")
```

### Silver Tongue
When you make a Charisma (Deception) check or a Charisma (Persuasion) check, you can expend one superiority die, and add the superiority die to the ability check.

```
def silvertongue(npc):
    npc.traits.append("***Maneuver: Silver Tongue.*** When you make a Charisma (Deception) check or a Charisma (Persuasion) check, you can expend one superiority die, and add the superiority die to the ability check.")
```

### Snipe
As a bonus action, you can expend one superiority die and make a ranged weapon attack. You can draw a thrown weapon as part of making this attack. If you hit, add the superiority die to the attack's damage roll.

```
def snipe(npc):
    npc.bonusactions.append("***Maneuver: Snipe.*** You can expend one superiority die and make a ranged weapon attack. You can draw a thrown weapon as part of making this attack. If you hit, add the superiority die to the attack's damage roll.")
```

### Studious Eye
When you make a Wisdom (Insight) check or an Intelligence (Investigation) check, you can expend one superiority die, and add the superiority die to the ability check.

```
def studiouseye(npc):
    npc.traits.append("***Maneuver: Studious Eye.*** When you make a Wisdom (Insight) check or an Intelligence (Investigation) check, you can expend one superiority die, and add the superiority die to the ability check.")
```

### Sweeping Attack
When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack.

```
def sweepingattack(npc):
    npc.traits.append("***Maneuver: Sweeping Attack.*** When you hit a creature with a melee weapon attack, you can expend one superiority die to attempt to damage another creature with the same attack. Choose another creature within 5 feet of the original target and within your reach. If the original attack roll would hit the second creature, it takes damage equal to the number you roll on your superiority die. The damage is of the same type dealt by the original attack.")
```

### Tactical Assessment
When you make an Intelligence (Investigation), an Intelligence (History), or a Wisdom (Insight) check, you can expend one superiority die and add the superiority die to the ability check.

```
def tacticalassessment(npc):
    npc.traits.append("***Maneuver: Tactical Assessment.*** When you make an Intelligence (Investigation), an Intelligence (History), or a Wisdom (Insight) check, you can expend one superiority die and add the superiority die to the ability check.")
```


### Trip Attack
When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw. On a failed save, you knock the target prone.

```
def tripattack(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Maneuver: Trip Attack.*** When you hit a creature with a weapon attack, you can expend one superiority die to attempt to knock the target down. You add the superiority die to the attack's damage roll, and if the target is Large or smaller, it must make a Strength saving throw (DC {8 + npc.proficiencybonus() + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}). On a failed save, you knock the target prone.") )
```


```
maneuvers = {
    'Ambush': ambush,
    'Bait and Switch': baitandswitch,
    'Brace': brace,
    "Commander's Strike": commanderstrike,
    'Commanding Presence': commandingpresence,
    'Disarming Attack': disarmingattack,
    'Distracting Strike': distractingstrike,
    'Evasive Footwork': evasivefootwork,
    'Feinting Attack': feintingattack,
    'Goading Attack': goadingattack,
    'Grappling Strike': grapplingstrike,
    'Lunging Attack': lungingattack,
    'Maneuvering Attack': maneuveringattack,
    'Menacing Attack': menacingattack,
    'Parry': parry,
    'Precision Attack': precisionattack,
    'Pushing Attack': pushingattack,
    'Quick Toss': quicktoss,
    'Rally': rally,
    'Restraining Strike': restrainingstrike,
    'Riposte': riposte,
    'Silver Tongue': silvertongue,
    'Snipe': snipe,
    'Studious Eye': studiouseye,
    'Sweeping Attack': sweepingattack,
    'Tactical Assessment': tacticalassessment,
    'Trip Attack': tripattack
}
def choosemaneuver(npc, dice = None, dicetype = None):
    if getattr(npc, "fightingmaneuvers", None) == None:
        npc.fightingmaneuvers = []
        npc.superioritydice = 4 if dice == None else dice
        npc.superioritydicetype = 'd8' if dicetype == None else dicetype

        npc.defer(lambda npc: npc.traits.append(f"***Superiority Dice (Recharges on short or long rest).*** You have {npc.superioritydice} {npc.superioritydicetype} superiority dice that can be used for your fighting maneuvers. You currently know the following maneuvers: " + ",".join(npc.fightingmaneuvers) + "."))

    avail = {}
    for manname in maneuvers:
        if manname not in npc.fightingmaneuvers:
            avail[manname] = maneuvers[manname]

    (manname, manfn) = choose("Choose a Fighting Maneuver: ", avail)
    npc.fightingmaneuvers.append(manname)
    manfn(npc)

allclasses['Fighter'].choosemaneuver = choosemaneuver
```
