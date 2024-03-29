# Monastic Tradition: Way of the Astral Self
A monk who follows the Way of the Astral Self believes their body is an illusion. They see their ki as a representation of their true form, an astral self. This astral self has the capacity to be a force of order or disorder, with some monasteries training students to use their power to protect the weak and other instructing aspirants in how to manifest their true selves in service to the mighty. 

> ### Forms of Your Astral Self
> The astral self is a translucent embodiment of the monk's psyche and soul. As a result, the form of an astral self reflects the mind of the monk who manifests it. Your astral self could be a humanoid knight with a helmeted face and large, muscular arms, or it could be a golden metallic form with thin arms like a modron.
> When choosing this path, consider the quirks that define your monk. Are they obsessed with something? Are you driven by justice or a selfish desire? Any of these motivations could manifest in the form of your astral self.

```
name = 'Way of the Astral Self'
description = "***Monastic Tradition: Way of the Astral Self.*** A monk who follows the Way of the Astral Self believes their body is an illusion. They see their ki as a representation of their true form, an astral self. This astral self has the capacity to be a force of order or disorder, with some monasteries training students to use their power to protect the weak and other instructing aspirants in how to manifest their true selves in service to the mighty."
```

## Arms of the Astral Self
*3rd-level Way of the Astral Self feature*

Your mastery of your ki allows you to summon a portion of your astral self. As a bonus action, you can spend 1 ki point to summon the arms of your astral self. When you do so, each creature of your choice that you can see within 10 feet of you must succeed on a Dexterity saving throw or take force damage equal to two rolls of your Martial Arts die.

For 10 minutes, these spectral arms hover near your shoulders or surround your arms (your choice). You determine the arms' appearance, and they vanish early if you are incapacitated or die. While the spectral arms are present, you gain the following benefits:

* You can use your Wisdom modifier in place of your Strength modifier when making Strength checks and Strength saving throws.
* You can use the spectral arms to make unarmed strikes.
* When you make an unarmed strike with the arms on your turn, your reach for it is 5 feet greater than normal.
* The unarmed strikes you make with the arms can use your Wisdom modifier in place of your Strength or Dexterity modifier for the attack and damage rolls, and their damage type is force.

```
def level3(npc):
    npc.defer(lambda npc: npc.bonusactions.append(f"***Ki: Arms of the Astral Self.*** you can spend 1 ki point to summon the arms of your astral self. When you do so, each creature of your choice that you can see within 10 feet of you must succeed on a Dexterity saving throw (DC {8 + npc.proficiencybonus() + npc.WISbonus()}) or take 2d{npc.martialartsdie} force damage. For 10 minutes, these spectral arms hover near your shoulders or surround your arms, and while they are present, you can use your Wisdom modifier in place of your Strength modifier when making Strength checks and saving throws; you can use the spectral arms to make unarmed strikes (*Melee Weapon Attack:* +{npc.proficiencybonus() + npc.WISbonus()} to hit, reach 10 feet, one target. Hit: 1d{npc.martialartsdie} + {npc.WISbonus()} force damage.{' This attack is considered magical for purposes of overcoming resistance and immunity to nonmagical attacks and damage.' if npc.levels('Monk') > 5 else ''}).") )
```

## Visage of the Astral Self
*6th-level Way of the Astral Self feature*

You can summon the visage of your astral self. As a bonus action, or as part of the bonus action you take to activate Arms of the Astral Self, you can spend 1 ki point to summon this visage for 10 minutes. It vanishes early if you are incapacitated or die. 

The spectral visage covers your face like a helmet or mask. You determine its appearance. 

While the spectral visage is present, you gain the following benefits:

* **Astral Sight.** You can see normally in darkness, both magical and nonmagical, to a distance of 120 feet.
* **Wisdom of the Spirit.** You have advantage on Wisdom (Insight) and Charisma (Intimidation) checks.
* **Word of the Spirit.** When you speak, you can direct your words to a creature of your choice that you can see within 60 feet of you, making it so only that creature can hear you. Alternatively, you can amplify your voice so that all creatures within 600 feet can hear you.

```
def level6(npc):
    npc.bonusactions.append(f"***Ki: Visage of the Astral Self.*** You can spend 1 ki point to summon the visage of your astral self for 10 minutes, covering your face like a helmet or mask. While present, you can see normally in darkness, both magical and nonmagical, to a distance of 120 feet; you have advantage on Wisdom (Insight) and Charisma (Intimidation) checks; when you speak, you can direct your words to a creature of your choice that you can see within 60 feet of you, making it so only that creature can hear you. Alternatively, you can amplify your voice so that all creatures within 600 feet can hear you.")
```

## Body of the Astral Self
*11th-level Way of the Astral Self feature*

When you have both your astral arms and visage summoned, you can cause the body of your astral self to appear (no action required). This spectral body covers your physical form like a suit of armor, connecting with the arms and visage. You determine its appearance. 

While the spectral body is present, you gain the following benefits:

* **Deflect Energy.** When you take acid, cold, fire, force, lightning, or thunder damage, you can use your reaction to deflect it. When you do so, the damage you take is reduced by 1d10 + your Wisdom modifier (minimum reduction of 1).
* **Empowered Arms.** Once on each of your turns when you hit a target with the Arms of the Astral Self, you can deal extra damage to the target equal to your Martial Arts die.

```
def level11(npc):
    npc.defer(lambda npc: npc.reactions.append(f"***Ki: Body of the Astral Self.*** When you take acid, cold, fire, force, lightning, or thunder damage, you can deflect it. When you do so, the damage you take is reduced by 1d10 + {npc.WISbonus()}.") )
    npc.defer(lambda npc: npc.bonusactions.append(f"***Ki: Arms of the Astral Self enhancement.*** Once on each of your turns when you hit a target with the Arms of the Astral Self, you can deal 1d{npc.martialartsdie} extra damage to the target.") )
```

## Awakened Astral Self
*17th-level Way of the Astral Self feature*

Your connection to your astral self is complete, allowing you to unleash its full potential. As a bonus action, you can spend 5 ki points to summon the arms, visage, and body of your astral self and awaken it for 10 minutes. This awakening ends early if you are incapacitated or die.

While your astral self is awakened, you gain the following benefits. 

* **Armor of the Spirit.** You gain a +2 bonus to Armor Class.
* **Astral Barrage.** Whenever you use the Extra Attack feature to attack twice, you can instead attack three times if all the attacks are made with your astral arms. 
* **Ki Consumption**. When a creature within 10 feet of you is reduced to 0 hit points, you can use your reaction to regain ki points equal to your Wisdom modifier (minimum 1).

```
def level17(npc):
    npc.defer(lambda npc: npc.bonusactions.append("***Ki: Awakened Astral Self.*** You can spend 5 ki points to summon the arms, visage, and body of your astral self and awaken it for 10 minutes. During this time, you gain a +2 bonus to Armor Class; whenever you use the Extra Attack feature to attack, you can attack three times if all the attacks are made with your astral arms; when a creature within 10 feet of you is reduced to 0 hit points, you can use your reaction to regain {npc.WISbonus()} ki points.") )
```
