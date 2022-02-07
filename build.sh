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
    new="news.md"

    res=$(cmp --silent $old $new)
    if [ res ]
    then
        rm $old
    else
        mv $old news_$(date).md
        mv news_* history
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

start() {
    git pull
    cp news.md news_$(date).md
    mv news_* ./history
    clean
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
