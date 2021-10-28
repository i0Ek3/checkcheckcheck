#!/bin/bash

file="news.md"

checkfile() {
    if [ -e $file ]
    then
        rm $file
        git rm $file
        touch $file
    else
        touch $file
    fi
}

main() {
    # TODO: refactor
    echo "------------------------------------------------------------"
    git pull
    echo "------------------------------------------------------------"
    checkfile
    python3 main.py
    echo "------------------------------------------------------------"
    ls -alh
    echo "------------------------------------------------------------"
    cat $file
    echo "------------------------------------------------------------"
}

main
