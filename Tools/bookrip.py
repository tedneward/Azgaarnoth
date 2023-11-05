#!/usr/bin/env python3

import os
import sys
from pypdf import PdfReader

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

print(sys.argv)
pdfFileObj = open(sys.argv[1], 'rb')
pdfReader = PdfReader(pdfFileObj)

start = 0
if len(sys.argv) > 2:
    start = int(sys.argv[2])
print("Starting at " + str(start))

stop = len(pdfReader.pages)
if len(sys.argv) > 3:
    stop = int(sys.argv[3])
print("Stopping at " + str(stop))
    
line = 0
lines = []
spellbreaks = []
pagect = start
while pagect < stop:
    pagetext = pdfReader.pages[pagect].extract_text()
    lines += pagetext.splitlines()
    print(pagect)
    pagect += 1

for l in lines:
    print(l)
