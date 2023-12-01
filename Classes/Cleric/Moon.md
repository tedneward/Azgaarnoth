# Divine Domain: Moon
Clerics of the Moon Domain draw on their divine connection to the moons to wield light and shadow, invoke good fortune and ill favor, and reveal or conceal as they see fit. Most Moon clerics worship the Moonweaver herself, but her followers are as varied as the stars in the sky. Some seek to protect the vulnerable and do good in the world, while others meddle with impunity and distort truth for selfish gain. Other Moon clerics worship not the gods but the moons themselves, especially those with an innate connection to the lunar cycles through lycanthropy.

This domain is available to the followers of [Trinitarians who worship Dara](../../Religions/Trinitarian.md#dara), [Larethian](../../Religions/Pantheon/Larethian.md), ...

```
name = 'Moon'
description = "***Divine Domain: Moon.*** Clerics of the Moon Domain draw on their divine connection to the moons to wield light and shadow, invoke good fortune and ill favor, and reveal or conceal as they see fit. Most Moon clerics worship the Moonweaver herself, but her followers are as varied as the stars in the sky. Some seek to protect the vulnerable and do good in the world, while others meddle with impunity and distort truth for selfish gain. Other Moon clerics worship not the gods but the moons themselves, especially those with an innate connection to the lunar cycles through lycanthropy."
```

### Domain Spells
*1st-level Moon Domain feature*

You gain domain spells at the cleric levels listed in the Moon Domain Spells table. See the Divine Domain class feature for how domain spells work.

**Moon Domain Spells**
Cleric Level | Spells
------------ | -------
1st | [faerie fire](../../Magic/Spells/faerie-fire.md), [silent image](../../Magic/Spells/silent-image.md)
3rd | [moonbeam](../../Magic/Spells/moonbeam.md), [invisibility](../../Magic/Spells/invisibility.md)
5th | [hypnotic pattern](../../Magic/Spells/hypnotic-pattern.md), [major image](../../Magic/Spells/major-image.md)
7th | [greater invisibility](../../Magic/Spells/greater-invisibility.md), [hallucinatory terrain](../../Magic/Spells/hallucinatory-terrain.md)
9th | [dream](../../Magic/Spells/dream.md), [passwall](../../Magic/Spells/passwall.md)

```
domainspells = {
    1: ['faerie fire', 'silent image'],
    3: ['moonbeam', 'invisibility'],
    5: ['hypnotic pattern', 'major image'],
    7: ['greater invisibility', 'hallucinatory terrain'],
    9: ['dream', 'passwall']
}

def level1(npc):
    def domainspellsforlevel(npc):
        results = []
        if npc.levels(spellcasting.casterclass) >= 1: results += domainspells[1]
        if npc.levels(spellcasting.casterclass) >= 3: results += domainspells[3]
        if npc.levels(spellcasting.casterclass) >= 5: results += domainspells[5]
        if npc.levels(spellcasting.casterclass) >= 7: results += domainspells[7]
        if npc.levels(spellcasting.casterclass) >= 9: results += domainspells[9]
        spellcasting.spellsalwaysprepared += results

    npc.defer(lambda npc: domainspellsforlevel(npc))
```

### Clarity of Catha
*1st-level Moon Domain feature*

You learn to shine light upon the mind's most dire moments, shielding those you protect. When a creature within 30 feet of you that use can see makes a Wisdom Saving Throw, you can use your reaction to grant that creature advantage on the save.

You can use the feature equal to your proficiency bonus, regaining all expended used when you finish a long rest.

```
    npc.defer(lambda npc: npc.reactions.append(f"***Clarity of Catha ({npc.proficiencybonus()}/Recharges on long rest).*** When a creature within 30 feet of you that use can see makes a Wisdom Saving Throw, you grant that creature advantage on the save.") )
```

### Channel Divinity: Blessing of the Full Moon
*2nd-level Moon Domain feature*

***Blessing of the Watchful Moon.*** For 1 hour, the blessed creature's speed is increased by 10 feet, and it has advantage on Wisdom (Perception or Survival) checks involving smell or made to track a creature.

***Blessing of the Blood-Drenched Moon.*** For 10 minutes, the blessed creature has advantage on attack rolls against a target if at least one of the blessed creature's allies is within 5 feet of the target and the ally isn't incapacitated. 

```
def level2(npc):
    npc.actions.append("***Channel Divinity: Blessing of the Watchful Moon.*** For 1 hour, the blessed creature's speed is increased by 10 feet, and it has advantage on Wisdom (Perception or Survival) checks involving smell or made to track a creature.")
    npc.actions.append("***Channel Divinity: Blessing of the Blood-Drenched Moon.*** For 10 minutes, the blessed creature has advantage on attack rolls against a target if at least one of the blessed creature's allies is within 5 feet of the target and the ally isn't incapacitated.")
```

### Channel Divinity: Mind of Two Moons
*6th-level Moon Domain feature*

You can use your Channel Divinity to invoke the twofold arcana of Exandria's moons. By expending one use of Channel Divinity, you can cast a second concentration spell while already concentrating on a first spell, as long as both spells are on your list of Moon Domain spells. If you need to make a Constitution saving throw to maintain your concentration on both spells, you make the save with disadvantage. On a failure, you lose concentration on both spells.

```
def level6(npc):
    npc.actions.append("***Channel Divinity: Mind of Two Moons.*** You can cast a second concentration spell while already concentrating on a first spell, as long as both spells are on your list of Moon Domain spells. If you need to make a Constitution saving throw to maintain your concentration on both spells, you make the save with disadvantage. On a failure, you lose concentration on both spells.")
```

### Empowered Cantrips
*8th-level Moon Domain feature*

Your cleric cantrips deal extra damage equal to your Wisdom modifier (minimum of 1).

```
def level8(npc):
    npc.defer(lambda npc: npc.traits.append("***Empowered Cantrips.*** Your cleric cantrips deal {npc.WISbonus()} extra damage.") )
```

### Eclipse of Ill Omen
*17th-level Moon Domain feature*

You can call upon the vermillion moon Ruidus to flare in the sky above you, eclipsing all other light. Its power surrounds you even where the sky can't be seen, and even on other planes. As a bonus action, you can manifest an area of reddish dim light in a 60-foot radius around you. In addition to the normal effects of dim light, creatures in the area make saving throws with disadvantage. When you create this eclipse, you can choose any number of creatures that are unaffected by it.

This eclipse lasts while you concentrate (as if concentrating on a spell) for up to 1 minute. Concentrating on this feature counts as concentrating on a Moon Domain spell for the purpose of your Mind of Two Moons feature.

Additionally, once per turn when you deal radiant damage to any creatures in this area of dim light, you can curse one of those creatures until the eclipse ends (no action required). A creature cursed in this way has its speed halved and can't regain hit points. 

Once you use this feature, you can't use it again until you finish a long rest.

```
def level17(npc):
    npc.bonusactions.append("***Eclipse of Ill Omen (Recharges on long rest).*** You can manifest an area of reddish dim light in a 60-foot radius around you. In addition to the normal effects of dim light, creatures in the area make saving throws with disadvantage. When you create this eclipse, you can choose any number of creatures that are unaffected by it. This eclipse lasts while you concentrate (as if concentrating on a spell) for up to 1 minute. Concentrating on this feature counts as concentrating on a Moon Domain spell for the purpose of your Mind of Two Moons feature. Additionally, once per turn when you deal radiant damage to any creatures in this area of dim light, you can curse one of those creatures until the eclipse ends (no action required). A creature cursed in this way has its speed halved and can't regain hit points.")
```
