#!/bin/bash
paintGreen () {
    gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;32m" text "\033[0m"
    }'
}

paintRed () {
    gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;31m" text "\033[0m"
    }'
}

verifyJson () {
    echo $(python3 $HOME/filtering/verifyJson.py $1)
}

if [ $(verifyJson $1) == 0 ];
then
    echo "JSON validation: $(paintGreen OK)";
    exit 0;
elif [ $(verifyJson $1) == 1 ];
then
    echo "$(paintRed ERROR): not a JSON file";
    exit 1;
else
    echo "$(paintRed ERROR): invalid JSON data";
    exit 2;
fi;
