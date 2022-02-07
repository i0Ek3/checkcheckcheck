#!/bin/bash

file="news.md"

checkfile() {
    if [ -e $file ]
    then
        rm $file
        git rm $file
    fi
    touch $file
}

showmsg() {
    # TODO: refactor
    echo "------------------------------------------------------------"
    git pull
    echo "------------------------------------------------------------"
    checkfile
    #python3 main.py
    python3 solidot.py
    echo "------------------------------------------------------------"
    ls -alh
    echo "------------------------------------------------------------"
    cat $file
    echo "------------------------------------------------------------"
}

cmpfile() {
    old="news_old.md"

    res=$(cmp --silent $old $file)
    if [ res ]
    then
        rm $old
    else
        archive
    fi
}

clean() {
    nums=`ls history | wc -l`
    if [ $nums -gt 56 ] # only one week
    then
        rm -rf ./history
        mkdir history
    fi
}

createmd() {
    if [ ! -e $file ]
    then
        touch $file
    fi
}

archive() {
    time=$(date "+%Y-%m-%d-%H-%M-%S")
    cp news.md news_$time.md
    mv news_* ./history
}

start() {
    git pull
    clean
    archive
    createmd

    #python3 main.py
    python3 solidot.py
}

installpkg() {
    pip3 install feedparser pytz
}

main() {
    installpkg
    start
}

main
