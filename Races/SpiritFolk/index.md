# Spirit Folk
Spirit Folk are rare descendants of humans and ancient natural spirits. These beings are a unique blend of human and elemental essence, closely attuned to the natural world. Their origins are shrouded in mystery, and their presence is most prominent in Yithi and Zhi.

Spirit Folk are known for their deep connection to the environment, their peaceful disposition, and their innate mystical abilities. Whether they hail from bamboo forests, towering mountains, meandering rivers, or the vast seas, they are a harmonious part of the world’s tapestry.

```
name = 'Spirit Folk'
description = "***Race: Spirit Folk.*** Spirit Folk are rare descendants of humans and ancient natural spirits. These beings are a unique blend of human and elemental essence, closely attuned to the natural world. Their origins are shrouded in mystery, and their presence is most prominent in Yithi and Zhi."
type = 'humanoid'
def level0(npc):
```

## Spirit Folk Traits
**Ability Score Increase.** Your Wisdom score increases by 2.

```
    npc.WIS += 2
```

**Size.** Spirit Folk vary in size, but they are generally similar to humans. Your size is Medium.

```
    npc.size = 'Medium'
```

**Speed.** Your base walking speed is 30 feet.

```
    npc.speed['walking'] = 30
```

**Languages.** You can read, write, speak, and understand Common and one additional language of your choice, typically reflecting the environment you come from.

```
    npc.languages.append('Common')
    npc.languages.append('CHOOSE')
```

**Natural Harmony.** You have proficiency in one of the following skills of your choice: Animal Handling, Medicine, Nature, or Survival.

```
    npc.skills.append(choose("Choose a skill: ", ['Animal Handling', 'Medicine', 'Nature', 'Survival']))
```

**Spiritual Affinity.** You can cast the Druidcraft cantrip as an innate magical ability. Wisdom is your spellcasting ability for it.

```
    spellcasting = innatecaster(npc, 'WIS', name)
```

**Subraces.** Choose one of the following subraces:

* [Bamboo](./Bamboo.md)
* [Mountain](./Mountain.md)
* [River](./River.md)
* [Sea](./Sea.md)

## Spirit Folk Names
Spirit Folk names often reflect their connection to nature and the elements.

Bamboo Spirit Folk Names. Chihiro, Haruki, Mei, Ren, Sora, Yuki, Zenko.

Mountain Spirit Folk Names. Daisuke, Hana, Kaito, Sakura, Taro, Yumi, Zenitsu.

River Spirit Folk Names. Akiko, Emi, Hiroshi, Kaede, Noriko, Ryuji, Yumi.

Sea Spirit Folk Names. Akira, Kaida, Makoto, Nami, Takeshi, Yori, Mizuki.

```
def generate_name(npc, gender):
    if npc.subrace.name == 'Bamboo':
        return random(['Chihiro', 'Haruki', 'Mei', 'Ren', 'Sora', 'Yuki', 'Zenko'])
    elif npc.subrace.name == 'Mountain':
        return random(['Daisuke', 'Hana', 'Kaito', 'Sakura', 'Taro', 'Yumi', 'Zenitsu'])
    elif npc.subrace.name == 'River':
        return random(['Akiko', 'Emi', 'Hiroshi', 'Kaede', 'Noriko', 'Ryuji', 'Yumi'])
    elif npc.subrace.name == 'Sea':
        return random(['Akira', 'Kaida', 'Makoto', 'Nami', 'Takeshi', 'Yori', 'Mizuki'])
```
