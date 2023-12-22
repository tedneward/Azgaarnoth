#!/bin/bash

./clean.sh

./copycontent.sh

./genCreatureLists.sh
./genSpellLists.sh

./mkdocs.sh

./uploadToDropbox.sh
