#!/usr/bin/env python3
import os

"""
Quick and dirty tool to split the single-file Feats.md into a whole directory of individual Feat files
and then create an markdown index.md to each of those files. It's served its purpose, but hanging on 
to it mostly for nostalgia's sake.
"""

featsroot = '../Feats'
entries = os.listdir(featsroot)
feats = { }
for c in range(ord('A'), ord('Z')+1):
   feats[chr(c)] = []

for f in entries:
    entry = featsroot + "/" + f

    excludedentries = [ 'index.md' ]
    
    if os.path.basename(entry)[-3:] == '.md' and (os.path.basename(entry) not in excludedentries):
        with open(entry, 'r') as featfile:
            name = featfile.readline().strip()[3:]
            print("Found " + name + " in " + entry)

            feats[name[0]].append(f"[{name}]({os.path.basename(entry)})")

with open('../Feats/index.md', 'w') as indexfile:
    indexfile.write("# Master Index of Feats\n")
    indexfile.write("\n")
    for key in feats.keys():
        indexfile.write(f"#### {key}\n")
        indexfile.write(" | ".join(feats[key]) + "\n\n")


def oldmain():
    with open("../Feats/index.md", 'r') as indexfile:
        lines = indexfile.readlines()

        linect = 0
        featbuffer = []
        while linect < len(lines):
            line = lines[linect]
            if line[0:2] == '##' and len(featbuffer) > 0:
              featname = (featbuffer[0][3:]).strip().replace(' ', '')
              featfilename = "../Feats/" + featname + ".md"
              print("Writing out " + featfilename + ":" + str(featbuffer))
              with open("../Feats/" + featfilename, 'w') as featfile:
                  featfile.writelines(featbuffer)
              featbuffer = []
            else:
              featbuffer.append(line)
              linect += 1
