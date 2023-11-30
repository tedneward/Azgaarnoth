# Otherworldly Patron: Great Old One
Your patron is a mysterious entity whose nature is utterly foreign to the fabric of reality. It might come from the Far Realm, the space beyond reality, or it could be one of the elder gods known only in legends. Its motives are incomprehensible to mortals, and its knowledge so immense and ancient that even the greatest libraries pale in comparison to the vast secrets it holds. The Great Old One might be unaware of your existence or entirely indifferent to you, but the secrets you have learned allow you to draw your magic from it.

Entities of this type include Ghaunadar, called That Which Lurks; Tharizdun, the Chained God; Dendar, the Night Serpent; Zargon, the Returner; and other unfathomable beings.

## Expanded Spell List
The Great Old One lets you choose from an expanded list of spells when you learn a warlock spell. The following spells are added to the warlock spell list for you.

**Great Old One Expanded Spells**
Spell Level|Spells
-----------|------
1st | [dissonant whispers](../../Magic/Spells/dissonant-whispers.md), [Tasha's hideous laughter](../../Magic/Spells/tashas-hideous-laughter.md)
2nd | [detect thoughts](../../Magic/Spells/detect-thoughts.md), [phantasmal force](../../Magic/Spells/phantasmal-force.md)
3rd | [clairvoyance](../../Magic/Spells/clairvoyance.md), [sending](../../Magic/Spells/sending.md)
4th | [dominate beast](../../Magic/Spells/dominate-beast.md), [Evard's black tentacles](../../Magic/Spells/evards-black-tentacles.md)
5th | [dominate person](../../Magic/Spells/dominate-person.md), [telekinesis](../../Magic/Spells/telekinesis.md)

## Awakened Mind
*1st-level Great Old One feature*

Your alien knowledge gives you the ability to touch the minds of other creatures. You can communicate telepathically with any creature you can see within 30 feet of you. You don't need to share a language with the creature for it to understand your telepathic utterances, but the creature must be able to understand at least one language.

```
def level1(npc):
    npc.languages.append("Telepathy (30 ft)")

    npc.traits.append("***Expanded Spell List.*** The following are considered warlock spells for you: 1st: {spelllinkify('dissonant whispers')}, {spelllinkify('tashas hideous laughter')}; 2nd: {spelllinkify('detect thoughts')}, {spelllinkify('phantasmal force')}; 3rd: {spelllinkify('clairvoyance')}, {spelllinkify('sending')}, 4th: {spelllinkify('dominate beast')}, {spelllinkify('evards black tentacles')}; 5th: {spelllinkify('dominate person')}, {spelllinkify('telekinesis')}.") 
```

## Entropic Ward
*6th-level Great Old One feature*

You learn to magically ward yourself against attack and to turn an enemy's failed strike into good luck for yourself. When a creature makes an attack roll against you, you can use your reaction to impose disadvantage on that roll. If the attack misses you, your next attack roll against the creature has advantage if you make it before the end of your next turn.

Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level6(npc):
    npc.reactions.append("***Entropic Ward (Recharges on short or long rest).*** When a creature makes an attack roll against you, you can use your reaction to impose disadvantage on that roll. If the attack misses you, your next attack roll against the creature has advantage if you make it before the end of your next turn.")
```

## Thought Shield
*10th-level Great Old One feature*

Your thoughts can't be read by telepathy or other means unless you allow it. You also have resistance to psychic damage, and whenever a creature deals psychic damage to you, that creature takes the same amount of damage that you do.

```
def level10(npc):
    npc.damageresistances.append("psychic")
    npc.traits.append("***Thought Shield.*** Your thoughts can't be read by telepathy or other means unless you allow it. Whenever a creature deals psychic damage to you, that creature takes the same amount of damage that you do.")
```

## Create Thrall
*14th-level Great Old One feature*

You gain the ability to infect a humanoid's mind with the alien magic of your patron. You can use your action to touch an incapacitated humanoid. That creature is then charmed by you until a Remove Curse spell is cast on it, the charmed condition is removed from it, or you use this feature again.

You can communicate telepathically with the charmed creature as long as the two of you are on the same plane of existence.

```
def level14(npc):
    npc.actions.append(f"***Create Thrall.*** You touch an incapacitated humanoid. That creature is then charmed by you until a {spelllinkify('remove curse')} spell is cast on it, the charmed condition is removed from it, or you use this feature again. You can communicate telepathically with the charmed creature as long as the two of you are on the same plane of existence.")
```
