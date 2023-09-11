# Fey Elves (*eladrin*)
One of your parents was a Fey Elf. When you create this character, choose the season your parent was in when you were conceived; you cannot change this once chosen.

* **Fey Step**. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest.
  When you reach 3rd level, your Fey Step gains an additional effect based on your season; if the effect requires a saving throw, the DC equals 8 + your proficiency bonus + your Charisma modifier. The effects are as follows:

  * **Autumn**. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it.
  * **Winter**. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn.
  * **Spring**. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.
  * **Summer**. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage).

```
name = 'Fey'
description = "***Elvish Heritage: Fey Elf.*** One of your parents was a Fey Elf."
def level0(npc):
  season = choose("Choose the season:", ['Autumn', 'Winter', 'Spring', 'Summer'])
  if season == 'Autumn':
    npc.description.append("***Fey Elf Heritage: Autumn.*** Autumn is the season of peace and goodwill, when summer's harvest is shared with all. Their skin takes on a darker-brownish hue, and their hair tends to take on more of a darker orange or even brown.")
  elif season == 'Winter':
    npc.description.append("***Fey Elf Heritage: Winter.*** Winter is the season of contemplation and dolor, when the vibrant energy of the world slumbers. Their skin fades in color, taking on whitish tones, even to the point of albinism depending on how deep the contemplation they feel, and their hair tends to mirror that.")
  elif season == 'Spring':
    npc.description.append("***Fey Elf Heritage: Spring.*** Spring is the season of cheerfulness and celebration, marked by merriment as winter's sorrow passes. Their hair will often erupt into a bold color hue, such as red, green, or even blue, and their skin will often take on a greenish tinge.")
  elif season == 'Summer':
    npc.description.append("***Fey Elf Heritage: Summer.*** Summer is the season of boldness and aggression, a time of unfettered energy. Their hair will turn fire-red or blonde, and their skin may take on a bronze color.")
  else:
    print("WTF?!? " + season + " shouldn't be an option!")
  npc.season = season

  npc.bonusactions.append("***Fey Step (Recharges on short or long rest).*** You can magically teleport up to 30 feet to an unoccupied space you can see.")

def level3(npc):
    if npc.season == 'Autumn':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"You can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it. Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}."))
    elif npc.season == 'Winter':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"You can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn. Save DC = {8 + npc.proficiencybonus() + npc.CHAbonus()}."))
    elif npc.season == 'Spring':
        replace("***Fey Step", npc.bonusactions, "You can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you.")
    elif npc.season == 'Summer':
        npc.defer(lambda npc: replace("***Fey Step", npc.bonusactions, f"You can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes {npc.CHAbonus()} fire damage."))
    else:
        print("WTF?!? " + npc.season + " shouldn't be an option!")
```
