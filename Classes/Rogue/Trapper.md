# Roguish Archetype: Trapper
There are those who will slide a blade into an enemy's ribs, those who would drip poison into their drinks, and then there are those who take the utmost pride in making the enemy's death look like an accident. Given just a little bit of time and materials, a Trapper can turn an hallway into a blood trough, a doorway into a portal to death, or a house into a morgue.

```
name = 'Trapper'
description = "***Roguish Archetype: Trapper.*** There are those who will slide a blade into an enemy's ribs, those who would drip poison into their drinks, and then there are those who take the utmost pride in making the enemy's death look like an accident. Given just a little bit of time and materials, a Trapper can turn an hallway into a blood trough, a doorway into a portal to death, or a house into a morgue."
```

## Trap Mastery
*3rd-level trapper feature*

You learn the secrets of arranging precision-perfect traps to catch your enemies in their most vulnerable moments. 

You gain proficiency with your choice of either Alchemist's Supplies, Poisoner's Kit, or Tinker's Tools.

```
def level3(npc):
    npc.proficiencies.append(choose("Choose: ", ["Alcemist's supplies", "Poisoner's kit", "Tinker's tools"]))
```

You also learn how to create and arrange amazing traps with which to catch your enemies. Arranging a trap takes 1 minute of uninterrupted work, and to do so you must both have the trap's materials and meet the trap's requirements. If a trap's materials include a tool, proficiency is not required, and the tool is not expended in the making of the trap.

To place a trap in a lock, you can use a door or any other object that can lock, and you can choose whether the trap activates upon unlocking or upon opening. If not placed in a lock, a trap activates when a creature other than you moves within the activation range of the trap. When you arrange a trap, you can choose to reduce its activation range to a lower value. A trap will attempt to target as many creatures other than you as it can when it activates, preferring closer targets, but it will always target the activating creature. A trap will only activate once and then fall apart.

```
    class TrapMastery:
        def __init__(self):
            self.trapdc = 0
            self.trapsknown = []
            self.maxtrapsknown = 0

    npc.trapmastery = TrapMastery()
    def settrapmastery(npc):
        npc.trapmastery.trapdc = 8 + npc.INTbonus() + npc.proficiencybonus()
        npc.trapmastery.maxtrapsknown = npc.INTbonus() if npc.INTbonus() > 0 else 1

        for _ in range(0, npc.trapmastery.maxtrapsknown):
            npc.trapmastery.trapsknown.append(choose("Choose a trap: ", ['Blade', 'Dart', 'Electric', 'Flame', 'Net', 'Pit', 'Poison Gas', 'Swinging', 'Thunderblast', 'Web']))

        npc.traits.append(f"***Trap Mastery ({npc.INTbonus()}/Recharges on long rest).*** Trap DC Save: {npc.trapmastery.trapdc}, {npc.trapmastery.maxtrapsknown} traps known:")

        for trap in npc.trapmastery.trapsknown:
            if trap == "Blade":
                npc.traits.append(f"***Blade Trap.*** **Materials:** Tinker's tools, thieves' tools, and 1 bladed weapon. **Requirements:** A place to arrange on a wall, floor, or ceiling. **Activation Range:** 10 feet **Activation Effect:** Up to two creatures within 10 feet of the trap must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature takes 2d8 slashing damage plus your Sneak Attack bonus.")
            elif trap == "Dart":
                npc.traits.append(f"***Dart Trap.*** **Materials:** Tinker's tools, thieves' tools, and 1 crossbow bolt **Requirements:** A place to arrange on a wall floor, or ceiling. **Activation Range:** 10 feet **Activation Effect:** One creature within 30 feet of the trap must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, the creature takes 4d4 piercing damage plus your Sneak Attack bonus.")
            elif trap == "Electric":
                npc.traits.append(f"***Electric Trap.*** **Materials:** Thieves' tools and alchemist's supplies **Requirements:** A place to arrange on a wall or floor, or in a locked object. **Activation Range:** 5 feet **Activation Effect:** One creature within 5 feet of the trap is afflicted by a shocking electric current and must make a Constitution saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature takes 1d8 lightning damage and, if the creature does not have resistance or immunity to lightning damage, it is paralyzed The creature repeats the saving throw at the end of each of their turns, ending the effect on a success.")
            elif trap == "Flame":
                npc.traits.append(f"***Flame Trap.*** **Materials:** Tinker's tools, and alchemist supplies or lantern oil **Requirements:** A place to arrange on a wall floor, or ceiling, or in a locked object. **Activation Range:** 15 feet **Activation Effect:** A gout of flame emanates from the trap, blasting all creatures within a line 30 feet long and 5 feet wide. Each creature in the area must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature takes {'2d6' if npc.levels('Rogue') < 7 else '4d6' if npc.levels('Rogue') < 13 else '6d6' if npc.levels('Rogue') < 19 else '8d6'} fire damage.")
            elif trap == "Net":
                npc.traits.append(f"***Net Trap.*** **Materials:** Tinker's tools and 2 nets. **Requirements:** A place to arrange on a wall or ceiling. **Activation Range:** 15 feet **Activation Effect:** Up to two creatures within 30 feet of the trap must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature is hit by an attack using a net.")
            elif trap == "Pit":
                npc.traits.append(f"***Pit Trap.*** **Materials:** Disguise kit, tinker's tools, or materials gathered from the nearby area with a DC 12 Wisdom (Survival) check.**Requirements:** A hole dug in the floor at least 5 feet deep, with a maximum radius of 5 feet and a maximum depth of {20 + npc.levels('Rogue')} feet. The trap must be arranged within the space of the top of the hole. **Activation Range:** The pit's entire area **Activation Effect:** The pit, which was covered and disguised, is revealed as the covering falls through and any who were standing on top of the pit must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature falls into the pit. On a successful saving throw, it instead falls into a space at the edge of the pit. Either way, it is knocked prone.")
            elif trap == "Poison Gas":
                npc.traits.append(f"***Poison-Gas Trap.*** **Materials:** Thieves' tools and poisoner's kit **Requirements:** A place to arrange on a wall floor, or ceiling, or in a locked object. **Activation Range:** 5 feet **Activation Effect:** A hiss of visible, colorful gas escapes from the trap, causing all creatures within 10 feet of the trap to make a Constitution saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature is poisoned. A poisoned creature repeats the saving throw at the end of each of their turns, ending the effect on a success.")
            elif trap == "Swinging":
                npc.traits.append(f"***Swinging Trap.*** **Materials:** Tinker's tools and thieves' tools **Requirements:** A place to arrange on a wall or ceiling, or in a locked object. **Activation Range:** 5 feet **Activation Effect:** Up to two creatures within 5 feet of the trap must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, the creature takes 2d10 bludgeoning damage (plus your Sneak Attack) and is knocked prone.")
            elif trap == "Thunderblast":
                npc.traits.append(f"***Thunderblast Trap.*** **Materials:** Tinker's tools and alchemist's supplies **Requirements:** A place to arrange on a wall floor, or ceiling. **Activation Range:** 5 feet **Activation Effect:** A blast of air pressure releases from the trap, causing each creature within 10 feet of the trap to make a Strength saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature takes {'1d8' if npc.levels('Rogue') < 7 else '2d8' if npc.levels('Rogue') < 13 else '3d8' if npc.levels('Rogue') < 19 else '4d8'} thunder damage, is pushed 10 feet, and is knocked prone.")
            elif trap == "Web":
                npc.traits.append(f"***Web Trap.*** **Materials:** Thieves' tools and alchemist's supplies **Requirements:** A place to arrange on a wall or floor, or in a locked object. **Activation Range:** 5 feet **Activation Effect:** A burst of sticky webbing releases from the trap, covering each creature within 10 feet of the trap and forcing them to make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). On a failed saving throw, a creature is grappled by the trap (the escape DC is {npc.trapmastery.trapdc}) and restrained while it is grappled in this way.")
            else:
                print("Unrecognized trap: " + trap)

    npc.defer(lambda npc: settrapmastery(npc))

    npc.description.append("***Traps.*** Arranging a trap takes 1 minute of uninterrupted work, and to do so you must both have the trap's materials and meet the trap's requirements. If a trap's materials include a tool, proficiency is not required, and the tool is not expended in the making of the trap.")
    npc.description.append("To place a trap in a lock, you can use a door or any other object that can lock, and you can choose whether the trap activates upon unlocking or upon opening. If not placed in a lock, a trap activates when a creature other than you moves within the activation range of the trap. When you arrange a trap, you can choose to reduce its activation range to a lower value. A trap will attempt to target as many creatures other than you as it can when it activates, preferring closer targets, but it will always target the activating creature. A trap will only activate once and then fall apart.")
    npc.description.append("When you finish arranging a trap, it is hidden. If an enemy isn't aware of your trap's existence, it has disadvantage on saving throws to defend against the trap's activation effect. A foe can detect your traps by using an action to make a Wisdom (Perception) ability check against your Trap DC. Once a trap is detected, a creature can take an action on its turn to walk and act very carefully and become unable to trigger the trap by moving until the end of its turn. A creature who is aware of a trap can also use an action to touch the trap and make an Intelligence (Investigation) or Dexterity (Sleight of Hand) ability check against your Trap DC. The creature has disadvantage on this ability check. On a success, the creature disarms your trap and it falls apart harmlessly. On a failure, the creature activates the trap.")
```

You can only use this feature to arrange a trap a number of times equal to your Intelligence modifier (minimum 1). When you finish a long rest, you restore all uses of this feature.

You know how to make a number of traps equal to your Intelligence modifier (minimum 1) chosen from the list below as the number increases. You can choose to replace one trap you know with a different trap when you gain a rogue level.

Traps that require your enemies to make an ability check or a saving throw against a DC use your Trap DC, which equals 8 + your Intelligence modifier+ your proficiency bonus.

When you finish arranging a trap, it is hidden. If an enemy isn't aware of your trap's existence, it has disadvantage on saving throws to defend against the trap's activation effect.

A foe can detect your traps by using an action to make a Wisdom (Perception) ability check against your Trap DC. Once a trap is detected, a creature can take an action on its turn to walk and act very carefully and become unable to trigger the trap by moving until the end of its turn.

A creature who is aware of a trap can also use an action to touch the trap and make an Intelligence (Investigation) or Dexterity (Sleight of Hand) ability check against your Trap DC. The creature has disadvantage on this ability check. On a success, the creature disarms your trap and it falls apart harmlessly. On a failure, the creature activates the trap.

## Caltrop Mastery
*3rd-level trapper feature*

You gain proficiency with fine caltrops, allowing you to use them for attacks with improved caltrop effects. An attack with fine caltrops doesn't target a creature, but targets a 5-foot diameter circular area on the ground.

**SPECIAL RANGED WEAPONS**
Weapon|Cost|Dmg|Weight|Properties
------|----|---|------|----------
Fine Caltrops|5 sp| -- |1 lb.|Special, Thrown (40 ft.)

Any creature that enters the area of your fine caltrops while the caltrops remain on top of the ground must make a Dexterity saving throw against your Trap DC. Any creature who cannot see the caltrops (if they are scattered in dense foliage, obscuring mist, etc., it requires a Wisdom (Perception) check against your Trap DC to find them) has disadvantage on this saving throw.

A creature that is aware of the caltrops and chooses to move at half speed through the area (see PHB, page 151) still makes the saving throw, but with advantage. On a failed saving throw for fine caltrops, a creature takes piercing damage equal to your Dexterity modifier (minimum 1). On a successful saving throw, a creature takes no damage.

```
    npc.proficiencies.append("Fine caltrops")
    npc.defer(lambda npc: npc.actions.append(f"***Fine caltrops (thrown).*** Ranged weapon attack. +{npc.proficiencybonus() + npc.DEXbonus()} to hit, Range 40, {5 if npc.levels('Rogue') < 13 else 15}' diameter circular area on the ground. Hit: Any creature that enters the area while the caltrops remain on top of the ground must make a Dexterity saving throw (DC {npc.trapmastery.trapdc}). Any creature who cannot see the caltrops (if they are scattered in dense foliage, obscuring mist, etc.) requires a Wisdom (Perception) check (DC {npc.trapmastery.trapdc}) to find them and has disadvantage on this saving throw. A creature that is aware of the caltrops and chooses to move at half speed through the area still makes the saving throw, but with advantage. On a failed saving throw for fine caltrops, a creature takes {npc.INTbonus()} piercing damage; on a successful saving throw, a creature takes no damage."))
```

## Precision Planning
*3rd-level trapper feature*

You can use your Sneak Attack when one of your traps deals bludgeoning, piercing, or slashing damage to a creature. You can also your use your Sneak Attack when you deal damage with fine caltrops, but only up to a number of times equal to your Intelligence modifier (minimum 1) regaining all uses when you finish a short or long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Precision Planning ({npc.INTbonus()}/Recharges on short or long rest).*** You can use your Sneak Attack when you deal damage with fine caltrops."))
```

## Hidden Threats
*9th-level trapper feature*

You learn the secrets of hiding and detecting traps of all kinds. You have advantage on Wisdom (Perception) checks to detect hidden doors, mechanisms, and traps, and your caltrops, fine caltrops, and traps that you arrange using your Trap Mastery feature grant enemies disadvantage on Perception checks made to detect them.

In addition, you gain the ability to completely ignore the effects of your own caltrops and fine caltrops. 

```
def level9(npc):
    npc.traits.append("***Hidden Threats.*** You have advantage on Wisdom (Perception) checks to detect hidden doors, mechanisms, and traps. Your caltrops, fine caltrops, and traps that you arrange using your Trap Mastery feature grant enemies disadvantage on Perception checks made to detect them.In addition, you gain the ability to completely ignore the effects of your own caltrops and fine caltrops.")
```

## Wide Spread
*13th-level trapper feature*

You learn how to make the most out of a handful of caltrops, throwing them wide but efficiently so that they cover a broader area. When you make an attack with fine caltrops, the diameter of the area they effect is 15 feet.

Also, when a trap you arranged with your Trap Mastery feature activates and targets one or two creatures, you can target an additional creature within 5 feet of one target as well, and when you arrange a trap that affects an area, you double the size of that area.

```
def level13(npc):
    npc.traits.append("***Wide Spread.*** When a trap you arranged with your Trap Mastery feature activates and targets one or two creatures, you can target an additional creature within 5 feet of one target as well, and when you arrange a trap that affects an area, you double the size of that area.")
```

## Perfect Timing
*17th-level trapper feature*

You learn how to coordinate your strikes with your traps perfectly. You can now both deal damage normally with your Sneak Attack and deal Sneak Attack damage using your Precision Planning feature on the same turn, though you can still use each ability only once per turn.

In addition, when you deal Sneak Attack damage to a creature using your Precision Planning feature, you gain advantage on weapon attacks made against that creature until the end of that turn.

Finally, you can use Precision Planning an unlimited number of times without having to rest. 

```
def level17(npc):
    npc.traits.append("***Perfect Timing.*** You can deal damage both normally with your Sneak Attack and deal Sneak Attack damage using your Precision Planning feature on the same turn, though you can still use each ability only once per turn.")

    replace("***Precision Planning", npc.traits, ".*** You can use your Sneak Attack when you deal damage with fine caltrops. You gain advantage on weapon attacks made against that creature until end of turn.")
```

## Traps

### Blade Trap
**Materials:** Tinker's tools, thieves' tools, and 1 bladed weapon

**Requirements:** A place to arrange on a wan floor, or ceiling.

**Activation Range:** 10 feet

**Activation Effect:** Up to two creatures within 10 feet of the trap must make a Dexterity saving throw. On a failed saving throw, a creature takes 2d8 slashing damage.

### Dart Trap
**Materials:** Tinker's tools, thieves' tools, and 1 crossbow bolt

**Requirements:** A place to arrange on a wall floor, or ceiling.

**Activation Range:** 10 feet

**Activation Effect:** One creature within 30 feet of the trap must make a Dexterity saving throw. On a failed saving throw, the creature takes 4d4 piercing damage.

### Electric Trap
**Materials:** Thieves' tools and alchemist's supplies

**Requirements:** A place to arrange on a wall or floor, or in a locked object.

**Activation Range:** 5 feet

**Activation Effect:** One creature within 5 feet of the trap is afflicted by a shocking electric current and must make a Constitution saving throw. On a failed saving throw, a creature takes ld8 lightning damage and, if the creature does not have resistance or immunity to lightning damage, it is paralyzed The creature repeats the saving throw at the end of each of their turns, ending the effect on a success.

### Flame Trap
**Materials:** Tinker tools, and alchemist supplies or lantern oil

**Requirements:** A place to arrange on a wall floor, or ceiling, or in a locked object.

**Activation Range:** 15 feet

**Activation Effect:** A gout of flame emanates from the trap, blasting all creatures within a line 30 feet long and 5 feet wide. Each creature in the area must make a Dexterity saving throw. On a failed saving throw, a creature takes 2d6 fire damage. This damage increases to 4d6 at 7th level to 6d6 damage at 13th level and to 8d6 at 19th level.

### Net Trap
**Materials:** Tinker's tools and 2 nets.

**Requirements:** A place to arrange on a wall or ceiling.

**Activation Range:** 15 feet

**Activation Effect:** Up to two creatures within 30 feet of the trap must make a Dexterity saving throw. On a failed saving throw, a creature is hit by an attack using a net.

### Pit Trap
**Materials:** Disguise kit, tinker's tools, or materials gathered from the nearby area with a DC 12 Wisdom (Survival) check.

**Requirements:** A hole dug in the floor at least 5 feet deep, with a maximum radius of 5 feet and a maximum depth of a number of feet equal to 20 + your rogue level. The trap must be arranged within the space of the top of the hole.

**Activation Range:** The pit's entire area

**Activation Effect:** The pit, which was covered and disguised, is revealed as the covering falls through and any who were standing on top of the pit must make a Dexterity saving throw. On a failed saving throw, a creature falls into the pit. On a successful saving throw, it instead falls into a space at the edge of the pit. Either way, it is knocked prone.

### Poison-Gas Trap
**Materials:** Thieves' tools and poisoner's kit

**Requirements:** A place to arrange on a wall floor, or ceiling, or in a locked object.

**Activation Range:** 5 feet

**Activation Effect:** A hiss of visible, colorful gas escapes from the trap, causing all creatures within 10 feet of the trap to make a Constitution saving throw. On a failed saving throw, a creature is poisoned A poisoned creature repeats the saving throw at the end of each of their turns, ending the effect on a success.

### Swinging Trap
**Materials:** Tinker's tools and thieves' tools

**Requirements:** A place to arrange on a wall or ceiling, or in a locked object.

**Activation Range:** 5 feet

**Activation Effect:** Up to two creatures within 5 feet of the trap must make a Dexterity saving throw. On a failed saving throw, the creature takes 2d10 bludgeoning damage and is knocked prone.

### Thunderblast Trap
**Materials:** Tinker's tools and alchemist's supplies

**Requirements:** A place to arrange on a wall floor, or ceiling.

**Activation Range:** 5 feet

**Activation Effect:** A blast of air pressure releases from the trap, causing each creature within 10 feet of the trap to make a Strength saving throw. On a failed saving throw, a creature takes ld8 thunder damage, is pushed 10 feet, and is knocked prone. This damage increases to 2d8 at 7th level to 3d8 damage at 13th level and to 4d8 at 19th level.

### Web Trap
**Materials:** Thieves' tools and alchemist's supplies

**Requirements:** A place to arrange on a wall or floor, or in a locked object.

**Activation Range:** 5 feet

**Activation Effect:** A burst of sticky webbing releases from the trap, covering each creature within 10 feet of the trap and forcing them to make a Dexterity saving throw. On a failed saving throw, a creature is grappled by the trap (the escape DC is your Trap DC) and restrained while it is grappled in this way. 
