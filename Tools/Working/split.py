#!/usr/bin/env python3

def spellprint(spell):
    print(f'#### {spell[0]}')
    print(f'*{spell[1]}* ()')
    print('___')
    print(f'- **{spell[2]}')
    print(f'- **{spell[3]}')
    print(f'- **{spell[4]}')
    print(f'- **{spell[5]}')
    print('---')
    print('\n'.join(spell[6:]))

def spellwrite(spell):
    def snakecasefilename(name):
        return name.replace(' ', '-').replace('\'', '').replace('/', '-').lower()

    with open(snakecasefilename(spell[0]) + ".md", "w") as spellfile:
        spellfile.write(f'#### {spell[0]}\n')
        spellfile.write(f'*{spell[1]}* ()\n')
        spellfile.write('___\n')
        spellfile.write(f'- **{spell[2]}\n')
        spellfile.write(f'- **{spell[3]}\n')
        spellfile.write(f'- **{spell[4]}\n')
        spellfile.write(f'- **{spell[5]}\n')
        spellfile.write('---\n')
        spellfile.write('\n'.join(spell[6:]))

elemspells = open('Blast.txt', 'r')
lines = elemspells.readlines()

spell = []
spells = []
for line in lines:
    line = line.strip()
    if line == '---':
        #spellprint(spell)
        #spells.append(spell)
        spellwrite(spell)
        spell = []
    elif line == '' and len(spell) == 0:
        pass
    else:
        spell.append(line)
