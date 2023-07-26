# Hobgoblins

name = 'Hobgoblin'

def apply_race(npc):
    npc.race = 'Hobgoblin'
    npc.size = 'Medium'
    npc.speed = '30 ft'

    # Ability Score Increase
    npc.CON += 2
    npc.INT += 1

    npc.features.append("**Darkvision**. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray.")
    npc.features.append("**Saving Face**. Hobgoblins are careful not to show weakness in front of their allies, for fear of losing status. If you miss with an attack roll or fail an ability check or a saving throw, you can gain a bonus to the roll equal to the number of allies you can see within 30 feet of you (maximum bonus of +5). Once you use this trait, you can't use it again until you finish a short or long rest.")

    npc.proficiencies.append('Martial weapon')
    npc.proficiencies.append('Martial weapon')
    npc.proficiencies.append('Light armor')

    npc.languages.append('Common')
    npc.languages.append('Goblin')

    npc.description.append('See the [Creatures entry on Hobgoblins](/Creatures/Hobgoblin.md) for background and details.')

subraces = []
