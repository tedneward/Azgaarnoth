## Dark Elf (*drow*)
Elvish scholars speak of an ancient schism amongst the Eldar--and some insist that this was the start of the Fall--that prompted an offshoot of the Eldar to take refuge underground. Rumors hold that these dark elves are the reason (somehow) Mt Bezulb continues to erupt consistently. Note that despite numerous claims to the contrary, *drow* and *shadar-kai* are not the same race, and in fact they seem to have an inborn implacable hatred of one another that defies explanation.

Most *drow* seem to hail from the Daw Mountains near the only active volcano in Azgaarnoth, Mt Bezulb.

* **Ability Score Increase**. Your Charisma score increases by 1.

* ***Drow* Magic**. You know the [dancing lights](https://www.dndbeyond.com/spells/dancing-lights) cantrip. When you reach 3rd level, you can cast Faerie Fire once, and it recharges after a long rest. When you reach 5th level, you can cast Darkness once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.

* ***Drow* Weapon Training**. You have proficiency with rapiers, shortswords, and hand crossbows.

* **Superior Darkvision**. Your darkvision has a range of 120 feet, instead of 60.

* **Sunlight Sensitivity**. You have disadvantage on attack rolls and Wisdom (Perception) checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive is in direct sunlight.

```
name = 'Dark'
def level0(npc):
  npc.description.append("***Subrace: Dark Elf.*** Elvish scholars speak of an ancient schism amongst the Eldar--and some insist that this was the start of the Fall--that prompted an offshoot of the Eldar to take refuge underground. Rumors hold that these dark elves, the *drow*, are the reason (somehow) Mt Bezulb continues to erupt consistently. Note that despite numerous claims to the contrary, *drow* and *shadar-kai* are not the same race, and in fact they seem to have an inborn implacable hatred of one another that defies explanation.")

  npc.CHA += 1

  npc.newspellcasting('Dark Elf', 'CHA').cantripsknown.append('dancing lights')

  npc.proficiencies.append('Rapier')
  npc.proficiencies.append('Shortsword')
  npc.proficiencies.append('Hand crossbow')

  npc.senses['darkvision'] = 120
  npc.traits.append(traits['sunlight-sensitivity'])

def level3(npc):
  npc.spellcasting['Dark Elf'].spells[1].append('faerie fire')
  npc.spellcasting['Dark Elf'].slots = [ 1 ]

def level5(npc):
  npc.spellcasting['Dark Elf'].spells[2].append('darkness')
  npc.spellcasting['Dark Elf'].slots = [ 1, 1 ]
```
