# Primal Path: Path of the Totem Warrior
The Path of the Totem Warrior is a spiritual journey, as the barbarian accepts a spirit animal as guide, protector, and inspiration. In battle, your totem spirit fills you with supernatural might, adding magical fuel to your barbarian rage.

Most barbarian tribes consider a totem animal to be kin to a particular clan. In such cases, it is unusual for an individual to have more than one totem animal spirit, though exceptions exist. These barbarians are usually found among the [Yithi](../../Nations/Yithi.md) or [Zhi](../../Nations/Zhi.md), but also a surprising number of them show up in the lands of the Al'Uma, among the tribes that take after the various animals as their sigil.

```
name = 'Totem Warrior'
description = "***Primal Path: Path of the Totem Warrior.*** The Path of the Totem Warrior is a spiritual journey, as the barbarian accepts a spirit animal as guide, protector, and inspiration. In battle, your totem spirit fills you with supernatural might, adding magical fuel to your barbarian rage."
```

## Spirit Seeker
*3rd-level Totem Warrior feature*

Yours is a path that seeks attunement with the natural world, giving you a kinship with beasts. You gain the ability to cast the [beast sense](../../Magic/Spells/beast-sense.md) and [speak with animals](../../Magic/Spells/speak-with-animals.md) spells, but only as rituals.

```
def level3(npc):
    npc.actions.append(f"***Spirit Seeker.*** You can cast {spelllinkify('beast sense')} as a ritual. You can cast {spelllinkify('speak with animals')} as a ritual.")
```

## Totem Spirit
*3rd-level Totem Warrior feature*

At 3rd level, when you adopt this path, you choose a totem spirit and gain its feature. You must make or acquire a physical totem object – an amulet or similar adornment – that incorporates fur or feathers, claws, teeth, or bones of the totem animal. At your option, you also gain minor physical attributes that are reminiscent of your totem spirit. For example, if you have a bear totem spirit, you might be unusually hairy and thick-skinned, or if your totem is the eagle, your eyes turn bright yellow.

Your totem animal might be an animal related to those listed here but more appropriate to your homeland. For example, you could choose a hawk or vulture in place of an eagle.

* **Bear**. While raging, you have resistance to all damage except psychic damage. The spirit of the bear makes you tough enough to stand up to any punishment.

* **Eagle**. While you're raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you, and you can use the Dash action as a bonus action on your turn. The spirit of the eagle makes you into a predator who can weave through the fray with ease.

* **Elk**. While you're raging and aren't wearing heavy armor, your walking speed increases by 15 feet. The spirit of the elk makes you extraordinarily swift.

* **Tiger**. While raging, you can add 10 feet to your long jump distance and 3 feet to your high jump distance. The spirit of the tiger empowers your leaps.

* **Wolf**. While you're raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you. The spirit of the wolf makes you a leader of hunters.

```
    spirit = choose("Choose a Totem Spirit: ", ['Bear', 'Eagle', 'Elk', 'Tiger', 'Wolf'])
    npc.spirit = spirit
    if npc.spirit == 'Bear':
        npc.traits.append("***Totem Spirit: Bear.*** While raging, you have resistance to all damage except psychic damage.")
    elif npc.spirit == 'Eagle':
        npc.traits.append("***Totem Spirit: Eagle.*** While raging and aren't wearing heavy armor, other creatures have disadvantage on opportunity attack rolls against you.")
        npc.bonusactions.append("***Totem Spirit: Eagle.*** You use the Dash action.")
    elif npc.spirit == 'Elk':
        npc.traits.append("***Totem Spirit: Elk.*** While raging and you aren't wearing heavy armor, your walking speed increases by 15 feet.")
    elif npc.spirit == 'Tiger':
        npc.traits.append("***Totem Spirit: Tiger.*** While raging, you add 10 feet to your long jump distance and 3 feet to your high jump distance.")
    elif npc.spirit == 'Wolf':
        npc.traits.append("***Totem Spirit: Wolf.*** While raging, your friends have advantage on melee attack rolls against any creature within 5 feet of you that is hostile to you.")
    else:
        error("WTF?!? There is no Totem Spirit '" + str(npc.spirit) + "'")
```

## Aspect of the Beast
*6th-level Totem Warrior feature*

You gain a magical benefit based on the totem animal of your choice. You can choose the same animal you selected at 3rd level or a different one.

* **Bear**. You gain the might of a bear. Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.

* **Eagle**. You gain the eyesight of an eagle. You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.

* **Elk**. Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated. The elk spirit helps you roam far and fast.

* **Tiger**. You gain proficiency in two skills from the following list: Athletics, Acrobatics, Stealth, and Survival. The cat spirit hones your survival instincts.

* **Wolf**. You gain the hunting sensibilities of a wolf. You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.

```
def level6(npc):
    spirit = choose("Choose a Totem Spirit: ", ['Bear', 'Eagle', 'Elk', 'Tiger', 'Wolf'])
    npc.spirit = spirit
    if npc.spirit == 'Bear':
        npc.traits.append("***Aspect of the Beast: Bear.*** Your carrying capacity (including maximum load and maximum lift) is doubled, and you have advantage on Strength checks made to push, pull, lift, or break objects.")
    elif npc.spirit == 'Eagle':
        npc.traits.append("***Aspect of the Beast: Eagle.*** You can see up to 1 mile away with no difficulty, able to discern even fine details as though looking at something no more than 100 feet away from you. Additionally, dim light doesn't impose disadvantage on your Wisdom (Perception) checks.")
    elif npc.spirit == 'Elk':
        npc.traits.append("***Aspect of the Beast: Elk.*** Whether mounted or on foot, your travel pace is doubled, as is the travel pace of up to ten companions while they're within 60 feet of you and you're not incapacitated.")
    elif npc.spirit == 'Tiger':
        chooseskill(npc, ['Athletics', 'Acrobatics', 'Stealth', 'Survival'])
        chooseskill(npc, ['Athletics', 'Acrobatics', 'Stealth', 'Survival'])
    elif npc.spirit == 'Wolf':
        npc.traits.append("***Aspect of the Beast: Wolf.*** You can track other creatures while traveling at a fast pace, and you can move stealthily while traveling at a normal pace.")
    else:
        error("WTF?!? There is no Totem Spirit '" + str(npc.spirit) + "'")
```

## Spirit Walker
*10th-level Totem Warrior feature*

You can cast the Commune with Nature spell, but only as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.

```
def level10(npc):
    npc.actions.append(f"***Spirit Walker.*** You cast {spelllinkify('commune with nature')} as a ritual. When you do so, a spiritual version of one of the animals you chose for Totem Spirit or Aspect of the Beast appears to you to convey the information you seek.")
```

## Totemic Attunement
*14th-level Totem Warrior feature*

You gain a magical benefit based on a totem animal of your choice. You can choose the same animal you selected previously or a different one.

* **Bear**. While raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.

* **Eagle**. While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.

* **Elk**. While raging, you can use a bonus action during your move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC 8 + your Strength bonus + your proficiency bonus) or be knocked prone and take bludgeoning damage equal to 1d12 + your Strength modifier.

* **Tiger**. While raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you can use a bonus action to make an additional melee weapon attack against it.

* **Wolf**. While raging, you can use a bonus action on your turn to knock a Large or smaller creature prone when you hit it with melee weapon attack.


```
def level14(npc):
    spirit = choose("Choose a Totem Spirit: ", ['Bear', 'Eagle', 'Elk', 'Tiger', 'Wolf'])
    npc.spirit = spirit
    if npc.spirit == 'Bear':
        npc.traits.append("***Totemic Attunement: Bear.*** While raging, any creature within 5 feet of you that's hostile to you has disadvantage on attack rolls against targets other than you or another character with this feature. An enemy is immune to this effect if it can't see or hear you or if it can't be frightened.")
    elif npc.spirit == 'Eagle':
        npc.traits.append("***Totemic Attunement: Eagle.*** While raging, you have a flying speed equal to your current walking speed. This benefit works only in short bursts; you fall if you end your turn in the air and nothing else is holding you aloft.")
    elif npc.spirit == 'Elk':
        npc.defer(lambda npc: npc.bonusactions.append("***Totemic Attunement: Elk.*** While raging, you can move to pass through the space of a Large or smaller creature. That creature must succeed on a Strength saving throw (DC {8 + npc.proficiencybonus() + npc.STRbonus()}) or be knocked prone and take 1d12 + {npc.STRbonus()} bludgeoning damage.") )
    elif npc.spirit == 'Tiger':
        npc.bonusactions.append("***Totemic Attunement: Tiger.*** While raging, if you move at least 20 feet in a straight line toward a Large or smaller target right before making a melee weapon attack against it, you make an additional melee weapon attack against it.")
    elif npc.spirit == 'Wolf':
        npc.bonusactions.append("***Totemic Attunement: Wolf.*** While raging, if you hit a Large or smaller creature with melee weapon attack, you knock it prone.")
    else:
        error("WTF?!? There is no Totem Spirit '" + str(npc.spirit) + "'")
```
