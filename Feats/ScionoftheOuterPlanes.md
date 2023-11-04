## Scion of the Outer Planes
You are influenced by and adept at navigating planar pathways and the strange realities of the Outer Planes.

Whether planar essence infuses you or you have extraplanar ancestry, your connection to a plane infuses you with the energies found there. Choose a type of plane listed in the table below. Your choice gives you resistance to a damage type and the ability to cast a cantrip, as specified in the table. You can cast this cantrip without material components, and your spellcasting ability for it is Intelligence, Wisdom, or Charisma (choose when you select this feat).

Plane | Damage Resistance | Cantrip
----- | ----------------- | -------
Astral Plane | Psychic | [message](../Magic/Spells/message.md)
Chaotic Outer Plane | Necrotic | [minor illusion](../Magic/Spells/minor-illusion.md)
Evil Outer Plane | Necrotic | [chill touch](../Magic/Spells/chill-touch.md)
Good Outer Plane | Radiant | [sacred flame](../Magic/Spells/sacred-flame.md)
Lawful Outer Plane | Radiant | [guidance](../Magic/Spells/guidance.md)
The Outlands | Psychic | [mage hand](../Magic/Spells/mage-hand.md)

```
name = 'Scion of the Outer Planes'
description = "***Feat: Scion of the Outer Planes.*** You are influenced by and adept at navigating planar pathways and the strange realities of the Outer Planes."
def prereq(npc): return True
def apply(npc):
    planes = {
        'Astral': ['psychic', 'message'],
        'Chaotic': ['necrotic', 'minor illusion'],
        'Evil': ['necrotic', 'chill touch'],
        'Good': ['radiant', 'sacred flame'],
        'Lawful': ['radiant', 'guidance'],
        'Outlands': ['psychic', 'mage hand']
    }
    (planename, planeeffects) = choose("Choose your planar connection: ", planes)
    npc.scionplane = planename
    npc.damageresistances.append(planeeffects[0])
    ability = choose("Choose your spellcasting ability: ", ['INT','WIS','CHA'])
    spellcasting = innatecaster(npc, ability, 'Scion')
    spellcasting.cantripsknown.append(spelllinkify(planeeffects[1]))
```
