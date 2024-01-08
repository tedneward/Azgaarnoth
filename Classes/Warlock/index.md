# Warlock
Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular.

```
name = 'Warlock'
description = "***Class: Warlock.*** Warlocks are seekers of the knowledge that lies hidden in the fabric of the multiverse. Through pacts made with mysterious beings of supernatural power, warlocks unlock magical effects both subtle and spectacular."
```

*You must have a Charisma score of 13 or higher in order to multiclass in or out of this class.*

Level|Proficiency Bonus|Cantrips Known|Spells Known|Spell Slots|Slot Level|Invocations Known|Features
-----|-----------------|--------------|------------|-----------|----------|-----------------|--------
1st  |+2|2|2 |1|1st|-|[Otherworldly Patron](#otherworldly-patron), [Pact Magic](#pact-magic)
2nd  |+2|2|3 |2|1st|2|[Eldritch Invocations](#eldritch-invocations)
3rd  |+2|2|4 |2|2nd|2|[Pact Boon](#pact-boon)
4th  |+2|3|5 |2|2nd|2|[Ability Score Improvement](#ability-score-improvement)
5th  |+3|3|6 |2|3rd|3|
6th  |+3|3|7 |2|3rd|3|[Otherworldly Patron feature](#otherworldly-patron)
7th  |+3|3|8 |2|4th|4|
8th  |+3|3|9 |2|4th|4|[Ability Score Improvement](#ability-score-improvement)
9th  |+4|3|10|2|5th|5|
10th |+4|4|10|2|5th|5|[Otherworldly Patron feature](#otherworldly-patron)
11th |+4|4|11|3|5th|5|[Mystic Arcanum](#mystic-arcanum) (6th level)
12th |+4|4|11|3|5th|6|[Ability Score Improvement](#ability-score-improvement)
13th |+5|4|12|3|5th|6|[Mystic Arcanum](#mystic-arcanum) (7th level)
14th |+5|4|12|3|5th|6|[Otherworldly Patron feature](#otherworldly-patron)
15th |+5|4|13|3|5th|7|[Mystic Arcanum](#mystic-arcanum) (8th level)
16th |+5|4|13|3|5th|7|[Ability Score Improvement](#ability-score-improvement)
17th |+6|4|14|4|5th|7|[Mystic Arcanum](#mystic-arcanum) (9th level)
18th |+6|4|14|4|5th|8|
19th |+6|4|15|4|5th|8|[Ability Score Improvement](#ability-score-improvement)
20th |+6|4|15|4|5th|8|[Eldritch Master](#eldritch-master)

```
class PactMagic:
    def __init__(self, npc):
        self.npc = npc
        self.maxcantripsknown = 0
        self.cantripsknown = []
        self.maxspellsknown = 0
        self.spellsknown = []
        self.spellslots = 0
        self.slotlevel = 0

    def calculate(self):
        npclevels = self.npc.levels('Warlock')
        self.maxcantripsknown = 2 if npclevels < 4 else 3 if npclevels < 10 else 4
        match npclevels:
            case 1: self.maxspellsknown = 2
            case 2: self.maxspellsknown = 3
            case 3: self.maxspellsknown = 4
            case 4: self.maxspellsknown = 5
            case 5: self.maxspellsknown = 6
            case 6: self.maxspellsknown = 7
            case 7: self.maxspellsknown = 8
            case 8: self.maxspellsknown = 9
            case 9 | 10: self.maxspellsknown = 10
            case 11 | 12: self.maxspellsknown = 11
            case 13 | 14: self.maxspellsknown = 12
            case 15 | 16: self.maxspellsknown = 13
            case 17 | 18: self.maxspellsknown = 14
            case 19 | 20: self.maxspellsknown = 15
        self.spellslots = 1 if npclevels < 2 else 2 if npclevels < 11 else 3 if npclevels < 17 else 4
        self.slotlevel = 1 if npclevels < 3 else 2 if npclevels < 5 else 3 if npclevels < 7 else 4 if npclevels < 9 else 5

    def spellsavedc(self): return 8 + self.npc.proficiencybonus() + self.npc.CHAbonus()

    def spellattackmodifier(self): return self.npc.proficiencybonus() + self.npc.CHAbonus()
```

As a warlock, you gain the following class features.

## Hit Points
**Hit Dice**: 1d8 per warlock level

**Hit Points at 1st Level**: 8 + your Constitution modifier

**Hit Points at Higher Levels**: 1d8 (or 5) + your Constitution modifier per warlock level after 1st

```
def everylevel(npc): npc.hits('d10')
```

## Proficiencies
**Armor**: Light armor

**Weapons**: Simple weapons

**Tools**: None

**Saving Throws**: Wisdom, Charisma

**Skills**: Choose two from Arcana, Deception, History, Intimidation, Investigation, Nature, and Religion

```
def level1(npc):
    npc.savingthrows.append("WIS")
    npc.savingthrows.append("CHA")

    for arm in armor['light']:
        npc.proficiencies.append(arm)
    for wpn in weapons['simple-melee'] | weapons['simple-ranged']:
        npc.proficiencies.append(wpn)

    skills = ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion']
    chooseskill(npc, skills)
    chooseskill(npc, skills)
```

## Equipment
You start with the following equipment, in addition to the equipment granted by your background:
* (a) a light crossbow and 20 bolts or (b) any simple weapon
* (a) a component pouch or (b) an arcane focus
* (a) a scholar's pack or (b) a dungeoneer's pack
* Leather armor, any simple weapon, and two daggers

```
    npc.equipment.append("Leather armor")
    npc.equipment.append("Simple weapon")
    npc.equipment.append("Two daggers")
    npc.equipment.append("Light crossbow and 20 bolts OR any simple weapon")
    npc.equipment.append("Component pouch OR arcane focus")
    npc.equipment.append("Scholar's pack OR dungeoneer's pack")
    npc.equipment.append("Dungeoneer's pack, or explorer's pack")
    npc.armorclass['Leather armor'] = 11
```

## Otherworldly Patron
At 1st level, you have struck a bargain with an otherworldly being of your choice:

* [Ancestor Spirit](AncestorSpirit.md)
* [Archfey](Archfey.md)
* [Celestial](Celestial.md)
* [Elemental Evil](ElementalEvil.md)
* [Fiend](Fiend.md)
* [Great Old One](GreatOldOne.md)
* [Hexblade](Hexblade.md)
* [Kraken](Kraken.md)
* [Legendary Dragon](LegendaryDragon.md)
* [Lurker in the Deep](LurkerDeep.md)
* [Noble Genie](NobleGenie.md)
* [Raven Queen](RavenQueen.md)
* [Ring](Ring.md)
* [Seeker](Seeker.md)
* [Undying](Undying.md)
* [UndyingLight](UndyingLight.md)
* [The Witch](Witch.md)

Your choice grants you features at 1st level and again at 6th, 10th, and 14th level.

```
    # Choose subclass
    (_, subclass) = choose("Choose a Patron:", subclasses)
    npc.subclasses[allclasses['Warlock']] = subclass
    npc.description.append(subclass.description)
```

## Pact Magic
Your arcane research and the magic bestowed on you by your patron have given you facility with spells.

Warlock spells, despite being similar in some respects to arcane spells cast by wizards, are in fact a divergent form of divine magic; as a result, warlocks know only the [spells listed here](SpellList.md), and even then only at their paton's whim. Patrons have been known, however, to grant warlocks insight into the deep mysteries of the universe and reveal new magical means to emulate arcane or divine spells, however, and so warlocks often scour Azgaarnoth looking for fragments of insight or knowledge that will gain favor with their patron and persuade the patron to reveal new mystical insights.

> Game notes: In other words, DM's choice about adding new warlock spells to the "known" list, and the warlock may need to do some in-game activity or adventure to obtain them.

### Cantrips
You know two cantrips of your choice from the [warlock spell list](SpellList.md#cantrip-level-spells). You learn additional warlock cantrips of your choice at higher levels, as shown in the Cantrips Known column of the Warlock table.

### Spell Slots
The Warlock table shows how many spell slots you have. The table also shows what the level of those slots is; all of your spell slots are the same level. To cast one of your warlock spells of 1st level or higher, you must expend a spell slot. You regain all expended spell slots when you finish a short or long rest.

For example, when you are 5th level, you have two 3rd-level spell slots. To cast the 1st-level spell Witch Bolt, you must spend one of those slots, and you cast it as a 3rd-level spell.

### Spells Known of 1st Level and Higher
At 1st level, you know two [1st-level spells of your choice from the warlock spell list](SpellList.md#1st-level-spells).

The Spells Known column of the Warlock table shows when you learn more warlock spells of your choice of 1st level or higher. A spell you choose must be of a level no higher than what's shown in the table's Slot Level column for your level. When you reach 6th level, for example, you learn a new warlock spell, which can be 1st, 2nd, or 3rd level.

Additionally, when you gain a level in this class, you can choose one of the warlock spells you know and replace it with another spell from the warlock spell list, which also must be of a level for which you have spell slots.

### Spellcasting Ability
Charisma is your spellcasting ability for your warlock spells, so you use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a warlock spell you cast and when making an attack roll with one.

**Spell save DC** = 8 + your proficiency bonus + your Charisma modifier

**Spell attack modifier** = your proficiency bonus + your Charisma modifier

### Spellcasting Focus
You can use an arcane focus as a spellcasting focus for your warlock spells.

### Spell Versatility
Whenever you finish a long rest, you can replace one spell you learned from this Pact Magic feature with another spell from the warlock spell list. The new spell must be the same level as the spell you replace.

```
    # Something something pact magic
    npc.pactmagic = PactMagic(npc)
    npc.defer(lambda npc: npc.pactmagic.calculate() )
    npc.defer(lambda npc: npc.actions.append(f"***Pact Magic.*** {npc.pactmagic.maxcantripsknown} cantrips known. {npc.pactmagic.spellslots} {npc.pactmagic.slotlevel}th-level spell slots. {npc.pactmagic.maxspellsknown} spells known. **Spell save DC** {npc.pactmagic.spellsavedc()}. **Spell attack modifier** +{npc.pactmagic.spellattackmodifier()}. Cantrips known: {', '.join(npc.pactmagic.cantripsknown)}. Spells known: {', '.join(npc.pactmagic.spellsknown)}.") )
```

## Eldritch Invocations
*2nd-level warlock feature*

In your study of occult lore, you have unearthed [eldritch invocations](Invocations.md), fragments of forbidden knowledge that imbue you with an abiding magical ability.

You gain two eldritch invocations of your choice. When you gain certain warlock levels, you gain additional invocations of your choice, as shown in the Invocations Known column of the Warlock table.

Additionally, when you gain a level in this class, you can choose one of the invocations you know and replace it with another invocation that you could learn at that level.

A level prerequisite in an invocation refers to warlock level, not character level.

```
    npc.pactboon = ''
    npc.invocations = []

def level2(npc):
    chooseinvocation(npc)
    chooseinvocation(npc)
def level5(npc):
    chooseinvocation(npc)
def level7(npc):
    chooseinvocation(npc)
def level9(npc):
    chooseinvocation(npc)
#level12 has both ability score and invocation
def level15(npc):
    chooseinvocation(npc)
def level18(npc):
    chooseinvocation(npc)
```

## Pact Boon
*3rd-level warlock feature*

Your otherworldly patron bestows a gift upon you for your loyal service. You gain one of the following features of your choice.

* **Pact of the Blade**: You can use your action to create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage.

    Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.

    You can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest.

    You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks.

```
def pactoftheblade(npc):
    npc.actions.append("***Summon Pact Weapon.*** You create a pact weapon in your empty hand. You can choose the form that this melee weapon takes each time you create it. You are proficient with it while you wield it. This weapon counts as magical for the purpose of overcoming resistance and immunity to nonmagical attacks and damage. Your pact weapon disappears if it is more than 5 feet away from you for 1 minute or more. It also disappears if you use this feature again, if you dismiss the weapon (no action required), or if you die.")
    npc.traits.append("***Bind Weapon.*** You can transform one magic weapon into your pact weapon by performing a special ritual while you hold the weapon. You perform the ritual over the course of 1 hour, which can be done during a short rest. You can then dismiss the weapon, shunting it into an extradimensional space, and it appears whenever you create your pact weapon thereafter. You can't affect an artifact or a sentient weapon in this way. The weapon ceases being your pact weapon if you die, if you perform the 1-hour ritual on a different weapon, or if you use a 1-hour ritual to break your bond to it. The weapon appears at your feet if it is in the extradimensional space when the bond breaks.")  
```

* **Pact of the Blood**: As part of your deepening pact, your patron replaces some of your blood with magic blood of their own. You have advantage on saving throws against blood magic, and you are immune to the [blood reading](../../Magic/Spells/blood-reading.md) spell. While you have no more than half of your hit points remaining, you can use a free hand as a spellcasting focus for your warlock spells.

    In addition, as a bonus action, you can spill your own blood and spend a number of your remaining hit dice equal to your warlock spell slot leveL but instead of healing you take 1d8 necrotic damage per hit die expended that ignores resistance and immunity. This damage doesn't cause saving throws for concentration.
    
    The next warlock spell you cast on this turn using your Pact Magic feature is also a Blood spell in addition to its other schools and does not require a spell slot. If the casting time is 1 bonus action, you can cast the spell as part of using this feature. 

    However, the spell can't restore a dead creature to life. Also, unless it is a necromancy spelL it can't cause any creature to regain hit points; instead of restoring hit points, it grants temporary hit points equal to half as many hit points as it would have restored. Once you use this feature to expend hit dice, you can't do so again until you finish a short or long rest.

```
def pactoftheblood(npc):
    npc.traits.append(f"***Pact of the Blood.*** You have saving throws against blood magic. You are immune to the {spelllinkify('blood reading')} spell. While you have no more than half of your hit points remaining, you can use a free hand as a spellcasting focus for your warlock spells.")
    npc.defer(lambda npc: npc.bonusactions.append(f"***Pact of the Blood: Blood Spell (Recharges on short or long rest).*** You spill your own blood and spend up to {npc.pactmagic.slotlevel} hit dice, but instead of healing you take 1d8 necrotic damage per hit die expended that ignores resistance and immunity. This damage doesn't cause saving throws for concentration. The next warlock spell you cast on this turn using your Pact Magic feature is also a Blood spell in addition to its other schools, and does not require a spell slot. If the casting time is 1 bonus action, you can cast the spell as part of using this feature. However, the spell can't restore a dead creature to life. Also, unless it is a necromancy spelL it can't cause any creature to regain hit points; instead of restoring hit points, it grants temporary hit points equal to half as many hit points as it would have restored.") )
```

* **Pact of the Chain**: You learn the [Find Familiar](../../Magic/Spells/find-familiar.md) spell and can cast it as a ritual. The spell doesn't count against your number of spells known. When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit, or sprite.Additionally, when you take the Attack action, you can forgo one of your own attacks to allow your familiar to use its reaction to make one attack of its own.

```
def pactofthechain(npc):
    npc.traits.append(f"***Pact of the Chain.*** You can cast {spelllinkify('find familiar')} as a ritual. When you cast the spell, you can choose one of the normal forms for your familiar or one of the following special forms: imp, pseudodragon, quasit, or sprite.")
    npc.actions.append("***Familiar Attack.*** When you take the Attack action, you can forgo one of your own attacks to allow your familiar to use its reaction to make one attack of its own.")
```

*  **Pact of the Ring**: You bear a nigh-indestructible ring. If the ring is lost or somehow destroyed, you can perform a 1-hour ceremony to create a replacement. While you bear this ring, once during your turn when you hit with an attack roll for a melee weapon or a cantrip, you can inflict extra radiant damage equal to your Charisma bonus on one target you hit with that attack. If the damage for the attack already includes your Charisma bonus (such as if you hit with eldritch blast and have the Agonizing Blast eldritch invocation), you cannot inflict this extra damage. An attack which includes this extra damage blazes with a violet, starlight glare.

```
def pactofthering(npc):
    npc.actions.append("***Pact of the Ring.*** Once during your turn when you hit with an attack roll for a melee weapon or a cantrip, you can inflict extra radiant damage equal to your Charisma bonus on one target you hit with that attack. If the damage for the attack already includes your Charisma bonus (such as if you hit with eldritch blast and have the Agonizing Blast eldritch invocation), you cannot inflict this extra damage. An attack which includes this extra damage blazes with a violet, starlight glare.")
```

* **Pact of the Shadow**: Your patron grants your own shadow a mind of its own, a dark reflection of your own mind that is subservient to you. Your shadow can stretch to move a short distance away from you and perform simple tasks at your mental command, acting as your servant.

    You are constantly accompanied by a magical servant that uses the rules from the unseen servant spelL except it has hit points equal to your proficiency bonus and it isn't invisible unless it is entirely in darkness. The servant shares its tum in initiative with your's. It can't move more than 10 feet away from you, but it can move through your space and end its tum there. While it is in your space and hasn't taken any action, left your space, or interacted with any object or creature since the start of your last turn, it is indistinguishable from a normal shadow, it is immune to damage, and it moves with you.

    When you cast a warlock spelL you can choose to cast it from your location or the location of your shadow servant. In addition, you can use a bonus action on your turn to command the servant to shove a creature that you can see within 5 feet of the servant, using your warlock spellcasting ability in place of its Strength for the Strength (Athletics) check.

    While you are in dim light or darkness, the servant can be up to 20 feet away from you instead of only 10 feet away. If at any time the servant is too far away from you, it is instantly pulled into your space. If the servant is reduced to 0 hit points, it disappears, and it reappears in your space with all its hit points when you finish a short or long rest or when you expend a warlock spell slot to conjure it with a 1 minute ritual.

```
def pactoftheshadow(npc):
    npc.traits.append(f"***Pact of the Shadow.*** You are constantly accompanied by a magical servant that uses the rules from the {spelllinkify('unseen servant')} spell, except it has hit points equal to your proficiency bonus and it isn't invisible unless it is entirely in darkness. The servant shares its turn in initiative with yours. It can't move more than 10 feet away from you, but it can move through your space and end its tum there. While it is in your space and hasn't taken any action, left your space, or interacted with any object or creature since the start of your last turn, it is indistinguishable from a normal shadow, it is immune to damage, and it moves with you. When you cast a warlock spelL you can choose to cast it from your location or the location of your shadow servant. While you are in dim light or darkness, the servant can be up to 20 feet away from you instead of only 10 feet away. If at any time the servant is too far away from you, it is instantly pulled into your space. If the servant is reduced to 0 hit points, it disappears, and it reappears in your space with all its hit points when you finish a short or long rest or when you expend a warlock spell slot to conjure it with a 1 minute ritual.")
    npc.defer(lambda npc: npc.bonusactions.append(f"***Pact of the Shadow: Shove.*** You command the shadow servant to shove a creature that you can see within 5 feet of the servant, the Strength (Athletics) check DC is {npc.pactmagic.spellsavedc}.") )
```

* **Pact of the Skull**: Your patron provides you with a magic skull (or another eerie object, such as a doll, an egg, a mirror, an orb, etc.) that houses an eldritch spirit of knowledge. The skull can speak and understand the same languages as you, but it can't move or perform any type of action. The skull has hit points equal to twice your proficiency bonus, its AC is equal to 10 + your spellcasting ability modifier, and it is immune to both poison and disease. Its ability scores (other than Strength and Dexterity, which are both 1) are equal to your Charisma score. You can also use the skull as a spellcasting focus for your warlock spells.

    When you finish a long rest with the skull in your possession, you can consult the spirit within to bolster your knowledge for a time. Choose Arcana, History, Medicine, Nature, Religion, or Survival. Alternatively, you can choose one tool proficiency or one language. You gain proficiency with the chosen skill or tooL or you can speak, read, and write the chosen language. This effect lasts until you finish your next long rest.

    In addition, whenever you finish a short or long rest, you can choose to receive eldritch knowledge from the skull. You learn one warlock cantrip of your choice. This cantrip doesn't count against the number of cantrips you can learn as a warlock. If you receive eldritch knowledge from the skull again, or if the skull is destroyed, you no longer know the chosen cantrip. 
    
    If the skull is lost or destroyed, you can receive a new one from your patron at the end of a long rest, but the process magically afflicts you with one level of exhaustion. This also destroys the previous skull if it still exists, turning it to ash.

```
def pactoftheskull(npc):
    npc.defer(lambda npc: npc.equipment.append(f"***Pact of the Skull: the Skull.*** Your patron provides you with a magic skull (or another eerie object, such as a doll, an egg, a mirror, an orb, etc.) that houses an eldritch spirit of knowledge. The skull can speak and understand the same languages as you, but it can't move or perform any type of action. The skull has {npc.proficiencybonus() * 2} hit points, its AC is {10 + npc.CHAbonus()}, and it is immune to both poison and disease. Its ability scores (other than Strength and Dexterity, which are each 1) are {npc.CHA()}. You can also use the skull as a spellcasting focus for your warlock spells. If the skull is lost or destroyed, you can receive a new one from your patron at the end of a long rest, but the process magically afflicts you with one level of exhaustion. This also destroys the previous skull if it still exists, turning it to ash.") )

    npc.traits.append("***Pact of the Skull.*** When you finish a long rest with the skull in your possession, you can consult the spirit within to bolster your knowledge for a time. Choose Arcana, History, Medicine, Nature, Religion, or Survival Alternatively, you can choose one tool proficiency or one language. You gain proficiency with the chosen skill or tooL or you can speak, read, and write the chosen language. This effect lasts until you finish your next long rest. In addition, whenever you finish a short or long rest, you can choose to receive eldritch knowledge from the skull. You learn one warlock can trip of your choice. This cantrip doesn't count against the number of cantrips you can learn as a warlock. If you receive eldritch knowledge from the skull again, or if the skull is destroyed, you no longer know the chosen cantrip.")
```

* **Pact of the Talisman**: Your patron gives you a special amulet, a talisman that can aid you, or anyone else who wears it, when the need is great. When the wearer makes an ability check with a skill in which they lack proficiency, they can add a d4 to the roll. If you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet.

    The talisman turns to ash when you die.

```
def pactofthetalisman(npc):
    npc.equipment.append("***Talisman of the Pact.*** When the wearer makes an ability check with a skill in which they lack proficiency, they can add a d4 to the roll. If you lose the talisman, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous amulet. The talisman turns to ash when you die.")
```

* **Pact of the Tome**: Your patron gives you a grimoire called a Book of Shadows. When you gain this feature, choose three cantrips from any class's spell list. While the book is on your person, you can cast those cantrips at will. They are considered warlock spells for you, and they needn't be from the same spell list. They don't count against your number of cantrips known.

  If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.

```
def pactofthetome(npc):
    npc.equipment.append("***Book of Shadows.*** While the book is on your person, you can cast the three CHOOSE cantrips at will. If you lose your Book of Shadows, you can perform a 1-hour ceremony to receive a replacement from your patron. This ceremony can be performed during a short or long rest, and it destroys the previous book. The book turns to ash when you die.")

pactboons = {
    'Pact of the Blade': pactoftheblade,
    'Pact of the Blood': pactoftheblood,
    'Pact of the Chain': pactofthechain,
    'Pact of the Ring': pactofthering,
    'Pact of the Shadow': pactoftheshadow,
    'Pact of the Skull': pactoftheskull,
    'Pact of the Talisman': pactofthetalisman,
    'Pact of the Tome': pactofthetome
}
def choosepact(npc):
    (pactname, pactfn) = choose("Choose your Pact: ", pactboons)
    npc.pactboon = pactname
    pactfn(npc)

def level3(npc):
    choosepact(npc)
```


## Ability Score Improvement
When you reach 4th level, and again at 8th, 12th, 16th, and 19th level, you can increase one ability score of your choice by 2, or you can increase two ability scores of your choice by 1. As normal, you can't increase an ability score above 20 using this feature.

```
def level4(npc): abilityscoreimprovement(npc)
def level8(npc): abilityscoreimprovement(npc)
def level12(npc): 
    abilityscoreimprovement(npc)
    chooseinvocation(npc)
def level16(npc): abilityscoreimprovement(npc)
def level19(npc): abilityscoreimprovement(npc)
```

## Mystic Arcanum
*11th-level warlock feature*

Your patron bestows upon you a magical secret called an arcanum. Choose one 6th-level spell from the warlock spell list as this arcanum.

You can cast your arcanum spell once without expending a spell slot. You must finish a long rest before you can do so again.

At higher levels, you gain more warlock spells of your choice that can be cast in this way: one 7th-level spell at 13th level, one 8th-level spell at 15th level, and one 9th-level spell at 17th level. You regain all uses of your Mystic Arcanum when you finish a long rest.

```
def level11(npc):
    def arcanumcasting(npc):
        arcanum = innatecaster(npc, 'CHA', 'Mystic Arcanum')
        arcanum.perday[1] = ['CHOOSE-6th-level']
        if npc.levels('Warlock') >= 13:
            arcanum.perday[1].append('CHOOSE-7th-level')
        if npc.levels('Warlock') >= 15:
            arcanum.perday[1].append('CHOOSE-8th-level')
        if npc.levels('Warlock') >= 17:
            arcanum.perday[1].append('CHOOSE-9th-level')
    npc.defer(lambda npc: arcanumcasting(npc) )
```

## Eldritch Master
*20th-level warlock feature*

You can draw on your inner reserve of mystical power while entreating your patron to regain expended spell slots. You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature. Once you regain spell slots with this feature, you must finish a long rest before you can do so again.

```
def level20(npc):
    npc.traits.append("***Eldritch Master (Recharges on long rest).*** You can spend 1 minute entreating your patron for aid to regain all your expended spell slots from your Pact Magic feature.")
```

```
# Warlock subclasses use invocations
dependentmodules = ['Invocations.md']
```

---

# Warlock Spells

## Cantrips
* [balance](../../Magic/Spells/balance.md)
* [blade ward](../../Magic/Spells/blade-ward.md)
* [blood boil](../../Magic/Spells/blood-boil.md)
* [blood dagger](../../Magic/Spells/blood-dagger.md)
* [blood siphon](../../Magic/Spells/blood-siphon.md)
* [bloodlink](../../Magic/Spells/bloodlink.md)
* [bolster](../../Magic/Spells/bolster.md)
* [booming blade](../../Magic/Spells/booming-blade.md)
* [chill touch](../../Magic/Spells/chill-touch.md)
* [corruption](../../Magic/Spells/corruption.md)
* [create bonfire](../../Magic/Spells/create-bonfire.md)
* [eidolic chains](../../Magic/Spells/eidolic-chains.md)
* [eldritch blast](../../Magic/Spells/eldritch-blast.md)
* [friends](../../Magic/Spells/friends.md)
* [frostbite](../../Magic/Spells/frostbite.md)
* [gore spike](../../Magic/Spells/gore-spike.md)
* [green flame blade](../../Magic/Spells/green-flame-blade.md)
* [hemokinesis](../../Magic/Spells/hemokinesis.md)
* [infestation](../../Magic/Spells/infestation.md)
* [lightning lure](../../Magic/Spells/lightning-lure.md)
* [mage hand](../../Magic/Spells/mage-hand.md)
* [mind sliver](../../Magic/Spells/mind-sliver.md)
* [magic stone](../../Magic/Spells/magic-stone.md)
* [minor illusion](../../Magic/Spells/minor-illusion.md)
* [poison spray](../../Magic/Spells/poison-spray.md)
* [prestidigitation](../../Magic/Spells/prestidigitation.md)
* [sword burst](../../Magic/Spells/sword-burst.md)
* [thunderclap](../../Magic/Spells/thunderclap.md)
* [toll the dead](../../Magic/Spells/toll-the-dead.md)
* [true strike](../../Magic/Spells/true-strike.md)

## 1st Level
* [armor of agathys](../../Magic/Spells/armor-of-agathys.md)
* [arms of hadar](../../Magic/Spells/arms-of-hadar.md)
* [blackout](../../Magic/Spells/blackout.md)
* [blood reading](../../Magic/Spells/blood-reading.md)
* [cause fear](../../Magic/Spells/cause-fear.md)
* [charm person](../../Magic/Spells/charm-person.md)
* [comprehend languages](../../Magic/Spells/comprehend-languages.md)
* [delude](../../Magic/Spells/delude.md)
* [expeditious retreat](../../Magic/Spells/expeditious-retreat.md)
* [healing elixir](../../Magic/Spells/healing-elixir.md)
* [hellish rebuke](../../Magic/Spells/hellish-rebuke.md)
* [hex](../../Magic/Spells/hex.md)
* [id insinuation](../../Magic/Spells/id-insinuation) (UA.md)
* [illusory script](../../Magic/Spells/illusory-script.md)
* [protection from evil and good](../../Magic/Spells/protection-from-evil-and-good.md)
* [puppet](../../Magic/Spells/puppet.md)
* [sense emotion](../../Magic/Spells/sense-emotion.md)
* [unseen servant](../../Magic/Spells/unseen-servant.md)
* [thunderwave](../../Magic/Spells/thunderwave.md)
* [witch bolt](../../Magic/Spells/witch-bolt.md)

## 2nd Level
* [Beluud's brutal jaunt](../../Magic/Spells/beluuds-brutal-jaunt.md)
* [carnage blast](../../Magic/Spells/carnage-blast.md)
* [cloud of daggers](../../Magic/Spells/cloud-of-daggers.md)
* [crown of madness](../../Magic/Spells/crown-of-madness.md)
* [darkness](../../Magic/Spells/darkness.md)
* [earthbind](../../Magic/Spells/earthbind.md)
* [enthrall](../../Magic/Spells/enthrall.md)
* [flock of familiars](../../Magic/Spells/flock-of-familiars.md)
* [hold person](../../Magic/Spells/hold-person.md)
* [invisibility](../../Magic/Spells/invisibility.md)
* [knock](../../Magic/Spells/knock.md)
* [mental barrier](../../Magic/Spells/mental-barrier.md)
* [mind thrust](../../Magic/Spells/mind-thrust.md)
* [mirror image](../../Magic/Spells/mirror-image.md)
* [misty step](../../Magic/Spells/misty-step.md)
* [ray of enfeeblement](../../Magic/Spells/ray-of-enfeeblement.md)
* [shatter](../../Magic/Spells/shatter.md)
* [spider climb](../../Magic/Spells/spider-climb.md)
* [suggestion](../../Magic/Spells/suggestion.md)
* [thought shield](../../Magic/Spells/thought-shield.md)

## 3rd Level
* [animate dead](../../Magic/Spells/animate-dead.md)
* [blood extraction](../../Magic/Spells/blood-extraction.md)
* [counterspell](../../Magic/Spells/counterspell.md)
* [dispel magic](../../Magic/Spells/dispel-magic.md)
* [enemies abound](../../Magic/Spells/enemies-abound.md)
* [fear](../../Magic/Spells/fear.md)
* [fly](../../Magic/Spells/fly.md)
* [gaseous form](../../Magic/Spells/gaseous-form.md)
* [hunger of hadar](../../Magic/Spells/hunger-of-hadar.md)
* [hypnotic pattern](../../Magic/Spells/hypnotic-pattern.md)
* [incite self-harm](../../Magic/Spells/incite-self-harm.md)
* [life transference](../../Magic/Spells/life-transference.md)
* [magic circle](../../Magic/Spells/magic-circle.md)
* [major image](../../Magic/Spells/major-image.md)
* [psionic blast](../../Magic/Spells/psionic-blast.md)
* [ray of fatigue](../../Magic/Spells/ray-of-fatigue.md)
* [remove curse](../../Magic/Spells/remove-curse.md)
* [spirit shroud](../../Magic/Spells/spirit-shroud.md)
* [summon fey](../../Magic/Spells/summon-fey.md)
* [summon shadow](../../Magic/Spells/summon-shadow.md)
* [summon undead](../../Magic/Spells/summon-undead.md)
* [tongues](../../Magic/Spells/tongues.md)
* [vampiric touch](../../Magic/Spells/vampiric-touch.md)
* [veiled blade](../../Magic/Spells/veiled-blade.md)

## 4th Level
* Banishment
* Blight
* [charm monster](../../Magic/Spells/charm-monster.md)
* Dimension Door
* Ego Whip (UA)
* [elemental bane](../../Magic/Spells/elemental-bane.md)
* Galder's Speedy Courier
* Hallucinatory Terrain
* [hemorrhage](../../Magic/Spells/hemorrhage.md)
* [jinx](../../Magic/Spells/jinx.md)
* [strangulate](../../Magic/Spells/strangulate.md)
* Summon Abberant Spirit (UA)
* [wind funnel](../../Magic/Spells/wind-funnel.md)

## 5th Level
* [chilling darkness](../../Magic/Spells/chilling-darkness.md)
* Contact Other Plane
* Dream
* Intellect Fortress (UA)
* Hold Monster
* mislead
* modify memory
* [phantasmal plunge](../../Magic/Spells/phantasmal-plunge.md)
* planar binding
* Scrying
* [soar](../../Magic/Spells/soar.md)
* teleportation circle

## 6th Level
* Arcane Gate
* Circle of Death
* Conjure Fey
* Create Undead
* Eyebite
* Flesh to Stone
* [globe of winter](../../Magic/Spells/globe-of-winter.md)
* Investiture of Flame
* Investiture of Ice
* Investiture of Stone
* Investiture of Wind
* magic jar
* Mass Suggestion
* [possess object](../../Magic/Spells/possess-object.md)
* Psychic Crush (UA)
* [soul blade](../../Magic/Spells/soul-blade.md)
* Summon Fiendish Spirit (UA)
* True Seeing

## 7th Level
* [crown of stars](../../Magic/Spells/crown-of-stars.md)
* [death's door](../../Magic/Spells/deaths-door.md)
* [dire jinx](../../Magic/Spells/dire-jinx.md)
* Etherealness
* Finger of Death
* Forcecage
* [living burial](../../Magic/Spells/living-burial.md)
* Plane Shift
* project image

## 8th Level
* Abi-Dalzim's horrid wilting
* Demiplane
* Dominate Monster
* [encasing ice](../../Magic/Spells/encasing-ice.md)
* Feeblemind
* Glibness
* Power Word: Stun
* [vertigo](../../Magic/Spells/vertigo.md)

## 9th Level
* [amnesia](../../Magic/Spells/amnesia.md)
* Astral Projection
* [blood to flame](../../Magic/Spells/blood-to-flame.md)
* Foresight
* [frailty](../../Magic/Spells/frailty.md)
* gate
* Imprisonment
* [omnisight](../../Magic/Spells/omnisight.md)
* Power Word: Kill
* [raise abomination](../../Magic/Spells/raise-abomination.md)
* shapechange
* True Polymorph
* weird
