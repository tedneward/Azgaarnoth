# Eldritch Invocations

### Agonizing Blast
*Prerequisite: eldritch blast cantrip*

When you cast [eldritch blast](../../Magic/Spells/eldritch-blast.md), add your Charisma modifier to the damage it deals on a hit.

```
def agonizingblast(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Agonizing Blast.*** When you cast *eldritch blast*, add {npc.CHAbonus()} to the damage it deals on a hit.") )

def agonizingblast_prereq(npc): return True
```

### Ally of Flame
*Prerequisite: Phoenix Patron*

Any time an ally makes a saving throw against one of your spells that deals fire damage they take half damage on a failed save and no damage on success. You may expend one hit dice to have a creature automatically succeed on their saving throw, you can protect as many creatures as you have hit dice.

```
def allyofflame(npc):
    npc.actions.append("***Ally of Flame.*** Any time an ally makes a saving throw against one of your spells that deals fire damage they take half damage on a failed save and no damage on success. You may expend one hit dice to have a creature automatically succeed on their saving throw, you can protect as many creatures as you have hit dice.")

def allyofflame_prereq(npc):
    return npc.subclasses[allclasses['Warlock']].name == 'Phoenix'
```

### Ambassador of the Depths
*Prerequisite: 5th level*

You can expend a warlock spell slot to cast [dive](../../Magic/Spells/dive.md). While the spell affects a target, that target also has darkvision that extends out to a range of 120 feet.

```
def ambassadorofthedepths(npc):
    npc.actions.append(f"***Ambassador of the Depths.*** You can expend a warlock spell slot to cast {spelllinkify('dive')}. While the spell affects a target, that target also has darkvision that extends out to a range of 120 feet.")

def ambassadorofthedepths_prereq(npc):
    return npc.levels('Warlock') >= 5
```

### Arcane Specialty
*Prerequisite: Pact of the Skull feature*

Choose one school of magic. When you use your magic skull as a spellcasting focus to cast a warlock spell of 1st-level or higher, if the spell belongs to the chosen school of magic, you can also cast a cantrip that belongs to the same school of magic as part of the same action. You can't use this invocation to cast eldritch blast.

Once you use this invocation, you must finish a long rest before you can use it again. When you finish a long rest with the skull in your possession, you can change the school of magic that you chose for this invocation.

```
def arcanespecialty(npc):
    npc.actions.append("***Arcane Specialty (Recharges on long rest).*** When you finish a long rest with the skull in your possession, you can select one school of magic (abjuration, conjuration, etc). When you use your magic skull as a spellcasting focus to cast a warlock spell of 1st-level or higher, if the spell belongs to the chosen school of magic, you can also cast a cantrip that belongs to the same school of magic as part of the same action. You can't use this invocation to cast eldritch blast.")

def arcanespecialty_prereq(npc):
    return npc.pactboon == 'Pact of the Skull'
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

### Baleful Blood
*Prerequisite: Pact of the Blood feature*

When you take slashing, bludgeoning, or piercing damage, or damage from a Blood spell, you can use your reaction to inflict vengeance on the creature that damaged you. If the target is within 60 feet of you and you can see it, it takes force damage equal to your Charisma modifier (minimum 1 damage).

You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
def balefulblood(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Baleful Blood ({npc.proficiencybonus()}/Recharges on long rest). When you take slashing, bludgeoning, or piercing damage, or damage from a Blood spell, you inflict vengeance on the creature that damaged you; if the target is within 60 feet of you and you can see it, it takes {npc.CHAbonus()} force damage.") )

def balefulblood_prereq(npc):
    return npc.pactboon == 'Pact of the Blood'
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
    npc.traits.append("***Book of Ancient Secrets.*** You can now inscribe magical rituals in your Book of Shadows. Choose two 1st-level spells that have the *ritual* tag from any class's spell list (the two needn't be from the same list). The spells appear in the book and don't count against the number of spells you know. With your Book of Shadows in hand, you can cast the chosen spells as rituals. You can't cast the spells except as rituals, unless you've learned them by some other means. You can also cast a warlock spell you know as a ritual if it has the *ritual* tag. On your adventures, you can add other ritual spells to your Book of Shadows. When you find such a spell, you can add it to the book if the spell's level is equal to or less than half your warlock level (rounded up) and if you can spare the time to transcribe the spell. For each level of the spell, the transcription process takes 2 hours and costs 50 gp for the rare inks needed to inscribe it. There is no limit to the number of rituals you can have in your Book.")

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

### Clinging Blaze
*Prerequisite: 9th level; Phoenix Patron.* 

Any time a creature takes fire damage from one of your spells of first level or higher they are set [ablaze](../../Conditions/Ablaze.md).

```
def clingingblaze(npc):
    npc.traits.append("***Clinging Blaze.*** Any time a creature takes fire damage from one of your spells of first level or higher they are set [ablaze](http://azgaarnoth.tedneward.com/conditions/Ablaze/).")

def clingingblaze_prereq(npc):
    return npc.levels('Warlock') >= 9 and npc.subclasses[allclasses['Warlock']].name == 'Phoenix'
```

### Cloak of Flies
*Prerequisite: 5th level*

As a bonus action, you can surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action.

The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes poison damage equal to your Charisma modifier (minimum of 0 damage).

Once you use this invocation, you can't use it again until you finish a short or long rest.

```
def cloakofflies(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Cloak of Flies (Recharges on short or long rest).*** You surround yourself with a magical aura that looks like buzzing flies. The aura extends 5 feet from you in every direction, but not through total cover. It lasts until you're incapacitated or you dismiss it as a bonus action. The aura grants you advantage on Charisma (Intimidation) checks but disadvantage on all other Charisma checks. Any other creature that starts its turn in the aura takes {npc.CHAbonus()} poison damage.") )

def cloakofflies_prereq(npc): return npc.levels('Warlock') >= 5
```

### Cold Terror
When you deal psychic damage to a creature using a warlock spell or feature, you ignore resistance to psychic damage unless the creature also has resistance or immunity to cold damage, and you treat vulnerability to cold damage as vulnerability to both damage types.

```
def coldterror(npc):
    npc.traits.append("***Cold Terror.*** When you deal psychic damage to a creature using a warlock spell or feature, you ignore resistance to psychic damage unless the creature also has resistance or immunity to cold damage, and you treat vulnerability to cold damage as vulnerability to both damage types.")

def coldterror_prereq(npc): return True
```

### Cursed Possessions
You gain the ability to imbue objects that you own with your dark magic to use to afflict others from afar. As an action, you can cast a warlock spell that would normally require an action or a bonus action, expending a spell slot as normal, infusing the magic into an object that you have carried for at least one long rest, to take effect later.

When a creature other than you touches the object while the spell is active, you are magically aware of it (though you do not know who the creature is). At that time, you can choose to have the spell take effect as if you had touched them directly and cast the spelL or as if you had cast it at the location of the object. Once you do, the spell is discharged and no longer infuses the object.

The spell discharges on its own without affecting anything when you finish a long rest. It also does so if you use this invocation again, or if you end your tum more than 300 feet away from the cursed item.

```
def cursedpossessions(npc):
    npc.actions.append("***Cursed Possessions.*** You can cast a warlock spell that would normally require an action or a bonus action, expending a spell slot as normal, infusing the magic into an object that you have carried for at least one long rest, to take effect later. When a creature other than you touches the object while the spell is active, you are magically aware of it (though you do not know who the creature is). At that time, you can choose to have the spell take effect as if you had touched them directly and cast the spelL or as if you had cast it at the location of the object. Once you do, the spell is discharged and no longer infuses the object. The spell discharges on its own without affecting anything when you finish a long rest. It also does so if you use this invocation again, or if you end your tum more than 300 feet away from the cursed item.")

def cursedpossessions_prereq(npc): return True
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

When you cast [eldritch blast](../../Magic/Spells/eldritch-blast.md), its range is 300 feet.

```
def eldritchspear(npc):
    npc.actions.append("***Eldritch Spear.*** When you cast eldritch blast, its range is 300 feet.")

def eldritchspear_prereq(npc): return True
```

### Elemental Attunement
When you finish a long rest, you choose one of four elements below to attune to. While attuned to an element, you know an associated cantrip as a warlock spell, and it doesn't count against the number of cantrips you can know as a warlock. You gain the following benefits while attuned to each element:

* **Air.** You know the [gust](../../Magic/Spells/gust.md) cantrip, and you can hold your breath for twice as long.
* **Earth.** You know the [mold earth](../../Magic/Spells/mold-earth.md) cantrip, and you have advantage on ability checks made to climb earth or stone.
* **Fire.** You know the [control flames](../../Magic/Spells/control-flames.md) cantrip, and you have advantage on saving throws made to resist the effects of extreme heat.
* **Water.** You know the [shape water](../../Magic/Spells/shape-water.md) cantrip, and you have advantage on saving throws made to resist the effects of extreme cold.

```
def elementalattunement(npc):
    npc.traits.append(f"***Elemental Attunement.*** When you finish a long rest, you choose one of four elements below to attune to. While attuned to an element, you know an associated cantrip as a warlock spell, and it doesn't count against the number of cantrips you can know as a warlock. You gain the following benefits while attuned to each element: **Air.** You know the {spelllinkify('gust')} cantrip, and you can hold your breath for twice as long. **Earth.** You know the {spelllinkify('mold earth')} cantrip, and you have advantage on ability checks made to climb earth or stone. **Fire.** You know the {spelllinkify('control flames')} cantrip, and you have advantage on saving throws made to resist the effects of extreme heat. **Water.** You know the {spelllinkify('shape water')} cantrip, and you have advantage on saving throws made to resist the effects of extreme cold.")

def elementalattunement_prereq(npc): return True
```

### Enticing Gaze
*Prerequisite: Vampiric Aspect invocation*

As an action, you can attempt to enthrall one creature that you can see within 60 feet. If the target can see you, it must succeed on a Wisdom saving throw or become charmed by you for 1 minute. While it is charmed in this way, it regards you as a trusted friend to be heeded and protected If you or your companions do anything harmful to the target, the effect ends immediately. You can't use this invocation while you are in sunlight.

Once you use this invocation, you must finish a long rest before you can use it again.

```
def enticinggaze(npc):
    npc.actions.append("***Enticing Gaze.*** You attempt to enthrall one creature that you can see within 60 feet. If the target can see you, it must succeed on a Wisdom saving throw or become charmed by you for 1 minute. While it is charmed in this way, it regards you as a trusted friend to be heeded and protected If you or your companions do anything harmful to the target, the effect ends immediately. You can't use this invocation while you are in sunlight.")

def enticinggaze_prereq(npc):
    return "Vampiric Aspect" in npc.invocations
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

### Glimpse the Visage of Death
When you deal necrotic damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target is blinded until the start of your next turn. Creatures that can't be charmed and creatures that can't be frightened are immune to this invocation.

Once you use this invocation, you must finish a long rest before you can use it again.

```
def glimpsethevisageofdeath(npc):
    npc.traits.append("***Glimpse the Visage of Death (Recharges on long rest).*** When you deal necrotic damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target is blinded until the start of your next turn. Creatures that can't be charmed and creatures that can't be frightened are immune to this invocation.")

def glimpsethevisageofdeath_prereq(npc): return True
```

### Grasp of Hadar
*Prerequisite: eldritch blast cantrip*

Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.

```
def graspofhadar(npc):
    npc.actions.append("***Grasp of Hadar.*** Once on each of your turns when you hit a creature with your eldritch blast, you can move that creature in a straight line 10 feet closer to you.")

def graspofhadar_prereq(npc): return True
```

### Grasping Shadow
*Prerequisite: Pact of the Shadow feature*

Your shadow servant can grapple creatures. You can use a bonus action on your turn to command the servant to grapple a creature within 5 feet of the servant, using your warlock spellcasting ability in place of its Strength for the Strength (Athletics) check.

```
def graspingshadow(npc):
    npc.bonusactions.append("***Grasping Shadow.*** You can command your shadow servant to grapple a creature within 5 feet of the servant, using your warlock spellcasting ability in place of its Strength for the Strength (Athletics) check.")

def graspingshadow_prereq(npc):
    return npc.pactboon == 'Pact of the Shadow'
```

### Hag's Heritage
*Prerequisite: Progenitor Patron*

You have advantage on saving throws against being charmed, magic can't put you to sleep, and you are a fey instead of your normal creature type. Also, you gain proficiency in your choice of either Deception, Perception, or Stealth, and you can speak, read, and write your choice of either AbyssaL Giant, Primordial or Sylvan.

In addition, you can use an action to cover yourself and anything you are wearing or carrying with a magical illusion that makes you look like an ugly creature of your general size and humanoid shape. The effect ends if you take a bonus action to end it or if you die.

The changes wrought by this effect fail to hold up to physical inspection. For example, you could appear to have no hair, but someone touching your head might feel your hair, if you have any hair. Otherwise, a creature must take an action to visually inspect the illusion and succeed on a Intelligence (Investigation) check against your warlock spell save DC to tell you are disguised

However, you also have the following flaws:

* **Foul Hunger.** You must eat five times as much food as normal for your size, but humanoid flesh counts as five times as much food for you.

* **Hideous Countenance.** Your true appearance is ugly, and those who see your true form or your cursed form may become disgusted or worse. Whenever a creature sees either your true form or your cursed form for the first time, it must succeed on a DC 13 Wisdom saving throw or else it becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek to flee from you or make you leave the area in nonviolent ways (at the DM's discretion1 depending on the nature of your interaction with it.

```
def hagsheritage_prereq(npc): return npc.subclasses[allclasses['Warlock']].name == 'Progenitor'
def hagsheritage(npc):
    npc.traits.append("***Hag's Heritage.*** You have advantage on saving throws against being charmed.")
    npc.conditionimmunities.append("sleep")
    npc.proficiencies.append(choose("Choose a proficiency: ", ['Deception','Perception','Stealth']))
    npc.languages.append(choose("Choose a language: ", ['Abyssal','Giant', 'Primordial','Sylvan']))

    npc.defer(lambda npc: npc.actions.append(f"***Hag's Heritage: Cast Illusion.*** You cover yourself and anything you are wearing or carrying with a magical illusion that makes you look like an ugly creature of your general size and humanoid shape. The effect ends if you take a bonus action to end it or if you die. A creature must take an action to visually inspect the illusion and succeed on a Intelligence (Investigation) check (DC {8 + npc.proficiencybonus() + npc.CHAbonus()}) to tell you are disguised. However, the changes wrought by this effect fail to hold up to physical inspection.") )
    
    npc.traits.append("***Foul Hunger.*** You must eat five times as much food as normal for your size, but humanoid flesh counts as five times as much food for you.")
    npc.traits.append("***Hideous Countenance.*** Your true appearance is ugly, and those who see your true form or your cursed form may become disgusted or worse. Whenever a creature sees either your true form or your cursed form for the first time, it must succeed on a Wisdom saving throw (DC 13) or else it becomes hostile toward you. A creature prone to violence might attack you. Another creature might seek to flee from you or make you leave the area in nonviolent ways (at the DM's discretion) depending on the nature of your interaction with it.")
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

### Increased Vitality
*Prerequisite: Phoenix Patron*

You gain a number of extra hit dice equal to your Charisma modifier.

```
def increasedvitality(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Increased Vitality.*** You gain {npc.CHAbonus()} extra hit dice.") )

def increasedvitality_prereq(npc):
    return npc.subclasses[allclasses['Warlock']].name == 'Phoenix'
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
def mistyvisions(npc):
    npc.traits.append(f"***Misty Visions.*** You can cast {spelllinkify('silent image')} at will, without expending a spell slot or material components.")

def mistyvisions_prereq(npc): return True
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

### Power of the Moon
*Prerequisite: Progenitor Patron*

While you're in your Cursed Shapechanger form and you're in moonlight at night, you gain a + 1 bonus to AC and attack rolls and have advantage on saving throws. In addition, you count as a shapechanger at all times.

However, you also have the following flaw:

***Silver Hypersensitivity.*** You have vulnerability to bludgeoning, piercing, and slashing damage dealt by silvered weapons. While touching silver, you have disadvantage on attack rolls and ability checks.

```
def powerofthemoon_prereq(npc): return npc.subclasses[allclasses['Warlock']].name == 'Progenitor'
def powerofthemoon(npc):
    npc.traits.append("***Power of the Moon.*** You count as a shapechanger at all times. While you're in your Cursed Shapechanger form, and in moonlight at night, you gain a +1 bonus to AC and attack rolls and have advantage on saving throws.")
    npc.traits.append("***Silver Hypersensitivity.*** You have vulnerability to bludgeoning, piercing, and slashing damage dealt by silvered weapons. While touching silver, you have disadvantage on attack rolls and ability checks.")
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

### Restorative Power
*Prerequisite: 5th level; Phoenix Patron* 

You can cast [greater restoration](../../Magic/Spells/greater-restoration.md) using a warlock spell slot, and one of your tears as an additional component.

```
def restorativepower(npc):
    npc.actions.append(f"***Restorative Power.*** You can cast greater {spelllinkify('restoration')} using a warlock spell slot, and one of your tears as an additional component.")

def restorativepower_prereq(npc):
    return npc.levels('Warlock') >= 5 and npc.subclasses[allclasses['Warlock']].name == 'Phoenix'
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

### Vampiric Aspect
*Prerequisite: Progenitor Patron*

You have resistance to necrotic damage and you are an undead in addition to your normal creature type, but when a game effect targets you, you choose whether it treats you as undead or as your normal creature type.

You can also choose one extra trait from your Cursed Shapechanger feature. You gain the benefit of that trait while in your cursed form. Finally, your Beast of the Curse feature treats bats, rats, and wolves as your chosen beasts, instead of your original choice.

However, you also have the following flaws:

***Forbiddance.*** You can't enter a residence without an invitation from one of the occupants.

***Harmed by Running Water.*** You take acid damage equal to 5 + your level when you end your turn in running water.

***No Reflection.*** You do not appear in reflections.

***Stake to the Heart.*** If a piercing weapon made of wood is driven into your heart while you are incapacitated, you are paralyzed until the stake is removed.

***Sunlight Hypersensitivity.*** You take radiant damage equal to 5 + your level when you start your turn in sunlight. While in sunlight, you have disadvantage on attack rolls and ability checks.

```
def vampiricaspect_prereq(npc): return npc.subclasses[allclasses['Warlock']].name == 'Progenitor'
def vampiricaspect(npc):
    npc.damageresistances.append('necrotic')
    npc.type = npc.type + "/undead"
    npc.traits.append("***Vampiric Aspect.*** You are an undead in addition to your normal creature type, but when a game affect targets you, you choose whether it treats you as undead or as your normal creature type.")
    npc.defer(lambda npc: npc.traits.append(f"***Water Sensitivity.*** You take {5 + npc.levels('Warlock')} acid damage when you end your turn in running water.") )
    npc.defer(lambda npc: npc.traits.append(f"***Radiant Sensitivity.*** You take {5 + npc.levels('Warlock')} radiant damage when you start your turn in sunlight. While in sunlight, you have disadvantage of attack rolls and ability checks.") )
```

### Venomous Familiar
*Prerequisite: Defiler or Kraken or Lurker Patron, Pact of the Chain feature*

When your familiar hits a creature with a melee attack, you can expend a warlock spell slot to deal 1d12 bonus poison damage to the target for each level of the spell slot used.

```
def venomousfamiliar(npc):
    npc.traits.append("***Venomous Familiar.*** When your familiar hits a creature with a melee attack, you can expend a warlock spell slot to deal 1d12 bonus poison damage to the target for each level of the spell slot used.")

def venomousfamiliar_prereq(npc):
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

-------------------------------------------------------------------------------------------------------------------------------

# New Invocations

### Accursed Blade
*Prerequisite: 5th level; Progenitor Patron; Pact of the Blade feature*

You gain a + 1 bonus to the damage rolls for weapon attacks made using your pact weapon while you are in your Cursed Shapechanger form.

Also, when you critically hit a creature or reduce one to 0 hit points with a weapon attack using your pact weapon or natural weapons while you're in your Cursed Shapechanger form, you can use your reaction and expend a warlock spell slot to cast [bestow curse](../../Magic/Spells/bestow-curse.md) on the target, requiring no components. Your weapon attack counts as the touch required by the spelL and you do not need to know the spell to cast it in this way.

### Anathema's Ward
*Prerequisite: 5th level; Defiler Patron*

You learn [protection from poison](../../Magic/Spells/protection-from-poison.md) as a warlock spell, and it doesn't count against the number of spells you can learn as a warlock. When you cast the spell, its range is 30 feet, and you don't have to touch the target.

### Beckon the Darkness
*Prerequisite: 18th level; Fiend or Hexblade Patron*

You can expend the 9th-level use of your Mystic Arcanum to cast [midnight](../../Magic/Spells/midnight.md).

### Befoul Food and Drink
*Prerequisite: 5th level; Defiler Patron or Hag's Heritage invocation*

You learn the [poison food and drink](../../Magic/Spells/poison-food-or-drink.md) spell as a warlock spelL and it doesn't count against the number of spells you can learn as a warlock. You can choose to cast the spell without expending a spell slot or requiring material components. Once you do so, you can't do so again until you finish a long rest.

### Blighted Blade
*Prerequisite: 7th level; Defiler Patron or Hag's Heritage invocation*

You can cast [envenomed weapon](../../Magic/Spells/envenomed-weapon.md) using a warlock spell slot. Once you use this invocation, you must finish a long rest before you can use it again.

### Bloodline Guardian
*Prerequisite: 7th level; Progenitor Patron*

You can cast [mordenkainen's faithful hound](../../Magic/Spells/mordenkainens-faithful-hound.md) using a warlock spell slot. Once you use this invocation, you must finish a long rest before you can use it again.

### Contagious Curse
*Prerequisite: 7th level; Power of the Moon invocation*

When you hit a creature with a natural weapon while in your Cursed Shapechanger form, you can subject the target to your lycanthropic curse. The target must succeed on a Constitution saving throw or else it is infected with your cursed beast's version of lycanthropy (if any). This ability does not grant you any special control or influence over the target, though it may change their alignment.

Once you use this invocation, you must finish a long rest before you can use it again.

### Cursed Regeneration
*Prerequisite: 5th level; Progenitor Patron*

You regain hit points equal to half your proficiency bonus once every hour, so long as this invocation is still functioning the entire time. At the start of each of your turns, you can choose to expend up that many hit dice to regain hit points as if you had finished a short rest. However, you must also choose one of the following flaws to gain when you learn this invocation:

* **Sunlight Weakness.** This invocation doesn't function if you are in sunlight or running water. If you start your turn in sunlight, take radiant damage, or end your turn in running water, this invocation doesn't function until the end of your next turn.
* **Alchemical Weakness.** This invocation doesn't function if any part of your body is touching fire or silver. If you take fire damage or damage from an attack using a silvered weapon, this invocation doesn't function until the end of your next turn.

### Dark and Terrible
*Prerequisite: 5th level; Progenitor Patron*

While you are in your cursed form, you can make an attack with your natural weapon twice, instead of once, when you take the Attack action on your turn. Also, your natural weapon deals 1d10 damage instead of 1d8 and counts as magical for overcoming resistance or immunity.

### Deathly Chills
When you deal cold damage to a creature using a warlock spell or feature, you ignore resistance to cold damage unless the creature also has resistance or immunity to necrotic damage, and you treat vulnerability to necrotic damage as vulnerability to both damage types.

### Desert Roamer
*Prerequisite: 5th level*

You are adapted to both hot climates and cold climates, and you don't need to drink water to survive.

### Eldritch Digestion
When you deal acid damage to a creature using a warlock spell or feature, you ignore resistance to acid damage unless the creature also has resistance or immunity to force damage, and you treat vulnerability to force damage as vulnerability to both damage types.

### Eldritch Mount
*Prerequisite: 5th level*

You can expend a warlock spell slot to cast [phantom steed](../../Magic/Spells/phantom-steed.md), although you are the only creature that can ride the steed conjured by the spell.

Once you use this invocation, you must finish a long rest before you can use it again.

### Enchanted Slumber
*Prerequisite: 15th level*

You can expend the 7th-level use of your Mystic Arcanum to cast [suspend animation](../../Magic/Spells/suspend-animation.md).

### Extended Family
*Prerequisite: 7th level; Progenitor Patron*

Choose another three beasts for your Beast of the Curse feature. You gain the benefits of that feature for all of your chosen beasts instead of only one.

You can take this invocation multiple times.

### Fang of the Malison
*Prerequisite: 12th level Defiler Patron, Pact of the Blade feature*

You can create a curved dagger using your Pact of the Blade feature. This weapon deals an extra 1d4 poison damage on a hit. When you hit a creature with it, you can expend a warlock spell slot to deal 1d8 bonus poison damage per spell level to the target and cause it to become poisoned until the start of your next turn.

### Flame Walker
*Prerequisite: 5th level*

You and any equipment you are wearing or carrying are immune to the damage dealt by nonmagical fire, and you can breathe ashes, smoke, and the stinking cloud spell without any negative effects. This can't prevent damage dealt by traps or creatures, such as the breath weapon of a red dragon or the blast of a fire cannon.

### Focused Regeneration
*Prerequisite: 15th level, Cursed Regeneration invocation*

Whenever you finish a short rest, you can expend two of your warlock spell slots to cast regenerate on yourself without needing components, but the spell only restores hit points while your Cursed Regeneration functions. 

Once you use this invocation, you must finish a long rest before you can use it again.

### Gestalt Mindlink
*Prerequisite: 9th level; Great Old One Patron*

You can cast [rary's telepathic bond](../../Magic/Spells/rarys-telepathic-bond.md) using a warlock spell slot. Once you use this invocation, you must finish a long rest before you can use it again.

### Glamour Walk
*Prerequisite: 9th level; Archfey Patron or Hags Heritage invocation*

You can cast the new [glamour veil](../../Magic/Spells/glamour-veil.md) spell without expending spell slots or requiring material components.

### Harbinger of the Pack
*Prerequisite: Progenitor Patron, Pact of the Chain feature*

In addition to Touch spells, you can cast spells that conjure, summon, or create another creature (such as conjure animals) through the familiar summoned by your Pact of the Chain feature as if the familiar was you.

### Heavenly Bolts
When you deal lightning damage to a creature using a warlock spell or feature, you ignore resistance to lightning damage unless the creature also has resistance or immunity to radiant damage, and you treat vulnerability to radiant damage as vulnerability to both damage types.

### Howl of Terror
*Prerequisite: 9th levei Power of the Moon invocation*

You gain one extra use of your Cursed Shapechanger feature's terrifying sound, which you regain each time you finish a long rest. If you are in moonlight when you release the sound, the range increases to 120 feet and creatures within 15 feet of you that can also see you make the saving throw with disadvantage.

### Hush of Winter
When you deal cold damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target is deafened and can't speak until the end of your next turn. Once you use this invocation, you must finish a long rest before you can use it again.

### Lunar Transformation
*Prerequisite: Power of the Moon invocation*

When you see the full moon in the sky, you can use your reaction to use your Cursed Shapechanger feature, without releasing a terrifying sound When you do so, you can choose to gain temporary hit points equal to your warlock level that last until you change form again.

Once you gain these temporary hit points, you can't gain them again until you finish a long rest.

### Maddening Poison
When you deal poison damage to a creature using a warlock spell or feature, you ignore resistance to poison damage unless the creature has resistance or immunity to psychic damage, and you treat vulnerability to psychic damage as vulnerability to both damage types.

### Minions of Darkness
*Prerequisite: 5th level*

You can cast [shadow spies](../../Magic/Spells/shadow-spies.md) using a warlock spell slot. Once you use this invocation, you must finish a long rest before you can use it again.

If you have the Pact of the Cauldron (from Legends of Prestige & Prowess), you can use your magic cauldron as the material component for the spell.

### Mirror World Summoning
*Prerequisite: 18th level; Archfey or Enigma Patron*

You can expend the 9th-level use of your Mystic Arcanum to cast [duplication](../../Magic/Spells/duplication.md).

### Noxious Fumes
When you deal acid damage to a creature using a warlock spell or feature, you can force the target to make a Constitution saving throw. On a failed save, the target is poisoned until the end of its next turn. Once you use this invocation, you must finish a long rest before you can use it again.

### Perchance to Dream
*Prerequisite: 15th level, Archfey Patron or Hag's Heritage invocation*

You can expend the 8th-level use of your Mystic Arcanum to cast [sandman's slumber](../../Magic/Spells/sandmans-slumber.md).

### Phantom Bargain
*Prerequisite: 9th level*

You can cast [spectral calling](../../Magic/Spells/spectral-calling.md) using a warlock spell slot. Once you use this invocation, you must finish a long rest before you can use it again.

### Plaguebearer
*Prerequisite: 12th levei Progenitor Patron*

When you hit a creature with a natural weapon granted by your Cursed Shapechanger form, you can use your reaction to expend a warlock spell slot to cast [contagion](../../Magic/Spells/contagion.md) upon the target, requiring no components.

Once you use this invocation, you must finish a long rest before you can use it again.

### Plague Herald
*Prerequisite: 18th level; Celestial or Undead Patron or Hag's Heritage invocation*

You can expend the 9th-level use of your Mystic Arcanum to cast [pestilence](../../Magic/Spells/pestilence.md).

### Prismatic Blaze
When you deal fire damage to a creature that isn't blinded using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target becomes charmed until the end of its next turn. While charmed in this way, the target is incapacitated and has a speed of 0. The effect ends if the target takes any additional damage or if someone else uses an action to shake it out of its stupor. Once you use this invocation, you must finish a long rest before you can use it again.

### Psychic Convulsion
When you deal psychic damage to a creature using a warlock spell or feature, you can force the target to make a Constitution saving throw. On a failed save, the target drops whatever it is holding and is restrained until the start of your next turn.

Once you use this invocation, you must finish a long rest before you can use it again.

### Recorded Lineage
*Prerequisite: Progenitor or Ancestor Patron, Pact of the Tome feature*

Your Book of Shadows holds the stories of your patron's children who came before you. Before you make an ability check, you can spend 1 minute studying your book to see if it contains relevant stories. Roll 1d6. On a 6, you find ancient inspiration in the tome, and gain advantage on the check. You cannot use this invocation more than once for the same check.

Once you gain this advantage, you must finish a long rest before you can gain it again.

### Reins of the Nightmare
*Prerequisite: 15th level, Fiend or Hexblade Patron*

You can cast find greater steed using a warlock spell slot, but when you do, you summon a [nightmare](../../Creatures/Extraplanar/Nightmare.md) instead of the normal options. It is always a fiend, and the steed disappears after 1 hour.

Once you use this invocation, you must finish a long rest before you can use it again.

### Release from the Skull
*Prerequisite: 12th level; Pact of the Skull feature*

While you are holding your magic skull, you can use your action to cast [spectral calling](../../Magic/Spells/spectral-calling.md) without expending a spell slot or requiring material components. When cast in this way, the spell summons the spirit of the skull, which is friendly to you and your allies. While the spirit is released, it uses the statistics for a psychic remnant (pg. 175). When the spell ends or the spirit is reduced to 0 hit points, it returns back inside the skull and is unharmed.

Once you use this invocation, you must finish a long rest before you can use it again.

### Ritual of the Damned
*Prerequisite: 18th level; Fiend or Undead Patron*

You can expend the 9th-level use of your Mystic Arcanum to cast [awaken the dead](../../Magic/Spells/awaken-the-dead.md).

### Sanguine Vigor
*Prerequisite: 12th level; Pact of the Blood feature*

You have advantage on saving throws against poison or disease. In addition, while you have no more than half of your hit points remaining, you also have advantage on Constitution saving throws.

### Scent of Corruption
*Prerequisite: 9th level; Defiler Patron*

You can cast detect poison and disease at-will, without expending a spell slot or requiring components.

### Scorching Radiance
When you deal radiant damage to a creature using a warlock spell or feature, you ignore resistance to radiant damage unless the creature also has resistance or immunity to fire damage, and you treat vulnerability to fire damage as vulnerability to both damage types.

### Slumber Puppet
*Prerequisite: 5th level*

You can cast [telekinesis](../../Magic/Spells/telekinesis.md) at-will, without expending a spell slot, but you can only target unconscious creatures with the spell when you cast it in this way..

### Speech of the Far Realm
*Prerequisite: 15th level; Enigma or Great Old One Patron*

You can expend the 8th-level use of your Mystic Arcanum to cast [telepathy](../../Magic/Spells/telepathy.md).

### Star of Darkness
*Prerequisite: 18th level; Fiend or Great Old One Patron*

You can expend the 9th-level use of your Mystic Arcanum to cast [gravity well](../../Magic/Spells/gravity-well.md).

### Strength from Hunger
*Prerequisite: 9th levei Vampiric Aspect invocation*

When you hit with an attack using your claws, you can choose to grapple the target instead of dealing damage. Also, when you hit a creature you have grappled with an attack using your bite, you can expend a warlock spell slot to add ld6 bonus necrotic damage per slot level to the attack. If the target of the attack is a valid target for your Dark Consumption feature, you also regain hit points equal to the necrotic damage dealt.

### Stretching Shadow
*Prerequisite: 12th level; Pact of the Shadow feature*

The range of each your warlock spells of 1st-level or higher is increased by 30 feet when you're in an area of dim light or darkness and your shadow servant is in your space. This doesn't increase the range of Touch spells or the reach of melee spell attacks.

### Stupefying Toxin
When you deal poison damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target has disadvantage on ability checks and attack rolls until the start of your next turn. While a creature is affected by this invocation and it is poisoned, it is also incapacitated.

Once you use this invocation, you must finish a long rest before you can use it again.

### Talisman of Adoption
*Prerequisite: Progenitor Patron, Pact of the Talisman feature*

While wearing your talisman, a creature gains all the benefits of your Beast of the Curse and Cursed Shapechanger features, including the ability to transform. It must use your cursed beast and cannot choose its own. If the talisman is removed while the wearer is transformed using the talisman's power, the creature returns to its original form. The wearer is not able to release a terrifying sound when it transforms.

### Twilight of the Soul
When you deal necrotic damage to a creature using a warlock spell or feature, you ignore resistance to necrotic damage unless the creature has resistance or immunity to radiant damage, and you treat vulnerability to radiant damage as vulnerability to both damage types.

### Umbra Flame
When you deal fire damage to a creature using a warlock spell or feature, you ignore resistance to fire damage unless the creature also has resistance or immunity to necrotic damage, and you treat vulnerability to necrotic damage as vulnerability to both damage types.

### Unholy Aspect
You learn the [thaumaturgy](../../Magic/Spells/thaumaturgy.md) spell, it is a warlock spell for you, and it doesn't count against the number of cantrips you can learn. Also, you do not need to provide any components when you cast [thaumaturgy](../../Magic/Spells/thaumaturgy.md), and you can cast it with a casting time of 1 bonus action.

### Vampiric Magic
*Prerequisite: 7th level; Vampiric Aspect invocation*

Choose two spells you know as a warlock. Those spells become Blood spells for you, and you can choose to change their names accordingly (such as changing hellish rebuke to "hellish bloodspray", or changing hex to "blood hex"). Whenever you gain a warlock leveL you can choose to replace one of these two spells with a different warlock spell you know. The old spell returns to its original form, and the new spell becomes a blood spell following the same rules.

In addition, when you deal damage to a creature that has blood using the eldritch blast can trip or a Blood spell, you can consume a portion of its spilt blood and regain hit points equal to your Charisma modifier (minimum 1 hit point). The next time you cast a blood spell before the end of your next turn, you also gain 2 temporary hit points.

You can use this invocation to heal a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

### Voice From Beyond
When you deal thunder damage to a creature using a warlock spell or feature, you ignore resistance to thunder damage unless the creature also has resistance or immunity to psychic damage, and you treat vulnerability to psychic damage as vulnerability to both damage types.

### Welcoming Light
When you deal radiant damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target becomes charmed by you until the end of your next turn. While charmed in this way, the target regards you as a friendly acquaintance. Once you use this invocation, you must finish a long rest before you can use it again.

### Whisper the Dread Wind
When you deal thunder damage to a creature using a warlock spell or feature, you can force the target to make a Wisdom saving throw. On a failed save, the target is frightened of you until the end of its next turn. Once you use this invocation, you must finish a long rest before you can use it again.

### Withering Lightning
When you deal lightning damage to a creature using a warlock spell or feature, you can force the target to make a Constitution saving throw. On a failed save, the target's hit point maximum is reduced for 1 minute by an amount equal to the lightning damage it took. Any effect that removes a disease allows the target's hit point maximum to return to normal before that time passes. Once you use this invocation, you must finish a long rest before you can use it again.

WEIGHTLESSNESS
Prerequisite: 5th level

You can cast feather fall targeting only yourself at will without expending a spell slot or requiring components.

EXPLOSIVE VENGEANCE
Prerequisite: 7th level Pact of the Chain, fireball known as a warlock spell

When another creature deals damage to your familiar and reduces it to O hit points, you can choose to use your reaction to cast fireball using a warlock spell slot centered at the location of your familiar, even if it is outside your normal range or line of sight for the spell. The spell originates from your familiar. After you do this, you gain one level of exhaustion and you can't cast any spells of 1st-level or higher on your next turn. Once you use this invocation, you must finish a long rest before you can use it again.

GRAVEBORNE
Prerequisite: 7th level
While you are buried or burrowing in earth or sealed underground, you don't need to eat, drink, or breathe.

BREATH OF BAHAMUT
Prerequisite: 9th level Dragon Patron (Any Metallic)

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

TIAMAT'S BARGAIN
Prerequisite: 9th level; Dragon Patron (Any Chromatic)

When you use your Breath of the Wynn feature, you can choose to use the breath weapon and damage type of any of the chromatic dragons from the list, instead of
using the entry for your patron. When you finish a long rest, you can choose to change the damage type that your Draconic Essence feature grants resistance to. Choose one from acid, cold, fire, lightning, or poison damage.

FIERY BREATH
Prerequisite: 12th level; burning hands known as a warlock spell

When you cast burning hands, you can do so as a bonus action, requiring only verbal components. Once you do, you can't do so again until you finish a long rest.

OPEN THE GATE BELOW
Prerequisite: 12th level; Any Water-themed Patron or Hydromancer feat

You can expend a warlock spell slot to cast the new dark lagoon spelL requiring only somatic components. Once you do so, you can't do so again until you finish a long rest.

TENTACLE GROWTH
Prerequisite: 12th level; Fathomless Patron or Great Old One Patron

You have an additional extremely flexible arm (a tentacle) that has reach 10 feet. Melee weapons wielded using this arm and no other arms have an additional 5 feet of reach, but the arm cannot wear shields. You also have advantage on ability checks made to grapple using this arm. If the arm is cut off or destroyed, it regrows with no apparent damage when you finish a long rest. You can take this invocation multiple times.

GIFT OF THE TREANTS
Prerequisite: 15th levei Archfey Patron or any Plant-themed Patron

You can expend the 8th-level use of your Mystic Arcanum to cast the new animate tree spell

HELLISH BLOOD
Prerequisite: 15th levei Fiend Patron or Pyromancer Feat

You are constantly affected by a lesser form of fire shield (warm option) that deals only ld6 damage. You can also expend a warlock spell slot to cast fire shield (as warm option only) on yourself as a bonus action, to increase the effect to that of a fire shield that deals 2d8 + 1d6 fire damage for the normal duration.

LOST TO THE COSMOS
Prerequisite: 15th level

You can cast nondetection using a warlock spell slot without requiring components, but you can only target yourself when you do so.

PULL OF THE DARK
Prerequisite: 15th level; Fathomless Patron, Eldritch Blast cantrip

When you hit a creature with eldritch blast more than once in a turn, you can have it make a Strength saving throw. On a failed saving throw, the creature is knocked prone or pulled up to 10 feet toward you (your choice).

WAVE CALLER
Prerequisite: 15th level; Any Water-themed Patron or Hydromancer feat

You can cast control water at-will, expending no spell slots and requiring only verbal components.

CONSIGN TO THE EARTH
Prerequisite: 18th level; Any Earth-themed or Grave-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the earth whelm spell.

FOG FORM
Prerequisite: 18th level; Any Water-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the ordainment of mist spell.

MAGMA FORM
Prerequisite: 18th level; Any Fire-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the ordainment of lava spell.

STEEL FORM
Prerequisite: 18th level; Any Weapon-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the ordainment of metal spell.

PEERS OF THE PATRON
Prerequisite: 18th level; Archfey Patron or any Elemental-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the summon primal spirit spell.

TAME THE WIND
Prerequisite: 18th level; Any Air-themed or Storm-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the wind wake spell.

THOUSAND-YEAR FLOOD
Prerequisite: 18th level; Any Water-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the grand flood spell.

VOLCANIC HERALD
Prerequisite: 18th level; Any Fire-themed Patron

You can expend the 9th-level use of your Mystic Arcanum to cast the caldera spell.

```
invocations = {
    'Agonizing Blast': [agonizingblast, agonizingblast_prereq],
    'Ally of Flame': [allyofflame, allyofflame_prereq],
    'Ambassador of the Depths': [ambassadorofthedepths, ambassadorofthedepths_prereq],
    'Arcane Specialty': [arcanespecialty, arcanespecialty_prereq],
    'Armor of Shadows': [armorofshadows, armorofshadows_prereq],
    'Ascendent Step': [ascendantstep, ascendantstep_prereq],
    'Aspect of the Moon': [aspectofthemoon, aspectofthemoon_prereq],
    'Baleful Blood': [balefulblood, balefulblood_prereq],
    'Beast Speech': [beastspeech, beastspeech_prereq],
    'Beguiling Influence': [beguilinginfluence, beguilinginfluence_prereq],
    'Bewitching Whispers': [bewitchingwhispers, bewitchingwhispers_prereq],
    'Bond of the Talisman': [bondofthetalisman, bondofthetalisman_prereq],
    'Book of Ancient Secrets': [bookofancientsecrets, bookofancientsecrets_prereq],
    "Chain Master's Fury": [chainmastersfury, chainmastersfury_prereq],
    'Chains of Carceri': [chainsofcarceri, chainsofcarceri_prereq],
    'Clinging Blaze': [clingingblaze, clingingblaze_prereq],
    "Cloak of Flies": [cloakofflies, cloakofflies_prereq],
    'Cold Terror': [coldterror, coldterror_prereq],
    'Cursed Possessions': [cursedpossessions, cursedpossessions_prereq],
    "Devil's Sight": [devilssight, devilssight_prereq],
    'Dreadful Word': [dreadfulword, dreadfulword_prereq],
    'Eldritch Armor': [eldritcharmor, eldritcharmor_prereq],
    'Eldritch Mind': [eldritchmind, eldritchmind_prereq],
    'Eldritch Sight': [eldritchsight, eldritchsight_prereq],
    'Eldritch Smite': [eldritchsmite, eldritchsmite_prereq],
    'Eldritch Spear': [eldritchspear, eldritchspear_prereq],
    'Elemental Attunement': [elementalattunement, elementalattunement_prereq],
    'Enticing Gaze': [enticinggaze, enticinggaze_prereq],
    'Eyes of the Rune Keeper': [eyesoftherunekeeper, eyesoftherunekeeper_prereq],
    'Far Scribe': [farscribe, farscribe_prereq],
    'Fiendish Vigor': [fiendishvigor, fiendishvigor_prereq],
    'Gaze of Two Minds': [gazeoftwominds, gazeoftwominds_prereq],
    'Ghostly Gaze': [ghostlygaze, ghostlygaze_prereq],
    'Gift of the Depths': [giftofthedepths, giftofthedepths_prereq],
    'Gift of the Ever-Living Ones': [giftoftheeverlivingones, giftoftheeverlivingones_prereq],
    'Gift of the Protectors': [giftoftheprotectors, giftoftheprotectors_prereq],
    'Glimpse the Visage of Death': [glimpsethevisageofdeath, glimpsethevisageofdeath_prereq],
    'Grasp of Hadar': [graspofhadar, graspofhadar_prereq],
    'Grasping Shadow': [graspingshadow, graspingshadow_prereq],
    "Hag's Heritage": [hagsheritage, hagsheritage_prereq],
    'Improved Pact Weapon': [improvedpactweapon, improvedpactweapon_prereq],
    'Increased Vitality': [increasedvitality, increasedvitality_prereq],
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
    'Misty Visions': [mistyvisions, mistyvisions_prereq],
    'One with Shadows': [onewithshadows, onewithshadows_prereq],
    'Otherworldly Leap': [otherworldlyleap, otherworldlyleap_prereq],
    'Power of the Moon': [powerofthemoon, powerofthemoon_prereq],
    'Protection of the Talisman': [protectionofthetalisman, protectionofthetalisman_prereq],
    'Rebuke of the Talisman': [rebukeofthetalisman, rebukeofthetalisman_prereq],
    'Relentless Hex': [relentlesshex, relentlesshex_prereq],
    'Repelling Blast': [repellingblast, repellingblast_prereq],
    'Restorative Power': [restorativepower, restorativepower_prereq],
    'Sculptor of Flesh': [sculptorofflesh, sculptorofflesh_prereq],
    'Shard Star Warrior': [shardstarwarrior, shardstarwarrior_prereq],
    'Shroud of Shadow': [shroudofshadow, shroudofshadow_prereq],
    'Sign of Ill Omen': [signofillomen, signofillomen_prereq],
    'Starlight Hex': [starlighthex, starlighthex_prereq],
    'Thief of Five Fates': [thiefoffivefates, thiefoffivefates_prereq],
    'Thirsting Blade': [thirstingblade, thirstingblade_prereq],
    'Tomb of Levistus': [tomboflevistus, tomboflevistus_prereq],
    "Tricker's Escape": [trickstersescape, trickstersescape_prereq],
    'Vampiric Aspect': [vampiricaspect, vampiricaspect_prereq],
    'Venomous Familiar': [venomousfamiliar, venomousfamiliar_prereq],
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
