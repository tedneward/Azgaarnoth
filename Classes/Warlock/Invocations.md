# Eldritch Invocations

### Agonizing Blast
*Prerequisite: eldritch blast cantrip*

When you cast [eldritch blast](../../Magic/Spells/eldritch-blast.md), add your Charisma modifier to the damage it deals on a hit.

### Armor of Shadows
You can cast [mage armor](../../Magic/Spells/mage-armor.md) on yourself at will, without expending a spell slot or material components.

```
def armorofshadows(npc):
    npc.actions.append(f"***Armor of Shadows.*** You can cast {spelllinkify('mage armor')} at will, without expending a spell slot or material components.")

def armorofshadows_prereq(npc): return True
```

### Ascendant Step
*Prerequisite: 9th level*

You can cast [levitate](../../Magic/Spells/levitate.md) on yourself at will, without expending a spell slot or material components.

```
def ascendantstep(npc):
    npc.actions.append(f"***Ascendant Step.*** You can cast {spelllinkify('levitate')} on yourself at will, without expending a spell slot or material components.")

def ascendantstep_prereq(npc): return npc.levels('Warlock') >= 9
```

### Aspect of the Moon
*Prerequisite: Pact of the Tome feature*

You no longer need to sleep and can't be forced to sleep by any means. To gain the benefits of a long rest, you can spend all 8 hours doing light activity, such as reading your Book of Shadows and keeping watch.

### Beast Speech
You can cast [speak with animals](../../Magic/Spells/speak-with-animals.md) at will, without expending a spell slot.

```
def beastspeech(npc):
    npc.actions.append(f"***Beast Speech.*** You can cast {spelllinkify('speak with animals')} at will, without expending a spell slot.")

def beastspeech_prereq(npc): return True
```

### Beguiling Influence
You gain proficiency in the Deception and Persuasion skills.

```
def beguilinginfluence(npc):
    npc.proficiencies.append('Deception')
    npc.proficiencies.append('Persuasion')

def beguilinginfluence_prereq(npc): return True
```

### Bewitching Whispers
*Prerequisite: 7th level*

You can cast [compulsion](../../Magic/Spells/compulsion.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def bewitchingwhispers(npc):
    npc.actions.append(f"***Bewitching Whispers (Recharges on long rest).*** You can cast {spelllinkify('compulsion')} using a warlock a spell slot.")

def bewitchingwhispers_prereq(npc): return npc.levels('Warlock') >= 7
```

### Bond of the Talisman
*Prerequisite: 12th level, Pact of the Talisman feature*

While someone else is wearing your talisman, you can use your action to teleport to the unoccupied space closest to them, provided the two of you are on the same plane of existence. The wearer of your talisman can do the same thing, using their action to teleport to you.

### Book of Ancient Secrets
*Prerequisite: Pact of the Tome feature*

You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class's spell list (the two needn't be from the same list). The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag.

On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it.

### Chain Master's Fury
*Prerequisite: 9th level, Pact of the Chain feature*

As a bonus action, you can command your familiar to make one attack.

### Chains of Carceri
*Prerequisite: 15th level, Pact of the Chain feature*

You can cast [hold monster](../../Magic/Spells/hold-monster.md) at will -- targeting a celestial, fiend, or elemental -- without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.

```
def chainsofcarceri(npc):
    npc.actions.append(f"***Chains of Carceri (Recharges on long rest).*** You can cast {spelllinkify('hold monster')} at will, targeting a celestial, fiend, or elemental, without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.")

def chainsofcarceri_prereq(npc): return npc.levels('Warlock') >= 15
```

### Cloak of Flies
*Prerequisite: 5th level*

As a bonus action, you can surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action.

The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).

Once you use this invocation, you can't use it again until you finish a short or long rest.

### Devil's Sight
You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.

```
def devilssight(npc):
    npc.traits.append(f"***Devil's Sight.*** You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.")
    npc.sight['devilsight'] = 120

def devilssight_prereq(npc): return npc.levels('Warlock') >= 15
```

### Dreadful Word
*Prerequisite: 7th level*

You can cast [confusion](../../Magic/Spells/confusion.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Eldritch Armor
*Prerequisite: Pact of the Blade feature*

As an action, you can touch a suit of armor that isn't being worn or carried by anyone and instantly don it, provided you aren't wearing armor already. You are proficient with this suit of armor until it's removed.

### Eldritch Mind
*Prerequisite: Pact of the Tome feature*

You have advantage on Constitution saving throws that you make to maintain your concentration on a spell.

### Eldritch Sight
You can cast [detect magic](../../Magic/Spells/detect-magic.md) at will, without expending a spell slot.

### Eldritch Smite
*Prerequisite: 5th level, Pact of the Blade feature*

Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller.

### Eldritch Spear
*Prerequisite: eldritch blast cantrip*

When you cast eldritch blast, its range is 300 feet.

### Eyes of the Rune Keeper
You can read all writing.

### Far Scribe
*Prerequisite: 5th level, Pact of the Tome feature*

A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of 1).

You can cast the [sending](../../Magic/Spells/sending.md) spell, targeting a creature whose name is on the page, without using a spell slot and without using material components. To do so, you must write the message on the page. The target hears the message in their mind, and if the target replies, their message appears on the page, rather than in your mind. The writing disappears after 1 minute.

As an action, you can magically erase a name on the page by touching the name on it.

### Fiendish Vigor
You can cast [false life](../../Magic/Spells/false-life.md) on yourself at will as a 1st-level spell, without expending a spell slot or material components.

```
def fiendishvigor(npc):
    npc.actions.append(f"***Fiendish Vigor.*** You can cast {spelllinkify('false life')} on yourself as a 1st-level spell at will, without expending a spell slot or material components.")

def fiendishvigor_prereq(npc): return True
```

### Gaze of Two Minds
You can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings.

### Ghostly Gaze
*Prerequisite: 7th level*

As an action, you gain the ability to see through solid objects to a range of 30 feet. Within that range, you have darkvision if you don't already have it. This special sight lasts for 1 minute or until your concentration ends (as if you were concentrating on a spell). During that time, you perceive objects as ghostly, transparent images.

Once you use this invocation, you can't use it again until you finish a short or long rest.

### Gift of the Depths
*Prerequisite: 5th level*

You can breathe underwater, and you gain a swimming speed equal to your walking speed.

You can also cast [water breathing](../../Magic/Spells/water-breathing.md) once without expending a spell slot. You regain the ability to do so when you finish a long rest.

### Gift of the Ever-Living Ones
*Prerequisite: Pact of the Chain feature*

Whenever you regain hit points while your familiar is within 100 feet of you, treat any dice rolled to determine the hit points you regain as having rolled their maximum value for you.

### Gift of the Protectors
*Prerequisite: 9th level, Pact of the Tome feature*

A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of 1).

When any creature whose name is on the page is reduced to 0 hit points but not killed outright, the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit from it until you finish a long rest.

As an action, you can magically erase a name on the page by touching the name on it.

### Grasp of Hadar
*Prerequisite: eldritch blast cantrip*

Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.

### Improved Pact Weapon
*Prerequisite: Pact of the Blade feature*

You can use any weapon you summon with your Pact of the Blade feature as a spellcasting focus for your warlock spells.

In addition, the weapon gains a +1 bonus to its attack and damage rolls, unless it is a magic weapon that already has a bonus to those rolls.

Finally, the weapon you conjure can be a shortbow, longbow, light crossbow, or heavy crossbow.

### Investment of the Chain Master
*Prerequisite: Pact of the Chain feature*

When you cast [find familiar](../../Magic/Spells/find-familiar.md), you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits:

* The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet.
* The familiar no longer needs to breathe.
* The familiar's weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.
* If the familiar forces a creature to make a saving throw, it uses your spell save DC.

### Lance of Lethargy
*Prerequisite: eldritch blast cantrip*

Once on each of your turns when you hit a creature with your eldritch blast, you can reduce that creature's speed by 10 feet until the end of your next turn.

### Lifedrinker
*Prerequisite: 12th level, Pact of the Blade feature*

When you hit a creature with your pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum 1).

### Maddening Hex
*Prerequisite: 5th level, hex spell or a warlock feature that curses*

As a bonus action, you cause a psychic disturbance around the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. When you do so, you deal psychic damage to the cursed target and each creature of your choice that you can see within 5 feet of it. The psychic damage equals your Charisma modifier (minimum of 1 damage). To use this invocation, you must be able to see the cursed target, and it must be within 30 feet of you.

### Mask of Many Faces
You can cast [disguise self](../../Magic/Spells/disguise-self.md) at will, without expending a spell slot.

### Master of Myriad Forms
*Prerequisite: 15th level*

You can cast [alter self](../../Magic/Spells/alter-self) at will, without expending a spell slot.md.



### Minions of Chaos
*Prerequisite: 9th level*

You can cast [conjure elemental](../../Magic/Spells/conjure-elemental.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Mire the Mind
*Prerequisite: 5th level*

You can cast [slow](../../Magic/Spells/slow.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Misty Visions
You can cast [silent image](../../Magic/Spells/silent-image.md) at will, without expending a spell slot or material components.

```
def mistyvision(npc):
    npc.traits.append("You can cast [silent image](../../Magic/Spells/silent-image.md) at will, without expending a spell slot or material components.")
def mistyvision_prereq(npc): return True
```

### One with Shadows
*Prerequisite: 5th level*

When you are in an area of dim light or darkness, you can use your action to become invisible until you move or take an action or a reaction.

### Otherworldly Leap
*Prerequisite: 9th level*

You can cast jump on yourself at will, without expending a spell slot or material components.

### Protection of the Talisman
*Prerequisite: 9th level, Pact of the Talisman feature*

When the wearer of your talisman makes a saving throw in which they lack proficiency, they can add a d4 to the roll.

### Rebuke of the Talisman
*Prerequisite: Pact of the Talisman feature*

When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you can use your reaction to deal psychic damage to the attacker equal to your Charisma modifier (minimum of 1 damage) and push it up to 10 feet away from the talisman's wearer.

### Relentless Hex
*Prerequisite: 7th level, hex spell or a warlock feature that curses*

Your curse creates a temporary bond between you and your target. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see within 5 feet of the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. To teleport in this way, you must be able to see the cursed target.

### Repelling Blast
*Prerequisite: eldritch blast cantrip*

When you hit a creature with eldritch blast, you can push the creature up to 10 feet away from you in a straight line.

### Sculptor of Flesh
*Prerequisite: 7th level*

You can cast [polymorph](../../Magic/Spells/polymorph.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Shroud of Shadow
*Prerequisite: 15th level*

You can cast [invisibility](../../Magic/Spells/invisibility.md) at will, without expending a spell slot.

```
def shroudofshadow(npc):
    npc.actions.append(f"***Shroud of Shadow.*** You can cast {spelllinkify('invisibility')} at will, without expending a spell slot.")

def shroudofshadow_prereq(npc):
    return npc.levels('Warlock') >= 15
```

### Sign of Ill Omen
*Prerequisite: 5th level*

You can cast [bestow curse](../../Magic/Spells/bestow-curse.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Thief of Five Fates
You can cast [bane](../../Magic/Spells/bane.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

### Thirsting Blade
*Prerequisite: 5th level, Pact of the Blade feature*

You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn.

### Tomb of Levistus
*Prerequisite: 5th level*

As a reaction when you take damage, you can entomb yourself in ice, which melts away at the end of your next turn. You gain 10 temporary hit points per warlock level, which take as much of the triggering damage as possible. Immediately after you take the damage, you gain vulnerability to fire damage, your speed is reduced to 0, and you are incapacitated. These effects, including any remaining temporary hit points, all end when the ice melts.

Once you use this invocation, you can't use it again until you finish a short or long rest.

```
def tomboflevistus(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Tomb of Levistus (Recharges on short or long rest).*** You entomb yourself in ice, which melts away at the end of your next turn. You gain {10 * npc.levels('Warlock')} temporary hit points, which take as much of the triggering damage as possible. Immediately after you take the damage, you gain vulnerability to fire damage, your speed is reduced to 0, and you are incapacitated. These effects, including any remaining temporary hit points, all end when the ice melts.") )

def tomboflevistus_prereq(npc):
    return npc.levels('Warlock') >= 5
```

### Trickster's Escape
*Prerequisite: 7th level*

You can cast [freedom of movement](../../Magic/Spells/freedom-of-movement.md) once on yourself without expending a spell slot. You regain the ability to do so when you finish a long rest.

```
def trickstersescape(npc):
    npc.actions.append(f"***Trickster's Escape (Recharges on long rest).*** You can cast {spelllinkify('freedom')} on yourself, without expending a spell slot.")

def trickstersescape_prereq(npc):
    return npc.levels('Warlock') >= 15
```

### Visions of Distant Realms
*Prerequisite: 15th level*

You can cast [arcane eye](../../Magic/Spells/arcane-eye.md) at will, without expending a spell slot.

```
def visionsofdistantrealms(npc):
    npc.actions.append(f"***Visions of Distant Realms.*** You can cast {spelllinkify('arcane eye')} at will, without expending a spell slot.")

def visionsofdistantrealms_prereq(npc):
    return npc.levels('Warlock') >= 15
```

### Voice of the Chain Master
*Prerequisite: Pact of the Chain feature*

You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech.

### Whispers of the Grave
*Prerequisite: 9th level*

You can cast [speak with dead](../../Magic/Spells/speak-with-dead.md) at will, without expending a spell slot.

```
def whispersofthegrave(npc):
    npc.actions.append(f"***Whispers of the Grave.*** You can cast {spelllinkify('speak with dead')} at will, without expending a spell slot.")

def whispersofthegrave_prereq(npc):
    return npc.levels('Warlock') >= 9
```

### Witch Sight
*Prerequisite: 15th level*

You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet of you and within line of sight.

```
def witchsight(npc):
    npc.senses['witchsight'] = 30
    npc.traits.append("***Witch Sight.*** You can see the true form of any shapechanger or creature concealed by illusion or transmutation magic while the creature is within 30 feet of you and within line of sight.")

def witchsight_prereq(npc):
    return npc.levels('Warlock') >= 15
```

```
invocations = {
    'Misty Vision': mistyvision,
    'Witch Sight': witchsight
}
def chooseinvocation(npc):
    choices = {}
    for (name, fn) in invocations.items():
        prereqfn = globals()[globals()[fn].__name__ + '_prereq']()
        if prereqfn(npc):
            if name in npc.invocations:
                pass
            else:
                choices[name] = details[1]

    (invocationname, invocationfn) = choose("Choose an Eldritch Invocation: ", invocations)
    npc.invocations.append(invocationname)
    invocationfn(npc)

allclasses['Warlock'].chooseinvocation = chooseinvocation
```
