#!/bin/bash

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