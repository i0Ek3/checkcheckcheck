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
    msg = "Auto update by GitHub Action"
    insert_info = "+++BEGIN+++\n\n## " + msg + "(" + "Update time: " + datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + ")" + "\n" + solidot + "\n+++END+++"
    filename = "news.md"

    with open (os.path.join(os.getcwd(), filename), 'r', encoding='utf-8') as f:
        news_content = f.read()

    new_content = re.sub(r'+++BEGIN+++(.|\n)*+++END+++', insert_info, news_content)

    with open (os.path.join(os.getcwd(), filename), 'w', encoding='utf-8') as f:
        f.write(new_content)

main()
