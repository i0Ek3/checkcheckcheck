#!/bin/bash

git pull
if [ -e news.md ]
then
    rm news.md
    git rm news.md
    touch news.md
else
    touch news.md
fi
python3 main.py

ls -alh
cat news.md
