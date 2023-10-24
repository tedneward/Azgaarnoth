mkdir testresults

for i in tests/*.npc
do
  echo Testing $i
  ./npcbuilder.py $i
  NPCFILE="$(basename $i)"
  echo Saving off $NPCFILE
  mv output.md testresults/$NPCFILE.md
done
