#!/bin/bash

if [ -e news.md ]
then
    rm news.md
else
    touch news.md
fi
python3 main.py

ls -alh
cat news.md
git pull
