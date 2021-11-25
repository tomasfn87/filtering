toGreen () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;32m" text "\033[0m" }'
}

toRed () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;31m" text "\033[0m" }'
}

toBlue () { gawk -v text=$1 'BEGIN {
    printf "%s", "\033[1;34m" text "\033[0m" }'
}

if [ $1 == $2 ]
then
    echo "$(toRed ERROR): cannot overwrite source file $(toBlue $2)";
    echo "Please rename the minified file or save it to another folder";
    exit 1
fi;

echo "Minifying file..."
python3 $HOME/filtering/minify.py $1 | cat > $2;
echo "$(toGreen DONE)". "File saved to $(toGreen $2)";
exit 0;
