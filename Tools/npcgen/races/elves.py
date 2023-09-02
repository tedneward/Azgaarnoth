name = 'Elf'
def apply_race(npc):
    npc.description.append("***Race: Elf.*** Elves are almost as diverse as humans in their occupations, entertainments, and while most elves have a strong familial tie between them, numerous elves have wandered away from home to make their mark within the world, then to return and take up familial responsibilities. Elves revere their familial ancestors, and will often have a shrine to a favored ancestor, but elves do not see their familial ancestors as gods, and many elves are quite comfortable serving in a religious order even as they put offerings to their revered ancestors out on important holidays.\nElvish personalities are as diverse as any other race, but owing to their longer lifespan, most elves take a longer view of things and prefer to plan before acting; however, some (like the *eladrin*) embrace the chaotic nature of the world, believing that to try and predict nature is to go against nature. Most elves have a long sense of history and their connection to the world, and many elves know their ancestral history back several generations--which, given their lifespans, can stretch for up to thousands of years. For this reason, elves are often seen as lorekeepers and sources of wisdom and insight, which some use unscrupulously to their advantage.")

    npc.DEX += 2

    npc.size = 'Medium'
    npc.speed = '30 ft'

    npc.features.append(commonfeatures['darkvision'])

    npc.features.append("***Fey Ancestry.*** You have advantage on saving throws against being charmed, and magic can't put you to sleep.")

    npc.conditionimmunities.append("sleep")

    npc.features.append("***Trance.*** Elves do not sleep. Instead they meditate deeply, remaining semi-conscious, for 4 hours a day. The Common word for this meditation is \"trance\". While meditating, you dream after a fashion; such dreams are actually mental exercises that have become reflexive after years of practice. After resting in this way, you gain the same benefit a human would from 8 hours of sleep.")

    npc.skills.append("Perception")

    npc.languages.append("Common")
    npc.languages.append("Elven")

def bright(npc):
  npc.description.append("***Bright Elf.*** The bright elves are one of the oldest and rarest subraces of elves, and thanks to their long years of close association with the Eldar they have an innate connection to the celestial light and song of creation. They are more lawful than other elven societies, and they value obedience as well as conformity. Many bright elves believe themselves to be the purest and most original form of elf, and see other elven subraces as little better than non-elves, but others among their ranks  are more accepting, often chiding their haughtier peers and worrying that such thinking is what led to the Fall.\nAs a bright elf, your body and soul are infused with light. A bright elf's skin is bronze, silvery, pearly, or pale white, and their hair is golden blond, platinum blond, or silvery white. Their eyes are usually golden or silvery gray, with streaks of white radiating from their pupils like a starburst.")

  asi = choose("Choose an ability score increase:", ['STR', 'CON', 'INT', 'WIS', 'CHA'])

  if asi == 'STR': 
    npc.STR += 1
  elif asi == 'CON': 
   npc.CON += 1
  elif asi == 'INT': 
   npc.INT += 1
  elif asi == 'WIS': 
   npc.WIS += 1
  elif asi == 'CHA': 
   npc.CHA += 1

  cantrip = choose("Choose a cantrip:", ['light', 'dancing lights', 'thaumaturgy'])
  npc.cantripsknown.append(cantrip)
  npc.features.append("***Ancient Magic.*** You know " + spelllinkify(cantrip) + " and Charisma is your spellcasting ability for it.")

  npc.features.append("***Brightfolk.*** You have advantage on saving throws to resist being blinded by effects that deal radiant damage or create light.")
  npc.resistance.append('radiant')

  npc.features.append("***Celestial Nature.*** You have two creature types: humanoid and celestial You can be affected by a game effect if it works on either of your creature types.")

def high(npc):
  npc.description.append("***High Elf.*** High elves and wood elves are, by this point in Azgaarnoth's history, fairly well intermixed and are found in most locations all across Azgaarnoth; at this point in their evolution, no non-elf can tell the difference between them.")

  npc.INT += 1

  npc.features.append("***Cantrip.*** You know one cantrip of your choice from the Wizard spell list. Intelligence is your spellcasting ability for it.")

  npc.proficiencies.append("Longsword")
  npc.proficiencies.append("Shortsword")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.languages.append("(Choice)")

def wood(npc):
  npc.description.append("***Wood Elf.*** Wood elves and high elves are, by this point in Azgaarnoth's history, fairly well intermixed and are found in most locations all across Azgaarnoth; at this point in their evolution, no non-elf can tell the difference between them.")

  npc.WIS += 1

  npc.proficiencies.append("Longsword")
  npc.proficiencies.append("Shortsword")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.speed = '35 ft'

  npc.features.append("***Mask of the Wild.*** You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena.")

def winged(npc):
  npc.description.append("***Winged Elf.*** The *avariel* are generally lighter in stature and size, often up to a full foot shorter than the average high or wood elf, and much lither of form. Their wings can be folded to curl up close to their backs, which if covered with clothing, could allow them to pass for another form of elf, though not under any sort of detailed scrutiny. (Most *avariel* don't like hiding their wings anyway, feeling it to be constricting and claustrophobic.) Generally they wear light clothing, though when flying at high altitudes will wrap themselves in furs or other insulating clothing to help with the chill of the high altitudes.")

  npc.speed += "30ft flying (without medium or heavy armor)"

  npc.languages.append('Auran')

def wild(npc):
  npc.description.append("***Wild Elf.*** The *grugach* are those elves that sought to escape the world into the wilds. *Grugach* look almost identical to any other elves, and so will generally not raise an eyebrow when seen on the street or on board a ship. Other elves will note the subtle differences that mark the *grugach*, however, particularly after some close contact.")

  npc.STR += 1

  npc.proficiencies.append("Spear")
  npc.proficiencies.append("Net")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  npc.features.append("***Cantrip***. You know one cantrip of your choice from the Druid spell list. Wisdom is your spellcasting ability for it.")

  npc.languages.remove("Common")
  npc.languages.append("Sylvan")

def sea(npc):
  npc.description.append("***Sea Elf.*** *Maerach* look strikingly similar to elves, aside from a small set of gills set just below their ears, which long hair (worn loosely) can usually hide.")

  npc.CON += 1

  npc.proficiencies.append("Spear")
  npc.proficiencies.append("Trident")
  npc.proficiencies.append("Light crossbow")
  npc.proficiencies.append("Net")

  npc.features.append(commonfeatures['sea-emissary'])
  npc.features.append(commonfeatures['amphibious'])
  npc.speed += '; 30ft swimming'

  npc.languages.append('Aquan')

def shadow(npc):
  npc.description.append("***Shadow Elf.*** These elves, the *shadar-kai*, remain a mystery even to their kin--their origins are lost, their homes are undiscovered, and their motives and allegiances are absolutely indiscernible. Individual *shadar-kai* have been seen wandering the world, identifiable more by their piercings and tatoos than anything else, leaving many to wonder if other *shadar-kai*, unpierced and untattooed, also wander the world--and why. *Eladrin* and *shadar-kai* are like reflections of each other: one bursting with emotion, the other nearly devoid of it.")

  npc.CON += 1

  npc.resistances.append('necrotic')

  npc.bonusactions.append("***Blessing of the Raven Queen***. As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a long rest.")

def dark(npc):
  npc.description.append("***Dark Elf.*** Elvish scholars speak of an ancient schism amongst the Eldar--and some insist that this was the start of the Fall--that prompted an offshoot of the Eldar to take refuge underground. Rumors hold that these dark elves, the *drow*, are the reason (somehow) Mt Bezulb continues to erupt consistently. Note that despite numerous claims to the contrary, *drow* and *shadar-kai* are not the same race, and in fact they seem to have an inborn implacable hatred of one another that defies explanation.")

  npc.CHA += 1

  npc.cantripsknown.append('dancing lights')

  npc.proficiencies.append('Rapier')
  npc.proficiencies.append('Shortsword')
  npc.proficiencies.append('Hand crossbow')

  npc.features.append(commonfeatures['superiordarkvision'])
  npc.features.append(commonfeatures['sunlight-sensitivity'])

def fey(npc):
  npc.description.append("**Fey Elves.** The *eladrin* are elves native to the Feywild, a realm of beauty, unpredictable emotion, and boundless magic. They are most often found in the wilds of [North Bedia](/Nations/Bedia.md), or on any of the scattered islands around Azgaarnoth. Intriguingly, they are also commonly found in the lands of the [Hordes](/Races/Hordes.md), without being forced into extensive combat against their neighbors.")

  season = choose("Choose the season association:", ['Autumn', 'Winter', 'Spring', 'Summer'])
  if season == 'Autumn':
    npc.description.append("***Season.*** Autumn is the season of peace and goodwill, when summer's harvest is shared with all. Their skin takes on a darker-brownish hue, and their hair tends to take on more of a darker orange or even brown.")
  elif season == 'Winter':
    npc.description.append("***Season.*** Winter is the season of contemplation and dolor, when the vibrant energy of the world slumbers. Their skin fades in color, taking on whitish tones, even to the point of albinism depending on how deep the contemplation they feel, and their hair tends to mirror that.")
  elif season == 'Spring':
    npc.description.append("***Season.*** Spring is the season of cheerfulness and celebration, marked by merriment as winter's sorrow passes. Their hair will often erupt into a bold color hue, such as red, green, or even blue, and their skin will often take on a greenish tinge.")
  elif season == 'Summer':
    npc.description.append("***Season.*** Summer is the season of boldness and aggression, a time of unfettered energy. Their hair will turn fire-red or blonde, and their skin may take on a bronze color.")
  else:
    print("WTF?!? " + season + " shouldn't be an option!")
  npc.season = season

  npc.CHA += 1
  npc.bonusactions.append("***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Once you use this trait, you can't do so again until you finish a short or long rest.")

subracemap = {
  'Bright' : bright,
  'High' : high,
  'Wood' : wood,
  'Winged' : winged,
  'Wild' : wild,
  'Sea' : sea,
  'Dark' : dark,
  'Shadow' : shadow,
  'Fey' : fey
}
subraces = list(subracemap.keys())
def apply_subrace(npc, which):
  npc.subrace = which
  subracemap[which](npc)

def level3(npc):
  if (npc.subrace == 'Fey'):
    if npc.season == 'Autumn':
      replace("***Fey Step.***", npc.bonusactions, "***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, up to two creatures of your choice that you can see within 10 feet of you must succeed on a Wisdom saving throw or be charmed by you for 1 minute, or until you or your companions deal any damage to it. Save DC equals 8 + your proficiency bonus + your Charisma modifier. Once you use this trait, you can't do so again until you finish a short or long rest.")
    elif npc.season == 'Winter':
      replace("***Fey Step.***", npc.bonusactions, "***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, one creature of your choice that you can see within 5 feet of you before you teleport must succeed on a Wisdom saving throw or be frightened of you until the end of your next turn. Save DC equals 8 + your proficiency bonus + your Charisma modifier. Once you use this trait, you can't do so again until you finish a short or long rest.")
    elif npc.season == 'Spring':
      replace("***Fey Step.***", npc.bonusactions, "***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. When you use your Fey Step, you can touch one willing creature within 5 feet of you. That creature then teleports instead of you, appearing in an unoccupied space of your choice that you can see within 30 feet of you. Once you use this trait, you can't do so again until you finish a short or long rest.")
    elif npc.season == 'Summer':
      replace("***Fey Step.***", npc.bonusactions, "***Fey Step.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. Immediately after you use your Fey Step, each creature of your choice that you can see within 5 feet of you takes fire damage equal to your Charisma modifier (minimum of 1 damage). Once you use this trait, you can't do so again until you finish a short or long rest.")
    else:
      print("WTF?!? " + npc.season + " shouldn't be an option!")
  elif (npc.subrace == 'Dark'):
    npc.features.append("**Dark Elf Magic.** You can cast " + spelllinkify('faerie fire') + " once, and it recharges after a long rest. Charisma is your spellcasting ability for this spell.")
  elif (npc.subrace == 'Shadow'):
    replace("***Blessing of the Raven Queen.***", npc.bonusactions, "***Blessing of the Raven Queen.*** As a bonus action, you can magically teleport up to 30 feet to an unoccupied space you can see. When you do, you also gain resistance to all damage when you teleport using this trait. The resistance lasts until the start of your next turn. During that time, you appear ghostly and translucent. Once you use this trait, you can't do so again until you finish a long rest.")

def level5(npc):
  if (npc.subrace == 'Dark'):
    replace("**Dark Elf Magic.**", npc.features, "**Dark Elf Magic.** You can cast " + spelllinkify('faerie fire') + " or " + spelllinkify('darkness') + " once, and it recharges after a long rest. Charisma is your spellcasting ability for these spells.")


