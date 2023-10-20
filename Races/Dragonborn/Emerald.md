# Emerald Dragonborn
Descendant of emerald dragons, emerald dragonborn are ....

### Breath Weapon
You can use your action to exhale psychic energy. It deals damage in a 15' cone. When you use your breath weapon, all creatures in the area must make a DEX saving throw. The DC of this saving throw is 8 + your Constitution modifier + your proficiency bonus. A creature takes 1d10 psychic damage on a failed save, and half as much damage on a successful one. The damage increase to 2d10 at 6th level, 3d10 at 11th, and 4d10 at 16th level. You may use your breath weapon a number of times equal to your Constitution modifier. You regain expended uses on a long rest.

### Damage Resistance
You have resistance to psychic damage.

### Psionic Mind
You can telepathically speak to any creature you can see within 30 feet of you. You don’t need to share a language with the creature, but the creature must be able to understand at least one language.

### Gem Flight
*5th-level Emerald Dragonborn feature*

You can use a bonus action to manifest spectral wings on your body. These wings last for 1 minute. For the duration, you gain a flying speed equal to your walking speed and can hover. Once you use this trait, you can’t do so again until you finish a long rest.

```
name = 'Emerald'
description = "***Emerald Dragonborn.*** ..."
def level0(npc):
    npc.damageresistances.append("psychic")
    npc.languages.append("Telepathy 30 ft")
    npc.defer(lambda npc: npc.actions.append(f"***Breath Weapon ({npc.proficiencybonus()}/Reharges on a long rest).*** You exhale psychic energy in a 15' cone. All creatures in the area must make a DEX saving throw, DC {8 + npc.CONbonus() + npc.proficiencybonus()}. A creature takes {'1d10' if npc.levels() < 6 else '2d10' if npc.levels() < 11 else '3d10' if npc.levels() < 16 else '4d10'} psychic damage on a failed save, or half on a successful one."))
def level5(npc):
    npc.bonusactions.append("***Gem Flight.*** You manifest spectral wings on your body. These wings last for 1 minute. For the duration, you gain a flying speed equal to your walking speed and can hover.")
```
