# Arcane Tradition: Bloodmancer
Blood mages learn to heighten their spellcraft by uniting the power of blood and arcane might. Blood is life, and wizards that travel this path of magic view the sanguine fluid flowing through their veins--and others' veins--as a wellspring of arcane power.

Because of the historical proclivities of bloodmancers, blood magic is a dark secret, and shunned by polite society. Open practitioners of blood magic are openly disliked or hated (at best), jailed, or immediately hunted and killed. Those who practice it must usually do so in secret, and take apprentices for one of two reasons: to pass on the knowledge to the next generation, or to have a ready supply of blood.

```
name = 'Bloodmancer'
description = "***Arcane Tradition: Bloodmancer.*** Blood mages learn to heighten their spellcraft by uniting the power of blood and arcane might. Blood is life, and wizards that travel this path of magic view the sanguine fluid flowing through their veins--and others' veins--as a wellspring of arcane power."
```

## Blood Savant
*2nd-level Bloodmancer feature*

You combine the source of your arcane power with the blood flowing through your veins. You gain proficiency in Medicine and double your proficiency bonus to any check made with the skill, instead of your normal proficiency bonus.

Furthermore, when you perform the Arcane Recovery feature, you also regain 1 expended hit die.

```
def level2(npc):
    npc.expertises.append('Medicine')
    npc.defer(lambda npc: replace("***Arcane Recovery.***", npc.traits, f" Once per day when you finish a short rest, you can regain 1 expended hit die and choose expended spell slots to recover. The spell slots can have a combined level of {((npc.levels('Wizard') + 1) // 2)}, and none of the slots can be 6th level or higher.") )
```

## Blood Magic
*2nd-level Bloodmancer feature*

You invoke blood magic to gain supernatural powers. 

**Blood Pool.** You have a number of blood points determined by your wizard level. You can have more blood points than shown on the table for your level. These points automatically regenerate after a long rest.

Level | Blood Points
----- | ------------
2-4   | 2
5-8   | 3
9-12  | 4
13-16 | 5
17-20 | 6

Additionally, you can use a bonus action to call upon the power of blood by either inflicting a minor or severe wound upon yourself.

**Minor Wound.** Inflicting a minor wound requires the expenditure of 1 hit die. Instead of regaining hit points, you gain 1 blood point.

**Severe Wound.** Inflicting a severe wound requires the expenditure of 2 hit dice. Instead of regaining hit points, you gain 2 blood points.

Willing creatures can offer up their blood, so long as they are within 5 feet of you when you perform the bonus action. Charmed creatures will always be willing, and the expenditure of hit dice does not count as "damage" or an "attack" for purposes of ending the charmed effect.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Blood Magic.*** You call upon the power of blood by either inflicting a minor (expend 1 hit die, gain {'1 blood point' if npc.levels('Wizard') < 14 else '2 blood points'}) or severe wound (expend 2 hit dice, gain {'2' if npc.levels('Wizard') < 14 else '4'} blood points) upon yourself or upon a willing creature within 5 feet of you. Charmed creatures will always be willing, and the expenditure of hit dice does not count as damage or an attack for purposes of ending the charmed effect.") )
```

## Blood Effect
*2nd-level Bloodmancer feature*

While you possess one or more blood points, you gain the following features:

* **Armor of Vitality.** When you do not wear armor, your AC equals 13 + your Constitution modifier.

* **Lifeblood.** You gain advantage on your first death saving throw of the day.

```
    def assignac(npc):
        npc.armorclass['Blood Magic'] = 13 + npc.CONbonus()
    npc.defer(lambda npc: assignac(npc) )
    npc.defer(lambda npc: npc.traits.append(f"***Blood Magic: Armor of Vitality.*** While you possess one or more blood points, and you do not wear armor, your AC is {13 + npc.CONbonus()}.") )
    npc.defer(lambda npc: npc.traits.append(f"***Blood Magic: Lifeblood.*** While you possess one or more blood points, you gain advantage on your death saving throws.") )
```

Furthermore, as a bonus action you can expend blood points to perform the following blood effects:

* **Blood Agony.** When you hit a creature with a melee or spell attack, you can expend 1 or more blood points to deal psychic damage to the target, in addition to the damage of the attack. The extra damage is 1d6 for 1 blood point, plus 1d6 for each additional blood point, to a maximum of 5d6.
    At 14th level, increase the damage die of Blood Agony to a d8.

* **Blood Sense.** The sound of blood pumping in the veins of the living registers upon your senses like a soothing rhythm upon your being. Expend 1 blood point as an action to focus your awareness upon the immediate area to reveal the presence of living creatures. Until the end of your next turn, you know the location of any beast, giant, or humanoid, within 60 feet that is not behind total cover. You know the type (humanoid, fey, beast, etc) of any being whose presence you sense, but not the identity of the creature. Constructs and undead will not register on your Blood Sense.

* **Fortitude of Blood.** Expend 1 blood point as a bonus action to gain a bonus to Constitution saving throws, which lasts for 1 minute, equal to your Intelligence modifier (minimum of +1). You can invoke this ritual twice. Afterward, you cannot perform it again until you finish a short or long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Blood Magic: Blood Agony.*** When you hit a creature with a melee or spell attack, you expend 1 or more blood points to deal psychic damage to the target, in addition to the damage of the attack. The extra damage is 1{'d6' if npc.levels('Wizard') < 14 else 'd8'} for 1 blood point, plus 1{'d6' if npc.levels('Wizard') < 14 else 'd8'} for each additional blood point, to a maximum of 5{'d6' if npc.levels('Wizard') < 14 else 'd8'}.") )
    npc.bonusactions.append("***Blood Magic: Blood Sense.*** Expend 1 blood point as an action to focus your awareness upon the immediate area to reveal the presence of living creatures. Until the end of your next turn, you know the location of any beast, giant, or humanoid, within 60 feet that is not behind total cover. You know the type of any being whose presence you sense, but not the identity of the creature.")
    npc.defer(lambda npc: npc.bonusactions.append("***Blood Magic: Fortitude of Blood (2/Recharges on short or long rest).*** Expend 1 blood point as a bonus action to gain a +{npc.INTbonus()} bonus to Constitution saving throws, which lasts for 1 minute. You can invoke this ritual twice. Afterward, you cannot perform it again until you finish a short or long rest.") )
```

## Burn the Blood
*6th-level Bloodmancer feature*

You gain resistance to psychic and fire damage. Furthermore, whenever you begin casting a spell of 1st level or higher that deals psychic or fire damage, a wave of pain and anguish erupts from you. This wave causes creatures of your choice within 10 feet to suffer psychic or fire damage (you choose each time you activate this feature) equal to half your wizard level.

```
def level6(npc):
    npc.damageresistances.append('psychic')
    npc.damageresistances.append('fire')
    npc.traits.append("***Burn the Blood.*** Whenever you begin casting a spell of 1st level or higher that deals psychic or fire damage, a wave of pain and anguish erupts from you. This wave causes creatures of your choice within 10 feet to suffer psychic or fire damage (you choose each time you activate this feature) equal to half your wizard level.")
```

## Cull the Blood
*6th-level Bloodmancer feature*

You learn to manipulate the flow blood, even if it is not your own, to either stem death or empower your blood magic.

* **Blood Siphon.** When you reduce a creature to 0 hit points with a melee or spell attack, you gain 1 blood point. Similarly, if a creature within 10 feet of you is reduced to 0 hit points, you gain 1 blood point.

* **Mark of Blood.** When an attack scores a critical hit against a living creature within 10 feet, you can spend 1 blood point as a reaction. Until the end of your next turn, you gain advantage on attack rolls against the creature.

* **Wellspring of Life.** When you make a death saving throw and roll a 19-20 on the d20, you regain 1d6 hit points instead of normal. At 14th level, you regain 1d6 hits points when you instead roll a 18-20 on a death saving throw.

```
    npc.traits.append("***Blood Siphon.*** When you reduce a creature to 0 hit points with a melee or spell attack, you gain 1 blood point. Similarly, if a creature within 10 feet of you is reduced to 0 hit points, you gain 1 blood point.")
    
    npc.reactions.append("***Mark of Blood.*** When an attack scores a critical hit against a living creature within 10 feet, you spend 1 blood point. Until the end of your next turn, you gain advantage on attack rolls against the creature.")
    
    npc.defer(lambda npc: npc.traits.append(f"***Wellspring of Life.*** When you make a death saving throw and roll a {'19' if npc.levels('Wizard') < 14 else '18'}-20 on the d20, you regain 1d6 hit points instead of normal.") )
```

## Inheritor of Blood
*10th-level Bloodmancer feature*

You can invoke the power of blood in others to bind your wounds. Should you drop to 0 hit points and do not die outright, you can make a DC 10 Constitution saving throw. If you succeed, one willing creature within 30 feet can expend one hit die and you regain a number of hit points equal to the result.

Each time you use this feature after the first, increase the DC by 5. When you finish a short or long rest, reset the DC to 10.

```
def level10(npc):
    npc.traits.append("***Inheritor of Blood.*** Should you drop to 0 hit points and do not die outright, you can make a DC 10 Constitution saving throw. If you succeed, one willing creature within 30 feet can expend one hit die and you regain a number of hit points equal to the result. Each time you use this feature after the first, increase the DC by 5. When you finish a short or long rest, reset the DC to 10.")
```

## Soul Burn
*10th-level Bloodmancer feature*

You can transform the blood within your veins into raw arcane power. As a bonus action on your turn, expend one or more blood points to create one spell slot. For each blood point you expend, roll 1d6 and consult the following Creating Spell Slots table for the result. You cannot create a spell slot higher than 5th level.

Result | Spell Slot Gained
------ | -----------
7-9    | 1st 
10-16  | 2nd
17-20  | 3rd
21-23  | 4th
24+    | 5th

```
    npc.bonusactions.append("***Soul Burn.*** Expend one or more blood points to create one spell slot. For each blood point you expend, roll 1d6: 7-9 1st; 10-16 2nd; 17-20 3rd; 21-23 4th; 24+ 5th.")
```

## Blood Soul Magus
*14th-level Bloodmancer feature*

You learned the final secret of weaving blood and raw arcane power into one source of magic. When you inflict a minor or severe wound through your Blood Magic feature, you gain a greater number of blood points. When you inflict a minor wound, instead gain 2 blood points, while a severe wound yields 4 blood points.
