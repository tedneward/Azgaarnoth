# Arcane Tradition: Psionics
Wizards study magical power in all its forms, including the magic of psionics. Those wizards who follow the tradition of Psionics hone the magical potential of their own minds. Sometimes called psionicists or psychics, these wizards interact with the multiverse through the lens of their psionic aptitude and awareness. Psionicists channel their magic by focusing their minds. By doing so they can transcend their physical bodies, adopting forms of pure thought, casting spells psionically to bypass the need for components, and perceiving the world with a broader range of senses. As a member of the Psionics tradition, you might have awoken your psionic potential through the strain of your esoteric studies, or perhaps you joined a scholarly order dedicated to unlocking the magic of the mind.

In the latter case, you likely joined the [MindMage](../../Organizations/MageSchools/MindMage.md) school, one of the very few that focuses on the use of psionics. It's also possible that you had the channels to your mind's power opened by a wandering ex-member of that school, but this happens quite rarely--most psionic wizards prefer to study within the walls of their *sanctum sanctorum* in [Mighal](../../Cities/Mighal.md).

```
name = "Psionics"
description = "***Arcane Tradition: Psionics.*** Wizards study magical power in all its forms, including the magic of psionics. Those wizards who follow the tradition of Psionics hone the magical potential of their own minds. Sometimes called psionicists or psychics, these wizards interact with the multiverse through the lens of their psionic aptitude and awareness. Psionicists channel their magic by focusing their minds. By doing so they can transcend their physical bodies, adopting forms of pure thought, casting spells psionically to bypass the need for components, and perceiving the world with a broader range of senses. As a member of the Psionics tradition, you might have awoken your psionic potential through the strain of your esoteric studies, or perhaps you joined a scholarly order dedicated to unlocking the magic of the mind."
```

## Psionic Focus
*2nd-level Psionic feature*

You have learned to channel psionic energy through a special object: a psionic focus. You gain the object with this feature (see the "Your Psionic Focus" sidebar for how you might have acquired the item).

While your psionic focus is on your person, you gain the following benefits:

* The object is a spellcasting focus for you.
* When you roll psychic or force damage for any of your wizard spells, you can reroll any of those damage dice that rolls a 1, but you must use the new roll.

If your psionic focus is lost, you can magically recreate it by meditating for 1 hour during a short or long rest, at the end of which the focus appears in your hand.

```
def level2(npc):
    npc.traits.append("***Psionic Focus.*** You have learned to channel psionic energy through a psionic focus. While your psionic focus is on your person, you gain the following benefits: The object is a spellcasting focus for you; When you roll psychic or force damage for any of your wizard spells, you can reroll any of those damage dice that rolls a 1, but you must use the new roll.")

    npc.equipment.append("***Psionic focus.*** If your psionic focus is lost, you can magically recreate it by meditating for 1 hour during a short or long rest, at the end of which the focus appears in your hand.")
```

> ### Your Psionic Focus
> Every member of the Psionics tradition has a story about how their psionic focus came into their life. Consider how you found yours and what form it takes.
> The event that brought your psionic focus to you probably holds personal significance. Did your master give it to you upon the completion of your apprenticeship? Was it awarded to you when you graduated from your academy of wizardry? Did it call to you in a jeweler's shop? Was it associated with the moment when your psionic powers first manifested? One morning, did you wake up with it humming under your pillow?
> The form your psionic focus takes is also yours to define, likely being a reflection of how your magic came into being, a symbol of your own psyche, or an item you use to focus your thoughts. It is a handheld object that has special meaning to you, but that can't be a weapon or magic item. Perhaps it's a childhood memento, the skull of an alien creature, a crystal that makes you feel a certain way, a coin that only lands on its edge, a fire- scarred planchette, or any other enigmatic personal relic.
> However the object arrived and whatever form it takes, your psionic focus is now yours, and you decide how to handle it. Will you mount it on a wand or staff? Would you prefer to wear it on a necklace or circlet? Have you embedded it into the cover of your spellbook? Wherever you put it, you can now channel your magic through it, and it is a sign of your membership in the revered tradition of psionic wizardry.

## Psionic Devotion
*2nd-level Psionics feature*

Your study of psionics begins to unleash your mind's potential. When you gain this feature, choose one of the following cantrips: *friends*, *mage hand*, or *message*. You learn that cantrip if you don't already know it, and it doesn't count against the number of wizard cantrips you know.

While your psionic focus is on your person, you can cast the chosen cantrip as a bonus action, requiring no components, and with the modification listed below:

* **[friends](../../Magic/Spells/friends.md)**. When the spell ends, the target doesn't become hostile to you.
* **[mage hand](../../Magic/Spells/mage-hand.md)**. You can make the hand invisible when you cast the spell, and controlling the spell is a bonus action for you.
* **[message](../../Magic/Spells/message.md)**. You don't need to point toward the target or whisper your message out loud.

```
    cantrip = choose("Choose a cantrip: ", ['friends', 'mage hand', 'message'])
    npc.spellcasting['Wizard'].cantripsknown.append(cantrip)
```

## Thought Form
*6th-level Psionics feature*

While you are carrying your psionic focus, you can use a bonus action to magically transform your body into pure psionic energy. The transformation lasts for 10 minutes, until you use a bonus action to assume your normal form, or until you are incapacitated or die.

While in Thought Form, you are a figure of luminous psychic energy, with your psionic focus hovering within. Your form can appear as anything you wish, but it is obviously magical, is the same size as you, and sheds dim light in a 5- foot-radius. Any other equipment you are wearing or carrying transforms with you and melds into your thought form. You also gain the following benefits:

* **Psionic Spellcasting**. When you cast a spell while in thought form, you can cast the spell psionically. If you do so, the spell doesn't require verbal, somatic, or material components that lack a gold cost.
* **Psychic Resilience**. You gain resistance to psychic damage and to bludgeoning, piercing, and slashing damage from nonmagical attacks.

You can transform using this feature a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Thought Form ({npc.INTbonus()}/Recharges on long rest).*** You magically transform your body into pure psionic energy. The transformation lasts for 10 minutes, until you use a bonus action to assume your normal form, or until you are incapacitated or die. While in thought form, you are a figure of luminous psychic energy, with your psionic focus hovering within. Your form can appear as anything you wish, but it is obviously magical, is the same size as you, and sheds dim light in a 5-foot-radius. {'You have a flying speed equal to your walking speed and can hover, and you can move through other creatures and objects as if they were difficult terrain. You take 1d10 force damage if you end your turn inside an object. If you return to your normal form while inside an object, you are shunted to the nearest unoccupied space, and you take 1d10 force damage for every 5 feet traveled.' if npc.levels('Wizard') >= 14 else ''}Any other equipment you are wearing or carrying transforms with you and melds into your thought form. You also gain the following benefits: **Psionic Spellcasting**. When you cast a spell while in thought form, you can cast the spell psionically. If you do so, the spell doesn't require verbal, somatic, or material components that lack a gold cost. **Psychic Resilience**. You gain resistance to psychic damage and to bludgeoning, piercing, and slashing damage from nonmagical attacks.") )
```

## Mental Discipline
*10th-level Psionics feature*

Your mind's power expands to greater heights. When you gain this feature, choose one of the following spells: [dominate person](../../Magic/Spells/dominate-person.md), [scrying](../../Magic/Spells/scrying.md), or [telekinesis](../../Magic/Spells/telekinesis.md). You can add the spell to your spellbook, and you can cast it without components.

You can also cast the chosen spell once without expending a spell slot. After you do so, you regain the ability to cast the spell without a slot when you finish a long rest.

```
def level10(npc):
    chosenspell = choose("Choose a spell: ", ['dominate person', 'scrying', 'telekinesis'])
    npc.actions.append(f"***Mental Discipline (Recharges on long rest).*** You can cast {spelllinkify(chosenspell)} once without expending a spell slot.")
```

## Empowered Psionics
*10th-level Psionics feature*

When you deal psychic or force damage with a wizard spell, you can add your Intelligence modifier to the damage against one of the spell's targets.

```
    npc.defer(lambda npc: npc.traits.append(f"***Empowered Psionics.*** When you deal psychic or force damage with a wizard spell, you add {npc.INTbonus()} to the damage against one of the spell's targets.") )
```

## Thought Travel
*14th-level Psionics feature*

While using your Thought Form, you have a flying speed equal to your walking speed and can hover, and you can move through other creatures and objects as if they were difficult terrain.

You take 1d10 force damage if you end your turn inside an object. If you return to your normal form while inside an object, you are shunted to the nearest unoccupied space, and you take 1d10 force damage for every 5 feet traveled.

---

# Psionic Spells
Spell selection is part of what defines a wizard and their individual fields of expertise. When creating your Psionics wizard, consider spells that are thematically appropriate for that tradition. Psionics as a theme generally includes spells that do the following:

* contact or manipulate minds
* allow the caster to perceive distant locations or planes
* alter perception
* move objects and creatures
* teleport
* deal psychic or force damage

Here is a list of wizard spells that fit with these themes. Spells marked with an asterisk are spells presented in this document.

#### Cantrips (0 Level)
* friends
* [mage hand](https://www.dndbeyond.com/spells/mage-hand)
* message 
* mind sliver 
* minor illusion 
* true strike

#### 1st Level
* alarm (ritual)
* [catapult](../../Magic/Spells/catapult.md)
* [cause fear](../../Magic/Spells/cause-fear.md)
* charm person
* comprehend languages (ritual) 
* disguise self
* id insinuation
* identify (ritual)
* magic missile
* silent image
* sleep
* Tasha's hideous laughter 
* unseen servant (ritual)

#### 2nd Level
* blindness/deafness
* blur
* crown of madness
* detect thoughts
* hold person
* invisibility
* levitate
* locate object
* mental barrier
* [mind spike](../../Magic/Spells/mind-spike.md)
* mind thrust
* mirror image
* [misty step](../../Magic/Spells/misty-step.md)
* phantasmal force
* see invisibility
* suggestion
* thought shield

#### 3rd Level
* blink
* [catnap](../../Magic/Spells/catnap.md)
* clairvoyance
* [enemies abound](../../Magic/Spells/enemies-abound.md)
* fear
* fly
* hypnotic pattern
* major image
* nondetection
* [psionic blast](../../Magic/Spells/psionic-blast.md)
* sending
* tongues

#### 4th Level
* arcane eye
* [charm monster](../../Magic/Spells/charm-monster.md) 
* confusion
* dimension door
* ego whip
* greater invisibility
* hallucinatory terrain 
* locate creature
* Otiluke's resilient sphere
* phantasmal killer

#### 5th Level
* Bigby's hand
* contact other plane (ritual)
* dominate person
* dream
* [far step](../../Magic/Spells/far-step.md)
* geas
* hold monster
* intellect fortress
* legend lore
* mislead
* modify memory
* Rary's telepathic bond (ritual)
* scrying
* seeming
* [skill empowerment](../../Magic/Spells/skill-empowerment.md)
* [synaptic static](../../Magic/Spells/synaptic-static.md)
* telekinesis
* teleportation circle
* wall of force

#### 6th Level
* arcane gate
* Drawmij's instant summons (ritual) 
* eyebite
* magic jar
* mass suggestion
* [mental prison](../../Magic/Spells/mental-prison.md)
* Otto's irresistible dance 
* programmed illusion
* psychic crush
* [scatter](../../Magic/Spells/scatter.md)
* true seeing

#### 7th Level
* etherealness
* forcecage
* mirage arcane
* plane shift
* [power word pain](../../Magic/Spells/power-word-pain.md)
* project image
* reverse gravity 
* sequester 
* teleport

#### 8th Level
* antipathy/sympathy
* dominate monster
* feeblemind
* [illusory dragon](../../Magic/Spells/illusory-dragon.md)
* [maddening darkness](../../Magic/Spells/maddening-darkness.md)
* mind blank
* power word stun 
* telepathy

#### 9th Level
* astral projection
* foresight
* imprisonment
* [psychic scream](../../Magic/Spells/psychic-scream.md)
