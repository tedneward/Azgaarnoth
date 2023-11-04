# Mystic Order: Order of the Immortal
The Order of the Immortal uses psionic energy to augment and modify the physical form. Followers of this order are known as Immortals. They use psionic energy to modify their bodies, strengthening them against attack and turning themselves into living weapons.

Their mastery of the physical form grants them their name, for Immortals are notoriously difficult to kill.

```
name = 'Order of the Immortal'
description = "***Mystic Order: Order of the Immortal.*** The Order of the Immortal uses psionic energy to augment and modify the physical form. Followers of this order are known as Immortals. They use psionic energy to modify their bodies, strengthening them against attack and turning themselves into living weapons."
```

## Bonus Disciplines
*1st-level Order of the Immortal feature*

You learn two additional psionic disciplines of your choice. They must be chosen from among the Immortal disciplines.

```
def level1(npc):
    allclasses['Mystic'].choosediscipline(npc, immortaldisciplines)
    allclasses['Mystic'].choosediscipline(npc, immortaldisciplines)
```

## Immortal Durability
*1st-level Order of the Immortal feature*

Your hit point maximum increases by 1 per mystic level.

In addition, while you aren't wearing armor or wielding a shield, your base AC equals 10 + your Dexterity modifier + your Constitution modifier.

```
    def boosthp(npc): npc.hitpoints += npc.levels('Mystic')
    npc.defer(lambda npc: boosthp(npc) )

    npc.defer(lambda npc: npc.traits.append("***Immortal Durability.*** While you aren't wearing armor or wielding a shield, your base AC equals {10 + npc.DEXbonus() + npc.CONbonus()}.") )
    def boostac(npc): npc.armorclass['Immortal Durability'] = 10 + npc.DEXbonus() + npc.CONbonus()
    npc.defer(lambda npc: boostac(npc) )
```

## Psionic Resilience
*3rd-level Order of the Immortal feature*

Your psionic energy grants you extraordinary fortitude. At the start of each of your turns, you gain temporary hit points equal to your Intelligence modifier (minimum of 0) if you have at least 1 hit point.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Psionic Resilience.*** At the start of each of your turns, you gain {npc.INTbonus()} temporary hit points if you have at least 1 hit point.") )
```

## Surge of Health
*6th-level Order of the Immortal feature*

You can draw on your psychic focus to escape death's grasp. As a reaction when you take damage, you can halve that damage against you. Your psychic focus immediately ends if it's active, and you can't use it until you finish a short or long rest.

You can't use this feature if you can't use your psychic focus.

```
def level6(npc):
    npc.reactions.append("***Surge of Health (Recharges on short or long rest).*** When you take damage, you halve that damage against you. Your psychic focus immediately ends if it's active. You can't use this feature if you can't use your psychic focus.")
```

## Immortal Will
*14th-level Order of the Immortal feature*

You can draw on your reserves of psionic power to survive beyond death. At the end of your turn while at 0 hit points, you can spend 5 psi points to immediately regain a number of hit points equal to your mystic level + your Constitution modifier.

```
def level14(npc):
    npc.defer(lambda npc: npc.traits.append("***Immortal Will.*** You can draw on your reserves of psionic power to survive beyond death. At the end of your turn while at 0 hit points, you can spend 5 psi points to immediately regain {npc.levels('Mystic') + npc.CONbonus()} hit points.") )
```

## Immortal Psionic Disciplines

* [adaptive body](Disciplines/adaptive-body.md)
* [bestial form](Disciplines/bestial-form.md)
* [brute force](Disciplines/brute-force.md)
* [celerity](Disciplines/celerity.md)
* [corrosive metabolism](Disciplines/corrosive-meltdown.md)
* [diminution](Disciplines/diminution.md)
* [giant growth](Disciplines/giant-growth.md)
* [iron durability](Disciplines/iron-durability.md)
* [psionic restoration](Disciplines/psionic-restoration.md)
* [psionic weapon](Disciplines/psionic-weapon.md)

```
def adaptivebody(npc):
    npc.bonusactions.append("***Psychic Focus: Adaptive Body.*** While focused on this discipline, you don’t need to eat, breathe, or sleep. To gain the benefits of a long rest, you can spend 8 hours engaged in light activity, rather than sleeping during any of it. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Environmental Adaptation (2 psi).*** You or a creature you touch ignores the effects of extreme heat or cold (but not cold or fire damage) for the next hour.")

    npc.reactions.append("***Adaptive Shield (3 psi).*** When you take acid, cold, fire, lightning, or thunder damage, you gain resistance to damage of that type--including the triggering damage--until the end of your next turn.")

    npc.actions.append("***Energy Adaptation (5 psi; concentration, 1 hr.).*** You touch one creature and give it resistance to acid, cold, fire, lightning, or thunder damage (your choice), which lasts until your concentration ends.")

    npc.actions.append("***Energy Immunity (7 psi; concentration, 1 hr.).*** You touch one creature and give it immunity to acid, cold, fire, lightning, or thunder damage (your choice), which lasts until your concentration ends.")

def bestialform(npc):
    npc.bonusactions.append("***Psychic Focus: Bestial Form.*** While focused on this discipline, you have advantage on Wisdom (Animal Handling) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.defer(lambda npc: npc.actions.append(f"***Bestial Claws (1–7 psi).*** You manifest long claws for an instant and make a melee weapon attack. *Melee Weapon Attack:* +{npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d10/psi point spent slashing damage.") )

    npc.bonusactions.append("***Bestial Transformation.*** As a bonus action, you alter your physical form to gain different characteristics. When you use this ability, you can choose one or more of the following effects: **Amphibious (2 psi)**. You gain gills, enabling you to breathe air and water; **Climbing (2 psi)**. You grow tiny hooked claws that give you gain a climbing speed equal to your walking speed; **Flight (5 psi)**. Wings sprout from your back, giving you a flying speed equal to your walking speed; **Keen Senses (2 psi)**. Your eyes and ears become more sensitive, giving you advantage on Wisdom (Perception) checks; **Perfect Senses (3 psi)**. You gain a keen sense of smell and an instinct to detect prey, enabling you to see invisible creatures and objects within 10 feet of you, even if you are blinded; **Swimming (2 psi)**. You gain fins and webbing between your fingers and toes, granting you a swimming speed equal to your walking speed; **Tough Hide (2 psi)**. Your skin becomes as tough as leather, granting you a +2 bonus to AC. Add the psi costs together to determine the total cost. This transformation lasts for 1 hour, until you die, or until you end it as a bonus action.")

def bruteforce(npc):
    npc.bonusactions.append("***Psychic Focus: Brute Force.*** While focused on this discipline, you have advantage on Strength (Athletics) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Brute Strike (1–7 psi).*** You gain a bonus to your next damage roll against a target you hit with a melee attack during the current turn. The bonus equals +1d6 per psi point spent, and the bonus damage is the same type as the attack. If the attack has more than one damage type, you choose which one to use for the bonus damage.")

    npc.reactions.append("***Knock Back (1–7 psi).*** When you hit a target with a melee attack, you can activate this ability as a reaction. The target must succeed on a Strength saving throw or be knocked 10 feet away from you per psi point spent. The target moves in a straight line. If it hits an object, this movement immediately ends and the target takes 1d6 bludgeoning damage per psi point spent.")

    npc.actions.append("***Mighty Leap (1–7 psi).*** As part of your movement, you jump in any direction up to 20 feet per psi point spent.")

    npc.bonusactions.append("***Feat of Strength (2 psi).*** As a bonus action, you gain a +5 bonus to Strength checks until the end of your next turn.")

def celerity(npc):
    npc.bonusactions.append("***Psychic Focus: Celerity.*** While focused on this discipline, your walking speed increases by 10 feet. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Rapid Step (1–7 psi).*** You increase your walking speed by 10 feet per psi point spent until the end of the current turn. If you have a climbing or swimming speed, this increase applies to that speed as well.")

    npc.bonusactions.append("***Agile Defense (2 psi).*** You take the Dodge action.")

    npc.actions.append("***Blur of Motion (2 psi).*** You cause yourself to be invisible during any of your movement during the current turn.")

    npc.bonusactions.append("***Surge of Speed (2 psi).*** You gain two benefits until the end of the current turn: you don’t provoke opportunity attacks, and you have a climbing speed equal to your walking speed.")

    npc.bonusactions.append("***Surge of Action (5 psi).*** As a bonus action, you can Dash or make one weapon attack.")

def corrosivemetabolism(npc):
    npc.bonusactions.append("***Psychic Focus: Corrosive Metabolism.*** While focused on this discipline, you have resistance to acid and poison damage. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Corrosive Touch (1–7 psi).*** You deliver a touch of acid to one creature within your reach. The target must make a Dexterity saving throw, taking 1d10 acid damage per psi point spent on a failed save, or half as much damage on a successful one.")

    npc.actions.append("***Venom Strike (1–7 psi).*** You create a poison spray that targets one creature you can see within 30 feet of you. The target must make a Constitution saving throw. On a failed save, it takes 1d6 poison damage per psi point spent and is poisoned until the end of your next turn. On a successful save, the target takes half as much damage and isn’t poisoned.")

    npc.reactions.append("***Acid Spray (2 psi).*** When you take piercing or slashing damage, you cause acid to spray from your wound; each creature within 5 feet of you takes 2d6 acid damage.")

    npc.actions.append("***Breath of the Black Dragon (5 psi).*** You exhale a wave of acid in a 60-foot line that is 5 feet wide. Each creature in the line must make a Constitution saving throw, taking 6d6 acid damage on a failed save, or half as much on a successful one. You can increase the damage by 1d6 per additional psi point spent on it.")

    npc.actions.append("***Breath of the Green Dragon (7 psi).*** You exhale a cloud of poison in a 90-foot cone. Each creature in the line must make a Constitution saving throw, taking 10d6 poison damage on a failed save, or half as much damage on a successful one.")

def diminution(npc):
    npc.bonusactions.append("***Psychic Focus: Diminution.*** While focused on this discipline, you have advantage on Dexterity (Stealth) checks. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Miniature Form (2 psi; concentration, 10 min.).*** You become Tiny until your concentration ends. While this size, you gain a +5 bonus to Dexterity (Stealth) checks and can move through gaps up to 6 inches across without squeezing.")

    npc.bonusactions.append("***Toppling Shift (2 psi).*** You shift to an incredibly small size and then suddenly return to normal, sending an opponent flying backward. Choose one creature you can see within 5 feet of you. It must succeed on a Strength saving throw or be knocked prone.")

    npc.reactions.append("***Sudden Shift (5 psi).*** When you are hit by an attack, you shift down to minute size to avoid the attack. The attack misses, and you move up to 5 feet without provoking opportunity attacks before returning to normal size.")

    npc.bonusactions.append("***Microscopic Form (7 psi; concentration, 10 min.).*** You become smaller than Tiny until your concentration ends. While this size, you gain a +10 bonus to Dexterity (Stealth) checks and a +5 bonus to AC, you can move through gaps up to 1 inch across without squeezing, and you can’t make weapon attacks.")

def giantgrowth(npc):
    npc.bonusactions.append("***Psychic Focus: Giant Growth.*** While focused on this discipline, your reach increases by 5 feet. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.bonusactions.append("***Ogre Form (2 psi; concentration, 1 min.).*** You gain 10 temporary hit points. In addition, until your concentration ends, your melee weapon attacks deal an extra 1d4 bludgeoning damage on a hit, and your reach increases by 5 feet. If you’re smaller than Large, you also become Large for the duration.")

    npc.bonusactions.append("***Giant Form (7 psi; concentration, 1 min.).*** You gain 30 temporary hit points. In addition, until your concentration ends, your melee weapon attacks deal an extra 2d6 bludgeoning damage on a hit, and your reach increases by 10 feet. If you’re smaller than Huge, you also become Huge for the duration.")

def irondurability(npc):
    npc.bonusactions.append("***Psychic Focus: Iron Durability.*** While focused on this discipline, you gain a +1 bonus to AC. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.reactions.append("***Iron Hide (1–7 psi).*** When you are hit by an attack, you gain a +1 bonus to AC for each psi point you spend on this ability. The bonus lasts until the end of your next turn. This bonus applies against the triggering attack.")

    npc.bonusactions.append("***Steel Hide (2 psi).*** You gain resistance to bludgeoning, piercing, and slashing damage until the end of your next turn.")

    npc.actions.append("***Iron Resistance (7 psi; concentration, 1 hr.).*** You gain resistance to bludgeoning, piercing, or slashing damage (your choice), which lasts until your concentration ends.")

def psionicrestoration(npc):
    npc.bonusactions.append("***Psychic Focus: Psionic Restoration.*** While focused on this discipline, you can touch a creature that has 0 hit points and stabilize it. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.")

    npc.actions.append("***Mend Wounds (1–7 psi).*** You spend psi points to restore hit points to one creature you touch. The creature regains 1d8 hit points per psi point spent.")

    npc.actions.append("***Restore Health (3 psi).*** You touch one creature and remove one of the following conditions from it: blinded, deafened, paralyzed, or poisoned. Alternatively, you remove one disease from the creature.")

    npc.actions.append("***Restore Life (5 psi).*** You touch one creature that has died within the last minute. The creature returns to life with 1 hit point. This ability can’t return to life a creature that has died of old age, nor can it restore a creature missing any vital body parts.")

    npc.actions.append("***Restore Vigor (7 psi).*** You touch one creature and choose one of the following: remove any reductions to one of its ability scores, remove one effect that reduces its hit point maximum, or reduce its exhaustion level by one.")

def psionicweapon(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Psychic Focus: Psionic Weapon.*** Whenever you focus on this discipline, choose one weapon you’re holding or your Unarmed Strike. When you attack with it while focused on this discipline, its damage is psychic and magical, rather than its normal damage type{', and you add either your Strength or Dexterity modifier to the damage rolls' if npc.levels('Mystic') >= 6 else ''}. The benefit lasts until you are incapacitated or until you use another bonus action to choose a different focus benefit. You can have only one psychic focus benefit at a time, and using the psychic focus of one discipline doesn't limit your ability to use other disciplines.") )

    npc.bonusactions.append("***Ethereal Weapon (1 psi).*** You temporarily transform one weapon you’re holding or your unarmed strike into pure psionic energy. The next attack you make with it before the end of your turn ignores the target’s armor, requiring no attack roll. Instead, the target makes a Dexterity saving throw against this discipline. On a failed save, the target takes the attack’s normal damage and suffers its additional effects. On a successful save, the target takes half damage from the attack but suffers no additional effects that would normally be imposed on a hit.")

    npc.bonusactions.append("***Lethal Strike (1–7 psi).*** You imbue a weapon you’re holding or your unarmed strike with psychic energy. The next time you hit with it before the end of your turn, it deals an extra 1d10 psychic damage per psi point spent.")

    npc.bonusactions.append("***Augmented Weapon (5 psi; concentration, 10 min.).*** Touch one simple or martial weapon. Until your concentration ends, that weapon becomes a magic weapon with a +3 bonus to its attack and damage rolls.")

immortaldisciplines = {
    'Adaptive Body': adaptivebody,
    'Bestial Form': bestialform,
    'Brute Force': bruteforce,
    'Celerity': celerity,
    'Corrosive Metabolism': corrosivemetabolism,
    'Diminution': diminution,
    'Giant Growth': giantgrowth,
    'Iron Durability': irondurability,
    'Psionic Restoration': psionicrestoration,
    'Psionic Weapon': psionicweapon
}
for ad in immortaldisciplines:
    allclasses['Mystic'].disciplines[ad] = immortaldisciplines[ad]
```
