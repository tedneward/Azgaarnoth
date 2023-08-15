# Tools
This directory contains a number of Python scripts/apps (they start as scripts, and slowly I'm coming to the idea that they need to become full-fledged apps, so hey, let's test how well Python "scales up" that way eh?) for managing this repo.

## Website
Converts the Markdown content to static HTML for upload to a static site host (like Site44). 

Make sure mkdocs is installed: `pip3 install mkdocs`

From within the Website directory, run `mkdocs build`, or better yet just run `bake.sh` (*nix, use WSL2 on Windows but be prepared for slow bash file perf, welcome to WSL2) and it will do the work: Erase the old work, copying the contents into the Website/docs folder (where mkdocs expects them to be) without accidentally recursing infinitely, then copying the resulting build (in the `site` folder) over to the target directory (in my Dropbox/Apps/Site44 directory) for upload. Note that by default it's going to `~/Dropbox/Apps/site44/azgaarnoth.tedneward.com`, unless there is a `sitetarget` file that contains a new target path. (Contents of that file are slurped up entirely whole, so no comments or anything allowed.)

Everything except the Tools and Supplements directory goes up into the website.

## Spelltool

## NPCGen

## CityGen

## Misc scripts

* `bookrip.py`: Starting point for slurping text content out of a PDF.
* `splitfile.py`: Hey, once we have all the text in a single file, split it into chunks. Useful for large spell lists (and, I think, creature lists, when I get there).

## FUTURE
Eventually, Spelltool, NPCGen, CityGen should all be classes/modules invoked from a master app. Maybe a Tk GUI app? Hm.

CLITool:
  --parsemd {dir}: Use Markdown as source material
  --parsesql {db}: Use SQLite db as source material
  --emitmd {dir}: Emit results (if any) to {dir} in Markdown
  --emitsql {db}: Emit results (if any) to SQLite {db}

