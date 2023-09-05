## Bloodline of Mammon
The great miser Mammon loves coins above all else. Tieflings tied to him excel at gathering and safeguarding wealth.

* **Ability Score Increase**. Your Intelligence score increases by 1.

* **Legacy of Minauros**. You know the [mage hand](https://www.dndbeyond.com/spells/mage-hand) cantrip. Once you reach 3rd level, you can cast the Tenser's Floating Disk spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the [arcane lock](https://www.dndbeyond.com/spells/arcane-lock) spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

``` 
name = 'Mammon'
def level0(npc):   
    npc.description.append("**Bloodline of Mammon.** The great miser Mammon loves coins above all else. Tieflings tied to him excel at gathering and safeguarding wealth.")

    npc.INT += 1

    npc.cantripsknown.append('mage hand')

def level3(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Infernal Legacy (Recharges on long rest).*** You can cast " + spelllinkify('tensers floating disk') + "as a 2nd-level spell. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))

def level5(npc):
    npc.defer(lambda npc: replace("***Infernal Legacy", npc.actions, f" (Recharges on long rest).*** You can cast {spelllinkify('tensers floating disk')} as a 2nd-level spell or {spelllinkify('arcane lock')}. (Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()})"))
```
