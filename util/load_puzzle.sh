. ./util/.env

DAY=${1:-$(date '+%d')}
mkdir $DAY && touch $DAY/sample.txt && cp ./util/main.py $DAY/main.py
wget --header "Cookie: session=$AOC_SESSION_COOKIE" "https://adventofcode.com/2021/day/$DAY/input" -O $DAY/input.txt
