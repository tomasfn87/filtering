echo "JSON file to be minified:";
read -ei "$(echo $HOME)"/ JSONFILE; echo;

echo "Checking JSON file integrity...";

if [ $( python3 ./verifyJson.py $JSONFILE ) == 0 ]
then
    echo "ERROR: invalid JSON file. Exiting...";
    exit 1;
else
    echo "DONE.";
fi;

echo; echo "Save minified JSON file to:";
read -ei "$(echo $JSONFILE)" MINIFIEDJSON; echo;

while [ $MINIFIEDJSON == $JSONFILE ]
do
    echo "ERROR: cannot overwrite '$JSONFILE'.";
    echo; echo "Please rename the minified file or save it to another folder:";
    read -ei "$(echo $JSONFILE)" MINIFIEDJSON;
done;

python3 ./minifyJson.py $JSONFILE | cat > $MINIFIEDJSON;
echo; echo "Minified JSON saved to: ";
echo "'$MINIFIEDJSON'.";

exit 0
