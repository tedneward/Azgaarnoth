# Martial Archetype: Deathless
Some warriors battle as if they are already acquainted with the grave. As still as a corpse until they strike with sudden power and swiftness, unbending in combat even when injured or nearly dead, these fighters are known in legends as Deathless. Some have already died and been returned, perhaps even as undead Others are warded against death by birth, curse, or artifice, such as those favored by a god of death. Yet most deathless are simply too tough -- or too lucky -- to die so easily.

```
name = 'Deathless'
description = "***Martial Archetype: Deathless.*** Some warriors battle as if they are already acquainted with the grave. As still as a corpse until they strike with sudden power and swiftness, unbending in combat even when injured or nearly dead, these fighters are known in legends as Deathless. Some have already died and been returned, perhaps even as undead Others are warded against death by birth, curse, or artifice, such as those favored by a god of death. Yet most deathless are simply too tough -- or too lucky -- to die so easily."
```

## Endless Toil
*3rd-level Deathless feature*

You have advantage on saving throws against disease, and you can't gain exhaustion from physical exertion, such as by traveling, engaging in combat, grappling or restraining a creature, or lifting and throwing things.

```
def level3(npc):
    npc.traits.append("***Endless Toil.*** You have advantage on saving throws against disease, and you can't gain exhaustion from physical exertion, such as by traveling, engaging in combat, grappling or restraining a creature, or lifting and throwing things.")
```

## Deathly Vigor
*3rd-level Deathless feature*

You become a tireless warrior in battle, capable of recovering from injuries without slowing your assault, and your bursts of vigor grant a speed to your attacks that would exhaust other warriors. 

When you use a bonus action to regain hit points using your Second Wind feature, you also gain temporary hit points equal to 5 + half your fighter leveL and you can make one weapon attack as part of the same bonus action. Once you reach 7th leveL you also have advantage on this weapon attack.

Also, when your turn begins and your Second Wind feature is expended, you can choose to regain it. Once you do, you can't do so again until you finish a long rest.

```
    npc.defer(lambda npc: replace("***Second Wind ", npc.bonusactions, f" (Recharges on short or long rest).*** On your turn, you can regain 1d10 + {npc.levels('Fighter')} hit points and gain {5 + (npc.levels('Fighter') // 2)} temporary hit points. Also, when you turn begins and your Second Wind is expended, you can choose to regain it. {'Once you do, you can't do so again' if npc.levels('Fighter') < 15 else 'You can do this up to three times, and then not again'} until you finish a long rest."))
```

## One Foot in the Grave
*7th-level Deathless feature*

You gain resistance to necrotic damage and poison damage, you are immune to disease, and you can't gain any exhaustion except from magical sources. Your grim and ghastly disposition also gives you advantage on Charisma (Intimidation) checks, but not towards celestials, constructs, fiends, or undead.

```
def level7(npc):
    npc.damageresistances('necrotic')
    npc.damageresistances('poison')
    npc.considtionimmunities('diseased')
    npc.traits.append("***One Foot in the Grave.*** You can't gain any exhaustion except from magical sources. Your grim and ghastly disposition also gives you advantage on Charisma (Intimidation) checks, but not towards celestials, constructs, fiends, or undead.")
```

## Grim Riposte
*10th-level Deathless feature*

Your deathly stillness can suddenly give way to bursts of frenzied, ghoulish motion that surprise your foes when their guards are down. When you are hit with a melee weapon attack and you have a weapon or a shield, you can use your reaction to parry the strike, forcing the attacker to reroll the attack roll and use the new result. If this causes the attack to miss, you can also make one weapon attack against the creature that attacked you as part of the reaction.

If you use this feature and cause the attacker to miss, you can't use it again until you finish a short or long rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.reactions.append("***Grim Ripste (Recharges on short or long rest).*** When you are hit with a melee weapon attack and you have a weapon or a shield, you parry the strike, forcing the attacker to reroll the attack roll and use the new result. If this causes the attack to miss, you can also make one weapon attack {'' if npc.levels('Fighter') < 15 else 'at advantage '}against the creature that attacked you as part of the reaction. If you use this feature and cause the attacker to miss, you can't use it again until you recharge.{'' if npc.levels('Fighter') < 15 else 'Whenever you roll initiative and your Grim Riposte is expended, you regain the use of it.'}") )
```

## Tireless Mastery
*15th-level Deathless feature*

You have advantage on weapon attacks granted by your Grim Riposte feature, and whenever you roll initiative and the feature is expended, you regain the use of it.

## The Undying
*18th-level Deathless feature*

You become something between life and death. You do not lose consciousness or become incapacitated for reaching 0 hit points, and taking damage while you are at 0 hit points does not impose any death saving throws. This does not prevent death. 

In addition, you can regain the use of your Second Wind feature using your Deathly Vigor feature up to three times between long rests, instead of only once.

```
def level18(npc):
    npc.traits.append("***The Undying.*** You do not lose consciousness or become incapacitated for reaching 0 hit points, and taking damage while you are at 0 hit points does not impose any death saving throws. This does not prevent death.")
```