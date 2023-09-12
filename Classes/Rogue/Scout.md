# Roguish Archetype: Scout
You are skilled in stealth and surviving far from the streets of a city, allowing you to scout ahead of your companions during expeditions. Rogues who embrace this archetype are at home in the wilderness and among barbarians and rangers, and many Scouts serve as the eyes and ears of war bands. Ambusher, spy, bounty hunter – these are just a few of the roles that Scouts assume as they range the world.

```
name = 'Scout'
description = "***Roguish Archetype: Scout.*** You are skilled in stealth and surviving far from the streets of a city, allowing you to scout ahead of your companions during expeditions. Rogues who embrace this archetype are at home in the wilderness and among barbarians and rangers, and many Scouts serve as the eyes and ears of war bands. Ambusher, spy, bounty hunter – these are just a few of the roles that Scouts assume as they range the world."
```

## Skirmisher
*3rd-level Scout feature*

You are difficult to pin down during a fight. You can move up to half your speed as a reaction when an enemy ends its turn within 5 feet of you. This movement doesn't provoke opportunity attacks.

```
def level3(npc):
    npc.reactions.append("***Skirmisher.*** You can move up to half your speed as a reaction when an enemy ends its turn within 5 feet of you. This movement doesn't provoke opportunity attacks.")
```

## Survivalist
*3rd-level Scout feature*

You gain proficiency in the Nature and Survival skills if you don't already have it. Your proficiency bonus is doubled for any ability check you make that uses either of those proficiencies.

```
    npc.proficiencies.append("Nature")
    npc.proficiencies.append("Survival")
    npc.traits.append("***Survivalist.*** Your proficiency bonus is doubled for any ability check you make that uses either of Nature or Survival.")
```

## Superior Mobility
*9th-level Scout feature*

Your walking speed increases by 10 feet. If you have a climbing or swimming speed, this increase applies to that speed as well.

```
def level9(npc):
    for s in npc.speed:
        if s == 'walking' or s == 'climbing' or s == 'swimming':
            npc.speed[s] += 10
```

## Ambush Master
*13th-level Scout feature*

You excel at leading ambushes and acting first in a fight.

You have advantage on initiative rolls. In addition, the first creature you hit during the first round of a combat becomes easier for you and others to strike; attack rolls against that target have advantage until the start of your next turn.

```
def level13(npc):
    npc.traits.append("***Ambush Master.*** You have advantage on initiative rolls. In addition, the first creature you hit during the first round of a combat becomes easier for you and others to strike; attack rolls against that target have advantage until the start of your next turn.")
```

## Sudden Strike
*17th-level Scout feature*

You can strike with deadly speed. If you take the Attack action on your turn, you can make one additional attack as a bonus action. This attack can benefit from your Sneak Attack even if you have already used it this turn, but you can't use your Sneak Attack against the same target more than once in a turn.

```
def level17(npc):
    npc.bonusactions.append("***Sudden Strike.*** If you take the Attack action on your turn, you can make one additional attack as a bonus action. This attack can benefit from your Sneak Attack even if you have already used it this turn, but you can't use your Sneak Attack against the same target more than once in a turn.")
```
