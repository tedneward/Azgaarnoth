# [Yuan-Ti](../Creatures/YuanTi.md)

```
name = 'Yuan-Ti'
description = "***Race: Yuan-Ti.*** You're a cold-blooded snake..."
type = 'humanoid'
```

* **Ability Score Increase**. Your Charisma score increases by 2, and your Intelligence score increases by 1.

```
def level0(npc):
    npc.CHA += 2
    npc.INT += 1
```

* **Age**. Purebloods mature at the same rate as humans and have lifespans similar in length to theirs.

* **Alignment**. Purebloods are devoid of emotion and see others as tools to manipulate. They care little for law or chaos and are typically neutral evil.

* **Size**. Purebloods match humans in average size and weight. Your size is Medium.

```
    npc.size = 'Medium'
```

* **Speed**. Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

* **Darkvision**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

```
    npc.senses['darkvision'] = 60
```

* **Magic Resistance**. You have advantage on saving throws against spells and other magical effects.

```
    npc.traits.append("***Magic Resistance.*** You have advantage on saving throws against spells and other magical effects.")
```

* **Poison Immunity**. You are immune to poison damage and the poisoned condition.

```
    npc.damageimmunities.append('poison')
    npc.conditionimmunities.append('poisoned')
```

* **Languages**. You can speak, read, and write Common, Abyssal, and Draconic.

```
    npc.languages.append('Common')
    npc.languages.append('Abyssal')
    npc.languages.append('Draconic')
```

* **Innate Spellcasting**. You know the [poison spray](../Magic/Spells/poison-spray.md) cantrip. You can cast [animal friendship](../Magic/Spells/animal-friendship.md) an unlimited number of times with this trait, but you can target only snakes with it. Starting at 3rd level, you can also cast [suggestion](../Magic/Spells/suggestion.md) with this trait. Once you cast it, you can't do so again until you finish a long rest. Charisma is your spellcasting ability for these spells.

```
    npc.cantripsknown.append('poison spray')
    npc.actions.append(f"***Innate Spellcasting.*** Charisma is your spellcasting ability.\n>\n>* At will: {spelllinkify('animal friendship')}")

def level3(npc):
    replace("***Innate Spellcasting.***", npc.actions, " Charisma is your spellcasting ability.\n\n>* At will: {spelllinkify('animal friendship')}\n>* 1/day: {spelllinkify('suggestion')}")
```
