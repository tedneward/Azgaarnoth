# Druidic Circle: Circle of Dreams
Druids who are members of the Circle of Dreams hail from regions that have strong ties to the Feywild. The druids' guardianship of the natural world makes for a natural alliance between them and good-aligned fey. These druids seek to fill the world with merriment and light. Their magic mends wounds and brings joy to downcast hearts, and the realms they protect are gleaming, fruitful places.

```
name = 'Circle of Dreams'
description = "***Druidic Circle: Circle of Dreams.*** Druids who are members of the Circle of Dreams hail from regions that have strong ties to the Feywild. The druids' guardianship of the natural world makes for a natural alliance between them and good-aligned fey. These druids seek to fill the world with merriment and light. Their magic mends wounds and brings joy to downcast hearts, and the realms they protect are gleaming, fruitful places."
```

## Balm of the Summer Court
*2nd-level Circle of Dreams feature*

You become imbued with the blessings of the Summer Court. You are a font of energy that lends relief to weary feet and respite from injuries. You have a pool of fey energy represented by a number of d6s equal to your druid level.

As a bonus action, you can choose an ally you can see within 120 feet of you and spend a number of those dice equal to half your druid level or less. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent, and its speed increases by 5 feet per die spent. The speed increase lasts for 1 minute.
You regain the expended dice when you finish a long rest.

```
def level2(npc):
    def assignfeydice(npc): npc.feydice = npc.levels('Druid')
    npc.defer(lambda npc: assignfeydice(npc) )
    npc.defer(lambda npc: npc.traits.append(f"***Balm of the Summer Court (Recharges on long rest).*** You become imbued with the blessings of the Summer Court. You are a font of energy that lends relief to weary feet and respite from injuries. You have a pool of fey energy represented by {npc.feydice} d6s.") )
    npc.defer(lambda npc: npc.bonusactions.append(f"***Balm of the Summer Court.*** You choose an ally you can see within 120 feet of you and spend {npc.levels('Druid') // 2} or less dice. Roll the spent dice and add them together. The target regains a number of hit points equal to the total. The target also gains 1 temporary hit point per die spent, and its speed increases by 5 feet per die spent. The speed increase lasts for 1 minute.") )
```

## Hearth of Moonlight and Shadow 
*6th-level Circle of Dreams feature*

Home is wherever you set up camp. During a short or long rest, you can invoke the shadowy power of the Gloaming Court to ward your campsite from intruders. At the start of the rest, you create an area with a 30-foot radius. Within this area, you and your allies gain a +5 bonus to Wisdom (Perception) checks to detect creatures, and any light from open flames (campfire, torches, and the like) is not visible outside the area. These effects end when the rest finishes or when you leave the area.

```
def level6(npc):
    npc.traits.append("***Hearth of Moonlight and Shadow.*** During a short or long rest, you can invoke the shadowy power of the Gloaming Court to ward your campsite from intruders. At the start of the rest, you create an area with a 30-foot radius. Within this area, you and your allies gain a +5 bonus to Wisdom (Perception) checks to detect creatures, and any light from open flames (campfire, torches, and the like) is not visible outside the area. These effects end when the rest finishes or when you leave the area.")
```

## Hidden Paths
*10th-level Circle of Dreams feature*

You can use the hidden, unpredictable magical pathways that some fey use to traverse space in a blink of an eye. On your turn, you can teleport up to 30 feet to a spot you can see. Each foot of this teleportation costs 1 foot of your movement.

You can also use this feature to teleport someone else. As an action, you can teleport a willing ally you touch up to 30 feet to a point you can see.

Once you use either option---teleporting yourself or an ally--you can't use that option again until 1d4 rounds have passed.

```
def level10(npc):
    npc.actions.append("***Hidden Paths (Recharges in 1d4 rounds).*** You can teleport up to 30 feet to a spot you can see. Each foot of this teleportation costs 1 foot of your movement. You can also use this feature to teleport a willing ally (that you touch) up to 30 feet to a point you can see.")
```

## Purifying Light
*14th-level Circle of Dreams feature*

The favor of the Summer Court allows you to end spells that hamper you and your allies. When you cast a spell with a spell slot and it restores hit points to you or an ally this turn, you can simultaneously target the healed creature with dispel magic, using a spell slot with a level equal to the slot used to cast the healing spell.

You can use this feature three times, and you regain expended uses of it when you finish a long rest. If the healing spell targets more than one creature, you can use this feature on more than one at the same time, expending one use of it per creature.

```
def level14(npc):
    npc.traits.append(f"***Purifying Light (3/Recharges on long rest).*** When you cast a spell with a spell slot and it restores hit points to you or an ally this turn, you can simultaneously target the healed creature with {spelllinkify('dispel magic')}, using a spell slot with a level equal to the slot used to cast the healing spell. If the healing spell targets more than one creature, you can use this feature on more than one at the same time, expending one use of it per creature.")
```
