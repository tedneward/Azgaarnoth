# Winged Elves (*avariel*)
The *avariel* are winged elves. If the *avariel* are still present on Azgaarnoth, they do an excellent job keeping themselves hidden from common sight. Nevertheless, the *avariel* were some of the first elves created as part of the Eldars' Firstborn, and many were tasked with supporting and pairing with the dragons that partnered with the Eldar. Legend held that they often lived in great aeyries in the highest mountains.

The *avariel* are generally lighter in stature and size, often up to a full foot shorter than the average high or wood elf, and much lither of form. Their wings can be folded to curl up close to their backs, which if covered with clothing, could allow them to pass for another form of elf, though not under any sort of detailed scrutiny. (Most *avariel* don't like hiding their wings anyway, feeling it to be constricting and claustrophobic.) Generally they wear light clothing, though when flying at high altitudes will wrap themselves in furs or other insulating clothing to help with the chill of the high altitudes.

Scholars who have (supposedly) studied the *avariel* have reported a general disinterest in the world of mortals, preferring a lifestyle that brings them higher and higher in the air, coming to the ground only when they must. Reportedly some *avariel* over the centuries have grown curious about "grounders" and the "world below", however, and journey among the rest of the mortals on the surface of Azgaarnoth, though whether this is by choice or some form of ostracization is never clear. Lombok Ganjuseri, High Scholar of the [Silent Tower](../../Organizations/MageSchools/SilentTower.md), published what is thought to be the definitive work on the *avariel*, in which he described the *avariel* as extremely "quick" with their emotions--quick to embrace, quick to leave, quick to love, and quick to abandon--but critics point out that his experience was with just a mated pair of the *avariel*, and that given Lombok's somewhat off-putting nature, their responses to him may have been more personal than racial.

* **Flight**. You have a flying speed of 30 feet. To use this speed, you can’t be wearing medium or heavy armor.

* **Languages**. You can speak, read, and write Auran.

```
name = 'Winged'
description = "***Subrace: Winged Elf.*** The *avariel* are generally lighter in stature and size, often up to a full foot shorter than the average high or wood elf, and much lither of form. Their wings can be folded to curl up close to their backs, which if covered with clothing, could allow them to pass for another form of elf, though not under any sort of detailed scrutiny. (Most *avariel* don't like hiding their wings anyway, feeling it to be constricting and claustrophobic.) Generally they wear light clothing, though when flying at high altitudes will wrap themselves in furs or other insulating clothing to help with the chill of the high altitudes."
def level0(npc):
  npc.description.append("***Flight.*** To use your wings to fly, you can’t be wearing medium or heavy armor.")

  npc.speed['flying'] = 30

  npc.languages.append('Auran')
```