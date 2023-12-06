# Arcane Tradition: Arcane Artillerist
The arcane artillerist is an expert at infusing magic with other components to create a strong offense from long range. They use unique alchemical components to enhance their spellcasting capabilities. They are commonly seen among the [mercenary companies](../../Organizations/MercCompanies/index.md), assisting adventurers, or aiding political leadership facing difficult challenges that require a lot of arcane firepower.

Artillerists are always a member of the [Crimson Sunrise](../../Organizations/MageSchools/CrimsonSunrise.md) mage school, and while they are freely encouraged to engage in activities outside the school's contract, they will be expected at some point in their career to take a contract under the school's guidance and approval.

```
name = 'Artillerist'
description = "***Arcane Tradition: Arcane Artillerist.*** The artillerist is an expert at infusing magic with other components to create a strong offense from long range. They use unique alchemical components to enhance their spellcasting capabilities."
```

## Alchemical Expert
*2nd-level Arcane Artillerist feature*

You are proficient in the Arcana skill, as well as with alchemist's supplies.

```
def level2(npc):
    npc.proficiencies.append('Arcana')
    npc.proficiencies.append("Alchemist's supplies")
```

## Siege Artillerist
*2nd-level Arcane Artillerist feature*

If you use your alchemist's supplies as the material component of your spells, you can imbue a spell to deal double damage to objects and structures. You can use this ability a number of times equal to your Intelligence modifier (minimum of once). 

You regain all expended uses when you finish a long rest.

```
    npc.defer(lambda npc: npc.traits.append(f"***Alchemical Enhancement: Siege Artillerist ({npc.INTbonus()}/Recharges on long rest).*** If you use your alchemist's supplies as the material component of your spells, you can imbue a spell to deal double damage to objects and structures.") )
```

## Fog of War
*6th-level Arcane Artillerist feature*

Using your alchemist's supplies as a material component of your spells, you can add a lasting smoke to any instantaneous area of effect spell you cast. Once the spell effect ends, it leaves behind a thick cloud of alchemical smoke for a short time. The residual smoke covers the same area as the spell, creating a heavily obscured area until the end of your next turn, and lightly obscured area until the end of your turn after that. You can use this ability a number of times equal to your Intelligence modifier (minimum 1).

You regain all expended uses of this ability when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.traits.append(f"***Alchemical Enhancement: Fog of War ({npc.INTbonus()}/Recharges on long rest).*** Using your alchemist's supplies as a material component of your spells, you can add a lasting smoke to any instantaneous area of effect spell you cast. Once the spell effect ends, it leaves behind a thick cloud of alchemical smoke for a short time. The residual smoke covers the same area as the spell, creating a heavily obscured area until the end of your next turn, and lightly obscured area until the end of your turn after that.") )
```

## Intense Elements
*10th-level Arcane Artillerist feature*

You are able to mix in alchemical concoctions to your elemental spells that allow them to increase in intensity, clinging to their targets for added effect. When you cast a spell that deals acid, cold, fire, or lightning damage, you can intensify it using your alchemist's supplies as a material component. Any 1s rolled on the damage dice of the spell are automatically treated as a 2 instead. You regain the use of this ability after finishing a short or long rest.

```
def level10(npc):
    npc.traits.append(f"***Intense Elements (Recharges on short or long rest).*** When you cast a spell that deals acid, cold, fire, or lightning damage, you can intensify it using your alchemist's supplies as a material component. Any 1s rolled on the damage dice of the spell are automatically treated as a 2 instead.")
```

## Concentration or Dilution
*14th-level Arcane Artillerist feature*

You have mastered alchemical mixtures capable of concentrating or dispersing your area of effect spells. When you cast a damage-dealing, area of effect spell, you can either:

* Choose to concentrate the spell effect, halving the area of effect but forcing saving throws to resist its effects to be made with disadvantage.
* Choose to dilute the spell effect, doubling its area of effect, but each affected creature gains resistance to the diluted damage type for this spell.

After using this ability you cannot use it again until after you finish a long rest.

```
def level14(npc):
    npc.traits.append("***Concentration/Dilution (Recharges on long rest).*** When you cast a damage-dealing, area of effect spell, you can either: Choose to concentrate the spell effect, halving the area of effect but forcing saving throws to resist its effects to be made with disadvantage; Choose to dilute the spell effect, doubling its area of effect, but each affected creature gains resistance to the diluted damage type for this spell.")
```
