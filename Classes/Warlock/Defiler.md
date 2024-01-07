# Otherworldly Patron: The Defiler
You have made a pact with a magical entity that defiles and corrupts. Your patron is a source of foul blight and toxicity, such as a hag coven, a powerful elder ooze, a yuan-ti archpriest, an archfiend of corruption, a noxious disease-spreading undead, or even a poisonous spirit of nature, such as a mysterious three-headed snake, That Which Rots, or the crocodilian Dragon of the Swamp.

Defilers have clear motivations, yet their methods for reaching their goals are often circuitous and inscrutable to their followers. Defilers are not always eviL but they universally desire to spread their form of corruption, blight, disease, or poison to the world Some see this as a gift, while others knowingly strive to cause torment.

## Expanded Spell List
The Defiler lets you choose from an expanded list of spells when you learn a warlock spell The following spells are added to the warlock spell list for you.

Spell Level | Spells
----------- | -------------
1st | [ray of sickness](../../Magic/Spells/ray-of-sickness.md), [Tasha's caustic brew](../../Magic/Spells/tashas-caustic-brew.md)
2nd | [blindness/deafness](../../Magic/Spells/blindness-deafness.md), [Melf's acid arrow](../../Magic/Spells/melfs-acid-arrow.md)
3rd | [stinking cloud](../../Magic/Spells/stinking-cloud.md), [toxic breath](../../Magic/Spells/toxic-breath.md)
4th | [venom lash](../../Magic/Spells/venom-lash.md), [vitriolic sphere](../../Magic/Spells/vitriolic-sphere.md)
5th | [cloudkill](../../Magic/Spells/cloudkill.md), [noxious geyser](../../Magic/Spells/noxious-geyser.md)

## Withering Affliction
*1st-level Defiler feature*

Your patron grants you the ability to inflict painful maladies. Choose one of [acid splash](../../Magic/Spells/acid-splash.md), [chill touch](../../Magic/Spells/chill-touch.md), or [poison spray](../../Magic/Spells/poison-spray.md). You learn the chosen cantrip as a warlock spell, and it doesn't count against the number of cantrips you can learn as a warlock.

In addition, when you deal acid, necrotic, or poison damage to a creature using a weapon attack or a warlock spell, you can choose to afflict the creature with magical corruption. The target must succeed on a Constitution saving throw against your warlock spell save DC or else become poisoned for 1 minute. While it is poisoned, the target repeats the saving throw at the end of each of its turns, ending the effect on a success, and taking poison damage equal to your proficiency bonus on a failure.

You can only use this feature to poison a creature two times, and you regain all expended uses when you finish a long rest. The number of uses per long rest increases to 3 at 5th leveL 4 at 11th leveL and 5 at 17th level.

```
def level1(npc):
    malady = choose("Choose one: ", ['acid splash', 'chill touch', 'poison spray'])
    npc.spellcasting['Warlock'].cantripsknown.append(malady)

    npc.defer(lambda npc: npc.traits.append(f"***Withering Affliction ({2 if npc.levels('Warlock') < 5 else 3 if npc.levels('Warlock') < 11 else 4 if npc.levels('Warlock') < 17 else 5}/Recharges on long rest).*** In addition, when you deal acid, necrotic, or poison damage to a creature using a weapon attack or a warlock spell, you can choose to afflict the creature with magical corruption. The target must succeed on a Constitution saving throw against your warlock spell save DC or else become poisoned for 1 minute. While it is poisoned, the target repeats the saving throw at the end of each of its turns, ending the effect on a success, and taking {npc.proficiencybonus()} poison damage on a failure.") )
```

## Agent of Corruption
*6th-level Defiler feature*

You become attuned to the essence of corruption itself. You gain resistance to acid damage and poison damage, and you have advantage on saving throws made against poison or disease.

In addition, once per turn, when one of your weapon attacks or warlock spells deals acid, necrotic, or poison damage to a creature that is already poisoned, you can increase the damage that creature takes by an amount equal to your Charisma modifier (minimum +1).

```
def level6(npc):
    npc.damageresistances.append('acid')
    npc.damageresistances.append('poison')
    npc.traits.append("***Agent of Corruption.*** You have advantage on saving throws made against poison or disease.")
    npc.traits.append("***Corrupting Influence (1/turn).*** When one of your weapon attacks or warlock spells deals acid, necrotic, or poison damage to a creature that is already poisoned, you can increase the damage that creature takes by an amount equal to your Charisma modifier (minimum +1).")
```

## Sickening Ward
*10th-level Defiler feature*

Your patron gifts you with a shield of toxic mist to sicken your attackers. When a creature within 15 feet of you hits you with an attack, you can use your reaction to shroud the attacker in poisonous mist. The attacker rerolls the attack roll and uses the new result. After the attack, it must also succeed on a Constitution saving throw against your warlock spell save DC or else it is poisoned until the end of its next turn.

Once you use this feature, you cannot use it again until you finish a short or long rest.

```
def level10(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Sickening Ward (Recharges on short or long rest).*** When a creature within 15 feet of you hits you with an attack, you shroud the attacker in poisonous mist. The attacker rerolls the attack roll and uses the new result. After the attack, it must also succeed on a Constitution saving throw (DC {npc.spellcasting['Warlock'].spellsavedc()}) against your warlock spell save DC or else it is poisoned until the end of its next turn.") )
```

## Tormenting Toxins
*14th-level Defiler feature*

You learn how to strengthen the ailments ravaging your foes. When a creature you can see within 30 feet of you makes a saving throw against one of your warlock spells that deals acid, necrotic, or poison damage or causes a creature to gain exhaustion or be blinded, deafened, poisoned, or diseased, if you cast the spell on a previous tum, you can use your reaction to roll ld8 and subtract the result from the creature's saving throw.

Also, your warlock spells and class features ignore immunity to the poisoned condition and treat immunity to poison damage as only resistance to poison damage. Any creature that otherwise can't be poisoned still has advantage on saving throws against being poisoned by your warlock spells and class features.

```
def level14(npc):
    npc.reactions.append("***Tormenting Toxins.*** When a creature you can see within 30 feet of you makes a saving throw against one of your warlock spells that deals acid, necrotic, or poison damage or causes a creature to gain exhaustion or be blinded, deafened, poisoned, or diseased, if you cast the spell on a previous tum, you roll 1d8 and subtract the result from the creature's saving throw.")

    npc.traits.append("***Tormenting Toxins.*** your warlock spells and class features ignore immunity to the poisoned condition and treat immunity to poison damage as only resistance to poison damage. Any creature that otherwise can't be poisoned still has advantage on saving throws against being poisoned by your warlock spells and class features.")
```
