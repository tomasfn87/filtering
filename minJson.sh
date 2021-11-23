#!/bin/bash
OK () {
    gawk -F ":" '
    BEGIN {
    printf "%s", "\033[1;32m" "OK" "\033[0m"
    } '
}

DONE () {
    gawk -F ":" '
    BEGIN {
    printf "%s", "\033[1;32m" "DONE" "\033[0m"
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

openJson () {   
    echo "Checking JSON file integrity...";

    if [ $(verifyJson $1) == 1 ];
    then
        echo "$(ERROR): not a JSON file.";
        echo; echo "Please choose a JSON file ('file.json'):";
        return 1
    elif [ $(verifyJson $JSONFILE) == 2 ];
    then 
        echo "$(ERROR): invalid JSON data.";
        echo; echo "Please choose a valid JSON file:";
        return 2
    else
        echo "JSON validation: $(OK)";
        return 0
    fi;
}

echo "Choose JSON file to minify:";
read -ei "$(echo $HOME)"/ JSONFILE;
openJson $JSONFILE
while [ $? != 0 ];
do
    read -ei "$(echo $JSONFILE)" JSONFILE;
    openJson $JSONFILE
done;

echo; echo "Save minified JSON file to:";
read -ei "$(echo $JSONFILE)" MINIFIEDJSON;

while [ $MINIFIEDJSON == $JSONFILE ]
do
    echo "$(ERROR): cannot overwrite source file '$JSONFILE'.";
    echo; echo "Please rename the minified file or save it to another folder:";
    read -ei "$(echo $MINIFIEDJSON)" MINIFIEDJSON;
done;

echo "Minifying JSON file..."
python3 $HOME/filtering/minifyJson.py $JSONFILE | cat > $MINIFIEDJSON;
echo "JSON minification: $(DONE)";
echo; echo "File saved to $MINIFIEDJSON";
exit 0;