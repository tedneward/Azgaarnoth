#!/bin/bash

cd ../../Magic/Spells

python3 ../../Tools/spelltools/spelltool.py --parsemd . --summarymd index.md

cd ../../Classes

cd Artificer; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Artificer --summarymd SpellList.md; cd ..
cd Bard; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Bard --summarymd SpellList.md; cd ..
cd Cleric; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Cleric --summarymd SpellList.md; cd ..
cd Druid; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Druid --summarymd SpellList.md; cd ..
cd Paladin; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Paladin --summarymd SpellList.md; cd ..
cd PaleMaster; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass "Pale Master" --summarymd SpellList.md; cd ..
cd Ranger; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Ranger --summarymd SpellList.md; cd ..
cd Shaman; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Shaman --summarymd SpellList.md; cd ..
cd Sorcerer; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Sorcerer --summarymd SpellList.md; cd ..
cd Warlock; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Warlock --summarymd SpellList.md; cd ..
cd Wizard; python3 ../../Tools/spelltools/spelltool.py --parsemd ../../Magic/Spells --findclass Wizard --summarymd SpellList.md; cd ..

cd ../Tools/Website
