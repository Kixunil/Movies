Movies
======

Simple scripts for playing or downloading movies. Thanks to majjacz for initial idea, reverse-engineering and proof of concept.

Dependencies: schema docopt requests (use pip install), for playmovie.sh also dialog, for zenmovie.sh zenity.

Usage
-----
./movielist.py update - updates database
./movielist.py list - prints database to stdout
./playmovie.sh [REGEX] - uses CLI dialog to choose movie, you may filter showed movies with REGEX (used by grep -E)
./zenmovie.sh [REGEX] - uses zenity to show nice GTK dialog; similar to playmovie.sh

To download, just change PLAYER to wget -O dstfile.mp4

Bugs
----
./playmovie doesn't allow choosing quality
Code is quite messy

Contributing
------------
Just make pull request. Any useful improvements are appreciated!

Contact
-------

Send questions to martin dot habovstiak at gmail dot com
