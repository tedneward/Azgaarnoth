# Arcane Tradition: Corruption
Some wizards, driven by a particularly strong thirst for power, open portals to the most unholy, perverse, gruesome, and chaotic plane of existence: the Abyss. This chaotic power allows those who folow the Corruption Magic tradition to learn how to bend the darkest energies to their will. This magic is the most experimental and dangerous of all, and these mages are fearless pioneers of this new branch. Though, with great power comes great... side efects.

Every time a corrupt magician summons and experiments over the forces of chaos, the stain of the Abyss spreads around like a plague. Those who dwell with the Abyss on a daily basis are afected by this corruption, and there's no way to stop it -- only to slow it down. Such taint is the price of experimenting with the most powerful radiation in existence, and for overcoming the limits of the Material Plane.

Because of the corrupting energies of the Abyss -- and their poor reputation among the other schools - corrupted magicians usualy travel alone or with other corrupted magicians, sometimes as part of an underground [mage school](../../Organizations/MageSchools/RedOrb.md).

```
name = 'Corruption'
description = "***Arcane Tradition: Corruption.*** Some wizards, driven by a particularly strong thirst for power, open portals to the most unholy, perverse, gruesome, and chaotic plane of existence: the Abyss. This chaotic power allows those who folow the Corruption Magic tradition to learn how to bend the darkest energies to their will. This magic is the most experimental and dangerous of all, and these mages are fearless pioneers of this new branch. Though, with great power comes great... side efects."
```

## Abyssal Focus
*2nd-level Corruption Magic feature*

Your Corruption Magic features require the use of a special, personalized focus. This is a focus that only you can use, and must be created through your own magical efforts. 

At the end of a long rest, you can channel and crystallize Abyssal energy to create an Abyssal focus that serves as a spellcasting focus for your wizard spells. The focus is destroyed if you create another one, or if you die. When the focus is destroyed, it causes Signs of Corruption in a 25-foot cube for 1 hour. It also deals radiant damage equal to your wizard level to anything within that cube.

***Abyssal Shard.*** While holding your Abyssal Focus, you can pluck a shard from it (no action required). As an action, you can throw it up to 30 feet, implanting it into the ground. At the end of your turn, the shard evaporates and causes Signs of Corruption on it for 1 minute.

Once you use this feature, you can't use it again until you finish a long rest or you make a Constitution saving throw with a DC equal to 7 + the number of times you've used this feature with your current Abyssal Focus. You receive a bonus to this save equal to twice of your exhaustion level. On a failed save, Signs of Corruption immediately occurs centered on you instead and you become [corrupted](../../Conditions/Corrupted.md) for 1 minute. If you fail the save by 5 or more, you also suffer one level of exhaustion.

***Corrupted Spellcasting.*** When you cast a spell, you can incorporate Abyssal energy into the spell, changing its nature temporarily in following ways:

* If the spell deals damage, all of the spell's damage type becomes radiant damage.
* The spell uses a Constitution saving throw with your spell save DC, instead of an attack roll or the spell's original saving throw.
* If this spell has area of effect, that effect now spreads around corners, even if the original spell's effect did not.
* A [corrupted](../../Conditions/Corrupted.md) creature has disadvantage against this spell.

As part of the spellcasting, you may also remove and expend an Abyssal Shard. When you use an Abyssal Shard with a spell:

* You can ignore material components up to 100 gp in value.
* A [corrupted](../../Conditions/Corrupted.md) creature that fails its saving throw against this spell becomes blinded.

```
def level2(npc):
    npc.traits.append("***Abyssal Focus.*** At the end of a long rest, you can channel and crystallize Abyssal energy to create an Abyssal focus that serves as a spellcasting focus for your wizard spells. The focus is destroyed if you create another one, or if you die. When the focus is destroyed, it causes Signs of Corruption in a 25-foot cube for 1 hour. It also deals radiant damage equal to your wizard level to anything within that cube.")
    npc.actions.append("***Abyssal Shard (Recharges on long rest or CON save/DC 7 + uses).*** While holding your Abyssal Focus, you can pluck a shard from it and throw it up to 30 feet, implanting it into the ground. At the end of your turn, the shard evaporates and causes Signs of Corruption on it for 1 minute. Once you use this feature, you can't use it again until you finish a long rest or you make a Constitution saving throw with a DC equal to 7 + the number of times you've used this feature with your current Abyssal Focus. You receive a bonus to this save equal to twice of your exhaustion level. On a failed save, Signs of Corruption immediately occurs centered on you instead and you become [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) for 1 minute. If you fail the save by 5 or more, you also suffer one level of exhaustion.")
    npc.traits.append("***Corrupted Spellcasting.*** When you cast a spell, you can incorporate Abyssal energy into the spell, changing its nature temporarily in following ways: If the spell deals damage, all of the spell's damage type becomes radiant damage; The spell uses a Constitution saving throw with your spell save DC, instead of an attack roll or the spell's original saving throw; If this spell has area of effect, that effect now spreads around corners, even if the original spell's effect did not; A [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) creature has disadvantage against this spell. As part of the spellcasting, you may also remove and expend an Abyssal Shard. When you use an Abyssal Shard with a spell, you can ignore material components up to 100 gp in value; a [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) creature that fails its saving throw against this spell becomes blinded.")
```

## Signs of Corruption
*2nd-level Corruption feature*

When you draw upon your Abyssal connection, corruption is released around you, creating an area where vegetation withers and dies. The area is plagued by a myriad of bizarre phenomena.

***Signs of Corruption.*** The area of 15-foot cube is lightly obscured, and any healing done within it is halved. When a creature enters the zone for the first time on a turn or starts its turn there, it must succeed on a Constitution saving throw against your wizard spell save DC or become [corrupted](../../Conditions/Corrupted.md) for 1 minute.

Upon reaching 10th level in this class, the size of the cube increases to 25 feet.

```
    npc.defer(lambda npc: npc.traits.append(f"***Signs of Corruption.*** When you draw upon your Abyssal connection, corruption is released around you. The area of a {'15' if npc.levels('Wizard') < 10 else '25'}-foot cube, centered on you, is lightly obscured, and any healing done within it is halved. Any vegetation within the cube withers and dies. When a creature enters the zone for the first time on a turn or starts its turn there, it must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.INTbonus()}) or become [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) for 1 minute.") )
```

## Fleshwarping
*6th-level Corruption Magic feature*

As an action, you can touch a creature and use an Abyssal Shard to alter that creature's form, granting a benefit from the following options:

* **Strength.** The target gains advantage on Strength saving throws, and when it hits with a melee weapon attack against a creature, that creature must succeed on a Constitution saving throw against your spell save DC or be pushed up to 10 feet away and knocked prone.
* **Resilience.** The target gains temporary hit points equal to your proficiency bonus at the start of each of its turns. It also has advantage on Constitution saving throws.
* **Flight.** The target gains a fly speed equal to half of its walking speed and the ability to hover in place.
* **Swimming.** The target gains a swimming speed equal to its walking speed and the ability to breathe underwater.
* **Climbing.** The target gains a climb speed equal to its walking speed and can cling to walls and ceilings without making an ability check.

The effect lasts for 10 minutes. The affected creature has disadvantage to all Charisma-based ability checks for the duration.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append("***Fleshwarping.*** You touch a creature and use an Abyssal Shard to alter that creature's form, granting a benefit for 10 minutes (during which the affected creature has disadvantage on all Charisma-based ability checks); the benefit can be one of the following options: **Strength.** The target gains advantage on Strength saving throws, and when it hits with a melee weapon attack against a creature, that creature must succeed on a Constitution saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}) or be pushed up to 10 feet away and knocked prone. **Resilience.** The target gains {npc.proficiencybonus()} temporary hit points at the start of each of its turns. It also has advantage on Constitution saving throws. **Flight.** The target gains a fly speed equal to half of its walking speed and the ability to hover in place. **Swimming.** The target gains a swimming speed equal to its walking speed and the ability to breathe underwater.**Climbing.** The target gains a climb speed equal to its walking speed and can cling to walls and ceilings without making an ability check.") )
```

## Corrupted Empowerment
*10th-level Corruption Magic feature*

When you are affected by the [corrupted](../../Conditions/Corrupted.md) condition, you embrace the darkness and draw strength from it. Upon becoming corrupted, you regain one expended spell slot. The level of the spell slot must be 3rd level or lower. For each level of exhaustion you have, the level of the spell slot you regain increases by one.

You can only use this feature once per long rest, unless you choose to suffer one level of exhaustion. Only by completing a long rest can you remove a level of exhaustion gained in this way.

```
def level10(npc):
    npc.traits.append("***Corrupted Empowerment (Recharges on long rest or one level of exhaustion).*** When you are affected by the [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) condition, you embrace the darkness and draw strength from it. Upon becoming corrupted, you regain one expended spell slot. The level of the spell slot must be 3rd level or lower. For each level of exhaustion you have, the level of the spell slot you regain increases by one.")
```

## Abyssal Dominion
*14th-level Corruption Magic feature*

As you delve further into the depths of the Abyss, your mastery over its corrupting energies grows stronger. When a creature becomes [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted), it also becomes vulnerable to one damage type of your choice, as long as it does not have resistance or immunity to that damage.

Furthermore, when you use an Abyssal Shard with a spell, you can ignore material components up to a 500 gp value.

```
def level14(npc):
    npc.traits.append("***Abyssal Dominion.*** When a creature becomes [corrupted](http://azgaarnoth.tedneward.com/conditions/Corrupted) due to an effect of a spell you cast or action you take, it also becomes vulnerable to one damage type of your choice, as long as it does not have resistance or immunity to that damage. Additionally, when you use an Abyssal Shard with a spell, you can ignore material components up to a 500 gp value.")
```

---

## Role-playing corruption
Integrating the corruption theme into your gameplay can elevate the overall experience at the table. When describing the effects of your corrupted spells or the process of handling your Abyssal Focus, let the following examples inspire you to create a more immersive atmosphere for all players.

### Abyssal Focus
*During my long rest, I perform a dark ritual to create my Abyssal Focus. I draw an intricate circle of runes on the ground, surrounding it with candles. As I chant in an ancient language, the components merge together, swirling in a vortex of dark power. The runes flare with an unnatural light, binding the malevolent energies into my chosen object. With a final incantation, the ritual is complete, and my new Abyssal Focus lies before me, pulsating with dark power, ready to be wielded.*

You can describe your Abyssal Focus in following ways:

* ***Crystal.*** The Abyssal Focus takes the form of a jagged, obsidian crystal, dark and ominous, with veins of crimson light pulsating within its depths. As you hold it, you feel the malevolent energy coursing through it, eager to be unleashed.
* ***Wand.*** As an Abyssal Focus, the wand is made of twisted, blackened wood, adorned with twisted runes that glow with an unsettling red hue. It seems to vibrate with a sinister hum, as if whispering eldritch secrets to those who dare to wield it.
* ***Rod.*** In the form of a rod, the Abyssal Focus is a dark, metallic scepter with a foreboding, twisted design. Red gems are embedded along its length, glowing with an ominous light that dances and flickers in the shadows.
* ***Orb.*** The Abyssal Focus manifests as a deep red orb, its smooth surface marred by swirling patterns of darkness. It pulses with a menacing aura, like a malevolent heartbeat, emanating an unsettling warmth as it throbs in your hand.
* ***Amulet.*** As an amulet, the Abyssal Focus is a wickedly sharp, black pendant, etched with crimson runes that pulse with dark energy. Suspended from a chain of dark metal, it hangs ominously around your neck, a constant reminder of the power it contains.

You can use these examples to describe throwing the Abyssal Shard:

* *I concentrate, drawing a twisted, pulsing shard of Abyssal energy, which forms and vibrates menacingly in my hand. As I hurl it through the air, it lands with a sickening thud, corrupting the very essence of its surroundings, tainting the air and causing plants and trees to wither and decay.*
* *With determination, I pull a jagged, quivering shard from the insidious darkness, feeling its malevolent power thrumming in my grip. I launch it with precision, and upon impact, it releases a creeping corruption that seeps into the ground, warping the landscape and filling the air with an unsettling aura.*
* *Focusing intently, I extract a sinister, throbbing shard of corruption from the swirling Abyssal energy. I throw it with deadly intent, and as it strikes the ground, the shard dissipates, unleashing a torrent of malignant influence that corrupts the very fabric of reality, blighting the environment and instilling unease in all who draw near.*

These examples can be used to describe corrupting your spells with Abyssal energies:

* *I channel the chaotic energy of the Abyss into my spell, feeling it twist and warp the arcane forces within. As the spell is unleashed, its energy intrudes around corners, and the once chilling power now burns with a radiant fury, striking at the bodies of those caught in its path.*
* *With a whispered invocation, I infuse my spell with the insidious darkness of the Abyss, altering its very essence. The spell's energy now radiates with an eerie, corrupting light, searing its targets with the force of the Abyss and circumventing obstacles with unnatural ease.*
* *As I weave the spell, I taint it with the sinister influence of the Abyss, the magic contorting and shifting under the weight of this corruption. The spell's once familiar effects are transformed, now burning with a terrifying radiance and navigating the terrain in ways that defycomprehension.*

### Fleshwarping
When using your Fleshwarping feature, you can describe its effects like this:

* ***Strength.*** *I extract a shard from my focus and touch it to your body. As the Abyssal energy transfers, your muscles bulge and grow, pulsating with raw power. The shard crumbles, leaving you altered and formidable.*
* ***Resilence.*** *I pull a shard from my focus and press it against your form. As it evaporates, you swell with newfound resilience, your body now able to shrug off blows that once caused injury.*
* ***Flight.*** *With a shard in hand, I work my arcane magic upon your flesh, warping it to sprout grotesque, leathery wings. The shard dissolves, leaving you hovering above the battlefield.*
* ***Swimming.*** *I extract a shard and touch it to your body, reshaping your form to suit an aquatic environment. Your limbs become webbed, and gills emerge, allowing you to swim and breathe underwater as the shard vanishes.*
* ***Climbing.*** *Using a shard, I channel dark magic to contort your flesh, imbuing you with adhesive pads that grant the ability to climb walls and ceilings. The shard crumbles, leaving you defying gravity as you cling to surfaces.*

### Abyssal Dominion
*As I delve into the unfathomable depths of the Abyss, I channel its corrupting energies to bolster my spellcasting. Grasping a shard, I deftly weave a spell that leaves my enemies writhing in pain, their very essence tainted by the dark power that courses through them.*
