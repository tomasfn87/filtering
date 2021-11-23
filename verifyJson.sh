#!/bin/bash
OK () {
    gawk -F ":" '
    BEGIN {
    printf "%s", "\033[1;32m" "OK" "\033[0m"
    } '
}

ERROR () {
    gawk -F ":" '
    BEGIN {
    printf "%s", "\033[31m" "ERROR" "\033[0m"
    } '
}

verifyJson () {
    echo $(python3 $HOME/filtering/verifyJson.py $1)
}

if [ $(verifyJson $1) == 0 ];
then
    echo "JSON validation: $(OK)";
    exit 0;
elif [ $(verifyJson $1) == 1 ];
then
    echo "$(ERROR): not a JSON file";
    exit 1;
else
    echo "$(ERROR): invalid JSON data";
    exit 2;
fi;
