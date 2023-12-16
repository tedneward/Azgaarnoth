# Monastic Tradition: Way of the Sacred Inks
Initiates of the Sacred Inks spend years practicing celestial calligraphy. Once they are ready, the monks mark their body with increasingly complex celestial tattoos, granting them access to divine power. As their spiritual connection to the divine grows, so does the beauty of their celestial tattoos.

This monastic tradition is very popular among the Hordes, particularly in [Yithi](../../Nations/Yithi.md), [Zhi](../../Nations/Zhi.md), and [Tragekia](../../Nations/Tragekia.md). The Ulmhorde has some, but not as many, and the tradition has traveled out to the rest of Azgaarnoth.

```
name = 'Way of the Sacred Inks'
description = "***Monastic Tradition: Way of the Sacred Inks.*** Initiates of the Sacred Inks spend years practicing celestial calligraphy. Once they are ready, the monks mark their body with increasingly complex celestial tattoos, granting them access to divine power. As their spiritual connection to the divine grows, so does the beauty of their celestial tattoos."
```

## Celestial Artist
*3rd-level Way of the Sacred Inks feature*

You have been taught the ancient techniques of celestial tattoo artist. You learn to speak, read, and write in Celestial, though most monks will refuse to speak Celestial out loud.

You also gain proficiency with Calligrapher's supplies, and whenever you make a check with calligrapher's supplies, you add twice your proficiency bonus.

```
def level3(npc):
    npc.languages.append('Celestial')
    npc.proficiencies.append("Calligrapher's supplies")
```

## Divine Conduit
*3rd-level Way of the Sacred Inks feature*

Your celestial tattoos allow you to channel the radiant power of the upper planes. You gain the following features:

* Whenever you spend a Hit Die to regain your hit points during a short rest you can spend 1 ki point to regain the maximum amount of hit points, instead of rolling.
* When you hit a target with an Unarmed Strike you can spend ki points (up to your Wisdom modifier) to deal additional radiant damage to the target equal to one roll of your martial arts die per ki point spent.
* As an action you can touch a creture and spend 2 ki points to restore a number of its hit points equal to one roll of your martial arts die + your Wisdom modifier.

```
    npc.defer(lambda npc: npc.traits.append(f"***Divine Conduit.*** Whenever you spend a Hit Die to regain your hit points during a short rest you can spend 1 ki point to regain the maximum amount of hit points, instead of rolling. Additionally, when you hit a target with an Unarmed Strike, you can spend up to {npc.WISbonus()} ki points to deal additional 1d{npc.martialartsdie} per ki point spent radiant damage") )

    npc.defer(lambda npc: npc.actions.append(f"***Divine Conduit.*** You touch a creature and spend 2 ki points to restore one roll of your martial arts die + {npc.WISbonus()} hit points.") )
```

## Heavenly Protection
*6th-level Way of the Sacred Inks feature*

Your connection to the divine and the complexity of your celestial tattoos has increased, granting you a blessing that protects you from death. When you are reduced to 0 hit points, you can choose to fall to 1 hit point instead.

Once you use this feature you must finish a long rest before you can use it again.

```
def level6(npc):
    npc.traits.append("***Heavenly Protection (Recharges on long rest).*** When you are reduced to 0 hit points, you can choose to fall to 1 hit point instead.")
```

## Light of the Heavens
*11th-level Way of the Sacred Inks feature*

As a bonus action, you can unveil the divine light of your celestial tattoos and cause them to emit bright sunlight in a 10-foot radius for 1 minute. While your tattoos are revealed, you add your Wisdom modifier (minimum of +1) to any hit points that you restore and any radiant damage that you deal with a Divine Conduit feature.

This feature instantly ends early if you are incapacitated or if you use your bonus action to end it. Once you use this feature you must finish a short or long rest before you can unveil your celestial tattoos in this way again.

```
def level11(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Light of the Heavens.*** You unveil the divine light of your celestial tattoos and cause them to emit bright sunlight in a 10-foot radius for 1 minute. While your tattoos are revealed, you add {npc.WISbonus()} to any hit points that you restore and any radiant damage that you deal with a Divine Conduit feature. This feature instantly ends early if you are incapacitated or if you use your bonus action to end it.") )
```

## Master of the Sacred Inks
*17th-level Way of the Sacred Inks feature*

You are a sanctified master of the sacred inks. As an action, you can draw out the power of your tattoos to take on an angelic form for 1 minute, granting you the benefits below:

* You gain all the benefits of your Light of the Heavens feature.
* Your tattoos manifest angelic wings. You gain a flying speed equal to your walking speed and can hover.
* When you hit a creature with an Unarmed Strike you can choose to deal radiant damage instead of bludgeoning.

Once you use this feature you must complete a long rest before you can use it again. If you have no uses remaining you can spend 5 ki points to use this feature again.

```
def level17(npc):
    npc.actions.append("***Master of the Sacred Inks (Recharges on long rest or 5 ki points).*** You draw out the power of your tattoos to take on an angelic form for 1 minute. You manifest angelic wings that grant you a flying speed equal to your walking speed and let you hover. When you hit a creature with an Unarmed Strike you can choose to deal radiant damage instead of bludgeoning. The divine light of your celestial tattoos emit bright sunlight in a 10-foot radius, and you add {npc.WISbonus()} to any hit points that you restore and any radiant damage that you deal with a Divine Conduit feature.")
```
