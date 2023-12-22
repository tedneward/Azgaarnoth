# Mark of Making
The Mark of Making guides its bearer through any act of creation. The bearer of the mark can mend broken things with a touch, and always has a minor magic item they've been working on. An artificer or a wizard will get the most out of the mark, but anyone can find a use for an enchanted blade.

### Traits
The Mark of Making only manifests on humans. If your character has the Mark of Making, these traits replace the human's Ability Score Increase trait given in the Player's Handbook.

**Ability Score Increase**. Your Intelligence and Dexterity scores increase by 1. Increase either Intelligence or Dexterity by an additional 1 point.

**Artisan's Intuition**. When you make an ability check with artisan's tools, roll 1d4 and add it to the result.

**Maker's Gift**. You know the cantrip [mending](../../Magic/Spells/mending.md). You gain proficiency with one type of artisan's tools.

**Magecraft**. You can create a temporary magic item out of common materials. Choose a cantrip from the spell list below. Describe the item connected to it. As long as you possess the item, you know that cantrip. At the end of a long rest, you can replace this with a new item and select a new cantrip from the list. Intelligence is your spellcasting ability for these cantrips.

**Magecraft Cantrip Spell List**

* [balance](../../Magic/Spells/balance.md)
* [blade ward](../../Magic/Spells/blade-ward.md)
* [blood boil](../../Magic/Spells/blood-boil.md)
* [bolster](../../Magic/Spells/bolster.md)
* [booming blade](../../Magic/Spells/booming-blade.md)
* [control flames](../../Magic/Spells/control-flames.md)
* [create bonfire](../../Magic/Spells/create-bonfire.md)
* [dancing lights](../../Magic/Spells/dancing-lights.md)
* [dazzle](../../Magic/Spells/dazzle.md)
* [disarm](../../Magic/Spells/disarm.md)
* [friends](../../Magic/Spells/friends.md)
* [frostbite](../../Magic/Spells/frostbite.md)
* [gust](../../Magic/Spells/gust.md)
* [light](../../Magic/Spells/light.md)
* [mage hand](../../Magic/Spells/mage-hand.md)
* [mending](../../Magic/Spells/mending.md)
* [message](../../Magic/Spells/message.md)
* [mold earth](../../Magic/Spells/mold-earth.md)
* [prestidigitation](../../Magic/Spells/prestidigitation.md)
* [sapping sting](../../Magic/Spells/sapping-sting.md)
* [shape water](../../Magic/Spells/shape-water.md)
* [shocking grasp](../../Magic/Spells/shocking-grasp.md)
* [thunderclap](../../Magic/Spells/thunderclap.md)

**Spellsmith**. You can spend one minute to weave a temporary enchantment into a nonmagical suit of armor or weapon. For the next hour the object becomes a magic item, gaining a +1 bonus to AC if it's armor or a +1 bonus to hit and damage if it's a weapon. Once you use this trait, you can't use it again until you finish a long rest.

```
name = 'Making Dragonmarked'
description = "***Dragonmark: Mark of Making.*** A dragonmark is a distinctive symbol that appears on the skin. Dragonmarks are painted in vivid shades of blue and purple and seem to shimmer or even move slightly. When used, they grow warm to the touch. A dragonmark can’t be removed--even if a limb bearing a dragonmark is cut away, the mark eventually manifests on another part of the bearer’s body. The Mark of Making guides its bearer through any act of creation. The bearer of the mark can mend broken things with a touch, and always has a minor magic item they've been working on. An artificer or a wizard will get the most out of the mark, but anyone can find a use for an enchanted blade."

def level0(npc):
    npc.INT += 1
    npc.DEX += 1

    npc.traits.append("***Artisan's Intuition.*** When you make an ability check with artisan's tools, roll 1d4 and add it to the result.")

    npc.cantripsknown.append("mending")

    npc.traits.append("***Magecraft.*** You can create a temporary magic item out of common materials. Choose a cantrip from the Magecraft Cantrip Spell List. Describe the item connected to it. As long as you possess the item, you know that cantrip. At the end of a long rest, you can replace this with a new item and select a new cantrip from the list. Intelligence is your spellcasting ability for these cantrips.")

    npc.traits.append("***Spellsmith.*** You can spend one minute to weave a temporary enchantment into a nonmagical suit of armor or weapon. For the next hour the object becomes a magic item, gaining a +1 bonus to AC if it's armor or a +1 bonus to hit and damage if it's a weapon. Once you use this trait, you can't use it again until you finish a long rest.")

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
