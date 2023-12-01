# Otherworldly Patron: The Undead
The Undead is an entity that resides in the dark corners of the multiverse. Your patron some other ancient undead being, many times spoken of only in hushed whispers (and even then behind powerful anti-scrying magic, lest the name draw the attention of the being). You may seek to gain knowledge from your patron's countless lifetimes of experience, while it may see you as a piece of a centuries long plan.

One such name whispered quietly is that of the ancient lich [Kali Kaal](../../People/KaliKaal.md).

```
name = 'Undead'
description = "***Otherworldly Patron: The Undead.*** The Undead is an entity that resides in the dark corners of the multiverse. Your patron some other ancient undead being, many times spoken of only in hushed whispers (and even then behind powerful anti-scrying magic, lest the name draw the attention of the being). You may seek to gain knowledge from your patron's countless lifetimes of experience, while it may see you as a piece of a centuries long plan."
```

## Expanded Spell List
*1st-level Undead feature*

The Undead lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.

**Undead Expanded Spells**

Spell Level|Spells
-----------|------
1st | [bane](../../Magic/Spells/bane.md), [false life](../../Magic/Spells/false-life.md)
2nd | [blindness/deafness](../../Magic/Spells/blindness-deafness.md), [phantasmal force](../../Magic/Spells/phantasmal-force.md)
3rd | [speak with dead](../../Magic/Spells/speak-with-dead.md), [phantom steed](../../Magic/Spells/phantom-steed.md)
4th | [death ward](../../Magic/Spells/death-ward.md), [greater invisibility](../../Magic/Spells/greater-invisibility.md)
5th | [antilife shell](../../Magic/Spells/antilife-shell.md), [cloudkill](../../Magic/Spells/cloudkill.md)

```
def level1(npc):
    npc.traits.append(f"***Expanded Spell List.*** The following spells are added to the warlock spell list for you: 1st: {spelllinkify('bane')}, {spelllinkify('false life')}; 2nd: {spelllinkify('blindness-deafness')}, {spelllinkify('phantasmal force')}; 3rd: {spelllinkify('speak with dead')}, {spelllinkify('phantom steed')}; 4th: {spelllinkify('death ward')}, {spelllinkify('greater invisibility')}; 5th: {spelllinkify('antilife shell')}, {spelllinkify('cloudkill')}")
```

## Form of Dread
*1st-level Undead feature*

You manifest an aspect of your patron's dreadful power. As a bonus action, you transform for 1 minute. You gain the following benefits while transformed:

* You gain temporary hit points equal to 1d10 + your warlock level.

* Once during each of your turns, when you hit a creature with an attack, you can force it to make a Wisdom saving throw, and if the saving throw fails, the target is frightened of you until the end of your next turn.

* You are immune to the frightened condition.

You can transform a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

The appearance of your Form of Dread reflects some aspect of your patron. For example, your form could be a shroud of shadows forming the crown and robes of your lich patron, or your face might transform into bat-like features due to your vampire patron.

```
    npc.defer(lambda npc: npc.bonusactions.append(f"***Form of Dread ({npc.proficiencybonus()}/Recharges on long rest).*** You transform into an aspect of your patron's power. You gain the following benefits while transformed: You gain 1d10 + {npc.levels('Warlock')} temporary hit points; Once during each of your turns, when you hit a creature with an attack, you can force it to make a Wisdom saving throw (DC {npc.pactmagic.spellsavedc}), and if the saving throw fails, the target is frightened of you until the end of your next turn; You are immune to the frightened condition{' and necrotic damage' if npc.levels('Warlock') >= 10 else ''}.") )
```

## Grave Touched
*6th-level Undead feature*

Your patron's powers have a profound effect on your body and magic. You don't need to eat, drink, or breathe.

In addition, when you hit a creature with an attack and roll damage against the creature, you can replace the damage type with necrotic damage. While you are using your Form of Dread, you can roll one additional damage die when determining the necrotic damage the target takes. 

```
def level6(npc):
    npc.traits.append("***Grave Touched.*** You don't need to eat, drink, or breathe.")
    npc.actions.append("***Grave Touched.*** When you hit a creature with an attack and roll damage against the creature, you can replace the damage type with necrotic damage. While you are using your Form of Dread, you can roll one additional damage die when determining the necrotic damage the target takes.")
```

## Mortal Husk
*10th-level Undead feature*

Your connection to undeath and necrotic energy now saturates your body. You have resistance to necrotic damage. If you are transformed using your Form of Dread, you instead become immune to necrotic damage.

In addition, when you are reduced to 0 hit points, you can cause your body to explode. Each creature within 30 feet of you takes necrotic damage equal to 2d10 + your warlock level. You then revive with 1 hit point in your previous space, along with your gear, and you gain 1 level of exhaustion. Once you revive this way, you can't do so again until you finish 1d4 long rests.

```
def level10(npc):
    npc.damageresistances.append("necrotic")
    npc.defer(lambda npc: npc.traits.append("***Mortal Husk (Recharges on 1d4 long rests).*** When you are reduced to 0 hit points, you can cause your body to explode. Each creature within 30 feet of you takes necrotic damage equal to 2d10 + {npc.levels('Warlock')}. You then revive with 1 hit point in your previous space, along with your gear, and you gain 1 level of exhaustion.") )
```

## Spirit Projection
*14th-level Undead feature*

Your body is now simply a vessel for your spirit.

As an action, you can project your spirit from your body. The body you leave behind is unconscious and in a state of suspended animation.

Your spirit can remain outside your body for up to 1 hour or until your concentration is broken (as if concentrating on a spell). When your projection ends, your spirit returns to your body or your body magically teleports to your spirit's space (your choice).

While projecting your spirit, you gain the following benefits:

* Your spirit and body gain resistance to bludgeoning, piercing, and slashing damage.
* When you cast a spell of the conjuration or necromancy school, the spell doesn't require verbal, somatic, or material components that lack a gold cost.
* You have a flying speed equal to your walking speed and can hover. You can move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object.
* While you are using your Form of Dread, once during each of your turns when you deal necrotic damage to a creature, you regain hit points equal to half the amount of necrotic damage dealt.

Once you use this feature, you can't do so again until you finish a long rest.

```
def level14(npc):
    npc.traits.append("***Spirit Projection.*** Your body is now simply a vessel for your spirit.")
    npc.actions.append("***Spirit Projection (Recharges on long rest).*** You project your spirit from your body. The body you leave behind is unconscious and in a state of suspended animation. Your spirit can remain outside your body for up to 1 hour or until your concentration is broken (as if concentrating on a spell). When your projection ends, your spirit returns to your body or your body magically teleports to your spirit's space (your choice). While projecting your spirit, you gain the following benefits: Your spirit and body gain resistance to bludgeoning, piercing, and slashing damage; When you cast a spell of the conjuration or necromancy school, the spell doesn't require verbal, somatic, or material components that lack a gold cost; You have a flying speed equal to your walking speed and can hover, and you can move through creatures and objects as if they were difficult terrain, but you take 1d10 force damage if you end your turn inside a creature or an object; While you are using your Form of Dread, once during each of your turns when you deal necrotic damage to a creature, you regain hit points equal to half the amount of necrotic damage dealt.")
```
