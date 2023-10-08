# Monastic Tradition: Way of the Drunken Master
The Way of the Drunken Master teaches its students to move with the jerky, unpredictable movements of a drunkard. A drunken master sways, tottering on unsteady feet, to present what seems like an incompetent combatant but proves frustrating to engage. The drunken master's erratic stumbles conceal a carefully executed dance of blocks, parries, advances, attacks, and retreats. Cunning warriors can see through the drunken master's apparent incompetence to recognize the masterful technique employed.


```
name = 'Way of the Drunken Master'
description = "***Monastic Tradition: Way of the Drunken Master.*** The Way of the Drunken Master teaches its students to move with the jerky, unpredictable movements of a drunkard. A drunken master sways, tottering on unsteady feet, to present what seems like an incompetent combatant but proves frustrating to engage. The drunken master's erratic stumbles conceal a carefully executed dance of blocks, parries, advances, attacks, and retreats. Cunning warriors can see through the drunken master's apparent incompetence to recognize the masterful technique employed."
```

## Drunken Technique
*3rd-level Way of the Drunken Master feature*

You gain proficiency in the Performance skill if you don't already have it; your martial arts technique mixes martial training with the precision of a dancer and the antics of a jester.

You also learn how to twist and turn quickly as part of your Flurry of Blows. Whenever you use Flurry of Blows, you gain the benefit of the Disengage action, and your walking speed increases by 10 feet until the end of the current turn.

```
def level3(npc):
    npc.skills.append("Performance")
    npc.actions.append("***Drunken Technique.*** Whenever you use Flurry of Blows, you gain the benefit of the Disengage action, and your walking speed increases by 10 feet until the end of the current turn.")
```

## Tipsy Sway
*6th-level Way of the Drunken Master feature*

Your swaying in combat becomes maddeningly unpredictable. As a reaction when an enemy misses you with a melee attack roll, you can cause that attack to hit one creature of your choice, other than the attacker, that you can see within 5 feet of you. Once you use this feature, you can't use it again until you finish a short or long rest.

```
def level4(npc):
    npc.reactions.append("***Tipsy Sway (Recharges on short or long rest).*** When an enemy misses you with a melee attack roll, you can cause that attack to hit one creature of your choice, other than the attacker.")
```

## Drunkard's Luck
*11th-level Way of the Drunken Master feature*

You always seem to get a lucky bounce at just the right moment to save you from doom. When you make a saving throw, you can spend 1 ki point to give yourself advantage on that roll. You must decide to use this feature before rolling.

```
def level11(npc):
    npc.traits.append("***Ki: Drunkard's Luck.*** When you make a saving throw, you can spend 1 ki point to give yourself advantage on that roll. You must decide to use this feature before rolling.")
```

## Intoxicated Frenzy
*17th-level Way of the Drunken Master feature*

You gain the ability to make an overwhelming number of attacks against a group of enemies. When you use your Flurry of Blows, you can make up to three additional attacks with it (up to a total of five attacks), provided that each Flurry of Blows attack targets a different creature this turn.

```
def level17(npc):
    npc.actions.append("***Intoxicated Frenzy.*** When you use your Flurry of Blows, you can make up to three additional attacks with it (up to a total of five attacks), provided that each Flurry of Blows attack targets a different creature this turn.")
```
