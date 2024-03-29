# Monastic Tradition: Way of the Long Death
Monks of the Way of the Long Death are obsessed with the meaning and mechanics of dying. They capture creatures and prepare elaborate experiments to capture, record, and understand the moments of their demise. They then use this knowledge to guide their understanding of martial arts, yielding a deadly fighting style.

Owing to their rather macabre interests, monasteries dedicated to the Way of the Long Death are often not welcome near settlements; however, many of the Long Death adherents can be found in the *hospitals* of the [Way of Mercy](Mercy.md), as the study of death is equally important to both Traditions. Masters of Mercy will frequently take on a Long Death student, and Masters of the Long Death will frequently reciprocate. Additionally, Long Death monks will often accompany Mercy monks as escorts and sparring partners when Mercy must travel to far-off places.

Masters of the Long Death are also frequently found in the company of magi of the [Night's Blessing](../../Organizations/MageSchools/NightsBlessing.md) and sometimes the [Twilight Star](../../Organizations/MageSchools/TwilightStar.md), and, less often, as part of several [mercenary companies](../../Organizations/MercCompanies/MercCompanies.md).

```
name = 'Way of the Long Death'
description = "***Monastic Tradition: Way of the Long Death.*** Monks of the Way of the Long Death are obsessed with the meaning and mechanics of dying. They capture creatures and prepare elaborate experiments to capture, record, and understand the moments of their demise. They then use this knowledge to guide their understanding of martial arts, yielding a deadly fighting style."
```

## Touch of Death
*3rd-level Way of the Long Death feature*

Your study of death allows you to extract vitality from another creature as it nears its demise. When you reduce a creature within 5 feet of you to 0 hit points, you gain temporary hit points equal to your Wisdom modifier + your monk level (minimum of 1 temporary hit point).

```
def level3(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Touch of Death.*** When you reduce a creature within 5 feet of you to 0 hit points, you gain {npc.WISbonus() + npc.levels('Monk')} temporary hit points.") )
```

## Hour of Reaping
*6th-level Way of the Long Death feature*

You gain the ability to unsettle or terrify those around you as an action, for your soul has been touched by the shadow of death. When you take this action, each creature within 30 feet of you that can see you must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.

```
def level6(npc):
    npc.actions.append(f"***Hour of Reaping.*** Each creature within 30 feet of you that can see you must succeed on a Wisdom saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}) or be frightened of you until the end of your next turn.")
```

## Mastery of Death
*11th-level Way of the Long Death feature*

You use your familiarity with death to escape its grasp. When you are reduced to 0 hit points, you can expend 1 ki point (no action required) to have 1 hit point instead.

```
def level11(npc):
    npc.traits.append("***Ki: Mastery of Death.*** When you are reduced to 0 hit points, you can expend 1 ki point (no action required) to have 1 hit point instead.")
```

## Touch of the Long Death
*17th-level Way of the Long Death feature*

Your touch can channel the energy of death into a creature. As an action, you touch one creature within 5 feet of you, and you expend 1 to 10 ki points. The target must make a Constitution saving throw, and it takes 2d10 necrotic damage per ki point spent on a failed save, or half as much damage on a successful one.

```
def level17(npc):
    npc.actions.append("***Ki: Touch of the Long Death.*** You touch one creature within 5 feet of you, and you expend 1 to 10 ki points. The target must make a Constitution saving throw (DC {8 + npc.WISbonus() + npc.proficiencybonus()}), taking 2d10 necrotic damage per ki point spent on a failed save, or half as much damage on a successful one.")
```
