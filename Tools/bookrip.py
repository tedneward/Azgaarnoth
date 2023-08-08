#!/usr/bin/env python3

import os
import sys
from PyPDF2 import PdfReader

def spellprint(spell):
    print(f'# {spell[0]}')
    print(f'*{spell[1]}* ()')
    print('___')
    print(f'- **{spell[2]}')
    print(f'- **{spell[3]}')
    print(f'- **{spell[4]}')
    print(f'- **{spell[5]}')
    print('---')
    print('\n'.join(spell[6:]))


pdfFileObj = open('The_Elemental_Spellbook_v1.0.pdf', 'rb')
pdfReader = PdfReader(pdfFileObj)
page = 3
line = 0
lines = []
spellbreaks = []
while page < len(pdfReader.pages):
    pagetext = pdfReader.pages[page].extract_text()
    lines += pagetext.splitlines()
    page += 1

for l in lines:
    if l[0:len('Casting Time: ')] == 'Casting Time: ':
        spellbreaks.append(line - 2)
    line += 1

i = 0
start = 0
end = 0
spells = []
while i < len(spellbreaks):
    end = spellbreaks[i]
    spell = lines[start:end]
    spellprint(spell)
    start = end
    i += 1

