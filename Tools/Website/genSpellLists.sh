#!/bin/bash

cd ../../Magic/Spells

python3 ../../Tools/spelltool.py --parsemd . --listmd all > ../../Tools/Website/docs/Magic/Spells/index.md

cd ../../Classes

cd Artificer; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Artificer > ../../Tools/Website/docs/Classes/Artificer/SpellList.md; cd ..
cd Bard; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Bard > ../../Tools/Website/docs/Classes/Bard/SpellList.md; cd ..
cd Cleric; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Cleric > ../../Tools/Website/docs/Classes/Cleric/SpellList.md; cd ..
cd Druid; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Druid > ../../Tools/Website/docs/Classes/Druid/SpellList.md; cd ..
cd Paladin; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Paladin > ../../Tools/Website/docs/Classes/Paladin/SpellList.md; cd ..
cd PaleMaster; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd "Pale Master" > ../../Tools/Website/docs/Classes/PaleMaster/SpellList.md; cd ..
cd Ranger; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Ranger > ../../Tools/Website/docs/Classes/Ranger/SpellList.md; cd ..
cd Shaman; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Shaman > ../../Tools/Website/docs/Classes/Shaman/SpellList.md; cd ..
cd Sorcerer; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Sorcerer > ../../Tools/Website/docs/Classes/Sorcerer/SpellList.md; cd ..
cd Warlock; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Warlock > ../../Tools/Website/docs/Classes/Warlock/SpellList.md; cd ..
cd Wizard; python3 ../../Tools/spelltool.py --parsemd ../../Magic/Spells --listmd Wizard > ../../Tools/Website/docs/Classes/Wizard/SpellList.md; cd ..

cd ../Tools/Website
