# Mark of Sentinel
The Mark of Sentinel warns and protects. It heightens senses and reflexes, allowing an heir to respond to threats with uncanny speed. It can shield its bearer from harm. Whether on the battlefield or the ballroom, someone who carries the Mark of Sentinel is always prepared for danger.

### Traits
The Mark of Sentinel only manifests on humans. If your character has the Mark of Sentinel, these traits replace the human's Ability Score Increase trait given in the Player's Handbook.

**Ability Score Increase**. Your Strength and Wisdom scores both increase by 1. In addition, one ability score of your choice increases by 1.

**Sentinel's Intuition**. When you roll for Initiative or make a Wisdom (Perception) check to notice a threat, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

**Sentinel's Shield**. You know the [blade ward](../../Magic/Spells/blade-ward.md) cantrip. You can cast the shield spell once with this trait and you regain ability to do so after you finish a short or long rest.

**Vigilant Guardian**. As an action, you can designate an ally you can see as your ward. You have advantage on Wisdom (Insight) and Wisdom (Perception) checks made to spot threats to your ward. In addition, when you are within 5 feet of your ward, and that creature is the target of an attack that you can see, you can use your reaction to swap places with your ward. When you do, you become the target of the attack.

```
name = 'Sentinel Dragonmarked'
description = "***Dragonmark: Mark of Sentinel.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. The Mark of Sentinel warns and protects. It heightens senses and reflexes, allowing an heir to respond to threats with uncanny speed. It can shield its bearer from harm. Whether on the battlefield or the ballroom, someone who carries the Mark of Sentinel is always prepared for danger."

def level0(npc):
    npc.STR += 1
    npc.WIS += 1
    abilities = [ 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']
    ability = choose("Choose an ability to improve: ", abilities)
    if ability == 'STR': npc.STR += 1
    elif ability == 'DEX': npc.DEX += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    elif ability == 'CHA': npc.CHA += 1

    npc.traits.append("***Sentinel's Intuition.*** When you roll for Initiative or make a Wisdom (Perception) check to notice a threat, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    spellcasting = innatecaster(npc, 'INT', "Sentinel Dragonmark")
    spellcasting.cantripsknown.append("blade ward")
    npc.actions.append(f"***Sentinel's Shield (Recharges on short or long rest).*** You can cast the {spelllinkify('shield')} spell.")

    npc.actions.append("***Vigilant Guardian. You can designate an ally you can see as your ward. You have advantage on Wisdom (Insight) and Wisdom (Perception) checks made to spot threats to your ward. In addition, when you are within 5 feet of your ward, and that creature is the target of an attack that you can see, you can use your reaction to swap places with your ward. When you do, you become the target of the attack.")

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
