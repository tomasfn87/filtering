#!/bin/bash

toGreen () { gawk -v text=$1 'BEGIN {
  printf "%s", "\033[1;32m" text "\033[0m" }' 
}

toRed () { gawk -v text=$1 'BEGIN {
  printf "%s", "\033[1;31m" text "\033[0m" }'
}

toYellow () { gawk -v text=$1 'BEGIN {
  printf "%s", "\033[1;33m" text "\033[0m" }'
}

verifyJson () {
  echo $(python3 $HOME/filtering/verifyJson.py $1)
}

INPUT="$1";
OUTPUT="$2";
NEW_FILE=maybe;

if [ $2 == $1 ];
then
  echo "$(toRed ERROR): source file and output file cannot be the same"
  exit 3;
fi;

echo -n " * Checking if source file exists...    "
if [ -f $1 ];
then
  echo "[$(toGreen OK)]";
else
  echo "$(toRed ERROR): file not found"
  exit 6;
fi;

echo -n " * Checking source file integrity...    ";
if [ $(verifyJson $1) == 1 ];
then
  echo "$(toRed ERROR)";
  echo "Not a JSON file; please choose a JSON file ('file.json')";
  exit 1;
elif [ $(verifyJson $1) == 2 ];
then 
  echo "$(toRed ERROR)";
  echo "Invalid JSON data; please choose a valid JSON file";
  exit 2;
else
  echo "[$(toGreen OK)]"; 
fi;

if [[ $2 == "" || $2 == " " ]]
then
  echo "$(toRed ERROR): please specify minified JSON path";
  exit 5;
fi;

echo -n " * Checking if target file exists...    "
if [ -f $2 ];
then
  echo "[$(toGreen OK)] File will be overwritten...";
else
  touch $2;
  NEW_FILE=yes
  echo "[NO] File will be created..."
fi;

echo -n " * Checking target file extension...    "
if [ $(verifyJson $2) == 1 ];
then
  echo "$(toRed ERROR)";
  echo "Target file extension must be '.json'"
  if [ $NEW_FILE == yes ];
  then 
    rm $2;
    exit 4;
  fi;
else
  echo "[$(toGreen OK)]";  
fi;

echo -n " * Minifying JSON file...               "
python3 $HOME/filtering/minify.py $1 | cat > $2;
echo "[$(toGreen OK)]";

echo -n " * Checking output file...              "
if [ $(verifyJson $2) != 0 ];
then
  echo "$(toRed ERROR)"
  echo "Minified JSON validation failed";
else
  echo "[$(toGreen OK)]";
  echo; echo "File saved to $(toYellow $(realpath $OUTPUT))";
fi;
exit 0;
