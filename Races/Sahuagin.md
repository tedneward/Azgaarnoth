# [Sahuagin](../Creatures/Sahuagin.md)

A fish-like monstrous humanoid species that lives in oceans, seas, underground lakes, and underwater caves

```
name = 'Sahuagin'
type = 'humanoid'
```

**Ability Score Increase.** Your Strength score increases by 2 and Wisdom score each increases by 1.

**Age.** The adult age and lifespan of Sahuagin is not widely known, but many speculate that they live to be slightly older than humans, about 100-120 years at most. Sahuagin reach maturity at 22 years old.

**Alignment.** Sahuagin tend towards chaotic and mainly evil alignments due to their viciousness and innate savagery.

**Size.** Sahuagin stand 5 to 6 feet tall and average about 200 pounds. Your size is Medium.

**Speed.** Your base walking speed is 20 feet, and you have a swimming speed of 40 feet.

**Darkvision.** You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.

**Bite.** Your piranha-like mouth is a natural weapon, which you can use to make unarmed strikes. If you hit with it, you can deal piercing damage equal to 1d4 + your Strength modifier, instead of the bludgeoning damage normal for an unarmed strike.

**Limited Amphibiousness.** You can breathe air and water, but need to be submerged at least once every 8 hours to avoid dehydration, suffering one level of exhaustion.

**Shark Telepathy.** You can communicate simple ideas with sharks. They may understand you, but you have no way of understanding them.

**Blood in the Water.** Your specialized sense of smell can detect blood. You are aware of creatures within 20 feet that have hit points below their maximum, and can bleed. When in water, this range extends to 60 feet.

**Sharks Frenzy.** You do not fear battle, for you can gorge on the flesh of enemies to stay prime. As a bonus action, you can make a special attack with your Bite. If the attack hits, it deals its normal damage, and you gain temporary hit points (minimum of 1) equal to your Constitution modifier, and you can't use this trait again until you finish a short or long rest. These temporary hit points disappear when you finish a long rest.

**Languages.** You can speak, read, and write Common and Aquan

There are no known sub-races of sahuagin (yet).

```
def level0(npc):
    npc.description.append("***Race: Sahuagin.*** A fish-like monstrous humanoid species that lives in oceans, seas, underground lakes, and underwater caves.")

    npc.STR += 2
    npc.WIS += 1
    npc.size = 'Medium'
    npc.speed['walking'] = 20
    npc.speed['swimming'] = 40
    npc.senses['darkvision'] = 60
    npc.senses['blood'] = 20

    npc.defer(lambda npc: npc.actions.append(f"***Bite.*** Melee Weapon Attack: {npc.proficiencybonus() + npc.STRbonus()} to hit, reach 5 ft., one target. Hit: 1d4 + {npc.STRbonus()} piercing damage."))

    npc.traits.append("***Limited Amphibiousness.*** You can breathe air and water, but need to be submerged at least once every 8 hours to avoid dehydration. For each 8 hours period you do not submerge, you suffer one additional level of exhaustion.")

    npc.traits.append("***Shark Telepathy.*** You can communicate simple ideas with sharks. They may understand you, but you have no way of understanding them.")

    npc.traits.append("***Blood in the Water.*** Your specialized sense of smell can detect blood. You are aware of creatures within 20 feet that have hit points below their maximum, and can bleed. When in water, this range extends to 60 feet.")

    npc.defer(lambda npc: npc.bonusactions.append(f"***Sharks Frenzy (Recharges on short or long rest).*** You can make a special attack with your Bite. If the attack hits, it deals its normal damage, and you gain {npc.CONbonus()} temporary hit points. These temporary hit points disappear when you finish a long rest."))
```
