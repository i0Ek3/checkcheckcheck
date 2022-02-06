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

showmsg() {
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

cmpfile() {
    old="news_old.md"
    new="news.md"

    res=$(cmp --silent $old $new)
    if res
    then
        rm $old
    else
        mv $old history
        cd history
        mv $old news_$(date).md
        cd -
    fi
}

clean() {
    nums=`ls history | wc -l`
    if [ nums -gt 56 ] # only one week
    then
        rm -rf ./history
    fi
    mkdir history
}

start() {
    git pull
    clean
    mv news* ./history
    python3 main.py
}

main() {
    pip3 install feedparser pytz
    start
    #cmpfile
}

main
