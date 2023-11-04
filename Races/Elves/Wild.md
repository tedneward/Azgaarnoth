# Wild Elves (*grugach*)
The *grugach* are those elves that sought to escape the world into the wilds, and for the most part, they reside almost exclusively in [North Bedia](../../Nations/Bedia.md) in the wilderness far from any civilization. Periodically, a young *grugach* will seek a different path, and venture into civilization, and these often make fierce scouts or rangers, either in partnership with druids or working on behalf of a [Mercenary Company](../../Organizations/MercCompanies/index.md), particularly in the incessant battles on [Chidia](../../Geography/Chidia.md). *Grugach* look almost identical to any other elves, and so will generally not raise an eyebrow when seen on the street or on board a ship. Other elves will note the subtle differences that mark the *grugach*, however, particularly after some close contact.

Many scholars have suggested that the *grugach* are a "devolved" form of the elves, reduced to "spears and loincloths" because they have eschewed civilization, but those who have met and walked among the *grugach* tell a very different story: the *grugach* are as fully sophisticated as any Lirian city in their society and abstract thought, choosing their simpler way of life as a way to better commune with nature and distance themselves from the pain and horror that often accompanies civilized life. Their "spears and loincloths" (which actually don't do justice to the painstakingly beautiful wooden weapons the *grugach* produce, which often are as hard and as sharp as steel or even mithral) are emblematic of their desire to operate in conjunction with nature, not subjugate it. As with most elves, they revere beauty, but see just as much beauty in the tangle of brush or the patterns of the hunt as they do music or art.

Contrary to popular belief, *grugach* do not kidnap children to live with them in the woods, and will often be wary but welcoming of visitors to their realms. A visitor who is lost in a *grugach* realm will be approached by a solitary hunter (though others will lurk, unseen, in the woods surrounding to provide aid and support should that be necessary), and the *grugach* will render aid, directions, or even provide food or shelter should the lost wanderer require it. To be invited into a *grugach* realm requires a much deeper level of trust, however, and usually is reserved only for those who demonstrate strong reverence for nature and the Balance. Rangers and druids almost always earn this trust, while other classes may have to work harder at it.

If anyone is fool enough to disturb a *grugach* realm, these elves take to arms and fight in earnest. *Grugach* master the basic weapons needed to hunt and forage in the wood, and are masters with them. Every copse of trees becomes a sniper’s nest, and each forest meadow is an ambush point. The *grugach* set pits filled with stakes, snares that leave an intruder helpless to *grugach* arrows, and other snares designed to kill rather than capture. Their arcane arts call the power of nature to their hands, and their divine connections with the Pantheonic dieties of nature visit harsh reprisal on those foolish enough to underestimate the *grugach's* ability to destroy their enemies. The *grugach* fight to the death to preserve their realms.

*Grugach* are generally neutral in ethos, seeing that nature is neither good nor evil in its own right. In fact, some of the older *grugach* believe that good and evil are concepts born of civilization, and most closely associate with the Balance and the Great Circle espoused by [Druidism](../../Religions/Druidism.md).

* **Ability Score Increase**. Your Strength score increases by 1.

* ***Grugach* Weapon Training**. You have proficiency with the spear, shortbow, longbow, and net.

* **Cantrip**. You know one cantrip of your choice from the druid spell list. Wisdom is your spellcasting ability for it.

* **Languages**. Unlike other elves, you don’t speak, read, or write Common. You instead speak, read, and write Sylvan.

```
name = 'Wild'
description = "***Subrace: Wild Elf.*** The *grugach* are those elves that sought to escape the world into the wilds. *Grugach* look almost identical to any other elves, and so will generally not raise an eyebrow when seen on the street or on board a ship. Other elves will note the subtle differences that mark the *grugach*, however, particularly after some close contact."
def level0(npc):
  npc.STR += 1

  npc.proficiencies.append("Spear")
  npc.proficiencies.append("Net")
  npc.proficiencies.append("Longbow")
  npc.proficiencies.append("Shortbow")

  spellcasting = innatecaster(npc, 'WIS', "Wild Elf")
  spellcasting.cantripsknown.append("CHOOSE-Druid")

  npc.languages.remove("Common")
  npc.languages.append("Sylvan")
```
