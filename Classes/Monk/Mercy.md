# Monastic Tradition: Way of Mercy
Monks of the Way of Mercy learn to manipulate the life force of others to bring aid to those in need. They are wandering physicians to the poor and hurt. However, to those beyond their help--whether ailing or evil--they bring a swift end as an act of mercy.

Monks of Mercy are revered everywhere they travel when among the civilized lands, and no civilized creature on Azgaarnoth will deliberately attack a monk of Mercy without extreme provocation. Many Masters of Mercy travel with a small retinue of other Mercy monks as a sort of "traveling hospital" to the various villages, towns, cities, and holdings outside of major urban areas. The monks are also willing to take any sort--from the smallet kobold to the boldest giant--as an initiate, so long as they abide by the Laws of Mercy.

Monks of Mercy are frequently confused with Monks of Tranquility--at least until they don their masks, which they typically only do when providing mercy (of whatever sort)--and most creatures provide both the same degree of respect. Monks of Mercy and Tranquility are fierce opponents to one another, however, and often refuse to be within eyeshot/earshot of one another.

```
name = "Way of Mercy"
description = "***Monastic Tradition: Way of Mercy.*** Monks of the Way of Mercy learn to manipulate the life force of others to bring aid to those in need. They are wandering physicians to the poor and hurt. However, to those beyond their help--whether ailing or evil--they bring a swift end, as an act of mercy. Most distinctively, monks of Mercy don a mask when they dispense mercy--of either sort."
```

## Implements of Mercy
*3rd-level Way of Mercy feature*

You gain proficiency in the Insight and Medicine skills, and you gain proficiency with the herbalism kit.

You also gain a special mask, which you often wear when using the features of this subclass. You determine its appearance, or generate it randomly by rolling on the Merciful Mask table. 

**Merciful Mask**

d6 | Mask Appearance
-- | ---------------
 1 | Raven
 2 | Blank and white
 3 | Crying visage
 4 | Laughing visage
 5 | Skull
 6 | Butterfly

```
def level3(npc):
    npc.skills.append('Insight')
    npc.skills.append('Medicine')
    npc.proficiencies.append('Herbalism Kit')
    npc.traits.append("***Implements of Mercy.*** When dispensing mercy (either the beneficial kind or the ending kind), you don a mask of distinctive appearance.")
    npc.equipment.append("Mask of mercy. (CHOOSE: Raven; blank, white; crying visage; laughing visage; skull; butterfly; other)")
```

## Hand of Healing
*3rd-level Way of Mercy feature*

Your mystical touch can mend wounds. As an action, you can spend 1 ki point to touch a creature and restore a number of hit points equal to a roll of your Martial Arts die + your Wisdom modifier.

When you use your Flurry of Blows, you can replace one of the unarmed strikes with a use of this feature without spending a ki point for the healing.

```
    npc.defer(lambda npc: npc.actions.append(f"***Ki: Hand of Healing.*** You can spend 1 ki point to touch a creature and restore 1d{npc.martialartsdie} + {npc.WISbonus()} hitpoints. When you use your Flurry of Blows, you can replace {'one' if npc.levels('Monk') < 11 else 'all'} of the Unarmed Strikes with a use of this feature without spending a ki point for the healing.{' You can also end one disease or one of the following conditions affecting the creature: blinded, deafened, paralyzed, poisoned, or stunned.' if npc.levels('Monk') >= 6 else ''}") )
```

## Hands of Harm
*3rd-level Way of Mercy feature*

You use your ki to inflict wounds. When you hit a creature with an unarmed strike, you can spend 1 ki point to deal extra necrotic damage equal to one roll of your Martial Arts die + your Wisdom modifier. You can use this feature only once on each of your turns.

```
    npc.defer(lambda npc: npc.actions.append(f"***Ki: Hands of Harm.*** Once per turn, when you hit a creature with an Unarmed Strike, you can {'spend 1 ki point to ' if npc.levels('Monk') < 11 else ''}deal 1d{npc.martialartsdie} + {npc.WISbonus()} extra necrotic damage.{' You can subject that creature to the poisoned condition until the end of your next turn.' if npc.levels('Monk') >= 6 else ''}") )
```

## Physician's Touch
*6th-level Way of Mercy feature*

You can administer even greater cures with a touch, and if you feel it's necessary, you can use your knowledge to cause harm.

When you use Hand of Healing on a creature, you can also end one disease or one of the following conditions affecting the creature: blinded, deafened, paralyzed, poisoned, or stunned.

When you use Hand of Harm on a creature, you can subject that creature to the poisoned condition until the end of your next turn.

## Flurry of Healing and Harm
*11th-level Way of Mercy feature*

You can now mete out a flurry of comfort and hurt. When you use Flurry of Blows, you can now replace each of the unarmed strikes with a use of your Hand of Healing, without spending ki points for the healing.

In addition, when you make an unarmed strike with Flurry of Blows, you can use Hand of Harm with that strike without spending the ki point for Hand of Harm. You can still use Hand of Harm only once per turn.

## Hand of Ultimate Mercy
*17th-level Way of Mercy feature*

Your mastery of life energy opens the door to the ultimate mercy. As an action, you can touch the corpse of a creature that died within the past 24 hours and expend 5 ki points. The creature then returns to life, regaining a number of hit points equal to 4d10 + your Wisdom modifier. If the creature died while subject to any of the following conditions, it revives with them removed: blinded, deafened, paralyzed, poisoned, and stunned. 

Once you use this feature, you can't use it again until you finish a long rest. 

```
def level17(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Hand of Ultimate Mercy (Recharges on long rest).*** you can touch the corpse of a creature that died within the past 24 hours and expend 5 ki points. The creature then returns to life, regaining 4d10 + {npc.WISbonus()} hit points. If the creature died while blinded, deafened, paralyzed, poisoned, and/or stunned, it revives with those conditions removed.") )
```
