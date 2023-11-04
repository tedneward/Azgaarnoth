## Bloodline of Mammon
The great miser Mammon loves coins above all else. Tieflings tied to him excel at gathering and safeguarding wealth.

* **Ability Score Increase**. Your Intelligence score increases by 1.

* **Legacy of Minauros**. You know the [mage hand](https://www.dndbeyond.com/spells/mage-hand) cantrip. Once you reach 3rd level, you can cast the Tenser's Floating Disk spell once as a 2nd-level spell. Once you reach 5th level, you can also cast the [arcane lock](https://www.dndbeyond.com/spells/arcane-lock) spell once. You must finish a long rest to cast these spells again with this trait. Charisma is your spellcasting ability for these spells.

``` 
name = 'Mammon'
def level0(npc):   
    npc.description.append("**Bloodline of Mammon.** The great miser Mammon loves coins above all else. Tieflings tied to him excel at gathering and safeguarding wealth.")

    npc.INT += 1

    spellcasting = innatecaster(npc, 'CHA', "Mammon Tiefling")
    spellcasting.cantripsknown.append('mage hand')

def level3(npc):
    npc.spellcasting['Mammon Tiefling'].perday[1] = [ 'tensers floating disk' ]

def level5(npc):
    npc.spellcasting['Mammon Tiefling'].perday[1].append('arcane lock')
```
