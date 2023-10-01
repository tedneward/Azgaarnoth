# Mark of Scribing
The Mark of Scribing deals with communication---both the written and spoken word. A gnome who bears the mark can feel words as though they are living creatures, struggling to make their meaning known. The mark provides a range of gifts. It translates languages, but it also allows its bearer to speak to others at a distance and to inscribe their words wherever they wish.

```
name = 'Scribing Dragonmarked'
description = "***Dragonmark: Mark of Scribing.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. The Mark of Scribing deals with communication---both the written and spoken word. A gnome who bears the mark can feel words as though they are living creatures, struggling to make their meaning known. The mark provides a range of gifts. It translates languages, but it also allows its bearer to speak to others at a distance and to inscribe their words wherever they wish."
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

    spellcasting = innatecaster(npc, 'INT', name)
    spellcasting.cantripsknown.append('message')
    spellcasting.perday[1] = []
    spellcasting.perday[1].append('comprehend languages')

    npc.languages.append("CHOOSE")

    quirk = random([
        "Your dragonmark is unusually small.",
        "Your dragonmark is remarkably large.",
        "Your dragonmark slowly moves around your body.",
        "Your dragonmark glows dramatically when you use it.",
        "Your dargonmark emits a soft hum when you use it.",
        "Your dragonmark itches when you’re near someone with a dragonmark.",
        "Your dragonmark tingles when you’re near someone with the same mark.",
        "Your dragonmark tickles when you use it.",
        "Your dragonmark is an unusual color but a normal shape."
    ])
    npc.description.append(f"***Dragonmark Quirk.*** {quirk}")
```
