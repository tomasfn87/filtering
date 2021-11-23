paintGreen () { gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;32m" text "\033[0m" }'
}

paintRed () { gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;31m" text "\033[0m" }'
}

paintBlue () { gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;34m" text "\033[0m" }'
}

paintYellow () { gawk -v text=$1 'BEGIN {
        printf "%s", "\033[1;33m" text "\033[0m" }'
}

echo $(paintGreen $1)
echo $(paintRed $1)
echo $(paintBlue $1)
echo $(paintYellow $1)