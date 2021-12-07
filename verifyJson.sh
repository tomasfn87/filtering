#!/bin/bash

toGreen () {
  gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;32m" text "\033[0m"
  }'
}

toRed () {
  gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;31m" text "\033[0m"
  }'
}

verifyJson () {
  echo $(python3 $HOME/filtering/verifyJson.py $1)
}

echo -n " * Checking if source file exists...    "
if [ -f $1 ];
then
  echo "[$(toGreen OK)]";
else
  echo "$(toRed ERROR): file not found"
  exit 3;
fi;

echo -n " * Checking if source filed is JSON...  " 
if [ $(verifyJson $1) == 0 ];
then
  echo "[$(toGreen OK)]";
  exit 0;
elif [ $(verifyJson $1) == 1 ];
then
  echo "$(toRed ERROR): not a JSON file";
  exit 1;
else
  echo "$(toRed ERROR): invalid JSON data";
  exit 2;
fi;
