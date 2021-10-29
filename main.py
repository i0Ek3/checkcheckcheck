import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def get_link_info(feed_url, num):
    result = ""
    feed = feedparser.parse(feed_url)
    feed_entries = feed["entries"]
    feed_entries_length = len(feed_entries)
    all_number = 0;

    if(num > feed_entries_length):
        all_number = feed_entries_length
    else:
        all_number = num

    for entrie in feed_entries[0: all_number]:
        title = entrie["title"]
        link = entrie["link"]
        result = result + "\n" + "[" + title + "](" + link + ")" + "\n"

    return result

def main():
    solidot = get_link_info("https://www.solidot.org/index.rss", 5)

    timenow1 = datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    timenow2 = datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d')

    msg = " Auto update by GitHub Action."
    insert_info = "\n\n## Update time: " + timenow1 + msg + "\n" + solidot + "\n"

    filename = "news_" + timenow2 + ".md"
    with open (os.path.join(os.getcwd(), filename), 'w', encoding='utf-8') as f:
        f.write(insert_info)

main()
