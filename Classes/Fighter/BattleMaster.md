# Martial Archetype: Battle Master
Those who emulate the archetypal Battle Master employ martial techniques passed down through generations. To a Battle Master, combat is an academic field, sometimes including subjects beyond battle such as weaponsmithing and calligraphy. Not every fighter absorbs the lessons of history, theory, and artistry that are reflected in the Battle Master archetype, but those who do are well-rounded fighters of great skill and knowledge.

Battle mastery is taught almost exclusively at the Great Academy run by the [Order of the Bronze Dragon](../../Organizations/MilitantOrders/DraconicOrder/Bronze.md), but many of its instructors and students have gone on to found much smaller schools or take on apprentices after leaving. Taking this archetype will typically involve spending some amount of time at the Academy or studying under one of its alumni in some fashion. Battle Masters are also found in many of the [Dueling Colleges](../../Organizations/DuelingColleges.md) across Azgaarnoth, and many [Mercenary Companies](../../Organizations/MercCompanies/) provide "field study" for Battle Masters.

```
name = 'Battle Master'
description = "***Martial Archetype: Battle Master.*** Those who emulate the archetypal Battle Master employ martial techniques passed down through generations. To a Battle Master, combat is an academic field, sometimes including subjects beyond battle such as weaponsmithing and calligraphy. Not every fighter absorbs the lessons of history, theory, and artistry that are reflected in the Battle Master archetype, but those who do are well-rounded fighters of great skill and knowledge."
```

## Combat Superiority
*3rd-level Battle Master feature*

You learn maneuvers that are fueled by special dice called superiority dice.

***Maneuvers.*** You learn three maneuvers of your choice. Many maneuvers enhance an attack in some way. You can use only one maneuver per attack. You learn two additional maneuvers of your choice at 7th, 10th, and 15th level. These are listed in [Maneuvers](Maneuvers.md).

***Superiority Dice.*** You have four superiority dice, which are d8s. You gain another superiority die at 7th level and one more at 15th level.

```
def level3(npc):
    npc.superioritydicetype = 'd8'
    npc.superioritydice = 4
    allclasses['Fighter'].choosemaneuver(npc)
    allclasses['Fighter'].choosemaneuver(npc)
    allclasses['Fighter'].choosemaneuver(npc)
```

### Maneuver Versatility
If you know any maneuvers from the above list, you can replace one maneuver you know with a different maneuver whenever you finish a long rest. This change reflects your physical and mental preparation for the day ahead.

## Student of War
*3rd-level Battle Master feature*

You gain proficiency with one type of artisan's tools of your choice.

```
    npc.proficiencies.append(choose("Choose one: ", tools['artisan']))
```

## Know Your Enemy
*7th-level Battle Master feature*

If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice:

* Strength score
* Dexterity score
* Constitution score
* Armor Class
* Current hit points
* Total class levels, if any
* Fighter class levels, if any

```
def level7(npc):
    npc.superioritydice += 1
    allclasses['Fighter'].choosemaneuver(npc)
    allclasses['Fighter'].choosemaneuver(npc)

    npc.traits.append("***Know Your Enemy.*** If you spend at least 1 minute observing or interacting with another creature outside combat, you can learn certain information about its capabilities compared to your own. The DM tells you if the creature is your equal, superior, or inferior in regard to two of the following characteristics of your choice: Strength score; Dexterity score; Constitution score; Armor Class; current hit points; total class levels (if any); fighter class levels (if any)")
```

## Improved Combat Superiority
*10th-level Battle Master feature*

Your superiority dice turn into d10s. At 18th level, they turn into d12s.

```
def level10(npc):
    npc.superioritydicetype = 'd10'
    allclasses['Fighter'].choosemaneuver(npc)
    allclasses['Fighter'].choosemaneuver(npc)

def level18(npc):
    npc.superioritydicetype = 'd12'
```

## Relentless
*15th-level Battle Master feature*

When you roll initiative and have no superiority dice remaining, you regain 1 superiority die.

```
def level15(npc):
    npc.superioritydice += 1
    allclasses['Fighter'].choosemaneuver(npc)
    allclasses['Fighter'].choosemaneuver(npc)

    npc.traits.append("***Relentless.*** When you roll initiative and have no superiority dice remaining, you regain 1 superiority die.")
```

---

### Battle Master Builds
The suite of maneuvers you choose, when combined with a fighting style and feats, allows you to create a broad range of fighters, each with its own flavor and play style. Below are recommendations for how you might build a Battle Master to reflect various types of warriors. Each of these builds contains suggested fighting styles, maneuvers, and feats.

#### Archer
**Fighting Style:** [Archery](Styles.md#archery)

**Maneuvers:** [Disarming Attack](Maneuvers.md#disarming-attack), [Distracting Strike](Manuevers.md#distracting-strike), [Precision Attack](Maneuvers.md#precision-attack)

**Feats:** [Sharpshooter](../Feats/Sharpshooter.md)

You prefer to deal with your enemies from afar, trusting in a well-placed arrow, javelin, or sling bullet to end a fight without a response. You rely on accuracy and probably subscribe to the axiom that "those who live by the sword die by the bow." 


#### Bodyguard
**Fighting Style:** [Interception](Styles.md#interception), [Protection](Styles.md#protection) 

**Maneuvers:** [Bait and Switch](Maneuvers.md#bait-and-switch), [Disarming Attack](Maneuvers.md#disarming-attack), [Goading Attack](Maneuvers.md#goading-attack), [Grappling Strike](Maneuvers.md#grappling-strike)

**Feats:** [Alert](../../Feats/Alert.md), [Observant](../../Feats/Observant.md), [Sentinel](../../Feats/Sentinel.md), [Tough](../../Feats/Tough.md)

Love, money, or some other obligation motivates you to place your own body between harm and the one you're sworn to protect. You have honed the ability to sniff out potential threats and see your charge through dangerous situations.


#### Brawler
**Fighting Style:** [Blind Fighting](Styles.md#blind-fighting), [Two-Weapon Fighting](Styles.md#two-weapon-fighting), [Unarmed Fighting](Styles.md#unarmed-fighting)

**Maneuvers:** [Ambush](Maneuvers.md#ambush), [Disarming Attack](Maneuvers.md#disarming-attack), [Feinting Attack](Maneuvers.md#feinting-attack), [Pushing Attack](Maneuvers.md#pushing-attack), [Trip Attack](Maneuvers.md#trip-attack)

**Feats:** [Athlete](../../Feats/Athlete.md), [Durable](../../Feats/Durable.md), [Grappler](../../Feats/Grappler.md), [Resilient](../../Feats/Resilient.md), [Shield Master](../../Feats/ShieldMaster.md), [Tavern Brawler](../../Feats/TavernBrawler.md), [Tough](../../Feats/Tough.md)

When bottles start breaking and chairs start flying, you're in your element. You love a good scrap, and you've likely seen your share of them. You may or may not have formal training, and while others might call you a dirty fighter, you're still alive.


#### Duelist
**Fighting Style:** [Dueling](Styles.md#dueling), [Two-Weapon Fighting](Styles.md#two-weapon-fighting)

**Maneuvers:** [Evasive Footwork](Maneuvers.md#evasive-footwork), [Feinting Attack](Maneuvers.md#feinting-attack), [Lunging Attack](Maneuvers.md#lunging-attack), [Parry](Maneuvers.md#parry), [Precision Attack](Maneuvers.md#precision-attack), [Riposte](Maneuvers.md#riposte)

**Feats:** [Defensive Duelist](../../Feats/DefensiveDuelist.md), [Dual Wielder](../../Feats/DualWielder.md), [Observant](../../Feats/Observant.md), [Savage Attacker](../../Feats/SavageAttacker.md), [Weapon Master](../../Feats/WeaponMaster.md)

You regard the duel as a proud tradition, a test of skill and wits that brings honor to those who can defeat an enemy while respecting the art. Your search for improvement is a consuming passion, and you draw on the expertise of the masters who've come before you as you work to perfect your form.


#### Gladiator
**Fighting Style:** [Defense](Styles.md#defense), [Two-Weapon Fighting](Styles.md#two-weapon-fighting)

**Maneuvers:** [Goading Attack](Maneuvers.md#goading-attack), [Menacing Attack](Maneuvers.md#menacing-attack), [Sweeping Attack](Maneuvers.md#sweeping-attack), [Trip Attack](Maneuvers.md#trip-attack)

**Feats:** [Athlete](../../Feats/Athlete.md), [Charger](../../Feats/Charger.md), [Dual Wielder](../../Feats/DualWielder.md), [Durable](../../Feats/Durable.md), [Grappler](../../Feats/Grappler.md), [Savage Attacker](../../Feats/SavageAttacker.md), [Tough](../../Feats/Tough.md), [Weapon Master](../../Feats/WeaponMaster.md)

You've fought to entertain crowds, whether for sport or as punishment. Along the way, you learned to use all manner of weapons to battle all kinds of adversaries. You're practical yet theatrical, and you know how to employ fear as an effective tool in a fight.


#### Hoplite
**Fighting Style:** [Defense](Styles.md#defense), [Thrown Weapon Fighting](Styles.md#two-weapon-fighting)

**Maneuvers:** [Brace](Maneuvers.md#brace), [Lunging Attack](Maneuvers.md#lunging-attack), [Parry](Maneuvers.md#parry), [Precision Attack](Maneuvers.md#precision-attack)

**Feats:** [Athlete](../../Feats/Athlete.md), [Grappler](../../Feats/Grappler.md), [Polearm Master](../../Feats/PolearmMaster.md), [Sentinel](../../Feats/Sentinel.md), [Shield Master](../../Feats/ShieldMaster.md)

With spear and shield, you follow in the footsteps of the heroes of ages past. You rely on discipline and athleticism to overcome improbable odds. Whether fighting in ranks alongside your comrades or squaring off as a lone warrior, you're equal to the task.


#### Lancer
**Fighting Style:** [Dueling](Styles.md#dueling)

**Maneuvers:** [Lunging Attack](Maneuvers.md#lunging-attack), [Menacing Attack](Maneuvers.md#menacing-attack), [Precision Attack](Maneuvers.md#precision-attack), [Pushing Attack](Maneuvers.md#pushing-attack)

**Feats:** [Heavy Armor Master](../../Feats/HeavyArmorMaster.md), [Mounted Combatant](../../Feats/MountedCombatant.md), [Savage Attacker](../../Feats/SavageAttacker.md)

When the cavalry is called in, that means you. You ride out to greet your enemy with the point of your weapon. As you charge, the ground trembles, and only the heaviest blows can deter you.


#### Outrider
**Fighting Style:** [Archery](Styles.md#archery)

**Maneuvers:** [Ambush](Maneuvers.md#ambush), [Distracting Strike](Manuevers.md#distracting-strike), [Goading Attack](Maneuvers.md#goading-attack), , [Quick Toss](Maneuvers.md#quick-toss), [Precision Attack](Maneuvers.md#precision-attack)

**Feats:** [Alert](../../Feats/Alert.md), [Crossbow Expert](../../Feats/CrossbowExpert.md), [Mounted Combatant](../../Feats/MountedCombatant.md), [Observant](../../Feats/Observant.md), [Sharpshooter](../../Feats/Sharpshooter.md)

You find freedom in the saddle and a companion in your mount. A headlong charge into combat is a blunt instrument for oafs. You prefer mobility and range, opting to find advantageous positions that allow you to deal with foes at full gallop while evading the most dangerous threats.


#### Pugilist
**Fighting Style:** [Unarmed Fighting](Styles.md#unarmed-fighting)

**Maneuvers:** [Disarming Attack](Maneuvers.md#disarming-attack), [Evasive Footwork](Maneuvers.md#evasive-footwork), [Grappling Strike](Maneuvers.md#grappling-strike), [Menacing Attack](Maneuvers.md#menacing-attack), [Pushing Attack](Maneuvers.md#pushing-attack), [Riposte](Maneuvers.md#riposte), [Trip Attack](Maneuvers.md#trip-attack)

**Feats:** [Athlete](../../Feats/Athlete.md), [Durable](../../Feats/Durable.md), [Grappler](../../Feats/Grappler.md), [Savage Attacker](../../Feats/SavageAttacker.md), [Tavern Brawler](../../Feats/TavernBrawler.md)

Where others rely on steel, you've got your fists. Whether through training or experience, you've developed a superior technique that can help you overcome an enemy in an up-close fight.


#### Shock Trooper
**Fighting Style:** [Great Weapon Fighting](Styles.md#great-weapon-fighting)

**Maneuvers:** [Menacing Attack](Maneuvers.md#menacing-attack), [Pushing Attack](Maneuvers.md#pushing-attack), [Sweeping Attack](Maneuvers.md#sweeping-attack)

**Feats:** [Charger](../../Feats/Charger.md), [Great Weapon Master](../../Feats/GreatWeaponMaster.md), [Heavy Armor Master](../../Feats/HeavyArmorMaster.md)

Subtlety is not your style. You're trained to get straight into the fighting, busting through enemy lines and applying tremendous pressure quickly. Those who ignore you in combat do so at their peril. 


#### Skirmisher
**Fighting Style:** [Archery](Styles.md#archery), [Thrown Weapon Fighting](Styles.md#thrown-weapon-fighting)

**Maneuvers:** [Ambush](Maneuvers.md#ambush), [Bait and Switch](Maneuvers.md#bait-and-switch), [Distracting Strike](Manuevers.md#distracting-strike), [Quick Toss](Maneuvers.md#quick-toss)

**Feats:** [Alert](../../Feats/Alert.md), [Dual Wielder](../../Feats/DualWielder.md), [Mobile](../../Feats/Mobile.md), [Skulker](../../Feats/Skulker.md)

You thrive amid the chaos of battle. You use your mobility and versatility in combat to soften your adversaries and disrupt their formations. An enemy's plan rarely survives contact with you.


#### Strategist
**Fighting Style:** [Defense](Styles.md#defense)

**Maneuvers:** [Commander's Strike](Maneuvers.md#commanders-strike), [Commanding Presence](Maneuvers.md#commanding-presence), [Maneuvering Attack](Maneuvers.md#maneuvering-attack), [Rally](Maneuvers.md#rally), [Tactical Assessment](Maneuvers.md#tactical-assessment)

**Feats:** [Inspiring Leader](../../Feats/InspiringLeader.md), [Keen Mind](../../Feats/KeenMind.md), [Linguist](../../Feats/Linguist.md)

To you, battles unfold like a game of chess. You understand that strength and speed are important in a fight, but it takes intellect and experience to know how best to apply them. That's where you come in.
