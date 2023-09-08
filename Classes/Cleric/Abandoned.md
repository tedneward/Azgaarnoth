# Divine Domain: Abandoned
Nearly all clerics pray to a god, and their belief in them is what gives them their power. However, some clerics worship dead powers, or gods that prefer not to give powers to the unworthy, or the unproven. And some have lost their god's trust, leaving them without their power. These are the clerics of the Abandoned Domain.

```
name = 'Abandoned'
description = "***Divine Domain: Abandoned.*** Some clerics worship dead powers, or gods that prefer not to give powers to the unworthy, or the unproven. And some have lost their god's trust, leaving them without their power. These are the clerics of the Abandoned Domain."
```

## Spell Collection
*1st-level Abandoned Domain feature*

You have an empty place in your soul where domain spells would usually reside (ignore the Domain spells this class gives you; they are placeholders). Thankfully for you, that space can be filled. At level 1, when you successfully save against a spell that is 5th level or lower, you can use a reaction to add that spell to your list of prepared spells the next time you finish a long rest if you can use that level spell slot. For the first two spells per spell level you use this ability with, they are added to your list of Domain spells, even if you cannot yet cast at that level. During a long rest, you can also use a spell scroll to add the spell to your list of prepared spells if you can cast it, adding it to your Domain spells if it is of an appropriate level which is not filled yet.

## Empty Soul
*1st-level Abandoned Domain feature*

Your soul feels empty, and it craves any kind of healing. Whenever you are healed, you are healed for the maximum amount of hit points possible from the source of healing.

```
def level1(npc):
    npc.traits.append("***Empty Soul.*** Whenever you are healed, you are healed for the maximum amount of hit points possible from the source of healing.")
```

## Channel Divinity: Healing Pool
*2nd-level Abandoned Domain feature*

You can expend one use of Channel Divinity as an action to make a melee spell attack against one creature. On a hit, the creature takes poison damage equal to 1d10 + your Cleric level. Then, you can add an amount of hit points into a Healing Pool equal to the damage done, separate from your health. As a bonus action, you can add any amount of hit points to a creature you can touch, including yourself, by spending an equal amount of hit points from your Healing Pool. 

```
def level2(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Channel Divinity: Healing Pool. Melee Spell attack, +{npc.spellcasting[name].spellattack()} to hit, range 5 ft., one creature. Hit: 1d10 + {npc.spellcasting[name].casterlevel()}, which is added into a Healing Pool equal to the damage done, separate from your health."))

    npc.bonusactions.append("***Healing Pool.*** Add any amount of hit points to a creature you can touch, including yourself, by spending an equal amount of hit points from your Healing Pool.")
```

## Divine Resistance
*6th-level Abandoned Domain feature*

Your distance from divinity has made you resistant to the effects of certain extraplanar beings. You are resistant to radiant damage, as well any other damage types ONLY when it is dealt by any creature considered "fiend" or "celestial." You also have Advantage on saving throws to resist non-damaging effects by fiends or celestials if the effect is magical or inflicted by magical means, unless you choose otherwise. Any effects paired with damage are not resisted.

```
def level6(npc):
  npc.damageresistances.append("Celestial")
  npc.damageresistances.append("any damage types dealt by any celestial or fiend creature")
  npc.traits.append("***Divine Resistance.*** You also have Advantage on saving throws to resist non-damaging effects by fiends or celestials if the effect is magical or inflicted by magical means, unless you choose otherwise. Any effects paired with damage are not resisted.")
```

## Divine Strike
*8th-level Abandoned Domain feature*

Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra 1d8 damage of the same type dealt by the weapon to the target. When you reach 14th level, the extra damage increases to 2d8.

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Divine Strike.*** Once on each of your turns when you hit a creature with a weapon attack, you can cause the attack to deal an extra {'1d8' if npc.levels('Cleric') < 14 else '2d8'} damage of the same type dealt by the weapon to the target."))
```

## Divine Rejection
*17th-level Abandoned Domain feature*

You have built up even more barriers from divine and demonic forces. You now have immunity to radiant damage. Additionally, you are now immune to any non-damaging effects that a creature considered a "fiend" or "celestial" might inflict on you, unless you wish it to be inflicted, as long as the effect is magical or is inflicted by magical means. Any effects paired with damage are not resisted.

```
def level17(npc):
    npc.damageimmunities.append('radiant')
    npc.damageimmunities.append('any damage types dealth by any celestial or fiend creature')
```
