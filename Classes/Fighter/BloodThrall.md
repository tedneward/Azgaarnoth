# Martial Archetype: Blood Thrall
Blood thralls learn to draw strength from the dark gifts bestowed upon them by the perverse beings who once bound them to service. It requires a deep inner resolve to wield these dark boons without succumbing to savagery. Within the deepest reaches of night, bound once through blood to serve a vampire, demonic overlord, or even a mage or sorcerer well-versed in the power inherent in blood, you linger in a realm of madness from which few ever return. The strength of your dark master pulsates through your veins and whether from a forbidden ritual or enthralling kiss, it empowers your resolve. Though free from loathsome servitude, the haunting voice of your master forever beckons you to return.

However, the common folk--and even many of the nobility--deeply distrust the Blood Thrall, both because of the influence once held (or worse, currently held) by that patron. Even if the Blood Thrall can convince others that the patron holds no influence, the sight of a Blood Thrall drawing nourishment and power from the blood of its enemies is enough to set even the stoutest heart in flight.

```
name = 'Blood Thrall'
description = "***Martial Archetype: Blood Thrall.*** Within the deepest reaches of night, bound through blood to serve a vampire or demonic overlord, or even a mage or sorcerer well-versed in the power inherent in blood, you linger in a realm of madness from which few ever return. The strength of your dark master pulsates through your veins and whether from a forbidden ritual or enthralling kiss, it empowers your resolve."
```

## Blood Drinker
*3rd-level Blood Thrall feature*

You can gain nourishment from the blood of your victims. When you hit a living creature with a melee weapon attack, your attack deals an extra 1d8 points of damage. If the target is Large or smaller, it must also make a Strength saving throw. On a failed save, you gain temporary hit points equal to the roll of your extra damage + your Strength or Dexterity modifier (your choice).

**Blood Drinker save DC** = 8 + your proficiency bonus + your Strength or Dexterity modifier (your choice).

You can use this feature twice between rests and only once a turn. Once you expended all uses of this feature, you must finish a short or long rest before you can use it again.

At 10th level, the extra damage die becomes a d10. At 18th level, it becomes a d12.

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Blood Drinker (2/Recharges on short or long rest).*** You gain nourishment from your victims. When you hit a living creature with a melee weapon attack, your attack deals an extra 1d{8 if npc.levels('Fighter') < 10 else 10 if npc.levels('Fighter') < 18 else 12} points of damage. If the target is Large or smaller, it must also make a Strength saving throw (DC {8 + npc.proficiencybonus() + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}).{'Creatures have a disadvantage to Strength saving throws.' if npc.levels('Fighter') >= 15 else ''} On a failed save, you gain temporary hit points equal to the roll of your extra damage + {npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus()}.") )
```

## Dark Gift
*7th-level Blood Thrall feature*

You learn to draw upon the blood of your patron that still courses through your veins. You gain one of the following features of your choice.

**Aberrant Climber.** As a bonus action, you gain a climbing speed equal to your current speed until the end of your turn.

**Celerity.** You can take a bonus action on each of your turns in combat to take the Dash action.

**Charming Gaze.** You can cast [charm person](http://azgaarnoth.tedneward.com/magic/spells/charm-person/) as a 1st-level spell. Once you use this feature, you cannot use it again until you finish a rest.

**Gaze of the Hunter.** As a bonus action, one creature within 5 feet cannot make an opportunity attack until the start of your next turn. Creatures immune to the charmed condition are unaffected by gaze of the hunter.

**Dark Sight.** You can cast [darkvision](http://azgaarnoth.tedneward.com/magic/spells/darkvision/) on yourself at will, without expending material components.

**Freed Mind.** You have advantage on saving throws against being charmed.

**Shadow Life.** When a target fails its Strength saving throw against your blood drinker feature, you gain 5 additional temporary hit points.

```
def level7(npc):
    choice = choose("Choose a feature: ", ['Aberrant Climber', 'Celerity', 'Charming Gaze', 'Gaze of the Hunter', 'Dark Sight', 'Freed Mind', 'Shadow Life'])
    if choice == 'Aberrant Climber':
        npc.bonusactions.append("***Aberrant Climber.*** You gain a climbing speed euqal to your current speed until the end of your turn.")
    elif choice == 'Celerity':
        npc.bonusactions.append("***Celerity.*** You can take the Dash action.")
    elif choice == 'Charming Gaze':
        npc.actions.append(f"***Charming Gaze (Recharges on short or long rest).*** You can cast {spelllinkify('charm person')} as a 1st-level spell.")
    elif choice == 'Gaze of the Hunter':
        npc.bonusactions.append("***Gaze of the Hunter.*** One creature within 5 feet cannot make an opportunity attack until the start of your next turn. Creatures immune to the charmed condition are unaffected by this.")
    elif choice == 'Dark Sight':
        npc.actions.append(f"***Dark Sight.*** You can cast {spelllinkify('darkvision')} on yourself at will, without expending material components.")
    elif choice == 'Freed Mind':
        npc.traits.append("***Freed Mind.*** You have advantage on saving throws against being charmed.")
    elif choice == 'Shadow Life':
        npc.defer(lambda npc: replace("***Blood Drinker", npc.traits, f" (2/Recharges on short or long rest).*** You gain nourishment from your victims. When you hit a living creature with a melee weapon attack, your attack deals an extra 1d{8 if npc.levels('Fighter') < 10 else 10 if npc.levels('Fighter') < 18 else 12} points of damage. If the target is Large or smaller, it must also make a Strength saving throw. On a failed save, you gain temporary hit points equal to the roll of your extra damage + {5 + (npc.STRbonus() if npc.STRbonus() > npc.DEXbonus() else npc.DEXbonus())}.") )
```

## Shadowed Blood
*10th-level Blood Thrall feature*

When you use the Second Wind feature while you are in darkness, you can regain hit points equal to 2d6 + your fighter level instead of normal.

At 18th level, the points you regain is instead equal to 2d8 + your fighter level.

```
def level10(npc):
    npc.defer(lambda npc: replace("***Second Wind", npc.bonusactions, f" (Recharges on short or long rest).*** On your turn, you can regain {'2d6' if npc.levels('Fighter') < 18 else '2d8'} + {npc.levels('Fighter')} hit points."))
```

## Dark Strength
*15th-level Blood Thrall feature*

Creatures have a disadvantage to Strength saving throws against your blood drinker feature.

Furthermore, whenever you gain temporary hit points, select one dark gift for every 5 points you receive. You benefit from the chosen dark gift until you no longer have temporary hit points.

```
def level15(npc):
    npc.traits.append("***Dark Strength.*** Whenever you gain temporary hit points, select one Dark Gift (Aberrant Climber, Celerity, Charming Gaze, Gaze of the Hunter, Dark Sight, Freed Mind, or Shadow Life) for every 5 points you receive. You benefit from the chosen Dark Gift until you no longer have temporary hit points.")
```

## Agile Evasion
*18th-level Blood Thrall feature*

You can use the Dodge action as a bonus action. Once you use this feature, you must finish a short or long rest before you can use it again.

```
def level18(npc):
    npc.bonusactions.append("***Agile Evasion (Recharges on short or long rest).*** You can use the Dodge action.")
```
