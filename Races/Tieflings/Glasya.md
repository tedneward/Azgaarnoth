## Bloodline of Glasya
Glasya, Hell's criminal mastermind, grants her tiefiings magic that is useful for committing heists.

* **Ability Score Increase**. Your Dexterity score increases by 1.

* **Legacy of Malbolge**. You know the Minor Illusion cantrip. Once you reach 3rd level, you can cast the Disguise Self spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the Invisibility spell once as a 3rd-level spell. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

```
name = 'Glasya'
def level0(npc):
    npc.description.append("**Bloodline of Glasya.** Glasya, Hell's criminal mastermind, grants her tiefiings magic that is useful for committing heists.")

    npc.DEX += 1

    npc.cantripsknown.append('minor illusion')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('disguise self') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('disguise self')} as a 2nd-level spell or {spelllinkify('invisibility')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
