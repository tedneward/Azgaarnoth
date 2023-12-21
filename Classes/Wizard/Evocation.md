# Arcane Tradition: School of Evocation
You focus your study on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. Some evokers find employment in military forces, serving as artillery to blast enemy armies from afar. Others use their spectacular power to protect the weak, while some seek their own gain as bandits, adventurers, or aspiring tyrants.

Evokers are drawn naturally to the [Fiery Fist](../../Organizations/MageSchools/FieryFist.md) and [Crimson Sunrise](../../Organizations/MageSchools/CrimsonSunrise.md) mage schools, among others, and are often heavily recruited by [mercenary companies](../../Organizations/MercCompanies/MercCompanies.md).

```
name = 'Evocation'
description = "***Arcane Tradition: School of Evocation.*** You focus your study on magic that creates powerful elemental effects such as bitter cold, searing flame, rolling thunder, crackling lightning, and burning acid. Some evokers find employment in military forces, serving as artillery to blast enemy armies from afar. Others use their spectacular power to protect the weak, while some seek their own gain as bandits, adventurers, or aspiring tyrants."
```

## Evocation Savant
*2nd-level Evocation feature*

The gold and time you must spend to copy a Evocation spell into your spellbook is halved.

```
def level2(npc):
    npc.traits.append("***Evocation Savant.*** The gold and time you must spend to copy a Evocation spell into your spellbook is halved.")
```

## Sculpt Spells
*2nd-level Evocation feature*

You can create pockets of relative safety within the effects of your evocation spells. When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save.

```
    npc.traits.append("***Sculpt Spells.*** When you cast an evocation spell that affects other creatures that you can see, you can choose a number of them equal to 1 + the spell's level. The chosen creatures automatically succeed on their saving throws against the spell, and they take no damage if they would normally take half damage on a successful save.")
```

## Potent Cantrip
*6th-level Evocation feature*

Your damaging cantrips affect even creatures that avoid the brunt of the effect. When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip.

```
def level6(npc):
    npc.traits.append("***Potent Cantrip.*** When a creature succeeds on a saving throw against your cantrip, the creature takes half the cantrip's damage (if any) but suffers no additional effect from the cantrip.")
```

## Empowered Evocation
*10th-level Evocation feature*

You can add your Intelligence modifier (minimum of +1) to the damage roll of any wizard evocation spell that you cast. The damage bonus applies to one damage roll of a spell, not multiple rolls.

```
def level10(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Empowered Evocation.*** You add {npc.INTbonus()} to the damage roll of any wizard evocation spell that you cast. The damage bonus applies to one damage roll of a spell, not multiple rolls.") )
```

## Overchannel
*14th-level Evocation feature*

You can increase the power of your simpler spells. When you cast a wizard spell of 5th level or lower that deals damage and isn't a cantrip, you can deal maximum damage with that spell.

The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity.

```
def level14(npc):
    npc.traits.append("***Overchannel.*** When you cast a wizard spell of 5th level or lower that deals damage and isn't a cantrip, you can deal maximum damage with that spell. The first time you do so, you suffer no adverse effect. If you use this feature again before you finish a long rest, you take 2d12 necrotic damage for each level of the spell, immediately after you cast it. Each time you use this feature again before finishing a long rest, the necrotic damage per spell level increases by 1d12. This damage ignores resistance and immunity.")
```
