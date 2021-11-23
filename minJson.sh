toGreen () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;32m" text "\033[0m" }' 
}

toRed () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;31m" text "\033[0m" }'
}

toBlue () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;34m" text "\033[0m" }'
}

verifyJson () {
    echo $(python3 $HOME/filtering/verifyJson.py $1)
}

openJson () {   
    echo "Checking JSON file integrity...";

    if [ $(verifyJson $1) == 1 ];
    then
        echo "$(toRed ERROR): not a JSON file";
        echo; echo "Please choose a JSON file ('file.json'):";
        return 1
    elif [ $(verifyJson $JSONFILE) == 2 ];
    then 
        echo "$(toRed ERROR): invalid JSON data";
        echo; echo "Please choose a valid JSON file:";
        return 2
    else
        echo "JSON validation: $(toGreen OK)";
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
    echo "$(toRed ERROR): cannot overwrite source file $(toBlue $JSONFILE)";
    echo "Please rename the minified file or save it to another folder:";
    read -ei "$(echo $MINIFIEDJSON)" MINIFIEDJSON;
done;

echo "Minifying JSON file..."
python3 $HOME/filtering/minifyJson.py $JSONFILE | cat > $MINIFIEDJSON;
echo "JSON minification: $(toGreen DONE)";
echo; echo "File saved to $(toGreen $MINIFIEDJSON)";
exit 0;