# Mark of Scribing
The Mark of Scribing deals with communication---both the written and spoken word. A gnome who bears the mark can feel words as though they are living creatures, struggling to make their meaning known. The mark provides a range of gifts. It translates languages, but it also allows its bearer to speak to others at a distance and to inscribe their words wherever they wish.

```
name = 'Scribing Dragonmarked'
```

### Traits
The Mark of Scribing manifests exclusively on gnomes. If your character has the Mark of Scribing, this is your gnome subrace. 

**Ability Score Increase.** Your Charisma score increases by 1.

**Gifted Scribe**. You are proficient with calligrapher's supplies and forgery kits. When you make an ability check using either one of these tools, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

**Scribe's Insight**. You can cast [comprehend languages](../Magic/Spells/comprehend-languages.md) once with this trait, and you regain the ability to do so when you finish a long rest. Intelligence is your spellcasting ability for it.

**Whispering Wind**. You know the [message](../Magic/Spells/message.md) cantrip. Intelligence is your spellcasting ability for it.

**Extra Language**. You can speak, read, and write one extra language of your choice.

```
def level0(npc):
    npc.CHA += 1

    npc.proficiencies.append("Calligrapher's supplies")
    npc.proficiencies.append("Forgery kit")
    npc.traits.append("***Gifted Scribe.*** When you make an ability check using either calligrapher's supplies or forgery kits, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    npc.newspellcasting('Dragonmark', 'INT').cantripsknown.append('message')
    npc.spellcasting['Dragonmark'].spells[1].append('comprehend languages')
    npc.spellcasting['Dragonmark'].slots = [ 1 ]

    npc.languages.append("CHOOSE")
```
