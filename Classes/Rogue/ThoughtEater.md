# Roguish Archetype: Thought Eater
Is there anything more delicious than a secret? Select investigators and blackmailers blessed with the powers of the feywild would contend that nothing is more desirable than emotion, which can be consumed to fuel magic, or simply leveraged against the original owner to bend them to your will.

```
name = 'Thought Eater'
description = "***Roguish Archetype: Thought Eater.*** Is there anything more delicious than a secret? Select investigators and blackmailers blessed with the powers of the feywild would contend that nothing is more desirable than emotion, which can be consumed to fuel magic, or simply leveraged against the original owner to bend them to your will."
```

## Voiceless Cries
*3rd-level Thought Eater feature*

You passively siphon the background thoughts of the creatures you meet throughout the day, learning what is most on their mind in that moment. This is considered a form of telepathy, but gives you no ability to probe for specific information. Questions verbally directed at the target creature naturally shape the course of its thoughts.

Additionally, you can consume particiularly strong emotions you detect with this ability. As a bonus action, you can end the Frightened or Charmed condition on a creature within 30 feet of you.

```
def level3(npc):
    npc.traits.append("***Voiceless Cries.*** You passively siphon the background thoughts of the creatures you meet throughout the day, learning what is most on their mind in that moment. This is considered a form of telepathy, but gives you no ability to probe for specific information. Questions verbally directed at the target creature naturally shape the course of its thoughts.")
    npc.bonusactions.append("***Voiceless Cries.*** You can consume particiularly strong emotions you detect with this ability, so you can end the Frightened or Charmed condition on a creature within 30 feet of you.")
```

## Wingless Flutters
*9th-level Thought Eater feature*

You can the ability to harvest the thoughts of others, directing them at your whim. When you sense a thought or emotion (up to 25 words in length) with your Voiceless Cries ability, you may harvest it with this ability, and it begins to float around you on the ethereal plane, manifesting in an abstract, spectral form of your choosing. You can harvest a number of thoughts each day equal to your proficiency bonus. Unused thoughts fade away at dusk each day.

You use an action to cast a version of the sending spell which expends a harvested thought and delivers it to a target of your choice. This is considered a form of telepathy.

```
def level9(npc):
    npc.defer(lambda npc: npc.traits.append("***Wingless Flutters ({npc.proficiencybonus()}/Recharges at dawn).*** When you sense a thought or emotion (up to 25 words in length) with your Voiceless Cries ability, you may harvest it with this ability, and it begins to float around you on the ethereal plane, manifesting in an abstract, spectral form of your choosing. You can harvest a number of thoughts each day equal to your proficiency bonus. Unused thoughts fade away at dusk each day."))
    npc.action.append("***Wingless Flutters.*** You use an action to cast a version of the {spelllinkify('sending')} spell which expends a harvested thought and delivers it to a target of your choice. This is considered a form of telepathy.")
```

## Toothless bites
*13th-level Thought Eater feature*

You can use your magic to augment your attacks. You can expend a thought harvested by your Wingless Flutters ability to deal an extra 4d6 psychic damage on a successful melee weapon attack.

```
def level13(npc):
    npc.traits.append("***Toothless bites.*** You can expend a thought harvested by your Wingless Flutters ability to deal an extra 4d6 psychic damage on a successful melee weapon attack.")
```

## Mouthless Mutters
*17th-level Thought Eater feature*

You can extrude an aura of fey magic that causes all creatures within 30 feet of you to emit audible surface thoughts as per your Voiceless Cries ability for as long as they remain inside the area of effect, which remains centered on you until you choose to end it as a bonus action.

```
def level17(npc):
    npc.bonusactions.append("***Mouthless Mutters.*** You can extrude an aura of fey magic that causes all creatures within 30 feet of you to emit audible surface thoughts as per your Voiceless Cries ability for as long as they remain inside the area of effect, which remains centered on you until you choose to end it as a bonus action.")
```