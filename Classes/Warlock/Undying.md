# Otherworldly Patron: The Undying
Death holds no sway over your patron, who has unlocked the secrets of everlasting life, although such a prize – like all power – comes at a price. Once mortal, the Undying has seen mortal lifetimes pass like the seasons, like the flicker of endless days and nights. It has the secrets of the ages to share, secrets of life and death. What makes the Undying different from the Undead patron is inherent in the names: while the Undead patron is a powerful undead, the Undying is not--just a mortal that has, somehow found a way to become (to mortal eyes at least) immortal.

In Azgaarnoth, Undying patrons include Lochlar the Shadow King, master of the legendary Warlock's Crypt, and it is whispered that some warlocks have even created a Pact with the [Dread Emperor](../../People/DreadEmperor.md), though this has never been proven and could be rumors spread by the Dread Emperor to enhance the fear and mystery to his name.

## Expanded Spell List
The Undying lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.

**Undying Expanded Spells**
Spell Level|Spells
-----------|------
1st | [false life](../../Magic/Spells/false-life.md), [ray of sickness](../../Magic/Spells/ray-of-sickness.md)
2nd | [blindness/deafness](../../Magic/Spells/blindness-deafness.md), [silence](../../Magic/Spells/silence.md)
3rd | [feign death](../../Magic/Spells/feign-death.md), [speak with dead](../../Magic/Spells/speak-with-dead.md)
4th | [aura of life](../../Magic/Spells/aura-of-life.md), [death ward](../../Magic/Spells/death-ward.md)
5th | [contagion](../../Magic/Spells/contagion.md), [legend lore](../../Magic/Spells/legend-lore.md)

```
def level1(npc):
    npc.traits.append(f"***Expanded Spell List.*** The following spells are added to the warlock spell list for you: 1st: {spelllinkify('false life')}, {spelllinkify('ray of sickness')}; 2nd: {spelllinkify('blindness-deafness')}, {spelllinkify('silence')}; 3rd: {spelllinkify('feign death')}, {spelllinkify('speak with dead')}; 4th: {spelllinkify('aura of life')}, {spelllinkify('death ward')}; 5th: {spelllinkify('contagion')}, {spelllinkify('legend lore')}")
```

## Among the Dead
*1st-level Undying patron feature*

You learn the Spare the Dying cantrip, which counts as a warlock cantrip for you. You also have advantage on saving throws against any disease.

Additionally, undead have difficulty harming you. If an undead targets you directly with an attack or a harmful spell, that creature must make a Wisdom saving throw against your spell save DC (an undead needn't make the save when it includes you in an area effect, such as the explosion of Fireball). On a failed save, the creature must choose a new target or forfeit targeting someone instead of you, potentially wasting the attack or spell. On a successful save, the creature is immune to this effect for 24 hours. An undead is also immune to this effect for 24 hours if you target it with an attack or a harmful spell.

```
def level1(npc):
    npc.pactmagic.cantripsknown.append('spare the dying')
    npc.traits.append("***Among the Dead.*** You have advantage on saving throws against any disease. Additionally, undead have difficulty harming you. If an undead targets you directly with an attack or a harmful spell, that creature must make a Wisdom saving throw against your spell save DC (an undead needn't make the save when it includes you in an area effect, such as the explosion of Fireball). On a failed save, the creature must choose a new target or forfeit targeting someone instead of you, potentially wasting the attack or spell. On a successful save, the creature is immune to this effect for 24 hours. An undead is also immune to this effect for 24 hours if you target it with an attack or a harmful spell.")
```

## Defy Death
*6th-level Undying patron feature*

You can give yourself vitality when you cheat death or when you help someone else cheat it. You can regain hit points equal to 1d8 + your Constitution modifier (minimum of 1 hit point) when you succeed on a death saving throw or when you stabilize a creature with Spare the Dying.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append("***Defy Death (Recharges on long rest). You can regain 1d8 + {npc.CONbonus()} hit points when you succeed on a death saving throw or when you stabilize a creature with {spelllinkify('spare the dying')}.") )
```

## Undying Nature
*10th-level Undying patron feature*

You can hold your breath indefinitely, and you don't require food, water, or sleep, although you still require rest to reduce exhaustion and still benefit from finishing short and long rests.

In addition, you age at a slower rate. For every 10 years that pass, your body ages only 1 year, and you are immune to being magically aged.

```
def level10(npc):
    npc.traits.append("***Undying Nature.*** You can hold your breath indefinitely, and you don't require food, water, or sleep, although you still require rest to reduce exhaustion and still benefit from finishing short and long rests. In addition, you age at a slower rate. For every 10 years that pass, your body ages only 1 year, and you are immune to being magically aged.")
```

## Indestructible Life
*14th-level Undying patron feature*

You partake of some of the true secrets of the Undying. On your turn, you can use a bonus action to regain hit points equal to 1d8 + your warlock level. Additionally, if you put a severed body part of yours back in place when you use this feature, the part reattaches.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level14(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Indestructible Life (Recharges on short or long rest).*** You regain 1d8 + {npc.levels('Warlock')} hit points. Additionally, if you put a severed body part of yours back in place when you use this feature, the part reattaches.") )
```
