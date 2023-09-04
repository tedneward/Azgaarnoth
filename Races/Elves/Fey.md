# Fey Elves (*eladrin*)
The *eladrin* are elves native to the Feywild, a realm of beauty, unpredictable emotion, and boundless magic.  They are most often found in the wilds of [North Bedia](../../Nations/Bedia.md), or on any of the scattered islands around Azgaarnoth. Intriguingly, they are also commonly found in the lands of the [Hordes](../index.md#hordes), without being forced into extensive combat against their neighbors.

An *eladrin* is associated with one of the four seasons and has coloration reminiscent of that season, which can also affect the *eladrin*'s mood:

* **Autumn** is the season of peace and goodwill, when summer's harvest is shared with all. Your skin takes on a darker-brownish hue, and your hair tends to take on more of a darker orange or even brown.
* **Winter** is the season of contemplation and dolor, when the vibrant energy of the world slumbers. Your skin fades in color, taking on whitish tones, even to the point of albinism depending on how deep the contemplation you feel, and your hair tends to mirror that.
* **Spring** is the season of cheerfulness and celebration, marked by merriment as winter's sorrow passes. Your hair will often erupt into a bold color hue, such as red, green, or even blue, and your skin will often take on a greenish tinge.
* **Summer** is the season of boldness and aggression, a time of unfettered energy. Your hair will turn fire-red or blonde, and your skin may take on a bronze color.

Some *eladrin* remain associated with a particular season for their entire lives, whereas other eladrin transform, adopting characteristics of a new season.

* **Ability Score Increase**. Your Charisma score increases by 1.

* **Fey Step**. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest.
  When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Charisma modifier. The effects are as follows:

  * **Autumn**. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it.
  * **Winter**. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.
  * **Spring**. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.
  * **Summer**. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage).

  When finishing a long rest, any *eladrin* can change their season. An *eladrin* might choose the season that is present in the world or perhaps the season that most closely matches the *eladrin*'s current emotional state. For example, an *eladrin* might shift to autumn if filled with contentment, another *eladrin* could change to winter if plunged into sorrow, still another might be bursting with joy and become an *eladrin* of spring, and fury might cause an *eladrin* to change to summer.

```
name = 'Fey'
def level0(npc):
  npc.description.append("***Subrace: Fey Elves.*** The *eladrin* are elves native to the Feywild, a realm of beauty, unpredictable emotion, and boundless magic. They are most often found in the wilds of [North Bedia](http://azgaarnoth.tedneward.com/Nations/Bedia.md), or on any of the scattered islands around Azgaarnoth. Intriguingly, they are also commonly found in the lands of the [Hordes](http://azgaarnoth.tedneward.com/Races/index.md#hordes), without being forced into extensive combat against their neighbors.")

  season = choose("Choose the season association:", ['Autumn', 'Winter', 'Spring', 'Summer'])
  if season == 'Autumn':
    npc.description.append("***Fey Elf Season: Autumn.*** Autumn is the season of peace and goodwill, when summer's harvest is shared with all. Their skin takes on a darker-brownish hue, and their hair tends to take on more of a darker orange or even brown.")
  elif season == 'Winter':
    npc.description.append("***Fey Elf Season: Winter.*** Winter is the season of contemplation and dolor, when the vibrant energy of the world slumbers. Their skin fades in color, taking on whitish tones, even to the point of albinism depending on how deep the contemplation they feel, and their hair tends to mirror that.")
  elif season == 'Spring':
    npc.description.append("***Fey Elf Season: Spring.*** Spring is the season of cheerfulness and celebration, marked by merriment as winter's sorrow passes. Their hair will often erupt into a bold color hue, such as red, green, or even blue, and their skin will often take on a greenish tinge.")
  elif season == 'Summer':
    npc.description.append("***Fey Elf Season: Summer.*** Summer is the season of boldness and aggression, a time of unfettered energy. Their hair will turn fire-red or blonde, and their skin may take on a bronze color.")
  else:
    print("WTF?!? " + season + " shouldn't be an option!")
  npc.season = season

  npc.CHA += 1
  npc.bonusactions.append("***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see.")

def level3(npc):
    if npc.season == 'Autumn':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it. Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}."))
    elif npc.season == 'Winter':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn. Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}."))
    elif npc.season == 'Spring':
        replace("***Fey Step", npc.bonusactions, "***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.")
    elif npc.season == 'Summer':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes {npc.CHAbonus()} fire damage."))
    else:
        print("WTF?!? " + npc.season + " shouldn't be an option!")
```
