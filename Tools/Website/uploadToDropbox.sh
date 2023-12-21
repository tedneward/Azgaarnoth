#!/bin/bash

# Upload it (via Dropbox)
target=~/Dropbox/Apps/site44/azgaarnoth.tedneward.com/
if test -f "sitetarget"; then
  target=`cat sitetarget`
fi

echo "Copying site to $target..."
cp -Rv site/* $target
