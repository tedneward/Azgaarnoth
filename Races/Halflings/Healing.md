# Mark of Healing
A halfling with the Mark of Healing can save a life with a touch, restoring vitality and the will to live. When dealing with mundane medicine, the mark helps its bearer sense the nature of maladies and afflictions and find the best solution. When enhanced by dragonshard focus items, the mark can even draw the dead back to life.

```
name = 'Healing Dragonmarked'
```

### Traits
The Mark of Healing manifests exclusively on halflings. If your character has the Mark of Healing, this is your halfling subrace.

```
def level0(npc):
```

* **Ability Score Increase**. Your Wisdom score increases by 1.

```
    npc.WIS += 1
```

* **Medical Intuition**. When you make a Wisdom (Medicine) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.

```
    npc.traits.append("***Medical Intuition.*** When you make a Wisdom (Medicine) check, you can roll one Intuition die, a d4, and add the number rolled to the ability check.")
```

* **Healing Touch**. As an action, you can draw power from your dragonmark to spend one of your Hit Dice and revitalize yourself or a creature you touch. Roll the die, add your Wisdom modifier, and the creature regains a number of hit points equal to the total. Once you use this trait, you can’t use it again until you finish a short or long rest.

```
    npc.defer(lambda npc: npc.actions.append(f"***Healing Touch (Recharges on short or long rest).*** You can draw power from your dragonmark to spend one of your Hit Dice (plus {self.WISbonus()}) and a creature (either yourself or another within reach) regains that number of hit points."))
```

* **Jorasco’s Blessing**. You know the cantrip [spare the dying](../Magic/Spells/spare-the-dying.md). Wisdom is your spellcasting ability for this.

```
    npc.cantripsknown.append('spare the dying')
```
