# Dragonmark: Mark of Storm
It is believed that the dragonmark dates back to the very earliest days of the [Eldar](../../History/Eldar.md), and that the Eldar handed out the dragonmark to favored [Firstborn](../index.md#firstborn) or [humans](../Humans.md) as rewards for excellent service. No [Created](../index.md#created) have ever borne a dragonmark, and for many milennia, it was believed that no [Hordes](../index.md#hordes)ish race could bear one, but time has proven that to be a false assumption--at least, for those of mixed parentage.

Dragonmarked are generally "born wild" and, once known, often tracked down by either the [Draconic Order](../../Organizations/MilitantOrders/DraconicOrder/index.md) or hunted by the [Cult of the Wyrm](../../Organizations/CultOfTheWyrm.md), to either recruit or destroy. Dragonmarked are not part of a particular [noble House](../../Organizations/Houses/index.md), but bloodlines do carry through genetic lines (or so it seems), and many of the noble Houses carry the dragonmark within their bloodlines... as do most of the other races by this point in Azgaarnoth's history, although perhaps not as strongly as the nobility.

As a dragonmarked character grows in level, you can take the [Greater Dragonmark feat](../../Feats/GreaterDragonmark.md) to reflect the growing power of your dragonmark. This represents the evolution of a dragonmark--an exponential increase in both the size of the dragonmark and the powers it bestows. Only a fraction of dragonmarked ever develop a Greater Dragonmark. This brings attention to the bearer of the Mark--both wanted and unwanted.

## Intuition Dice
A dragonmark improves your ability to perform a specific type of task. Each dragonmark has a trait that allows you to roll an Intuition die, a d4, when you perform an ability check with a particular skill or tool. You add the number rolled to the ability check. You don’t have to be proficient with the skill or tool to gain this benefit.

Feats, magic items, and other features may improve your Intuition die. This increases the type of die you roll by one size (d6, d8, d10) to a maximum of a d10. You can only roll one Intuition die for a check; if you receive Intuition dice from multiple sources, increase one die by one type and roll that one.

For example, if a dragonmarked trait and feat both grant intuition with Dexterity (Stealth) checks, you roll a d6, instead of a d4. Three instances would increase your Intuition Die to a d8, and so on.

## Dragonmark Appearance
A dragonmark is a distinctive symbol that appears on the skin. There are twelve known dragonmarks, each unique in design and power. A dragonmark can appear on any part of the body. One half-elf could have the Mark of Detection across an eye, while another has it in the palm of their hand. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch and may glow (though this doesn’t produce useful illumination). A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. All dragonmarks share the same initial appearance but a dragonmark can grow in size and complexity if a character takes the Greater Dragonmark feat or if the mark is tied to class abilities.

While dragonmarks share the same general appearance, your dragonmark could have a unique quality. If you’d like to explore this, roll on the Dragonmark Quirks table.

### Dragonmark Quirks
1d6 | Quirk
--- | -----
1 | Your dragonmark is unusually small or remarkably large.
2 | Your dragonmark slowly moves around your body.
3 | Your dragonmark glows dramatically when you use it.
4 | Your dragonmark tingles when you’re near someone with the same mark.
5 | Your dragonmark tickles when you use it.
6 | Your dragonmark is an unusual color but a normal shape.

Wind and water welcome the half-elf who carries the Mark of Storms. The wind catches them when they fall, and they swim with remarkable speed. Those who possess the Greater Dragonmark and dragonshard focus items can call on even greater powers, shaping the weather and calling on the power of the storm.

### Traits
The Mark of Storm manifests exclusively on half-elves. If your character has the Mark of Detection, these traits replace the half-elf’s Ability Score Increase, Skill Versatility, and Languages given in the Player’s Handbook.

**Ability Score Increase**. Your Dexterity and Charisma scores both increase by 1. In addition, one ability score of your choice increases by 1.

**Sea Monkey**. Your base walking speed is 30 feet, and you have a swim speed of 30 feet.

**Windwright’s Intuition**. When you make a Dexterity (Acrobatics) check or any ability check involving operating or maintaining a water or air vehicle, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

**Storm’s Blessing**. You have resistance to lightning damage.

**Headwinds**. You know the [gust](../../Magic/Spells/gust.md) cantrip. When you reach 3rd level, you can cast the [gust of wind](../../Magic/Spells/gust-of-wind.md) spell once with this trait and regain the ability to do so when you finish a long rest.

```
name = 'Storm Dragonmarked'
description = "***Dragonmark: Mark of Storm.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. Wind and water welcome the half-elf who carries the Mark of Storms. The wind catches them when they fall, and they swim with remarkable speed. Those who possess the Greater Dragonmark and dragonshard focus items can call on even greater powers, shaping the weather and calling on the power of the storm."
def level0(npc):
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

    npc.DEX += 1
    npc.CHA += 1
    ability = choose("Choose an ability to improve: ", abilities)
    if ability == 'STR': npc.STR += 1
    elif ability == 'DEX': npc.DEX += 1
    elif ability == 'CON': npc.CON += 1
    elif ability == 'INT': npc.INT += 1
    elif ability == 'WIS': npc.WIS += 1
    elif ability == 'CHA': npc.CHA += 1

    npc.traits.append("***Windwright’s Intuition.*** When you make a Dexterity (Acrobatics) check or any ability check involving operating or maintaining a water or air vehicle, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")

    npc.damageresistances.append('lightning')

    spellcasting = innatecaster(npc, 'INT', "Storm Dragonmark")
    spellcasting.cantripsknown.append("gust")

def level3(npc):
    npc.spellcasting['Storm Dragonmark'].perday[1] = []
    npc.spellcasting['Storm Dragonmark'].perday[1].append('gust of wind')
```
