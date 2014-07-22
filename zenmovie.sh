#!/bin/bash

export PLAYER="mplayer -cache 1024 -cache-min 2" # 1MiB
#export PLAYER="wget -O download.mp4"

#./movielist.py list | grep -i "$1" | sed 's/\t/\n/' | xargs -d '\n' dialog --menu "Select movie" 24 80 20 2> >(read ID; ./playmp4 "`./test.py "$ID"`")
ID="`./movielist.py list | tail -n +2 | grep -i "$1" | sed 's/\t/\n/g' | zenity --width=800 --height=600 --list --title="Movies" --text="Vyber si film" --column=Id --column="IMDB rating" --column="Názov filmu" --hide-column=1 --print-column=1`" || exit 1

test -z "$ID" && exit 1

URL="$(wget -qO - "$(./test.py "$ID")" | sed -e 's/;url/;\nurl/g' -e 's/?/\n?/g' | grep 'url[0-9]\+=' | sort | uniq | tac | sed -re 's/^url([0-9]+)=/\1p /' | awk '{ print $2, $1; }' | sed 's/ /\n/g' | zenity --list --title="Movies" --text="Vyber si kvalitu" --column=URL --column=Kvalita --hide-column=1 --print-column=1)"

test -z "$URL" && exit 2

$PLAYER "$URL"
