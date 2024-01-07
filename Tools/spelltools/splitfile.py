#!/usr/bin/env python3

elemspells = open('elementalspells.md', 'r')
lines = elemspells.readlines()

spellfile = None
lineslen = len(lines)
for itr in range(lineslen):
    if(lines[itr][0:2] == '# '):
        if spellfile != None:
            spellfile.close()
        spellfile = open(lines[itr][3:] + '.md')
    
    spellfile.write(lines[itr])
