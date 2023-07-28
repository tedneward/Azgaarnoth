"""
# Minotaurs
Born the strongest of the [Hordes](Hordes.md), minotaurs swiftly discovered that they had no love of leadership or organization, and swiftly moved to either take what was theirs by right, or by force, and soon separated from the rest into their own clans. They could be brought out to join the Hordes in battle as a clan if persuaded by the right amounts of tribute, treasure, or other offerings, and many believe the minotaur clans were the first [Mercenary Companies](/Organizations/MercCompanies/MercCompanies.md). (In fact, several mercenary companies are either made up entirely out of a minotaur clan, or feature minotaurs prominently in the leadership structure today.)

Minotaurs found in [Yithi](/Nations/Yithi.md) and (less often) [Zhi](/Nations/Zhi.md) are quite strikingly different from their Horde-homed brethren, frequently solitary, thoughtful, and quite committed to rule of law and order.

Minotaurs are often drawn to the more martial classes, such as fighter or barbarian, but minotaurs are found within all of the classes.

## Culture
Minotaurs embrace the notion that the weak should perish and that the strong must rule—=and that they themselves are the strongest and most powerful race in Azgaarnoth. They believe their destiny is to rule the world, and that their dominion will be one of conquest and military might. To that end, all minotaurs are trained in weapons, armor, and tactics from a young age. The minotaurs' arrogance stems from a combination of strength, cunning, and intellect—-three virtues they hold dear, and which they deem the foundation of their greatness. They believe that this combination of traits is what sets them apart from their rivals.

## Honor Above All
For all their cruelty, minotaurs are bound by a powerful sense of honor. Each victory brings greater honor to both individual minotaurs and their families. Defeat invokes a stain that only death can fully wash away.

Honor demands that minotaurs keep their word once it is offered, and each minotaur remains faithful to friends and clan above all else. Minotaurs rarely befriend folk of other races, as they all too often encounter them only in battle. If a minotaur does strike up a friendship, it is typically with other creatures that display the minotaurs' virtues and love of battle. To such friends, a minotaur becomes an ally whose support will never waver.

## Names
Minotaur clan names originate with a great hero whose descendants take on that name as their own, doing their best to live up to the ideals of their ancestor.

**Male Names**: Beliminorgath, Cinmac, Dastrun, Edder, Galdar, Ganthirogani, Hecariverani, Kyris, Tosher, Zurgas

**Female Names**: Ayasha, Calina, Fliara, Helati, Keeli, Kyri, Mogara, Sekra, Tariki, Telia

**Clan Names**: Athak, Bregan, Entragath, Kaziganthi, Lagrangli, Mascun, Orilg, Sumarr, Teskos, Zhakan

## Traits
* **Ability Score Increase**. Your Strength score increases by 2, and your Constitution score increases by 1.

* **Age**. Minotaurs enter adulthood at around the age of 17 and can live up to 150 years.

* **Size**. Minotaurs typically stand well over 6 feet tall and weigh an average of 300 pounds. Your size is Medium.

* **Speed**. Your base walking speed is 30 feet.

* **Horns**. You are never unarmed. You are proficient with your horns, which are a melee weapon that deals 1d6 + your Strength modifier piercing damage. Your horns grant you advantage on all checks made to shove a creature, but not to avoid being shoved yourself.

* **Goring Rush**. When you use the Dash action during your turn, you can make a melee attack with your horns as a bonus action.

* **Hammering Horns**. When you use the Attack action during your turn to make a melee attack, you can attempt to shove a creature with your horns as a bonus action. You cannot use this shove attempt to knock a creature prone.

* **Menacing.** You	have proficiency in the Intimidation skill. 

* **Languages**. You can speak, read, and write Common.

* **Alignment**. Minotaurs believe in a strict code of honor, and thus tend toward law. They are loyal to the death and make implacable enemies, even as their brutal culture and disdain for weakness push them toward evil.

* **Hybrid Nature**. You have two creature types: humanoid and monstrosity. You can be affected by a game effect if it works on either of your creature types.

## Subraces / Variants

### Sea Reaver
The Sea Reaver minotaurs are those minotaurs who, early in the Hordes' existence, took to the sea as sailors, pirates, and merchants. They found a love for the sea that balanced against their love of order, and never looked back. Bound by the sea on all sides, the minotaurs focused their tenacity, strength, and cunning to become some of the most skilled and ferocious mariners in the world. They range across the water in their ships, raiding and pillaging as they wish. Sea Reavers sometimes engage in trade, but they much prefer to take what they want by force. After all, as the strongest of all folk, they deserve the treasures and goods that lesser creatures have gathered.

Some Sea Reavers have found that there is more gain to be had from trade than pillage, but they are often set upon by their fellow minotaurs for weakness. Many Sea Reavers have found employ within the various [Merchant Guilds](/Organizations/MerchantGuilds/MerchantGuilds.md) as both escorts and privateers, and many a Sea Reaver has combined the two activities in one trip.

Sea Reavers have the following additional features:

* **Sailor**. You gain proficiency with navigator's tools and vehicles (water).

### Marshal
Marshal minotaurs are those minotaurs within [Yithi](/Nations/Yithi.md) and [Zhi](/Nations/Zhi.md) that have chosen to take up a life of civilization and enforcing the law. They form a loose network of roaming adjudicators and magistrates, often dispensing rough justice in places where bringing a criminal to trial would be problematic or impossible. They will frequently work together when the time arises, may demand logistical support of any governor, and are always well-equipped. Many minotaur Marshals are paladins.

Marshals have the following additional features:

* **Magistrate**. You have deep knowledge of the law. Additionally, while within the borders of your home nation, you have the resources of the Court to draw upon for equipment, including small numbers of common magic items (if the GM deems it available in the city or township).

*Source: [Unearthed Arcana: Centaurs and Minotaurs](https://dnd.wizards.com/articles/unearthed-arcana/centaurs-and-minotaurs)*
"""
name = 'Minotaur'
def apply_race(npc):
    npc.size = 'Medium'
    npc.speed = '30 ft'

    # Ability Score Increase
    npc.STR += 2
    npc.CON += 1

    npc.skills.append("Intimidation")

    npc.languages.append("Common")

    npc.actions.append("*Horns**. You are proficient with your horns, which are a melee weapon that deals 1d6 + your Strength modifier piercing damage. Your horns grant you advantage on all checks made to shove a creature, but not to avoid being shoved yourself.")

    npc.bonusactions.append("**Goring Rush**. When you use the Dash action during your turn, you can make a melee attack with your horns as a bonus action.")
    npc.bonusactions.append("**Hammering Horns**. When you use the Attack action during your turn to make a melee attack, you can attempt to shove a creature with your horns as a bonus action. You cannot use this shove attempt to knock a creature prone.")

subraces = []
