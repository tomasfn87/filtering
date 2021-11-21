read -p "Read JSON file: " -e -i "$(echo $HOME)"/ JSONFILE;

read -p  "Save minified JSON file: " -e -i "$(echo $JSONFILE)" MINIFIEDJSON;

while [ $MINIFIEDJSON == $JSONFILE ]
do
    echo "ERROR: cannot overwrite $JSONFILE.";
    echo "Please rename your minified JSON file:";
    read -ei "$(echo $JSONFILE)" MINIFIEDJSON
done

python3 minifyJson.py $JSONFILE | cat > $MINIFIEDJSON;

echo Minified Json saved at $MINIFIEDJSON.
