# Primal Path: Path of the Wild Magic
Many places in the multiverse abound with beauty, intense emotion, and rampant magic; the Feywild, the Upper Planes, and other realms of supernatural power radiate with such forces and can profoundly influence people. As folk of deep feeling, barbarians are especially susceptible to these wild influences, with some barbarians being transformed by the magic. These magic-suffused barbarians walk the Path of Wild Magic. Elf, tiefling, aasimar, and genasi barbarians often seek this path, eager to manifest the otherworldly magic of their ancestors.

```
name = 'Wild Magic'
description = "***Primal Path: Path of the Wild Magic.*** Many places in the multiverse abound with beauty, intense emotion, and rampant magic; the Feywild, the Upper Planes, and other realms of supernatural power radiate with such forces and can profoundly influence people. As folk of deep feeling, barbarians are especially susceptible to these wild influences, with some barbarians being transformed by the magic. These magic-suffused barbarians walk the Path of Wild Magic."
```

## Magic Awareness
*3rd-level Path of Wild Magic feature*

As an action, you can open your awareness to the presence of concentrated magic. Until the end of your next turn, you know the location of any spell or magic item within 60 feet of you that isn't behind total cover. When you sense a spell, you learn which school of magic it belongs to.

You can use this feature a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
def level3(npc):
    npc.defer(lambda npc: npc.actions.append("***Magic Awareness ({npc.proficiencybonus()}/Recharges on long rest).*** Until the end of your next turn, you know the location of any spell or magic item within 60 feet of you that isn't behind total cover. When you sense a spell, you learn which school of magic it belongs to.") )
```

## Wild Surge
*3rd-level Path of Wild Magic feature*

The magical energy roiling inside you sometimes erupts from you. When you enter your rage, roll on the Wild Magic table to determine the magical effect produced. If the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Constitution modifier. 

**WILD MAGIC**

d8|Magical Effect
--|--------------
1 | Shadowy tendrils lash around you. Each creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d12 necrotic damage. You also gain 1d12 temporary hit points.
2 | You teleport up to 30 feet to an unoccupied space you can see. Until your rage ends, you can use this effect again on each of your turns as a bonus action.
3 | An intangible spirit, which looks like a flumph or a pixie (your choice), appears within 5 feet of one creature of your choice that you can see within 30 feet of you. At the end of the current turn, the spirit explodes, and each creature within 5 feet of it must succeed on a Dexterity saving throw or take 1d6 force damage. Until your rage ends, you can use this effect again, summoning another spirit, on each of your turns as a bonus action.
4 | Magic infuses one weapon of your choice that you are holding. Until your rage ends, the weapon's damage type changes to force, and it gains the light and thrown properties, with a normal range of 20 feet and a long range of 60 feet. If the weapon leaves your hand, the weapon reappears in your hand at the end of the current turn.
5 | Whenever a creature hits you with an attack roll before your rage ends, that creature takes 1d6 force damage, as magic lashes out in retribution.
6 | Until your rage ends, you are surrounded by multicolored, protective lights; you gain a +l bonus to AC, and while within 10 feet of you, your allies gain the same bonus.
7 | Flowers and vines temporarily grow around you; until your rage ends, the ground within 15 feet of you is difficult terrain for your enemies.
8 | A bolt of light shoots from your chest. Another creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw or take 1d6 radiant damage and be blinded until the start of your next turn. Until your rage ends, you can use this effect again on each of your turns as a bonus action.

```
    npc.defer(lambda npc: npc.traits.append("***Wild Surge.*** When you enter your rage, the Wild Magic inside of you produces a magical effect; roll {'a d8' if npc.levels('Barbarian') < 14 else '2d8 and choose which of the two effects to unleash. If you roll the same number on both dice, you can ignore the number and choose the effect'}: **1:** Shadowy tendrils lash around you. Each creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}) or take 1d12 necrotic damage. You also gain 1d12 temporary hit points. **2:** You teleport up to 30 feet to an unoccupied space you can see. Until your rage ends, you can use this effect again on each of your turns as a bonus action. **3:** An intangible spirit, which looks like a flumph or a pixie (your choice), appears within 5 feet of one creature of your choice that you can see within 30 feet of you. At the end of the current turn, the spirit explodes, and each creature within 5 feet of it must succeed on a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}) or take 1d6 force damage. Until your rage ends, you can use this effect again, summoning another spirit, on each of your turns as a bonus action. **4:** Magic infuses one weapon of your choice that you are holding. Until your rage ends, the weapon's damage type changes to force, and it gains the light and thrown properties, with a normal range of 20 feet and a long range of 60 feet. If the weapon leaves your hand, the weapon reappears in your hand at the end of the current turn. **5:** Whenever a creature hits you with an attack roll before your rage ends, that creature takes 1d6 force damage, as magic lashes out in retribution. **6:** Until your rage ends, you are surrounded by multicolored, protective lights; you gain a +1 bonus to AC, and while within 10 feet of you, your allies gain the same bonus. **7:** Flowers and vines temporarily grow around you; until your rage ends, the ground within 15 feet of you is difficult terrain for your enemies. **8:** A bolt of light shoots from your chest. Another creature of your choice that you can see within 30 feet of you must succeed on a Constitution saving throw (DC {8 + npc.proficiencybonus() + npc.CONbonus()}) or take 1d6 radiant damage and be blinded until the start of your next turn. Until your rage ends, you can use this effect again on each of your turns as a bonus action.") )
```

## Bolstering Magic
*6th-level Path of Wild Magic feature*

You can harness your wild magic to bolster yourself or a companion. As an action, you can touch one creature (which can be yourself) and confer one of the following benefits of your choice to that creature:

* For 10 minutes, the creature can roll a d3 whenever making an attack roll or an ability check and add the number rolled to the d20 roll.
* Roll a d3. The creature regains one expended spell slot, the level of which equals the number rolled or lower (the creature's choice). Once a creature receives this benefit, that creature can't receive it again until after a long rest.

You can take this action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append("***Bolstering Magic ({npc.proficiencybonus()}/Recharges on long rest).*** You touch one creature (which can be yourself) and confer one of the following benefits of your choice to that creature: **(a)** For 10 minutes, the creature can roll a d3 whenever making an attack roll or an ability check and add the number rolled to the d20 roll; **(b)** Roll a d3. The creature regains one expended spell slot, the level of which equals the number rolled or lower (the creature's choice). Once a creature receives this benefit, that creature can't receive it again until after a long rest.") )
```

## Unstable Backlash
*10th-level Path of Wild Magic feature*

When you are imperiled during your rage, the magic within you can lash out; immediately after you take damage or fail a saving throw while raging, you can use your reaction to roll on the Wild Magic table and immediately produce the effect rolled. This effect replaces your current Wild Magic effect.

```
def level10(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Unstable Backlash.*** Immediately after you take damage or fail a saving throw while raging, you roll generate a new Wild Surge effect; roll {'a d8' if npc.levels('Barbarian') < 14 else '2d8 and choose which of the two effects to unleash. If you roll the same number on both dice, you can ignore the number and choose the effect'} for your Wild Surge and immediately produce the effect rolled. This effect replaces your current Wild Surge effect.") )
```

## Controlled Surge
*14th-level Path of Wild Magic feature*

Whenever you roll on the Wild Magic table, you can roll the die twice and choose which of the two effects to unleash. If you roll the same number on both dice, you can ignore the number and choose any effect on the table. 
