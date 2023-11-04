# Eldritch Invocations

### Agonizing Blast
*Prerequisite: eldritch blast cantrip*

When you cast [eldritch blast](../../Magic/Spells/eldritch-blast.md), add your Charisma modifier to the damage it deals on a hit.

```
def agonizingblast(npc):
    npc.defer(lambda npc: npc.actions.append("***Agonizing Blast.*** When you cast *eldritch blast*, add {npc.CHAbonus()} to the damage it deals on a hit.") )

def agonizingblast_prereq(npc): return True
```

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

```
def aspectofthemoon(npc):
    npc.traits.append("***Aspect of the Moon.*** You no longer need to sleep and can't be forced to sleep by any means. To gain the benefits of a long rest, you can spend all 8 hours doing light activity, such as reading your Book of Shadows and keeping watch.")

    npc.conditionimmunities.append("sleep")

def aspectofthemoon_prereq(npc):
    return npc.pactboon == 'Pact of the Tome'
```

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

```
def bondofthetalisman(npc):
    npc.actions.append("***Bond of the Talisman.*** While someone else is wearing your talisman, you  teleport to the unoccupied space closest to them, provided the two of you are on the same plane of existence. The wearer of your talisman can do the same thing, using their action to teleport to you.")

def bondofthetalisman_prereq(npc): return npc.levels('Warlock') >= 12 and npc.pactboon == 'Pact of the Talisman'
```

### Book of Ancient Secrets
*Prerequisite: Pact of the Tome feature*

You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the ritual tag from any class's spell list (the two needn't be from the same list). The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag.

On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it.

```
def bookofancientsecrets(npc):
    npc.traits.append("***Book of Ancient Secrets.*** You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the *ritual* tag from any class's spell list (the two needn't be from the same list). The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the ritual tag. On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it.")

def bookofancientsecrets_prereq(npc):
    return npc.pactboon == 'Pact of the Tome'
```

### Chain Master's Fury
*Prerequisite: 9th level, Pact of the Chain feature*

As a bonus action, you can command your familiar to make one attack.

```
def chainmastersfury(npc):
    npc.bonusactions.append("***Chain Master's Fury.*** You command your familiar to make one attack.")

def chainmastersfury_prereq(npc):
    return npc.pactboon == 'Pact of the Tome' and npc.levels('Warlock') >= 9
```

### Chains of Carceri
*Prerequisite: 15th level, Pact of the Chain feature*

You can cast [hold monster](../../Magic/Spells/hold-monster.md) at will -- targeting a celestial, fiend, or elemental -- without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.

```
def chainsofcarceri(npc):
    npc.actions.append(f"***Chains of Carceri (Recharges on long rest).*** You can cast {spelllinkify('hold monster')} at will, targeting a celestial, fiend, or elemental, without expending a spell slot or material components. You must finish a long rest before you can use this invocation on the same creature again.")

def chainsofcarceri_prereq(npc): return npc.levels('Warlock') >= 15 and npc.pactboon == 'Pact of the Chain'
```

### Cloak of Flies
*Prerequisite: 5th level*

As a bonus action, you can surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action.

The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).

Once you use this invocation, you can't use it again until you finish a short or long rest.

```
def cloakofflies(npc):
    npc.bonusactions.append("***Cloak of Flies (Recharges on short or long rest).*** You surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action. The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).")

def cloakofflies_prereq(npc): return npc.levels('Warlock') >= 5
```

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

```
def dreadfulword(npc):
    npc.actions.append(f"***Dreadful Word (Recharges on long rest).*** You cast {spelllinkify('confusion')} using a warlock spell slot.")

def dreadfulword_prereq(npc): return npc.levels('Warlock') >= 7
```

### Eldritch Armor
*Prerequisite: Pact of the Blade feature*

As an action, you can touch a suit of armor that isn't being worn or carried by anyone and instantly don it, provided you aren't wearing armor already. You are proficient with this suit of armor until it's removed.

```
def eldritcharmor(npc):
    npc.actions.append("***Eldritch Armor.*** You touch a suit of armor that isn't being worn or carried by anyone and instantly don it, provided you aren't wearing armor already. You are proficient with this suit of armor until it's removed.")

def eldritcharmor_prereq(npc): return npc.pactboon == 'Pact of the Blade'
```

### Eldritch Mind
*Prerequisite: Pact of the Tome feature*

You have advantage on Constitution saving throws that you make to maintain your concentration on a spell.

```
def eldritchmind(npc):
    npc.traits.append("***Eldritch Mind.*** You have advantage on Constitution saving throws that you make to maintain your concentration on a spell.")

def eldritchmind_prereq(npc): return npc.pactboon == 'Pact of the Tome'
```

### Eldritch Sight
You can cast [detect magic](../../Magic/Spells/detect-magic.md) at will, without expending a spell slot.

```
def eldritchsight(npc):
    npc.actions.append(f"***Eldritch Sight.*** You cast {spelllinkify('detect magic')} at will, without expending a spell slot.")

def eldritchsight_prereq(npc): return True
```

### Eldritch Smite
*Prerequisite: 5th level, Pact of the Blade feature*

Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller.

```
def eldritchsmite(npc):
    npc.actions.append("***Eldritch Smite.*** Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller.")

def eldritchsmite_prereq(npc): return npc.levels("Warlock") >= 5 and npc.pactboon == "Pact of the Blade"
```

### Eldritch Spear
*Prerequisite: eldritch blast cantrip*

When you cast eldritch blast, its range is 300 feet.

```
def eldritchspear(npc):
    npc.actions.append("***Eldritch Spear.*** When you cast eldritch blast, its range is 300 feet.")

def eldritchspear_prereq(npc): return True
```

### Eyes of the Rune Keeper
You can read all writing.

```
def eyesoftherunekeeper(npc): 
    npc.traits.append("***Eyes of the Rune Keeper.*** You can read all writing")

def eyesoftherunekeeper_prereq(npc): return True 
```

### Far Scribe
*Prerequisite: 5th level, Pact of the Tome feature*

A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of 1).

You can cast the [sending](../../Magic/Spells/sending.md) spell, targeting a creature whose name is on the page, without using a spell slot and without using material components. To do so, you must write the message on the page. The target hears the message in their mind, and if the target replies, their message appears on the page, rather than in your mind. The writing disappears after 1 minute.

As an action, you can magically erase a name on the page by touching the name on it.

```
def farscribe(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Far Scribe.*** A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain {npc.CHAbonus()} names. You can cast the {spelllinkify('sending')} spell, targeting a creature whose name is on the page, without using a spell slot and without using material components. To do so, you must write the message on the page. The target hears the message in their mind, and if the target replies, their message appears on the page, rather than in your mind. The writing disappears after 1 minute. As an action, you can magically erase a name on the page by touching the name on it.") )

def farscribe_prereq(npc):
    return npc.levels("Warlock") >= 5 and npc.pactboon == 'Pact of the Tome'
```

### Fiendish Vigor
You can cast [false life](../../Magic/Spells/false-life.md) on yourself at will as a 1st-level spell, without expending a spell slot or material components.

```
def fiendishvigor(npc):
    npc.actions.append(f"***Fiendish Vigor.*** You can cast {spelllinkify('false life')} on yourself as a 1st-level spell at will, without expending a spell slot or material components.")

def fiendishvigor_prereq(npc): return True
```

### Gaze of Two Minds
You can use your action to touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings.

```
def gazeoftwominds(npc):
    npc.actions.append("***Gaze of Two Minds.*** You touch a willing humanoid and perceive through its senses until the end of your next turn. As long as the creature is on the same plane of existence as you, you can use your action on subsequent turns to maintain this connection, extending the duration until the end of your next turn. While perceiving through the other creature's senses, you benefit from any special senses possessed by that creature, and you are blinded and deafened to your own surroundings.")

def gazeoftwominds_prereq(npc): return True
```

### Ghostly Gaze
*Prerequisite: 7th level*

As an action, you gain the ability to see through solid objects to a range of 30 feet. Within that range, you have darkvision if you don't already have it. This special sight lasts for 1 minute or until your concentration ends (as if you were concentrating on a spell). During that time, you perceive objects as ghostly, transparent images.

Once you use this invocation, you can't use it again until you finish a short or long rest.

```
def ghostlygaze(npc):
    npc.actions.append("***Ghostly Gaze (Recharges on short or long rest).*** you gain the ability to see through solid objects to a range of 30 feet. Within that range, you have darkvision if you don't already have it. This special sight lasts for 1 minute or until your concentration ends (as if you were concentrating on a spell). During that time, you perceive objects as ghostly, transparent images.")

def ghostlygaze_prereq(npc): return npc.levels('Warlock') >= 7
```

### Gift of the Depths
*Prerequisite: 5th level*

You can breathe underwater, and you gain a swimming speed equal to your walking speed.

You can also cast [water breathing](../../Magic/Spells/water-breathing.md) once without expending a spell slot. You regain the ability to do so when you finish a long rest.

```
def giftofthedepths(npc):
    npc.traits.append("***Gift of the Depths.*** You can breathe underwater, and you gain a swimming speed equal to your walking speed.")
    npc.speed['swimming'] = npc.speed['walking']
    npc.actions.append(f"***Gift of the Depths (Recharges on long rest).*** You can cast {spelllinkify('water breathing')} once without expending a spell slot.")

def giftofthedepths_prereq(npc): return npc.levels('Warlock') >= 5
```

### Gift of the Ever-Living Ones
*Prerequisite: Pact of the Chain feature*

Whenever you regain hit points while your familiar is within 100 feet of you, treat any dice rolled to determine the hit points you regain as having rolled their maximum value for you.

```
def giftoftheeverlivingones(npc):
    npc.traits.append("***Gift of the Ever-Living Ones.*** Whenever you regain hit points while your familiar is within 100 feet of you, treat any dice rolled to determine the hit points you regain as having rolled their maximum value for you.")

def giftoftheeverlivingones_prereq(npc): return npc.pactboon == 'Pact of the Chain'
```

### Gift of the Protectors
*Prerequisite: 9th level, Pact of the Tome feature*

A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of 1).

When any creature whose name is on the page is reduced to 0 hit points but not killed outright, the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit from it until you finish a long rest.

As an action, you can magically erase a name on the page by touching the name on it.

```
def giftoftheprotectors(npc):
    npc.traits.append("***Gift of the Protectors.*** A new page appears in your Book of Shadows. With your permission, a creature can use its action to write its name on that page, which can contain a number of names equal to your Charisma modifier (minimum of 1). When any creature whose name is on the page is reduced to 0 hit points but not killed outright, the creature magically drops to 1 hit point instead. Once this magic is triggered, no creature can benefit from it until you finish a long rest. As an action, you can magically erase a name on the page by touching the name on it.")

def giftoftheprotectors_prereq(npc): return npc.levels('Warlock') >= 9 and npc.pactboon == 'Pact of the Tome'
```

### Grasp of Hadar
*Prerequisite: eldritch blast cantrip*

Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.

```
def graspofhadar(npc):
    npc.actions.append("***Grasp of Hadar.*** Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.")

def graspofhadar_prereq(npc): return True
```

### Ironfell Blade
*Prerequisites: 5th level, Pact of the Ring feature*. 

When you take the attack action on your turn and attack with a melee weapon that inflicts slashing or piercing damage, you can attack with that weapon twice, instead of once.

```
def ironfellblade(npc):
    npc.actions.append("***Ironfell Blade.*** When you take the Attack action on your turn and attack with a melee weapon that inflicts slashing or piercing damage, you attack with that weapon twice, instead of once.")

def ironfellblade_prereq(npc): return npc.levels('Warlock') >= 5 and npc.pactboon == 'Pact of the Ring'
```

### Iron Sky Starfall
*Prerequisite: 9th level, [eldritch blast](../../Magic/Spells/eldritch-blast.md) cantrip, Pact of the Ring feature*. 

When you hit a creature with your eldritch blast, you can cast [hold person](../../Magic/Spells/hold-person.md) as a bonus action using a warlock spell slot. The spell's target must be the creature you hit with eldritch blast.

```
def ironskystarfall(npc):
    npc.bonusactions.append(f"***Iron Sky Starfall.*** When you hit a creature with your eldritch blast, you cast {spelllinkify('hold person')} using a warlock spell slot. The spell's target must be the creature you hit with eldritch blast.")

def ironskystarfall_prereq(npc):
    return npc.levels('Warlock') >= 9 and npc.pactboon == 'Pact of the Ring'
```

### Improved Pact Weapon
*Prerequisite: Pact of the Blade feature*

You can use any weapon you summon with your Pact of the Blade feature as a spellcasting focus for your warlock spells.

In addition, the weapon gains a +1 bonus to its attack and damage rolls, unless it is a magic weapon that already has a bonus to those rolls.

Finally, the weapon you conjure can be a shortbow, longbow, light crossbow, or heavy crossbow.

```
def improvedpactweapon(npc):
    npc.traits.append("***Improved Pact Weapon.*** You can use any weapon you summon with your Pact of the Blade feature as a spellcasting focus for your warlock spells. In addition, the weapon gains a +1 bonus to its attack and damage rolls, unless it is a magic weapon that already has a bonus to those rolls. Finally, the weapon you conjure can be a shortbow, longbow, light crossbow, or heavy crossbow.")

def improvedpactweapon_prereq(npc): return npc.pactboon == 'Pact of the Blade'
```

### Investment of the Chain Master
*Prerequisite: Pact of the Chain feature*

When you cast [find familiar](../../Magic/Spells/find-familiar.md), you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits:

* The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet.
* The familiar no longer needs to breathe.
* The familiar's weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks.
* If the familiar forces a creature to make a saving throw, it uses your spell save DC.

```
def investmentofthechainmaster(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Investment of the Chain Master.*** When you cast {spelllinkify('find familiar')}, you infuse the summoned familiar with a measure of your eldritch power, granting the creature the following benefits: The familiar gains either a flying speed or a swimming speed (your choice) of 40 feet; The familiar no longer needs to breathe; The familiar's weapon attacks are considered magical for the purpose of overcoming immunity and resistance to nonmagical attacks; If the familiar forces a creature to make a saving throw, it uses your spell save DC ({npc.pactmagic.spellsavedc()}).") )

def investmentofthechainmaster_prereq(npc): return npc.pactboon == 'Pact of the Chain'
```

### Lance of Lethargy
*Prerequisite: eldritch blast cantrip*

Once on each of your turns when you hit a creature with your eldritch blast, you can reduce that creature's speed by 10 feet until the end of your next turn.

```
def lanceoflethargy(npc):
    npc.actions.append("***Lance of Lethargy.*** Once on each of your turns when you hit a creature with your eldritch blast, you can reduce that creature's speed by 10 feet until the end of your next turn.")

def lanceoflethargy_prereq(npc): return True
```

### Lifedrinker
*Prerequisite: 12th level, Pact of the Blade feature*

When you hit a creature with your pact weapon, the creature takes extra necrotic damage equal to your Charisma modifier (minimum 1).

```
def lifedrinker(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Lifedrinker.*** When you hit a creature with your Pact weapon, the create takes {npc.CHAbonus()} extra necrotic damage") )

def lifedrinker_prereq(npc): return npc.levels('Warlock') >= 12 and npc.pactboon == 'Pact of the Blade'
```

### Maddening Hex
*Prerequisite: 5th level, hex spell or a warlock feature that curses*

As a bonus action, you cause a psychic disturbance around the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. When you do so, you deal psychic damage to the cursed target and each creature of your choice that you can see within 5 feet of it. The psychic damage equals your Charisma modifier (minimum of 1 damage). To use this invocation, you must be able to see the cursed target, and it must be within 30 feet of you.

```
def maddeninghex(npc):
    npc.bonusactions.append(f"***Maddening Hex.*** You cause a psychic disturbance around the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. When you do so, you deal {npc.CHAbonus()} psychic damage to the cursed target and each creature of your choice that you can see within 5 feet of it. To use this invocation, you must be able to see the cursed target, and it must be within 30 feet of you.")

def maddeninghex_prereq(npc): return npc.levels('Warlock') >= 5
```

### Mask of Many Faces
You can cast [disguise self](../../Magic/Spells/disguise-self.md) at will, without expending a spell slot.

```
def maskofmanyfaces(npc):
    npc.traits.append(f"***Mask of Many Faces.*** You can cast {spelllinkify('disguise self')} at will, without expending a spell slot or material components.")

def maskofmanyfaces_prereq(npc): return True
```

### Master of Myriad Forms
*Prerequisite: 15th level*

You can cast [alter self](../../Magic/Spells/alter-self) at will, without expending a spell slot.md.

```
def masterofmyriadforms(npc):
    npc.traits.append(f"***Master of Myriad Forms.*** You can cast {spelllinkify('alter self')} at will, without expending a spell slot or material components.")

def masterofmyriadforms_prereq(npc): return npc.levels('Warlock') >= 15
```

### Minions of Chaos
*Prerequisite: 9th level*

You can cast [conjure elemental](../../Magic/Spells/conjure-elemental.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def minionsofchaos(npc):
    npc.traits.append(f"***Minions of Chaos.*** You can cast {spelllinkify('conjure elemental')} at will, without expending a spell slot or material components.")

def minionsofchaos_prereq(npc): return npc.levels('Warlock') >= 15
```

### Mire the Mind
*Prerequisite: 5th level*

You can cast [slow](../../Magic/Spells/slow.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def mirethemind(npc):
    npc.traits.append("***Mire the Mind (Recharges on long rest).*** You can cast [slow](../../Magic/Spells/slow.md) once using a warlock spell slot.")
def mirethemind_prereq(npc): return npc.levels('Warlock') >= 5
```

### Misty Visions
You can cast [silent image](../../Magic/Spells/silent-image.md) at will, without expending a spell slot or material components.

```
def mistyvision(npc):
    npc.traits.append(f"***Misty Visions.*** You can cast {spelllinkify('silent image')} at will, without expending a spell slot or material components.")

def mistyvision_prereq(npc): return True
```

### One with Shadows
*Prerequisite: 5th level*

When you are in an area of dim light or darkness, you can use your action to become invisible until you move or take an action or a reaction.

```
def onewithshadows(npc):
    npc.actions.append("***One with Shadows.*** When you are in an area of dim light or darkness, you become invisible until you move or take an action or reaction.")

def onewithshadows_prereq(npc): return npc.levels('Warlock') >= 5
```

### Otherworldly Leap
*Prerequisite: 9th level*

You can cast [jump](../../Magic/Spells/jump.md) on yourself at will, without expending a spell slot or material components.

```
def otherworldlyleap(npc):
    npc.traits.append(f"***Otherworldly Leap.*** You can cast {spelllinkify('jump')} on yourself at will, without expending a spell slot or material components.")

def otherworldlyleap_prereq(npc): return npc.levels('Warlock') >= 9
```

### Protection of the Talisman
*Prerequisite: 9th level, Pact of the Talisman feature*

When the wearer of your talisman makes a saving throw in which they lack proficiency, they can add a d4 to the roll.

```
def protectionofthetalisman(npc):
    npc.traits.append("***Protection of the Talisman.*** When the wearer of your talisman makes a saving throw in which they lack proficiency, they can add a d4 to the roll.")

def protectionofthetalisman_prereq(npc): return npc.levels('Warlock') >= 9 and npc.pactboon == 'Pact of the Talisman'
```

### Rebuke of the Talisman
*Prerequisite: Pact of the Talisman feature*

When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you can use your reaction to deal psychic damage to the attacker equal to your Charisma modifier (minimum of 1 damage) and push it up to 10 feet away from the talisman's wearer.

```
def rebukeofthetalisman(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Rebuke of the Talisman.*** When the wearer of your talisman is hit by an attacker you can see within 30 feet of you, you deal {npc.CHAbonus()} psychic damage to the attacker and push it up to 10 feet away from the talisman's wearer.") )
    
def rebukeofthetalisman_prereq(npc): return npc.levels('Warlock') >= 9 and npc.pactboon == 'Pact of the Talisman'
```

### Relentless Hex
*Prerequisite: 7th level, hex spell or a warlock feature that curses*

Your curse creates a temporary bond between you and your target. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see within 5 feet of the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. To teleport in this way, you must be able to see the cursed target.

```
def relentlesshex(npc):
    npc.bonusactions.append("***Relentless Hex.*** You magically teleport up to 30 feet to an unoccupied space you can see within 5 feet of the target cursed by your hex spell or by a warlock feature of yours, such as Hexblade's Curse or Sign of Ill Omen. To teleport in this way, you must be able to see the cursed target.")

def relentlesshex_prereq(npc): return npc.levels('Warlock') >= 7
```

### Repelling Blast
*Prerequisite: eldritch blast cantrip*

When you hit a creature with eldritch blast, you can push the creature up to 10 feet away from you in a straight line.

```
def repellingblast(npc):
    npc.traits.append("***Repelling Blast.*** When you hit a creature with *eldritch blast*, you can push the creature up to 10 feet away from you in a straight line.")

def repellingblast_prereq(npc): return True
```

### Sculptor of Flesh
*Prerequisite: 7th level*

You can cast [polymorph](../../Magic/Spells/polymorph.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def sculptorofflesh(npc):
    npc.actions.append(f"***Sculptor of Flesh (Recharges on long rest).*** You can cast {spelllinkify('polymorph')} once using a warlock spell slot.")

def sculptorofflesh_prereq(npc): return npc.levels('Warlock') >= 7
```

### Shard Star Warrior
*Prerequisites: 15th level*. 

When you make an attack roll for a melee weapon or a cantrip, you score a critical hit on a roll of 19 or 20 if you have not already inflicted a critical hit that turn.

```
def shardstarwarrior(npc):
    npc.actions.append("***Shard Star Warrior.*** When you make an attack roll for a melee weapon or a cantrip, you score a critical hit on a roll of 19 or 20 if you have not already inflicted a critical hit that turn.")

def shardstarwarrior_prereq(npc): return npc.levels('Warlock') >= 15
```

### Shroud of Shadow
*Prerequisite: 15th level*

You can cast [invisibility](../../Magic/Spells/invisibility.md) at will, without expending a spell slot.

```
def shroudofshadow(npc):
    npc.actions.append(f"***Shroud of Shadow.*** You can cast {spelllinkify('invisibility')} at will, without expending a spell slot.")

def shroudofshadow_prereq(npc): return npc.levels('Warlock') >= 15
```

### Sign of Ill Omen
*Prerequisite: 5th level*

You can cast [bestow curse](../../Magic/Spells/bestow-curse.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def signofillomen(npc):
    npc.actions.append(f"***Sign of Ill Omen (Recharges on long rest).*** You can cast {spelllinkify('bestow curse')} once using a warlock spell slot.")

def signofillomen_prereq(npc): return npc.levels('Warlock') >= 5
```

### Starlight Hex
*Prerequisites: 5th level*. 

When you cast the [hex](../../Magic/Spells/hex.md) spell using a warlock spell slot, the initial target you choose as its first subject immediately takes 1d8 magical radiant damage and must succeed on a Constitution saving throw. On a failure, it is blinded until the end of its next turn. 

Also, whenever you inflict necrotic damage with your hex spell, you may choose for it to be radiant damage instead.

```
def starlighthex(npc):
    npc.actions.append("***Starlight Hex.*** When you cast the {spelllinkify('hex')} spell using a warlock spell slot, the initial target you choose as its first subject immediately takes 1d8 magical radiant damage and must succeed on a Constitution saving throw. On a failure, it is blinded until the end of its next turn. Also, whenever you inflict necrotic damage with your hex spell, you may choose for it to be radiant damage instead.")

def starlighthex_prereq(npc): return npc.levels('Warlock') >= 5
```

### Thief of Five Fates
You can cast [bane](../../Magic/Spells/bane.md) once using a warlock spell slot. You can't do so again until you finish a long rest.

```
def thiefoffivefates(npc):
    npc.actions.append(f"***Thief of Five Fates (Recharges on long rest).*** You can cast {spelllinkify('bane')} once using a warlock spell slot.")

def thiefoffivefates_prereq(npc): return True
```

### Thirsting Blade
*Prerequisite: 5th level, Pact of the Blade feature*

You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn.

```
def thirstingblade(npc):
    npc.actions.append("***Thirsting Blade.*** You can attack with your pact weapon twice, instead of once, whenever you take the Attack action on your turn.")

def thirstingblade_prereq(npc): return npc.levels('Warlock') >= 5 and npc.pactboon == 'Pact of the Blade'
```

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

### Voices of the Chain Master
*Prerequisite: Pact of the Chain feature*

You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech.

```
def voicesofthechainmaster(npc):
    npc.traits.append("***Voices of the Chain Master.*** You can communicate telepathically with your familiar and perceive through your familiar's senses as long as you are on the same plane of existence. Additionally, while perceiving through your familiar's senses, you can also speak through your familiar in your own voice, even if your familiar is normally incapable of speech.")

def voicesofthechainmaster_prereq(npc): return npc.pactboon == 'Pact of the Chain'
```

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

DEATHLY CHILLS
When you deal cold damage to a creature using a
warlock spell or feature, you ignore resistance to cold
damage unless the creature also has resistance or immunity
to necrotic damage, and you treat vulnerability to
necrotic damage as vulnerability to both damage types.

ELDRITCH DIGESTION
When you deal acid damage to a creature using a
warlock spell or feature, you ignore resistance to acid
damage unless the creature also has resistance or
immunity to force damage, and you treat vulnerability to
force damage as vulnerability to both damage types.

ELEMENTAL ATTUNEMENT
When you finish a long rest, you choose one of four
elements below to attune to. While attuned to an
element, you know an associated can trip ( each is from
Xanathar's Guide to Everything) as a warlock spelL and
it doesn't count against the number of cantrips you can
know as a warlock. You gain the following benefits
while attuned to each element:
Air. You know the gust cantrip, and you can hold your
breath for twice as long.
Earth. You know the mold earth cantrip, and you have
advantage on ability checks made to climb earth or stone.
Fire. You know the control flames cantrip, and you
have advantage on saving throws made to resist the
effects of extreme heat.
Water. You know the shape water cantrip, and you
have advantage on saving throws made to resist the
effects of extreme cold

HEAVENLY BOLTS
When you deal lightning damage to a creature using a
warlock spell or feature, you ignore resistance to
lightning damage unless the creature also has
resistance or immunity to radiant damage, and you treat
vulnerability to radiant damage as vulnerability to both
damage types.

HUSH OFWINTER
When you deal cold damage to a creature using a
warlock spell or feature, you can force the target to
make a Wisdom saving throw. On a failed save, the
target is deafened and can't speak until the end of your
next turn.
Once you use this invocation, you must finish a long
rest before you can use it again.

NOXIOUS FuMES
When you deal acid damage to a creature using a
warlock spell or feature, you can force the target to
make a Constitution saving throw. On a failed save, the
target is poisoned until the end of its next turn.
Once you use this invocation, you must finish a long
rest before you can use it again.

PRISMATIC BLAZE
When you deal fire damage to a creature that isn't
blinded using a warlock spell or feature, you can force
the target to make a Wisdom saving throw. On a failed
save, the target becomes charmed until the end of its
next turn. While charmed in this way, the target is
incapacitated and has a speed of 0. The effect ends if
the target takes any additional damage or if someone
else uses an action to shake it out of its stupor.
Once you use this invocation, you must finish a long
rest before you can use it again.

SCORCHING RADIANCE
When you deal radiant damage to a creature using a
warlock spell or feature, you ignore resistance to
radiant damage unless the creature also has resistance
or immunity to fire damage, and you treat vulnerability
to fire damage as vulnerability to both damage types.

UMBRA FLAME
When you deal fire damage to a creature using a
warlock spell or feature, you ignore resistance to fire
damage unless the creature also has resistance or immunity
to necrotic damage, and you treat vulnerability to
necrotic damage as vulnerability to both damage types.

VOICE FROM BEYOND
When you deal thunder damage to a creature using a
warlock spell or feature, you ignore resistance to
thunder damage unless the creature also has resistance
or immunity to psychic damage, and you treat
vulnerability to psychic damage as vulnerability to both
damage types.

WELCOMING LIGHT
When you deal radiant damage to a creature using a
warlock spell or feature, you can force the target to
make a Wisdom saving throw. On a failed save, the
target becomes charmed by you until the end of your
next turn. While charmed in this way, the target regards
you as a friendly acquaintance.
Once you use this invocation, you must finish a long
rest before you can use it again.

WHISPER THE DREAD WIND
When you deal thunder damage to a creature using a
warlock spell or feature, you can force the target to
make a Wisdom saving throw. On a failed save, the
target is frightened of you until the end of its next turn.
Once you use this invocation, you must finish a long
rest before you can use it again.

WITHERING LIGHTNING
When you deal lightning damage to a creature using a
warlock spell or feature, you can force the target to
make a Constitution saving throw. On a failed save, the
target's hit point maximum is reduced for 1 minute by
an amount equal to the lightning damage it took. Any
effect that removes a disease allows the target's hit point
maximum to return to normal before that time passes.
Once you use this invocation, you must finish a long
rest before you can use it again.

AMBASSADOR OF THE DEPTHS
Prerequisite: 5th level
You can expend a warlock spell slot to cast the new dive
spell While the spell affects a target, that target also has
darkvision that extends out to a range of 120 feet.

DESERT ROAMER
Prerequisite: 5th level
You are adapted to both hot climates and cold climates,
as described in the Dungeon Master's Guide, and you
don't need to drink water to survive.

FLAME WALKER
Prerequisite: 5th level
You and any equipment you are wearing or carrying are
immune to the damage dealt by nonmagical fire, and you
can breathe ashes, smoke, and the stinking cloud spell
without any negative effects. This can't prevent damage
dealt by traps or creatures, such as the breath weapon of
a red dragon or the blast of a fire cannon.

WEIGHTLESSNESS
Prerequisite: 5th level
You can cast feather fall targeting only yourself at will
without expending a spell slot or requiring components.

EXPLOSIVE VENGEANCE
Prerequisite: 7th leve~ Pact of the Chain, fireball known
as a warlock spell
When another creature deals damage to your familiar
and reduces it to O hit points, you can choose to use
your reaction to cast fireball using a warlock spell slot
centered at the location of your familiar, even if it is
outside your normal range or line of sight for the spell
The spell originates from your familiar. After you do
this, you gain one level of exhaustion and you can't cast
any spells of 1st-level or higher on your next turn.
Once you use this invocation, you must finish a long
rest before you can use it again.

GRAVEBORNE
Prerequisite: 7th level
While you are buried or burrowing in earth or sealed
underground, you don't need to eat, drink, or breathe.

BREATH OF BAHAMUT
Prerequisite: 9th leve~ Dragon Patron (Any Metallic)
You can use an action to expend a warlock spell slot to
exhale a secondary breath weapon in a 30-foot cone.
Each creature in the area suffers the following effects,
determined by your dragon patron's kind These effects
end instantly if you lose your concentration (as if you
were concentrating on a spell} Any saving throws are
made against your warlock spell save DC.
Brass. Targets must succeed on a Constitution saving
throw or fall unconscious for 1 minute. This effect ends
for a creature if the creature takes damage or someone
uses an action to wake it. Any creature with hit points
equal to or greater than your warlock level x 4 automatically
succeeds on the saving throw.
Bronze. Targets must succeed on a Strength saving
throw or else be pushed 60 feet away from you.
Copper. Each target must make a Constitution saving
throw. On a failed save, a creature can't use reactions,
its speed is halved, and it can't make more than one
attack on its turn. Also, the creature can use either an
action or a bonus action on its turn, but not both. These
effects last for 1 minute. A creature repeats the saving
throw at the end of each of its turns, ending the effect
on itself on a success.
Gold Each target must succeed on a Strength saving
throw or suffer disadvantage on Strength-based attacks,
Strength checks, and other Strength saving throws for 1
minute. A creature repeats the saving throw at the end of
each of its turns, ending the effect on itself on a success.
Silver. Targets must succeed on a Constitution saving
throw or be paralyzed until the end of your next turn.
Any creature with hit points equal to or greater than
your warlock level x 3 automatically succeeds on the
saving throw.

TIAMAT' S BARGAIN
Prerequisite: 9th leve~ Dragon Patron (Any Chromatic)
When you use your Breath of the Wynn feature, you
can choose to use the breath weapon and damage type
of any of the chromatic dragons from the list, instead of
using the entry for your patron.
When you finish a long rest, you can choose to change
the damage type that your Draconic Essence feature
grants resistance to. Choose one from acid, cold, fire,
lightning, or poison damage.

FIERY BREATH
Prerequisite: 12th levd burning hands known as a
warlock spell
When you cast burning hands, you can do so as a bonus
action, requiring only verbal components. Once you do,
you can't do so again until you finish a long rest.

OPEN THE GATE BELOW
Prerequisite: 12th levei Any Water-themed Patron or
Hydromancer feat
You can expend a warlock spell slot to cast the new dark
lagoon spelL requiring only somatic components. Once
you do so, you can't do so again until you finish a long rest.

TENTACLE GROWTH
Prerequisite: 12th levei Fathomless Patron or Great
Old One Patron
You have an additional extremely flexible arm (a tentacle)
that has reach 10 feet. Melee weapons wielded using
this arm and no other arms have an additional 5 feet of
reach, but the arm cannot wear shields. You also have
advantage on ability checks made to grapple using this
arm. If the arm is cut off or destroyed, it regrows with no
apparent damage when you finish a long rest.
You can take this invocation multiple times.

GIFT OF THE 'TREANTS
Prerequisite: 15th levei Archfey Patron or any Plantthemed
Patron
You can expend the 8th-level use of your Mystic Arcanum
to cast the new animate tree spell

HELLISH BLOOD
Prerequisite: 15th levei Fiend Patron or Pyromancer
Feat
You are constantly affected by a lesser form of fire shield
(warm option) that deals only ld6 damage. You can also
expend a warlock spell slot to cast fire shield (as warm
option only) on yourself as a bonus action, to increase
the effect to that of a fire shield that deals 2d8 + ld6 fire
damage for the normal duration.

LOST TO THE COSMOS
Prerequisite: 15th level
You can cast nondetection using a warlock spell slot
without requiring components, but you can only target
yourself when you do so.

PULL OF THE DARK
Prerequisite: 15th levei Fathomless Patron, Eldritch
Blast cantrip
When you hit a creature with eldritch blast more than
once in a turn, you can have it make a Strength saving
throw. On a failed saving throw, the creature is knocked
prone or pulled up to 10 feet toward you (your choice}

WAVE CALLER
Prerequisite: 15th levd Any Water-themed Patron or
Hydromancer feat
You can cast control water at-wilL expending no spell
slots and requiring only verbal components.

CONSIGN TO THE EARTH
Prerequisite: 18th levei Any Earth-themed or Gravethemed
Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new earth whelm spell

FOG FORM
Prerequisite: 18th levei Any Water-themed Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new ordainment of mist spell

MAGMA FORM
Prerequisite: 18th levei Any Fire-themed Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new ordainment of lava spell

STEEL FORM
Prerequisite: 18th levd Any Tech-themed or Weaponthemed
Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new ordainment of metal spell

PEERS OF THE PATRON
Prerequisite: 18th levei Archfey Patron or any
Elemental-themed Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new summon primal spirit spell

TAME THE WIND
Prerequisite: 18th levei Any Air-themed or Stormthemed
Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new wind wake spell

THOUSAND-YEAR FLOOD
Prerequisite: 18th levei Any Water-themed Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new grand flood spell

VOLCANIC HERALD
Prerequisite: 18th levei Any Fire-themed Patron
You can expend the 9th-level use of your Mystic Arcanum
to cast the new caldera spell

```
invocations = {
    'Agonizing Blast': [agonizingblast, agonizingblast_prereq],
    'Armor of Shadows': [armorofshadows, armorofshadows_prereq],
    'Ascendent Step': [ascendantstep, ascendantstep_prereq],
    'Aspect of the Moon': [aspectofthemoon, aspectofthemoon_prereq],
    'Beast Speech': [beastspeech, beastspeech_prereq],
    'Beguiling Influence': [beguilinginfluence, beguilinginfluence_prereq],
    'Bewitching Whispers': [bewitchingwhispers, bewitchingwhispers_prereq],
    'Bond of the Talisman': [bondofthetalisman, bondofthetalisman_prereq],
    'Book of Ancient Secrets': [bookofancientsecrets, bookofancientsecrets_prereq],
    "Chain Master's Fury": [chainmastersfury, chainmastersfury_prereq],
    'Chains of Carceri': [chainsofcarceri, chainsofcarceri_prereq],
    "Cloak of Flies": [cloakofflies, cloakofflies_prereq],
    "Devil's Sight": [devilssight, devilssight_prereq],
    'Dreadful Word': [dreadfulword, dreadfulword_prereq],
    'Eldritch Armor': [eldritcharmor, eldritcharmor_prereq],
    'Eldritch Mind': [eldritchmind, eldritchmind_prereq],
    'Eldritch Sight': [eldritchsight, eldritchsight_prereq],
    'Eldritch Smite': [eldritchsmite, eldritchsmite_prereq],
    'Eldritch Spear': [eldritchspear, eldritchspear_prereq],
    'Eyes of the Rune Keeper': [eyesoftherunekeeper, eyesoftherunekeeper_prereq],
    'Far Scribe': [farscribe, farscribe_prereq],
    'Fiendish Vigor': [fiendishvigor, fiendishvigor_prereq],
    'Gaze of Two Minds': [gazeoftwominds, gazeoftwominds_prereq],
    'Ghostly Gaze': [ghostlygaze, ghostlygaze_prereq],
    'Gift of the Depths': [giftofthedepths, giftofthedepths_prereq],
    'Gift of the Ever-Living Ones': [giftoftheeverlivingones, giftoftheeverlivingones_prereq],
    'Gift of the Protectors': [giftoftheprotectors, giftoftheprotectors_prereq],
    'Grasp of Hadar': [graspofhadar, graspofhadar_prereq],
    'Improved Pact Weapon': [improvedpactweapon, improvedpactweapon_prereq],
    'Investment of the Chain Master': [investmentofthechainmaster, investmentofthechainmaster_prereq],
    'Ironfell Blade': [ironfellblade, ironfellblade_prereq],
    'Iron Sky Starfall': [ironskystarfall, ironskystarfall_prereq],
    'Lance of Lethargy': [lanceoflethargy, lanceoflethargy_prereq],
    'Lifedrinker': [lifedrinker, lifedrinker_prereq],
    'Maddening Hex': [maddeninghex, maddeninghex_prereq],
    'Mask of Many Faces': [maskofmanyfaces, maskofmanyfaces_prereq],
    'Master of Myriad Forms': [masterofmyriadforms, masterofmyriadforms_prereq],
    'Minions of Chaos': [minionsofchaos, minionsofchaos_prereq],
    'Mire the Mind': [mirethemind, mirethemind_prereq],
    'Misty Vision': [mistyvision, mistyvision_prereq],
    'One with Shadows': [onewithshadows, onewithshadows_prereq],
    'Otherworldly Leap': [otherworldlyleap, otherworldlyleap_prereq],
    'Protection of the Talisman': [protectionofthetalisman, protectionofthetalisman_prereq],
    'Rebuke of the Talisman': [rebukeofthetalisman, rebukeofthetalisman_prereq],
    'Relentless Hex': [relentlesshex, relentlesshex_prereq],
    'Repelling Blast': [repellingblast, repellingblast_prereq],
    'Sculptor of Flesh': [sculptorofflesh, sculptorofflesh_prereq],
    'Shard Star Warrior': [shardstarwarrior, shardstarwarrior_prereq],
    'Shroud of Shadow': [shroudofshadow, shroudofshadow_prereq],
    'Sign of Ill Omen': [signofillomen, signofillomen_prereq],
    'Starlight Hex': [starlighthex, starlighthex_prereq],
    'Thief of Five Fates': [thiefoffivefates, thiefoffivefates_prereq],
    'Thirsting Blade': [thirstingblade, thirstingblade_prereq],
    'Tomb of Levistus': [tomboflevistus, tomboflevistus_prereq],
    "Tricker's Escape": [trickstersescape, trickstersescape_prereq],
    'Visions of Distant Realms': [visionsofdistantrealms, visionsofdistantrealms_prereq],
    'Voices of the Chain Master': [voicesofthechainmaster, voicesofthechainmaster_prereq],
    'Whispers of the Grave': [whispersofthegrave, whispersofthegrave_prereq],
    'Witch Sight': [witchsight, witchsight_prereq]
}
def chooseinvocation(npc):
    choices = {}
    for (name, fnlist) in invocations.items():
        prereqfn = fnlist[1]
        if prereqfn(npc) and name not in npc.invocations:
            choices[name] = fnlist[0]

    (invocationname, invocationfn) = choose("Choose an Eldritch Invocation: ", choices)
    npc.invocations.append(invocationname)
    invocationfn(npc)

allclasses['Warlock'].chooseinvocation = chooseinvocation
```
