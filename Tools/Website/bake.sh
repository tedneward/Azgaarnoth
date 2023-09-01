#!/bin/bash

# Clean up from previous runs, if any
rm -r docs
rm -r site

# Copy content into `docs`
mkdir docs
for i in ../../*
do
  if [ $i != "../../Tools" ] && [ $i != "../../Supplements" ]
  then
    if [ -d $i ]
    then
      # Get directory name out of i, mkdir it in docs
      DIR="$(basename $i)"
      echo $DIR
      mkdir docs/$DIR
      cp -r $i/* docs/$DIR
    else
      cp $i docs
    fi
  fi
done

# Convert it
mkdocs build

# Upload it (via Dropbox)
target="~/Dropbox/Apps/site44/azgaarnoth.tedneward.com"
if test -f "sitetarget"; then
  target=`cat sitetarget`
fi

echo "Copying site to $target..."
cp -r site/* $target
