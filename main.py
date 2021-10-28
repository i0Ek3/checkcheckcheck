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

    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    timenow = "Update time: " + datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    msg = " Auto update by GitHub Actions."
    insert_info = "\n\n## " + timenow + msg + "\n" + solidot + "\n"

    filename = "news_" + str(datetime.now().strftime('%Y-%m-%d-%H-%M')) + ".md"
    with open (os.path.join(os.getcwd(), filename), 'w', encoding='utf-8') as f:
        f.write(insert_info)

main()
