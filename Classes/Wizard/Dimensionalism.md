# Arcane Tradition: Dimensionalism
Dimensionalists are wizards specializing in dimensional magic, manipulating the very fabric between the planes of existence. A dangerous field of study, many dimensionalists are lost to the various planes during their experimentation, but those that master manipulating the fabric of reality, are forces to be reckoned with.

Dimensionalists are often tied quite closely to the [Shining Door](../../Organizations/MageSchools/ShiningDoor.md) school.

```
name = 'Dimensionalism'
description = "***Arcane Tradition: Dimensionalism.*** Dimensionalists are wizards specializing in dimensional magic, manipulating the very fabric between the planes of existence. A dangerous field of study, many dimensionalists are lost to the various planes during their experimentation, but those that master manipulating the fabric of reality, are forces to be reckoned with."
```

## Dimensional Knowledge
*2nd-level Dimensionalism feature*

You gain proficiency in the Arcana skill if you don't already have it, and your proficiency bonus is doubled for any Intelligence check that you make in relation to the planes, or planar knowledge.

```
def level2(npc):
    npc.proficiencies.append('Arcana')
    npc.traits.append("***Dimensional Knowledge.*** Your proficiency bonus is doubled for any Intelligence check that you make in relation to the planes, or planar knowledge.")
```

## Dimensional Pocket
*2nd-level Dimensionalism feature*

You are able to alter the fabric of reality to create a small dimensional pocket that you can manipulate for storing items. The size of the area that you can create is equal to your Intelligence modifier in cubic feet. As an action, you can access your pocket dimension, regardless of your location, to store or retrieve items inside it. Only you can see into, or access, your dimensional pocket. Living creatures cannot be stored in the pocket.

```
    npc.defer(lambda npc: npc.traits.append("***Dimensional Pocket.*** You are able to alter the fabric of reality to create a small dimensional pocket, {npc.INTbonus()} cubic feet in size, that you can manipulate for storing items. Living creatures cannot be stored in the pocket.") )
    npc.actions.append("***Access Pocket.*** You can access your pocket dimension, regardless of your location, to store or retrieve items inside it. Only you can see into, or access, your dimensional pocket.")
```

## Dimensional Tear
*6th-level Dimensionalism feature*

You can briefly tear the fabric of reality, releasing a 15-foot cone of energy from your hands. The dimension you choose to access, determines the type of energy released; fire, cold, lightning, thunder, poison, radiant, or necrotic. All creatures in the cone must make a Dexterity saving throw, taking 1d6 + your wizard level damage (of the chosen type) on a failed save, or half as much damage on a successful one. You regain the use of this ability after finishing a short or long rest.

```
def level6(npc):
    npc.defer(lambda npc: npc.actions.append(f"***Dimensional Tear (Recharges on short or long rest).*** You can briefly tear the fabric of reality, releasing a 15-foot cone of energy from your hands. The dimension you choose to access, determines the type of energy released; fire, cold, lightning, thunder, poison, radiant, or necrotic. All creatures in the cone must make a Dexterity saving throw, taking 1d6 + {npc.levels('Wizard')} damage of the chosen type on a failed save, or half as much on a successful one.") )
```

## Dimensional Slip
*10th-level Dimensionalism feature*

You are briefly able to slip between dimensions with minimal effort. When you move, you can elect to move through the Astral Plane instead. Movement through the Astral Plane using this ability is considered difficult terrain, and you automatically end your movement back on the Material Plane. Whilst in the Astral Plane, you don't move through solid objects, but rather you bypass their spaces – ignoring non-solid obstacles, creatures, or terrain features – and your movement does not provoke opportunity attacks.

```
def level10(npc):
    npc.traits.append("***Dimensional Slip.*** When you move, you can elect to move through the Astral Plane instead. Movement through the Astral Plane using this ability is considered difficult terrain, and you automatically end your movement back on the Material Plane. Whilst in the Astral Plane, you don't move through solid objects, but rather you bypass their spaces – ignoring non-solid obstacles, creatures, or terrain features – and your movement does not provoke opportunity attacks.")
```

## Demiplane Refuge
*14th-level Dimensionalism feature*

Using your action, you are able to generate and maintain a small demiplane, that you can access at will. The demiplane is limited to a 20-foot cube, and you control lighting, atmosphere, and gravity. You can store objects in the demiplane, and you alone can enter. You can exist on the demiplane as long as you have sufficient food and water. When you exit, you re-enter the Material Plane at the same point where you left.

```
def level14(npc):
    npc.actions.append("***Demiplane Refuge.*** You are able to generate and maintain a small demiplane, that you can access at will. The demiplane is limited to a 20-foot cube, and you control lighting, atmosphere, and gravity. You can store objects in the demiplane, and you alone can enter. You can exist on the demiplane as long as you have sufficient food and water. When you exit, you re-enter the Material Plane at the same point where you left.")
```

---

# Dimensionalist Spells

## 1st
* [dimensional window](../../Magic/Spells/dimensional-window.md)

## 2nd
* [dimensional reach](../../Magic/Spells/dimensional-reach.md)

## 3rd
* [dimensional doorway](../../Magic/Spells/dimensional-doorway.md)

## 5th
* [fleeting journey](../../Magic/Spells/fleeting-journey.md)

