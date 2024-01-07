# Arcane Tradition: Onomancy
Practitioners of magic well know the power of names, but wizards who follow the tradition of Onomancy use their magic to manipulate the words that encompass existence. Onomancers expand their study into language itself, searching for threads of magical significance that weave through names. Something that is named stands out in the multiverse, distinct from the tapestry of creation all around it. 

That distinction creates power that onomancers seek to tap. By speaking a target's true name, the wizard's spells slip between the cracks of the target's defenses, conforming to its essential nature through the power of its name. To protect themselves, wizards who follow this tradition often hide their true names, typically by adopting monikers and pseudonyms.

> ### Game Notes
> Onomancy, or naming magic, is a method of spellcasting that uses a creature's true name to enhance a spell's effects. A true name is the name by which a self-aware creature identifies itself. This name might be the name a person was given at birth, or one a person chose or earned later in life. Whatever a name's origin, the simplest way for you to know your true name is to think truthfully about yourself and then think, "My name is ..." Your true name is how you finish that sentence.
> You can try to hide your true name by using a pseudonym, but you must be wary not to inhabit that false name too deeply. If a false name comes to be the best expression of who you are, it becomes your true name. Changing one's true name is never a quick choice; it's something that happens over time as a name becomes the creature's truth.
> As a quick guide, a creature has a true name if it understands at least one language or it has an alignment.

Onomancers believe that their power derives from the studies of runes themselves, the thought being that runes are the names of some of the core foundations of the power of the world, and thus they are closest to the recovery of rune magic.

Onomancers generally do not cluster within schools, preferring instead to conduct their research and investigation alone.

```
name = 'Onomancy'
description = "***Arcane Tradition: Onomancy.*** Practitioners of magic well know the power of names, but wizards who follow the tradition of Onomancy use their magic to manipulate the words that encompass existence. Onomancers expand their study into language itself, searching for threads of magical significance that weave through names. Something that is named stands out in the multiverse, distinct from the tapestry of creation all around it."
```

## Bonus Proficiencies
*2nd-level Onomancy feature*

You learn one language of your choice and gain proficiency with calligrapher's tools.

```
def level2(npc):
    npc.languages.append("CHOOSE")
    npc.proficiencies.append("Calligrapher's tools")
```

## Extract Name
*2nd-level Onomancy feature*

You can magically compel a creature to divulge its true name. As a bonus action, you target one creature you can see within 60 feet of you. The target must make a Wisdom saving throw against your spell save DC. On a successful save, you discern that this magic failed, and you can't use this feature on the target again until the next dawn. On a failed save, the target is charmed by you until the end of your next turn, and you mentally learn the charmed target's name or the fact that the target lacks a name.

You can use this feature a number of times equal to your Intelligence modifier (minimum of once), and you regain all expended uses of it when you finish a long rest.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Extract Name ({npc.INTbonus()}/Recharges on long rest).*** A target within 60 feet of you that you can see must make a Wisdom saving throw (DC {npc.spellcasting['Wizard'].spellsavedc()}). On a successful save, you discern that this magic failed, and you can't use this feature on the target again until the next dawn. On a failed save, the target is charmed by you until the end of your next turn, and you mentally learn the charmed target's name or the fact that the target lacks a name.") )
```

## Fateful Naming
*2nd-level Onomancy feature*

You can bend magic to assist or hinder creatures through the power of their true names, and even use those names as an anchor to affect others around them. The [bane](../../Magic/Spells/bane.md) and [bless](../../Magic/Spells/bless.md) spells are wizard spells for you, and you add them to your spellbook. You always have them prepared, yet they don't count against the number of spells you can prepare.

You can cast either spell without expending a spell slot if you speak the true name of one target of the spell as part of casting it. You can cast the spells in this way a number of times equal to your Intelligence modifier (a minimum of once), and you regain all expended uses when you finish a long rest.

```
    npc.spellcasting['Wizard'].spellbook.append('bane')
    npc.spellcasting['Wizard'].spellbook.append('bless')
    npc.defer(lambda npc: npc.actions.append(f"***Fateful Naming ({npc.INTbonus()}/Recharges on long rest).*** You can cast {spelllinkify('bane')} or {spelllinkify('bless')} without expending a spell slot if you speak the true name of one target of the spell as part of casting it.") )
```

## Resonant Utterance
*6th-level Onomancy feature*

You learn words of power called Resonants, which allow you to tailor your spells through the use of a target's true name.

***Resonants Known.*** When you gain this feature, you learn two Resonants of your choice, which are detailed in the "Resonant Options" section. Each time you gain a level in this class, you can replace one resonant you know with a different one.

***Using a Resonant.*** You can use one Resonant when you cast a wizard spell with a spell slot and speak the true name of one creature targeted by the spell. Speaking the name is part of casting the spell.

You can use Resonants a number of times equal to half of your wizard level (round down), and you regain all expended uses when you finish a long rest.

**Resonant Options.** Here are your options when choosing a Resonant:

* **Absorption**. When you cast a spell that deals damage to the named target, you gain 3d6 temporary hit points. The number of temporary hit points you gain increases by 1d6 when you reach 10th level (4d6) and 14th level (5d6) in this class.

* **Devastation**. If the spell requires the named creature to make a saving throw, that creature has disadvantage on the first save it makes against the spell.

* **Dissolution**. The first time the named creature takes damage from the spell, that creature takes an extra 2d8 force damage. The extra force damage increases by 1d8 when you reach 10th level (3d8) and 14th level (4d8) in this class.

* **Nullification**. If the named target is affected by any other spells, you know what those spells are, and you can attempt to end one of your choice by succeeding on an Intelligence check with a DC equal to 10 + the level of the chosen spell.

* **Puppetry**. The first time the named creature takes damage from the spell, you can knock the creature prone or move it up to 10 feet, either directly toward you or away from you.

* **Sympathy**. If the named creature is within range of the spell, you can target the creature with the spell even if you can't see the creature or it has total cover against the spell.

```
resonantoptions = [
    'Absorption',
    'Devastation',
    'Dissolution',
    'Nullification',
    'Puppetry',
    'Sympathy'
]
def chooseresonant(npc):
    choices = resonantoptions
    for res in resonantoptions:
        if res in npc.spellcasting['Wizard'].resonants:
            choices.remove(res)
    npc.spellcasting['Wizard'].resonants.append(choose("Choose a resonant: ", choices))

def applyresonants(npc):
    print("applyresonants")
    for res in npc.spellcasting['Wizard'].resonants:
        if res == 'Absorption': 
            npc.actions.append(f"***Resonant: Absorption.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. In doing so, you gain {'3d6' if npc.levels('Wizard') < 10 else '4d6' if npc.levels('Wizard') < 14 else '5d6'} temporary hit points.")
        elif res == 'Devastation':
            npc.actions.append(f"***Resonant: Devastation.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. If the spell requires the named creature to make a saving throw, that creature has disadvantage on the first save it makes against the spell.")
        elif res == 'Dissolution':
            npc.actions.append(f"***Resonant: Dissolution.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. The first time the named creature takes damage from the spell, that creature takes an extra {'2d8' if npc.levels('Wizard') < 10 else '3d8' if npc.levels('Wizard') < 14 else '4d8'} force damage.")
        elif res == 'Nullification':
            npc.actions.append(f"***Resonant: Nullification.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. If the named target is affected by any other spells, you know what those spells are, and you can attempt to end one of your choice by succeeding on an Intelligence check with a DC equal to 10 + the level of the chosen spell.")
        elif res == 'Puppetry':
            npc.actions.append(f"***Resonant: Puppetry.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. The first time the named creature takes damage from the spell, you can knock the creature prone or move it up to 10 feet, either directly toward you or away from you.")
        elif res == 'Sympathy':
            npc.actions.append(f"***Resonant: Sympathy.*** You cast a wizard spell with a spell slot that deals damage to the named target and speak the true name of one creature targeted by the spell. If the named creature is within range of the spell, you can target the creature with the spell even if you can't see the creature or it has total cover against the spell.")
        else:
            error("WTF? Resonant: " + str(res))

def level6(npc):
    spellcasting = npc.spellcasting['Wizard']
    spellcasting.resonants = []
    npc.traits.append(f"***Resonant Utterance ({npc.levels('Wizard') // 2}/Recharges on long rest).*** See below for options.")
    chooseresonant(npc)
    chooseresonant(npc)

    npc.defer(applyresonants)
```

## Durable Magic
*10th-level Onomancy feature*

The magic you channel helps ward off harm. While you maintain concentration on a spell, you have a +2 bonus to AC and all saving throws.

```
def level10(npc):
    npc.traits.append("***Durable Magic.*** While you maintain concentration on a spell, you have a +2 bonus to AC and all saving throws.")
```

## Inexorable Pronouncement
*10th-level Onomancy feature*

You learn two new Resonants of your choice from your Resonant Utterance feature.

```
    chooseresonant(npc)
    chooseresonant(npc)
```

## Relentless Naming
*14th-level Onomancy feature*

You have learned how to bypass a named creature's defenses against certain types of damage. When you cast a spell that deals damage to a creature whose true name you speak as part of casting the spell, you can cause the spell to deal force or psychic damage (your choice) to the creature, instead of the spell's normal damage type.

```
def level14(npc):
    npc.actions.append("***Relentless Naming.*** You cast a spell that deals damage to a creature whose true name you speak as part of casting the spell, causing the spell to deal force or psychic damage (your choice) to the creature, instead of the spell's normal damage type.")
```
