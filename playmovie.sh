#!/bin/bash

./movielist.py list | grep -i "$1" | sed 's/\t/\n/' | xargs -d '\n' dialog --menu "Select movie" 24 80 20 2> >(read ID; ./playmp4 "`./test.py "$ID"`")
