# Sorcerous Origin: Aberrant Mind
An alien influence has wrapped its tendrils around you, warping you in both body and mind. Perhaps a psychic splinter lodged in your psyche after you suffered domination by an aboleth. Maybe you were born somewhere tainted by the Far Realm, a planar blot that changed you forever. Or perhaps mind flayers kidnapped you, subjecting you to the nightmarish process of ceremorphosis---but the transformation failed and left you altered.

```
name = 'Aberrant Mind'
description = "***Sorcerous Origin: Aberrant Mind.*** An alien influence has wrapped its tendrils around you, warping you in both body and mind. Perhaps a psychic splinter lodged in your psyche after you suffered domination by an aboleth. Maybe you were born somewhere tainted by the Far Realm, a planar blot that changed you forever. Or perhaps mind flayers kidnapped you, subjecting you to the nightmarish process of ceremorphosis---but the transformation failed and left you altered."
```

## Invasive Thoughts
*1st-level Aberrant Mind feature*

You gain the ability to use a bonus action to magically create a telepathic link with one creature you can see within 30 feet of you. Until the link ends, you can telepathically speak to the target through the link, and if it understands at least one language, it can speak telepathically to you. The link lasts for 10 minutes, and it ends early if you are incapacitated or die, or if you use another bonus action to break the link or to establish this link with a different creature.

```
def level1(npc):
    npc.bonusactions.append("***Invasive Thoughts.*** You create a telepathic link with one creature you can see within 30 feet of you. Until the link ends, you can telepathically speak to the target through the link, and if it understands at least one language, it can speak telepathically to you. The link lasts for 10 minutes, and it ends early if you are incapacitated or die, or if you use another bonus action to break the link or to establish this link with a different creature.")
```

## Psionic Spells
*1st-level Aberrant Mind feature*

Your aberrant nature changes your mind in subtle but profound ways. You learn additional spells when you reach certain levels in this class, as shown on the Psionic Spells table. The spell counts as a sorcerer spell for you, but it doesn't count against the number of sorcerer spells you know. These spells can't be replaced when you gain a level in this class.

**Psionic Spells**
Sorcerer Level | Spells 
-------------- | ------
1st | arms of Hadar, dissonant whispers
3rd | calm emotions, detect thoughts
5th | hunger of Hadar, sending
7th | compulsion, Evard's black tentacles
9th | modify memory, Rary's telepathic bond

```
    def psionicspells(npc):
        level = npc.levels('Sorcerer')
        spellcasting = npc.spellcasting['Sorcerer']
        spellcasting.spellsalwaysprepared.append('arms of hadar')
        spellcasting.spellsalwaysprepared.append('dissonant whispers')
        if level > 2:
            spellcasting.spellsalwaysprepared.append('calm emotions')
            spellcasting.spellsalwaysprepared.append('detect thoughts')
        if level > 4:
            spellcasting.spellsalwaysprepared.append('hunger of hadar')
            spellcasting.spellsalwaysprepared.append('sending')
        if level > 6:
            spellcasting.spellsalwaysprepared.append('compulsion')
            spellcasting.spellsalwaysprepared.append('evards black tentacles')
        if level > 8:
            spellcasting.spellsalwaysprepared.append('modify memory')
            spellcasting.spellsalwaysprepared.append('rarys telepathic bond')

    npc.defer(lambda npc: psionicspells(npc) )
```

## Warped Being
*1st-level Aberrant Mind feature*

Your aberrant origin protects you from harm. Your body might have a coating of viscous slime, tough hide, scales, or an invisible psionic barrier (choose the form of protection when you gain this feature). Whatever form the protection takes, your AC equals 13 + your Dexterity modifier while you aren't wearing armor.

```
    npc.armorclass['Natural armor'] = (13 + npc.DEXbonus())
```

## Psionic Sorcery
*6th-level Aberrant Mind feature*

When you cast any of the spells gained from your Psionic Spells feature, you can cast it by expending a spell slot as normal or by spending a number of sorcery points equal to the spell's level. If you cast the spell using sorcery points, it requires no components.

```
def level6(npc):
    npc.actions.append("***Psionic Sorcery.*** You can cast one of your Psionic Spells by expending a spell slot as normal, or by spending a number of sorcery points equal to the spell's level. If you cast the spell using sorcery points, it requires no components.")
```

## Psychic Defenses
*6th-level Aberrant Mind feature*

You gain resistance to psychic damage, and you have advantage on saving throws against being charmed or frightened.

```
    npc.damageresistances.append('psychic')
    npc.traits.append("***Psychic Defenses.*** You have advantage on saving throws against being charmed or frightened.")
```

## Revelation in Flesh
*14th-level Aberrant Mind feature*

You can unleash the aberrant truth hidden within your flesh. As a bonus action, you can spend 1 or more sorcery points to magically transform your body for 1 minute. For each sorcery point you spend, you can gain one of the following benefits of your choice, the effects of which last until the transformation ends:

* You gain a swimming speed equal to your walking speed and the ability to breathe water. Gills grow from your neck or fan out from behind your ears, your fingers become webbed, or you grow lashing cilia that extend through your clothing.
* You gain a flying speed equal to your walking speed and can hover. As you fly, your skin glistens with mucus.
* Your body, along with any equipment you are wearing or carrying, becomes slimy and pliable. You can move through any space as narrow as 1 inch without squeezing, and you can spend 5 feet of movement to escape from nonmagical restraints or being grappled.
* Your eyes turn black or become writhing sensory tendrils. You are aware of the location of any hidden or invisible creature within 60 feet of you.

```
def level14(npc):
    npc.bonusactions.append("***Revelation in Flesh.*** You spend 1 or more sorcery points to magically transform your body for 1 minute. For each sorcery point you spend, you gain one of the following benefits of your choice, and the effects last until the transformation ends: You gain a swimming speed equal to your walking speed and the ability to breathe water. Gills grow from your neck or fan out from behind your ears, your fingers become webbed, or you grow lashing cilia that extend through your clothing. **and/or** You gain a flying speed equal to your walking speed and can hover. As you fly, your skin glistens with mucus. **and/or** Your body, along with any equipment you are wearing or carrying, becomes slimy and pliable. You can move through any space as narrow as 1 inch without squeezing, and you can spend 5 feet of movement to escape from nonmagical restraints or being grappled. **and/or** Your eyes turn black or become writhing sensory tendrils. You are aware of the location of any hidden or invisible creature within 60 feet of you.")
```

## Warp Reality
*18th-level Aberrant Mind feature*

You become the focal point of a reality-warping anomaly. As an action, you can magically radiate a transparent, 20-foot-radius aura for 1 minute. This might take the form of a sphere of rippling psychic energy, a fluctuating amoebic gel, an extrusion of ephemeral parasites, or some other manifestation. Other creatures treat the aura as difficult terrain, and when they start their turn in it, they take 2d10 psychic damage. When you activate this feature, you can choose any number of creatures you can see to be unaffected by the aura.

As a bonus action, you can end the aura early. If you do so, you and any number of creatures you choose within the aura are teleported to a location you can see within 1 mile of you. Each creature must appear within 20 feet of you and in an unoccupied space. An unwilling creature that succeeds on a Charisma saving throw against your spell save DC is not teleported.

Once you use this feature, you can't use it again until you finish a long rest.

```
def level18(npc):
    npc.actions.append("***Warp Reality (Recharges on long rest).*** You magically radiate a transparent, 20-foot-radius aura for 1 minute. This might take the form of a sphere of rippling psychic energy, a fluctuating amoebic gel, an extrusion of ephemeral parasites, or some other manifestation. Other creatures treat the aura as difficult terrain, and when they start their turn in it, they take 2d10 psychic damage. When you activate this feature, you can choose any number of creatures you can see to be unaffected by the aura.")
    npc.bonusactions.append("***End Warped Reality Aura.*** (This can only be done if your Warp Reality Aura is active.) You and any number of creatures you choose within the aura are teleported to a location you can see within 1 mile of you. Each creature must appear within 20 feet of you and in an unoccupied space. An unwilling creature that succeeds on a Charisma saving throw against your spell save DC is not teleported.")
```
