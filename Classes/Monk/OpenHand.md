# Monastic Tradition: Way of the Open Hand
Monks of the Way of the Open Hand are the ultimate masters of martial arts combat, whether armed or unarmed. They learn techniques to push and trip their opponents, manipulate ki to heal damage to their bodies, and practice advanced meditation that can protect them from harm.

Open Hand monks are some of the easiest to find, and their monasteries equally so; many are found in cities (though heavily cordoned off from the city outside), and several are in fact attached to a [dueling college](../../Organizations/DuelingColleges.md) for a variety of reasons (both economical and spiritual). In [Yithi](../../Nations/Yithi.md) and [Zhi](../../Nations/Zhi.md), Open Hand monks and [Kensai](Kensai.md) monks are frequently found sparring against one another in friendly competition, though at times it has been known to get "personal" between duelists.

Many [mercenary companies](../../Organizations/MercCompanies/MercCompanies.md) employ Open Hand monks, frequently as teachers, however, rather than front-line troops.

```
name = 'Way of the Open Hand'
description = "***Monastic Tradition: Way of the Open Hand.*** Monks of the Way of the Open Hand are the ultimate masters of martial arts combat, whether armed or unarmed. They learn techniques to push and trip their opponents, manipulate ki to heal damage to their bodies, and practice advanced meditation that can protect them from harm."
```

## Open Hand Technique
*3rd-level Way of the Open Hand feature*

You can manipulate your enemy's ki when you harness your own. Whenever you hit a creature with one of the attacks granted by your Flurry of Blows, you can impose one of the following effects on that target:

* It must succeed on a Dexterity saving throw or be knocked prone.

* It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you.

* It can't take reactions until the end of your next turn.

```
def level3(npc):
    for ba in npc.bonusactions:
        if ba[0:26] == "***Ki: Flurry of Blows.***":
            npc.bonusactions.remove(ba)
    npc.bonusactions.append("***Ki: Flurry of Blows: Open Hand Technique.*** Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two Unarmed Strikes. Whenever you hit a creature with one of these attacks, you can impose one of the following effects on that target: It must succeed on a Dexterity saving throw or be knocked prone; It must make a Strength saving throw. If it fails, you can push it up to 15 feet away from you; or it can't take reactions until the end of your next turn.")
```

## Wholeness of Body
*6th-level Way of the Open Hand feature*

You gain the ability to heal yourself. As an action, you can regain hit points equal to three times your monk level. You must finish a long rest before you can use this feature again.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Wholeness of Body (Recharge on long rest).*** You can regain {3 * npc.levels('Monk')} hit points."))
```

## Tranquility
*11th-level Way of the Open Hand feature*

You can enter a special meditation that surrounds you with an aura of peace. At the end of a long rest, you gain the effect of a Sanctuary spell that lasts until the start of your next long rest (the spell can end early as normal). The saving throw DC for the spell equals 8 + your Wisdom modifier + your proficiency bonus.

```
def level11(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Tranquility.*** At the end of a long rest, you gain the effect of a {spelllinkify('sanctuary')} spell (save DC {8 + npc.WISbonus() + npc.proficiencybonus()}) that lasts until the start of your next long rest (the spell can end early as normal).") )
```

## Quivering Palm
*17th-level Way of the Open Hand feature*

You gain the ability to set up lethal vibrations in someone's body. When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage.

You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action.

```
def level17(npc):
    npc.traits.append("***Ki: Quivering Palm.*** When you hit a creature with an unarmed strike, you can spend 3 ki points to start these imperceptible vibrations, which last for a number of days equal to your monk level. The vibrations are harmless unless you use your action to end them. To do so, you and the target must be on the same plane of existence. When you use this action, the creature must make a Constitution saving throw. If it fails, it is reduced to 0 hit points. If it succeeds, it takes 10d10 necrotic damage. You can have only one creature under the effect of this feature at a time. You can choose to end the vibrations harmlessly without using an action.")
```
