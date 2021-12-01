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

if [[ $2 == "" || $2 == " " ]]
then
    echo "$(toRed ERROR): please specify minified JSON path";
    exit 5;
fi;

if [ $2 == $1 ];
then
    echo "$(toRed ERROR): source file and output file cannot be the same"
    exit 3;
fi;

if [ $(verifyJson $2) == 1 ];
then
    echo "$(toRed ERROR): output minified JSON file extension must be '.json'";
    exit 4;
fi;
touch $2;

echo -n "Checking JSON file integrity... ";

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
    echo "$(toGreen OK)"; 
fi;

echo -n "Minifying JSON file..."
python3 $HOME/filtering/minify.py $1 | cat > $2;
echo "$(toGreen DONE)";
echo "File saved to:";
echo "$(toYellow $2)";

echo -n "Checking '$2'..."
if [ $(verifyJson $2) != 0 ];
then
    echo "$(toRed ERROR)"
    echo "Minified JSON validation failed";
else
    echo "$(toGreen OK)";
fi;
exit 0;
