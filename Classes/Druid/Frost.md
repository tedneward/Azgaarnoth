# Druidic Circle: Circle of Frost
Druids within the Circle of Frost understand that winter is not just a period of time during the season--it is the fate to which we all head. The coldness of space, the void, death, it is all the same frost, and druids of frost seek to bring all of creation back to its original--frosty--state.

```
name = 'Circle of Frost'
description = "***Druidic Circle: Circle of Frost.*** Druids within the Circle of Frost understand that winter is not just a period of time during the season--it is the fate to which we all head. The coldness of space, the void, death, it is all the same frost, and druids of frost seek to bring all of creation back to its original--frosty--state."
```

## Circle Spells
*2nd-level Circle of Frost feature*

Your connection to the power of ice and snow has given you the ability to summon an [ice axe](../../Magic/Spells/ice-axe.md), as per the spell (using a 3rd-level spell slot), using a bonus action. You can summon this weapon a number of times equal to your proficiency bonus, and it recharges on a short rest.

In addition, you gain access to a number of spells, shown below. Once you gain access to one of these spells, you always have it prepared, and it doesn't count against the number of spells you can prepare each day. If you gain access to a spell that doesn't appear on the druid spell list, the spell is nonetheless a druid spell for you.

Druid Level| Spells
---------- | ------
2nd | [frost trap](../../Magic/Spells/frost-trap.md), [ice beam](../../Magic/Spells/ice-beam.md), [cure wounds](../../Magic/Spells/cure-wounds.md)
3rd | [frost breath](../../Magic/Spells/frost-breath.md), [icingdeath's frost](../../Magic/Spells/icingdeaths-frost.md)
5th | [ice warrior](../../Magic/Spells/ice-warrior.md), [sleet storm](../../Magic/Spells/sleet-storm.md)
7th | [aura of purity](../../Magic/Spells/aura-of-purity.md), [ice body](../../Magic/Spells/ice-body.md)
9th | [snow snakes](../../Magic/Spells/snow-snakes.md), [mass cure wounds](../../Magic/Spells/mass-cure-wounds.md)

```
circlespells = {
    2: ['frost trap', 'ice beam', 'cure wounds'],
    3: ['frost breath', "icingdeath's frost"],
    5: ['ice warrior', 'sleet storm'],
    7: ['aura of purity', 'ice body'],
    9: ['snow snakes', 'mass cure wounds']
}
def level2(npc):
    def circlespellsforlevel(npc):
        results = []
        if npc.levels(baseclass.name) >= 2: results += circlespells[2]
        if npc.levels(baseclass.name) >= 3: results += circlespells[3]
        if npc.levels(baseclass.name) >= 5: results += circlespells[5]
        if npc.levels(baseclass.name) >= 7: results += circlespells[7]
        if npc.levels(baseclass.name) >= 9: results += circlespells[9]
        npc.spellcasting[baseclass.name].spellsalwaysprepared += results

    npc.defer(lambda npc: circlespellsforlevel(npc))

    npc.bonusactions.append(f"***Ice Axe ({npc.proficiencybonus()}/Recharges on short rest).*** You summon an {spelllinkify('ice axe')} as if using a 3rd-level spell slot.")
```

## Enhanced Cold
*6th-level Circle of Frost feature*

Whenever you cast a spell that deals cold damage or restores hit points, roll a d8. You can add this number to the damage or healing roll of the spell.

```
def level6(npc):
    npc.traits.append("***Enhanced Cold.*** Whenever you cast a spell that deals cold damage or restores hit points, roll a d8. You can add this number to the damage or healing roll of the spell.")
```

## Cleansing Frost
*10th-level Circle of Frost feature*

You gain the ability to turn death into magical swirling frost that can heal or incinerate. When a Small or larger creature dies within 30 feet of you, a harmless spectral cloud springs forth in the dead creature's space and hovers there for 1 minute. When a creature you can see enters that space, you can use your reaction to extinguish the spectral cloud there and either heal the creature or deal cold damage to it. The healing or damage equals 2d10 + your Wisdom modifier. 

You can use this reaction a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest. 

```
def level10(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Cleansing Frost ({npc.proficiencybonus()}/Recharges on long rest).*** When a Small or larger creature dies within 30 feet of you, a harmless spectral cloud springs forth in the dead creature's space and hovers there for 1 minute. When a creature you can see enters that space, you can use this reaction to extinguish the spectral cloud there and either heal the creature or deal cold damage to it. The healing or damage equals 2d10 + {npc.WISbonus()}.") )
```

## Chill of Revival
*14th-level Circle of Frost feature*

Your familiarity with the chill of death gives you the ability to come back from the nearness of it. If you are reduced to 0 hit points and thereby fall unconscious, you can use your action to regain half your hit points and immediately rise to your feet. 

Once you use this feature, you can't use it again until you finish a long rest.

```
def level14(npc):
    npc.actions.append("***Chill of Revival (Recharges on long rest).*** If you are at 0 hit points and unconscious, you regain half your hit points and immediately rise to your feet.")
```
