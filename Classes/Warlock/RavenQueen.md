# Otherworldly Patron: Raven Queen
Your patron is the Raven Queen, a mysterious being who rules the Shadowfell from a palace of ice deep within that dread realm. The Raven Queen watches over the world, anticipating each creature's death and ensuring that it meets its end at the proscribed time and place. As the ruler of the Shadowfell, she dwells in a decayed, dark reflection of the world. Her ability to reach into the world is limited. Thus, she turns to mortal warlocks to serve her will. Warlocks sworn to the Raven Queen receive visions and whispers from her in their dreams, sending them on quests and warning them of impending dangers.

The Raven Queen's followers are expected to serve her will in the world. She concerns herself with ensuring that those fated to die pass from the world as expected, and bids her agents to defeat those who seek to cheat death through undeath or other imitations of immortality. She hates intelligent undead and expects her followers to strike them down, whereas mindless undead such as skeletons and zombies are little more than stumbling automatons in her eyes.

```
name = 'Raven Queen'
description = "***Otherworldly Patron: Raven Queen.*** Your patron is the Raven Queen, a mysterious being who rules the Shadowfell from a palace of ice deep within that dread realm. The Raven Queen watches over the world, anticipating each creature's death and ensuring that it meets its end at the proscribed time and place. As the ruler of the Shadowfell, she dwells in a decayed, dark reflection of the world. Her ability to reach into the world is limited. Thus, she turns to mortal warlocks to serve her will. Warlocks sworn to the Raven Queen receive visions and whispers from her in their dreams, sending them on quests and warning them of impending dangers."
```

## Expanded Spell List
The Raven Queen lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.

**Raven Queen Expanded Spells**
Spell Level|Spells
-----------|------
1st|[false life](../../Magic/Spells/false-life.md), [sanctuary](../../Magic/Spells/sanctuary.md)
2nd|[silence](../../Magic/Spells/silence.md), [spiritual weapon](../../Magic/Spells/spiritual-weapon.md)
3rd|[feign death](../../Magic/Spells/feign-death.md), [speak with dead](../../Magic/Spells/speak-with-dead.md)
4th|[ice storm](../../Magic/Spells/ice-storm.md), [locate creature](../../Magic/Spells/locate-creature.md)
5th|[commune](../../Magic/Spells/commune.md), [cone of cold](../../Magic/Spells/cone-of-cold.md)

## Sentinel Raven
*1st-level Raven Queen feature*

```
def level1(npc):
    npc.languages.append("Telepathy (30 ft)")

    npc.traits.append(f"***Expanded Spell List.*** The following are considered warlock spells for you: 1st: {spelllinkify('false life')}, {spelllinkify('sanctuary')}; 2nd: {spelllinkify('silence')}, {spelllinkify('spiritual weapon')}; 3rd: {spelllinkify('feign death')}, {spelllinkify('speak with dead')}, 4th: {spelllinkify('ice storm')}, {spelllinkify('locate creature')}; 5th: {spelllinkify('commune')}, {spelllinkify('cone of cold')}.") 
```

You gain the service of a spirit sent by the Raven Queen to watch over you. The spirit assumes the form and game statistics of a raven, and it always obeys your commands, which you can give telepathically while it is within 100 feet of you.

While the raven is perched on your shoulder, you gain darkvision with a range of 30 feet and a bonus to your passive Wisdom (Perception) score and to Wisdom (Perception) checks. The bonus equals your Charisma modifier. While perched on your shoulder, the raven can't be targeted by any attack or other harmful effect; only you can cast spells on it; it can't take damage; and it is incapacitated.

You can see through the raven's eyes and hear what it hears while it is within 100 feet of you.

In combat, you roll initiative for the raven and control how it acts. If it is slain by a creature, you gain advantage on all attack rolls against the killer for the next 24 hours.

The raven doesn't require sleep. While it is within 100 feet of you, it can awaken you from sleep as a bonus action.

The raven vanishes when it dies, if you die, or if the two of you are separated by more than 5 miles.

At the end of a short or long rest, you can call the raven back to you--no matter where it is or whether it died--and it reappears within 5 feet of you.

```
    npc.defer(lambda npc: npc.traits.append(f"***Raven Spirit (Re-forms on short or long rest).*** While the raven is perched on your shoulder, you gain a +{npc.CHAbonus()} bonus to your passive Wisdom (Perception) score and Wisdom (Perception) checks, and you gain darkvision with a range of 30 feet. While on your shoulder, it can't be targeted by any attack or other harmful effect, only you can cast spells on it, it can't take damage, and it is considered incapacitated until you instruct it to leave. You can see through the raven's eyes and hear what it hears while it is within 100 feet of you. In combat, you roll initiative for the raven and control how it acts. If it is slain by a creature, you gain advantage on all attack rolls against the killer for the next 24 hours.The raven doesn't require sleep. While it is within 100 feet of you, it can awaken you from sleep as a bonus action. The raven vanishes when it dies, if you die, or if the two of you are separated by more than 5 miles.At the end of a short or long rest, you can call the raven back to you--no matter where it is or whether it died--and it reappears within 5 feet of you.") )
```

## Soul of the Raven
*6th-level Raven Queen feature*

You gain the ability to merge with your raven spirit. As a bonus action when your raven is perched on your shoulder, your body merges with your raven's form. While merged, you become Tiny, you replace your speed with the raven's, and you can use your action only to Dash, Disengage, Dodge, Help, Hide, or Search. During this time, you gain the benefits of your raven being perched on your shoulder. As an action, you and the raven return to normal.

```
def level6(npc):
    npc.bonusactions.append("***Soul of the Raven.*** When your raven is perched on your shoulder, your body merges with your raven's form. While merged, you become Tiny, you replace your speed with the raven's, and you can use your action only to Dash, Disengage, Dodge, Help, Hide, or Search. During this time, you gain the benefits of your raven being perched on your shoulder. As an action, you and the raven return to normal.")
```

## Raven's Shield
*10th-level Raven Queen feature*

The Raven Queen grants you a protective blessing. You gain advantage on death saving throws, immunity to the frightened condition, and resistance to necrotic damage.

```
def level10(npc):
    npc.traits.append("***Raven's Shield.*** You gain advantage on death saving throws.")
    npc.conditionimmunities.append('frightened')
    npc.damageresistances.append('necrotic')
```

## Queen's Right Hand
*14th-level Raven Queen feature* 

You can channel the Raven Queen's power to slay a creature. You can cast Finger of Death. After you cast the spell with this feature, you can't do so again until you finish a long rest.

```
def leve14(npc):
    npc.actions.append("***Queen's Right Hand.*** You cast [finger of death](http://azgaarnoth.tedneward.com/magic/spells/finger-of-death/)")
```

*Source: [Unearthed Arcana: Warlock and Wizard](https://dnd.wizards.com/articles/unearthed-arcana/warlock-and-wizard)*
